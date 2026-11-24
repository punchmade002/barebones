import json, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-46.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"

text = open(BATCH, encoding="utf-8").read()
blocks = re.split(r"^=+\s*$", text, flags=re.M)
ok = True
for block in blocks:
    m = re.search(r"^QUESTION (\S+)", block, flags=re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)" \((\d+) marks?\)', block, flags=re.M)
    cands = set(re.findall(r"^\[([^\]]+)\]", block, flags=re.M))
    data = json.load(open(OUT + qid + ".json", encoding="utf-8"))
    labels = [p[0] for p in parts]
    if list(data.keys()) != labels:
        print(qid, "LABEL MISMATCH", list(data.keys()), labels); ok = False
    for label, marks in parts:
        pts = data.get(label)
        if pts is None:
            continue
        if len(pts) > int(marks) // 2:
            print(qid, label, "too many points", len(pts)); ok = False
        for p in pts:
            if not (1 <= p["k"] <= len(p["of"])):
                print(qid, label, "bad k", p); ok = False
            for i in p["of"]:
                if i not in cands:
                    print(qid, label, "unknown id", i); ok = False
    total = sum(len(v) for v in data.values())
    empty = [k for k, v in data.items() if not v]
    print(qid, "parts", len(parts), "points", total, "empty", empty)
print("OK" if ok else "FAILURES")
