import json, re, sys, os

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-96.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in re.split(r'\n=+\n', text) if 'QUESTION ' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    path = os.path.join(OUT, qid + '.json')
    if not os.path.exists(path):
        print('MISSING', qid); ok = False; continue
    data = json.load(open(path, encoding='utf-8'))
    if sorted(data.keys()) != sorted(labels) or len(data) != len(labels):
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    for lab in labels:
        mps = data.get(lab, [])
        for mp in mps:
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, lab, 'bad k', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'MPs', sum(len(data[l]) for l in labels), 'empty', [l for l in labels if not data[l]])
print('OK' if ok else 'FAILED')
