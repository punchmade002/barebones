import json, re, sys
B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
batch = open(B + 'batches/batch-112.txt', encoding='utf-8').read()
qs = batch.split('QUESTION ')[1:]
labels_expected = {}
cands = {}
for q in qs:
    qid = q.split()[0]
    labels = re.findall(r'PART "([^"]+)"', q)
    labels_expected[qid] = labels
    cands[qid] = set(re.findall(r'^\[([^\]]+)\]', q, re.M))
ok = True
for qid, labels in labels_expected.items():
    d = json.load(open(B + 'out/geography-pp-2026-higher-' + qid.split('-')[-1] + '.json', encoding='utf-8'))
    if list(d.keys()) != labels:
        print('LABEL MISMATCH', qid, list(d.keys()), labels); ok = False
    n = 0
    for part, pts in d.items():
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])): print('K BAD', qid, part, p); ok = False
            for i in p['of']:
                if i not in cands[qid]: print('BAD ID', qid, part, i); ok = False
    print(qid, 'parts', len(d), 'points', n, 'empty', [k for k, v in d.items() if not v])
print('OK' if ok else 'FAIL')
