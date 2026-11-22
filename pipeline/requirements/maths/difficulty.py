"""Difficulty grade (Beginner / Intermediate / Advanced) and in-chapter rank for every skill.

  python3 pipeline/requirements/maths/difficulty.py pack    # writes difficulty/in/P1.json, P2.json for the graders
  python3 pipeline/requirements/maths/difficulty.py check   # checks difficulty/out/*.json → difficulty.json

difficulty.json is the source of truth (hand-editable): {"grades": {id: grade}, "order": {chapter: [ids, easiest first]}}.
build.py reads it and adds `grade` and `rank` to skills.json.
"""
import json
import re
import statistics as st
import sys
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).parent
WORK = HERE / 'difficulty'
GRADES = ['Beginner', 'Intermediate', 'Advanced']


def evidence(skills):
    """Per skill, from the exam parts tagged with it: how often, on which level, how big and how late in the question."""
    tags = json.loads((HERE / 'skill-tags.json').read_text())
    ev = {i: [] for i in skills}
    for pid, t in tags.items():
        level, label = re.search(r'-(higher|ordinary)-', pid)[1], pid.split('#')[1]
        letter = re.match(r'\(([a-h])\)', label)
        for i in t['skills']:
            if i in ev:
                ev[i].append(dict(hl=level == 'higher', primary=t['primary'] == i, part=letter[1] if letter else 'a'))
    out = {}
    for i, e in ev.items():
        prim = [x for x in e if x['primary']]
        out[i] = dict(examParts=len(e), asMainSkill=len(prim),
                      shareHigher=round(st.mean(x['hl'] for x in e), 2) if e else None,
                      typicalPart=st.median_low(sorted(x['part'] for x in prim or e)) if e else None)
    return out


def pack():
    data = json.loads((HERE / 'skills.json').read_text())
    skills = {s['id']: s for s in data['skills']}
    ev = evidence(skills)
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    (WORK / 'out').mkdir(exist_ok=True)
    # a whole chapter goes to one grader (the paper most of its skills are on), so its order comes from one place
    votes = {}
    for s in skills.values():
        votes.setdefault(s['chapter'], []).append(s['paper'])
    home = {c: max(set(v), key=v.count) for c, v in votes.items()}
    for paper in (1, 2):
        chaps = {}
        for s in skills.values():
            if home[s['chapter']] == paper:
                chaps.setdefault(s['chapter'], []).append(dict(
                    id=s['id'], level=s['level'], title=s['title'], io=f"{s['input']} → {s['output']}",
                    example=s['example'], needs=s['prereqs'], exam=ev[s['id']]))
        out = [dict(chapter=c, title=data['chapters'][c], skills=v) for c, v in sorted(chaps.items(), key=lambda kv: int(kv[0][5:]))]
        (WORK / 'in' / f'P{paper}.json').write_text(json.dumps(out, ensure_ascii=False))
        print(f'P{paper}: {len(out)} chapters, {sum(len(c["skills"]) for c in out)} skills')


def problems(skills, grades, order):
    """Rule breaks: missing/duplicate skills, bad grades, a prereq ranked after its skill in the same chapter,
    a skill graded easier than one of its prereqs."""
    errs = []
    placed = [i for ids in order.values() for i in ids]
    for i in skills:
        if grades.get(i) not in GRADES:
            errs.append(f'{i}: grade {grades.get(i)!r}')
        if placed.count(i) != 1:
            errs.append(f'{i}: ranked {placed.count(i)} times')
        elif i not in order.get(skills[i]['chapter'], []):
            errs.append(f'{i}: ranked outside its chapter')
    for c, ids in order.items():
        pos = {i: n for n, i in enumerate(ids)}
        g = [GRADES.index(grades[i]) for i in ids if grades.get(i) in GRADES]
        if g != sorted(g):
            errs.append(f'{c}: grades go down somewhere along the order')
        for i in ids:
            for p in skills.get(i, {}).get('prereqs', []):
                if p in pos and pos[p] > pos[i]:
                    errs.append(f'{c}: {p} must come before {i} (it is a prereq)')
                if grades.get(p) in GRADES and grades.get(i) in GRADES and GRADES.index(grades[p]) > GRADES.index(grades[i]):
                    errs.append(f'{i} ({grades[i]}) is easier than its prereq {p} ({grades[p]})')
    return errs


def check():
    skills = {s['id']: s for s in json.loads((HERE / 'skills.json').read_text())['skills']}
    grades, order = {}, {}
    for f in sorted((WORK / 'out').glob('P*.json')):
        for ch in json.loads(f.read_text()):
            order[ch['chapter']] = [r['id'] for r in ch['skills']]
            grades.update({r['id']: r['grade'] for r in ch['skills']})
    errs = problems(skills, grades, order)
    print('\n'.join(errs) or 'ok')
    if not errs:
        (HERE / 'difficulty.json').write_text(json.dumps(dict(grades=grades, order=order), ensure_ascii=False, indent=1) + '\n')
        counts = {g: sum(v == g for v in grades.values()) for g in GRADES}
        print(f'{len(grades)} skills graded {counts} → difficulty.json')
    return errs


_s = {'a': dict(chapter='c', prereqs=[]), 'b': dict(chapter='c', prereqs=['a'])}
assert problems(_s, {'a': 'Beginner', 'b': 'Advanced'}, {'c': ['a', 'b']}) == []
assert len(problems(_s, {'a': 'Advanced', 'b': 'Beginner'}, {'c': ['b', 'a']})) == 2

if __name__ == '__main__':
    {'pack': pack, 'check': check}[sys.argv[1]]()
