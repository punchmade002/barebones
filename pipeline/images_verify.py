"""Stage 7b — DIAGRAM VISUAL VALIDATION (reform: crop + validate visually).

images.py crops each candidate figure out of the paper page but does NOT attach it — the
bounding box can be wrong (blank, cut-off, or just text) even when has_figure was true. This
stage looks at the actual CROP and confirms it shows a clear, complete, relevant figure before it
reaches a question's `diagram` field. Partial crops are retained as review blockers rather than
being silently cached as "no figure".

One worker job per source page (up to six crops in a labelled contact sheet). Reads/writes the same sidecar
`_data/reports/figures-<subject>.json` images.py uses: entries with `pending_crop` become either
`{"has_figure": true, "diagram": <path>}` (attached) or `{"has_figure": false, "reason": "rejected-crop"}`.

    python3 images_verify.py chemistry prepare
    python3 images_verify.py chemistry collect
"""
from __future__ import annotations
import json
import re
import sys
from io import BytesIO
from pathlib import Path

from config import CANONICAL, REPORTS, EXAM_IMAGES, SUPPLIED_FIGURE_RE
from segment import render_js, _save

EMIT_TOOL = {
    "name": "emit_verify",
    "description": "Confirm whether a cropped image shows a clear, complete exam figure.",
    "input_schema": {
        "type": "object",
        "properties": {"results": {"type": "array", "items": {"type": "object",
            "properties": {
                "key": {"type": "string"},
                "relevant": {"type": "boolean"}, "complete": {"type": "boolean"},
                "tight": {"type": "boolean"}, "reason": {"type": "string"},
                "needs_recrop": {"type": "boolean"}},
            "required": ["key", "relevant", "complete", "tight", "needs_recrop"]}}},
        "required": ["results"],
    },
}

_TASK = ("The image contains the source exam page with the detected box and the resulting crop. "
         "Independently judge relevance, completeness and tightness. Tight means no neighbouring "
         "question stem, answer prose or unrelated visual. Any false field blocks publication.")


def _stage(subject: str) -> str:
    return f"images-verify-{subject}"


def _sidecar_path(subject: str) -> Path:
    return REPORTS / f"figures-{subject}.json"


def _pending(subject: str) -> dict:
    from images import _load_sidecar                       # versioned {id_scheme_version, entries}
    side = _load_sidecar(_sidecar_path(subject))
    return {k: v for k, v in side.items()
            if isinstance(v, dict) and v.get("pending_crop")}


def _parse(content):
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_verify":
            inp = b.input if isinstance(b.input, dict) else {}
            return inp.get("results", []) if isinstance(inp.get("results"), list) else []
    return []


def validate_output(obj, job=None) -> bool:
    if not isinstance(obj, dict) or not isinstance(obj.get("results"), list) or not obj["results"]:
        return False
    keys = []
    for item in obj["results"]:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str):
            return False
        if any(not isinstance(item.get(field), bool)
               for field in ("relevant", "complete", "tight", "needs_recrop")):
            return False
        keys.append(item["key"])
    if len(keys) != len(set(keys)):
        return False
    if isinstance(job, dict):
        expected = job.get("meta", {}).get("keys", [])
        if expected and keys != expected:
            return False
    return True


