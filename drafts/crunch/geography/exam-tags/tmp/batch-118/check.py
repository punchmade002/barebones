import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-118.txt', encoding='utf-8').read()
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
blocks = [b for b in batch.split('\n====') if b.strip()]
ok = True
for q in ['geography-pp-2026-higher-q122', 'geography-pp-2026-higher-q123', 'geography-pp-2026-higher-q124']:
    qid = q
    block = next(b for b in re.split(r'=+\n', batch) if ('QUESTION ' + qid) in b)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    d = json.load(open(out + qid + '.json', encoding='utf-8'))
    if list(d.keys()) != labels:
        print(qid, 'label mismatch', list(d.keys()), labels); ok = False
    n = 0; empty = []
    for lab, pts in d.items():
        if not pts: empty.append(lab)
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])): print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cands: print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(d), 'points', n, 'empty', empty, 'candidates', len(cands))
print('OK' if ok else 'FAIL')
