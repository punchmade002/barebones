import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-99.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')
# per-question: id, parts (labels in order), candidate ids
qs = {}
for raw in re.split(r'\n={5,}\n', text):
    m = re.search(r'^QUESTION (\S+)', raw, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', raw, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', raw, re.M))
    qs[qid] = (labels, cands)

errors = []
for qid, (labels, cands) in qs.items():
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        errors.append(f'{qid}: parse error {e}')
        continue
    if list(data.keys()) != labels:
        errors.append(f'{qid}: keys {list(data.keys())} != labels {labels}')
    for part, pts in data.items():
        if not isinstance(pts, list):
            errors.append(f'{qid} {part}: not a list')
            continue
        for p in pts:
            of = p.get('of', [])
            k = p.get('k')
            if not isinstance(k, int) or not (1 <= k <= len(of)):
                errors.append(f'{qid} {part}: bad k {p}')
            for i in of:
                if i not in cands:
                    errors.append(f'{qid} {part}: id not in candidates {i}')
    total = sum(len(v) for v in data.values())
    empty = [p for p, v in data.items() if not v]
    print(qid, 'parts', len(data), 'points', total, 'empty', empty)

print('ERRORS:' if errors else 'OK, no errors')
for e in errors:
    print(e)
