import json, re
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-113.txt').read()
cands = set(re.findall(r'^\[([^\]]+)\]', batch, re.M))
labels = re.findall(r'^PART "([^"]+)"', batch, re.M)
d = json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2026-higher-q109.json'))
assert list(d.keys()) == labels, (list(d.keys()), labels)
n = 0
for part, mps in d.items():
    for mp in mps:
        n += 1
        assert 1 <= mp['k'] <= len(mp['of']), (part, mp)
        assert len(mp['of']) <= 2, (part, mp)
        for i in mp['of']:
            assert i in cands, (part, i)
print('ok', {p: len(m) for p, m in d.items()}, 'total', n)
