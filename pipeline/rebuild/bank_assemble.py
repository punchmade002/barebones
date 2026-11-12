"""Build <subject>-exam-questions.js from the rebuilt state and the fill runs (chem_assemble.py, any subject).

    python3 pipeline/rebuild/bank_assemble.py <subject>

Layers, applied in order by part id "<key>|<label>":
  1. audited old answers (old-answers/<key>.txt, exact label, on-spec parts)        model_source audited
  2. <DATA>/<subject>/fill/short.json   Haiku fill run: {id: {model, by}}           haiku / sonnet-figure / sonnet-fix
  3. <DATA>/<subject>/fill/long.json    Sonnet long-answer run: {id: {model, by}}   sonnet-long / sonnet-long-fix
  4. <DATA>/<subject>/fill/figcheck-fixes.json, then tidy.json and manual.json: {id: model}
     (source unchanged, except figcheck sets sonnet-fix; manual.json holds edits from the final read)
Parts with no answer (long answers still failing after one fix round included) ship as flagged
with no model and are listed in pipeline/_data/rebuild-review/<subject>.md.
notesRefs are the scan's loIds, else the question's chapter.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE, lab, old_answers, order  # noqa: E402
from assemble import LEVEL_NAME, SUBJECTS  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
NAMES = {'pe': 'Physical Education', 'chemistry': 'Chemistry', 'biology': 'Biology', 'geography': 'Geography', 'history': 'History'}
# Papers set on the specification students sit now; everything else is legacy.
CURRENT_SPEC = {'pe': lambda year: True,
                # Geography: the 2003 syllabus is examined to June 2027; its replacement starts in 2028.
                'geography': lambda year: True,
                # History: the 2003 Later Modern syllabus is still examined.
                'history': lambda year: True}
# History scans name sections DBQ/IRL/EUR; the app's sections (exam-breakdown.js) are 1/2/3.
SECTION_NO = {'history': {'DBQ': 1, 'IRL': 2, 'EUR': 3}}


def load(path):
    return json.loads(path.read_text()) if path.exists() else {}


def main(subject):
    data = BASE / subject
    fill = {}
    for name in ('short.json', 'long.json', 'thirty.json'):   # thirty: Geography 30-mark essays
        fill.update(load(data / 'fill' / name))
    figfix = load(data / 'fill' / 'figcheck-fixes.json')
    tidy = load(data / 'fill' / 'tidy.json')
    tidy.update(load(data / 'fill' / 'manual.json'))   # reviewer edits found on the final read, {id: model}
    flagged_long = {f['id']: f.get('issue', '') for name in ('long-flagged.json', 'thirty-flagged.json')
                    for f in load(data / 'fill' / name).get('flagged', [])}
    crops = json.loads((data / 'crops.json').read_text())
    cfg = SUBJECTS[subject]
    current = CURRENT_SPEC.get(subject, lambda year: False)
    valid = {re.sub(r'-s\d+$', '', f.stem) for f in (data / 'notes').glob('*-s*.md')}
    fallback = sorted(valid)[0] if valid else ''
    bank, review, sources = [], [], Counter()
    for f in sorted((data / 'state').glob('*.json'), key=lambda p: order(p.name.split('.')[0])):
        if f.name.endswith('.scan.json'):
            continue
        st = json.loads(f.read_text())
        key = st['key']
        scan = {p['label']: p for p in json.loads((data / 'state' / f'{key}.scan.json').read_text())['parts']}
        crop = crops[key]
        old = old_answers(subject, key)
        old_text = (data / 'old-answers' / f'{key}.txt').read_text() if old else ''
        parts = []
        for p in st['parts']:
            sp = scan.get(p['label'], {})
            L = lab(p['label'])
            pid = f'{key}|{p["label"]}'
            model, status, source = '', 'flagged', ''
            if not p.get('offSpec') and L in old:
                model, source = old[L], 'audited'
                status = 'kept' if re.search(rf'^{re.escape(L)} ?\[kept\]', old_text, re.M) else 'written'
            elif pid in fill:
                model, status, source = fill[pid]['model'], 'written', fill[pid]['by']
            if model and pid in figfix and figfix[pid].strip():
                model, source = figfix[pid], 'sonnet-fix'
            if model and pid in tidy and tidy[pid].strip():
                model = tidy[pid]
            if not model:
                why = flagged_long.get(pid, 'no answer')
                review.append(f'- {key} {p["label"] or "(whole question)"}: {why}\n  {p["text"][:300]}')
            sources[source or 'none'] += 1
            refs = p.get('loIds') or ([sp['chapterId']] if sp.get('chapterId') else [])
            parts.append({
                'label': p['label'],
                'marks': p['marks'],
                'model': model.strip(),
                'model_source': source,
                'answerStatus': status,
                'type': p['type'],
                'diagramRelation': p['diagramRelation'],
                'offSpec': bool(p.get('offSpec')),
                'notesRefs': refs if model else [],
                '_chapter': sp.get('chapterId', ''),
            })
        # A chapter must be one the notes have (off-spec Topic 7/8 parts can name a removed one);
        # a part's loIds are the surest sign of its chapter, its scanned chapterId the next.
        def chapters_of(p):
            from_refs = [re.sub(r'-s\d+$', '', r) for r in p['notesRefs'] if re.sub(r'-s\d+$', '', r) in valid]
            return from_refs or ([p['_chapter']] if p['_chapter'] in valid else [])
        on_spec = [c for p in parts if not p['offSpec'] for c in chapters_of(p)] or [c for p in parts for c in chapters_of(p)]
        chapter = Counter(on_spec).most_common(1)[0][0] if on_spec else fallback
        for p in parts:
            del p['_chapter']
            if p['model'] and not p['notesRefs']:
                p['notesRefs'] = [chapter]
        # Geography keys Part Two as q101+; students see the number printed on the paper.
        printed = crop['number'] % 100 if subject == 'geography' else crop['number']
        section = SECTION_NO.get(subject, {}).get(crop['section'], crop['section'])
        bank.append({
            'id': f'{subject}-pp-{key}',
            'subject': subject,
            'chapterId': chapter,
            'sectionId': f'{cfg["prefix"]}-section{section}',
            'source': f'LC {NAMES.get(subject, subject.title())} {LEVEL_NAME[crop["level"]]} {crop["year"]} — '
                      + (f'{cfg["paper"](crop["section"])} — Q{printed}' if subject == 'geography'
                         else f'Section {section} — Q{crop["number"]}'),
            'year': crop['year'],
            'level': crop['level'],
            'paper': cfg['paper'](crop['section']),
            'questionNumber': printed,
            'legacy': not current(crop['year']),
            'totalMarks': st.get('questionMarks') or cfg['default_marks'][crop['section']],
            'attemptRule': st.get('attemptRule', ''),
            'images': crop['images'],
            'parts': parts,
        })

    name = NAMES.get(subject, subject.title())
    header = (f'// {name} exam bank, rebuilt from the papers (pipeline/EXAM_BANK_REBUILD.md).\n'
              '// Each question is shown as crops of the original paper (images[]), never as\n'
              '// transcribed text. Every model answer was written against the official marking\n'
              '// scheme: short answers by Haiku with a Sonnet sample check, long answers by Sonnet\n'
              '// with every one checked by a second Sonnet. Generated by pipeline/rebuild/bank_assemble.py;\n'
              '// do not edit by hand.\n')
    body = json.dumps(bank, indent=1, ensure_ascii=False)
    assert not re.search(r'"(question|text|context)":', body), 'question text must never ship'
    (ROOT / f'{subject}-exam-questions.js').write_text(
        header + 'window.EXAM_QUESTIONS_DB = (window.EXAM_QUESTIONS_DB || []).concat(\n' + body + '\n);\n')
    out = ROOT / 'pipeline/_data/rebuild-review'
    out.mkdir(parents=True, exist_ok=True)
    (out / f'{subject}.md').write_text(f'# {name} rebuild: parts with no answer\n\n' + '\n'.join(review) + '\n')
    statuses = Counter(p['answerStatus'] for q in bank for p in q['parts'])
    print(f'{len(bank)} questions, {sum(statuses.values())} parts: {dict(statuses)}; sources {dict(sources)}; '
          f'{len(review)} unanswered -> {out / f"{subject}.md"}')


if __name__ == '__main__':
    main(sys.argv[1])
