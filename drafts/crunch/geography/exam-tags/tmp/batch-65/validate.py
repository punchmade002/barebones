import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-65.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
qs = re.split(r'^QUESTION ', text, flags=re.M)[1:]
ok = True
for q in qs:
    qid = q.split()[0]
    labels = re.findall(r'^PART "([^"]+)"', q, flags=re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', q, flags=re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    counts = {}
    for lab, pts in data.items():
        counts[lab] = len(pts)
        for p in pts:
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print(qid, lab, 'bad k', p); ok = False
            for i in of:
                if i not in cands:
                    print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'points', sum(counts.values()), 'empty', [l for l,c in counts.items() if c == 0])
print('OK' if ok else 'FAIL')
