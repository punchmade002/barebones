import json
import re

BASE = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics'
out = json.load(open(BASE + '/exam-refs/out-21.json', encoding='utf-8'))
catalogue_ids = set()
for line in open(BASE + '/catalogue.txt', encoding='utf-8'):
    m = re.match(r'^(hom-[\w-]+) \|', line)
    if m:
        catalogue_ids.add(m.group(1))

expected = {}
qkey = None
for line in open(BASE + '/exam-refs/batch-21.txt', encoding='utf-8'):
    m = re.match(r'^QUESTION (\S+) ', line)
    if m:
        qkey = m.group(1)
        expected[qkey] = []
        continue
    m = re.match(r'^PART (\S+) \[', line)
    if m and qkey:
        expected[qkey].append(m.group(1))

problems = []
if set(out) != set(expected):
    problems.append('question keys differ: missing %s extra %s' % (set(expected) - set(out), set(out) - set(expected)))
part_total = 0
sub_total = 0
for q, labels in expected.items():
    got = out.get(q, {})
    if set(got) != set(labels):
        problems.append('%s: part labels differ, missing %s extra %s' % (q, set(labels) - set(got), set(got) - set(labels)))
    for lab in labels:
        ids = got.get(lab)
        part_total += 1
        if not ids or not isinstance(ids, list):
            problems.append('%s %s: empty' % (q, lab))
            continue
        if len(ids) > 4:
            problems.append('%s %s: more than 4 ids' % (q, lab))
        for i in ids:
            if i not in catalogue_ids:
                problems.append('%s %s: unknown id %s' % (q, lab, i))
        sub_total += len(ids)

print('problems:', problems if problems else 'none')
print('questions:', len(expected))
print('parts:', part_total)
print('average subsections per part: %.2f' % (sub_total / part_total))
