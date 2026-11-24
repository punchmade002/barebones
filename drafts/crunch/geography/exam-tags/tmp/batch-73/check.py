import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-73.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
parts_expected = {}
cands = {}
for b in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    cands[qid] = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    parts_expected[qid] = re.findall(r'^PART "([^"]+)"', b, re.M)
ok = True
for qid in cands:
    d = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    labels = list(d.keys())
    if labels != parts_expected[qid]:
        print(qid, 'label mismatch', labels, parts_expected[qid]); ok = False
    n = 0
    for lab, pts in d.items():
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])):
                print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cands[qid]:
                    print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', n, 'empty', [l for l in labels if not d[l]])
print('OK' if ok else 'FAIL')
