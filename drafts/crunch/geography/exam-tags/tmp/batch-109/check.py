import json, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-109.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"

text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in re.split(r"^=+\s*$", text, flags=re.M) if "QUESTION " in b]

ok = True
for b in blocks:
    qid = re.search(r"^QUESTION (\S+)", b, re.M).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r"^\[([^\]]+)\]", b, re.M))
    data = json.load(open(OUT + qid + ".json", encoding="utf-8"))
    if list(data.keys()) != labels:
        print(qid, "label mismatch", list(data.keys()), labels); ok = False
    mp_total = 0
    empty = []
    for lab in labels:
        mps = data.get(lab, [])
        if not mps:
            empty.append(lab)
        for mp in mps:
            mp_total += 1
            if not (1 <= mp["k"] <= len(mp["of"])):
                print(qid, lab, "bad k", mp); ok = False
            for i in mp["of"]:
                if i not in cands:
                    print(qid, lab, "id not in candidates", i); ok = False
    print(qid, "parts", len(labels), "marking points", mp_total, "empty", empty)
print("OK" if ok else "FAILED")
