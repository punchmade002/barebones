"""Scan + scheme journal for History topic blocks, parsed locally from the text layer (no agents).

    python3 pipeline/rebuild/hist_scan_journal.py <out.jsonl>

History Later Modern papers are regular: every topic block (q2-q13) is either a Higher block of
four 100-mark essays ("1."-"4."), or an Ordinary block of A (5 short questions on a stimulus,
6 marks each), B (one short paragraph from four headings, 30) and C (one longer paragraph from
four questions, 40). The scheme gives no content points for essays or B/C: only the CM/OE rule
and, for some questions, a "TWO elements" note. Ordinary A answers are listed per topic.
The DBQ (q1) is left to the Haiku DBQ workflow. Anything off-pattern is printed as PROBLEM.
"""
import json
import re
import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'pipeline/_data/rebuild/history'
TOPIC = re.compile(r'^(?:Later Modern\s+)?(Ireland|Europe and the wider world)\s*:?\s*Topic\s*(\d)\s*$', re.I)
SKIP = re.compile(r'^(Answer one of the following( questions)?:?|Recommended maximum time.*|'
                  r'Write a short paragraph on one of the following:?|Refer to the instructions.*|'
                  r'Answer the questions below if you are following the Alternative.*|front cover of this examination paper\.?|'
                  r'SECTION \d.*|Page \d+ of \d+)$', re.I)
ITEM = re.compile(r'^(\d)\.\s*(.*)$')
BARE = re.compile(r'^(\d)$')          # "2" printed without its full stop (2016 OL, 2022 OL)
PART = re.compile(r'^([ABC])?\s*\(\s*(\d+)\s*marks?\s*\)\s*$', re.I)   # 2013 OL q3 loses its "C"
# scheme headers may carry the title on the same line ("Ireland: Topic 1 Ireland and the Union...")
SCHEME_TOPIC = re.compile(r'^(?:Later Modern\s+)?(Ireland|Europe and the wider world)\s*:?\s*Topic\s*(\d)\b', re.I)
# 2023-26 OL: answers to the alternative-instructions Part A come last, under this line
SCHEME_EXTRA = re.compile(r'^Extra (Part|Section) A questions', re.I)
MARK = re.compile(r'\s*\((\d+)\)\s*$')

ESSAY_POINTS = [
    'Cumulative Mark (CM), max 60: each paragraph (or paragraph equivalent) is marked 0-12; '
    'excellent (11-12) = outstanding analysis, clearly expressed, accurate and substantial information. '
    'Full CM needs about 5-6 such paragraphs.',
    'Overall Evaluation (OE), max 40: excellent (34-40) = excellent treatment of the set question, '
    'showing detailed learning, analysis and extensive coverage; answers the question as set, no irrelevant material.',
]
ESSAY_RULE = 'CM 60 + OE 40 = 100'
CORE = ('A Core Statement is a significant relevant factual statement, a valid relevant explanation/opinion/comment, '
        'or a significant relevant introductory or concluding statement; each completed Core Statement = 5 marks.')


def clean(lines):
    out = []
    for raw in lines:
        t = re.sub(r'\s+', ' ', raw).strip()
        if t:
            out.append(t)
    return out


def items(lines, expect):
    """Numbered items 1..expect in order; text runs on until the next number."""
    found, cur = [], None
    for t in lines:
        m = ITEM.match(t) or BARE.match(t)
        if m and int(m.group(1)) == len(found) + 1 and len(found) < expect:
            cur = [m.group(2)] if m.lastindex > 1 and m.group(2) else []
            found.append(cur)
        elif cur is not None:
            cur.append(t)
    res = []
    for words in found:
        text = ' '.join(words)
        mk = MARK.search(text)
        res.append((MARK.sub('', text).strip(), int(mk.group(1)) if mk else None))
    return res


def scheme_blocks(year, level):
    """{(sec, topic): [lines]} from the Later Modern scheme; the last header of a topic wins."""
    text = (DATA / 'scheme' / f'{year}-{level}' / 'scheme.txt').read_text()
    lines = clean(l for l in text.splitlines() if not l.startswith('===== PAGE'))
    heads = [(i, m) for i, l in enumerate(lines) if (m := SCHEME_TOPIC.match(l) or SCHEME_EXTRA.match(l))]
    blocks = {}
    for n, (i, m) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        body = lines[i + 1:end]
        cut = next((k for k, l in enumerate(body) if re.match(r'^(SECTION \d|Section \d)', l)), len(body))
        if SCHEME_EXTRA.match(m.group(0)):
            blocks[('ALT', 0)] = body[:cut]
            continue
        # the Extra A block ends the topic above it
        extra = next((k for k, l in enumerate(body) if SCHEME_EXTRA.match(l)), len(body))
        blocks[('EUR' if m.group(1)[0] in 'Ee' else 'IRL', int(m.group(2)))] = body[:min(cut, extra)]
    return blocks


