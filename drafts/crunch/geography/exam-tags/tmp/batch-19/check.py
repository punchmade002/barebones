import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-19.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = re.split(r'^=+\s*$', text, flags=re.M)
ok = True
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, flags=re.M)
    if not m:
        continue
    qid = m.group(1)
    # candidate ids are the bracketed ids on lines after CANDIDATES
    cand_part = block.split('CANDIDATES', 1)[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, flags=re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, flags=re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    mp = 0
    empty = []
    for label, mps in data.items():
        if not mps:
            empty.append(label)
        for mpt in mps:
            mp += 1
            of = mpt['of']
            if not (1 <= mpt['k'] <= len(of)):
                print(qid, label, 'bad k', mpt); ok = False
            if len(of) > 2:
                print(qid, label, 'too many ids', mpt); ok = False
            for i in of:
                if i not in cands:
                    print(qid, label, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(data), 'marking points', mp, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
