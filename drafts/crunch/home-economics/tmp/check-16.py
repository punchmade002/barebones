import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/exam-refs/batch-16.txt'
OUT = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/exam-refs/out-16.json'
CAT = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/catalogue.txt'

catalogue_ids = set()
with open(CAT, encoding='utf-8') as f:
    for line in f:
        m = re.match(r'^(hom-[a-z0-9-]+) \|', line)
        if m:
            catalogue_ids.add(m.group(1))

questions = []  # (qid, [part labels])
with open(BATCH, encoding='utf-8') as f:
    for line in f:
        if line.startswith('QUESTION '):
            qid = line.split()[1]
            questions.append((qid, []))
        elif line.startswith('PART ') and questions:
            m = re.match(r'^PART (\(.*?\)) \[', line)
            if m:
                questions[-1][1].append(m.group(1))
            else:
                m2 = re.match(r'^PART (\(whole\))', line)
                if m2:
                    questions[-1][1].append(m2.group(1))

with open(OUT, encoding='utf-8') as f:
    out = json.load(f)

errors = []
if list(out.keys()) != [q for q, _ in questions]:
    errors.append('question keys do not match batch order')
total_parts = 0
total_subs = 0
for qid, parts in questions:
    if qid not in out:
        errors.append('missing question ' + qid)
        continue
    got = out[qid]
    if list(got.keys()) != parts:
        errors.append('part labels mismatch for %s: want %s got %s' % (qid, parts, list(got.keys())))
    for p in parts:
        ids = got.get(p, [])
        if not ids or len(ids) > 4:
            errors.append('bad count for %s %s' % (qid, p))
        for i in ids:
            if i not in catalogue_ids:
                errors.append('unknown id %s in %s %s' % (i, qid, p))
        total_parts += 1
        total_subs += len(ids)

print('questions', len(questions))
print('parts', total_parts)
print('avg subsections per part', round(total_subs / total_parts, 2) if total_parts else 0)
print('errors', errors if errors else 'none')
sys.exit(1 if errors else 0)
