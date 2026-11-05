#!/usr/bin/env python3
"""Put each subject's whole past papers and marking schemes into the app's Exam papers archive.

scripts/fetch_exam_papers.py downloads every paper the SEC archive lists into
pipeline/_data/exam-papers/<subject>/ (gitignored) with a manifest of what each file is. This
script copies them to exam-papers/<subject>/, where the app serves them, and writes:

  exam-papers/<subject>/papers.js   the subject's paper list, loaded when its archive is opened
  exam-papers.js                    a few lines per subject (course, years, where the list is),
                                    loaded with the app

The PDFs are not opened; everything comes from the archive's own listing.

    python3 scripts/build_exam_papers.py biology
    python3 scripts/build_exam_papers.py all

Rebuilding some subjects keeps the entries already in exam-papers.js for the others.
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOWNLOADS = ROOT / "pipeline" / "_data" / "exam-papers"
OUT_DIR = ROOT / "exam-papers"
OUT_JS = ROOT / "exam-papers.js"

# Per subject:
#   archiveName    pattern matching the subject's name(s) in the SEC archive's Subject list
#   fromYear       earliest year fetched: the start of the syllabus the oldest papers were set on
#   course, firstExamined
#                  the course students sit now; papers set before `firstExamined` are tagged
#                  Old Course in the archive
#   variants       label prefix for a subject the archive lists under more than one name
#   labels         nicer names for the archive's booklet labels (also keeps older file names,
#                  which students' notes are saved against)
SUBJECTS = {
    "biology": {
        "archiveName": r"^Biology$",
        "fromYear": 2004,  # the previous syllabus, first examined 2004
        "course": "2025 specification",
        "firstExamined": 2027,
        "labels": {"Section A&B": "Sections A & B", "Section A B": "Sections A & B"},
    },
    "business": {
        "archiveName": r"^Business$",
        "fromYear": 1999,  # the previous syllabus, first examined 1999
        "course": "2025 specification",
        "firstExamined": 2027,
        "labels": {"Section 2 & 3": "Sections 2 & 3"},
    },
    "chemistry": {
        "archiveName": r"^Chemistry$",
        "fromYear": 2002,  # the previous syllabus, first examined 2002
        "course": "2025 specification",
        "firstExamined": 2027,
    },
    "geography": {
        "archiveName": r"^Geography$",
        "fromYear": 2006,
        "course": "current syllabus",
        "firstExamined": 2006,
        # The map, photograph and source paper go with both levels' papers
        "labels": {"Part 1": "Part One", "Part 2": "Part Two", "Map": "Ordnance Survey map",
                   "Picture Illustration": "Photograph", "Source Paper": "Source paper",
                   "Case Study": "Case study"},
        "unnamedExtra": "Map legend",  # 2010 lists the map's legend as a sheet with no name
    },
    "history": {
        # Listed as "History" in some years and as two fields, Early and Later Modern, in others
        "archiveName": r"^History\b",
        "fromYear": 2006,
        "course": "current syllabus",
        "firstExamined": 2006,
        "variants": {r"Early Modern": "Early Modern", r"Later Modern": "Later Modern"},
    },
    "home-economics": {
        "archiveName": r"^Home Economics",
        "fromYear": 2004,
        "course": "current syllabus",
        "firstExamined": 2004,
        "labels": {"Section B&C": "Sections B & C", "Practical Paper": "Practical coursework"},
    },
    "maths": {
        # Project Maths was phased in 2012-2014, with two sets of papers each year; 2015 was
        # the first year everyone sat the whole course
        "archiveName": r"^Mathematics$",
        "fromYear": 2015,
        "course": "current syllabus",
        "firstExamined": 2015,
    },
    "pe": {
        "archiveName": r"^Physical Education$",
        "fromYear": 2020,
        "course": "2018 specification",
        "firstExamined": 2020,
    },
}

LEVEL_ORDER = {"higher": 0, "ordinary": 1, "foundation": 2, "common": 3}


def variant_for(cfg: dict, listing: str) -> str:
    return next((label for pattern, label in cfg.get("variants", {}).items()
                 if re.search(pattern, listing)), "")


def label_for(cfg: dict, entry: dict, variant: str) -> str:
    part = cfg.get("labels", {}).get(entry["part"], entry["part"])
    if entry["level"] == "common" and not part:
        part = cfg.get("unnamedExtra", "")
    if entry["kind"] == "scheme":
        base = f"Marking scheme · {part}" if part else "Marking scheme"
    else:
        base = part or "Exam paper"
    return f"{variant} · {base}" if variant else base


def image_pdf(path: Path) -> bytes:
    """Wrap an image in a PDF so the viewer can show it and students can write on it. A JPEG's
    own bytes go in unchanged; a TIFF or PNG is saved as a high-quality JPEG first, a page each."""
    from PIL import Image, ImageSequence  # only Geography's maps and photographs need it

    with Image.open(path) as im:
        if im.format != "JPEG":
            pages = [frame.convert("RGB") for frame in ImageSequence.Iterator(im)]
            out = io.BytesIO()
            pages[0].save(out, "PDF", save_all=True, append_images=pages[1:], quality=90,
                          resolution=(im.info.get("dpi") or (150, 150))[0] or 150)
            return out.getvalue()
    data = path.read_bytes()
    with Image.open(path) as im:
        width, height = im.size
        colour = {"L": "/DeviceGray", "CMYK": "/DeviceCMYK"}.get(im.mode, "/DeviceRGB")
        dpi = (im.info.get("dpi") or (150, 150))[0] or 150
    page_w, page_h = width * 72 / dpi, height * 72 / dpi
    draw = f"q {page_w:.2f} 0 0 {page_h:.2f} 0 0 cm /Im0 Do Q".encode()
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {page_w:.2f} {page_h:.2f}] "
        f"/Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>".encode(),
        f"<< /Type /XObject /Subtype /Image /Width {width} /Height {height} /ColorSpace {colour} "
        f"/BitsPerComponent 8 /Filter /DCTDecode /Length {len(data)} >>\nstream\n".encode()
        + data + b"\nendstream",
        f"<< /Length {len(draw)} >>\nstream\n".encode() + draw + b"\nendstream",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, obj in enumerate(objects, 1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode()
    out += b"".join(f"{o:010d} 00000 n \n".encode() for o in offsets)
    out += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# A paper added by hand to the downloads folder, named like the downloader's files:
#   2021-higher-papers.pdf, 2021-ordinary-scheme.pdf, 2021-higher-papers-paper-one.pdf,
#   2016-higher-papers-early-modern.pdf, 2014-common-papers-map.pdf (or .jpg)
DROPPED = re.compile(r"^(\d{4})-(higher|ordinary|foundation|common)-(papers|scheme)(?:-(.+))?\.(pdf|jpg|jpeg|tif|tiff|png)$")


def dropped_in(cfg: dict, src: Path, listed: set[str]) -> list[dict]:
    entries = []
    for path in sorted(src.iterdir()):
        m = DROPPED.match(path.name.lower())
        if not m or path.name in listed:
            continue
        rest, variant = m[4] or "", ""
        for label in cfg.get("variants", {}).values():
            if rest.startswith(slug(label)):
                variant, rest = label, rest[len(slug(label)):].strip("-")
        print(f"  added by hand: {path.name}")
        entries.append({"year": int(m[1]), "level": m[2], "kind": m[3], "variant": variant,
                        "part": rest.replace("-", " ").title(), "file": path.name})
    return entries


def build(subject_id: str) -> dict:
    cfg = SUBJECTS[subject_id]
    src = DOWNLOADS / subject_id
    manifest = src / "manifest.json"
    if not manifest.exists():
        sys.exit(f"No downloaded papers in {src}; run scripts/fetch_exam_papers.py {subject_id} first")
    entries = json.loads(manifest.read_text())["entries"]
    entries += dropped_in(cfg, src, {e["file"] for e in entries})

    dest = OUT_DIR / subject_id
    if dest.is_dir():
        shutil.rmtree(dest)  # a clean copy, so files the archive no longer lists don't linger
    dest.mkdir(parents=True)

    # A field name only tells papers apart when the archive listed more than one that year
    # (History's marking scheme covers both fields under one name)
    fields: dict[tuple, set] = {}
    for entry in entries:
        fields.setdefault((entry["year"], entry["kind"]), set()).add(entry["variant"])

    # The archive sometimes calls a level's only paper or scheme "Paper One"; on its own that
    # reads as if Paper Two were missing
    counts: dict[tuple, int] = {}
    for entry in entries:
        key = (entry["year"], entry["level"], entry["kind"], entry["variant"])
        counts[key] = counts.get(key, 0) + 1

    papers = []
    for order, entry in enumerate(entries):
        several = len(fields[(entry["year"], entry["kind"])]) > 1
        if (counts[(entry["year"], entry["level"], entry["kind"], entry["variant"])] == 1
                and re.fullmatch(r"Paper (One|1)", entry["part"])):
            entry = {**entry, "part": ""}
        label = label_for(cfg, entry, entry["variant"] if several else "")
        name = f"{entry['year']}-{entry['level']}-{slug(label)}.pdf"
        if entry["file"].endswith(".pdf"):
            shutil.copyfile(src / entry["file"], dest / name)
        else:
            (dest / name).write_bytes(image_pdf(src / entry["file"]))
        papers.append({
            "year": entry["year"],
            "level": entry["level"],
            "kind": entry["kind"],
            "label": label,
            "file": f"exam-papers/{subject_id}/{name}",
            "oldCourse": entry["year"] < cfg["firstExamined"],
            "_order": order,
        })

    # Newest first; then by level, field, papers before schemes, and the archive's own order
    papers.sort(key=lambda p: (-p["year"], LEVEL_ORDER.get(p["level"], 9), p["kind"] == "scheme",
                               p["label"].split(" · ")[0] if " · " in p["label"] else "", p["_order"]))
    for p in papers:
        del p["_order"]

    body = json.dumps(papers, indent=1)
    lists = dest / "papers.js"
    lists.write_text(
        "// Generated by scripts/build_exam_papers.py — do not edit by hand.\n"
        "window.EXAM_PAPER_LISTS = window.EXAM_PAPER_LISTS || {};\n"
        f"window.EXAM_PAPER_LISTS[{json.dumps(subject_id)}] = {body};\n"
    )
    version = hashlib.sha1(lists.read_bytes()).hexdigest()[:8]
    years = [p["year"] for p in papers]
    return {
        "course": cfg["course"],
        "firstExamined": cfg["firstExamined"],
        "from": min(years),
        "to": max(years),
        "papers": sum(p["kind"] == "papers" for p in papers),
        "list": f"exam-papers/{subject_id}/papers.js?v={version}",
    }


def read_existing() -> dict:
    if not OUT_JS.exists():
        return {}
    m = re.search(r"window\.EXAM_PAPERS = (\{.*\});", OUT_JS.read_text(), re.S)
    archive = json.loads(m[1]) if m else {}
    # Drop entries in the old one-file format, which listed every paper here
    return {k: v for k, v in archive.items() if "list" in v}


def main() -> None:
    ids = sys.argv[1:]
    if ids == ["all"]:
        ids = list(SUBJECTS)
    if not ids or any(s not in SUBJECTS for s in ids):
        sys.exit(f"Usage: build_exam_papers.py <all|{'|'.join(SUBJECTS)}> [...]")
    archive = read_existing()
    for subject_id in ids:
        archive[subject_id] = build(subject_id)
        a = archive[subject_id]
        print(f"{subject_id}: {a['papers']} papers, {a['from']}–{a['to']}")
    archive = dict(sorted(archive.items()))
    OUT_JS.write_text(
        "// Generated by scripts/build_exam_papers.py — do not edit by hand.\n"
        "// One summary per subject; each subject's paper list loads when its archive is opened.\n"
        f"window.EXAM_PAPERS = {json.dumps(archive, indent=2)};\n"
    )


if __name__ == "__main__":
    main()
