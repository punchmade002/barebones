import json, re, sys
B = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-11.txt"
O = "/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/"
text = open(B, encoding="utf-8").read()
qs = {}
cur = None
for line in text.splitlines():
    m = re.match(r"QUESTION (\S+)", line)
    if m:
        cur = m.group(1); qs[cur] = {"parts": [], "cands": set()}; continue
    if cur is None: continue
    p = re.match(r'PART "([^"]+)"', line)
    if p: qs[cur]["parts"].append(p.group(1))
    c = re.match(r"\[([^\]]+)\]", line)
    if c: qs[cur]["cands"].add(c.group(1))
ok = True
for q, info in qs.items():
    d = json.load(open(O + q + ".json", encoding="utf-8"))
    if list(d.keys()) != info["parts"]:
        print(q, "PART MISMATCH", list(d.keys()), info["parts"]); ok = False
    n = 0; empty = []
    for part, mps in d.items():
        if not mps: empty.append(part)
        for mp in mps:
            n += 1
            if not (1 <= mp["k"] <= len(mp["of"])): print(q, part, "bad k", mp); ok = False
            if len(mp["of"]) > 2 and True: pass
            for i in mp["of"]:
                if i not in info["cands"]: print(q, part, "bad id", i); ok = False
    print(q, "parts", len(d), "mps", n, "empty", empty)
print("OK" if ok else "FAIL")
