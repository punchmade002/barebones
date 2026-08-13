"""Apply reviewed replacement bboxes and re-queue their crop-verification jobs.

The mapping JSON shape is:
  {"<question-id>#<part-index>": {"page_job": "page_0123", "bbox": [x0,y0,x1,y1]}}

Old rejected crops and verifier outputs are moved to a recoverable archive. The relevant
verification input PNG is replaced with the new crop and its output is removed, so the normal
images-verify worker must inspect the replacement before it can be attached.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

from config import DATA, EXAM_IMAGES, REPORTS
from images import _crop, _load_sidecar, _save_sidecar


def apply(subject: str, mapping_path: Path, archive_dir: Path) -> int:
    mapping = json.loads(mapping_path.read_text())
    if not isinstance(mapping, dict) or not mapping:
        raise SystemExit(f"No recrop mappings in {mapping_path}")
    image_stage = DATA / "agent" / f"images-{subject}"
    verify_stage = DATA / "agent" / f"images-verify-{subject}"
    side_path = REPORTS / f"figures-{subject}.json"
    sidecar = _load_sidecar(side_path)
    archive_dir.mkdir(parents=True, exist_ok=True)

    applied = 0
    for key, correction in mapping.items():
        page_job = Path(str(correction.get("page_job", ""))).stem
        bbox = correction.get("bbox")
        page_input = image_stage / "in" / f"{page_job}.json"
        if not page_input.exists():
            raise SystemExit(f"Missing page job for {key}: {page_input}")
        rec = json.loads(page_input.read_text())
        meta = rec.get("meta", {})
        item = next((x for x in meta.get("items", []) if x.get("key") == key), None)
        if not item:
            raise SystemExit(f"Key {key} is not in {page_input.name}")
        entry = sidecar.get(key)
        if not isinstance(entry, dict) or not entry.get("pending_crop"):
            raise SystemExit(f"Key {key} has no pending crop in {side_path.name}")

        new_rel = _crop(subject, {**meta, **item}, bbox)
        if not new_rel:
            raise SystemExit(f"Replacement bbox for {key} did not produce a crop: {bbox}")
        old_crop = EXAM_IMAGES.parent / entry["pending_crop"]
        if old_crop.exists():
            shutil.move(str(old_crop), archive_dir / old_crop.name)

        entry["pending_crop"] = new_rel
        entry.pop("needs_review", None)
        entry.pop("reason", None)
        sidecar[key] = entry

        cid = re.sub(r"[^A-Za-z0-9_-]+", "_", key)
        verify_input = verify_stage / "in" / f"{cid}.json"
        verify_rec = json.loads(verify_input.read_text())
        verify_png = verify_stage / "in" / verify_rec["image"]
        verify_png.write_bytes((EXAM_IMAGES.parent / new_rel).read_bytes())
        verify_output = verify_stage / "out" / f"{cid}.json"
        if verify_output.exists():
            shutil.move(str(verify_output), archive_dir / verify_output.name)
        applied += 1

    _save_sidecar(side_path, sidecar)
    print(f"[recrop] applied {applied} replacement bbox(es); verification outputs re-queued")
    return applied


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 3:
        raise SystemExit("usage: python3 recrop.py <subject> <mapping.json> <archive-dir>")
    apply(args[0], Path(args[1]), Path(args[2]))
