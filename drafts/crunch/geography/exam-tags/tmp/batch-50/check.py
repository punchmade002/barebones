import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-50.txt', encoding='utf-8').read()
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
for qid in ['geography-pp-2020-higher-q109', 'geography-pp-2020-higher-q110']:
    qblock = batch.split('QUESTION ' + qid, 1)[1].split('\n=', 1)[0]
    labels = re.findall(r'^PART "([^"]+)"', qblock, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', qblock, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    mp = 0; empty = []
    for part, pts in data.items():
        if not pts: empty.append(part)
        for p in pts:
            mp += 1
            assert 1 <= p['k'] <= len(p['of']) and len(p['of']) <= 2, (qid, part, p)
            for i in p['of']:
                assert i in cands, (qid, part, i)
    print(qid, 'parts', len(labels), 'marking points', mp, 'empty', empty)
