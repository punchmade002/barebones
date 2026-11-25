import json, os, re, sys

BATCH = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-31.txt"
OUT = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out"

text = open(BATCH, encoding="utf-8").read()
blocks = [b for b in re.split(r"^=+\s*$", text, flags=re.M) if "QUESTION " in b]

for block in blocks:
    qid = re.search(r"^QUESTION (\S+)", block, re.M).group(1)
    cands = set(re.findall(r"^\[([^\]]+)\]", block, re.M))
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    path = os.path.join(OUT, qid + ".json")
    data = json.load(open(path, encoding="utf-8"))
    errors = []
    if list(data.keys()) != parts:
        errors.append("keys %r != parts %r" % (list(data.keys()), parts))
    total = 0
    empty = []
    for label, mps in data.items():
        if not mps:
            empty.append(label)
        for mp in mps:
            total += 1
            of = mp["of"]
            if not (1 <= mp["k"] <= len(of)):
                errors.append("%s bad k %r" % (label, mp))
            for i in of:
                if i not in cands:
                    errors.append("%s id not in candidates: %s" % (label, i))
    print(qid, "parts=%d" % len(parts), "marking_points=%d" % total,
          "empty=%s" % (empty if empty else "none"),
          "OK" if not errors else "ERRORS: " + "; ".join(errors))
