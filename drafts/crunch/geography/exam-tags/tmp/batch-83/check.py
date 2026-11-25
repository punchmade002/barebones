import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-83.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for b in blocks:
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    for lab, pts in data.items():
        for p in pts:
            total += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            for i in p['of']:
                if i not in cands:
                    ok = False
                    print('BAD ID', qid, lab, i)
    print(qid, 'parts', len(labels), 'points', total, 'empty', [l for l, p in data.items() if not p])
print('OK' if ok else 'FAILED')