def _comparison_png(entries: list[tuple[str, dict, Path]]) -> tuple[bytes, bool]:
    """One source page plus up to six numbered crop cards."""
    first = entries[0][1]
    pdf, page_index = first.get("source_pdf"), first.get("source_page")
    if not (pdf and isinstance(page_index, int)):
        return entries[0][2].read_bytes(), False
    try:
        import fitz
        from PIL import Image, ImageDraw
        page = fitz.open(pdf).load_page(page_index)
        pix = page.get_pixmap(dpi=110, alpha=False)
        page_im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        draw = ImageDraw.Draw(page_im)
        colours = [(220, 20, 60), (20, 90, 220), (0, 150, 90),
                   (180, 90, 0), (145, 40, 180), (0, 150, 160)]
        for number, (_key, entry, _crop) in enumerate(entries, 1):
            bbox = entry.get("bbox")
            if not (isinstance(bbox, list) and len(bbox) == 4):
                return entries[0][2].read_bytes(), False
            x0, y0, x1, y1 = bbox
            rect = (int(x0 * pix.width), int(y0 * pix.height),
                    int(x1 * pix.width), int(y1 * pix.height))
            colour = colours[(number - 1) % len(colours)]
            for width in range(4):
                draw.rectangle((rect[0]-width, rect[1]-width, rect[2]+width, rect[3]+width),
                               outline=colour)
            draw.text((rect[0] + 4, max(0, rect[1] - 16)), str(number), fill=colour)
        page_im.thumbnail((620, 960))
        canvas = Image.new("RGB", (1420, 1040), "white")
        labels = ImageDraw.Draw(canvas)
        labels.text((20, 12), "SOURCE PAGE — numbered detected boxes", fill="black")
        canvas.paste(page_im, (20 + (620-page_im.width)//2, 44))
        for index, (key, _entry, crop) in enumerate(entries):
            crop_im = Image.open(crop).convert("RGB")
            crop_im.thumbnail((350, 270))
            col, row = index % 2, index // 2
            x, y = 670 + col * 370, 44 + row * 325
            labels.text((x, y), f"{index + 1}. {key}"[:52], fill=colours[index % len(colours)])
            canvas.paste(crop_im, (x, y + 24))
        out = BytesIO(); canvas.save(out, format="PNG")
        return out.getvalue(), True
    except Exception as exc:
        print(f"[images-verify] could not build page comparison: {exc}")
        return entries[0][2].read_bytes(), False


def prepare(subject: str) -> int:
    """Queue up to six crops from one source page in each verification job."""
    import agent_bridge as bridge
    pending = _pending(subject)
    grouped: dict[tuple, list[tuple[str, dict, Path]]] = {}
    for key, v in pending.items():
        crop = EXAM_IMAGES.parent / v["pending_crop"]     # repo-root-relative
        if not crop.exists():
            continue
        group = (v.get("source_pdf"), v.get("source_page"))
        if not group[0] or not isinstance(group[1], int):
            group = (key, -1)  # legacy sidecar: isolate it so it cannot taint other crops
        grouped.setdefault(group, []).append((key, v, crop))
    jobs = []
    for page_no, (_group, entries) in enumerate(sorted(grouped.items(), key=lambda x: str(x[0]))):
        for chunk_no in range(0, len(entries), 6):
            chunk = entries[chunk_no:chunk_no + 6]
            comparison, context_compared = _comparison_png(chunk)
            listed = "\n\n".join(f"{i + 1}. KEY: {key}\nQUESTION: {entry.get('question', '')[:1000]}"
                                      for i, (key, entry, _crop) in enumerate(chunk))
            jobs.append({
                "custom_id": f"page_{page_no:04d}_{chunk_no // 6:02d}",
                "prompt": "Compare every numbered box on the source page with its numbered crop. "
                          "Return exactly one result for each KEY in order. Relevant means the "
                          "supplied visual needed by that question; complete includes every edge, "
                          "axis, label, legend and table cell; tight excludes neighbouring prose.\n\n"
                          + listed,
                "tool": EMIT_TOOL, "image_png": comparison,
                "meta": {"keys": [key for key, _entry, _crop in chunk],
                         "context_compared": context_compared},
            })
    if not jobs:
        return 0
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[images-verify] {len(pending)} crop(s) grouped into {len(jobs)} page batch job(s)")
    return len(jobs)


def collect(subject: str) -> None:
    """Attach confirmed crops to their part; delete + flag rejected ones; re-render."""
    import agent_bridge as bridge
    import ids
    from images import _load_sidecar, _save_sidecar
    rows = json.loads((CANONICAL / f"{subject}.json").read_text())
    # raises on duplicate ids: a lossy index attaches a crop to whichever row was last, so a
    # figure can end up rendered against a question it does not belong to
    by_id = ids.index_by_id(rows, where="images_verify.collect")
    side_path = _sidecar_path(subject)
    sidecar = _load_sidecar(side_path)
    ins, outs = bridge.inputs(_stage(subject)), bridge.outputs(_stage(subject))
    attached = rejected = 0
    for cid, content in outs.items():
        meta = ins.get(cid, {}).get("meta", {})
        returned = {item.get("key"): item for item in _parse(content) if isinstance(item, dict)}
        for key in meta.get("keys", []):
            entry = sidecar.get(key, {})
            rel = entry.get("pending_crop")
            if not rel:
                continue
            result = returned.get(key)
            if result is None:
                sidecar[key] = {"has_figure": True, "needs_review": True,
                                "reason": "crop verifier omitted this key", "diagram": rel}
                rejected += 1
                continue
            relevant, complete, tight = (result.get("relevant"), result.get("complete"),
                                         result.get("tight"))
            reason, needs_recrop = result.get("reason", ""), result.get("needs_recrop")
            context_compared = bool(meta.get("context_compared"))
            if relevant and complete and tight and context_compared:
                q = by_id.get(entry.get("qid"))
                idx = entry.get("idx", -1)
                if q and 0 <= idx < len(q["parts"]):
                    q["parts"][idx]["diagram"] = rel
                    sidecar[key] = {"has_figure": True, "diagram": rel, "qa_version": 2,
                                    "relevant": True, "complete": True, "tight": True,
                                    "context_compared": True}
                    attached += 1
                else:
                    sidecar[key] = {"has_figure": True, "needs_review": True,
                                    "reason": "verified crop target no longer exists", "diagram": rel}
            else:
                crop = EXAM_IMAGES.parent / rel
                if crop.exists():
                    crop.unlink()                          # don't leave rejected crops around
                if needs_recrop or (relevant and (not complete or not tight)) or not context_compared:
                    sidecar[key] = {"has_figure": True, "needs_review": True,
                                    "reason": f"needs-recrop: {reason}"[:160],
                                    "qid": entry.get("qid"), "idx": entry.get("idx")}
                else:
                    sidecar[key] = {"has_figure": False,
                                    "reason": f"rejected-crop: {reason}"[:160]}
                rejected += 1
            _save_sidecar(side_path, sidecar)
            _save(subject, rows)
    # One supplied stimulus often serves consecutive parts. Vision can correctly crop it for
    # the first part yet reject a second, tighter crop as prose-only. If a sibling explicitly
    # points above/below and this question has exactly one confirmed diagram, reuse it.
    shared = 0
    for q in rows:
        diagrams = {p.get("diagram") for p in q.get("parts", []) if p.get("diagram")}
        if len(diagrams) != 1:
            continue
        rel = next(iter(diagrams))
        for idx, part in enumerate(q.get("parts", [])):
            if part.get("diagram") or not SUPPLIED_FIGURE_RE.search(part.get("question", "")):
                continue
            part["diagram"] = rel
            sidecar[f"{q['id']}#{idx}"] = {"has_figure": True, "diagram": rel,
                                           "qa_version": 2, "relevant": True,
                                           "complete": True, "tight": True,
                                           "context_compared": True,
                                           "reason": "shared sibling stimulus"}
            shared += 1
    _save_sidecar(side_path, sidecar)
    _save(subject, rows)
    js = render_js(subject, rows)
    print(f"\n[images-verify] attached {attached} confirmed diagram(s), rejected {rejected} bad "
          f"crop(s), shared {shared} sibling stimulus link(s) — re-rendered {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject)
        print("nothing to verify" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
