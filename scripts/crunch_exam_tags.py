"""Tag each Higher Level exam part to the note points that earn its marks (Crunch Mode, see CRUNCH_MODE.md).

    python3 scripts/crunch_exam_tags.py biology          # one package per question → drafts/crunch/<subject>/exam-tags/packages/
    python3 scripts/crunch_exam_tags.py biology merge    # check agent output → content/crunch/<subject>-exam-tags.json

Agent output, one file per question (exam-tags/out/<question id>.json):
    {"<part label>": [{"k": 1, "of": ["bio11-s7.0.2"]}, {"k": 3, "of": [five ids]}], ...}
Each entry is one marking point: the student earns it by knowing any k of the listed points.
An empty list means the notes don't cover that part.
"""
import json
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
    sys.exit(merge(sys.argv[1]) if "merge" in sys.argv else main(sys.argv[1]))
