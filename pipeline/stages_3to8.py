"""Stages 3–8 — typed stubs with the contract each must satisfy.

These are deliberately not implemented end-to-end: stages 3, 5 and 6 need an LLM/embedding
call, and the exact prompts are where you'll iterate most. Each function below states its
input, output, and the one hard decision it owns. Implement them against the canonical
record shape defined here so the LOAD stage (stage 7) stays a dumb renderer.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
import json
from pathlib import Path

from config import EXTRACTED, CANONICAL, EXAM_DB_OUT, EXAM_IMAGES


# ── Canonical record — the single shape everything converges on ───────────────
@dataclass
class Part:
    label: str
    question: str
    marks: int = 0
    model: str = ""            # cleaned marking-scheme answer (stage 6)
    diagram: str = ""          # exam-images/<subject>/... (stage 3 crop)


@dataclass
class Question:
    id: str
    subject: str
    year: int
    source: str
    chapterId: str = ""        # filled by stage 5
    sectionId: str = ""        # filled by stage 5
    tag_confidence: float = 0.0
    parts: list[Part] = field(default_factory=list)
    keyTerms: list[dict] = field(default_factory=list)   # stage 6: {term,definition,section}


# ── Stage 3 — SEGMENT ─────────────────────────────────────────────────────────
def segment(doc_json: dict) -> list[Question]:
    """pages[] -> Question[] with parts. Owns: where one question ends and the next begins.
    Regex the obvious markers (Section A/B/C, Qn, (a)/(i), '(N marks)'); send messy pages
    to an LLM. Crop diagram regions to EXAM_IMAGES and set Part.diagram. TODO."""
    raise NotImplementedError


# ── Stage 4 — PAIR ────────────────────────────────────────────────────────────
def pair_marking_scheme(questions: list[Question], scheme_json: dict) -> None:
    """Align on (year, level, paper, question, part); write raw scheme text into Part.model.
    Mostly deterministic on numbering; LLM only for ambiguous cases. Mutates in place. TODO."""
    raise NotImplementedError


# ── Stage 5 — TAG ─────────────────────────────────────────────────────────────
def tag_topics(questions: list[Question], syllabus_los: list[dict]) -> None:
    """Embed question + every LO, take top-k by cosine, let an LLM pick chapterId/sectionId
    from those candidates; record tag_confidence. Low confidence -> review queue (stage 8).
    Owns the 'by topic' decision — Examly's real moat. TODO."""
    raise NotImplementedError


# ── Stage 6 — DERIVE ──────────────────────────────────────────────────────────
def derive_flashcards(questions: list[Question]) -> None:
    """Turn each marking point into a keyTerm {term,definition,section}; optionally clean
    Part.model into a readable answer while keeping raw text. Mutates in place. TODO."""
    raise NotImplementedError


# ── Stage 7 — LOAD (renders canonical -> bare bones files; no judgement here) ──
def load_to_app(subject: str) -> None:
    canon = CANONICAL / f"{subject}.json"
    questions = [Question(**q) for q in json.loads(canon.read_text())]
    db = [{
        "id": q.id, "subject": q.subject, "chapterId": q.chapterId,
        "sectionId": q.sectionId, "source": q.source, "year": q.year,
        "parts": [asdict(Part(**p)) if isinstance(p, dict) else asdict(p) for p in q.parts],
    } for q in questions]
    js = ("window.EXAM_QUESTIONS_DB = (window.EXAM_QUESTIONS_DB || []).concat(\n"
          + json.dumps(db, indent=2, ensure_ascii=False) + "\n);\n")
    out = EXAM_DB_OUT.with_name(f"exam-questions-db.{subject}.generated.js")
    out.write_text(js)
    print(f"[load] {out.name}  ({len(db)} questions)  — diff against exam-questions-db.js")


# ── Stage 8 — QA ──────────────────────────────────────────────────────────────
def qa(subject: str, min_confidence: float = 0.6) -> dict:
    """Validate required fields, dedupe on (subject,year,paper,q), build coverage-by-chapter
    and a review queue of tag_confidence < min_confidence. Returns a report dict. TODO."""
    raise NotImplementedError


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "load":
        load_to_app(sys.argv[2])
    else:
        print("Stages 3–8 are stubs. Implement segment/pair/tag/derive, then:")
        print("  python stages_3to8.py load <subject>")
