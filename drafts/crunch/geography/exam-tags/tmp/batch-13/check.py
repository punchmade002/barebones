import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-13.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
for blk in blocks:
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    errs = []
    if list(data.keys()) != labels:
        errs.append('labels mismatch: %s vs %s' % (list(data.keys()), labels))
    total = 0
    for lab, mps in data.items():
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                errs.append('bad k %s in %s' % (mp, lab))
            if len(mp['of']) > 2:
                errs.append('too many ids in %s' % lab)
            for i in mp['of']:
                if i not in cands:
                    errs.append('id not in candidates: %s (%s)' % (i, lab))
    empty = [l for l, v in data.items() if not v]
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty, 'candidates', len(cands))
    print('  errors:', errs if errs else 'none')