def essay_notes(body):
    """{n: note} — "NOTE: TWO elements (...) If only ONE, Max. CM = 50" per essay number."""
    notes, cur = {}, None
    for l in body:
        m = re.match(r'^(\d)\.$', l)
        if m:
            cur = int(m.group(1))
            continue
        if cur and (l.startswith('NOTE') or (notes.get(cur) and not l.startswith('Max'))):
            if l.startswith('Max') or l.startswith('='):
                continue
            notes[cur] = (notes.get(cur, '') + ' ' + l).strip()
    # a page number printed after the last note on a page ("... Max. CM = 50 17")
    return {k: re.sub(r'(= \d0|OE\.?)\s+\d{1,2}$', r'\1', v) for k, v in notes.items()}


def ol_answers(body):
    """{'A1': (answer, marks)} from an Ordinary topic's scheme notes."""
    out, cur = {}, None
    for l in body:
        m = re.match(r'^A(\d)\.\s*(.*)$', l)
        if m:
            cur = f'A{m.group(1)}'
            out[cur] = [m.group(2)] if m.group(2) else []
            continue
        if re.match(r'^[BC]\s*-', l):
            cur = None
        if cur:
            out[cur].append(l)
    res = {}
    for k, words in out.items():
        text = ' '.join(words)
        # marks are single-digit "(6)", sometimes split "(3) ... (6)" for two elements (2006 OL)
        # Usually the last "(6)" is the total and earlier "(3)"s are its elements; 2006 OL instead
        # splits one answer as "(3) ... (6)" = 9. Callers pick whichever makes Part A total 30.
        found = [int(x) for x in re.findall(r'\((\d)\)', text)]
        answer = re.sub(r';\s*\d{1,2}$', '', re.sub(r'\s*\(\d\)', ';', text)).strip(' ;`')   # page number after "(6)"
        res[k] = (answer, found[-1] if found else 6, sum(found) or 6)
    return res


def has_picture(crop):
    for seg in crop['segments']:
        if 'box' not in seg:
            continue
        page = fitz.open(ROOT / f"pipeline/_data/raw/history/{seg['paper']}-EV-papers.pdf")[seg['page'] - 1]
        box = fitz.Rect(seg['box'])
        if any(fitz.Rect(i['bbox']).intersects(box) and fitz.Rect(i['bbox']).height > 40
               for i in page.get_image_info()):
            return True
    return False


