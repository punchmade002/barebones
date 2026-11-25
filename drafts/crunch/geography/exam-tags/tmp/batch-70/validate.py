import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-70.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('=' * 40) if 'QUESTION ' in b]
ok = True
for block in blocks:
    qid = re.search(r'QUESTION (\S+)', block).group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cand_part = block.split('CANDIDATES (shortlist):')[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    total = 0
    empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, lab, 'bad k', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('OK' if ok else 'FAILED')
