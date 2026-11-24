import json, re, sys, glob, os

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-106.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n=') if b.strip()]
ok = True
for block in re.split(r'\n={5,}\n', text):
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    path = os.path.join(OUT, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, 'LABELS MISMATCH', list(data.keys()), labels); ok = False
    total = 0; empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, lab, 'BAD K', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, lab, 'BAD ID', i); ok = False
    print(qid, 'parts', len(data), 'marking points', total, 'empty', empty)
print('OK' if ok else 'FAILURES')
