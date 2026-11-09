"""Turn chem-answer-audit workflow results into per-question old-answer files for the writer.

    python3 pipeline/rebuild/chem_old_answers.py <workflow-output.json> [...]

Each audited part was matched to its exact paper question and part (two Haiku auditors), and
checked against the marking scheme; parts either auditor flagged were rewritten by Sonnet and
re-checked. Only answers that ended the audit at full marks are offered for reuse:
  kept     both auditors (or Sonnet, re-checked) found the stored answer earns full marks
  written  Sonnet's rewrite passed the re-check
Writes <DATA>/chemistry/old-answers/<year>-<level>-q<N>.txt, one line per part:
  (b)(ii) [kept]: <answer>
The writer may reuse a line only if it answers that exact scanned part and meets every scheme
point (EXAM_BANK_REBUILD.md, "Old answers").
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'pipeline/_data/rebuild/chemistry'


def label(raw):
    raw = re.sub(r'\s+', '', raw or '')
    return raw if raw.startswith('(') or not raw else f'({raw.strip("()")})'


def main(files):
    src = (ROOT / 'chemistry-exam-questions.js').read_text()
    body = src[src.index('(window.EXAM_QUESTIONS_DB || []).concat(') + len('(window.EXAM_QUESTIONS_DB || []).concat('):src.rindex(')')]
    db = json.loads(body)
    out = defaultdict(dict)
    counts = defaultdict(int)
    for f in files:
        data = json.loads(Path(f).read_text())
        for r in (data.get('result') or data)['results']:
            A = {(v['qi'], v['pi']): v for v in r['A']}
            B = {(v['qi'], v['pi']): v for v in r['B']}
            flagged = {tuple(map(int, k.split(':'))) for k in r['flagged']}
            final = {}
            for rd in r['rounds']:
                checks = {(c['qi'], c['pi']): c for c in rd['checks']}
                for it in rd['items']:
                    k = (it['qi'], it['pi'])
                    final[k] = (it, checks.get(k))
            for k in set(A) | set(B) | flagged:
                if not (0 <= k[0] < len(db) and 0 <= k[1] < len(db[k[0]]['parts'])):
                    counts['bad index'] += 1          # an auditor returned a qi/pi outside its packet
                    continue
                q = db[k[0]]
                p = q['parts'][k[1]]
                level = 'higher' if 'Higher' in q['source'] else 'ordinary'
                if k not in flagged:
                    v = A.get(k) or B.get(k)
                    status, answer, qn, lab = 'kept', p['model'], v['questionNumber'], v['partLabel']
                else:
                    it, ck = final.get(k, (None, None))
                    if not it or not ck or not ck.get('pass') or it['action'] == 'cannot':
                        counts['dropped'] += 1
                        continue
                    status = 'kept' if it['action'] == 'keep' else 'written'
                    answer = p['model'] if it['action'] == 'keep' else it['model']
                    qn, lab = it['questionNumber'], it['partLabel']
                qn = re.sub(r'\D', '', str(qn))
                if not qn or not answer.strip():
                    counts['untagged'] += 1
                    continue
                key = f'{q["year"]}-{level}-q{int(qn)}'
                out[key][label(lab) + f'#{k[0]}:{k[1]}'] = (label(lab), status, answer.strip())
                counts[status] += 1
    target = DATA / 'old-answers'
    target.mkdir(parents=True, exist_ok=True)
    for key, parts in out.items():
        lines = [f'{lab} [{status}]: {ans}' for lab, status, ans in sorted(parts.values())]
        (target / f'{key}.txt').write_text('\n'.join(lines) + '\n')
    print(f'{len(out)} question files; ' + ', '.join(f'{k} {v}' for k, v in sorted(counts.items())))


if __name__ == '__main__':
    main(sys.argv[1:])
