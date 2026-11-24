import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-22.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print(qid, 'part keys mismatch', list(data.keys()), parts); ok = False
    mp = 0
    empty = []
    for p, mps in data.items():
        if not mps:
            empty.append(p)
        for mk in mps:
            mp += 1
            of = mk['of']
            if not (1 <= mk['k'] <= len(of)):
                print(qid, p, 'bad k', mk); ok = False
            if len(of) > 2:
                print(qid, p, 'more than 2 ids without any-k rule', mk); ok = False
            for i in of:
                if i not in cands:
                    print(qid, p, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(parts), 'marking points', mp, 'empty', empty)
print('OK' if ok else 'FAILURES')
