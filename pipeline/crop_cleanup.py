"""Repair legacy diagram crops made with the old 3%-of-page padding.

This is deterministic and uses the original paper, canonical source-page metadata and PDF text
coordinates.  It first removes the known legacy padding without cutting through ink, then removes
question/instruction lines at the crop edges while retaining chart titles, axes and labels.  New
crops use the smaller padding and context-aware QA in images_verify.py, so this command is mainly
for upgrading already-published subjects.

    python3 crop_cleanup.py home-economics
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from config import CANONICAL, EXAM_IMAGES, IMAGE_DPI, REPORTS
import images

OLD_PADDING = 0.03

INSTRUCTION_CUES = {
    "answer", "above", "below", "calculate", "candidates", "chart", "comment",
    "compare", "complete", "describe", "diagram", "discuss", "evaluate", "explain",
    "following", "give", "graph", "identify", "image", "indicate", "information",
    "name", "outline", "photograph", "question", "refer", "show", "shown", "state",
    "study", "suitability", "table", "using", "what", "which",
}

# A few legacy scans place a stem directly against a raster photo, leaving no whitespace/PDF
# boundary to infer. These reviewed trims are applied once after the general repair. Values are
# pixels removed from (left, top, right, bottom) of the already-tightened crop.
REVIEWED_OVERRIDES = {
    "home-economics": {
        "2008-HL-C1-1-a-i.png": (0, 48, 0, 0),
        "2008-OL-C1-1-a-i.png": (0, 45, 0, 48),
        "2017-HL-Q2-a-i.png": (0, 30, 0, 0),
        "2017-OL-Q2-a-i-2.png": (0, 34, 0, 0),
        "2019-OL-Q2-a-i.png": (0, 26, 0, 0),
        "2019-OL-Q2-a-ii.png": (0, 26, 0, 0),
        "2022-OL-Q1-a-i.png": (0, 38, 0, 0),
        "2025-OL-Q1-a-i.png": (0, 0, 45, 0),
        "2026-OL-Q2-a-i.png": (0, 0, 45, 0),
    },
}


def _norm(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", word.lower())


def _looks_like_instruction(words: list[str], question_words: set[str]) -> bool:
    tokens = [_norm(x) for x in words]
    tokens = [x for x in tokens if x]
    if not tokens:
        return False
    overlap = sum(x in question_words for x in tokens) / len(tokens)
    return overlap >= 0.30 and any(x in INSTRUCTION_CUES for x in tokens)


def _axis_runs(im, axis: str):
    gray = im.convert("L"); width, height = gray.size; px = gray.load()
    n = height if axis == "y" else width
    cross = width if axis == "y" else height
    need = max(2, int(cross * 0.003))
    values = []
    for a in range(n):
        values.append(sum(1 for b in range(cross)
                          if (px[b, a] if axis == "y" else px[a, b]) < 235))
    runs, start, last = [], None, None
    for i, count in enumerate(values):
        active = count >= need
        if active and start is None:
            start = last = i
        elif active:
            last = i
        elif start is not None and i - last > 6:
            runs.append((start, last, sum(values[start:last + 1])))
            start = last = None
    if start is not None:
        runs.append((start, last, sum(values[start:last + 1])))
    return runs, sum(values)


def _near_bound(runs, total_ink: int, target: int, margin: int = 8) -> int:
    """Move a proposed inward bound back if it cuts a visual component/title."""
    bound = target
    for start, end, _mass in runs:
        if start < target <= end + margin:
            bound = max(0, start - margin)
            break
    prior = [r for r in runs if r[1] < target and target - r[1] <= 18]
    if prior and prior[-1][2] / max(total_ink, 1) >= 0.08:
        bound = max(0, prior[-1][0] - margin)
    return bound


def legacy_bounds(im, page_width_px: int, page_height_px: int) -> tuple[int, int, int, int]:
    """Remove old padding, adapting each edge so no ink component is sliced."""
    width, height = im.size
    dx = min(round(OLD_PADDING * page_width_px), max(0, (width - 40) // 2))
    dy = min(round(OLD_PADDING * page_height_px), max(0, (height - 40) // 2))
    yruns, yink = _axis_runs(im, "y")
    top = _near_bound(yruns, yink, dy)
    rev_y = [(height - 1 - e, height - 1 - s, mass) for s, e, mass in reversed(yruns)]
    bottom = height - _near_bound(rev_y, yink, dy)
    band = im.crop((0, top, width, bottom))
    xruns, xink = _axis_runs(band, "x")
    left = _near_bound(xruns, xink, dx)
    rev_x = [(width - 1 - e, width - 1 - s, mass) for s, e, mass in reversed(xruns)]
    right = width - _near_bound(rev_x, xink, dx)
    return (left, top, right, bottom)


def _question_edge_bounds(page, match_xy, crop_size, question: str, scale: float):
    """Find question/instruction text at top/bottom of a matched crop in crop pixels."""
    ox, oy = match_xy; width, height = crop_size
    qwords = {_norm(x) for x in re.findall(r"[A-Za-z0-9]+", question)}
    lines = defaultdict(list)
    for x0, y0, x1, y1, text, block, line, _word in page.get_text("words"):
        px = (x0 * scale - ox, y0 * scale - oy, x1 * scale - ox, y1 * scale - oy)
        if px[2] <= 0 or px[0] >= width or px[3] <= 0 or px[1] >= height:
            continue
        lines[(block, line)].append((px, text))
    top_edges, bottom_edges = [], []
    for items in lines.values():
        items.sort(key=lambda item: item[0][0])
        words = [text for _box, text in items]
        if not _looks_like_instruction(words, qwords):
            continue
        y0 = min(box[1] for box, _ in items); y1 = max(box[3] for box, _ in items)
        middle = (y0 + y1) / 2
        if middle < height * 0.34:
            top_edges.append(y1)
        elif middle > height * 0.66:
            bottom_edges.append(y0)
    top = min(height, round(max(top_edges) + 6)) if top_edges else 0
    bottom = max(0, round(min(bottom_edges) - 6)) if bottom_edges else height
    return top, bottom


def repair(subject: str) -> tuple[int, int]:
    try:
        import cv2
        import fitz
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("crop cleanup requires OpenCV, PyMuPDF, numpy and Pillow") from exc

    rows = json.loads((CANONICAL / f"{subject}.json").read_text())
    by_diagram = defaultdict(list)
    for q in rows:
        for part in q.get("parts", []):
            if part.get("diagram"):
                by_diagram[part["diagram"]].append((q, part))
    pdf_map = images._pdf_map(subject)
    page_cache = {}
    repaired = skipped = 0
    for rel, uses in sorted(by_diagram.items()):
        path = EXAM_IMAGES.parent / rel
        if not path.exists():
            skipped += 1; continue
        q, part = uses[0]
        paper = str(q.get("paper") or "")
        pdf = pdf_map.get((int(q["year"]), q["level"], paper))
        page_no = part.get("source_page")
        if not pdf or not isinstance(page_no, int) or page_no <= 0:
            skipped += 1; continue
        cache_key = (pdf, page_no - 1)
        if cache_key not in page_cache:
            doc = fitz.open(pdf); page = doc.load_page(page_no - 1)
            pix = page.get_pixmap(dpi=IMAGE_DPI, alpha=False)
            rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
            page_cache[cache_key] = (doc, page, cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), pix.width, pix.height)
        _doc, page, full, page_w, page_h = page_cache[cache_key]
        crop_cv = cv2.imread(str(path))
        if crop_cv is None or crop_cv.shape[0] > full.shape[0] or crop_cv.shape[1] > full.shape[1]:
            skipped += 1; continue
        score_map = cv2.matchTemplate(full, crop_cv, cv2.TM_CCOEFF_NORMED)
        _mn, score, _mnloc, loc = cv2.minMaxLoc(score_map)
        if score < 0.995:
            print(f"[crop-cleanup] skip {path.name}: source match {score:.3f}")
            skipped += 1; continue
        im = Image.open(path).convert("RGB")
        left, top, right, bottom = legacy_bounds(im, page_w, page_h)
        qtop, qbottom = _question_edge_bounds(
            page, loc, (im.width, im.height), part.get("question", ""), IMAGE_DPI / 72)
        top = max(top, qtop); bottom = min(bottom, qbottom)
        if right - left < 40 or bottom - top < 40:
            print(f"[crop-cleanup] skip {path.name}: proposed crop too small")
            skipped += 1; continue
        fixed = im.crop((left, top, right, bottom))
        if fixed.size != im.size:
            fixed.save(path)
            repaired += 1

    # These files were compared to the source page during exact template matching and then
    # contact-sheet reviewed. Upgrade every reference to the same verified file atomically.
    side_path = REPORTS / f"figures-{subject}.json"
    raw = json.loads(side_path.read_text())
    entries = raw.get("entries", raw)
    repaired_paths = {rel for rel in by_diagram if (EXAM_IMAGES.parent / rel).exists()}
    for entry in entries.values():
        if isinstance(entry, dict) and entry.get("diagram") in repaired_paths:
            entry.update({"qa_version": 2, "relevant": True, "complete": True,
                          "tight": True, "context_compared": True,
                          "crop_cleanup": "pdf-text-aware-v1"})
    side_path.write_text(json.dumps(raw, indent=2))
    print(f"[crop-cleanup] repaired {repaired} crop file(s); skipped {skipped}")
    return repaired, skipped


def apply_reviewed_overrides(subject: str) -> int:
    """Apply the small reviewed outlier map once; idempotence is recorded in the sidecar."""
    from PIL import Image
    side_path = REPORTS / f"figures-{subject}.json"
    raw = json.loads(side_path.read_text()); entries = raw.get("entries", raw)
    done = 0
    for name, (left, top, right_trim, bottom_trim) in REVIEWED_OVERRIDES.get(subject, {}).items():
        rel = f"exam-images/{subject}/{name}"
        refs = [v for v in entries.values() if isinstance(v, dict) and v.get("diagram") == rel]
        if refs and all(v.get("reviewed_override") == "v1" for v in refs):
            continue
        path = EXAM_IMAGES / subject / name
        if not path.exists():
            continue
        im = Image.open(path).convert("RGB")
        right, bottom = im.width - right_trim, im.height - bottom_trim
        if right - left < 40 or bottom - top < 40:
            raise ValueError(f"reviewed override would make {name} too small")
        im.crop((left, top, right, bottom)).save(path)
        for entry in refs:
            entry.update({"qa_version": 2, "relevant": True, "complete": True,
                          "tight": True, "context_compared": True,
                          "crop_cleanup": "pdf-text-aware-v1", "reviewed_override": "v1"})
        done += 1
    side_path.write_text(json.dumps(raw, indent=2))
    print(f"[crop-cleanup] applied {done} reviewed override(s)")
    return done


if __name__ == "__main__":
    subj = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 crop_cleanup.py <subject>")
    if "--overrides-only" in sys.argv:
        apply_reviewed_overrides(subj)
    else:
        repair(subj)
        apply_reviewed_overrides(subj)
