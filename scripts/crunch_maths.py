"""Export Maths for the Crunch map, with skills in place of note points (see CRUNCH_MODE.md).

    python3 scripts/crunch_maths.py [higher|ordinary]   # writes drafts/crunch/maths[-ordinary]/map/data.json

Same data.json shape as crunch_map.py, so crunch-score.js and the map page score it unchanged:
- items are the skills database (pipeline/requirements/maths/skills.json); Higher has every skill, Ordinary
  drops HL-only skills. One "subsection" per app chapter.
- links are the skills' prereqs, all essential: a skill can't be used without the skills it's built from.
- cost: Beginner 1, Intermediate 1.5, Advanced 2.
- papers come from the rebuilt exam bank (marks) and skill-tags.json (each part's skills). A part's marks go half
  to its primary skill and half shared by its other skills (each earnable alone, like partial credit), plus a spread
  slot over the skills of the chapters it touches, as crunch_map.py does for tagged parts.
- Paper structure: 2015-2020 every question compulsory (Section A Q1-6, Section B Q7-9); from 2021 Section A any
  5 of 6 and Section B any 3 of 4, on each paper.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQ = ROOT / "pipeline" / "requirements" / "maths"
# shortcut: the bank on this branch stops at 2025; maths-older has 2015-2026. Read it from there while it's unmerged.
OLDER = ROOT / ".claude" / "worktrees" / "maths-older" / "maths-exam-questions.js"
BANK = OLDER if OLDER.exists() else ROOT / "maths-exam-questions.js"
COST = {"Beginner": 1, "Intermediate": 1.5, "Advanced": 2}


def main(level="higher"):
    S = json.loads((REQ / "skills.json").read_text())
    skills = [s for s in S["skills"] if level == "higher" or s["level"] != "HL"]
    tags = json.loads((REQ / "skill-tags.json").read_text())
    chapter_ids = [c for c in S["chapters"] if any(s["chapter"] == c for s in skills)]
    ch_index = {c: i for i, c in enumerate(chapter_ids)}
    title = lambda c: S["chapters"][c]["title"] if isinstance(S["chapters"][c], dict) else S["chapters"][c]
    chapters = [[c, title(c)] for c in chapter_ids]
    skills.sort(key=lambda s: (ch_index[s["chapter"]], s.get("rank", 0)))
    pos = {s["id"]: i for i, s in enumerate(skills)}
    items = [[s["id"], ch_index[s["chapter"]], COST[s["grade"]], s["title"]] for s in skills]
    links = [[pos[s["id"]], pos[p], 1] for s in skills for p in s["prereqs"] if p in pos]
    of_chapter = {c: [pos[s["id"]] for s in skills if s["chapter"] == c] for c in chapter_ids}

    src = BANK.read_text()
    qs = [q for q in json.loads(src[src.index("[", src.index("concat(")):src.rindex("]") + 1]) if q.get("level") == level]
    by_year, untagged, marks, years = {}, set(), {}, {}
    for q in qs:
        slots = []
        for p in q["parts"]:
            t = tags.get(f"{q['id']}#{p['label']}")
            if not t:
                untagged.add(q["year"])
                continue
            hit = [x for x in t["skills"] if x in pos]
            if not hit:
                continue
            primary = t["primary"] if t["primary"] in pos else hit[0]
            others = [x for x in hit if x != primary]
            share = p["marks"] / 2 if others else p["marks"]
            slots.append([share, 1, [pos[primary]]])
            slots += [[(p["marks"] - share) / len(others), 1, [pos[x]]] for x in others]
            chs = sorted({skills[pos[x]]["chapter"] for x in hit})
            slots.append([p["marks"], 0, [i for c in chs for i in of_chapter[c]]])
            for c in chs:
                marks[c] = marks.get(c, 0) + p["marks"] / len(chs)
                years.setdefault(c, set()).add(q["year"])
        if slots:
            g = ("A" if q["questionNumber"] <= 6 else "B") + q["paper"][-1] + ("" if q["year"] >= 2021 else "old")
            by_year.setdefault(q["year"], []).append({"g": g, "slots": [[round(m, 4), k, o] for m, k, o in slots]})
    papers = [{"year": y, "qs": by_year[y], **({"untagged": True} if y in untagged else {})} for y in sorted(by_year)]
    # each section is a quarter of the two papers (150 of 600 marks)
    groups = {f"{sec}{n}{era}": [0.25, None if era else (5 if sec == "A" else 3)]
              for sec in "AB" for n in "12" for era in ("", "old")}
    subs = [[c, t, i, round(marks.get(c, 0), 2), sorted(years.get(c, [])), ""] for i, (c, t) in enumerate(chapters)]
    name = "maths" if level == "higher" else "maths-ordinary"
    out = ROOT / "drafts" / "crunch" / name / "map"
    out.mkdir(parents=True, exist_ok=True)
    (out / "data.json").write_text(json.dumps(
        {"subject": name, "chapters": chapters, "subs": subs, "items": items, "links": links, "papers": papers,
         "groups": groups, "picks": {}, "pickCount": {}, "aac": None}, ensure_ascii=False, separators=(",", ":")))
    print(f"{len(items)} skills, {len(links)} prereq links, {len(chapters)} chapters, {len(papers)} papers "
          f"({', '.join(str(p['year']) for p in papers)}; untagged parts in {sorted(untagged) or 'none'}) → {out / 'data.json'}")


if __name__ == "__main__":
    main(*(sys.argv[1:] or ["higher"]))
