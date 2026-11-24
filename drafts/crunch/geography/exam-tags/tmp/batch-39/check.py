import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-39.txt', encoding='utf-8').read()
# split questions
qs = re.split(r'^QUESTION ', batch, flags=re.M)[1:]
for q in qs:
    qid = q.split()[0]
    cands = set(re.findall(r'^\[([^\]]+)\]', q, flags=re.M))
    labels = re.findall(r'^PART "([^"]+)"', q, flags=re.M)
    d = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    assert list(d.keys()) == labels, (qid, list(d.keys()), labels)
    total = 0; empty = []
    for lab, mps in d.items():
        if not mps: empty.append(lab)
        for mp in mps:
            total += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'mps', total, 'empty', empty)
