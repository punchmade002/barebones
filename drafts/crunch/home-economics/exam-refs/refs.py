"""Home Ec exam parts -> the note subsections they test (notesRefs), which the bank doesn't have yet.

    python3 drafts/crunch/home-economics/exam-refs/refs.py build   # -> batch-<n>.txt, one package per ~20 HL questions
    python3 drafts/crunch/home-economics/exam-refs/refs.py merge   # out-<n>.json -> content/crunch/home-economics-exam-refs.json

The other subjects got notesRefs from the exam-bank rebuild's scan; Home Ec hasn't been rebuilt. crunch_map.py reads
this file for parts without notesRefs. Drop it once the rebuilt bank carries its own.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BUDGET = 40_000


def higher():
    s = (ROOT / "home-economics-exam-questions.js").read_text()
    return [q for q in json.loads(s[s.index("[", s.index("concat(")):s.rindex("]") + 1]) if "-HI-" in q["id"]]


def build():
    batches, cur, size = [], [], 0
    for q in higher():
        block = [f"QUESTION {q['id']} ({q['source']}; filed under {q['chapterId']})"]
        for p in q["parts"]:
            block.append(f"PART {p['label'] or '(whole)'} [{p['marks']} marks]\n  Q: {p['question'].strip()}\n  A: {(p.get('model') or '').strip()}")
        text = "\n".join(block)
        if cur and size + len(text) > BUDGET:
            batches.append(cur)
            cur, size = [], 0
        cur.append(text)
        size += len(text)
    batches.append(cur)
    for f in HERE.glob("batch-*.txt"):
        f.unlink()
    for n, b in enumerate(batches, 1):
        (HERE / f"batch-{n}.txt").write_text("\n\n".join(b) + "\n")
    print(f"{len(batches)} batches, {sum(map(len, batches))} questions")


def merge():
    sids = {l.split(" | ")[0] for l in (HERE.parent / "catalogue.txt").read_text().splitlines() if " | " in l}
    want = {q["id"]: [p["label"] or "(whole)" for p in q["parts"]] for q in higher()}
    refs, errs = {}, []
    for f in sorted(HERE.glob("out-*.json")):
        for qid, parts in json.loads(f.read_text()).items():
            if qid not in want:
                errs.append(f"{f.name}: unknown question {qid}")
                continue
            for label, rs in parts.items():
                bad = [r for r in rs if r not in sids]
                if label not in want[qid] or bad or not rs:
                    errs.append(f"{f.name}: {qid} {label} {bad or 'empty or unknown label'}")
                    continue
                refs.setdefault(qid, {})["" if label == "(whole)" else label] = rs
    missing = [(q, l) for q, ls in want.items() for l in ls if ("" if l == "(whole)" else l) not in refs.get(q, {})]
    (ROOT / "content" / "crunch" / "home-economics-exam-refs.json").write_text(json.dumps(refs, indent=0))
    print(f"{sum(map(len, refs.values()))} parts tagged, {len(missing)} missing, {len(errs)} problems")
    for e in errs[:20] + [f"missing {m}" for m in missing[:20]]:
        print(" ", e)


if __name__ == "__main__":
    {"build": build, "merge": merge}[sys.argv[1]]()
