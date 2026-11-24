"""Tag each Higher Level exam part to the note points that earn its marks (Crunch Mode, see CRUNCH_MODE.md).

    python3 scripts/crunch_exam_tags.py biology          # one package per question → drafts/crunch/<subject>/exam-tags/packages/
    python3 scripts/crunch_exam_tags.py biology merge    # check agent output → content/crunch/<subject>-exam-tags.json
    python3 scripts/crunch_exam_tags.py geography short  # cheap mode: shortlisted candidates, ~50 KB batches of questions
                                                         # → exam-tags/batches/batch-NN.txt + batches.json

Cheap mode shows each question only the note points that share the most distinctive words (idf-weighted) with
each line of its model answer: the top 8 per line (4 for parts of 20+ marks). Tested on Biology's Sonnet tags: 91% of marking points keep
at least one of their tagged points, from 12% of the candidates. A missed point just leaves that marking point
untagged, and the map's spread share still covers its subsection.

Agent output, one file per question (exam-tags/out/<question id>.json):
    {"<part label>": [{"k": 1, "of": ["bio11-s7.0.2"]}, {"k": 3, "of": [five ids]}], ...}
Each entry is one marking point: the student earns it by knowing any k of the listed points.
An empty list means the notes don't cover that part.
"""
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crunch_points import ROOT, items


def questions(subject):
    s = (ROOT / f"{subject}-exam-questions.js").read_text()
    return [q for q in json.loads(s[s.index("[", s.index("concat(")):s.rindex("]") + 1]) if q.get("level") == "higher"]


def package(q, all_items):
    refs = sorted({r for p in q["parts"] for r in p.get("notesRefs") or [] if r in all_items})
    lines = [f"QUESTION {q['id']} ({q['source']}, {q['totalMarks']} marks)", ""]
    for p in q["parts"]:
        lines += [f"PART {p['label']} ({p['marks']} marks) subsections: {', '.join(p.get('notesRefs') or []) or 'none'}",
                  f"MODEL ANSWER: {p['model']}", ""]
    for sid in refs:
        title, rows = all_items[sid]
        lines += [f"CANDIDATES {sid}: {title}"] + [f"[{i}] {t}" for i, t, _ in rows] + [""]
    return "\n".join(lines), refs


STOP = set("the and for that with this from are was were which their they them into than then there these those what "
           "when where will would also can has have had its not but all any each other such more most some been being one "
           "two three per via use used using does did how why who whom your you our out over under about between because "
           "only very".split())


def tok(t):
    return [w for w in re.findall(r"[a-z0-9]+", t.lower()) if len(w) > 2 and w not in STOP]


def shortlister(all_items, top=8, top_long=4):
    """part -> the candidate ids worth showing: for each model-answer line, its `top` best word matches
    (`top_long` for parts of 20+ marks, whose 40-line answers would otherwise show nearly the whole subsection)."""
    df, n = {}, 0
    for _, rows in all_items.values():
        for _, t, _ in rows:
            n += 1
            for w in set(tok(t)):
                df[w] = df.get(w, 0) + 1
    idf = {w: math.log(n / d) for w, d in df.items()}

    def short(part):
        pts = [(i, set(tok(t))) for r in part.get("notesRefs") or [] if r in all_items for i, t, _ in all_items[r][1]]
        keep = set()
        for line in re.split(r"\n|(?<=[.;])\s+", part.get("model") or ""):
            lw = set(tok(line))
            if not lw:
                continue
            ranked = sorted(((sum(idf.get(w, 0) for w in lw & ws) / math.sqrt(len(ws) or 1), i) for i, ws in pts), reverse=True)
            keep |= {i for sc, i in ranked[:top if part["marks"] < 20 else top_long] if sc > 0}
        return keep
    return short


def short_package(q, all_items, short):
    lines = [f"QUESTION {q['id']} ({q['source']}, {q['totalMarks']} marks)", ""]
    keep = set()
    for p in q["parts"]:
        lines += [f"PART \"{p['label']}\" ({p['marks']} marks)", f"MODEL ANSWER: {p.get('model') or '(none)'}", ""]
        keep |= short(p)
    lines.append("CANDIDATES (shortlist):")
    lines += [f"[{i}] {t}" for _, rows in all_items.values() for i, t, _ in rows if i in keep]  # notes order
    return "\n".join(lines) + "\n"


