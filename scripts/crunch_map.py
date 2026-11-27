"""Export one subject's Crunch point graph for the Crunch map page (see CRUNCH_MODE.md).

    python3 scripts/crunch_map.py biology   # writes drafts/crunch/<subject>/map/data.json

data.json is one object: chapters [[id, title]], subs [[sid, title, chapter index, exam marks, [years examined], track]],
items [[id, sub index, cost, text]], links [[item index, needs index, 1 essential | 0 helpful]],
papers [{year, qs: [{g: group, need: track, slots: [[marks, k, [item index]]]}]}] (Higher Level),
groups {group: [share of the paper, how many to answer]}, picks {kind: [[track, label]]}.
A track ("kind:value", e.g. "option:geoecology") marks content only some students study; the page keeps the
student's pick and drops the rest, and a question with `need` set is only on the paper for that track.
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
from crunch_exam_tags import tok

# The AAC (coursework) and its share of the overall grade, from <subject>-exam-info.js. The cut covers the written paper only.
AAC = {"biology": {"name": "Biology in Practice Investigation", "weight": 0.4},
       "geography": {"name": "Geographical Investigation", "weight": 0.2},
       "history": {"name": "Research Study Report", "weight": 0.2},
       "chemistry": {"name": "Chemistry in Practice Investigation", "weight": 0.4},
       # shortcut: Textiles (Elective 2) students' extra 10% coursework isn't modelled; add it if the app asks for the elective first
       "home-economics": {"name": "Food Studies coursework", "short": "coursework", "weight": 0.2},
       # PE's coursework is two parts, the Physical Activity Project (20%) and the Performance Assessment (30%)
       "pe": {"name": "coursework (project and performance)", "short": "coursework", "weight": 0.5}}


def geo_track(sid):
    ch = sid.rsplit("-s", 1)[0]
    if ch.startswith("geo-economic-"):
        return "elective:economic"
    if ch in ("geo-population-migration", "geo-urban"):
        return "elective:human"
    if ch.startswith("geo-option-"):
        return "option:" + ch[len("geo-option-"):]
    if ch == "geo-region-continental":
        return "region:" + sid
    return ""


def hist_topics(kind):
    return [["%s:hist-%s%d" % (kind, kind, n), t] for n, t in enumerate(HIST_TITLES[kind], 1)]


HIST_TITLES = {"ire": ["Ireland and the Union, 1815-1870", "Movements for political and social reform, 1870-1914",
                       "The pursuit of sovereignty and the impact of partition, 1912-1949", "The Irish diaspora, 1840-1966",
                       "Politics and society in Northern Ireland, 1949-1993", "Government, economy and society in the Republic, 1949-1989"],
               "eur": ["Nationalism and state formation in Europe, 1815-1871", "Nation states and international tensions, 1871-1920",
                       "Dictatorship and democracy in Europe, 1920-1945", "Division and realignment in Europe, 1945-1992",
                       "European retreat from empire and the aftermath, 1945-1990", "The United States and the world, 1945-1989"]}


def hist_track(sid):
    ch = sid.rsplit("-s", 1)[0]  # hist-ire3
    return ch.split("-")[1][:3] + ":" + ch


HOM_ELECTIVES = {"4": "elective:design", "5": "elective:textiles", "6": "elective:social"}  # by syllabus area
_hom_refs = {}


def hom_track(sid):
    """Elective content is syllabus areas 4-6; areas 1-3 are the Core everyone studies."""
    if sid not in _hom_refs:
        ref = json.loads((ROOT / "content" / "home-economics" / f"{sid}.json").read_text()).get("syllabusRef") or "1"
        _hom_refs[sid] = HOM_ELECTIVES.get(str(ref)[0], "")
    return _hom_refs[sid]


def hom_question(q):
    """Section A best 10 short questions; B Q1 compulsory plus two of Q2-5; C one question: Q1-3 are Electives 1-3,
    Q4 (since 2021) is a Core question anyone may take."""
    sec, n = q["sectionId"][-1], int(re.sub(r"\D", "", q["id"].rsplit("-", 1)[1]))
    if sec == "a":
        return "A", ""
    if sec == "b":
        return ("B1" if n == 1 else "B"), ""
    return "C", (["elective:design", "elective:textiles", "elective:social"][n - 1] if n <= 3 else "")


GEO_OPTIONS = ["global-interdependence", "geoecology", "culture-identity", "atmosphere-ocean"]  # Q13-15, 16-18, 19-21, 22-24


def geo_question(q):
    n, sec = q["questionNumber"], q["sectionId"]
    if sec == "geo-sectionP1":
        return "short", ""
    if sec == "geo-sectioncore":
        return ("physical" if n <= 3 else "regional"), ""
    if sec == "geo-sectionelective":
        return "elective", "elective:" + ("economic" if n <= 9 else "human")
    return "option", "option:" + GEO_OPTIONS[(n - 13) // 3]


# Paper structure per subject. groups: {group: [share of the paper, answer K]}, K None = all, marks-weighted;
# 0 < K < 1 = that share of the group's questions; K >= 1 = the best K. question(q) -> (group, track it needs or "").
SUBJECTS = {
    "biology": {"groups": {"A": [1 / 6, None], "BC": [5 / 6, 5 / 6]},
                "question": lambda q: ("A" if q["sectionId"] == "bio-sectionA" else "BC", ""), "track": lambda sid: ""},
    # HL written paper: Part One 80 (best 10 of 12 short questions), then 80 each for one physical, one regional,
    # one elective and one option question.
    "geography": {"groups": {"short": [0.2, 10], "physical": [0.2, 1], "regional": [0.2, 1], "elective": [0.2, 1], "option": [0.2, 1]},
                  "question": geo_question, "track": geo_track,
                  "picks": {"elective": [["elective:economic", "Economic Activities"], ["elective:human", "Human Environment"]],
                            "option": [["option:" + o, t] for o, t in zip(GEO_OPTIONS, ["Global Interdependence", "Geoecology", "Culture and Identity", "Atmosphere-Ocean Environment"])],
                            "region": [["region:geo-region-continental-s1", "India"], ["region:geo-region-continental-s2", "Brazil"]]}},
    # HL: Q1 documents (100) on one topic, then three essays (100 each) from the student's other topics, each the
    # student's pick of four titles; the alternative rules allow any three from two topics, so: the best 3 essays.
    # Students study two Irish and two European topics. Every essay title is its own question (split), and its
    # marks follow the model answer's paragraphs to the subsections they draw on (paragraphs).
    "history": {"groups": {"docs": [0.25, None], "essay": [0.75, 3]},
                "question": lambda q: ("docs" if q["sectionId"] == "hist-section1" else "essay", hist_track(q["chapterId"] + "-s0")),
                "track": hist_track, "split": True, "paragraphs": True,
                "picks": {"ire": hist_topics("ire"), "eur": hist_topics("eur")}, "pickCount": {"ire": 2, "eur": 2}},
    # HL (2023-2026 rules): Section A best 10 of 12 short questions (80), Section B the case study (50),
    # Section C best 3 of 5 long questions (120). Physical activity areas are left out (crunch_points.LEFT_OUT).
    "pe": {"groups": {"A": [80 / 250, 10], "B": [50 / 250, None], "C": [120 / 250, 3]},
           "question": lambda q: (q["sectionId"][-1], ""), "track": lambda sid: ""},
    # 2027 HL: Q1 compulsory (50) and five of Q2-7 (50 each). The bank is the old course (2001-2025: 11 questions,
    # any 8). Re-marked the 2027 way, as Biology: old Q4, the short questions, is the compulsory Q1; the rest are
    # optional, best 5 in 6.
    "chemistry": {"groups": {"Q1": [1 / 6, None], "rest": [5 / 6, 5 / 6]},
                  "question": lambda q: ("Q1" if q["id"].endswith("-q4") else "rest", ""), "track": lambda sid: ""},
    # HL 320: Section A best 10 of 12-14 (60), Section B Q1 (80) and two of Q2-5 (100), Section C one question (80).
    # shortcut: Elective 2's Section C is 40 marks (paper out of 280); modelled as 80, so Textiles shares are a little high.
    "home-economics": {"groups": {"A": [60 / 320, 10], "B1": [80 / 320, None], "B": [100 / 320, 2], "C": [80 / 320, 1]},
                       "question": hom_question, "track": hom_track,
                       "picks": {"elective": [["elective:design", "Home Design and Management"],
                                              ["elective:textiles", "Textiles, Fashion and Design"],
                                              ["elective:social", "Social Studies"]]}},
}


def paragraph_slots(part, all_items, pos, idf, vec):
    """One spread slot per model-answer paragraph, on the subsection of the part's notesRefs it shares the most
    distinctive words with (all of them if it shares none). Each paragraph carries an equal share of the marks."""
    refs = [r for r in part.get("notesRefs") or [] if r in all_items]
    if not refs:
        return []
    paras = [x for x in (part.get("model") or "").split("\n") if tok(x)] or [""]
    slots = []
    for para in paras:
        words = set(tok(para))
        best = max(refs, key=lambda r: sum(idf.get(w, 0) for w in words & vec[r]) / len(vec[r]) ** 0.5, default=None)
        hit = [best] if best and words & vec[best] else refs
        slots.append([part["marks"] / len(paras), 0, [pos[i] for r in hit for i, _, _ in all_items[r][1]]])
    return slots


def variants(refs, track):
    """A part on one study region counts for every region a student could have studied instead (India or Brazil)."""
    out = [refs]
    for r in refs:
        kind = track(r).split(":")[0]
        if kind == "region":
            alts = [s for s in ALL_SIDS if track(s).split(":")[0] == kind and s != r]
            out += [[a if x == r else x for x in refs] for a in alts]
    return out


ALL_SIDS = []


def higher_questions(subject):
    s = (ROOT / f"{subject}-exam-questions.js").read_text()
    qs = json.loads(s[s.index("[", s.index("concat(")):s.rindex("]") + 1])
    # Home Ec's bank predates the rebuild: no level field (the id says -HI-) and no notesRefs (exam-refs.json has them)
    refs_file = ROOT / "content" / "crunch" / f"{subject}-exam-refs.json"
    refs = json.loads(refs_file.read_text()) if refs_file.exists() else {}
    for q in qs:
        for p in q["parts"]:
            p["marks"] = p.get("marks") or 0  # a few off-spec parts have no marks
            if not p.get("notesRefs") and p["label"] in refs.get(q["id"], {}):
                p["notesRefs"] = refs[q["id"]][p["label"]]
    return [q for q in qs if q.get("level", "higher" if "-HI-" in q["id"] else "") == "higher"]


def exam_marks(qs, track):
    """Higher Level past-paper marks and years per subsection; a part tagged to several subsections splits its marks evenly."""
    marks, years = {}, {}
    for q in qs:
        for p in q["parts"]:
            for refs in variants(p.get("notesRefs") or [], track):
                for r in refs:
                    marks[r] = marks.get(r, 0) + p["marks"] / len(refs)
                    years.setdefault(r, set()).add(q["year"])
    return marks, years


def papers(qs, all_items, pos, tags, cfg):
    """Each paper's questions as marking-point slots over item indexes, with their group in the paper structure."""
    by_year = {}
    if cfg.get("paragraphs"):
        import math
        vec = {sid: {w for _, t, _ in rows for w in tok(t)} for sid, (_, rows) in all_items.items()}
        df = {}
        for ws in vec.values():
            for w in ws:
                df[w] = df.get(w, 0) + 1
        idf = {w: math.log(len(vec) / d) for w, d in df.items()}
    if cfg.get("split"):  # a choice of titles inside one question: each title is a question of its own
        qs = [q for q0 in qs for q in ([q0] if cfg["question"](q0)[0] == "docs" else [{**q0, "parts": [p]} for p in q0["parts"]])]
    untagged = set()  # years with questions a point-tagged subject hasn't tagged yet (e.g. a new paper)
    for q in qs:
        slots = []
        if tags and q["id"] not in tags and not cfg.get("paragraphs"):
            untagged.add(q["year"])
        for p in q["parts"]:
            if cfg.get("paragraphs") and q["id"] not in tags:
                slots += paragraph_slots(p, all_items, pos, idf, vec)
                continue
            tagged = tags.get(q["id"], {}).get(p["label"])
            if tagged is not None:
                for s in tagged:
                    slots.append([p["marks"] / len(tagged), s["k"], [pos[i] for i in s["of"]]])
                # the same marks again, spread over every point of the subsections the tags fall in (k = 0 means
                # "spread"). The page blends the two, because new papers ask other points of the same topics.
                subs_hit = sorted({i.split(".")[0] for s in tagged for i in s["of"]})
                if subs_hit:
                    slots.append([p["marks"], 0, [pos[i] for r in subs_hit for i, _, _ in all_items[r][1]]])
                # Tags on one study region (India) give the other regions (Brazil) the same share, spread over their
                # points both ways (tagged-style and spread), so a student who picked the other region isn't short.
                on_region = [s for s in tagged if any(cfg["track"](i.split(".")[0]).startswith("region:") for i in s["of"])]
                for r in {i.split(".")[0] for s in on_region for i in s["of"]}:
                    for alt in variants([r], cfg["track"])[1:]:
                        pts = [pos[i] for i, _, _ in all_items[alt[0]][1]]
                        m = p["marks"] * len(on_region) / len(tagged)
                        slots += [[m / len(pts), 1, [i]] for i in pts] + [[m, 0, pts]]
            else:
                for refs in variants(p.get("notesRefs") or [], cfg["track"]):
                    pts = [pos[i] for r in refs if r in all_items for i, _, _ in all_items[r][1]]
                    slots += [[p["marks"] / len(pts), 1, [i]] for i in pts]
        if slots:
            g, need = cfg["question"](q)
            by_year.setdefault(q["year"], []).append({"g": g, **({"need": need} if need else {}),
                                                      "slots": [[round(m, 4), k, o] for m, k, o in slots]})
    # An untagged year is marked the fallback way (every point of its subsections), far harsher than tagged years:
    # the page trains on it but doesn't use it as a backtest year (crunchBacktest).
    return [{"year": y, "qs": by_year[y], **({"untagged": True} if y in untagged else {})} for y in sorted(by_year)]


