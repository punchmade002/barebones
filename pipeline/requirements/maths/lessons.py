"""Build a lesson for every skill with 3+ exam parts: a main problem + 2 backups, colour-marked steps,
think-first prompts, "what's different" notes and an optional graph.

  python3 pipeline/requirements/maths/lessons.py pack       # lessons/in/LNN.json, 5 skills each
  python3 pipeline/requirements/maths/lessons.py check      # validates lessons/out/*.json → lessons/check.json
  python3 pipeline/requirements/maths/lessons.py assemble   # maths-lessons.js + copies part crops into exam-images

Agents (lessons/INSTRUCTIONS.md) only choose the 3 parts and add marks; the maths comes from the
checked exam bank. `check` proves it: with every \\hl{n}{…} removed, each line must equal the bank's
line exactly, and a graph's points must lie on its curve.
"""
import json
import re
import shutil
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
ROOT = HERE.parents[2]
WORKTREE = ROOT / '.claude' / 'worktrees' / 'maths-older'      # full bank, part crops
WORK = HERE / 'lessons'
SKIP_YEAR = '-2026-'          # this branch ships 2015–2025 only, like master
PER_BATCH, MAX_CANDIDATES = 5, 6
sys.path.insert(0, str(HERE))
from tag import load_bank  # noqa: E402

SKILLS = {s['id']: s for s in json.loads((HERE / 'skills.json').read_text())['skills']}


def bank_parts():
    bank = load_bank(WORKTREE / 'maths-exam-questions.js')
    crops = json.loads((WORKTREE / 'pipeline/_data/rebuild/maths/crops.json').read_text())
    out = {}
    for q in bank:
        key = q['id'].replace('maths-pp-', '')
        for p in q['parts']:
            m = re.match(r'\(([a-h])\)', p['label'])
            img = crops.get(key, {}).get('parts', {}).get(m.group(1)) if m else None
            out[f"{q['id']}#{p['label']}"] = dict(q=q, p=p, image=img or q['images'][0])
    return out


def ready():
    tags = json.loads((HERE / 'skill-tags.json').read_text())
    by = {}
    for pid, t in tags.items():
        if t['primary'] and SKIP_YEAR not in pid:
            by.setdefault(t['primary'], []).append(pid)
    return {s: ps for s, ps in by.items() if len(ps) >= 3}


def unmark(s):
    """Remove \\hl{n}{…} wrappers, keeping the inner text (brace-matched, nesting allowed)."""
    prev = None
    while prev != s:                  # nested marks: strip until stable
        prev, s = s, _strip_once(s)
    return s


def _strip_once(s):
    j = s.find('\\hl{')
    if j < 0:
        return s
    k = s.index('}{', j) + 2
    depth, m = 1, k
    while depth:
        depth += {'{': 1, '}': -1}.get(s[m], 0)
        m += 1
    return s[:j] + s[k:m - 1] + s[m:]


def mark_bodies(s):
    """The inner text of every \\hl{n}{…} in s."""
    out, j = [], s.find('\\hl{')
    while j >= 0:
        k = s.index('}{', j) + 2
        depth, m = 1, k
        while depth:
            depth += {'{': 1, '}': -1}.get(s[m], 0)
            m += 1
        out.append(s[k:m - 1])
        j = s.find('\\hl{', k)
    return out


norm = lambda s: re.sub(r'\s+', '', s or '')

assert unmark('\\hl{2}{x} &= \\frac{\\hl{3}{-17}}{\\hl{2}{5}}') == 'x &= \\frac{-17}{5}'
assert unmark('$\\hl{4}{f\'\'(1) = 6 > 0}$, so min') == "$f''(1) = 6 > 0$, so min"


def pack():
    parts, skills = bank_parts(), ready()
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    (WORK / 'out').mkdir(exist_ok=True)
    jobs = []
    for sid in sorted(skills, key=lambda s: (SKILLS[s]['chapter'], s)):
        s = SKILLS[sid]
        prefer = 'ordinary' if s['level'] in ('JC', 'OL') else 'higher'
        cands = sorted(skills[sid], key=lambda pid: (parts[pid]['q']['level'] != prefer,
                                                     len(parts[pid]['p']['workedSolution']['steps']), pid))
        jobs.append(dict(skill=dict(id=sid, title=s['title'], level=s['level'], input=s['input'], output=s['output']),
                         candidates=[dict(part=pid, level=parts[pid]['q']['level'], year=parts[pid]['q']['year'],
                                          marks=parts[pid]['p']['marks'],
                                          steps=[dict(title=st['title'], lines=[{k: v for k, v in ln.items() if k in ('tex', 'text')}
                                                                                for ln in st['lines']])
                                                 for st in parts[pid]['p']['workedSolution']['steps']],
                                          final=parts[pid]['p']['workedSolution']['finalAnswer'])
                                     for pid in cands[:MAX_CANDIDATES]]))
    for n in range(0, len(jobs), PER_BATCH):
        (WORK / 'in' / f'L{n // PER_BATCH + 1:02}.json').write_text(json.dumps(jobs[n:n + PER_BATCH], ensure_ascii=False, indent=1))
    print(f'{len(jobs)} skills → {(len(jobs) + PER_BATCH - 1) // PER_BATCH} batches in {WORK / "in"}')


