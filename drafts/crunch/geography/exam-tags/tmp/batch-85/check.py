import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-85.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = text.split('=' * 40)
for b in blocks:
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    empty = []
    for lab, pts in data.items():
        if not pts:
            empty.append(lab)
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            for i in p['of']:
                assert i in cands, (qid, lab, i)
        total += len(pts)
    print(qid, 'parts', len(labels), 'points', total, 'empty', empty)
