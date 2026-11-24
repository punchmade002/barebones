import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-69.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

lines = open(BATCH, encoding='utf-8').read().split('\n')
questions = {}
cur = None
for line in lines:
    m = re.match(r'^QUESTION (\S+)', line)
    if m:
        cur = m.group(1)
        questions[cur] = {'parts': [], 'cands': set()}
        mode = None
        continue
    if cur is None:
        continue
    m = re.match(r'^PART "([^"]+)"', line)
    if m:
        questions[cur]['parts'].append(m.group(1))
    m = re.match(r'^\[([^\]]+)\]', line)
    if m:
        questions[cur]['cands'].add(m.group(1))

ok = True
for q, info in questions.items():
    path = OUT + q + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(q, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != info['parts']:
        print(q, 'PART KEYS MISMATCH', list(data.keys()), info['parts']); ok = False
    mp_total = 0
    empty = []
    for part, mps in data.items():
        if not mps:
            empty.append(part)
        for mp in mps:
            mp_total += 1
            k, of = mp['k'], mp['of']
            if not (1 <= k <= len(of)):
                print(q, part, 'BAD k', mp); ok = False
            for i in of:
                if i not in info['cands']:
                    print(q, part, 'UNKNOWN ID', i); ok = False
    print(q, 'parts', len(info['parts']), 'marking points', mp_total, 'empty', empty)

print('ALL OK' if ok else 'PROBLEMS')
sys.exit(0 if ok else 1)
