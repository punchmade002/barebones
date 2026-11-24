"""Material for a skill's Learn phase (the whiteboard before its practice problems).

  python3 pipeline/requirements/maths/learn.py scheme <skill id>   # learn/scheme/<skill>.json: marking-scheme text per exam part
  python3 pipeline/requirements/maths/learn.py pack [skill ...]    # learn/in/Bnn.json for Sonnet writers (learn/INSTRUCTIONS.md)
  python3 pipeline/requirements/maths/learn.py check [BATCH]       # learn/out/*.json → learn/check.json (a batch name prints it)
  python3 pipeline/requirements/maths/learn.py assemble            # passing skills → build/maths-learn.js (then package.py)

Facts (chapter, rank, needs, leads to, how often it is examined) come from the skills database and the exam
tags. A writer adds what the skill does, a worked example (checked with SymPy like a practice problem), an
optional graph (checked like a lesson graph) and exam tips whose quotes are checked against the scheme text.
The scheme text comes from the official marking-scheme PDFs, split by question with the page map in
.claude/worktrees/maths-older/pipeline/rebuild/maths_crops.py (scheme_pages).
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WORK = HERE / 'learn'
sys.path.insert(0, str(ROOT / '.claude/worktrees/maths-older/pipeline/rebuild'))
sys.path.insert(0, str(HERE))
import maths_crops as mc  # noqa: E402

SKIP_YEAR = '-2026-'     # 2026 papers are not on this branch's bank
YEARS = range(2015, 2026)
LEVELS = ('higher', 'ordinary')
PER_BATCH = 4
PARTS_PER_LEVEL = 6      # scheme extracts a writer sees per level: main-skill parts first, then the most recent
SCHEME_CHARS = 2000


@lru_cache(None)
def pages(year, level):
    return mc.scheme_pages(year, level)[0]


@lru_cache(None)
def scheme_text(year, level, paper, q):
    doc = fitz.open(mc.PAPERS / f'{year}-{level}-marking-scheme.pdf')
    return '\n'.join(doc[p - 1].get_text() for p in pages(year, level).get((paper, q), []))


def tidy(t):
    """PDF text keeps one token per line and odd glyphs for superscripts; squash it for reading."""
    t = re.sub(r'[ \t]+', ' ', t.replace('ଶ', '²').replace('ଷ', '³'))
    return re.sub(r'\n\s*\n+', '\n', t).strip()


def parse_pid(pid):
    m = re.search(r'(\d{4})-(higher|ordinary)-p(\d)-q(\d+)#(.*)', pid)
    return int(m[1]), m[2], int(m[3]), int(m[4]), m[5]


@lru_cache(None)
def tags():
    return {p: t for p, t in json.loads((HERE / 'skill-tags.json').read_text()).items() if SKIP_YEAR not in p}


def scheme(sid):
    out = []
    for pid, t in sorted(tags().items()):
        if sid not in t['skills']:
            continue
        year, level, paper, q, label = parse_pid(pid)
        out.append(dict(part=pid, level=level, year=year, paper=paper, question=q, label=label,
                        mainSkill=t['primary'] == sid, scheme=tidy(scheme_text(year, level, paper, q))))
    d = WORK / 'scheme'
    d.mkdir(parents=True, exist_ok=True)
    (d / f'{sid}.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    empty = [o['part'] for o in out if not o['scheme']]
    print(f'{sid}: {len(out)} parts, {len(empty)} with no scheme text {empty[:3]}')


def excerpt(text, label):
    """The scheme covers the whole question; start near the part's first label, e.g. (b) of (b)(ii)."""
    m = re.match(r'\(\w+\)', label)
    i = text.find(m[0]) if m else -1
    start = max(0, i - 150) if i >= 0 else 0
    return text[start:start + SCHEME_CHARS]


def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()


assert excerpt('intro (a) one (b) two', '(b)(ii)').endswith('(b) two') and norm(' A\n b ') == 'a b'


