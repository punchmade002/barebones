import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-51.txt', encoding='utf-8').read()
for block in batch.split('\n' + '=' * 40):
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    empty = []
    for lab, pts in data.items():
        if not pts:
            empty.append(lab)
        for p in pts:
            total += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            for i in p['of']:
                assert i in cands, (qid, lab, i)
    print(qid, len(labels), total, empty)
