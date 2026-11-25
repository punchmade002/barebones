import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
batch = open(base + 'batches/batch-87.txt', encoding='utf-8').read()
questions = re.split(r'\n=+\n', batch)
for q in questions:
    m = re.search(r'QUESTION (\S+)', q)
    if not m: continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', q, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', q, re.M))
    data = json.load(open(base + 'out/' + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0; empty = []
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for mp in mps:
            total += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
