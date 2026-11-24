"""Export one subject's Crunch point graph for the Crunch map page (see CRUNCH_MODE.md).

    python3 scripts/crunch_map.py biology   # writes drafts/crunch/<subject>/map/data.json

data.json is one object: chapters [[id, title]], subs [[sid, title, chapter index, exam marks, [years examined]]],
items [[id, sub index, cost, text]], links [[item index, needs index, 1 essential | 0 helpful]],
papers [{year, qs: [{opt: 0 compulsory | 1 optional, slots: [[marks, k, [item index]]]}]}] (Higher Level).
A slot is one marking point, earned by knowing any k of its items. Parts tagged to points
(content/crunch/<subject>-exam-tags.json) use those tags; untagged parts fall back to one slot per
point of their subsections, the part's marks split evenly.
The page (drafts/crunch/crunch-map.html) does the scoring, so tuning needs no re-export.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crunch_points import ROOT, items


def higher_questions(subject):
    s = (ROOT / f"{subject}-exam-questions.js").read_text()
    return [q for q in json.loads(s[s.index("[", s.index("concat(")):s.rindex("]") + 1]) if q.get("level") == "higher"]


def exam_marks(qs):
    """Higher Level past-paper marks and years per subsection; a part tagged to several subsections splits its marks evenly."""
    marks, years = {}, {}
    for q in qs:
        for p in q["parts"]:
            refs = p.get("notesRefs") or []
            for r in refs:
                marks[r] = marks.get(r, 0) + p["marks"] / len(refs)
                years.setdefault(r, set()).add(q["year"])
    return marks, years


def papers(qs, all_items, pos, tags):
    """Each paper's questions as marking-point slots over item indexes. Section A is compulsory (the 2027 Q1); B and C are optional."""
    by_year = {}
    for q in qs:
        slots = []
        for p in q["parts"]:
            tagged = tags.get(q["id"], {}).get(p["label"])
            if tagged is not None:
                for s in tagged:
                    slots.append([p["marks"] / len(tagged), s["k"], [pos[i] for i in s["of"]]])
            else:
                pts = [pos[i] for r in p.get("notesRefs") or [] if r in all_items for i, _, _ in all_items[r][1]]
                slots += [[p["marks"] / len(pts), 1, [i]] for i in pts]
        if slots:
            by_year.setdefault(q["year"], []).append({"opt": 0 if q["sectionId"] == "bio-sectionA" else 1,
                                                      "slots": [[round(m, 4), k, o] for m, k, o in slots]})
    return [{"year": y, "qs": by_year[y]} for y in sorted(by_year)]


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
    qs = higher_questions(subject)
    marks, years = exam_marks(qs)
    subs, rows = [], []
    for si, sid in enumerate(sids):
        title, its = all_items[sid]
        subs.append([sid, title, ch_index[sid.split("-")[0]], round(marks.get(sid, 0), 2), sorted(years.get(sid, []))])
        for iid, text, h in its:
            p = points[iid]
            assert p["hash"] == h, f"{iid} text changed since it was rated; re-run that package"
            rows.append([iid, si, p["cost"], text])
    pos = {r[0]: i for i, r in enumerate(rows)}
    links = [[pos[iid], pos[l["id"]], 1 if l["strength"] == "essential" else 0]
             for iid, *_ in rows for l in points[iid]["needs"]]
    tag_file = ROOT / "content" / "crunch" / f"{subject}-exam-tags.json"
    tags = json.loads(tag_file.read_text()) if tag_file.exists() else {}
    paper_list = papers(qs, all_items, pos, tags)
    out = ROOT / "drafts" / "crunch" / subject / "map"
    out.mkdir(parents=True, exist_ok=True)
    (out / "data.json").write_text(json.dumps(
        {"subject": subject, "chapters": chapters, "subs": subs, "items": rows, "links": links, "papers": paper_list},
        ensure_ascii=False, separators=(",", ":")))
    print(f"{len(rows)} items, {len(links)} links, {len(subs)} subsections, {len(chapters)} chapters, "
          f"{len(paper_list)} papers ({len(tags)} questions tagged to points) → {out / 'data.json'}")


if __name__ == "__main__":
    main(sys.argv[1])
