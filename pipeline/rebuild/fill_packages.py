"""Package a subject's parts for the answer fill (the Chemistry recipe, any subject).

    python3 pipeline/rebuild/fill_packages.py <subject> [--split]

--split only prints the short/long split with examples. Otherwise writes:
  <DATA>/<subject>/fill/pNN.json      short-answer packages for the Haiku writers
  <DATA>/<subject>/fill/lNN.json      long-answer packages for the Sonnet writers (LONG_SIZE questions)
  <DATA>/<subject>/fill/packages.json the package lists and the fixed-seed check sample

Targets are every part without an audited old answer under the exact same label (off-spec parts
included: they keep their offSpec tag). Short questions are sorted by paper and cut into packages
of SIZE questions, also capped at MAX_PARTS parts and MAX_KB: a 102-part Chemistry package made
Haiku drop 25 answers. Each file is a JSON array with one item per line (Read truncates lines over
2,000 characters): a question's shared context (case study, data table) goes on its own line(s)
ahead of its parts. A hint is an earlier answer whose label contains, or is contained by, this
part's label: audited old answers first, else the previous bank's answer (unaudited, so flagged).
"""
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path.home() / 'barebones/pipeline/_data/rebuild'
SIZE, LONG_SIZE, THIRTY_SIZE = 10, 5, 5
NOTES_SIZE = 40          # History notes packages: parts of one chapter per Haiku agent
MAX_PARTS, MAX_KB = 50, 50
HINT_CHARS, LINE_CHARS = 500, 1800
SEED = 20261109


def lab(s):
    return re.sub(r'\s+', '', s or '')


def order(key):
    y, level, q = key.split('-')
    return int(y), level, int(q[1:])


def is_long(subject, p):
    """A part whose full-marks answer runs to more than a paragraph (see README of the split)."""
    if subject == 'pe':
        # Worth 10+ marks (a Section C or case-study part: several developed points or rows), or
        # an 8-9 mark part the scan tagged long-answer (one levels-of-response discussion, e.g.
        # "Describe how mass participation events provide opportunities for business").
        # 8-mark "outline/describe two ..." (2 x 4) and anything under 8 marks stay short.
        marks = p.get('marks') or 0
        return marks >= 10 or (marks >= 8 and 'long-answer' in (p.get('type') or []))
    if subject == 'geography':
        # An essay or discussion the scheme marks in SRPs/aspects, worth 15+ marks (40-mark OL B,
        # 80-mark HL options, 15-27 mark essays). 30-mark one-part essays are is_thirty() instead.
        return 'long-answer' in (p.get('type') or []) and (p.get('marks') or 0) >= 15 and not is_thirty(subject, p)
    if subject == 'history':
        # More than a paragraph: HL essays (100 marks, CM by paragraph) and HL DBQ contextualisation
        # (40 marks, CM 24 by paragraph). OL B ("a short paragraph"), OL C ("a longer paragraph")
        # and OL DBQ Q4 (4 Core Statements) are one paragraph each and stay short.
        marks = p.get('marks') or 0
        return 'long-answer' in (p.get('type') or []) and (marks >= 100 or (p['label'] == '4' and marks >= 40))
    return 'long-answer' in (p.get('type') or [])


def is_notes(subject, key, p):
    """History parts the scheme gives no content for, marked by 5-mark Core Statements: OL B and C
    paragraphs and the OL DBQ's question 4. They go in packages of one chapter, with that
    chapter's notes index, so the writer reads the notes once for many parts."""
    if subject != 'history' or '-ordinary-' not in key:
        return False
    return p['label'] == '4' if key.endswith('-q1') else p['label'][:1] in ('B', 'C')


def is_thirty(subject, p):
    """Geography's 30-markers: a one-part essay worth 30 marks (HL/OL B and C, or one of its
    "answer (i) or (ii)" alternatives). 30-mark A parts are skills questions and stay short."""
    return (subject == 'geography' and p.get('marks') == 30 and 'long-answer' in (p.get('type') or [])
            and not re.sub(r'^\d+', '', p['label']).startswith('A'))


def old_answers(subject, key):
    """{label: answer} from old-answers/<key>.txt (entries may run over several lines)."""
    path = BASE / subject / 'old-answers' / f'{key}.txt'
    out, cur = {}, None
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        m = re.match(r'(\(\S*\)|) ?\[(?:kept|written)\]: (.*)', line)
        if m:
            cur = lab(m.group(1))
            out[cur] = (out[cur] + '\n' + m.group(2)) if cur in out else m.group(2)
        elif cur is not None:
            out[cur] += '\n' + line
    return out


