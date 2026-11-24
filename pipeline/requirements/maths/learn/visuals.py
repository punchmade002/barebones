"""Figures for the maths Learn page's worked examples: generated, then checked by a separate reader looking at the real page.

  python3 visuals.py pack                 # skills that need a new figure (triage.json) → in/Vnn.json, 4 per batch
  python3 visuals.py checks               # every skill that will show a figure or graph → check/Cnn.json, 6 per batch
  python3 visuals.py render <batch|id>…   # screenshot each skill's worked example on maths-learn.html → png/<id>.png
  python3 visuals.py status               # what passed, what failed, what is still unchecked

Writers (INSTRUCTIONS.md) draw with figlib.py and save {skill: svg} to out/Vnn.json; render shows their SVG in
place of the page's own figure. Checkers (CHECK.md) read the screenshots and write verdicts/Cnn.json.
package.py then publishes a figure only if its latest verdict passed; a figure that failed is dropped,
because no picture is better than a wrong one.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / 'visuals'
MATHS = HERE.parent
ROOT = MATHS.parents[2]
PER_WRITE, PER_CHECK = 4, 6


def learn_data():
    s = (MATHS / 'build/maths-learn.js').read_text()
    return json.loads(s[s.index('{'):s.rindex('}') + 1])


def batches(prefix, folder='out'):
    return sorted((WORK / folder).glob(f'{prefix}*.json'))


def new_svgs():
    """the latest SVG each writer saved, by skill (later batches and fixes win)"""
    svgs = {}
    for f in batches('V'):
        svgs.update(json.loads(f.read_text()))
    return svgs


def fingerprint(sid, svgs):
    """what a check looked at: a writer's SVG (by hash) or the page's own graph or figure"""
    return hashlib.sha1(svgs[sid].encode()).hexdigest()[:12] if sid in svgs else 'page'


def verdicts():
    """latest verdict per skill, with `of`: the fingerprint of the figure that check batch was made for"""
    out = {}
    for f in batches('C', 'verdicts'):
        of = {x['skill']: x['of'] for x in json.loads((WORK / 'check' / f.name).read_text())}
        for sid, v in json.loads(f.read_text()).items():
            out[sid] = v | {'of': of.get(sid)}
    return out


def example(sid, L):
    s = L[sid]
    return {'question': s['example']['question'], 'final': s['example']['final'],
            'steps': [{'say': st['say'], 'rows': st['rows']} for st in s['example']['steps']]}


def write_batches(prefix, folder, items, per):
    (WORK / folder).mkdir(parents=True, exist_ok=True)
    start = len(batches(prefix, folder))
    for k in range(0, len(items), per):
        (WORK / folder / f'{prefix}{start + k // per + 1:02d}.json').write_text(json.dumps(items[k:k + per], ensure_ascii=False, indent=1))
    print(f'{len(items)} skills → {(len(items) + per - 1) // per} batches from {prefix}{start + 1:02d}')


def pack():
    """batch every skill that needs a figure and has neither a passing one nor one waiting to be drawn or checked;
    a figure a checker rejected comes back with its `issues` for the writer to fix"""
    L, T, svgs, V = learn_data(), json.loads((WORK / 'triage.json').read_text()), new_svgs(), verdicts()
    waiting = {x['skill'] for f in batches('V', 'in') for x in json.loads(f.read_text())} - set(svgs)
    todo = []
    for sid, t in T.items():
        if not t['need'] or sid in waiting:
            continue
        v = V.get(sid) if sid in V and V[sid]['of'] == fingerprint(sid, svgs) else None
        page_ok = (L[sid]['graph'] or L[sid]['diagram']) and t.get('keep') is not False
        if sid in svgs or page_ok:
            if v and not v['ok']:
                todo.append((sid, v['issues']))          # rejected: draw it again
        else:
            todo.append((sid, None))                     # nothing yet
    write_batches('V', 'in', [{'skill': sid, 'title': L[sid]['title'], 'show': T[sid]['show'], 'example': example(sid, L)}
                              | ({'issues': issues} if issues else {}) for sid, issues in todo], PER_WRITE)


def shown(L):
    """skill → what its worked example will show: 'new' (a writer's SVG), 'page' (its own graph or figure), or None"""
    svgs, T = new_svgs(), json.loads((WORK / 'triage.json').read_text())
    out = {}
    for sid, s in L.items():
        if sid in svgs:
            out[sid] = 'new'
        elif (s['diagram'] or s['graph']) and T.get(sid, {}).get('keep') is not False:
            out[sid] = 'page'
    return out


def checks():
    """batch every skill whose figure has not passed a check of the exact figure it will now show"""
    L, svgs, V = learn_data(), new_svgs(), verdicts()
    todo = [sid for sid in shown(L) if not (sid in V and V[sid]['of'] == fingerprint(sid, svgs))]
    T = json.loads((WORK / 'triage.json').read_text())
    write_batches('C', 'check', [{'skill': sid, 'of': fingerprint(sid, svgs), 'title': L[sid]['title'], 'show': T.get(sid, {}).get('show'),
                                  'example': example(sid, L)} for sid in todo], PER_CHECK)


def render(args):
    from playwright.sync_api import sync_playwright
    ids = []
    for a in args:
        f = next((p for p in [WORK / 'in' / f'{a}.json', WORK / 'check' / f'{a}.json'] if p.exists()), None)
        ids += [x['skill'] for x in json.loads(f.read_text())] if f else [a]
    svgs = new_svgs()
    (WORK / 'png').mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1200, 'height': 900}, device_scale_factor=1)
        for sid in ids:
            page.goto(f'file://{ROOT}/maths-learn.html?skill={sid}')
            page.wait_for_selector('#example .answer', timeout=15000)
            if sid in svgs:                     # the writer's figure, in the place the page will show it
                page.evaluate('''svg => { const ex = document.querySelector('#example .ex'); ex.classList.remove('solo');
                  let g = ex.querySelector('.graph'); if (!g) { g = document.createElement('div'); g.className = 'graph'; ex.append(g) }
                  g.innerHTML = svg; fit() }''', svgs[sid])
            page.locator('#example').screenshot(path=str(WORK / 'png' / f'{sid}.png'))
            print('png/' + sid + '.png')
        browser.close()


def status():
    L, svgs, V = learn_data(), new_svgs(), verdicts()
    S = shown(L)
    def current(sid):
        v = V.get(sid)
        return v if v and v['of'] == fingerprint(sid, svgs) else None
    passed = [s for s in S if (current(s) or {}).get('ok')]
    failed = [s for s in S if current(s) and not current(s)['ok']]
    print(f'{len(S)} skills show a figure: {len(passed)} passed, {len(failed)} failed, {len(S) - len(passed) - len(failed)} unchecked')
    for s in failed:
        print(' ', s, '|', '; '.join(current(s)['issues'])[:200])


def usable():
    """skill → (graph, diagram) to publish: only figures whose latest check of that exact figure passed"""
    L, svgs, V = learn_data(), new_svgs(), verdicts()
    out = {}
    for sid, kind in shown(L).items():
        v = V.get(sid)
        ok = v and v.get('ok') and v['of'] == fingerprint(sid, svgs)
        if kind == 'new':
            out[sid] = (None, svgs[sid] if ok else None)
        else:
            out[sid] = (L[sid]['graph'], L[sid]['diagram']) if ok else (None, None)
    return out


if __name__ == '__main__':
    cmd = sys.argv[1]
    {'pack': pack, 'checks': checks, 'render': lambda: render(sys.argv[2:]), 'status': status}[cmd]()
