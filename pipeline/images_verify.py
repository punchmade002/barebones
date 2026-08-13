"""Stage 7b — DIAGRAM VISUAL VALIDATION (reform: crop + validate visually).

images.py crops each candidate figure out of the paper page but does NOT attach it — the
bounding box can be wrong (blank, cut-off, or just text) even when has_figure was true. This
stage looks at the actual CROP and confirms it shows a clear, complete, relevant figure before it
reaches a question's `diagram` field. Partial crops are retained as review blockers rather than
being silently cached as "no figure".

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

from config import CANONICAL, REPORTS, EXAM_IMAGES, SUPPLIED_FIGURE_RE
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
            "needs_recrop": {"type": "boolean",
                             "description": "true when a real relevant figure is present but the crop is cut off or incomplete"},
        },
        "required": ["ok", "needs_recrop"],
    },
}

_TASK = ("Look at each cropped image and the supplied question. Confirm the crop is a clear, "
         "COMPLETE figure relevant to that question. Set needs_recrop=true only when the relevant "
         "figure is real but cut off/incomplete; false for blank, prose-only, or unrelated crops.")


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
            return bool(inp.get("ok")), inp.get("reason", ""), bool(inp.get("needs_recrop"))
    return False, "malformed verifier output", False


def validate_output(obj) -> bool:
    return (isinstance(obj, dict) and isinstance(obj.get("ok"), bool)
            and isinstance(obj.get("needs_recrop"), bool))


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
        question = v.get("question", "")
        jobs.append({
            "custom_id": cid,
            "prompt": "Does this crop show a clear, complete figure relevant to the question? "
                      "Set needs_recrop=true if the relevant figure exists but is cut off.\n\n"
                      f"QUESTION:\n{question[:1500]}",
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
        ok, reason, needs_recrop = _parse(content)
        if ok:
            q = by_id.get(entry.get("qid"))
            idx = entry.get("idx", -1)
            if q and 0 <= idx < len(q["parts"]):
                q["parts"][idx]["diagram"] = rel
                sidecar[key] = {"has_figure": True, "diagram": rel}
                attached += 1
            else:
                sidecar[key] = {"has_figure": True, "needs_review": True,
                                "reason": "verified crop target no longer exists", "diagram": rel}
        else:
            crop = EXAM_IMAGES.parent / rel
            if crop.exists():
                crop.unlink()                              # don't leave rejected crops around
            if needs_recrop:
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
