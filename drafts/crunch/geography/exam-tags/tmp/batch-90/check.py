import json, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-90.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2024-higher-q106.json"
QID = "geography-pp-2024-higher-q106"

lines = open(BATCH, encoding="utf-8").read().splitlines()
ids = set()
parts = []
in_cand = False
for ln in lines:
    if ln.startswith("CANDIDATES"):
        in_cand = True
        continue
    if in_cand:
        m = re.match(r"^\[([^\]]+)\]", ln)
        if m:
            ids.add(m.group(1))
    m = re.match(r'^PART "([^"]+)"', ln)
    if m:
        parts.append(m.group(1))

data = json.load(open(OUT, encoding="utf-8"))
errors = []
if list(data.keys()) != parts:
    errors.append("part labels mismatch: %r vs %r" % (list(data.keys()), parts))
for label, mps in data.items():
    for mp in mps:
        k, of = mp["k"], mp["of"]
        if not (1 <= k <= len(of)):
            errors.append("%s bad k %r for %r" % (label, k, of))
        if len(of) > 2:
            errors.append("%s more than 2 ids without any-k rule: %r" % (label, of))
        for i in of:
            if i not in ids:
                errors.append("%s unknown id %s" % (label, i))
print("parts:", len(data), "marking points:", sum(len(v) for v in data.values()))
print("empty parts:", [l for l, v in data.items() if not v])
print("errors:", errors if errors else "none")
