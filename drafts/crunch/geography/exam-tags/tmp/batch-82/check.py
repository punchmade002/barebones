import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-82.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for block in blocks:
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'PART "([^"]+)"', block)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    with open(OUT + qid + '.json', encoding='utf-8') as f:
        data = json.load(f)
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels)
        ok = False
    empty = []
    mps = 0
    for lab, mpl in data.items():
        if not mpl:
            empty.append(lab)
        for mp in mpl:
            mps += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, lab, 'BAD k', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, lab, 'UNKNOWN ID', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', mps, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
