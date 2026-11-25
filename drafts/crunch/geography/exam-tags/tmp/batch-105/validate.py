import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-105.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
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
                if i not in cands:
                    ok = False
                    print('BAD ID', qid, lab, i)
    print(qid, 'parts', len(labels), 'points', total, 'empty', empty)
print('OK' if ok else 'FAIL')
