"""Stage 0 — RESOURCE BUNDLE ingestion (the pipeline's source of truth).

Each subject gets a drop folder `pipeline/resources/<subject>/`. Put any authoritative material
there — official spec, course summary, teacher's guide, worked questions, notes — as PDF or text.
This module pools it all into one text corpus that the rest of the pipeline treats as ground truth:

  - scaffold_gen.py  derives the topic list from it (not inferred from papers)
  - flashcards.py    sources concepts/definitions from it (not from past-paper question text)
  - model_answers.py grounds H1 answers in it (not the model's general knowledge)
  - config.cutoff_for reads the subject's current-syllabus year from it

The corpus + a small `<subject>.meta.json` (the derived cutoff) are cached under
`_data/resources/`. Re-ingest is cheap and idempotent unless the source files change.

    python3 resources.py home-economics          # ingest + print a summary
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

from config import RESOURCES, RESOURCE_CACHE, CURRENT_YEAR

try:
    import fitz  # PyMuPDF — same dep digest/extract already use
except ImportError:
    fitz = None

MAX_CORPUS_CHARS = 400_000         # cap the pooled corpus so model calls stay bounded
TEXT_SUFFIXES = {".txt", ".md", ".text"}

# Phrases that introduce the year a syllabus was first examined / revised.
_CUTOFF_RE = re.compile(
    r"(?:first examined|introduced|revised syllabus|new syllabus|current syllabus|"
    r"examined from|in effect from|specification\s+(?:introduced|from))[^\d]{0,40}(\b(?:19|20)\d{2}\b)",
    re.I)


def subject_dir(subject: str) -> Path:
    return RESOURCES / subject


def has_bundle(subject: str) -> bool:
    d = subject_dir(subject)
    return d.is_dir() and any(f.is_file() for f in d.rglob("*"))


def _files(subject: str) -> list[Path]:
    d = subject_dir(subject)
    if not d.is_dir():
        return []
    return sorted(f for f in d.rglob("*") if f.is_file() and not f.name.startswith("."))


def role_of(path: Path) -> str:
    """Light filename heuristic so callers can weight material. No manifest required."""
    n = path.name.lower()
    if n.startswith(("guide", "teacher")):
        return "guide"
    if n.startswith(("summary", "notes", "revision")):
        return "summary"
    if n.startswith(("spec", "syllabus", "curriculum")):
        return "spec"
    if "worked" in n or "questions" in n or "answers" in n:
        return "worked-questions"
    return "material"


def _read_file(path: Path) -> str:
    suf = path.suffix.lower()
    if suf == ".pdf":
        if fitz is None:
            return "[skipped PDF: install pymupdf]"
        try:
            doc = fitz.open(path)
            txt = "\n".join(p.get_text("text") for p in doc)
            doc.close()
            return txt
        except Exception as e:
            return f"[unreadable PDF: {e}]"
    if suf in TEXT_SUFFIXES:
        return path.read_text(errors="replace")
    if suf == ".docx":
        try:
            import docx  # python-docx, optional
            return "\n".join(p.text for p in docx.Document(str(path)).paragraphs)
        except Exception:
            return "[skipped .docx: pip install python-docx]"
    return ""                                          # unknown type — ignore


def extract_cutoff(text: str) -> int | None:
    """Best-effort: the syllabus introduction year stated in the material. None if not stated."""
    years = [int(m.group(1)) for m in _CUTOFF_RE.finditer(text)]
    years = [y for y in years if 1990 <= y <= CURRENT_YEAR]
    if not years:
        return None
    return min(years)                                  # the earliest stated intro year


def _corpus_path(subject: str) -> Path:
    return RESOURCE_CACHE / f"{subject}.corpus.txt"


def _meta_path(subject: str) -> Path:
    return RESOURCE_CACHE / f"{subject}.meta.json"


def ingest(subject: str, force: bool = False) -> dict:
    """Build (or reuse) the corpus + meta for a subject. Returns a summary dict."""
    files = _files(subject)
    summary = {"subject": subject, "files": len(files), "chars": 0,
               "cutoff": None, "roles": {}, "bundle": bool(files)}
    if not files:
        return summary

    # rebuild if any source file is newer than the cache (or force / missing)
    cpath, mpath = _corpus_path(subject), _meta_path(subject)
    newest = max(f.stat().st_mtime for f in files)
    if cpath.exists() and not force and cpath.stat().st_mtime >= newest:
        corpus = cpath.read_text()
    else:
        chunks = []
        for f in files:
            role = role_of(f)
            summary["roles"][role] = summary["roles"].get(role, 0) + 1
            body = _read_file(f).strip()
            if body:
                chunks.append(f"\n\n===== {role.upper()}: {f.relative_to(subject_dir(subject))} =====\n{body}")
        corpus = "".join(chunks)[:MAX_CORPUS_CHARS]
        cpath.write_text(corpus)

    cutoff = extract_cutoff(corpus)
    summary["chars"] = len(corpus)
    summary["cutoff"] = cutoff
    if not summary["roles"]:                            # populate roles when reusing cached corpus
        for f in files:
            r = role_of(f); summary["roles"][r] = summary["roles"].get(r, 0) + 1
    mpath.write_text(json.dumps({"subject": subject, "cutoff": cutoff,
                                 "files": len(files)}, indent=2))
    return summary


def corpus(subject: str) -> str:
    """The pooled resource text for a subject ('' if no bundle). Ingests on demand."""
    if _corpus_path(subject).exists():
        return _corpus_path(subject).read_text()
    ingest(subject)
    p = _corpus_path(subject)
    return p.read_text() if p.exists() else ""


if __name__ == "__main__":
    subj = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 resources.py <subject> [--force]")
    s = ingest(subj, force=("--force" in sys.argv))
    if not s["bundle"]:
        print(f"No resource bundle at {subject_dir(subj)} — create it and drop files in.")
    else:
        print(f"[resources] {subj}: {s['files']} file(s) {s['roles']}, {s['chars']} chars, "
              f"cutoff {s['cutoff'] or '(not stated — will fall back to estimate)'}")
