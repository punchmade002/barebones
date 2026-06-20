"""Content validation — the keystone the re-queue, coverage, and merge gate hang off.

A job/file existing is NOT proof its content is good. Before this module the pipeline happily
published placeholder questions ("Part (a)"), empty answers, generic AI answers written onto an
empty question stub, and questions attributed to years no paper was ever acquired for. These pure
functions catch all of that and are import-safe from any stage (only `year_is_real` touches disk).

Two granularities matter, because the same part means different things at different stages:

  * EXTRACTION problems (placeholder/too-short question, an ai-h1 answer to nothing) mean the
    *segmentation* failed — the part is junk no matter what. These are fatal at segment time and
    drive the re-queue (see `extraction_problems` / `validate_output`).

  * A missing `model` answer ("empty-answer") is NORMAL at segment time — it's exactly what
    model_answers.py exists to fill later. So it is NOT an extraction failure; it only counts as a
    real problem at the *merge gate*, by which point every part should have an answer.

`part_problems` returns the full set (used by the merge gate). `extraction_problems` returns only
the fatal-at-segment subset.
"""
from __future__ import annotations
import re
from functools import lru_cache

# Questions that are really just structural chrome the segmenter failed to strip / fill.
PLACEHOLDER = re.compile(
    r'^\s*(Part \([a-z]+\)|Question \d+|Extended response question on|'
    r'Elective \d|\(a\) and either|\(?[ivx]+\)?)\s*$', re.I)

# Problems that mean the extraction itself failed (vs. an answer simply not being in the marking
# scheme yet, which is normal at segment time and is what model_answers.py later fills in).
EXTRACTION_PROBLEMS = frozenset({"placeholder-question", "question-too-short", "answer-to-nothing"})


def is_placeholder(part: dict) -> bool:
    q = (part.get("question") or "").strip()
    return not q or bool(PLACEHOLDER.match(q))


def part_problems(part: dict, scheme_text: str = "") -> list[str]:
    """Every problem with a single part. `scheme_text` is accepted for future scheme-aware checks
    but unused today. Includes 'empty-answer', which is only a *real* problem at the merge gate."""
    probs = []
    q = (part.get("question") or "").strip()
    if not q or PLACEHOLDER.match(q):
        probs.append("placeholder-question")
    elif len(q) < 12:                                       # already-flagged empties don't double up
        probs.append("question-too-short")
    if not (part.get("model") or "").strip():
        probs.append("empty-answer")
    if part.get("model_source") == "ai-h1" and is_placeholder(part):
        probs.append("answer-to-nothing")                  # generic answer manufactured for no question
    return probs


def extraction_problems(part: dict) -> list[str]:
    """Only the problems that mean segmentation failed — safe to use as a drop/re-queue trigger
    without nuking parts that simply await a model answer."""
    return [p for p in part_problems(part) if p in EXTRACTION_PROBLEMS]


def validate_output(obj) -> bool:
    """pending()'s callback for the SEGMENT stage. `obj` is the worker's raw answer object,
    shaped {"questions": [{"parts": [...]}, ...]}. Re-queue the whole paper if more than 10% of
    its parts are extraction failures. Empty answers are deliberately NOT counted here."""
    qs = obj.get("questions", []) if isinstance(obj, dict) else []
    if not qs:
        return False
    parts = [p for x in qs if isinstance(x, dict) for p in x.get("parts", []) if isinstance(p, dict)]
    total = len(parts)
    if total == 0:
        return False
    bad = sum(1 for p in parts if extraction_problems(p))
    return bad / total <= 0.10                              # tolerate ≤10% before the paper re-queues


def scan_canonical(canon: list[dict]) -> list[dict]:
    """Audit a whole canonical store. Returns [{id, label, problems}] for every bad part — the
    exact list of junk to purge or re-run. Uses the full part_problems (incl. empty-answer)."""
    out = []
    for q in canon:
        for p in q.get("parts", []):
            probs = part_problems(p)
            if probs:
                out.append({"id": q.get("id"), "label": p.get("label", ""), "problems": probs})
    return out


@lru_cache(maxsize=None)
def _acquired_years(subject: str) -> frozenset[int]:
    """Years for which a real paper was actually acquired — read from the digested papers and the
    downloaded PDFs on disk. Cached per subject for the life of the process."""
    from config import RAW, DIGEST
    years: set[int] = set()
    dd = DIGEST / subject
    if dd.exists():
        for f in dd.glob("*.json"):
            if f.name == "_index.json":
                continue
            m = re.match(r"(\d{4})", f.name)
            if m:
                years.add(int(m.group(1)))
    # RAW dir names have been inconsistent (e.g. "home economics" vs "home-economics"); check both.
    for cand in {subject, subject.replace("-", " "), subject.replace(" ", "-")}:
        rd = RAW / cand
        if rd.exists():
            for f in rd.glob("*papers*.pdf"):
                m = re.match(r"(\d{4})", f.name)
                if m:
                    years.add(int(m.group(1)))
    return frozenset(years)


def year_is_real(subject: str, year) -> bool:
    """True if a paper was genuinely acquired for this subject+year. Kills fabricated years
    (questions attributed to a year no PDF/digest exists for)."""
    try:
        return int(year) in _acquired_years(subject)
    except (TypeError, ValueError):
        return False
