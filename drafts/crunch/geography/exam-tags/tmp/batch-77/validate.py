import json, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-77.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"

text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in text.split("=" * 40) if "QUESTION " in b]
ok = True
for b in blocks:
    qid = re.search(r"QUESTION (\S+)", b).group(1)
    labels = re.findall(r'PART "([^"]+)"', b)
    cands = set(re.findall(r"^\[([^\]]+)\]", b, re.M))
    path = OUT + qid + ".json"
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print(qid, "PARSE FAIL", e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, "LABEL MISMATCH", list(data.keys()), labels); ok = False
    mp = 0
    empty = []
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for m in mps:
            mp += 1
            of = m["of"]
            if not (1 <= m["k"] <= len(of)): print(qid, lab, "BAD K", m); ok = False
            if len(of) > 2: print(qid, lab, "TOO MANY IDS", m); ok = False
            for i in of:
                if i not in cands: print(qid, lab, "BAD ID", i); ok = False
    print(qid, "parts", len(labels), "marking points", mp, "empty", empty)
print("ALL OK" if ok else "PROBLEMS")
