import json, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-54.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"

text = open(BATCH, encoding="utf-8").read()
blocks = re.split(r"\n=+\n", text)
qs = {}
for b in blocks:
    m = re.search(r"QUESTION (\S+)", b)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r"^\[([^\]]+)\]", b, re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    qs[qid] = (cands, labels)

ok = True
for qid, (cands, labels) in qs.items():
    path = OUT + qid + ".json"
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print(qid, "PARSE FAIL", e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, "LABEL MISMATCH", list(data.keys()), labels); ok = False
    n = 0
    empty = []
    for part, pts in data.items():
        if not pts:
            empty.append(part)
        for p in pts:
            n += 1
            if not (1 <= p["k"] <= len(p["of"])):
                print(qid, part, "BAD k", p); ok = False
            for i in p["of"]:
                if i not in cands:
                    print(qid, part, "UNKNOWN ID", i); ok = False
    print(qid, "parts", len(data), "marking points", n, "empty", empty)
print("OK" if ok else "FAILURES")
