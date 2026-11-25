import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-08.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n=') ]
qs = {}
for b in re.split(r'\n={5,}\n', text):
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]*)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    qs[qid] = (parts, cands)
errors = []
summary = []
for qid, (parts, cands) in qs.items():
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        errors.append(f'{qid}: parse error {e}'); continue
    if list(data.keys()) != parts:
        errors.append(f'{qid}: labels {list(data.keys())} != {parts}')
    npts = 0; empty = []
    for label, pts in data.items():
        if not pts: empty.append(label)
        for p in pts:
            npts += 1
            if not isinstance(p.get('of'), list) or not (1 <= p.get('k', 0) <= len(p['of'])):
                errors.append(f'{qid} {label}: bad k/of {p}')
            for i in p.get('of', []):
                if i not in cands:
                    errors.append(f'{qid} {label}: id not in candidates {i}')
    summary.append((qid, len(parts), npts, empty))
for s in summary:
    print(s)
print('ERRORS:', errors if errors else 'none')
