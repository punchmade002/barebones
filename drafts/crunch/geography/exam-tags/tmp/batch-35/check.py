import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-35.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in re.split(r'^=+\s*$', text, flags=re.M) if b.strip()]
ok = True
for block in blocks:
    qid = re.search(r'^QUESTION (\S+)', block, re.M).group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cand_part = block.split('CANDIDATES', 1)[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('PARSE FAIL', path, e); ok = False; continue
    if list(data.keys()) != labels:
        print('LABEL MISMATCH', qid, list(data.keys()), labels); ok = False
    total = 0; empty = []
    for part, pts in data.items():
        if not pts:
            empty.append(part)
        for p in pts:
            total += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print('BAD K', qid, part, p); ok = False
            if len(of) > 2 and 'any' not in '':
                print('NOTE >2 ids', qid, part, p)
            for i in of:
                if i not in cands:
                    print('BAD ID', qid, part, i); ok = False
        limit = {'4A': 10, '4B': 15, '4C': 15, '5B': 15, '5C': 15}
    print(qid, 'parts', len(data), 'points', total, 'empty', empty)

print('ALL OK' if ok else 'PROBLEMS')
