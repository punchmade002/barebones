import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-94.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
qs = re.split(r'^=+\s*$', text, flags=re.M)
ok = True
for block in qs:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m: continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print(qid, 'PART ORDER/LABEL MISMATCH', list(data.keys()), parts); ok = False
    mp = 0
    for lab, mps in data.items():
        for mpk in mps:
            k, of = mpk['k'], mpk['of']
            if not (1 <= k <= len(of)) or len(of) > 2:
                print(qid, lab, 'BAD k/of', mpk); ok = False
            for i in of:
                if i not in cands:
                    print(qid, lab, 'NOT IN CANDIDATES', i); ok = False
        mp += len(mps)
    print(qid, 'parts', len(parts), 'marking points', mp, 'empty', [l for l, v in data.items() if not v])
print('ALL OK' if ok else 'PROBLEMS')
