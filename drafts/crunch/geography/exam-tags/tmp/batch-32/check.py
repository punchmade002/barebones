import json, os, re

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-32.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out"

text = open(BATCH, encoding="utf-8").read()
blocks = re.split(r"^=+\s*$", text, flags=re.M)
ok = True
for block in blocks:
    m = re.search(r"^QUESTION (\S+)", block, flags=re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, flags=re.M)
    cands = set(re.findall(r"^\[(geo-[^\]]+)\]", block, flags=re.M))
    path = os.path.join(OUT, qid + ".json")
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print(qid, "PARSE FAIL", e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, "LABEL MISMATCH", list(data.keys()), labels); ok = False
    mp = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            mp += 1
            of = p["of"]
            if not (1 <= p["k"] <= len(of)):
                print(qid, label, "BAD k", p); ok = False
            if len(of) > 2:
                print(qid, label, "more than 2 ids", p); ok = False
            for i in of:
                if i not in cands:
                    print(qid, label, "UNKNOWN ID", i); ok = False
    print(qid, "parts", len(data), "marking points", mp, "empty", empty)
print("ALL OK" if ok else "PROBLEMS")
