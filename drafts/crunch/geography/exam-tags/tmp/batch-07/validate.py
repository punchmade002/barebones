import json, os, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-07.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out"

text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in text.split("=" * 40) if "QUESTION " in b]

ok = True
for b in blocks:
    qid = re.search(r"QUESTION (\S+)", b).group(1)
    labels = re.findall(r'PART "([^"]+)"', b)
    cands = set(re.findall(r"^\[([^\]]+)\]", b.split("CANDIDATES (shortlist):")[1], re.M))
    path = os.path.join(OUT, qid + ".json")
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print(qid, "PARSE FAIL", e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, "LABEL MISMATCH", list(data.keys()), labels); ok = False
    npts = 0
    for lab, pts in data.items():
        for p in pts:
            npts += 1
            k, of = p["k"], p["of"]
            if not (1 <= k <= len(of)):
                print(qid, lab, "BAD k", p); ok = False
            for i in of:
                if i not in cands:
                    print(qid, lab, "BAD ID", i); ok = False
    empty = [lab for lab, pts in data.items() if not pts]
    print(qid, len(labels), npts, empty)

print("ALL OK" if ok else "PROBLEMS")
