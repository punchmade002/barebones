import json, re, sys
BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-41.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"
text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in text.split("=" * 40) if "QUESTION " in b]
ok = True
for b in blocks:
    qid = re.search(r"^QUESTION (\S+)", b, re.M).group(1)
    cands = set(re.findall(r"^\[([^\]]+)\]", b, re.M))
    labels = re.findall(r'^PART "(.+?)"', b, re.M)
    path = OUT + qid + ".json"
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print("PARSE FAIL", qid, e); ok = False; continue
    if list(data.keys()) != labels:
        print("LABEL MISMATCH", qid, list(data.keys()), labels); ok = False
    total = 0; empty = []
    for part, pts in data.items():
        if not pts: empty.append(part)
        for p in pts:
            total += 1
            of = p["of"]
            if not (1 <= p["k"] <= len(of)):
                print("BAD K", qid, part, p); ok = False
            for i in of:
                if i not in cands:
                    print("BAD ID", qid, part, i); ok = False
    print(qid, "parts", len(labels), "points", total, "empty", empty)
print("ALL OK" if ok else "PROBLEMS")
