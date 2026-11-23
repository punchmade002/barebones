"""Write practice problems for skills with fewer than 3 exam parts, so every skill gets a 3-problem lesson.

  python3 pipeline/requirements/maths/practice.py pack [skill ...]   # practice/in/WNN.json, 4 skills each
  python3 pipeline/requirements/maths/practice.py check              # practice/out/*.json → practice/check.json
  python3 pipeline/requirements/maths/practice.py merge              # passing problems → practice-bank.json

A Sonnet writer (practice/INSTRUCTIONS.md) writes exam-style problems with worked solutions in the bank's
format. `check` proves the maths two ways with the bank rebuild's SymPy checker (maths_verify.py): every
line's `sym` must follow from the line before, and `answerSym`, the answer worked out independently
from the question, must equal `finalSym`. lessons.py then treats practice-bank.json like exam parts.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WORK = HERE / 'practice'
PER_BATCH = 4
sys.path.insert(0, str(ROOT / '.claude/worktrees/maths-older/pipeline/rebuild'))
sys.path.insert(0, str(HERE))
import maths_verify as mv  # noqa: E402
from lessons import SKILLS, SKIP_YEAR, bank_parts, bare_tex  # noqa: E402

# taught on the whiteboard only: constructions and formal geometry proofs have no answer to check
LEARN_ONLY = re.compile(r'^(con-|geo-prove-|geo-cuts$)')


def exam_parts():
    tags = json.loads((HERE / 'skill-tags.json').read_text())
    by = {}
    for pid, t in tags.items():
        if t['primary'] and SKIP_YEAR not in pid:
            by.setdefault(t['primary'], []).append(pid)
    return by


def todo():
    """{skill: problems to write} for every skill short of 3 exam parts, except learn-only ones."""
    by = exam_parts()
    return {s: 3 - len(by.get(s, [])) for s in SKILLS if len(by.get(s, [])) < 3 and not LEARN_ONLY.match(s)}


def pack(only=None):
    need, parts, by = todo(), bank_parts(), exam_parts()
    tags = json.loads((HERE / 'skill-tags.json').read_text())
    path = HERE / 'practice-bank.json'
    done = {v['skill'] for v in json.loads(path.read_text()).values()} if path.exists() and not only else set()
    sids = [s for s in sorted(need, key=lambda s: (int(SKILLS[s]['chapter'][5:]), SKILLS[s].get('rank', 0)))
            if (not only or s in only) and s not in done]
    jobs = []
    for sid in sids:
        s = SKILLS[sid]
        # style references: its own exam parts, else parts that use it as a step (worked solutions only)
        refs = by.get(sid) or [p for p, t in tags.items() if sid in t['skills'] and SKIP_YEAR not in p][:2]
        jobs.append(dict(
            skill=dict(id=sid, title=s['title'], level=s['level'], input=s['input'], output=s['output'],
                       example=s['example'], needs=[SKILLS[p]['title'] for p in s['prereqs']]),
            write=need[sid], examParts=len(by.get(sid, [])),
            references=[dict(part=p, level=parts[p]['q']['level'], marks=parts[p]['p']['marks'],
                             steps=parts[p]['p']['workedSolution']['steps'], final=parts[p]['p']['workedSolution']['finalAnswer'])
                        for p in refs[:2] if p in parts]))
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    (WORK / 'out').mkdir(exist_ok=True)
    for n in range(0, len(jobs), PER_BATCH):
        (WORK / 'in' / f'W{n // PER_BATCH + 1:02}.json').write_text(json.dumps(jobs[n:n + PER_BATCH], ensure_ascii=False))
    print(f'{len(jobs)} skills, {sum(j["write"] for j in jobs)} problems → {(len(jobs) + PER_BATCH - 1) // PER_BATCH} batches')


def unescape_newlines(s):
    """Writers often double-escape \\n in JSON; outside $…$ a literal backslash-n can only mean a line break."""
    return re.sub(r'(\$[^$]*\$)|\\n', lambda m: m[1] or '\n', s)


assert unescape_newlines('a\\nb $\\neq$') == 'a\nb $\\neq$'


def as_answer(text):
    """answerSym is computed, so solve()/div() hand back a list or tuple that parse() reads as one value."""
    kind, v = mv.parse(text)
    return ('list', list(v)) if kind == 'one' and isinstance(v, (list, tuple, mv.sp.Tuple)) else (kind, v)


def check_problem(pr):
    errs = []
    if isinstance(pr.get('question'), str):
        pr['question'] = unescape_newlines(pr['question'])
    for st in (pr.get('workedSolution') or {}).get('steps') or []:
        for ln in st.get('lines', []):
            if 'text' in ln:
                ln['text'] = unescape_newlines(ln['text'])
    for f in ('question', 'level', 'marks', 'workedSolution', 'finalSym', 'answerSym'):
        if not pr.get(f):
            errs.append(f'missing {f}')
    if errs:
        return errs
    if pr['level'] not in ('higher', 'ordinary'):
        errs.append(f'level {pr["level"]!r}')
    if bare_tex(pr['question']):
        errs.append('question has LaTeX outside $…$')
    steps = pr['workedSolution'].get('steps') or []
    if not steps or not pr['workedSolution'].get('finalAnswer'):
        errs.append('needs steps and a finalAnswer')
    for k, st in enumerate(steps, 1):
        for ln in st.get('lines', []):
            if 'text' in ln and bare_tex(ln['text']):
                errs.append(f'step {k}: text line has LaTeX outside $…$')
    errs += [f"step {i['step']} line {i['line']}: {i['status']}: {i['detail']}" for i in mv.check_lines(pr) if i['status'] != 'unknown']
    if not any('sym' in ln for st in steps for ln in st.get('lines', [])):
        errs.append('no sym on any line: the working cannot be checked')
    try:
        approx = '.' in pr['finalSym']   # an answer rounded to the cents or decimals shown
        same = mv.safe_equivalent(as_answer(pr['answerSym']), mv.parse(pr['finalSym']),
                                  mv.tolerance(pr['answerSym'], pr['finalSym'], approx=approx))
        if same is not True:
            errs.append(f'answerSym {pr["answerSym"]} does not give finalSym {pr["finalSym"]}' if same is False
                        else f'could not compare answerSym {pr["answerSym"]} with finalSym {pr["finalSym"]}')
    except Exception as exc:
        errs.append(f'answerSym/finalSym: {exc}'[:200])
    return errs


def check(batch=None):
    """All batches → check.json; with a batch name, just print that batch's problems (writers self-check)."""
    need, report, ok = todo(), {}, {}
    for f in sorted((WORK / 'out').glob(f'{batch or "W*"}.json')):
        for job in json.loads(f.read_text()):
            sid, probs = job['skill'], job.get('problems', [])
            errs = {f'{sid}#{k + 1}': check_problem(p) for k, p in enumerate(probs)}
            if len(probs) != need.get(sid):
                errs[sid] = [f'wrote {len(probs)} problems, needed {need.get(sid)}']
            report.update({k: v for k, v in errs.items() if v})
            ok[sid] = [p for k, p in enumerate(probs) if not errs.get(f'{sid}#{k + 1}')]
    if batch:
        print('\n'.join(f'{k}: {e}' for k, v in report.items() for e in v) or f'{batch}: all problems pass')
        return ok
    (WORK / 'check.json').write_text(json.dumps(report, ensure_ascii=False, indent=1))
    good = sum(len(v) for v in ok.values())
    print(f'{good} problems pass, {len(report)} with errors, across {len(ok)} skills (of {len(need)} to fill)')
    return ok


def merge():
    """Passing problems → practice-bank.json, keyed practice-<skill>-<n>; a re-run replaces that skill's entries."""
    path = HERE / 'practice-bank.json'
    bank = json.loads(path.read_text()) if path.exists() else {}
    for sid, probs in check().items():
        bank = {k: v for k, v in bank.items() if v['skill'] != sid}
        for k, p in enumerate(probs, 1):
            bank[f'practice-{sid}-{k}'] = dict(p, skill=sid)
    path.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(bank)} practice problems in {path.name}')


assert LEARN_ONLY.match('con-3') and LEARN_ONLY.match('geo-prove-thm11') and not LEARN_ONLY.match('geo-thm9')

if __name__ == '__main__':
    {'pack': lambda: pack(sys.argv[2:]), 'check': lambda: check(*sys.argv[2:3]), 'merge': merge}[sys.argv[1]]()
