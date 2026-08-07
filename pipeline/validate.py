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

The second half of this module (from "THE GATE" below) is the reform's stage-level gate —
`post_segment` and `enforce` — which builds on these pure checks with its own defect taxonomy,
retry bookkeeping, quarantine, and the auto-publish-if-clean thresholds run.py reads.
"""
from __future__ import annotations
import json
import random
import re
import sys
from functools import lru_cache

from config import (CANONICAL, REPORTS, MIN_QUESTION_CHARS, STUB_QUESTION_RE,
                    LENGTH_MIN_RATIO, LENGTH_MAX_RATIO, SEGMENT_RETRY_ATTEMPTS,
                    MAX_QUARANTINE_FRAC, MAX_SOFT_WARN_FRAC, TAG_REVIEW_THRESHOLD,
                    recommended_words, writable_words)

# How far past the time budget an answer may run before it's flagged as unwritable. Word counts
# and handwriting speed are both approximations, so a small overshoot isn't worth a warning.
OVER_TIME_TOLERANCE = 1.15

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

# ══════════════════════════════════════════════════════════════════════════════
# THE GATE (reform C/D/G) — keep broken records out of the app.
#
# The old pipeline merged whatever the model emitted: ~20% of home-economics questions were
# empty stubs ("Part (a)"), many had marks of 0, and answers were written against those stubs.
# Nothing caught it. This is the safety net, used at two points by run.py:

# 1. AFTER segment (`post_segment`): scan the freshly extracted questions. If any are broken
#    (stub question text, or marks of 0), re-segment just those papers with the strong model —
#    up to SEGMENT_RETRY_ATTEMPTS times. When the budget is spent, the irrecoverable *stub*
#    parts are quarantined so downstream stages never waste effort on them.
#
# 2. BEFORE merge (`enforce`): a hard gate. Any remaining stub parts are dropped to
#    `_data/canonical/<subject>.quarantine.json`, the app JS is re-rendered from the clean set,
#    and a human-readable sample + report are written. run.py will not merge unless `--merge`
#    is passed, so a bad run can't silently reach the live app.
#
# Defect taxonomy:
#   HARD  stub_question   — question text missing or only a label; unusable -> dropped at the gate
#   SOFT  no_marks        — marks <= 0; answer can't be sized -> triggers a retry, surfaced, kept
#   SOFT  length_mismatch — answer far from its mark-derived target -> surfaced (warning only)
#   SOFT  not_writable_in_time — answer longer than a student could write in the time allowed
#
#     python3 validate.py home-economics            # scan + write the report/sample (no changes)
#     python3 validate.py home-economics --enforce  # drop stubs to quarantine, re-render, sample
# ══════════════════════════════════════════════════════════════════════════════

LOW_TAG_CONF = 0.6              # below this a question's chapter tag is "low confidence"


def _load(subject: str) -> list[dict]:
    return json.loads((CANONICAL / f"{subject}.json").read_text())


def _save(subject: str, rows: list[dict]) -> None:
    (CANONICAL / f"{subject}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))


def _paper_key(q: dict) -> str:
    # Imported lazily: model_answers imports this module at load time, so a module-level
    # `from model_answers import q_level` would be a circular import.
    from model_answers import q_level
    return f"{q.get('year')}-{q_level(q)}"


# ── defect detection ──────────────────────────────────────────────────────────
def is_stub(p: dict) -> bool:
    """True if the part's question text is missing or only a label like 'Part (a)'."""
    t = (p.get("question") or "").strip()
    return len(t) < MIN_QUESTION_CHARS or bool(STUB_QUESTION_RE.match(t))


def _word_count(s: str) -> int:
    return len(re.findall(r"\b\w+\b", s or ""))


