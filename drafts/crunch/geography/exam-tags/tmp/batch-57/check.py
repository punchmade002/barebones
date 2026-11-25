import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-57.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
qs = re.split(r'^=+$', text, flags=re.M)
ok = True
for q in qs:
    m = re.search(r'^QUESTION (\S+)', q, re.M)
    if not m: continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', q, re.M))
    labels = re.findall(r'^PART "([^"]+)"', q, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    for lab, mps in data.items():
        for mp in mps:
            k, of = mp['k'], mp['of']
            if not (1 <= k <= len(of)): print(qid, lab, 'bad k', mp); ok = False
            for i in of:
                if i not in cands: print(qid, lab, 'bad id', i); ok = False
    print(qid, 'parts', len(labels), 'mps', sum(len(v) for v in data.values()), 'empty', [l for l, v in data.items() if not v])
print('OK' if ok else 'FAIL')
