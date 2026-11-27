import json, re, sys

base = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics'
batch_path = base + '/exam-refs/batch-15.txt'
cat_path = base + '/catalogue.txt'
out_path = base + '/exam-refs/out-15.json'

questions = {}
cur = None
for line in open(batch_path, encoding='utf-8'):
    m = re.match(r'^QUESTION (\S+)', line)
    if m:
        cur = m.group(1)
        questions[cur] = []
        continue
    m = re.match(r'^PART (.+?) \[', line)
    if m and cur:
        questions[cur].append(m.group(1).strip())

catalogue_ids = set()
for line in open(cat_path, encoding='utf-8'):
    if ' | ' in line:
        catalogue_ids.add(line.split(' | ')[0].strip())

data = json.load(open(out_path, encoding='utf-8'))

errors = []
for q, parts in questions.items():
    if q not in data:
        errors.append('missing question ' + q)
        continue
    for p in parts:
        if p not in data[q]:
            errors.append('missing part %s in %s' % (p, q))
    for p, ids in data[q].items():
        if p not in parts:
            errors.append('extra part %s in %s' % (p, q))
        if not ids:
            errors.append('empty part %s in %s' % (p, q))
        for i in ids:
            if i not in catalogue_ids:
                errors.append('bad id %s' % i)
for q in data:
    if q not in questions:
        errors.append('extra question ' + q)

n_parts = sum(len(v) for v in data.values())
n_subs = sum(len(ids) for v in data.values() for ids in v.values())
print('questions', len(data))
print('parts', n_parts)
print('avg subsections per part', round(n_subs / n_parts, 2))
print('errors', errors if errors else 'none')