def main(subject):
    all_items = items(subject)
    points = json.loads((ROOT / "content" / "crunch" / f"{subject}-points.json").read_text())
    index_js = (ROOT / "subject-index.js").read_text()
    cfg = SUBJECTS[subject]
    chap = lambda sid: sid.rsplit("-s", 1)[0]
    chapter_ids = sorted({chap(sid) for sid in all_items}, key=lambda c: index_js.index('"id":"%s"' % c))
    chapters = []
    for c in chapter_ids:
        m = re.search(r'\{"id":"%s","title":"([^"]+)"' % c, index_js)
        chapters.append([c, m.group(1) if m else c])
    ch_index = {c: i for i, (c, _) in enumerate(chapters)}
    sids = sorted(all_items, key=lambda s: (ch_index[chap(s)], int(s.rsplit("-s", 1)[1])))
    ALL_SIDS[:] = sids
    qs = higher_questions(subject)
    marks, years = exam_marks(qs, cfg["track"])
    subs, rows = [], []
    for si, sid in enumerate(sids):
        title, its = all_items[sid]
        subs.append([sid, title, ch_index[chap(sid)], round(marks.get(sid, 0), 2), sorted(years.get(sid, [])), cfg["track"](sid)])
        for iid, text, h in its:
            p = points[iid]
            assert p["hash"] == h, f"{iid} text changed since it was rated; re-run that package"
            rows.append([iid, si, p["cost"], text])
    pos = {r[0]: i for i, r in enumerate(rows)}
    links = [[pos[iid], pos[l["id"]], 1 if l["strength"] == "essential" else 0]
             for iid, *_ in rows for l in points[iid]["needs"]]
    tag_file = ROOT / "content" / "crunch" / f"{subject}-exam-tags.json"
    tags = json.loads(tag_file.read_text()) if tag_file.exists() else {}
    paper_list = papers(qs, all_items, pos, tags, cfg)
    out = ROOT / "drafts" / "crunch" / subject / "map"
    out.mkdir(parents=True, exist_ok=True)
    (out / "data.json").write_text(json.dumps(
        {"subject": subject, "chapters": chapters, "subs": subs, "items": rows, "links": links, "papers": paper_list,
         "groups": cfg["groups"], "picks": cfg.get("picks", {}), "pickCount": cfg.get("pickCount", {}), "aac": AAC.get(subject)},
        ensure_ascii=False, separators=(",", ":")))
    print(f"{len(rows)} items, {len(links)} links, {len(subs)} subsections, {len(chapters)} chapters, "
          f"{len(paper_list)} papers ({len(tags)} questions tagged to points) → {out / 'data.json'}")


if __name__ == "__main__":
    main(sys.argv[1])
