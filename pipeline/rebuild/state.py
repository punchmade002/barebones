"""Pack each question's scan + marking-scheme results into one small file for the writer/checker.

    python3 pipeline/rebuild/state.py biology <journal.jsonl> [...]

Writer and checker agents read only <DATA>/<subject>/state/<key>.json, so their context stays
small: no repo exploration, no re-reading the scheme. Scans saved earlier as
state/<key>.scan.json are used when a journal has none.
"""
import json
import sys
from pathlib import Path

from assemble import DATA, SUBJECTS, read_journal


def main(subject, journals):
    base = DATA / subject
    found = {}
    for path in journals:
        for key, q in read_journal(path).items():
            found.setdefault(key, {}).update({k: v for k, v in q.items() if k in ('scan', 'scheme')})
    crops = json.loads((base / 'crops.json').read_text())
    written = 0
    for key, q in found.items():
        scan_file = base / 'state' / f'{key}.scan.json'
        scan = q.get('scan') or (json.loads(scan_file.read_text()) if scan_file.exists() else None)
        scheme = q.get('scheme')
        if not scan or not scheme:
            continue
        # loIds must name a notes file; a scan that gave a syllabus code ("3.2.1") instead
        # falls back to every notes file of that part's chapter.
        notes_dir = base / 'notes'
        for p in scan['parts']:
            chapter = p.get('chapterId') or ''
            good = [lo for lo in p.get('loIds', []) if (notes_dir / f'{lo}.md').exists()]
            if '-s' in chapter:                # a notes id given as the chapter ("chem23-s1")
                if (notes_dir / f'{chapter}.md').exists() and chapter not in good:
                    good.append(chapter)
                chapter = chapter.split('-s')[0]
                p['chapterId'] = chapter
            if not good and chapter:
                good = sorted(f.stem for f in notes_dir.glob(f'{chapter}-s*.md'))
            p['loIds'] = good
        marks = {p['label']: p for p in scheme['parts']}
        labels = [p['label'] for p in scan['parts']]
        # A bare lead-in such as "(b)" ahead of "(b)(i)" carries no task or marks of its own.
        scan['parts'] = [p for p in scan['parts'] if p['label'] in marks
                         or not any(o != p['label'] and o.startswith(p['label']) for o in labels)]
        scan_file.write_text(json.dumps(scan, ensure_ascii=False))
        # Count-based Section A schemes ("6 correct = 20") give no per-part marks; fall back to
        # the section total and an even split so timing and marks still show sensibly.
        total = scheme['questionMarks'] or SUBJECTS[subject]['default_marks'][crops[key]['section']]
        # Parts the scheme left without marks (e.g. "answer A or B" options) share what the
        # question total has not already given out.
        missing = [p for p in scan['parts'] if not marks.get(p['label'], {}).get('marks')]
        given = sum(marks[p['label']]['marks'] for p in scan['parts'] if marks.get(p['label'], {}).get('marks'))
        if missing and len(missing) < len(scan['parts']) and total and total > given:
            share = round((total - given) / len(missing), 1)
            for p in missing:
                marks.setdefault(p['label'], {'schemePoints': [], 'fullMarksRule': ''})['marks'] = share
        if not any(marks.get(p['label'], {}).get('marks') for p in scan['parts']):
            share = round(total / max(len(scan['parts']), 1), 1)
            for p in scan['parts']:
                marks.setdefault(p['label'], {'schemePoints': [], 'fullMarksRule': ''})['marks'] = share
        old = base / 'old-answers' / f'{key}.txt'
        state = {
            'key': key,
            'crops': [str(base / 'crops-png' / f'{key}-{i}.png') for i in range(1, len(crops[key]['images']) + 1)],
            'attemptRule': scan['attemptRule'],
            'context': scan.get('context', ''),     # shared material (case study, table) as text
            'questionMarks': total,
            'schemeNote': scheme['note'],
            'oldAnswer': str(old) if old.exists() else None,
            'parts': [{**{k: p[k] for k in ('label', 'text', 'type', 'diagramRelation', 'loIds', 'offSpec', 'offSpecReason')},
                       **({'resource': p['resource']} if p.get('resource', 'none') != 'none' else {}),
                       **{k: marks.get(p['label'], {}).get(k) for k in ('marks', 'schemePoints', 'fullMarksRule')}}
                      for p in scan['parts']],
        }
        (base / 'state' / f'{key}.json').write_text(json.dumps(state, indent=1, ensure_ascii=False))
        written += 1
    print(f'{written} question states in {base / "state"}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
