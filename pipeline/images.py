"""Stage 7 — DIAGRAM CROPS, vision-guided.

Runs AFTER segment.py. For each question part that reads like it leans on a figure (a cheap
keyword pre-filter, config.FIGURE_CUE_RE), it finds the paper page the part is on, asks the
vision model for the figure's bounding box, crops just that region out of the PDF, saves it to
exam-images/<subject>/, and writes the path into the part's `diagram` field — the exact field the
app already renders (app.js "Show Diagram" + inline <img>). Finally it re-renders the generated
exam-questions JS so the diagrams ship.

Idempotent and cost-aware:
- Only figure-cued parts get a vision call (the crop itself is fully vision-guided).
- A sidecar (_data/reports/figures-<subject>.json) records every part already evaluated — both
  hits and misses — so re-runs never re-spend tokens. `--force` ignores it.
- A part that already has a `diagram` whose file exists is left untouched.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 images.py chemistry --sync            # immediate, concurrent
    python3 images.py chemistry --sync --limit 3  # only first 3 figure candidates (smoke test)
    python3 images.py chemistry                    # Batch API (unattended)
"""
from __future__ import annotations
import base64
import csv
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from config import (CANONICAL, REPORTS, EXAM_IMAGES, IMAGE_DPI, BBOX_PADDING,
                    FIGURE_CUE_RE, SCAN_ALL_PARTS_FOR_FIGURES)
from segment import MODEL, _retry, _digests, render_js, _save, level_of
import ids

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

MAX_TOKENS = 600
LEVEL_TAG = {"higher": "HL", "ordinary": "OL"}

EMIT_TOOL = {
    "name": "emit_figure",
    "description": "Report figure dependency and location for every listed question part on one page.",
    "input_schema": {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "key": {"type": "string"},
                        "has_figure": {"type": "boolean"},
                        "bbox": {"type": "array", "items": {"type": "number"},
                                 "minItems": 4, "maxItems": 4},
                    },
                    "required": ["key", "has_figure"],
                },
            },
        },
        "required": ["results"],
    },
}


_level_of = level_of          # canonical rows now carry `level`; kept as an alias for callers


# ── sidecar ───────────────────────────────────────────────────────────────────
# The sidecar is keyed by "<question id>#<part index>", so it is only meaningful for the ID
# scheme that produced those keys. It is stored inside a versioned envelope: when the scheme
# changes, the whole map is dropped rather than left to suppress re-evaluation of parts whose
# ids have moved. The old un-versioned flat shape is read as version 1.
def _load_sidecar(path: Path) -> dict:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text())
    version = raw.get("id_scheme_version", 1) if isinstance(raw, dict) else 1
    entries = raw.get("entries", {}) if "id_scheme_version" in raw else raw
    if version != ids.ID_SCHEME_VERSION:
        print(f"[images] sidecar {path.name} was written for id scheme v{version} "
              f"(now v{ids.ID_SCHEME_VERSION}) — discarding {len(entries)} stale entr(ies); "
              f"figure candidates will be re-evaluated.")
        return {}
    return entries


def _save_sidecar(path: Path, entries: dict) -> None:
    path.write_text(json.dumps(
        {"id_scheme_version": ids.ID_SCHEME_VERSION, "entries": entries}, indent=2))