# ── facts: everything that is counted, not written ──
def facts(sid):
    from lessons import SKILLS
    from lessons import outputs
    s, chapters = SKILLS[sid], json.loads((HERE / 'skills.json').read_text())['chapters']
    have = set(json.loads((HERE / 'build/maths-lessons.js').read_text().split('window.MATHS_LESSONS = ', 1)[1].split(';\n', 1)[0]))
    node = lambda i: dict(id=i, title=SKILLS[i]['title'], grade=SKILLS[i].get('grade'), lesson=i in have)
    exam = {}
    for lv in LEVELS:
        by, main = [0] * len(YEARS), 0
        for pid, t in tags().items():
            year, level, *_ = parse_pid(pid)
            if level == lv and sid in t['skills']:
                by[year - YEARS[0]] += 1
                main += t['primary'] == sid
        exam[lv] = dict(byYear=by, main=main)
    ch = chapters[s['chapter']] if isinstance(chapters, dict) else next(c for c in chapters if c['id'] == s['chapter'])
    return dict(id=sid, title=s['title'], level=s['level'], grade=s.get('grade'), chapter=ch['title'] if isinstance(ch, dict) else ch,
                rank=s.get('rank'), ofRank=sum(1 for v in SKILLS.values() if v['chapter'] == s['chapter']),
                needs=[node(p) for p in s['prereqs']], leadsTo=[node(u) for u in s.get('usedBy', [])],
                exam=exam, lesson=sid in have)


def sources(sid, level):
    """The scheme extracts a writer sees for one level, and the full text quotes are checked against."""
    rows = []
    for pid, t in tags().items():
        year, lv, paper, q, label = parse_pid(pid)
        if lv == level and sid in t['skills']:
            rows.append((t['primary'] != sid, -year, pid, paper, q, label, year))
    seen, out = set(), []
    for _, _, pid, paper, q, label, year in sorted(rows):
        if (year, paper, q) in seen or len(out) == PARTS_PER_LEVEL:
            continue
        seen.add((year, paper, q))
        full = tidy(scheme_text(year, level, paper, q))
        if full:
            out.append(dict(part=pid, year=year, label=label, main=tags()[pid]['primary'] == sid, full=full,
                            scheme=excerpt(full, label)))
    return out


def pack(only=()):
    from lessons import SKILLS
    done = {o['skill'] for f in (WORK / 'out').glob('*.json') for o in json.loads(f.read_text())} if not only else set()
    sids = [s for s in sorted(SKILLS, key=lambda s: (int(SKILLS[s]['chapter'][5:]), SKILLS[s].get('rank', 0)))
            if (s in only if only else s not in done)]
    jobs = []
    for sid in sids:
        s, f = SKILLS[sid], facts(sid)
        jobs.append(dict(
            skill=dict(id=sid, title=s['title'], level=s['level'], input=s['input'], output=s['output'], example=s['example'],
                       needs=[n['title'] for n in f['needs']], leadsTo=[n['title'] for n in f['leadsTo']],
                       learnOnly=not f['lesson']),
            exam={lv: dict(partsPerYear=dict(zip(map(str, YEARS), f['exam'][lv]['byYear'])), mainSkillParts=f['exam'][lv]['main'])
                  for lv in LEVELS},
            schemes={lv: [{k: v for k, v in x.items() if k != 'full'} for x in sources(sid, lv)] for lv in LEVELS}))
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    (WORK / 'out').mkdir(exist_ok=True)
    n0 = len(list((WORK / 'in').glob('B*.json')))
    for i in range(0, len(jobs), PER_BATCH):
        (WORK / 'in' / f'B{n0 + i // PER_BATCH + 1:02}.json').write_text(json.dumps(jobs[i:i + PER_BATCH], ensure_ascii=False))
    print(f'{len(jobs)} skills → {(len(jobs) + PER_BATCH - 1) // PER_BATCH} batches from B{n0 + 1:02}')


