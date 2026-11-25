import json, re, sys
batch = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-28.txt"
out = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2018-higher-q111.json"
text = open(batch, encoding="utf-8").read()
labels = re.findall(r'^PART "([^"]+)"', text, re.M)
cands = set(re.findall(r'^\[([^\]]+)\]', text, re.M))
data = json.load(open(out, encoding="utf-8"))
errs = []
if list(data.keys()) != labels: errs.append(f"label mismatch: {list(data.keys())} vs {labels}")
for lab, mps in data.items():
    for mp in mps:
        if not (1 <= mp["k"] <= len(mp["of"])): errs.append(f"{lab}: bad k {mp}")
        if len(mp["of"]) > 2: errs.append(f"{lab}: >2 ids {mp}")
        for i in mp["of"]:
            if i not in cands: errs.append(f"{lab}: unknown id {i}")
    if len(mps) > 15: errs.append(f"{lab}: too many MPs")
print("labels:", len(labels), "errors:", errs or "none")
print("MP counts:", {k: len(v) for k, v in data.items()})
print("empty:", [k for k, v in data.items() if not v])