def _sanitize(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", (s or "").strip()).strip("-")
    return s or "q"


# ── page location ─────────────────────────────────────────────────────────────
_WORD_RE = re.compile(r"[A-Za-z]{4,}")


def _sample_words(text: str, n: int = 12) -> list[str]:
    seen, out = set(), []
    for w in _WORD_RE.findall(text or ""):
        lw = w.lower()
        if lw not in seen:
            seen.add(lw); out.append(lw)
        if len(out) >= n:
            break
    return out


def locate_page(part_text: str, pages: list[tuple]) -> tuple | None:
    """pages: [(pdf_path, page_index0, page_text, paper_no)]. Return the best (pdf_path, page_index) the
    part text sits on, or None if no page is a confident match."""
    sample = _sample_words(part_text)
    if not sample:
        return None
    best, best_score = None, 0
    for pdf_path, idx, text, *_rest in pages:
        low = (text or "").lower()
        score = sum(1 for w in sample if w in low)
        if score > best_score:
            best, best_score = (pdf_path, idx), score
    if best and best_score >= max(3, int(len(sample) * 0.4)):
        return best
    return None


# ── manifest + digests -> page index ────────────────────────────────────────────
def _pdf_map(subject: str) -> dict:
    """(year:int, level, paper) -> papers PDF path (prefer the English version)."""
    man = REPORTS / f"manifest-{subject}.csv"
    if not man.exists():
        raise SystemExit(f"No manifest-{subject}.csv — run `python3 run.py {subject}` first.")
    out: dict = {}
    with man.open() as f:
        for r in csv.DictReader(f):
            if r.get("kind") != "papers" or int(r.get("bytes", 0) or 0) <= 0:
                continue
            key = (int(r["year"]), r["level"], r.get("paper", ""))
            if key not in out or r.get("version") == "EV":
                out[key] = r["path"]
    return out


def _pages_for(subject: str, pdf_map: dict) -> dict:
    """(year:int, level) -> [(pdf_path, page_index0, page_text, paper_no)]."""
    by_level: dict = {}
    for dg in _digests(subject, limit=None):
        paper = dg.get("paper")
        if not paper:
            continue
        pdf = pdf_map.get((dg["year"], dg["level"], dg.get("paper_no", "")))
        if not pdf:
            continue
        bucket = by_level.setdefault((dg["year"], dg["level"]), [])
        for p in paper["pages"]:
            bucket.append((pdf, p["page"] - 1, p.get("text", ""), dg.get("paper_no", "")))
    return by_level


# ── candidates ──────────────────────────────────────────────────────────────────
def _candidates(rows: list[dict], pages_by_level: dict, sidecar: dict, force: bool) -> list[dict]:
    cands, multi = [], {}
    # In exhaustive mode every part is a candidate, so every multi-part question gets stable,
    # collision-free filenames. Cue hits are still sorted first for bounded smoke tests.
    for q in rows:
        multi[q["id"]] = (len(q.get("parts", [])) if SCAN_ALL_PARTS_FOR_FIGURES else
                          sum(1 for p in q.get("parts", [])
                              if FIGURE_CUE_RE.search(p.get("question", ""))))
    for q in rows:
        level, year = _level_of(q), q["year"]
        for i, part in enumerate(q.get("parts", [])):
            key = f"{q['id']}#{i}"
            qtext = part.get("question", "")
            cue = bool(FIGURE_CUE_RE.search(qtext))
            if not SCAN_ALL_PARTS_FOR_FIGURES and not cue:
                continue
            if part.get("diagram") and (EXAM_IMAGES.parent / part["diagram"]).exists():
                continue                              # already cropped
            if not force and key in sidecar:
                continue                              # already evaluated (hit or miss)
            pages = pages_by_level.get((year, level), [])
            loc = None
            source_page = part.get("source_page")
            paper_no = str(q.get("paper", "") or "")
            if isinstance(source_page, int) and source_page > 0:
                loc = next(((pdf, idx) for pdf, idx, _text, pno in pages
                            if idx == source_page - 1 and (not paper_no or str(pno) == paper_no)), None)
            if not loc:
                loc = locate_page(qtext, pages)
            if not loc:
                sidecar[key] = {"has_figure": False, "reason": "page-not-located"}
                continue
            pdf_path, page_index = loc
            tag = LEVEL_TAG.get(level, level[:2].upper())
            name = f"{year}-{tag}-{_sanitize(q.get('source','').split('—')[-1]) or _sanitize(str(i))}"
            if multi[q["id"]] > 1:
                name += f"-{_sanitize(part.get('label') or str(i))}"
            cands.append({"key": key, "q": q, "part": part, "pdf": pdf_path,
                          "page": page_index, "qtext": qtext, "name": name,
                          "cue": cue})
    return sorted(cands, key=lambda c: (not c["cue"], c["key"]))


def _prompt(items: list[dict]) -> str:
    listed = "\n\n".join(f"KEY: {c['key']}\nQUESTION: {c['qtext'][:1200]}" for c in items)
    return ("This is one page of a Leaving Certificate exam paper. Inspect the WHOLE page once, "
            "then return exactly one result for EVERY keyed question part below. A supplied figure "
            "can serve several parts; reuse its bbox for each dependent key. Figure means diagram, "
            "graph, map, photo, illustration, food label, advertisement, symbol set, or structured "
            "data table—not plain prose. For each dependent part set has_figure=true and give a "
            "tight [x0,y0,x1,y1] fractional bbox around just the visual. Otherwise false.\n\n" + listed)


def _page_png(pdf_path: str, page_index: int) -> bytes:
    """Render a whole exam page to PNG bytes for the worker to look at."""
    return fitz.open(pdf_path).load_page(page_index).get_pixmap(dpi=IMAGE_DPI).tobytes("png")


def _page_has_visual_evidence(pdf_path: str, page_index: int, items: list[dict]) -> bool:
    """Conservative zero-model rejection.

    Never skip a cue-bearing page. Otherwise inspect the PDF object tree: raster/image blocks or
    any vector drawing keep the page in vision review. We only reject genuinely text-only pages,
    so reducing calls cannot hide an ordinary embedded diagram, graph, ruled table, or photo.
    Any PDF inspection uncertainty also keeps the page.
    """
    if any(c.get("cue") for c in items):
        return True
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_index)
        if page.get_images(full=True) or page.get_drawings():
            return True
        blocks = page.get_text("dict").get("blocks", [])
        return any(b.get("type") == 1 for b in blocks)  # inline raster block
    except Exception:
        return True


