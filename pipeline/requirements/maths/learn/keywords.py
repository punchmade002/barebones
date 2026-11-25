"""Search keywords for each maths skill page, written by readers (KEYWORDS.md) from the skill's own record.

  python3 keywords.py pack     # every skill → keywords/in/Knn.json, 25 per batch
  python3 keywords.py status   # how many skills have keywords

package.py adds them to each skill's package with the terms every skill shares (course, level, paper, chapter).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / 'keywords'
MATHS = HERE.parent
PER = 25


def written():
    out = {}
    for f in sorted((WORK / 'out').glob('K*.json')):
        out.update(json.loads(f.read_text()))
    return out


def pack():
    db = json.loads((MATHS / 'skills.json').read_text())
    s = (MATHS / 'build/maths-learn.js').read_text()
    L = json.loads(s[s.index('{'):s.rindex('}') + 1])
    items = [{'skill': k['id'], 'title': k['title'], 'chapter': db['chapters'][k['chapter']], 'level': k['level'],
              'input': k['input'], 'output': k['output'], 'example': k['example'], 'what': L[k['id']]['what']['say'],
              'question': L[k['id']]['example']['question']} for k in db['skills']]
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    for k in range(0, len(items), PER):
        (WORK / 'in' / f'K{k // PER + 1:02d}.json').write_text(json.dumps(items[k:k + PER], ensure_ascii=False, indent=1))
    print(f'{len(items)} skills → {(len(items) + PER - 1) // PER} batches')


def status():
    db = json.loads((MATHS / 'skills.json').read_text())
    w = written()
    missing = [k['id'] for k in db['skills'] if not w.get(k['id'])]
    n = [len(v) for v in w.values()]
    print(f'{len(db["skills"]) - len(missing)} of {len(db["skills"])} skills have keywords (median {sorted(n)[len(n) // 2] if n else 0})')
    if missing:
        print('  missing:', ' '.join(missing[:20]))


if __name__ == '__main__':
    {'pack': pack, 'status': status}[sys.argv[1]]()
