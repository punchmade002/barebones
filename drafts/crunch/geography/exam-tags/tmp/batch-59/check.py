import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-59.txt', encoding='utf-8').read()
qs = re.split(r'^=+\s*$', batch, flags=re.M)
for block in batch.split('\n=')[0:0]:
    pass
questions = {}
for chunk in re.split(r'\n={5,}\n', batch):
    m = re.search(r'^QUESTION (\S+)', chunk, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', chunk, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', chunk, re.M))
    questions[qid] = (labels, cands)
for qid, (labels, cands) in questions.items():
    d = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    assert list(d.keys()) == labels, (qid, list(d.keys()), labels)
    total = 0; empty = []
    for part, mps in d.items():
        if not mps: empty.append(part)
        for mp in mps:
            assert 1 <= mp['k'] <= len(mp['of']), (qid, part, mp)
            assert all(i in cands for i in mp['of']), (qid, part, mp)
            total += 1
    print(qid, len(labels), total, empty)
