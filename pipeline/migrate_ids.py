"""Re-issue unique question ids on an existing canonical store (id scheme v1 -> v2).

The v1 id was `{subject}-pp-{year}-{LV}-{label}`, which is not unique for any subject that
reuses question labels. History is the worst case on disk: 1,752 questions share 587 ids, so
two thirds of the store was unreachable through `{q["id"]: q for q in rows}` and the answer and
diagram stages were writing onto whichever row happened to be last.

This rewrites ids in place using ids.assign_unique_ids, backfilling the `level` and `label`
fields v1 rows never stored, and repairs the `source` line's subject capitalisation at the same
time. Nothing else in a row is touched — questions, marks, model answers and diagram paths are
carried over untouched.

    python3 migrate_ids.py history --dry-run     # report only, write nothing
    python3 migrate_ids.py history               # rewrite the store (backup written first)

Writes alongside the store:
    <subject>.json.v1.bak              the pre-migration store
    reports/id-migration-<subject>.json   old id -> new id, for auditing
"""
from __future__ import annotations
import json
import re
import sys

from config import CANONICAL, REPORTS, display_name
import ids


def _recover_label(q: dict, subject: str) -> str:
    """The question label ('Q1', 'D4'), from the v1 id where possible.

    The v1 id ends with the label and is the only reliable source: the `source` string ends with
    the label only for on-course papers — reference papers append " [REFERENCE — pre-current-
    syllabus]", whose em-dash defeats a naive rsplit on "—".
    """
    if q.get("label"):
        return q["label"]
    old = q.get("id") or ""
    lvl = ids.level_tag(q.get("level") or ("higher" if "Higher" in q.get("source", "") else "ordinary"))
    prefix = f"{subject}-pp-{q.get('year')}-{lvl}-"
    if old.startswith(prefix):
        return old[len(prefix):]
    m = re.search(r"—\s*([^—\[]+?)\s*(?:\[|$)", q.get("source", ""))
    return (m.group(1).strip() if m else "") or "q"


def _fix_source(q: dict, subject: str) -> str:
    """Rebuild the source line with the proper display name, preserving the REFERENCE suffix."""
    src = q.get("source", "")
    ref = " [REFERENCE — pre-current-syllabus]" if "[REFERENCE" in src else ""
    level = (q.get("level") or "").capitalize() or ("Higher" if "Higher" in src else "Ordinary")
    return f"LC {display_name(subject)} {level} {q['year']} — {q.get('label', '')}" + ref


def run(subject: str, dry_run: bool = False) -> int:
    cpath = CANONICAL / f"{subject}.json"
    if not cpath.exists():
        raise SystemExit(f"No {cpath} — nothing to migrate.")
    rows = json.loads(cpath.read_text())

    before_dups = ids.duplicate_ids(rows)
    before_reachable = len({r.get("id") for r in rows})
    print(f"{subject}: {len(rows)} rows, {before_reachable} distinct id(s), "
          f"{len(before_dups)} duplicated id(s) covering "
          f"{sum(before_dups.values())} row(s)")

    # backfill the fields v1 never stored, then re-issue ids over the whole store in order
    for q in rows:
        q.setdefault("subject", subject)
        if not q.get("level"):
            q["level"] = "higher" if "Higher" in q.get("source", "") else "ordinary"
        q["label"] = _recover_label(q, subject)
    old_ids = [q.get("id") for q in rows]
    ids.assign_unique_ids(rows)
    for q in rows:
        q["source"] = _fix_source(q, subject)

    mapping = [{"old": o, "new": q["id"]} for o, q in zip(old_ids, rows)]
    changed = sum(1 for m in mapping if m["old"] != m["new"])
    after_dups = ids.duplicate_ids(rows)
    print(f"  -> {len({q['id'] for q in rows})} distinct id(s), {len(after_dups)} duplicate(s), "
          f"{changed} row(s) re-identified")
    print(f"  -> sample: {mapping[0]['old']}  ->  {mapping[0]['new']}")
    print(f"  -> source: {rows[0]['source']}")
    if after_dups:
        raise SystemExit(f"BUG: {len(after_dups)} duplicate(s) survived migration — not writing.")

    if dry_run:
        print("\n--dry-run: nothing written.")
        return changed

    bak = cpath.with_suffix(".json.v1.bak")
    if not bak.exists():                                   # never overwrite the original backup
        bak.write_text(json.dumps(json.loads(cpath.read_text()), ensure_ascii=False, indent=2))
        print(f"  backup: {bak.name}")
    cpath.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    (REPORTS / f"id-migration-{subject}.json").write_text(json.dumps(
        {"subject": subject, "id_scheme_version": ids.ID_SCHEME_VERSION,
         "rows": len(rows), "changed": changed, "mapping": mapping}, indent=2))

    import segment
    js = segment.render_js(subject, rows)
    print(f"  wrote: {cpath.name}, id-migration-{subject}.json, {js.name}")
    print("\nNote: the images sidecar is keyed by question id and will be discarded "
          "automatically on the next images run (id scheme version bump).")
    return changed


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 migrate_ids.py <subject> [--dry-run]")
    run(subj, dry_run=("--dry-run" in args))
