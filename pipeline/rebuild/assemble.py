"""Turn a rebuild workflow's journal into the internal question store and the app's bank.

    python3 pipeline/rebuild/assemble.py biology <journal.jsonl> [<journal.jsonl> ...]

Reads the scan / scheme / write / check results each agent returned and writes:
  <DATA>/<subject>/questions/<key>.json   everything, including transcribed text and scheme
                                          points (internal: never shipped)
  <subject>-exam-questions.js             the app bank: question crops, marks, tags and answers
                                          that passed the checker. No question text.
  pipeline/_data/rebuild-review/<subject>.md   parts left for the user: checker disputes and
                                               gaps in the notes (gitignored)
Later journals override earlier ones, so re-runs of single questions can be layered on top.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = Path.home() / 'barebones/pipeline/_data/rebuild'
LEVEL_NAME = {'higher': 'Higher', 'ordinary': 'Ordinary'}
# Per-subject paper layout. Biology: Sections A+B answerbook and a separate Section C paper.
# Chemistry (1999 syllabus papers): one paper, Section A experiments (Q1-3) and Section B, 50 marks a question.
SUBJECTS = {
    'biology': {'prefix': 'bio', 'default_marks': {'A': 20, 'B': 30, 'C': 60},
                'paper': lambda section: 'A+B' if section in ('A', 'B') else 'C'},
    'chemistry': {'prefix': 'chem', 'default_marks': {'A': 50, 'B': 50},
                  'paper': lambda section: ''},
    # PE (2018 specification): one answerbook; Section A short questions (8 marks), Section B the
    # case study (Q13, 50 marks), Section C long questions (40 marks each).
    'pe': {'prefix': 'pe', 'default_marks': {'A': 8, 'B': 50, 'C': 40},
           'paper': lambda section: ''},
    # Geography (2003 syllabus): Part One short questions (HL 8, OL 10 marks), Part Two keyed q101+
    # (core 1-6, electives 7-12, HL options 13-24), 80 marks a question at HL.
    'geography': {'prefix': 'geo', 'default_marks': {'P1': 8, 'core': 80, 'elective': 80, 'option': 80},
                  'paper': lambda section: 'Part One' if section == 'P1' else 'Part Two'},
    # History (2003 syllabus, Later Modern paper only): q1 the documents-based question, q2-7
    # Ireland topics 1-6, q8-13 Europe topics 1-6; 100 marks each.
    'history': {'prefix': 'hist', 'default_marks': {'DBQ': 100, 'IRL': 100, 'EUR': 100},
                'paper': lambda section: {'DBQ': 'Section 1', 'IRL': 'Section 2', 'EUR': 'Section 3'}[section]},
}


def read_journal(path):
    """{key: {'scan':…, 'scheme':…, 'write': {round: …}, 'check': {round: …}}} from one journal."""
    labels, out = {}, {}
    for line in Path(path).read_text().splitlines():
        entry = json.loads(line)
        if entry['type'] == 'started':
            labels[entry['key']] = entry['label']
        elif entry['type'] == 'result' and entry.get('result'):
            stage, _, rest = labels[entry['key']].partition(':')
            key, _, rnd = rest.partition('#')
            slot = out.setdefault(key, {'write': {}, 'check': {}})
            if stage in ('write', 'check'):
                slot[stage][int(rnd)] = entry['result']
            else:
                slot[stage] = entry['result']
    return out


def resolve(q):
    """Final answer per part label (latest rewrite wins) and its last checker verdict."""
    answers, verdicts, history = {}, {}, []
    for rnd in sorted(q['write']):
        for a in q['write'][rnd]['parts']:
            answers[a['label']] = a
    for rnd in sorted(q['check']):
        for v in q['check'][rnd]['parts']:
            verdicts[v['label']] = v
            history.append({'round': rnd, **v})
    return answers, verdicts, history


def main(subject, journals):
    merged = {}
    for path in journals:
        for key, q in read_journal(path).items():
            slot = merged.setdefault(key, {'write': {}, 'check': {}})
            if 'scan' in q:                  # a fresh scan restarts the question
                slot.clear()
                slot.update({'write': {}, 'check': {}})
            slot.update({k: v for k, v in q.items() if k not in ('write', 'check')})
            slot['write'].update(q['write'])
            slot['check'].update(q['check'])

    for key, slot in merged.items():          # state.py's cleaned scans win over raw journal scans
        scan_file = DATA / subject / 'state' / f'{key}.scan.json'
        if scan_file.exists():
            slot['scan'] = json.loads(scan_file.read_text())

    crops = json.loads((DATA / subject / 'crops.json').read_text())
    store = DATA / subject / 'questions'
    store.mkdir(parents=True, exist_ok=True)
    bank, review = [], []

    for key in sorted(merged, key=lambda k: (crops[k]['year'], crops[k]['level'], crops[k]['number'])):
        q, crop = merged[key], crops[key]
        if 'scan' not in q or 'scheme' not in q or not q['write']:
            review.append((key, None, 'incomplete', 'pipeline did not finish this question', ''))
            continue
        answers, verdicts, history = resolve(q)
        scheme = {p['label']: p for p in q['scheme']['parts']}
        state_file = DATA / subject / 'state' / f'{key}.json'
        if state_file.exists():               # state.py fills marks the scheme left blank
            for p in json.loads(state_file.read_text())['parts']:
                scheme[p['label']] = {**scheme.get(p['label'], {}), 'marks': p['marks']}
        parts = []
        for p in q['scan']['parts']:
            a = answers.get(p['label'], {})
            v = verdicts.get(p['label'], {})
            s = scheme.get(p['label'], {})
            status = a.get('status', 'missing')
            passed = v.get('verdict') == 'pass'
            if status == 'off-spec' and passed:
                final = 'off-spec'
            elif status == 'answered' and passed:
                final = 'kept' if a.get('reusedOld') else 'written'
            elif status == 'notes-gap' and passed:
                final = 'notes-gap'
            else:
                final = 'flagged'
            part = {**p, 'offSpec': final == 'off-spec', 'scanOffSpec': p['offSpec'], 'marks': s.get('marks', 0), 'schemePoints': s.get('schemePoints', []),
                          'fullMarksRule': s.get('fullMarksRule', ''), 'answer': a.get('answer', ''),
                          'notesRefs': a.get('notesRefs', []), 'gap': a.get('gap', ''),
                          'answerStatus': final, 'checker': v}
            parts.append(part)
            if final in ('flagged', 'notes-gap'):
                review.append((key, part, final, v.get('problems', ''), a.get('gap', '')))

        record = {'key': key, **crop, 'attemptRule': q['scan']['attemptRule'],
                  'cropOk': q['scan']['cropOk'], 'cropIssues': q['scan']['cropIssues'],
                  'questionMarks': q['scheme']['questionMarks'], 'schemeNote': q['scheme']['note'],
                  'parts': parts, 'checkHistory': history}
        (store / f'{key}.json').write_text(json.dumps(record, indent=1, ensure_ascii=False))
        resolved_file = DATA / subject / 'crop-resolved.json'
        resolved = json.loads(resolved_file.read_text()) if resolved_file.exists() else {}
        if not q['scan']['cropOk'] and key not in resolved:
            review.append((key, None, 'crop', q['scan']['cropIssues'], ''))

        on_spec = [p['chapterId'] for p in parts if not p['offSpec']] or [p['chapterId'] for p in parts]
        cfg = SUBJECTS[subject]
        paper = cfg['paper'](crop['section'])
        bank.append({
            'id': f'{subject}-pp-{key}',
            'subject': subject,
            'chapterId': Counter(on_spec).most_common(1)[0][0],
            'sectionId': f'{cfg["prefix"]}-section{crop["section"]}',
            'source': f'LC {subject.title()} {LEVEL_NAME[crop["level"]]} {crop["year"]} — '
                      f'Section {crop["section"]} — Q{crop["number"]}',
            'year': crop['year'],
            'level': crop['level'],
            'paper': paper,
            'questionNumber': crop['number'],
            'legacy': True,
            'totalMarks': q['scheme']['questionMarks'] or cfg['default_marks'][crop['section']],
            'images': crop['images'],
            'parts': [{
                'label': p['label'],
                'marks': p['marks'],
                'model': p['answer'] if p['answerStatus'] in ('written', 'kept') else '',
                'model_source': {'written': 'notes', 'kept': 'kept'}.get(p['answerStatus'], ''),
                'answerStatus': p['answerStatus'],
                'type': p['type'],
                'diagramRelation': p['diagramRelation'],
                'offSpec': p['offSpec'],
                'notesRefs': p['notesRefs'] if p['answerStatus'] in ('written', 'kept') else [],
            } for p in parts],
        })

    header = (f'// {subject.title()} exam bank, rebuilt from the papers (pipeline/EXAM_BANK_REBUILD.md).\n'
              '// Each question is shown as crops of the original paper (images[]), never as\n'
              '// transcribed text. Model answers come only from the app notes and the spec, each\n'
              '// checked against the marking scheme by a second agent. Generated by\n'
              '// pipeline/rebuild/assemble.py; do not edit by hand.\n')
    body = json.dumps(bank, indent=1, ensure_ascii=False)
    assert not re.search(r'"(question|text)":', body), 'question text must never ship'
    (ROOT / f'{subject}-exam-questions.js').write_text(
        header + 'window.EXAM_QUESTIONS_DB = (window.EXAM_QUESTIONS_DB || []).concat(\n' + body + '\n);\n')

    out = ROOT / 'pipeline/_data/rebuild-review'
    out.mkdir(parents=True, exist_ok=True)
    lines = [f'# {subject.title()} rebuild: parts needing a decision', '']
    for key, p, kind, problems, gap in review:
        lines.append(f'## {key} {p["label"] if p else ""} [{kind}]')
        if p:
            lines += ['', f'**Question (internal transcription):** {p["text"]}', '',
                      f'**Scheme:** {"; ".join(p.get("schemePoints", []))} ({p.get("fullMarksRule", "")})', '',
                      f'**Last answer:** {p.get("answer", "")}', '']
        if gap:
            lines += [f'**Missing from the notes:** {gap}', '']
        if problems:
            lines += [f'**Checker:** {problems}', '']
    (out / f'{subject}.md').write_text('\n'.join(lines))

    statuses = Counter(p['answerStatus'] for q in bank for p in q['parts'])
    print(f'{len(bank)} questions, {sum(statuses.values())} parts: {dict(statuses)}; '
          f'{len(review)} review items -> {out / (subject + ".md")}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
