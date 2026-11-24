import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-103.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read().split('\n')
questions = []
cur = None
section = None
for line in text:
    if line.startswith('QUESTION '):
        cur = {'id': line.split()[1], 'parts': [], 'cands': set()}
        questions.append(cur)
        section = None
    elif cur is None:
        continue
    elif line.startswith('PART "'):
        cur['parts'].append(line.split('"')[1])
    elif line.startswith('CANDIDATES'):
        section = 'c'
    elif line.startswith('==='):
        section = None
    elif section == 'c':
        m = re.match(r'^\[([^\]]+)\]', line)
        if m:
            cur['cands'].add(m.group(1))

ok = True
for q in questions:
    path = OUT + q['id'] + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(q['id'], 'PARSE FAIL', e); ok = False; continue
    keys = list(data.keys())
    if keys != q['parts']:
        print(q['id'], 'PART MISMATCH', keys, q['parts']); ok = False
    points = 0
    empty = []
    for part, pts in data.items():
        if not pts:
            empty.append(part)
        for p in pts:
            points += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print(q['id'], part, 'BAD K', p); ok = False
            if len(of) > 2:
                print(q['id'], part, 'TOO MANY IDS', p); ok = False
            if len(set(of)) != len(of):
                print(q['id'], part, 'DUP IDS', p); ok = False
            for i in of:
                if i not in q['cands']:
                    print(q['id'], part, 'UNKNOWN ID', i); ok = False
    print(q['id'], 'parts', len(data), 'points', points, 'empty', empty)

print('ALL OK' if ok else 'FAILURES')
