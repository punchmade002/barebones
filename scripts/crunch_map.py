"""Export one subject's Crunch point graph for the Crunch map page (see CRUNCH_MODE.md).

    python3 scripts/crunch_map.py biology   # writes drafts/crunch/<subject>/map/data.json

data.json is one object: chapters [[id, title]], subs [[sid, title, chapter index]],
items [[id, sub index, cost, text]], links [[item index, needs index, 1 essential | 0 helpful]].
The page (drafts/crunch/crunch-map.html) does the scoring, so tuning needs no re-export.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crunch_points import ROOT, items


def main(subject):
    all_items = items(subject)
    points = json.loads((ROOT / "content" / "crunch" / f"{subject}-points.json").read_text())
    index_js = (ROOT / "subject-index.js").read_text()
    chapter_ids = sorted({sid.split("-")[0] for sid in all_items}, key=lambda c: int(re.sub(r"\D", "", c)))
    chapters = []
    for c in chapter_ids:
        m = re.search(r'\{"id":"%s","title":"([^"]+)"' % c, index_js)
        chapters.append([c, m.group(1) if m else c])
    ch_index = {c: i for i, (c, _) in enumerate(chapters)}
    sids = sorted(all_items, key=lambda s: [int(n) for n in re.findall(r"\d+", s)])
    subs, rows = [], []
    for si, sid in enumerate(sids):
        title, its = all_items[sid]
        subs.append([sid, title, ch_index[sid.split("-")[0]]])
        for iid, text, h in its:
            p = points[iid]
            assert p["hash"] == h, f"{iid} text changed since it was rated; re-run that package"
            rows.append([iid, si, p["cost"], text])
    pos = {r[0]: i for i, r in enumerate(rows)}
    links = [[pos[iid], pos[l["id"]], 1 if l["strength"] == "essential" else 0]
             for iid, *_ in rows for l in points[iid]["needs"]]
    out = ROOT / "drafts" / "crunch" / subject / "map"
    out.mkdir(parents=True, exist_ok=True)
    (out / "data.json").write_text(json.dumps(
        {"subject": subject, "chapters": chapters, "subs": subs, "items": rows, "links": links},
        ensure_ascii=False, separators=(",", ":")))
    print(f"{len(rows)} items, {len(links)} links, {len(subs)} subsections, {len(chapters)} chapters → {out / 'data.json'}")


if __name__ == "__main__":
    main(sys.argv[1])