def main(out_path):
    crops = json.loads((DATA / 'crops.json').read_text())
    lines_out, problems, n = [], [], 0
    schemes = {}
    for key, c in sorted(crops.items()):
        if c['section'] == 'DBQ':
            continue
        year, level, sec = c['year'], c['level'], c['section']
        topic = c['number'] - (7 if sec == 'EUR' else 1)
        chapter = f"hist-{'eur' if sec == 'EUR' else 'ire'}{topic}"
        blocks = schemes.setdefault((year, level), scheme_blocks(year, level))
        sblock = blocks.get(('ALT', 0) if c.get('alternative') else (sec, topic), [])
        if not sblock:
            problems.append(f'{key}: no scheme block for {sec} topic {topic}')
        text = clean((DATA / 'text' / f'{key}.txt').read_text().splitlines())
        # drop the topic header and its title line
        if text and TOPIC.match(text[0]):
            text = text[2:]
        body = [t for t in text if not SKIP.match(t)]
        parts, context = [], ''
        if level == 'higher':
            got = items(body, 4)
            notes = essay_notes(sblock)
            if len(got) != 4:
                problems.append(f'{key}: {len(got)} essays')
            for i, (q, mk) in enumerate(got, 1):
                if mk not in (100, None):
                    problems.append(f'{key}: essay {i} marked ({mk})')
                pts = ESSAY_POINTS + ([f'Scheme note: {notes[i]}'] if notes.get(i) else [])
                parts.append({'label': str(i), 'text': q, 'type': ['long-answer'], 'diagramRelation': 'none',
                              'marks': 100, 'schemePoints': pts, 'fullMarksRule': ESSAY_RULE})
            attempt = 'Answer ONE of the four questions on this topic (one essay, 100 marks).'
            qmarks = 100
        else:
            sections, cur = {}, None
            for t in body:
                m = PART.match(t)
                if m:
                    cur = (m.group(1) or {'30': 'B' if 'A' in sections else 'A', '40': 'C'}.get(m.group(2), '?')).upper()
                    sections[cur] = []
                elif cur:
                    sections[cur].append(t)
            answers = ol_answers(sblock)
            if sum(v[1] for v in answers.values()) != 30 and sum(v[2] for v in answers.values()) == 30:
                answers = {k: (a, total) for k, (a, _, total) in answers.items()}
            else:
                answers = {k: (a, last) for k, (a, last, _) in answers.items()}
            n_a = len(answers) if 4 <= len(answers) <= 5 else 5     # 2006-10 sometimes set four
            want = {'A': n_a} if c.get('alternative') else {'A': n_a, 'B': 4, 'C': 4}
            if sum(mk for _, mk in answers.values()) != 30:
                problems.append(f'{key}: Part A scheme marks total {sum(mk for _, mk in answers.values())} '
                                f'{[(k, v[1]) for k, v in answers.items()]}')
            picture = has_picture(c)
            for part, expect in want.items():
                lines = sections.get(part, [])
                got = items(lines, expect)
                if len(got) != expect:
                    problems.append(f'{key}: part {part} has {len(got)} items (want {expect})')
                if part == 'A':
                    first = next((k for k, t in enumerate(lines) if ITEM.match(t)), len(lines))
                    context = ' '.join(lines[:first])
                for i, (q, _) in enumerate(got, 1):
                    label = f'{part}{i}'
                    if part == 'A':
                        ans, mk = answers.get(label, ('', 6))
                        if not ans:
                            problems.append(f'{key}: no scheme answer for {label}')
                        parts.append({'label': label, 'text': q, 'type': ['short-answer'],
                                      'diagramRelation': 'refers-to-figure' if picture else 'none',
                                      'marks': mk, 'schemePoints': [f'Scheme answer: {ans}'] if ans else [],
                                      'fullMarksRule': f'{mk} marks: the answer as given in the scheme'})
                    else:
                        cm = 20 if part == 'B' else 30
                        parts.append({'label': label, 'text': q, 'type': ['long-answer'], 'diagramRelation': 'none',
                                      'marks': cm + 10,
                                      'schemePoints': [f'Cumulative Mark (CM), max {cm}: {cm // 5} completed Core Statements. {CORE}',
                                                       'Overall Evaluation (OE), max 10: how well the answer responds to the heading or set question (excellent 9-10).'],
                                      'fullMarksRule': f'CM {cm} ({cm // 5} Core Statements x 5) + OE 10 = {cm + 10}'})
            attempt = ('Alternative instructions only: answer all five questions on the extract (30 marks).'
                       if c.get('alternative') else
                       'Answer A (all five questions), ONE heading in B and ONE question in C (100 marks).')
            qmarks = 30 if c.get('alternative') else 100
        scan = {'attemptRule': attempt, 'context': context, 'cropIssues': '',
                'parts': [{'label': p['label'], 'text': p['text'], 'type': p['type'],
                           'diagramRelation': p['diagramRelation'], 'resource': 'none', 'chapterId': chapter,
                           'loIds': [], 'offSpec': False, 'offSpecReason': ''} for p in parts]}
        scheme = {'questionMarks': qmarks,
                  'note': 'Marked by CM + OE (no content points in the scheme).' if level == 'higher' else
                          'A: 6 marks per answer as listed. B and C: Core Statements (5 marks each) + OE.',
                  'parts': [{k: p[k] for k in ('label', 'marks', 'schemePoints', 'fullMarksRule')} for p in parts]}
        for stage, res in (('scan', scan), ('scheme', scheme)):
            lines_out.append({'type': 'started', 'key': f'{stage}:{key}', 'label': f'{stage}:{key}'})
            lines_out.append({'type': 'result', 'key': f'{stage}:{key}', 'result': res})
        n += 1
    Path(out_path).write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in lines_out) + '\n')
    print(f'{n} topic blocks -> {out_path}')
    for p in problems:
        print('PROBLEM', p)


if __name__ == '__main__':
    main(sys.argv[1])
