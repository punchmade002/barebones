"""Tag every maths exam part with the skill ids it uses.

  python3 pipeline/requirements/maths/tag.py pack <bank.js>   # writes tagging/in/bNNN.json (10 questions each)
  python3 pipeline/requirements/maths/tag.py collect           # checks tagging/out/*.json → skill-tags.json + report

An agent reads one in/bNNN.json and writes out/bNNN.json:
  {"<questionId>#<label>": {"primary": "<skill id>", "skills": ["<id>", ...]}, ...}
Only the worked solution is sent: students see crops, and the solution shows every operation.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
WORK = HERE / 'tagging'
SKILLS = {s['id']: s for s in json.loads((HERE / 'skills.json').read_text())['skills']}


def load_bank(path):
    s = Path(path).read_text()
    return json.loads(s[s.index('concat(') + 7:s.rindex(')')])


def plain(sol):
    """Worked solution as compact text lines (titles, prose, tex)."""
    out = []
    for st in sol.get('steps', []):
        out.append('## ' + st['title'])
        out += [ln.get('tex') or ln.get('text') or '' for ln in st.get('lines', [])]
    out.append('ANSWER: ' + str(sol.get('finalAnswer', '')))
    return '\n'.join(out)


def pack(bank_path):
    bank = load_bank(bank_path)
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    (WORK / 'out').mkdir(exist_ok=True)
    for n in range(0, len(bank), 10):
        batch = []
        for q in bank[n:n + 10]:
            for p in q['parts']:
                batch.append(dict(part=f"{q['id']}#{p['label']}", level=q['level'], chapters=p.get('topics', []),
                                  marks=p.get('marks'), solution=plain(p.get('workedSolution') or {})))
        (WORK / 'in' / f'b{n // 10 + 1:03}.json').write_text(json.dumps(batch, ensure_ascii=False, indent=1))
    catalog = '\n'.join(f"{i} [{s['level']}, {s['chapter']}] {s['title']}" for i, s in SKILLS.items())
    (WORK / 'catalog.txt').write_text(catalog + '\n')
    print(f'{len(bank)} questions → {(len(bank) + 9) // 10} batches in {WORK}/in')


def collect():
    tags, problems = {}, []
    expected = {}
    for f in sorted((WORK / 'in').glob('b*.json')):
        expected.update({p['part']: f.stem for p in json.loads(f.read_text())})
        out = WORK / 'out' / f.name
        if not out.exists():
            problems.append(f'{f.stem}: no output')
            continue
        for part, t in json.loads(out.read_text()).items():
            if part not in expected:
                problems.append(f'{f.stem}: unknown part {part}')
                continue
            bad = [i for i in [t.get('primary')] + t.get('skills', []) if i not in SKILLS]
            if bad:
                problems.append(f'{part}: unknown skill ids {bad}')
            skills = [i for i in t.get('skills', []) if i in SKILLS]
            if t.get('primary') in SKILLS and t['primary'] not in skills:
                skills.insert(0, t['primary'])
            tags[part] = dict(primary=t.get('primary') if t.get('primary') in SKILLS else None, skills=skills)
    missing = [p for p, b in expected.items() if p not in tags and (WORK / 'out' / f'{b}.json').exists()]
    problems += [f'{p}: not tagged' for p in missing]
    count = {i: 0 for i in SKILLS}
    prim = {i: 0 for i in SKILLS}
    for t in tags.values():
        for i in t['skills']:
            count[i] += 1
        if t['primary']:
            prim[t['primary']] += 1
    (HERE / 'skill-tags.json').write_text(json.dumps(tags, ensure_ascii=False, indent=1) + '\n')
    report = dict(parts=len(expected), tagged=len(tags), problems=problems,
                  primaryUnder3=sorted(i for i, c in prim.items() if c < 3),
                  neverUsed=sorted(i for i, c in count.items() if c == 0),
                  primaryCounts=prim)
    (WORK / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1) + '\n')
    print(f"{len(tags)}/{len(expected)} parts tagged, {len(problems)} problems, "
          f"{len(report['primaryUnder3'])} skills with < 3 primary parts, {len(report['neverUsed'])} never used")
    return report


if __name__ == '__main__':
    {'pack': lambda: pack(sys.argv[2]), 'collect': collect}[sys.argv[1]]()
