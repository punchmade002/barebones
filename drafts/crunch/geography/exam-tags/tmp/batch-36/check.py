import json, re, sys
B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
qid = 'geography-pp-2019-higher-q106'
lines = open(B + 'batches/batch-36.txt', encoding='utf-8').read().split('\n')
cands = set(re.findall(r'^\[([^\]]+)\]', '\n'.join(lines), re.M))
labels = re.findall(r'^PART "([^"]+)"', '\n'.join(lines), re.M)
d = json.load(open(B + 'out/' + qid + '.json', encoding='utf-8'))
assert list(d.keys()) == labels, (list(d.keys()), labels)
n = 0
for k, mps in d.items():
    for mp in mps:
        n += 1
        assert 1 <= mp['k'] <= len(mp['of']), (k, mp)
        for i in mp['of']:
            assert i in cands, (k, i)
print('ok parts', len(d), 'marking points', n, 'empty', [k for k, v in d.items() if not v])