def previous_bank(subject):
    """{key: {label: answer}} from the bank file currently shipped (unaudited; hints only)."""
    path = ROOT / f'{subject}-exam-questions.js'
    if not path.exists():
        return {}
    s = path.read_text()
    db = json.loads(s[s.index('.concat(') + 8:s.rindex(')')])
    out = {}
    if subject == 'history':
        return history_bank(db)
    for q in db:
        g = re.search(r'(Higher|Ordinary) (\d{4}) (?:Paper|Part) (1|2|One|Two) — Q(\d+)([ABC]?)$', q.get('source', ''))
        if subject == 'geography' and g:
            n = int(g.group(4))
            two = g.group(3) in ('2', 'Two')
            key = f'{g.group(2)}-{g.group(1).lower()}-q{100 + n if two else n}'
            def glab(label, letter=g.group(5), n=n):   # old split questions ("Q1A", label "A" or "(i)")
                if not letter:
                    return lab(label)
                return lab(f'{n}{label}' if label == letter else f'{n}{letter}{label}')
            out.setdefault(key, {}).update({glab(p.get('label')): p.get('model', '') for p in q['parts'] if p.get('model')})
            continue
        m = re.search(r'(Higher|Ordinary) (\d{4}).*Q(\d+)', q.get('source', ''))
        if q.get('level') and q.get('questionNumber'):
            key = f'{q["year"]}-{q["level"]}-q{q["questionNumber"]}'
        elif m:
            key = f'{m.group(2)}-{m.group(1).lower()}-q{m.group(3)}'
        else:
            continue
        out[key] = {lab(p.get('label')): p.get('model', '') for p in q['parts'] if p.get('model')}
    return out


def history_bank(db):
    """The old History bank numbers questions per topic ("Q1"-"Q4" of hist-ire1), so map by
    year, level and chapter: the DBQ's chapter (labels "1(a)" ... "4") is q1; a topic is q2-q13
    (Ireland N -> 1+N, Europe N -> 7+N). OL A "1"-"5" become "A1"-"A5"; OL B and C kept only one
    option with no number, so they give no hint."""
    out = {}
    for q in db:
        m = re.search(r'(Higher|Ordinary) (\d{4})', q.get('source', ''))
        ch = re.match(r'hist-(ire|eur)(\d)$', q.get('chapterId', ''))
        if not m or not ch:
            continue
        level, year = m.group(1).lower(), m.group(2)
        dbq = any('(' in (p.get('label') or '') for p in q['parts']) or (
            level == 'higher' and q['parts'] and q['parts'][0].get('marks') == 40) or (
            level == 'ordinary' and q['parts'] and q['parts'][0].get('marks') in (20, 10))
        num = 1 if dbq else (1 if ch.group(1) == 'ire' else 7) + int(ch.group(2))
        slot = out.setdefault(f'{year}-{level}-q{num}', {})
        for p in q['parts']:
            label, model = lab(p.get('label')), p.get('model', '')
            if not model or (level == 'ordinary' and not dbq and label in ('B', 'C')):
                continue
            if level == 'ordinary' and not dbq and label.isdigit():
                label = f'A{label}'
            slot[label] = model
    return out


def chunks(text, n):
    return [text[i:i + n] for i in range(0, len(text), n)] or ['']


def build(subject):
    data = BASE / subject
    prev = previous_bank(subject)
    short_q, long_q, thirty_q = [], [], []
    notes_by_chapter = {}
    counts = {'parts': 0, 'audited': 0, 'short': 0, 'long': 0, 'thirty': 0, 'notes': 0, 'offSpec': 0}
    for f in sorted((data / 'state').glob('*.json'), key=lambda p: order(p.name.split('.')[0])):
        if f.name.endswith('.scan.json'):
            continue
        st = json.loads(f.read_text())
        key = st['key']
        old = old_answers(subject, key)
        prior = prev.get(key, {})
        context = (st.get('context') or '').strip()
        s_items, l_items, t_items = [], [], []
        for p in st['parts']:
            counts['parts'] += 1
            counts['offSpec'] += bool(p.get('offSpec'))
            L = lab(p['label'])
            if not p.get('offSpec') and L in old:
                counts['audited'] += 1
                continue
            item = {'id': f'{key}|{p["label"]}', 'text': p['text'], 'marks': p['marks'],
                    'scheme': p.get('schemePoints') or [], 'rule': p.get('fullMarksRule', '')}
            if p['diagramRelation'] != 'none':
                item['figure'] = p['diagramRelation']
            if p.get('resource'):
                item['resource'] = p['resource']
            if is_thirty(subject, p) or is_long(subject, p):
                item['notes'] = p.get('loIds') or []
            hint = next((old[o] for o in old if o.startswith(L) or L.startswith(o)), '')
            if hint:
                item['hint'] = hint[:HINT_CHARS]
            else:
                hint = next((prior[o] for o in prior if o and (o.startswith(L) or L.startswith(o))), prior.get(L, ''))
                if hint:
                    item['hint_unchecked'] = hint[:HINT_CHARS]
            if is_notes(subject, key, p):
                chapter = (p.get('loIds') or ['?'])[0].rsplit('-s', 1)[0]
                item['notes'] = chapter
                notes_by_chapter.setdefault(chapter, []).append(item)
                counts['notes'] += 1
                continue
            if is_thirty(subject, p):
                t_items.append(item)
            elif is_long(subject, p):
                l_items.append(item)
            else:
                s_items.append(item)
        counts['short'] += len(s_items)
        counts['long'] += len(l_items)
        counts['thirty'] += len(t_items)
        ctx = [{'context': f'{key}' + (f' ({i + 1}/{n})' if n > 1 else ''), 'text': c}
               for n, cs in [(len(chunks(context, LINE_CHARS)), chunks(context, LINE_CHARS))]
               for i, c in enumerate(cs)] if context else []
        if s_items:
            short_q.append({'key': key, 'items': ctx + s_items})
        if l_items:
            long_q.append({'key': key, 'items': ctx + l_items})
        if t_items:
            thirty_q.append({'key': key, 'items': ctx + t_items})
    build.notes = notes_by_chapter
    return short_q, long_q, thirty_q, counts


