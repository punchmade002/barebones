import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-29.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = re.split(r'^=+$', text, flags=re.M)

ok = True
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, flags=re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, flags=re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, flags=re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels)
        ok = False
    mps = 0
    empty = []
    for label, mpl in data.items():
        if not mpl:
            empty.append(label)
        for mp in mpl:
            mps += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, label, 'bad k', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, label, 'unknown id', i); ok = False
    print(qid, 'parts', len(data), 'marking points', mps, 'empty', empty, 'candidates', len(cands))

print('ALL OK' if ok else 'PROBLEMS')
