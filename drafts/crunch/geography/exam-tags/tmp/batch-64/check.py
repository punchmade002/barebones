import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
batch = open(base + 'batches/batch-64.txt', encoding='utf-8').read()
blocks = batch.split('=' * 40)
for qid in ['geography-pp-2021-higher-q117', 'geography-pp-2021-higher-q118', 'geography-pp-2021-higher-q119']:
    blk = next(b for b in blocks if 'QUESTION ' + qid + ' ' in b)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(base + 'out/' + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    for lab, pts in data.items():
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, p)
            assert len(p['of']) <= 2, (qid, p)
            for i in p['of']:
                assert i in cands, (qid, i)
        total += len(pts)
        print(qid, lab, 'points', len(pts), 'empty' if not pts else '')
    print(qid, 'TOTAL', total, 'OK')
