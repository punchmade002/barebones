"""Stage 0 — RESOURCE BUNDLE ingestion (the pipeline's source of truth).

Each subject gets a contract folder `pipeline/resources/<subject>/`. Every folder must contain
the same four files: `manifest.json`, `spec-syllabus.pdf`, `guide-simplestudy.md`, and
`worked-example-guidance.md`.
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
REQUIRED_FILES = (
    "manifest.json",
    "spec-syllabus.pdf",
    "guide-simplestudy.md",
    "worked-example-guidance.md",
)
REQUIRED_MANIFEST_KEYS = (
    "schemaVersion",
    "subject",
    "level",
    "sources",
    "unitCount",
    "topicCount",
    "alignmentStatus",
)

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
    if n == "manifest.json":
        return "manifest"
    if n.startswith(("guide", "teacher")):
        return "guide"
    if n.startswith(("summary", "notes", "revision")):
        return "summary"
    if n.startswith(("spec", "syllabus", "curriculum")):
        return "spec"
    if "worked" in n or "questions" in n or "answers" in n:
        return "worked-questions"
    return "material"


def validate_bundle(subject: str) -> list[str]:
    """Return actionable contract errors. An empty list means the bundle is pipeline-ready."""
    d = subject_dir(subject)
    if not d.is_dir():
        return [f"missing directory: {d}"]
    errors = [f"missing required file: {name}" for name in REQUIRED_FILES if not (d / name).is_file()]
    manifest_path = d / "manifest.json"
    if not manifest_path.is_file():
        return errors
    try:
        manifest = json.loads(manifest_path.read_text())
    except Exception as exc:
        return [*errors, f"manifest.json is invalid JSON: {exc}"]
    for key in REQUIRED_MANIFEST_KEYS:
        if key not in manifest:
            errors.append(f"manifest.json missing key: {key}")
    if manifest.get("schemaVersion") != 1:
        errors.append("manifest.json schemaVersion must be 1")
    if manifest.get("subject") != subject:
        errors.append(f"manifest subject must be '{subject}'")
    if manifest.get("level") != "Higher":
        errors.append("manifest level must be 'Higher'")
    sources = manifest.get("sources") or {}
    if (sources.get("research") or {}).get("provider") != "SimpleStudy":
        errors.append("research provider must be SimpleStudy")
    if (sources.get("syllabus") or {}).get("authority") != "NCCA":
        errors.append("syllabus authority must be NCCA")
    first_exam_year = (sources.get("syllabus") or {}).get("firstExamYear")
    if not isinstance(first_exam_year, int) or not 1990 <= first_exam_year <= CURRENT_YEAR + 5:
        errors.append("syllabus firstExamYear must be a plausible integer")
    if manifest.get("alignmentStatus") not in {"aligned", "transitional"}:
        errors.append("alignmentStatus must be 'aligned' or 'transitional'")
    if not isinstance(manifest.get("unitCount"), int) or manifest.get("unitCount", 0) < 1:
        errors.append("unitCount must be a positive integer")
    if not isinstance(manifest.get("topicCount"), int) or manifest.get("topicCount", 0) < 1:
        errors.append("topicCount must be a positive integer")
    for filename, headings in {
        "guide-simplestudy.md": ("## Source", "## Unit and topic structure", "## Pipeline guidance"),
        "worked-example-guidance.md": ("## Source pattern", "## Required answer shape", "## Original model"),
    }.items():
        path = d / filename
        if path.is_file():
            text = path.read_text(errors="replace")
            for heading in headings:
                if heading not in text:
                    errors.append(f"{filename} missing section: {heading}")
    return errors


def require_bundle(subject: str) -> None:
    errors = validate_bundle(subject)
    if errors:
        detail = "\n".join(f"  - {error}" for error in errors)
        raise SystemExit(f"Resource bundle for '{subject}' does not meet the contract:\n{detail}")


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
    if suf == ".json":
        try:
            return json.dumps(json.loads(path.read_text()), ensure_ascii=False, indent=2)
        except Exception as exc:
            return f"[unreadable JSON: {exc}]"
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


# Bump when a change to extraction would alter the corpus produced from unchanged inputs, so
# every subject re-ingests instead of serving a corpus built by the older code.
INGEST_VERSION = 2


def _fingerprint(subject: str, files: list[Path]) -> str:
    """Identity of the inputs a cached corpus was built from: every file's path, size and mtime,
    plus the extractor version. Any drift rebuilds."""
    parts = [f"v{INGEST_VERSION}"]
    for f in files:
        st = f.stat()
        parts.append(f"{f.relative_to(subject_dir(subject))}:{st.st_size}:{int(st.st_mtime)}")
    return "|".join(parts)


def _corpus_path(subject: str) -> Path:
    return RESOURCE_CACHE / f"{subject}.corpus.txt"


def _meta_path(subject: str) -> Path:
    return RESOURCE_CACHE / f"{subject}.meta.json"


def ingest(subject: str, force: bool = False) -> dict:
    """Build (or reuse) the corpus + meta for a subject. Returns a summary dict."""
    files = _files(subject)
    errors = validate_bundle(subject) if files else []
    summary = {"subject": subject, "files": len(files), "chars": 0,
               "cutoff": None, "roles": {}, "bundle": bool(files),
               "valid": bool(files) and not errors, "errors": errors}
    if not files:
        return summary

    # Rebuild unless the inputs fingerprint identically to what the cache was built from.
    # A bare `cache mtime >= newest source mtime` check is not enough: a corpus written moments
    # after its sources — but from a partial or failed read — looks fresh forever, and nothing in
    # the pipeline passes force=True. That is not hypothetical. Every subject but one was serving
    # ~5% of its bundle (spec-syllabus.pdf missing entirely) behind a cache that looked current.
    cpath, mpath = _corpus_path(subject), _meta_path(subject)
    fingerprint = _fingerprint(subject, files)
    cached_fp = None
    if mpath.exists():
        try:
            cached_fp = json.loads(mpath.read_text()).get("fingerprint")
        except (json.JSONDecodeError, OSError):
            cached_fp = None
    if cpath.exists() and not force and cached_fp == fingerprint:
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

    # The manifest records the first examination year explicitly. This is safer than treating an
    # implementation date mentioned in a specification as the first year with valid exam papers.
    manifest_path = subject_dir(subject) / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text())
        cutoff = int(manifest["sources"]["syllabus"]["firstExamYear"])
    except (FileNotFoundError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        cutoff = extract_cutoff(corpus)
    summary["chars"] = len(corpus)
    summary["cutoff"] = cutoff
    if not summary["roles"]:                            # populate roles when reusing cached corpus
        for f in files:
            r = role_of(f); summary["roles"][r] = summary["roles"].get(r, 0) + 1
    mpath.write_text(json.dumps({"subject": subject, "cutoff": cutoff,
                                 "files": len(files), "chars": len(corpus),
                                 "fingerprint": fingerprint}, indent=2))
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
    elif not s["valid"]:
        print(f"[resources] {subj}: INVALID")
        for error in s["errors"]:
            print(f"  - {error}")
    else:
        print(f"[resources] {subj}: {s['files']} file(s) {s['roles']}, {s['chars']} chars, "
              f"cutoff {s['cutoff'] or '(not stated — will fall back to estimate)'}")
