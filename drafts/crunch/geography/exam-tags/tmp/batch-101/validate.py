import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-101.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if 'QUESTION ' in b]
ok = True
for block in blocks:
    qid = re.search(r'QUESTION (\S+)', block).group(1)
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    cand_section = block.split('CANDIDATES (shortlist):', 1)[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_section, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    keys = list(data.keys())
    if keys != parts:
        ok = False
        print(qid, 'PART ORDER/LABEL MISMATCH', keys, parts)
    mp = 0
    empty = []
    for label, mps in data.items():
        if not mps:
            empty.append(label)
        for m in mps:
            mp += 1
            of = m['of']
            if not (1 <= m['k'] <= len(of)):
                ok = False
                print(qid, label, 'bad k', m)
            for i in of:
                if i not in cands:
                    ok = False
                    print(qid, label, 'id not in candidates', i)
    print(qid, 'parts', len(parts), 'marking points', mp, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
