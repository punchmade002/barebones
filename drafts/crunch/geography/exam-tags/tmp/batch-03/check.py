import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-03.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('QUESTION ')[1:]]
for b in blocks:
    qid = b.split()[0]
    parts = re.findall(r'^PART "([^"]*)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    total_mp = 0
    empty = []
    errs = []
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); continue
    if list(data.keys()) != parts:
        errs.append(f'labels {list(data.keys())} != {parts}')
    for p, mps in data.items():
        if not mps: empty.append(p)
        for mp in mps:
            total_mp += 1
            of = mp.get('of', [])
            if not (1 <= mp.get('k', 0) <= len(of)): errs.append(f'{p}: bad k {mp}')
            for i in of:
                if i not in cands: errs.append(f'{p}: id not in candidates {i}')
    print(qid, 'parts', len(parts), 'marking points', total_mp, 'empty', empty, 'ERRORS' if errs else 'ok', errs)
