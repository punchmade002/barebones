import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-76.txt', encoding='utf-8').read()
blocks = batch.split('QUESTION ')[1:]
for b in blocks:
    qid = b.split()[0]
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    data = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    n = 0; empty = []
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for mp in mps:
            n += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            assert len(mp['of']) <= 2, (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', n, 'empty', empty)
