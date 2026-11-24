import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-78.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = re.split(r'^QUESTION ', text, flags=re.M)[1:]
for b in blocks:
    qid = b.split()[0]
    cands = set(re.findall(r'^\[([^\]]+)\]', b, flags=re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, flags=re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0; empty = []
    for label, pts in data.items():
        if not pts: empty.append(label)
        for p in pts:
            total += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, label, p)
            for i in p['of']:
                assert i in cands, (qid, label, i)
    print(qid, 'parts', len(labels), 'points', total, 'empty', empty, 'cands', len(cands))
