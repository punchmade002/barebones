import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-92.txt').read()
cands = set(re.findall(r'^\[([^\]]+)\]', batch, re.M))
labels = re.findall(r'^PART "([^"]+)"', batch, re.M)
qid = 'geography-pp-2024-higher-q108'
d = json.load(open(f'/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/{qid}.json'))
assert list(d.keys()) == labels, (list(d.keys()), labels)
n = 0
for part, mps in d.items():
    for mp in mps:
        n += 1
        assert 1 <= mp['k'] <= len(mp['of']), (part, mp)
        for i in mp['of']:
            assert i in cands, (part, i)
    print(part, len(mps))
print('parts', len(d), 'marking points', n, 'empty', [p for p, m in d.items() if not m])