def notes_packages(subject, by_chapter):
    """One chapter per package, NOTES_SIZE parts each; the first line lists the chapter's notes files."""
    index = (BASE / subject / 'notes' / 'INDEX.md').read_text().splitlines()
    out = []
    for chapter in sorted(by_chapter):
        lines = [l for l in index if l.startswith(f'- {chapter}-s')]
        # "<loId> — [ref] title" per section; the file is notes/<loId>.md (the prompt gives the folder)
        head = {'context': f'notes for {chapter}', 'text': '\n'.join(
            re.sub(r'\s+->\s+notes/.*$', '', l)[2:] for l in lines)}
        items = by_chapter[chapter]
        for i in range(0, len(items), NOTES_SIZE):
            out.append({'name': f'n{len(out):02d}', 'papers': [chapter], 'items': [head] + items[i:i + NOTES_SIZE]})
    return out


def cut(questions, size, prefix):
    packages, cur = [], []

    def flush():
        if cur:
            packages.append({'name': f'{prefix}{len(packages):02d}',
                             'papers': sorted({q['key'].rsplit('-', 1)[0] for q in cur}),
                             'items': [it for q in cur for it in q['items']]})

    for q in questions:
        nxt = cur + [q]
        parts = sum(1 for x in nxt for it in x['items'] if 'id' in it)
        kb = len(json.dumps([it for x in nxt for it in x['items']], ensure_ascii=False)) / 1024
        if cur and (len(nxt) > size or parts > MAX_PARTS or kb > MAX_KB):
            flush()
            cur = [q]
        else:
            cur = nxt
    flush()
    return packages


def write(path, items):
    lines = [json.dumps(it, ensure_ascii=False) for it in items]
    assert max(len(line) for line in lines) < 2000, f'{path}: a line is over 2,000 characters'
    path.write_text('[\n' + ',\n'.join(lines) + '\n]\n')


def main(subject, split_only):
    short_q, long_q, thirty_q, counts = build(subject)
    print(f'{subject}: {counts["parts"]} parts; {counts["audited"]} audited reuse; '
          f'{counts["short"]} short targets in {len(short_q)} questions; '
          f'{counts["long"]} long targets in {len(long_q)} questions; '
          f'{counts["thirty"]} 30-markers in {len(thirty_q)} questions; {counts["offSpec"]} off-spec')
    if counts['notes']:
        print(f'{counts["notes"]} notes-based parts (one chapter per package)')
    if split_only:
        rng = random.Random(SEED)
        for name, qs in (('SHORT', short_q), ('LONG', long_q), ('THIRTY', thirty_q)):
            items = [it for q in qs for it in q['items'] if 'id' in it]
            print(f'\n--- {name} examples')
            for it in rng.sample(items, min(5, len(items))):
                print(f'  {it["id"]} [{it["marks"]}m] {it["text"][:150]!r}')
        return
    out = BASE / subject / 'fill'
    out.mkdir(parents=True, exist_ok=True)
    short = cut(short_q, SIZE, 'p')
    longp = cut(long_q, LONG_SIZE, 'l')
    thirty = cut(thirty_q, THIRTY_SIZE, 't')
    notesp = notes_packages(subject, getattr(build, 'notes', {}))
    for p in short + longp + thirty + notesp:
        write(out / f'{p["name"]}.json', p['items'])
    sample = sorted(random.Random(SEED).sample(range(len(short)), min(5, len(short))))
    (out / 'packages.json').write_text(json.dumps(
        {'short': [p['name'] for p in short], 'long': [p['name'] for p in longp],
         'thirty': [p['name'] for p in thirty], 'notes': [p['name'] for p in notesp],
         'notesSample': sorted(random.Random(SEED).sample(range(len(notesp)), min(3, len(notesp)))),
         'sample': sample}, indent=1))
    for kind, ps in (('short', short), ('long', longp), ('thirty', thirty), ('notes', notesp)):
        sizes = [sum(1 for it in p['items'] if 'id' in it) for p in ps]
        kbs = [len(json.dumps(p['items'], ensure_ascii=False)) // 1024 for p in ps]
        print(f'{kind}: {len(ps)} packages, parts/package max {max(sizes, default=0)}, KB max {max(kbs, default=0)}')
    print('sample', [short[i]['name'] for i in sample])


if __name__ == '__main__':
    main(sys.argv[1], '--split' in sys.argv)