def part_defects(subject: str, p: dict) -> list[str]:
    """All defects on a part. 'stub_question' is HARD; the rest are SOFT (kept, but surfaced)."""
    out = []
    if is_stub(p):
        out.append("stub_question")
    if not isinstance(p.get("marks"), int) or p.get("marks", 0) <= 0:
        out.append("no_marks")
    target = recommended_words(subject, p.get("marks", 0), p.get("scheme_points"))
    ans = (p.get("model") or "").strip()
    words = _word_count(ans) if ans else 0
    if target and ans:
        ratio = words / target
        if ratio < LENGTH_MIN_RATIO or ratio > LENGTH_MAX_RATIO:
            out.append("length_mismatch")
    # A model answer has to be one a student could actually produce in the time the exam gives
    # them. `recommended_words` already caps the target at WRITING_WPM, so this catches an author
    # that overshot the stated budget anyway — the exemplar is unusable as a model if it can't
    # be written in the time, however good the content is.
    if ans:
        writable = writable_words(p.get("time_minutes"))
        if writable and words > writable * OVER_TIME_TOLERANCE:
            out.append("not_writable_in_time")
    return out


HARD = {"stub_question"}


def scan(subject: str) -> dict:
    """Tally defects without modifying anything. Returns counts, the offending paper keys, and
    a few examples per defect for the report."""
    canonical = _load(subject)
    parts = [(q, i, p) for q in canonical for i, p in enumerate(q["parts"])]
    by_defect: dict[str, list] = {}
    bad_paper_keys: set[str] = set()
    hard = soft = 0
    for q, i, p in parts:
        defs = part_defects(subject, p)
        if not defs:
            continue
        bad_paper_keys.add(_paper_key(q))
        if HARD & set(defs):
            hard += 1
        else:
            soft += 1
        for d in defs:
            by_defect.setdefault(d, []).append({
                "qid": q["id"], "label": p.get("label", ""), "marks": p.get("marks", 0),
                "question": (p.get("question") or "")[:80]})
    return {"n_parts": len(parts), "hard": hard, "soft": soft,
            "n_bad_parts": hard + soft, "bad_paper_keys": sorted(bad_paper_keys),
            "by_defect": {k: v for k, v in by_defect.items()}}


# ── retry bookkeeping ───────────────────────────────────────────────────────────
def _attempts_path(subject: str):
    return REPORTS / f"segment-{subject}.attempts"


def _read_attempts(subject: str) -> int:
    p = _attempts_path(subject)
    return int(p.read_text().strip()) if p.exists() else 0


def _bump_attempts(subject: str) -> None:
    _attempts_path(subject).write_text(str(_read_attempts(subject) + 1))


def _reset_attempts(subject: str) -> None:
    p = _attempts_path(subject)
    if p.exists():
        p.unlink()
    _baseline_path(subject).unlink(missing_ok=True)


# ── gate baseline ───────────────────────────────────────────────────────────────
# `clean()` rewrites canonical without the stub parts it quarantined. That makes enforce()
# destructive: a second enforce() measures the set the first one already sanitised, so a run
# that quarantined 20% reports 0% the next time and auto-publishes. The gate has to judge the
# WHOLE run, so the pre-clean total and the cumulative drops are persisted here and only reset
# by --restart (via _reset_attempts).
def _baseline_path(subject: str):
    return REPORTS / f"gate-baseline-{subject}.json"


def _load_baseline(subject: str) -> dict | None:
    p = _baseline_path(subject)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def _save_baseline(subject: str, data: dict) -> None:
    _baseline_path(subject).write_text(json.dumps(data, indent=2))


def _drop_papers(subject: str, keys) -> int:
    """Remove every question belonging to the given paper keys from canonical (so segment
    re-queues those whole papers). Returns the number of questions removed."""
    keys = set(keys)
    canonical = _load(subject)
    keep = [q for q in canonical if _paper_key(q) not in keys]
    _save(subject, keep)
    return len(canonical) - len(keep)


