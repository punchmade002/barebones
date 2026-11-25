import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-42.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
lines = open(BATCH, encoding='utf-8').read().split('\n')
questions = {}
cur = None
mode = None
for ln in lines:
    if ln.startswith('QUESTION '):
        cur = ln.split()[1]
        questions[cur] = {'parts': [], 'cands': set()}
        mode = None
    elif ln.startswith('PART '):
        questions[cur]['parts'].append(re.match(r'PART "([^"]+)"', ln).group(1))
    elif ln.startswith('CANDIDATES'):
        mode = 'c'
    elif ln.startswith('===='):
        mode = None
    elif mode == 'c':
        m = re.match(r'\[([^\]]+)\]', ln)
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
    total = 0; empty = []
    for part, pts in data.items():
        if not pts: empty.append(part)
        for p in pts:
            total += 1
            if not (1 <= p['k'] <= len(p['of'])):
                print(q, part, 'BAD k', p); ok = False
            if len(p['of']) > 2:
                print(q, part, 'more than 2 ids', p); ok = False
            for i in p['of']:
                if i not in info['cands']:
                    print(q, part, 'ID NOT IN CANDIDATES', i); ok = False
    print(q, 'parts', len(data), 'points', total, 'empty', empty, 'candidates', len(info['cands']))
print('ALL OK' if ok else 'PROBLEMS')
