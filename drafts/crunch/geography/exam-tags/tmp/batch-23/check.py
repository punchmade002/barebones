import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-23.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = [b for b in text.split('\n====')]  # question blocks
ok = True
for qid in ['geography-pp-2018-higher-q103', 'geography-pp-2018-higher-q104']:
    blk = next(b for b in blocks if ('QUESTION ' + qid + ' ') in b)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0; empty = []
    for lab, pts in data.items():
        if not pts: empty.append(lab)
        for p in pts:
            total += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            assert len(p['of']) <= 2, (qid, lab, p)
            for i in p['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'points', total, 'empty', empty, 'cands', len(cands))