# ── the two run.py entry points ─────────────────────────────────────────────────
def post_segment(subject: str, limit: int | None = None) -> str:
    """After a segment collect. Returns 'ok' | 'retry' | 'cleaned'.
    'retry' means offending papers were re-queued — run.py should spawn the worker again."""
    rep = scan(subject)
    if rep["n_bad_parts"] == 0:
        _reset_attempts(subject)
        print("[validate] segment clean — no stub/zero-mark parts")
        return "ok"
    attempts = _read_attempts(subject)
    if attempts < SEGMENT_RETRY_ATTEMPTS:
        import agent_bridge as bridge
        import segment
        keys = rep["bad_paper_keys"]
        dropped = _drop_papers(subject, keys)
        bridge.reset(segment._stage(subject))
        _bump_attempts(subject)
        segment.prepare(subject, limit=limit)     # re-queues exactly the dropped papers
        print(f"[validate] {rep['hard']} stub + {rep['soft']} weak part(s) across "
              f"{len(keys)} paper(s); re-segmenting them "
              f"(attempt {attempts + 1}/{SEGMENT_RETRY_ATTEMPTS}, {dropped} questions re-queued)")
        return "retry"
    _reset_attempts(subject)
    creport = clean(subject)
    print(f"[validate] retry budget spent; quarantined {creport['dropped_parts']} stub part(s) / "
          f"{creport['dropped_questions']} question(s). {rep['soft']} weak part(s) kept & flagged.")
    return "cleaned"


def clean(subject: str) -> dict:
    """Drop HARD-defective (stub) parts to a quarantine file; rewrite canonical clean; re-render."""
    import segment
    canonical = _load(subject)
    kept, quarantined, dropped_parts = [], [], 0
    for q in canonical:
        good = [p for p in q["parts"] if not (HARD & set(part_defects(subject, p)))]
        bad = [p for p in q["parts"] if HARD & set(part_defects(subject, p))]
        dropped_parts += len(bad)
        if bad:
            quarantined.append({"id": q["id"], "dropped": bad})
        if good:
            q["parts"] = good
            kept.append(q)
        # a question with no good parts is dropped entirely
    dropped_questions = len(canonical) - len(kept)
    _save(subject, kept)
    qpath = CANONICAL / f"{subject}.quarantine.json"
    if quarantined:
        qpath.write_text(json.dumps(quarantined, ensure_ascii=False, indent=2))
    segment.render_js(subject, kept)
    return {"dropped_parts": dropped_parts, "dropped_questions": dropped_questions,
            "kept_questions": len(kept), "quarantine": str(qpath) if quarantined else None}


# ── report + human sample (reform G) ────────────────────────────────────────────
def write_report(subject: str) -> str:
    rep = scan(subject)
    path = REPORTS / f"validate-{subject}.json"
    path.write_text(json.dumps(rep, indent=2, ensure_ascii=False))
    return str(path)


def write_sample(subject: str, n_q: int = 12, n_cards: int = 15, seed: int = 0) -> str:
    """Write a markdown sample of questions+answers (and flashcards if present) for a human
    eyeball before publishing. Spreads the question sample across chapters."""
    canonical = _load(subject)
    rnd = random.Random(seed)
    by_ch: dict[str, list] = {}
    for q in canonical:
        by_ch.setdefault(q.get("chapterId", "?"), []).append(q)
    chosen, chapters = [], list(by_ch)
    rnd.shuffle(chapters)
    while len(chosen) < min(n_q, len(canonical)) and chapters:
        for ch in list(chapters):
            bucket = by_ch[ch]
            if bucket:
                chosen.append(bucket.pop(rnd.randrange(len(bucket))))
            else:
                chapters.remove(ch)
            if len(chosen) >= n_q:
                break

    lines = [f"# Sample review — {subject}", "",
             f"{len(canonical)} questions in canonical. Spot-check these before publishing.", ""]
    for q in chosen:
        lines.append(f"## {q['id']}  ·  chapter `{q.get('chapterId','?')}`  ·  {q.get('source','')}")
        for p in q["parts"]:
            src = p.get("model_source", "—")
            tgt = recommended_words(subject, p.get("marks", 0), p.get("scheme_points"))
            tgtxt = f", target ~{tgt}w, got {_word_count(p.get('model',''))}w" if tgt else ""
            lines.append(f"**[{p.get('label','')}] ({p.get('marks',0)} marks)** {p.get('question','')}")
            lines.append(f"> _({src}{tgtxt})_ {(p.get('model') or '(no answer)')}")
            lines.append("")

    fc = CANONICAL / f"flashcards.{subject}.json"
    if fc.exists():
        cards = [(cid, c) for cid, cs in json.loads(fc.read_text()).items() for c in cs]
        rnd.shuffle(cards)
        lines += ["", "## Flashcard sample", ""]
        for cid, c in cards[:n_cards]:
            lines.append(f"- **{c.get('term','')}** — {c.get('definition','')}  `({cid})`")

    path = REPORTS / f"sample-{subject}.md"
    path.write_text("\n".join(lines))
    return str(path)


