import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-107.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('====') if 'QUESTION ' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    for lab, mps in data.items():
        for mp in mps:
            total += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            assert len(mp['of']) <= 2, (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    empty = [l for l, m in data.items() if not m]
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
