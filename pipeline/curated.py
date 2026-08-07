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
CURATED_QUESTION_FILES = ["exam-questions-db.js"]

_QUESTION_RE = re.compile(r"""question\s*:\s*(['"])(.*?)\1""", re.S)
_SIG_LEN = 120


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def signature(text: str) -> str:
    return _norm(text)[:_SIG_LEN]


def curated_question_sigs() -> set[str]:
    """Normalised signatures of every curated question (across subjects — text is distinctive)."""
    sigs: set[str] = set()
    for name in CURATED_QUESTION_FILES:
        p = ROOT / name
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
    """True if this generated question matches a curated one (any part's text signature hits)."""
    if not sigs:
        return False
    for p in q.get("parts", []):
        if signature(p.get("question", "")) in sigs:
            return True
    return False


def drop_duplicates(canonical: list[dict]) -> tuple[list[dict], int]:
    """Return (kept, dropped_count) — generated questions that duplicate curated ones removed."""
    sigs = curated_question_sigs()
    if not sigs:
        return canonical, 0
    kept = [q for q in canonical if not is_duplicate(q, sigs)]
    return kept, len(canonical) - len(kept)
