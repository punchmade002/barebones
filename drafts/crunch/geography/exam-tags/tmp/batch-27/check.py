import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-27.txt', encoding='utf-8').read()
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
blocks = batch.split('=' * 40)
for qid in ['geography-pp-2018-higher-q109', 'geography-pp-2018-higher-q110']:
    # slice the batch for this question
    start = batch.index('QUESTION ' + qid)
    nxt = batch.find('QUESTION geography-pp-', start + 10)
    text = batch[start:] if nxt == -1 else batch[start:nxt]
    cands = set(re.findall(r'^\[([^\]]+)\]', text, re.M))
    labels = re.findall(r'^PART "([^"]+)"', text, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    errs = []
    if list(data.keys()) != labels:
        errs.append(('label mismatch', list(data.keys()), labels))
    n = 0
    for lab, pts in data.items():
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])):
                errs.append(('bad k', lab, p))
            for i in p['of']:
                if i not in cands:
                    errs.append(('unknown id', lab, i))
    empty = [l for l, p in data.items() if not p]
    print(qid, 'parts', len(labels), 'points', n, 'empty', empty, 'errors', errs or 'none')
