"""Curated content guard (reform: curated wins, generated fills gaps).

The app has hand-curated exam questions in `exam-questions-db.js` (never written by the pipeline —
merge.py only ever writes the additive `<subject>-exam-questions.js` / `<subject>-flashcards.js`).
This module lets the pipeline drop any GENERATED question that duplicates a curated one, so the
generated bank only ever fills gaps.

Curated question files use unquoted JS keys (not JSON), so we don't parse the object graph — we
extract question text by a tolerant regex and dedup on a normalised text SIGNATURE. Question
wording is highly distinctive, so a signature match means the same question (no cross-subject
false positives in practice). If the curated file is missing/unreadable, dedup is a safe no-op.
"""
from __future__ import annotations
import re

from config import ROOT

# Hand-curated sources that must win. Pipeline output (-exam-questions.js / -flashcards.js) is
# deliberately NOT listed — we never dedup generated content against our own previous output.
# The *-content.js packs carry curated questions too (bio-content.js alone has 115); listing only
# exam-questions-db.js left ~160 curated questions invisible, so generated duplicates of them
# published straight through.
CURATED_QUESTION_FILES = ["exam-questions-db.js"]
CURATED_QUESTION_GLOBS = ["*-content.js"]

_QUESTION_RE = re.compile(r"""question\s*:\s*(['"])(.*?)\1""", re.S)
_SIG_LEN = 120


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def signature(text: str) -> str:
    return _norm(text)[:_SIG_LEN]


def _curated_paths() -> list:
    paths = [ROOT / n for n in CURATED_QUESTION_FILES]
    for pat in CURATED_QUESTION_GLOBS:
        paths.extend(sorted(ROOT.glob(pat)))
    seen, out = set(), []
    for p in paths:                                    # de-dup, keep order
        if p.name not in seen:
            seen.add(p.name)
            out.append(p)
    return out


def curated_question_sigs() -> set[str]:
    """Normalised signatures of every curated question (across subjects — text is distinctive)."""
    sigs: set[str] = set()
    for p in _curated_paths():
        if not p.exists():
            continue
        try:
            text = p.read_text()
        except Exception:
            continue
        for m in _QUESTION_RE.finditer(text):
            sig = signature(m.group(2))
            if len(sig) >= 12:
                sigs.add(sig)
    return sigs


def is_duplicate(q: dict, sigs: set[str]) -> bool:
    """True if EVERY part of this generated question matches a curated one — i.e. the whole
    question is already covered. A single matching part is not enough: exam questions share long
    boilerplate stems (the Geography OS-map preamble is identical across years), so matching on
    any-part would discard the unique parts (b)/(c) riding behind a shared part (a)."""
    if not sigs:
        return False
    parts = q.get("parts", [])
    if not parts:
        return False
    return all(signature(p.get("question", "")) in sigs for p in parts)


def drop_duplicate_parts(q: dict, sigs: set[str]) -> int:
    """Remove the individual parts already covered by curated content. Returns how many went."""
    parts = q.get("parts", [])
    keep = [p for p in parts if signature(p.get("question", "")) not in sigs]
    dropped = len(parts) - len(keep)
    if dropped:
        q["parts"] = keep
    return dropped


def drop_duplicates(canonical: list[dict]) -> tuple[list[dict], int]:
    """Return (kept, dropped_question_count). Questions wholly covered by curated content are
    removed; a partially-overlapping question keeps only its non-duplicate parts."""
    sigs = curated_question_sigs()
    if not sigs:
        return canonical, 0
    kept = []
    for q in canonical:
        if is_duplicate(q, sigs):
            continue                                   # fully covered by curated — curated wins
        drop_duplicate_parts(q, sigs)                  # trim the parts curated already covers
        if q.get("parts"):
            kept.append(q)
    return kept, len(canonical) - len(kept)
