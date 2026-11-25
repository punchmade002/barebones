import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-15.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2017-higher-q108.json'

text = open(BATCH, encoding='utf-8').read()
qid = re.search(r'^QUESTION (\S+)', text, re.M).group(1)
parts = re.findall(r'^PART "([^"]+)"', text, re.M)
cand_block = text.split('CANDIDATES (shortlist):')[1]
cands = set(re.findall(r'^\[([^\]]+)\]', cand_block, re.M))

data = json.load(open(OUT, encoding='utf-8'))
errs = []
if set(data.keys()) != set(parts) or len(data) != len(parts):
    errs.append(f'label mismatch: file={list(data)} batch={parts}')
if list(data.keys()) != parts:
    errs.append('order differs from batch')
total = 0
for label, mps in data.items():
    total += len(mps)
    for mp in mps:
        if not (1 <= mp['k'] <= len(mp['of'])):
            errs.append(f'{label}: bad k in {mp}')
        for i in mp['of']:
            if i not in cands:
                errs.append(f'{label}: unknown id {i}')
print(qid, 'parts', len(data), 'marking points', total, 'errors', errs or 'none')
sys.exit(1 if errs else 0)
