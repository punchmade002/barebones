import json, re, sys

QID = 'geography-pp-2019-higher-q107'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/' + QID + '.json'
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-37.txt'

text = open(BATCH, encoding='utf-8').read()
block = text.split('QUESTION ' + QID, 1)[1].split('\n=', 1)[0]
cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
labels = re.findall(r'^PART "([^"]+)"', block, re.M)

data = json.load(open(OUT, encoding='utf-8'))
assert list(data.keys()) == labels, (list(data.keys()), labels)
total = 0
for lab, mps in data.items():
    for mp in mps:
        assert 1 <= mp['k'] <= len(mp['of']), (lab, mp)
        for i in mp['of']:
            assert i in cands, (lab, i)
        total += 1
    print(lab, len(mps), 'EMPTY' if not mps else '')
print('parts', len(data), 'marking points', total)
