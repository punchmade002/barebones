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

from config import CANONICAL, REPORTS, EXAM_IMAGES, IMAGE_DPI, BBOX_PADDING, FIGURE_CUE_RE
from segment import MODEL, _retry, _digests, render_js, _save

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

MAX_TOKENS = 600
LEVEL_TAG = {"higher": "HL", "ordinary": "OL"}

EMIT_TOOL = {
    "name": "emit_figure",
    "description": "Report whether this exam question has an accompanying figure on the page, and where.",
    "input_schema": {
        "type": "object",
        "properties": {
            "has_figure": {"type": "boolean",
                           "description": "true only if there is a real diagram/graph/map/image/"
                                          "structured table the question depends on (not plain prose)"},
            "bbox": {
                "type": "array",
                "description": "tight box around the figure as fractions of the page: "
                               "[x0, y0, x1, y1], origin top-left, each 0-1",
                "items": {"type": "number"},
                "minItems": 4, "maxItems": 4,
            },
        },
        "required": ["has_figure"],
    },
}


def _level_of(q: dict) -> str:
    return "higher" if "Higher" in q.get("source", "") else "ordinary"


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
    """pages: [(pdf_path, page_index0, page_text)]. Return the best (pdf_path, page_index) the
    part text sits on, or None if no page is a confident match."""
    sample = _sample_words(part_text)
    if not sample:
        return None
    best, best_score = None, 0
    for pdf_path, idx, text in pages:
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
    """(year:int, level) -> [(pdf_path, page_index0, page_text)] across all that level's papers."""
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
            bucket.append((pdf, p["page"] - 1, p.get("text", "")))
    return by_level


# ── candidates ──────────────────────────────────────────────────────────────────
def _candidates(rows: list[dict], pages_by_level: dict, sidecar: dict, force: bool) -> list[dict]:
    cands, multi = [], {}
    # how many figure-cued parts per question (to decide whether to suffix filenames by part)
    for q in rows:
        multi[q["id"]] = sum(1 for p in q.get("parts", [])
                             if FIGURE_CUE_RE.search(p.get("question", "")))
    for q in rows:
        level, year = _level_of(q), q["year"]
        for i, part in enumerate(q.get("parts", [])):
            key = f"{q['id']}#{i}"
            qtext = part.get("question", "")
            if not FIGURE_CUE_RE.search(qtext):
                continue
            if part.get("diagram") and (EXAM_IMAGES.parent / part["diagram"]).exists():
                continue                              # already cropped
            if not force and key in sidecar:
                continue                              # already evaluated (hit or miss)
            loc = locate_page(qtext, pages_by_level.get((year, level), []))
            if not loc:
                sidecar[key] = {"has_figure": False, "reason": "page-not-located"}
                continue
            pdf_path, page_index = loc
            tag = LEVEL_TAG.get(level, level[:2].upper())
            name = f"{year}-{tag}-{_sanitize(q.get('source','').split('—')[-1]) or _sanitize(str(i))}"
            if multi[q["id"]] > 1:
                name += f"-{_sanitize(part.get('label') or str(i))}"
            cands.append({"key": key, "q": q, "part": part, "pdf": pdf_path,
                          "page": page_index, "qtext": qtext, "name": name})
    return cands


def _prompt(qtext: str) -> str:
    return ("This is one page of a Leaving Certificate exam paper. The question below is on this "
            "page. If the question depends on an accompanying FIGURE on this page (a diagram, "
            "graph, map, chemical structure, labelled apparatus, or a structured data table), set "
            "has_figure=true and return a TIGHT bounding box around just that figure (exclude the "
            "question text and surrounding prose). If the question is plain text with no figure to "
            "show, set has_figure=false.\n\nQUESTION:\n" + qtext[:1500])


def _page_png(pdf_path: str, page_index: int) -> bytes:
    """Render a whole exam page to PNG bytes for the worker to look at."""
    return fitz.open(pdf_path).load_page(page_index).get_pixmap(dpi=IMAGE_DPI).tobytes("png")


def _parse(content) -> tuple[bool, list | None]:
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_figure":
            inp = b.input if isinstance(b.input, dict) else {}
            return bool(inp.get("has_figure")), inp.get("bbox")
    return False, None


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


_TASK = ("Look at each exam-page image and decide if the question depends on a FIGURE on it "
         "(diagram, graph, map, structure, labelled apparatus, structured data table). Return the "
         "object `schema` describes: has_figure, and if true a TIGHT bounding box [x0,y0,x1,y1] as "
         "fractions of the page (origin top-left) around JUST the figure — exclude question text.")


def prepare(subject: str, limit: int | None = None, force: bool = False) -> int:
    """Render a page image per figure-cued question part and queue it for the worker. Page-not-
    located parts are recorded as misses in the sidecar now. Returns the job count (0 = done)."""
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    import agent_bridge as bridge
    cpath = CANONICAL / f"{subject}.json"
    if not cpath.exists():
        raise SystemExit(f"No {cpath.name} — segment {subject} first.")
    rows = json.loads(cpath.read_text())
    side_path = REPORTS / f"figures-{subject}.json"
    sidecar = json.loads(side_path.read_text()) if side_path.exists() else {}

    pdf_map = _pdf_map(subject)
    pages_by_level = _pages_for(subject, pdf_map)
    cands = _candidates(rows, pages_by_level, sidecar, force)
    side_path.write_text(json.dumps(sidecar, indent=2))   # persist page-not-located misses
    if limit:
        cands = cands[:limit]
    if not cands:
        return 0
    jobs = []
    for c in cands:
        cid = re.sub(r"[^A-Za-z0-9_-]+", "_", c["key"])   # filesystem-safe id
        jobs.append({"custom_id": cid, "prompt": _prompt(c["qtext"]), "tool": EMIT_TOOL,
                     "image_png": _page_png(c["pdf"], c["page"]),
                     "meta": {"key": c["key"], "pdf": c["pdf"], "page": c["page"], "name": c["name"]}})
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[images] {len(jobs)} figure candidate(s) queued for the worker")
    return len(jobs)


def collect(subject: str) -> None:
    """Read the worker's has_figure/bbox answers, crop the figures, set part.diagram, re-render."""
    if fitz is None:
        raise SystemExit("Install PyMuPDF:  pip install pymupdf --break-system-packages")
    import agent_bridge as bridge
    cpath = CANONICAL / f"{subject}.json"
    rows = json.loads(cpath.read_text())
    side_path = REPORTS / f"figures-{subject}.json"
    sidecar = json.loads(side_path.read_text()) if side_path.exists() else {}
    by_id = {q["id"]: q for q in rows}
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)

    cropped = 0
    for cid, content in outs.items():
        meta = ins.get(cid, {}).get("meta", {})
        key = meta.get("key", cid)
        has_fig, bbox = _parse(content)
        rel = _crop(subject, meta, bbox) if (has_fig and bbox) else None
        if rel:
            qid, _, idx = key.partition("#")
            q = by_id.get(qid)
            if q and idx.isdigit() and int(idx) < len(q["parts"]):
                q["parts"][int(idx)]["diagram"] = rel
            sidecar[key] = {"has_figure": True, "diagram": rel}
            cropped += 1
            print(f"[crop] {key} -> {rel}")
        else:
            sidecar[key] = {"has_figure": False}
        side_path.write_text(json.dumps(sidecar, indent=2))
        _save(subject, rows)                              # durable after each crop
    js = render_js(subject, rows)
    print(f"\n{cropped} diagram(s) cropped into exam-images/{subject}/ — re-rendered {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, limit=limit, force=("--force" in args))
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
