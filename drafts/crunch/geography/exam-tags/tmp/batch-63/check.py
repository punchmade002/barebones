import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-63.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('=' * 40) if 'QUESTION ' in b]

ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    parts = re.findall(r'^PART "([^"]+)"', b, re.M)
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    keys = list(data.keys())
    if keys != parts:
        print(qid, 'PART MISMATCH', keys, parts); ok = False
    total = 0
    empty = []
    for p, mps in data.items():
        if not mps:
            empty.append(p)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                print(qid, p, 'BAD K', mp); ok = False
            if len(of) > 2:
                print(qid, p, 'TOO MANY IDS', mp); ok = False
            for i in of:
                if i not in cands:
                    print(qid, p, 'UNKNOWN ID', i); ok = False
    print(qid, 'parts', len(data), 'marking points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
