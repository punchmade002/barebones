"""Turn the History DBQ Haiku workflow journal into scan/scheme entries for state.py.

    python3 pipeline/rebuild/hist_dbq_journal.py <out.jsonl> <workflow journal.jsonl>

The workflow returned {questions: [{key, caseStudy, documents, parts, issues}]} per group of four
DBQs. Keys Haiku mangled are remapped by year+level; chapterId comes from the DBQ's topic header
on the paper; context is the case study plus the documents as printed (text layer).
"""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / 'pipeline/_data/rebuild/history'
TOPIC = re.compile(r'(Ireland|Europe and the wider world)\s*:\s*Topic\s*(\d)', re.I)
SCAN_KEYS = ('label', 'text', 'type', 'diagramRelation')
SCHEME_KEYS = ('label', 'marks', 'schemePoints', 'fullMarksRule')


def results(path):
    for line in Path(path).read_text().splitlines():
        e = json.loads(line)
        if e.get('type') == 'result' and isinstance(e.get('result'), dict) and 'questions' in e['result']:
            yield from e['result']['questions']


def main(out_path, journal):
    crops = json.loads((DATA / 'crops.json').read_text())
    want = {k for k, c in crops.items() if c['section'] == 'DBQ'}
    got, problems = {}, []
    for q in results(journal):
        key = q['key']
        if key not in want:
            m = re.search(r'(\d{4}).*?(higher|ordinary)', key, re.I)
            cand = f'{m.group(1)}-{m.group(2).lower()}-q1' if m else None
            if cand not in want:
                problems.append(f'unmapped key {key!r}')
                continue
            key = cand
        got[key] = q
    lines = []
    for key in sorted(want):
        q = got.get(key)
        if not q:
            problems.append(f'missing {key}')
            continue
        paper = (DATA / 'scan' / 'dbq' / f'{key}.paper.txt').read_text().replace('\xa0', ' ')
        t = TOPIC.search(paper)
        chapter = f"hist-{'eur' if t.group(1)[0] in 'Ee' else 'ire'}{t.group(2)}"
        docs = re.split(r'\n\s*[–—‐-]\s*Document\s+A\s*[–—‐-]', paper, maxsplit=1)
        if len(docs) == 1:
            docs = re.split(r'\n\s*Document\s+A\b', paper, maxsplit=1)
        doc_text = ('Document A -' + docs[1]).strip() if len(docs) > 1 else ''
        context = f"Case study: {q['caseStudy']}\nDocuments: {q['documents']}\n\n{re.sub(r'[ \t]+', ' ', doc_text)}"
        parts = q['parts']
        labels = [p['label'] for p in parts]
        if len(set(labels)) != len(labels):
            problems.append(f'{key}: duplicate labels {labels}')
        total = sum(p['marks'] for p in parts)
        if abs(total - 100) > 0.5:
            problems.append(f'{key}: marks total {total} {[(p["label"], p["marks"]) for p in parts]}')
        if q.get('issues'):
            problems.append(f'{key}: agent says: {q["issues"]}')
        scan = {'attemptRule': 'Answer all parts of the documents-based question (100 marks).', 'context': context,
                'cropIssues': q.get('issues', ''),
                'parts': [{**{k: p[k] for k in SCAN_KEYS}, 'resource': 'none', 'chapterId': chapter, 'loIds': [],
                           'offSpec': False, 'offSpecReason': ''} for p in parts]}
        scheme = {'questionMarks': 100, 'note': 'Documents-based question: comprehension, comparison, criticism, contextualisation.',
                  'parts': [{k: p[k] for k in SCHEME_KEYS} for p in parts]}
        for stage, res in (('scan', scan), ('scheme', scheme)):
            lines.append({'type': 'started', 'key': f'{stage}:{key}', 'label': f'{stage}:{key}'})
            lines.append({'type': 'result', 'key': f'{stage}:{key}', 'result': res})
    Path(out_path).write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in lines) + '\n')
    print(f'{len(lines) // 4} DBQs -> {out_path}')
    for p in problems:
        print('PROBLEM', p)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
