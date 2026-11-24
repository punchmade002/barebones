"""Draw back-to-back stem-and-leaf plots in the practice solutions as a KaTeX array, built from the question's data.

  python3 pipeline/requirements/maths/stemleaf.py   # rewrites the plot step in practice/out, practice-bank.json and lesson outputs
"""
import glob
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = 'stat-back-to-back'


def data(question):
    """[(name, [values])] from lines like 'Boys: $21, 34, 27$'."""
    return [(m[1].strip(), sorted(int(v) for v in m[2].split(',')))
            for m in re.finditer(r'(?m)^([A-Z][^:\n$]*):\s*\$([\d,\s]+)\$', question)]


def plot(a, b):
    (na, va), (nb, vb) = a, b
    stems = range(min(va + vb) // 10, max(va + vb) // 10 + 1)
    leaves = lambda vs, s, rev: '\\;'.join(str(v % 10) for v in sorted((v for v in vs if v // 10 == s), reverse=rev))
    rows = [f'\\text{{{na}}} & & \\text{{{nb}}}', '\\hline'] + [f'{leaves(va, s, True)} & {s} & {leaves(vb, s, False)}' for s in stems]
    return '\\begin{array}{r|c|l} ' + ' \\\\ '.join(rows).replace('\\\\ \\hline \\\\', '\\\\ \\hline') + ' \\end{array}'


assert plot(('A', [21, 25, 33]), ('B', [28, 30])) == \
    '\\begin{array}{r|c|l} \\text{A} & & \\text{B} \\\\ \\hline 5\\;1 & 2 & 8 \\\\ 3 & 3 & 0 \\end{array}'


def redraw(pr):
    """Replace the leaf-listing text lines of the plot step with the drawn plot; keep the layout sentence and key."""
    sets = data(pr['question'])
    if len(sets) != 2:
        return False
    for st in pr['workedSolution']['steps']:
        if 'plot' in st['title'].lower():
            # drop the old drawing (a previous plot, or text listing leaves stem by stem); keep everything else
            keep = [ln for ln in st['lines'] if not ('array' in ln.get('tex', '') or re.search(r'[Ss]tem \d', ln.get('text', '')))]
            st['lines'] = keep[:1] + [{'tex': plot(*sets)}] + keep[1:]
            return True
    return False


if __name__ == '__main__':
    for f in sorted(glob.glob(str(HERE / 'practice/out/*.json'))):
        d = json.loads(Path(f).read_text())
        hit = [redraw(p) for j in d if j['skill'] == SKILL for p in j['problems']]
        if any(hit):
            Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=1))
            print(f'{Path(f).name}: redrew {sum(hit)} plots')