def _parse(content) -> list[dict]:
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_figure":
            inp = b.input if isinstance(b.input, dict) else {}
            return inp.get("results", []) if isinstance(inp.get("results"), list) else []
    return []


def validate_output(obj) -> bool:
    if not isinstance(obj, dict) or not isinstance(obj.get("results"), list) or not obj["results"]:
        return False
    for item in obj["results"]:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str) \
                or not isinstance(item.get("has_figure"), bool):
            return False
        if item["has_figure"]:
            bbox = item.get("bbox")
            if not (isinstance(bbox, list) and len(bbox) == 4
                    and all(isinstance(v, (int, float)) for v in bbox)):
                return False
    return True


def _crop(subject: str, c: dict, bbox: list) -> str | None:
    """Crop bbox (fractions) out of the page, save PNG, return repo-root-relative path."""
    try:
        x0, y0, x1, y1 = [float(v) for v in bbox]
    except Exception:
        return None
    x0, x1 = sorted((max(0.0, min(1.0, x0)), max(0.0, min(1.0, x1))))
    y0, y1 = sorted((max(0.0, min(1.0, y0)), max(0.0, min(1.0, y1))))
    if (x1 - x0) < 0.02 or (y1 - y0) < 0.02:
        return None                                   # implausibly tiny -> treat as no figure
    page = fitz.open(c["pdf"]).load_page(c["page"])
    W, H = page.rect.width, page.rect.height
    px0 = max(0, (x0 - BBOX_PADDING) * W); py0 = max(0, (y0 - BBOX_PADDING) * H)
    px1 = min(W, (x1 + BBOX_PADDING) * W); py1 = min(H, (y1 + BBOX_PADDING) * H)
    clip = fitz.Rect(px0, py0, px1, py1)
    out_dir = EXAM_IMAGES / subject
    out_dir.mkdir(parents=True, exist_ok=True)
    fname, n = f"{c['name']}.png", 2
    while (out_dir / fname).exists():                  # don't clobber a different part's crop
        fname = f"{c['name']}-{n}.png"; n += 1
    page.get_pixmap(clip=clip, dpi=IMAGE_DPI).save(out_dir / fname)
    return f"exam-images/{subject}/{fname}"


def _stage(subject: str) -> str:
    return f"images-{subject}"


_TASK = ("Inspect each exam page exhaustively once. Return one keyed result for every listed part; "
         "a shared visual may use the same bbox for several keys. Include supplied photos, labels, "
         "advertisements, symbol sets and data tables as well as conventional diagrams/graphs.")


