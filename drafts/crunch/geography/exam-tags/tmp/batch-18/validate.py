import json, re, sys
BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-18.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"
text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in text.split("\n====") if b.strip()]
ok = True
for b in blocks:
    m = re.search(r"^QUESTION (\S+)", b, re.M)
    qid = m.group(1)
    cands = set(re.findall(r"^\[([^\]]+)\]", b, re.M))
    parts = re.findall(r'^PART "([^"]+)"', b, re.M)
    try:
        data = json.load(open(OUT + qid + ".json", encoding="utf-8"))
    except Exception as e:
        print(qid, "PARSE FAIL", e); ok = False; continue
    if list(data.keys()) != parts:
        print(qid, "label mismatch", list(data.keys()), parts); ok = False
    mp = 0; empty = []
    for p, mps in data.items():
        if not mps: empty.append(p)
        for mpt in mps:
            mp += 1
            k, of = mpt["k"], mpt["of"]
            if not (1 <= k <= len(of)): print(qid, p, "bad k", mpt); ok = False
            for i in of:
                if i not in cands: print(qid, p, "id not in candidates", i); ok = False
    print(qid, "parts", len(parts), "marking points", mp, "empty", empty)
print("OK" if ok else "FAILURES")