X = sp.Symbol('x', real=True)   # real, so d|f|/dx is sign(f)·f′ rather than re/im parts


def parse_f(expr):
    return sp.sympify(expr.replace('^', '**'), locals={'x': X, 'e': sp.E, 'pi': sp.pi, 'ln': sp.log})


def check_graph(g):
    errs = []
    try:
        f = parse_f(g['f'])
    except Exception as exc:          # noqa: BLE001 - any parse failure is a check failure
        return [f'graph f does not parse: {exc}']
    xmin, ymax, xmax, ymin = g['box']
    if not (xmin < xmax and ymin < ymax):
        errs.append('graph box must be [xmin, ymax, xmax, ymin]')
    fn = sp.lambdify(X, f, 'math')
    for pt in g.get('points', []):
        try:
            y = fn(pt['x'])
        except Exception:             # noqa: BLE001
            y = None
        if y is None or abs(y - pt['y']) > 0.01 * max(1, abs(pt['y'])) + 0.02:
            errs.append(f"graph point {pt} is not on f (f({pt['x']}) = {y})")
        if not (xmin <= pt['x'] <= xmax and ymin <= pt['y'] <= ymax):
            errs.append(f'graph point {pt} is outside the box')
    ok = 0
    for k in range(21):
        try:
            v = complex(fn(xmin + (xmax - xmin) * k / 20))
            ok += v.imag == 0
        except Exception:             # noqa: BLE001
            pass
    if ok < 15:
        errs.append('graph f is undefined over most of the box')
    return errs


def prose(s):
    """A text line may wrap words in $\\hl{n}{\\text{…}}$ to colour them; compare without those wrappers."""
    return re.sub(r'\\text\{([^{}]*)\}', r'\1', s).replace('$', '')


assert prose('A $\\text{quantity}$ of $200$') == prose('A quantity of 200')


def bare_tex(s):
    """Prose (ask, note) is shown as text with $…$ rendered: a bare z_2 or \\sqrt prints literally."""
    return bool(re.search(r'[_^\\]', re.sub(r'\$[^$]*\$', '', s)))


assert bare_tex('Which is z_2?') and not bare_tex('Which is $z_2$, the root of $\\sqrt{3}$?')


def check_lesson(job, out):
    errs, cands = [], {c['part']: c for c in job['candidates']}
    probs = out.get('problems', [])
    if len(probs) != 3 or len({p.get('part') for p in probs}) != 3:
        return ['need exactly 3 different problems']
    for n, pr in enumerate(probs):
        c = cands.get(pr['part'])
        if not c:
            errs.append(f"{pr['part']}: not one of the candidates")
            continue
        tag = pr['part'].split('maths-pp-')[-1]
        if re.search(r'marking scheme', json.dumps(c), re.I):
            errs.append(f'{tag}: its solution talks about the marking scheme; choose another candidate')
        if n and not (pr.get('note') or '').strip():
            errs.append(f'{tag}: backup needs a "what\'s different" note')
        if bare_tex(pr.get('note') or ''):
            errs.append(f'{tag}: note has LaTeX outside $…$')
        if len(pr.get('steps', [])) != len(c['steps']):
            errs.append(f'{tag}: has {len(pr.get("steps", []))} steps, bank has {len(c["steps"])}')
            continue
        used = set()
        for k, (a, b) in enumerate(zip(pr['steps'], c['steps'])):
            if not (a.get('ask') or '').strip():
                errs.append(f'{tag} step {k + 1}: missing ask')
            elif '?' not in a['ask']:
                errs.append(f'{tag} step {k + 1}: ask must contain a question, not only a command')
            elif bare_tex(a['ask']):
                errs.append(f'{tag} step {k + 1}: ask has LaTeX outside $…$')
            if norm(a.get('title')) != norm(b['title']):
                errs.append(f'{tag} step {k + 1}: title changed')
            if len(a.get('lines', [])) != len(b['lines']):
                errs.append(f'{tag} step {k + 1}: line count changed')
                continue
            for i, (la, lb) in enumerate(zip(a['lines'], b['lines'])):
                kind = 'tex' if 'tex' in lb else 'text'
                same = prose if kind == 'text' else (lambda t: t)
                if norm(same(unmark(la.get(kind, '')))) != norm(same(lb[kind])):
                    errs.append(f'{tag} step {k + 1} line {i + 1}: changed beyond adding \\hl marks')
                used |= set(re.findall(r'\\hl\{(\d)\}', la.get(kind, '')))
                if kind == 'text' and '\\hl' in re.sub(r'\$[^$]*\$', '', la.get('text', '')):
                    errs.append(f'{tag} step {k + 1} line {i + 1}: a mark in a text line must sit inside $…$')
                if any('&' in body or '\\\\' in body for body in mark_bodies(la.get(kind, ''))):
                    errs.append(f'{tag} step {k + 1} line {i + 1}: a mark contains & or \\\\ (breaks alignment)')
        if norm(unmark(pr.get('final', ''))) != norm(c['final']):
            errs.append(f'{tag}: final answer changed beyond adding \\hl marks')
        used |= set(re.findall(r'\\hl\{(\d)\}', pr.get('final', '')))
        legend = {str(k) for k in (pr.get('legend') or {})}
        if not used:
            errs.append(f'{tag}: no \\hl marks')
        if used - legend or used - {'1', '2', '3', '4'}:
            errs.append(f'{tag}: slots {sorted(used)} need a legend entry each (slots 1-4 only)')
        if pr.get('graph'):
            errs += [f'{tag}: {e}' for e in check_graph(pr['graph'])]
    return errs


