import json, re, sys
batch = open('batches/batch-09.txt', encoding='utf-8').read()
out = 'out/'
blocks = [b for b in batch.split('='*40) if 'QUESTION' in b]
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    parts = re.findall(r'^PART "([^"]*)"', b, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == parts, (qid, list(data.keys()), parts)
    pts = 0; empty = []
    for label, mps in data.items():
        if not mps: empty.append(label)
        for mp in mps:
            pts += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, label, mp)
            for i in mp['of']:
                assert i in cands, (qid, label, i)
    print(qid, 'parts', len(parts), 'points', pts, 'empty', empty)
