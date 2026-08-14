"""Stage 2 — EXTRACT. PDF -> per-page text + per-page PNG, written as one JSON per doc.

Modern SEC papers are real text (fast). Older papers and many practical-subject marking
schemes are scans -> the `needs_ocr` flag is set so a later pass (Tesseract or a vision
model) can fill them. We do NOT bulk-OCR here; that decision is logged, not forced.

Requires: PyMuPDF  ->  pip install pymupdf --break-system-packages
Idempotent: skips a doc whose extracted JSON already exists.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

from config import EXTRACTED, REPORTS
from textclean import normalize_glyphs

try:
    import fitz  # PyMuPDF
except ImportError:                                    # let the file import without the dep
    fitz = None

MANIFEST = REPORTS / "manifest.csv"
RENDER_DPI = 150                                       # enough for diagram crops + OCR


def extract_pdf(pdf_path: Path, out_dir: Path) -> dict:
    doc = fitz.open(pdf_path)
    pages, img_dir = [], out_dir / pdf_path.stem
    img_dir.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(doc):
        # Same normalisation as digest.extract_pages — font-encoded glyphs are fixed at the one
        # boundary where PDF bytes become text, so no downstream stage has to handle them.
        text = normalize_glyphs(page.get_text("text"))
        pix = page.get_pixmap(dpi=RENDER_DPI)
        img_path = img_dir / f"p{i + 1:02d}.png"
        pix.save(img_path)
        pages.append({
            "page": i + 1,
            "text": text,
            "image": str(img_path),
            "needs_ocr": len(text.strip()) < 40,       # near-empty text => scanned page
        })
    doc.close()
    return {"source": str(pdf_path), "pages": pages}


def run() -> None:
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    if not MANIFEST.exists():
        raise SystemExit("No manifest — run acquire.py first.")
    with MANIFEST.open() as f:
        rows = [r for r in csv.DictReader(f) if r["downloaded"] in ("True", "true", "1")]
    for r in rows:
        pdf = Path(r["path"])
        if not pdf.exists():
            continue
        out_json = EXTRACTED / r["subject"] / f"{pdf.stem}.json"
        if out_json.exists():
            continue                                   # idempotent
        out_json.parent.mkdir(parents=True, exist_ok=True)
        data = extract_pdf(pdf, EXTRACTED / r["subject"])
        data.update({k: r[k] for k in ("subject", "year", "level", "paper", "kind")})
        out_json.write_text(json.dumps(data, indent=2))
        scanned = sum(p["needs_ocr"] for p in data["pages"])
        print(f"[ok] {out_json.name}  ({len(data['pages'])} pages, {scanned} need OCR)")


if __name__ == "__main__":
    run()
