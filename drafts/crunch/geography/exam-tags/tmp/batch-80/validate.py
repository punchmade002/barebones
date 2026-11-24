import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-80.txt', encoding='utf-8').read()
blocks = re.split(r'^QUESTION ', batch, flags=re.M)[1:]
for b in blocks:
    qid = b.split()[0]
    labels = re.findall(r'^PART "([^"]+)"', b, flags=re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, flags=re.M))
    data = json.load(open(f'/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/{qid}.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0; empty = []
    for lab, pts in data.items():
        if not pts: empty.append(lab)
        for p in pts:
            total += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            for i in p['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'points', total, 'empty', empty, 'OK')