def jobs():
    return {j['skill']['id']: j for f in sorted((WORK / 'in').glob('L*.json')) for j in json.loads(f.read_text())}


def outputs():
    """Lessons by skill: first-pass out/L*.json, replaced by fix-round fixed/F*.json where one exists."""
    outs = {}
    for f in sorted((WORK / 'out').glob('L*.json')) + sorted((WORK / 'fixed').glob('F*.json')):
        outs.update({o['skill']: o for o in json.loads(f.read_text())})
    return outs


def check():
    outs = outputs()
    report = {sid: ['no output'] if sid not in outs else check_lesson(job, outs[sid]) for sid, job in jobs().items()}
    (WORK / 'check.json').write_text(json.dumps({k: v for k, v in report.items() if v}, ensure_ascii=False, indent=1))
    bad = {k: v for k, v in report.items() if v and v != ['no output']}
    done = sum(1 for v in report.values() if not v)
    print(f'{done}/{len(report)} lessons pass, {len(bad)} with errors, '
          f'{sum(v == ["no output"] for v in report.values())} not written yet')
    return report


def necessary(sid):
    depth = {}

    def walk(i, d):
        for p in SKILLS[i]['prereqs']:
            if p not in depth or depth[p] > d:
                depth[p] = d
                walk(p, d + 1)
    walk(sid, 1)
    return [dict(id=i, title=SKILLS[i]['title'], level=SKILLS[i]['level'], depth=d)
            for i, d in sorted(depth.items(), key=lambda kv: (kv[1], kv[0]))]


def assemble():
    parts, report = bank_parts(), check()
    lessons = {}
    for sid, out in outputs().items():
        if report.get(sid):
            continue                      # only lessons that pass every check ship
        probs = []
        for pr in out['problems']:
            src = parts[pr['part']]
            q, p = src['q'], src['p']
            g = pr.get('graph')
            if g:
                f_ = parse_f(g['f'])
                g = dict(g, f=sp.jscode(f_), df=sp.jscode(sp.diff(f_, X)))
            target = ROOT / src['image']
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(WORKTREE / src['image'], target)
            probs.append(dict(source=q['source'].replace('LC Maths ', 'LC ').replace(' — ', ' · '),
                              part=p['label'], marks=p['marks'], image=src['image'], note=pr.get('note'),
                              legend=pr['legend'], steps=pr['steps'], final=pr['final'],
                              svg=p['workedSolution'].get('svg'), graph=g))
        s = SKILLS[sid]
        lessons[sid] = dict(id=sid, title=s['title'], level=s['level'], chapter=s['chapter'],
                            necessary=necessary(sid), problems=probs)
    js = ('// Maths skill lessons, generated by pipeline/requirements/maths/lessons.py. Do not edit by hand.\n'
          'window.MATHS_LESSONS = ' + json.dumps(lessons, ensure_ascii=False) + ';\n'
          'window.MATHS_CHAPTERS = ' + json.dumps(json.loads((HERE / 'skills.json').read_text())['chapters'], ensure_ascii=False) + ';\n')
    (ROOT / 'maths-lessons.js').write_text(js)
    print(f'{len(lessons)} lessons → maths-lessons.js')


def fix():
    """Pack every failing lesson with its errors into fix/Fnn.json for a repair agent (see FIX.md)."""
    report, outs, js = check(), outputs(), jobs()
    bad = [sid for sid, errs in report.items() if errs and errs != ['no output']]
    d = WORK / 'fix'
    d.mkdir(exist_ok=True)
    (WORK / 'fixed').mkdir(exist_ok=True)
    for old in d.glob('F*.json'):
        old.unlink()
    for n in range(0, len(bad), PER_BATCH):
        batch = [dict(skill=js[sid]['skill'], errors=report[sid], candidates=js[sid]['candidates'], lesson=outs[sid]['problems'])
                 for sid in bad[n:n + PER_BATCH]]
        (d / f'F{n // PER_BATCH + 1:02}.json').write_text(json.dumps(batch, ensure_ascii=False, indent=1))
    print(f'{len(bad)} failing lessons → {(len(bad) + PER_BATCH - 1) // PER_BATCH} fix batches in {d}')


if __name__ == '__main__':
    {'pack': pack, 'check': check, 'assemble': assemble, 'fix': fix}[sys.argv[1]]()
