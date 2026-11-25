"""Audit exam-tag outputs: flag questions whose tagging looks rushed or off, and total the marks the tags can't reach.

    python3 drafts/crunch/biology/exam-tags/audit.py
"""
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from crunch_exam_tags import questions  # noqa: E402

out = Path(__file__).parent / "out"
rows, gap_marks, total_marks, no_answer_marks = [], 0, 0, 0
for q in questions("biology"):
    f = out / f"{q['id']}.json"
    if not f.exists():
        continue
    tags = json.loads(f.read_text())
    marks = sum(p["marks"] for p in q["parts"])
    total_marks += marks
    slots = sum(len(tags[p["label"]]) for p in q["parts"])
    empty = [p for p in q["parts"] if not tags[p["label"]] and p["marks"]]
    gap_marks += sum(p["marks"] for p in empty)
    no_answer_marks += sum(p["marks"] for p in q["parts"] if not (p.get("model") or "").strip())
    refs = {r for p in q["parts"] for r in p.get("notesRefs") or []}
    # tags whose subsection isn't one the part was tagged to (allowed, but many suggests drift)
    off = sum(1 for p in q["parts"] for s in tags[p["label"]] for i in s["of"] if i.split(".")[0] not in (p.get("notesRefs") or []))
    ids = sum(len(s["of"]) for p in q["parts"] for s in tags[p["label"]])
    rows.append((q["id"], marks, slots, len(empty), off / ids if ids else 0))

dens = [s / m for _, m, s, _, _ in rows if m]
mu, sd = statistics.mean(dens), statistics.pstdev(dens)
print(f"{len(rows)} questions audited. Marking points per mark: mean {mu:.2f}, sd {sd:.2f}")
print(f"Marks with no tags: {gap_marks} of {total_marks} ({100 * gap_marks / total_marks:.1f}%); "
      f"of which parts with no model answer in the bank: {no_answer_marks}")
for qid, m, s, e, off in rows:
    why = []
    if m and s / m < mu - 2 * sd:
        why.append(f"few marking points ({s} for {m} marks)")
    if m and s / m > mu + 2 * sd:
        why.append(f"many marking points ({s} for {m} marks)")
    if off > 0.5:
        why.append(f"{off:.0%} of tags outside the part's subsections")
    if why:
        print(f"  {qid}: {'; '.join(why)}")
