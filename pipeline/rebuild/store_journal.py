"""Rebuild a journal from the question store, so assemble.py can re-run after the original
workflow journals are gone.

    python3 pipeline/rebuild/store_journal.py biology > base.jsonl
    python3 pipeline/rebuild/assemble.py biology base.jsonl <new journals...>

Each <DATA>/<subject>/questions/<key>.json becomes one scan, scheme, write and check entry set.
Re-running assemble.py on the base journal alone gives back the same bank.
Agent results for new or re-done questions can also be given as JSON files:
    python3 pipeline/rebuild/store_journal.py --results <file.json> ...
where each file is {"<stage>:<key>[#<round>]": <result>, ...}.
"""
import json
import sys
from collections import defaultdict

from assemble import DATA

WRITE_STATUS = {'written': 'answered', 'kept': 'answered', 'off-spec': 'off-spec', 'notes-gap': 'notes-gap'}
SCAN_KEYS = ('label', 'text', 'type', 'diagramRelation', 'chapterId', 'loIds', 'offSpecReason')


def lines(label, result):
    return [json.dumps({'type': 'started', 'key': label, 'label': label}, ensure_ascii=False),
            json.dumps({'type': 'result', 'key': label, 'result': result}, ensure_ascii=False)]


def store_lines(subject):
    out = []
    for f in sorted((DATA / subject / 'questions').glob('*.json')):
        q = json.loads(f.read_text())
        key, parts = q['key'], q['parts']
        out += lines(f'scan:{key}', {
            'cropOk': q['cropOk'], 'cropIssues': q['cropIssues'], 'attemptRule': q['attemptRule'],
            'parts': [{**{k: p[k] for k in SCAN_KEYS}, 'offSpec': p['scanOffSpec'],
                       **({'resource': p['resource']} if 'resource' in p else {})} for p in parts]})
        out += lines(f'scheme:{key}', {
            'questionMarks': q['questionMarks'], 'note': q['schemeNote'],
            'parts': [{k: p[k] for k in ('label', 'marks', 'schemePoints', 'fullMarksRule')} for p in parts]})
        out += lines(f'write:{key}#1', {'parts': [{
            'label': p['label'], 'status': WRITE_STATUS.get(p['answerStatus'], 'answered'),
            'answer': p['answer'], 'notesRefs': p['notesRefs'], 'gap': p['gap'],
            'reusedOld': p['answerStatus'] == 'kept'} for p in parts]})
        rounds = defaultdict(list)
        for h in q['checkHistory']:
            rounds[h['round']].append({k: v for k, v in h.items() if k != 'round'})
        # parts never checked still need their final verdict
        seen = {h['label'] for h in q['checkHistory']}
        last = max(rounds, default=1)
        rounds[last] += [p['checker'] for p in parts if p['label'] not in seen and p['checker']]
        for rnd, verdicts in sorted(rounds.items()):
            out += lines(f'check:{key}#{rnd}', {'parts': verdicts})
    return out


if __name__ == '__main__':
    if sys.argv[1] == '--results':
        for path in sys.argv[2:]:
            for label, result in json.load(open(path)).items():
                print('\n'.join(lines(label, result)))
    else:
        print('\n'.join(store_lines(sys.argv[1])))
