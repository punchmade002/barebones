"""Validate saved requirements against the independent PDF extraction ledger.

This checks traceability and omissions, not the substantive correctness of prose.
Run with --self-test to prove deliberate missing-content mutations are rejected.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def normalise(text):
    return ' '.join(text.lower().replace('–', '-').replace('’', "'").split())


def check_bank(bank, source):
    errors = []
    points = bank.get('learningPoints', [])
    point_ids = [p['id'] for p in points]
    point_set = set(point_ids)
    outcomes = bank.get('outcomes', [])
    outcome_ids = [o['id'] for o in outcomes]
    official = {o['id']: o for o in source['officialOutcomes']}
    expected = {f'S{s}.{n:02}' for s, count in [(1, 11), (2, 11), (3, 10)] for n in range(1, count+1)}
    if set(official) != expected or len(source['officialOutcomes']) != 32:
        errors.append('Source extraction does not contain exactly the expected 32 official outcomes.')
    if len(point_ids) != len(point_set):
        errors.append('Duplicate point IDs.')
    if len(outcome_ids) != len(set(outcome_ids)):
        errors.append('Duplicate outcome IDs.')
    if {o['id'] for o in outcomes if o.get('kind') == 'official-learning-outcome'} != expected:
        errors.append('Official outcome inventory has omissions or additions.')
    page_text = {p['pdfPage']: normalise(p['text']) for p in source['pages']}
    for o in outcomes:
        mapped = set(o.get('learningPointIds', []))
        if not mapped or not mapped <= point_set:
            errors.append(f'{o["id"]}: missing or invalid learning-point mapping.')
        actual = {p['id'] for p in points if o['id'] in p.get('outcomeIds', [])}
        if mapped != actual:
            errors.append(f'{o["id"]}: forward/reverse outcome mappings differ.')
        if o['id'] in official:
            if o.get('officialText') != official[o['id']]['text'] or o['pdfPage'] != official[o['id']]['pdfPage']:
                errors.append(f'{o["id"]}: official source text/page differs from extraction.')
    for p in points:
        if not re.fullmatch(r'pe26-[a-z0-9]+(?:-[a-z0-9]+)*', p['id']):
            errors.append(f'Unstable/invalid point ID: {p["id"]}')
        if not p.get('statement') or len(p.get('acceptanceCriteria', [])) < 2 or any(not s.strip() for s in p.get('acceptanceCriteria', [])):
            errors.append(f'{p["id"]}: missing capability or adequate acceptance criteria.')
        if not p.get('outcomeIds') or not set(p['outcomeIds']) <= set(outcome_ids):
            errors.append(f'{p["id"]}: unknown parent outcome.')
        if not p.get('sourceRefs') or any(r.get('pdfPage') not in page_text or r.get('sourceId') != source['sourceId'] for r in p['sourceRefs']):
            errors.append(f'{p["id"]}: invalid source reference.')
        if p.get('requirementStatus') not in {'syllabus-explicit','supported-decomposition'}:
            errors.append(f'{p["id"]}: requirement basis is unspecified.')
        modes = set(p.get('evidenceModes', []))
        if not modes or not modes <= {'recall','reasoning','application','investigation','performance','project'}:
            errors.append(f'{p["id"]}: invalid evidence mode.')
        if modes & {'performance','investigation','project'} and p.get('flashcardAloneCanDemonstrate') is not False:
            errors.append(f'{p["id"]}: practical/inquiry evidence could be mistaken for recall.')
        if p.get('acceptedContentIds') or p.get('contentCoverageStatus') != 'not-assessed':
            errors.append(f'{p["id"]}: this requirements-only baseline must not claim existing content coverage.')
    source_units = {u['id']: u for u in source['contentUnits']}
    reconciled = bank.get('sourceContentReconciliation', [])
    if len(reconciled) != len(source_units) or {u['id'] for u in reconciled} != set(source_units):
        errors.append('Source content-bullet inventory has omissions or duplicates.')
    for u in reconciled:
        if u['id'] not in source_units:
            continue
        original = source_units[u['id']]
        if u['text'] != original['text'] or u['pdfPage'] != original['pdfPage']:
            errors.append(f'{u["id"]}: source bullet text or page changed.')
        mapped = set(u.get('learningPointIds', []))
        if not mapped or not mapped <= point_set:
            errors.append(f'{u["id"]}: missing learning-point coverage.')
        reverse = {p['id'] for p in points if u['id'] in p.get('sourceContentIds', [])}
        if mapped != reverse:
            errors.append(f'{u["id"]}: forward/reverse content mappings differ.')
    for p in points:
        if not set(p.get('sourceContentIds', [])) <= set(source_units):
            errors.append(f'{p["id"]}: unknown source-content reference.')
    for c in bank.get('namedContentChecks', []):
        term = normalise(c['sourceTerm'])
        if term not in page_text.get(c['pdfPage'], ''):
            errors.append(f'Named source term not found on page: {c}')
        if c['learningPointId'] not in point_set:
            errors.append(f'Named source item has no requirement: {c}')
    if len(bank.get('namedContentChecks', [])) < 100:
        errors.append('Named-content audit unexpectedly reduced.')
    accounted = [p['pdfPage'] for p in bank.get('sourcePageAccounting', [])]
    if len(accounted) != len(page_text) or set(accounted) != set(page_text):
        errors.append('Not every source page is accounted for exactly once.')
    if bank.get('coveragePolicy', {}).get('cardCountTargets') is not None:
        errors.append('Fixed card quotas must not determine completeness.')
    if bank.get('profile', {}).get('strandCount') != 3:
        errors.append('Wrong specification profile.')
    if bank.get('profile', {}).get('examYearVerified') or bank.get('profile', {}).get('examYear') is not None:
        errors.append('Unverified exam-year profile activated.')
    pdf = HERE / 'sources/specification-2026.pdf'
    actual_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if source.get('sha256') != actual_hash or bank['sources'][0].get('sha256') != actual_hash:
        errors.append('Source fingerprint changed; reconciliation must be reviewed.')
    return errors


def self_test(bank, source):
    mutations = {
        'missing point': lambda b: b['learningPoints'].pop(),
        'missing official outcome': lambda b: b['outcomes'].pop(0),
        'missing source bullet': lambda b: b['sourceContentReconciliation'].pop(),
        'empty content mapping': lambda b: b['sourceContentReconciliation'][0].update(learningPointIds=[]),
        'duplicate point id': lambda b: b['learningPoints'].append(copy.deepcopy(b['learningPoints'][0])),
        'missing rubric': lambda b: b['learningPoints'][0].update(acceptanceCriteria=[]),
        'false existing coverage': lambda b: b['learningPoints'][0].update(acceptedContentIds=['unverified-card']),
        'invented exam year': lambda b: b['profile'].update(examYear=2027),
        'changed source fingerprint': lambda b: b['sources'][0].update(sha256='wrong'),
    }
    for label, mutate in mutations.items():
        altered = copy.deepcopy(bank)
        mutate(altered)
        assert check_bank(altered, source), f'Mutation was not detected: {label}'
    print(f'PASS: {len(mutations)} deliberately broken banks rejected.')


if __name__ == '__main__':
    bank = json.loads((HERE / 'requirements.json').read_text())
    source = json.loads((HERE / 'sources/specification-pages.json').read_text())
    problems = check_bank(bank, source)
    if problems:
        print('\n'.join(problems))
        raise SystemExit(1)
    print(f'PASS: {len(bank["learningPoints"])} points; 32 official outcomes; {len(source["contentUnits"])} content bullets; source fingerprint verified.')
    if '--self-test' in sys.argv:
        self_test(bank, source)