# ── checks ──
def check_learn(sid, o):
    from lessons import bare_tex, check_graph, SKILLS
    from practice import check_problem, has_control
    errs, f = [], facts(sid)
    if has_control(o):
        errs.append('control character: a single backslash such as \\frac or \\theta was read as a JSON escape')
    w = o.get('what') or {}
    if not (isinstance(w.get('say'), list) and 1 <= len(w['say']) <= 3 and w.get('in') and w.get('out')):
        errs.append('what needs say (1–3 sentences), in and out')
    for t in (w.get('say') or []) + [w.get('in', ''), w.get('out', '')] + list((o.get('how') or {}).values()):
        if bare_tex(t):
            errs.append(f'LaTeX outside $…$: {t[:60]}')
    levels = [lv for lv in LEVELS if f['exam'][lv]['byYear'] != [0] * len(YEARS)]
    for lv in levels:
        if not (o.get('how') or {}).get(lv):
            errs.append(f'how.{lv} missing (it is examined at {lv} level)')
    ex = o.get('example') or {}
    steps = (ex.get('workedSolution') or {}).get('steps') or []
    if not steps or any(not st.get('say') or bare_tex(st['say']) for st in steps):
        errs.append('example: every step needs a say sentence (maths inside $…$)')
    if f['lesson']:
        errs += [f'example: {e}' for e in check_problem(ex)]
    elif not (ex.get('question') and steps and ex['workedSolution'].get('finalAnswer')):
        errs.append('example needs question, steps and a finalAnswer')
    if o.get('graph'):
        errs += check_graph(o['graph'])
    if o.get('diagram') is not None and not str(o['diagram']).lstrip().startswith('<svg'):
        errs.append('diagram must be an SVG string or null')
    for lv in LEVELS:
        srcs = {x['part']: x['full'] for x in sources(sid, lv)}
        tips = (o.get('tips') or {}).get(lv) or []
        if len(tips) > 4:
            errs.append(f'tips.{lv}: at most 4')
        for k, tp in enumerate(tips, 1):
            if bare_tex(tp.get('tip', '')):
                errs.append(f'tips.{lv} {k}: LaTeX outside $…$')
            if not tp.get('sources'):
                errs.append(f'tips.{lv} {k}: no sources')
            for src in tp.get('sources', []):
                if src.get('part') not in srcs:
                    errs.append(f"tips.{lv} {k}: {src.get('part')} is not one of this level's scheme parts")
                elif norm(src.get('quote', '')) not in norm(srcs[src['part']]) or len(norm(src.get('quote', ''))) < 8:
                    errs.append(f"tips.{lv} {k}: quote not in the {src['part']} scheme: {src.get('quote', '')[:60]}")
    return errs


def outputs():
    return {o['skill']: o for f in sorted((WORK / 'out').glob('B*.json')) for o in json.loads(f.read_text())}


def check(batch=None):
    outs = {o['skill']: o for f in sorted((WORK / 'out').glob(f'{batch}.json')) for o in json.loads(f.read_text())} if batch else outputs()
    report = {sid: check_learn(sid, o) for sid, o in outs.items()}
    bad = {k: v for k, v in report.items() if v}
    if batch:
        print('\n'.join(f'{k}: {e}' for k, v in bad.items() for e in v) or f'{batch}: all skills pass')
        return report
    (WORK / 'check.json').write_text(json.dumps(bad, ensure_ascii=False, indent=1))
    print(f'{len(report) - len(bad)}/{len(report)} skills pass')
    return report


def rows(lines):
    """Lesson-style lines → whiteboard rows: 'lhs &= rhs' splits on the first &, text becomes an aside."""
    from lessons import brace_scripts
    out = []
    for ln in lines:
        if 'tex' in ln:
            t = brace_scripts(ln['tex'])
            l, _, r = t.partition('&')
            out.append(dict(l=l.strip(), r=r.strip()) if _ else dict(full=t))
        else:
            out.append(dict(aside=ln['text']))
    return out


assert rows([{'tex': 'x &= 2'}, {'text': 'so'}, {'tex': 'y'}]) == [{'l': 'x', 'r': '= 2'}, {'aside': 'so'}, {'full': 'y'}]


def assemble():
    import sympy as sp
    from lessons import parse_f, X
    report, learn = check(), {}
    for sid, o in outputs().items():
        if report.get(sid):
            continue
        ex, g = o['example'], o.get('graph')
        if g:
            f_ = parse_f(g['f'])
            g = dict(g, f=sp.jscode(f_))
        learn[sid] = dict(facts(sid), what=o['what'], how=o.get('how') or {}, graph=g, diagram=o.get('diagram'),
                          example=dict(question=ex['question'], final=ex['workedSolution']['finalAnswer'],
                                       steps=[dict(title=st['title'], say=st['say'], rows=rows(st['lines'])) for st in ex['workedSolution']['steps']]),
                          tips={lv: [dict(tip=t['tip'], years=sorted({parse_pid(s['part'])[0] for s in t['sources']}))
                                     for t in (o.get('tips') or {}).get(lv) or []] for lv in LEVELS})
    (HERE / 'build/maths-learn.js').write_text('// Maths Learn phase, generated by pipeline/requirements/maths/learn.py. Do not edit by hand.\n'
                                         'window.MATHS_LEARN = ' + json.dumps(learn, ensure_ascii=False) + ';\n')
    print(f'{len(learn)} skills → maths-learn.js')


if __name__ == '__main__':
    {'scheme': lambda: scheme(sys.argv[2]), 'pack': lambda: pack(sys.argv[2:]), 'check': lambda: check(*sys.argv[2:3]),
     'assemble': assemble}[sys.argv[1]]()
