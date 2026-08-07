"""Stage 7b — DIAGRAM VISUAL VALIDATION (reform: crop + validate visually).

images.py crops each candidate figure out of the paper page but does NOT attach it — the
bounding box can be wrong (blank, cut-off, or just text) even when has_figure was true. This
stage looks at the actual CROP and confirms it shows a clear, complete figure before it reaches
a question's `diagram` field. Rejected crops are deleted and recorded, never shown to a student.

One worker job per pending crop (cheap haiku vision call). Reads/writes the same sidecar
`_data/reports/figures-<subject>.json` images.py uses: entries with `pending_crop` become either
`{"has_figure": true, "diagram": <path>}` (attached) or `{"has_figure": false, "reason": "rejected-crop"}`.

    python3 images_verify.py chemistry prepare
    python3 images_verify.py chemistry collect
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

from config import CANONICAL, REPORTS, EXAM_IMAGES
from segment import render_js, _save

EMIT_TOOL = {
    "name": "emit_verify",
    "description": "Confirm whether a cropped image shows a clear, complete exam figure.",
    "input_schema": {
        "type": "object",
        "properties": {
            "ok": {"type": "boolean",
                   "description": "true ONLY if the image clearly shows a complete figure "
                                  "(diagram/graph/map/chemical structure/labelled apparatus/data "
                                  "table). false if it's blank, mostly plain text, or a cut-off/partial figure."},
            "reason": {"type": "string", "description": "short why"},
        },
        "required": ["ok"],
    },
}

_TASK = ("Look at each cropped image and confirm it shows a clear, COMPLETE exam figure (diagram, "
         "graph, map, chemical structure, labelled apparatus, or structured data table) — not blank, "
         "not just text, not a partial/cut-off figure. Return `ok` true/false as `schema` describes.")


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
            return bool(inp.get("ok")), inp.get("reason", "")
    return False, ""


def prepare(subject: str) -> int:
    """Queue one verification job per pending crop (with the crop PNG for the worker to view)."""
    import agent_bridge as bridge
    pending = _pending(subject)
    jobs = []
    for key, v in pending.items():
        crop = EXAM_IMAGES.parent / v["pending_crop"]     # repo-root-relative
        if not crop.exists():
            continue
        cid = re.sub(r"[^A-Za-z0-9_-]+", "_", key)
        jobs.append({
            "custom_id": cid,
            "prompt": "Does this cropped image show a clear, complete exam figure? "
                      "Set ok=false if it is blank, mostly plain text, or a cut-off/partial figure.",
            "tool": EMIT_TOOL,
            "image_png": crop.read_bytes(),
            "meta": {"key": key},
        })
    if not jobs:
        return 0
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[images-verify] {len(jobs)} crop(s) queued for visual confirmation")
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
        key = ins.get(cid, {}).get("meta", {}).get("key", cid)
        entry = sidecar.get(key, {})
        rel = entry.get("pending_crop")
        if not rel:
            continue
        ok, reason = _parse(content)
        if ok:
            q = by_id.get(entry.get("qid"))
            idx = entry.get("idx", -1)
            if q and 0 <= idx < len(q["parts"]):
                q["parts"][idx]["diagram"] = rel
            sidecar[key] = {"has_figure": True, "diagram": rel}
            attached += 1
        else:
            crop = EXAM_IMAGES.parent / rel
            if crop.exists():
                crop.unlink()                              # don't leave rejected crops around
            sidecar[key] = {"has_figure": False, "reason": f"rejected-crop: {reason}"[:120]}
            rejected += 1
        _save_sidecar(side_path, sidecar)
        _save(subject, rows)
    js = render_js(subject, rows)
    print(f"\n[images-verify] attached {attached} confirmed diagram(s), rejected {rejected} bad "
          f"crop(s) — re-rendered {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject)
        print("nothing to verify" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
