"""Stage 2+ — DIGEST. Turn the downloaded PDFs into app-ready, paired text per paper.

For each (year, level) it pairs the exam paper with its marking scheme and emits one JSON
"ready to be broken into concept points and exam questions" downstream (Stage 3 segment,
Stage 5 tag, Stage 6 flashcards). Text comes from PyMuPDF; pages with almost no text are
flagged `needs_ocr` (older scans) rather than silently dropped.

    pip install pymupdf --break-system-packages
    python digest.py history
"""
from __future__ import annotations
import csv
import json
from collections import defaultdict
from pathlib import Path

from config import RAW, DIGEST, REPORTS

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None


def extract_pages(pdf_path: Path) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text").strip()
        pages.append({"page": i + 1, "text": text, "needs_ocr": len(text) < 40})
    doc.close()
    return pages


def run(subject: str) -> None:
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    manifest = REPORTS / f"manifest-{subject}.csv"
    if not manifest.exists():
        raise SystemExit(f"No manifest for {subject} — run acquire_form.py first.")
    with manifest.open() as f:
        rows = [r for r in csv.DictReader(f) if int(r.get("bytes", 0) or 0) > 0]

    # group by (year, level, paper, status); pair each paper with its scheme. `paper` is ""
    # for single-paper subjects (History, Chemistry) and "1"/"2" for Maths/English/Irish.
    groups: dict[tuple, dict] = defaultdict(dict)
    for r in rows:
        groups[(r["year"], r["level"], r.get("paper", ""), r["status"])][r["kind"]] = r["path"]

    out_dir = DIGEST / subject
    out_dir.mkdir(parents=True, exist_ok=True)
    index, scans = [], 0
    for (year, level, paper, status), kinds in sorted(groups.items()):
        digest = {
            "subject": subject, "year": int(year), "level": level,
            "paper_no": paper, "status": status,
            "paper":  {"pages": extract_pages(Path(kinds["papers"]))} if "papers" in kinds else None,
            "scheme": {"pages": extract_pages(Path(kinds["scheme"]))} if "scheme" in kinds else None,
        }
        n_ocr = sum(p["needs_ocr"] for src in (digest["paper"], digest["scheme"]) if src for p in src["pages"])
        scans += n_ocr
        ptag = f"-P{paper}" if paper else ""
        out = out_dir / f"{year}-{level}{ptag}{'-REF' if status == 'reference' else ''}.json"
        out.write_text(json.dumps(digest, ensure_ascii=False, indent=2))
        index.append({"file": out.name, "year": int(year), "level": level, "paper": paper,
                      "status": status, "has_paper": digest["paper"] is not None,
                      "has_scheme": digest["scheme"] is not None, "ocr_pages": n_ocr})
        print(f"[digest] {out.name}  paper={'Y' if digest['paper'] else '-'} "
              f"scheme={'Y' if digest['scheme'] else '-'}  ocr_pages={n_ocr}")

    (out_dir / "_index.json").write_text(json.dumps(index, indent=2))
    paired = sum(1 for i in index if i["has_paper"] and i["has_scheme"])
    print(f"\n{len(index)} paper-sets digested -> {out_dir}")
    print(f"  {paired} have BOTH paper + marking scheme (ready to pair Q↔model)")
    if scans:
        print(f"  {scans} pages need OCR (older scans) — feed to a vision/OCR pass before segmenting")


if __name__ == "__main__":
    import sys
    run(sys.argv[1] if len(sys.argv) > 1 else "history")
