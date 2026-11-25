import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-30.txt', encoding='utf-8').read()
blocks = re.split(r'^=+\s*$', batch, flags=re.M)
ok = True
for blk in blocks:
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)" \((\d+) marks\)', blk, re.M)
    data = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    assert list(data.keys()) == [l for l, _ in labels], (qid, list(data.keys()), labels)
    total = 0
    for lab, pts in data.items():
        total += len(pts)
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, p)
            for i in p['of']:
                if i not in cands:
                    ok = False; print('BAD ID', qid, i)
        marks = int(dict(labels)[lab])
        assert len(pts) <= marks // 2, (qid, lab)
    print(qid, 'parts', len(data), 'points', total, 'empty', [k for k, v in data.items() if not v], 'cands', len(cands))
print('OK' if ok else 'FAILURES')