def prepare(subject: str, limit: int | None = None, force: bool = False) -> int:
    """Render a page image per question part and queue it for the worker. Page-not-
    located parts are recorded as misses in the sidecar now. Returns the job count (0 = done)."""
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    import agent_bridge as bridge
    cpath = CANONICAL / f"{subject}.json"
    if not cpath.exists():
        raise SystemExit(f"No {cpath.name} — segment {subject} first.")
    rows = json.loads(cpath.read_text())
    side_path = REPORTS / f"figures-{subject}.json"
    sidecar = _load_sidecar(side_path)

    pdf_map = _pdf_map(subject)
    pages_by_level = _pages_for(subject, pdf_map)
    cands = _candidates(rows, pages_by_level, sidecar, force)
    _save_sidecar(side_path, sidecar)                     # persist page-not-located misses
    if limit:
        cands = cands[:limit]
    if not cands:
        return 0
    grouped: dict[tuple, list[dict]] = {}
    for c in cands:
        grouped.setdefault((c["pdf"], c["page"]), []).append(c)
    jobs = []
    skipped_pages = skipped_parts = 0
    for n, ((pdf, page), items) in enumerate(sorted(grouped.items())):
        if not _page_has_visual_evidence(pdf, page, items):
            skipped_pages += 1
            skipped_parts += len(items)
            for c in items:
                sidecar[c["key"]] = {"has_figure": False,
                                     "reason": "deterministic-text-only-page-v1"}
            continue
        jobs.append({"custom_id": f"page_{n:04d}", "prompt": _prompt(items), "tool": EMIT_TOOL,
                     "image_png": _page_png(pdf, page),
                     "meta": {"pdf": pdf, "page": page,
                              "items": [{"key": c["key"], "name": c["name"],
                                         "question": c["qtext"]} for c in items]}})
    _save_sidecar(side_path, sidecar)
    if not jobs:
        print(f"[images] skipped {skipped_pages} proven text-only page(s); no vision work remains")
        return 0
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[images] {len(cands)} part(s) grouped into {len(jobs)} page-level inspection job(s); "
          f"skipped {skipped_parts} part(s) on {skipped_pages} proven text-only page(s)")
    return len(jobs)


def collect(subject: str) -> None:
    """Read the worker's has_figure/bbox answers, crop the figures, set part.diagram, re-render."""
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    import agent_bridge as bridge
    cpath = CANONICAL / f"{subject}.json"
    rows = json.loads(cpath.read_text())
    side_path = REPORTS / f"figures-{subject}.json"
    sidecar = _load_sidecar(side_path)
    # raises on duplicate ids: a lossy index here attaches each crop to whichever row was last,
    # so a figure can end up rendered against a question it does not belong to
    by_id = ids.index_by_id(rows, where="images.collect")
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)

    cropped = 0
    for cid, content in outs.items():
        meta = ins.get(cid, {}).get("meta", {})
        expected = {item["key"]: item for item in meta.get("items", [])}
        returned = {item.get("key"): item for item in _parse(content) if isinstance(item, dict)}
        for key, item_meta in expected.items():
            result = returned.get(key)
            if result is None:
                sidecar[key] = {"needs_review": True, "reason": "page worker omitted this key"}
                continue
            crop_meta = {**meta, **item_meta}
            rel = _crop(subject, crop_meta, result.get("bbox")) if result.get("has_figure") else None
            if rel:
                qid, _, idx = key.partition("#")
                sidecar[key] = {"has_figure": True, "pending_crop": rel,
                                "qid": qid, "idx": int(idx) if idx.isdigit() else -1,
                                "question": item_meta.get("question", ""),
                                # Preserve source context so verification can compare the crop
                                # with the page and prove both completeness and tightness.
                                "bbox": result.get("bbox"), "source_pdf": meta.get("pdf"),
                                "source_page": meta.get("page")}
                cropped += 1
                print(f"[crop] {key} -> {rel} (pending visual check)")
            elif result.get("has_figure"):
                sidecar[key] = {"has_figure": True, "needs_review": True,
                                "reason": "invalid/empty crop from reported figure"}
            else:
                sidecar[key] = {"has_figure": False}
        _save_sidecar(side_path, sidecar)
    # `rows` is untouched here — images_verify attaches the confirmed crops and re-renders.
    print(f"\n{cropped} candidate crop(s) saved — images_verify will confirm before attaching.")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, limit=limit, force=("--force" in args))
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