def tag_review(subject: str) -> dict:
    """Best-guess tags stay (they're usable), but if MORE than TAG_REVIEW_THRESHOLD questions are
    low-confidence, collect them into a review bucket so the scaffold/tagging can be fixed."""
    canonical = _load(subject)
    low = [{"id": q["id"], "chapterId": q.get("chapterId", ""),
            "tag_confidence": q.get("tag_confidence", 0),
            "first_q": (q["parts"][0]["question"][:100] if q.get("parts") else "")}
           for q in canonical if q.get("tag_confidence", 1) < LOW_TAG_CONF]
    path = None
    if len(low) > TAG_REVIEW_THRESHOLD:
        p = REPORTS / f"tag-review-{subject}.json"
        p.write_text(json.dumps(low, indent=2, ensure_ascii=False))
        path = str(p)
    return {"low_confidence": len(low), "tag_review": path}


def enforce(subject: str) -> dict:
    """Pre-merge hard gate. Drops stub parts AND generated questions that duplicate curated ones
    (curated wins), raises a tag-review bucket if needed, writes quarantine/report/sample, and
    decides whether the run is clean enough to auto-publish."""
    import curated
    import segment
    # Judge the whole run, not just what survives this invocation — see _baseline_path above.
    base = _load_baseline(subject)
    before = base["before"] if base else len(_load(subject))
    prior_dropped_q = base["dropped_questions"] if base else 0
    prior_dropped_p = base["dropped_parts"] if base else 0

    creport = clean(subject)                          # drop stub parts/questions -> quarantine
    creport["dropped_questions"] += prior_dropped_q   # cumulative across re-runs
    creport["dropped_parts"] += prior_dropped_p
    _save_baseline(subject, {"before": before,
                             "dropped_questions": creport["dropped_questions"],
                             "dropped_parts": creport["dropped_parts"]})

    # curated wins: drop generated questions duplicating the hand-curated bank, then re-render
    kept, dup_dropped = curated.drop_duplicates(_load(subject))
    # Stamp the "how long should this take" label. This is the single choke point every publish
    # passes through, so doing it here is what guarantees the labels exist on the records the app
    # actually loads. Recomputed from marks each run, so it self-corrects; the store is rewritten
    # unconditionally because that is also what re-renders the JS after the dedup above.
    import timing
    tstat = timing.stamp(subject, kept)
    _save(subject, kept)
    segment.render_js(subject, kept)
    creport["kept_questions"] = len(kept)            # reflect post-dedup final count

    rep = scan(subject)                              # re-scan the cleaned set (soft defects remain)
    tr = tag_review(subject)
    report_path = write_report(subject)
    sample_path = write_sample(subject)

    total = max(1, before)
    parts = max(1, rep["n_parts"])
    quarantine_frac = creport["dropped_questions"] / total
    soft_frac = rep["soft"] / parts
    is_clean = (quarantine_frac <= MAX_QUARANTINE_FRAC
                and soft_frac <= MAX_SOFT_WARN_FRAC
                and not tr["tag_review"])
    return {**creport, "dup_dropped": dup_dropped, "remaining_soft": rep["soft"],
            "quarantine_frac": round(quarantine_frac, 3), "soft_frac": round(soft_frac, 3),
            "low_confidence": tr["low_confidence"], "tag_review": tr["tag_review"],
            "timed_parts": tstat["stamped"], "untimed_parts": tstat["missing"],
            "clean": is_clean, "report": report_path, "sample": sample_path}


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    if "--enforce" in args:
        print(json.dumps(enforce(subject), indent=2))
    else:
        rep = scan(subject)
        print(json.dumps(rep, indent=2)[:2000])
        print("report:", write_report(subject))
        print("sample:", write_sample(subject))