def batches(subject, budget=60_000):
    """Questions in paper order, short ones together and long ones together, packed into batches of up to `budget` bytes."""
    all_items = items(subject)
    short = shortlister(all_items)
    out = ROOT / "drafts" / "crunch" / subject / "exam-tags" / "batches"
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("batch-*.txt"):
        f.unlink()
    qs = sorted(questions(subject), key=lambda q: (q["totalMarks"] > 20, q["year"], q.get("questionNumber", 0)))
    groups, cur, size, kind = [], [], 0, None
    for q in qs:
        text = short_package(q, all_items, short)
        k = q["totalMarks"] > 20
        if cur and (size + len(text) > budget or k != kind or len(cur) >= 12):
            groups.append(cur)
            cur, size = [], 0
        cur.append((q["id"], text))
        size += len(text)
        kind = k
    groups.append(cur)
    index = {}
    for n, g in enumerate(groups, 1):
        name = f"batch-{n:02d}"
        (out / f"{name}.txt").write_text(("\n" + "=" * 40 + "\n\n").join(t for _, t in g))
        index[name] = [qid for qid, _ in g]
    (out.parent / "batches.json").write_text(json.dumps(index, indent=0))
    sizes = sorted((out / f"{k}.txt").stat().st_size for k in index)
    print(f"{len(index)} batches for {len(qs)} questions, median {sizes[len(sizes) // 2] // 1000} KB, largest {sizes[-1] // 1000} KB")


def check(q, cands, result):
    labels = [p["label"] for p in q["parts"]]
    errs = [f"missing part {l}" for l in labels if l not in result]
    errs += [f"extra part {l}" for l in result if l not in labels]
    for label, slots in result.items():
        if not isinstance(slots, list):
            errs.append(f"{label} not a list")
            continue
        for s in slots:
            of = s.get("of") if isinstance(s, dict) else None
            if not of or not isinstance(s.get("k"), int) or not 1 <= s["k"] <= len(of):
                errs.append(f"{label} bad slot {s}")
            else:
                errs += [f"{label} unknown point {i}" for i in of if i not in cands]
    return errs


def main(subject):
    all_items = items(subject)
    out = ROOT / "drafts" / "crunch" / subject / "exam-tags" / "packages"
    out.mkdir(parents=True, exist_ok=True)
    sizes = []
    for q in questions(subject):
        text, _ = package(q, all_items)
        (out / f"{q['id']}.txt").write_text(text)
        sizes.append(len(text))
    sizes.sort()
    print(f"{len(sizes)} packages, median {sizes[len(sizes) // 2] // 1000} KB, largest {sizes[-1] // 1000} KB, total {sum(sizes) // 1000} KB")


def merge(subject):
    all_items = items(subject)
    src = ROOT / "drafts" / "crunch" / subject / "exam-tags" / "out"
    merged, todo, bad = {}, [], {}
    for q in questions(subject):
        f = src / f"{q['id']}.json"
        if not f.exists():
            todo.append(q["id"])
            continue
        _, refs = package(q, all_items)
        cands = {i for sid in refs for i, _, _ in all_items[sid][1]}
        result = json.loads(f.read_text())
        errs = check(q, cands, result)
        if errs:
            bad[q["id"]] = errs
        else:
            merged[q["id"]] = result
    print(f"{len(merged)} questions merged, {len(todo)} not done, {len(bad)} with problems")
    for qid, errs in bad.items():
        print(f"  {qid}: {errs[:3]}{' …' if len(errs) > 3 else ''}")
    (ROOT / "content" / "crunch" / f"{subject}-exam-tags.json").write_text(json.dumps(merged, indent=0) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    q = {"parts": [{"label": "(a)"}, {"label": "(b)"}]}
    assert check(q, {"x", "y"}, {"(a)": [{"k": 1, "of": ["x"]}], "(b)": []}) == []
    assert len(check(q, {"x"}, {"(a)": [{"k": 2, "of": ["x"]}, {"k": 1, "of": ["z"]}]})) == 3  # bad k, unknown z, missing (b)
    assert tok("The Rivers, of Ireland") == ["rivers", "ireland"]
    sys.exit(merge(sys.argv[1]) if "merge" in sys.argv else batches(sys.argv[1]) if "short" in sys.argv else main(sys.argv[1]))
