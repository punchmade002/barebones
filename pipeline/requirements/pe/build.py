"""Build the reviewable PE bank from authored requirements and a source ledger."""
from __future__ import annotations

import copy
import fnmatch
import json
from collections import Counter
from pathlib import Path

from definitions import OUTCOMES, POINTS, ELIGIBLE_ACTIVITIES
from source_map import CONTENT_MAP, NAMED_FAMILIES

HERE = Path(__file__).resolve().parent
SOURCE_ID = 'ncca-pe-three-strand-2026'
SOURCE_URL = 'https://www.curriculumonline.ie/getmedia/e3c33f7c-a88b-4050-bed3-c892ec995ba2/SC-PE-Spec-ENG-INT.pdf'
LANDING_URL = 'https://www.curriculumonline.ie/senior-cycle/senior-cycle-subjects/physical-education-specification/'


def write_json(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def source_ref(page, locator):
    return {'sourceId': SOURCE_ID, 'pdfPage': page, 'printedPage': page - 1, 'locator': locator}


def source_accounting():
    groups = [
        ([1, 2, 30], 'navigation', 'Cover, contents and back cover; no separate learning requirements.'),
        (list(range(3, 11)), 'context', 'Senior-cycle context, rationale, aims, progression and key competencies; apply through outcomes and evidence criteria, not standalone memorisation quotas.'),
        ([11, 12], 'scope-and-depth', 'Three-strand structure and level differentiation recorded in the bank profile.'),
        ([13, 14], 'requirements', 'Practical learning scope and activity areas represented by PRACTICE and activity metadata.'),
        (list(range(15, 21)), 'requirements', 'All numbered outcomes and every left-column content bullet extracted and reconciled individually.'),
        ([21], 'teaching-context', 'Practical, inquiry, reflective and collaborative learning approaches represented through evidence modes and acceptance criteria.'),
        ([22, 23, 24], 'requirements-and-profile', 'Assessment structure and project capabilities captured; annual brief details explicitly unresolved.'),
        ([25], 'assessment-context', 'Written assessment applies the full course learning; accommodations remain official administrative guidance, not invented content exclusions.'),
        ([26], 'administrative-reference', 'Grading information retained in source; not a course knowledge requirement.'),
        ([27, 28], 'rubric-reference', 'Action verbs inform the required depth of acceptance criteria; not a separate set of flashcards.'),
        ([29], 'conditional-requirements', 'Complete activity-eligibility list retained; selection is conditional on the applicable SEC brief.'),
    ]
    return sorted([{'pdfPage': p, 'disposition': d, 'reason': why} for pages, d, why in groups for p in pages], key=lambda x: x['pdfPage'])


def build():
    extracted = json.loads((HERE / 'sources/specification-pages.json').read_text())
    outcomes = copy.deepcopy(OUTCOMES)
    points = copy.deepcopy(POINTS)
    original = {x['id']: x for x in extracted['officialOutcomes']}
    ids = {p['id'] for p in points}
    outcome_by_id = {x['id']: x for x in outcomes}

    for o in outcomes:
        o['kind'] = 'official-learning-outcome' if o['id'] in original else 'cross-course-capability'
        if o['id'] in original:
            o['officialText'] = original[o['id']]['text']
        o['sourceRefs'] = [source_ref(o['pdfPage'], o['id'])]
        o['learningPointIds'] = [p['id'] for p in points if o['id'] in p['outcomeIds']]

    reconciled = []
    for unit in extracted['contentUnits']:
        unit = copy.deepcopy(unit)
        index = int(unit['id'].split('-c')[1]) - 1
        patterns = CONTENT_MAP[unit['pdfPage']][index].split()
        matches = set()
        for pattern in patterns:
            found = {i for i in ids if fnmatch.fnmatchcase(i, 'pe26-' + pattern)}
            if not found:
                raise ValueError(f'No authored points for {unit["id"]}: {pattern}')
            matches |= found
        unit['learningPointIds'] = sorted(matches)
        unit['status'] = 'mapped-to-authored-requirements'
        reconciled.append(unit)

    for p in points:
        p['sourceRefs'] = [source_ref(outcome_by_id[o]['pdfPage'], o) for o in p['outcomeIds']]
        p['sourceContentIds'] = [u['id'] for u in reconciled if p['id'] in u['learningPointIds']]
        p['requirementStatus'] = 'syllabus-explicit' if p.pop('basis') == 'explicit' else 'supported-decomposition'
        p['editorialStatus'] = 'source-mapped-draft'
        p['contentCoverageStatus'] = 'not-assessed'
        p['acceptedContentIds'] = []
        p['flashcardAloneCanDemonstrate'] = False if set(p['evidenceModes']) & {'performance', 'project', 'investigation'} else None
        p['refreshPolicy'] = ('Verify current authoritative guidance before authoring factual answers; record source date.'
                              if p.pop('refresh') == 'current' else 'Review when the specification or supporting source changes.')
        p['requiresCurrentSource'] = 'Verify current' in p['refreshPolicy']
        if p['id'] in {'pe26-project-brief', 'pe26-project-eligibility'}:
            p['sourceRefs'] = [source_ref(23, 'Annual SEC brief'), source_ref(29, 'Appendix 2')]
        elif p['outcomeIds'] == ['AAC']:
            p['sourceRefs'] = [source_ref(23, 'Project process'), source_ref(24, 'Descriptors of quality')]

    named_checks = [{'pdfPage': page, 'sourceTerm': term, 'learningPointId': f'pe26-{prefix}-{suffix}'}
                    for page, prefix, pairs in NAMED_FAMILIES for suffix, term in pairs]

    issues = [
        {'id': 'teacher-depth-review', 'kind': 'editorial-review', 'blocks': 'exhaustiveness-certification',
         'detail': 'All 32 outcomes and 87 content bullets have draft mappings, but the breadth and depth of the decomposition and rubrics need subject-expert review. Structural reconciliation is not independent pedagogical validation.'},
        {'id': 'broad-anatomy-scope', 'kind': 'contextual-depth', 'blocks': 'activity-specific-completeness',
         'detail': 'The specification names relevant muscles, bones and joint actions without a fixed exhaustive anatomy list. Confirm concrete anatomy coverage for the activities used in teaching and assessment.'},
        {'id': 'current-domain-sources', 'kind': 'source-refresh', 'blocks': 'affected-answer-generation',
         'detail': 'Anti-doping, supplement evidence, current governing-body rules, policies and development programmes require current authoritative sources before answers are written. A requirement statement is not the factual answer.'},
        {'id': 'annual-project-brief', 'kind': 'cohort-overlay', 'blocks': 'assessment-profile-activation',
         'detail': 'No annual SEC project brief has been selected. Do not infer themes, deadlines, reporting format or accommodations from an older examination.'},
        {'id': 'reported-cohort-alignment', 'kind': 'administrative-verification', 'blocks': 'exam-year-profile-activation',
         'detail': 'User selected the three-strand course and reports sixth year. NCCA labels this specification for introduction in September 2026. The content target is explicit, but no exam-year mapping is asserted.'},
        {'id': 'secondary-source-limit', 'kind': 'source-depth', 'blocks': 'exhaustiveness-certification',
         'detail': 'The local SimpleStudy guide is an older topic taxonomy, not full three-strand lesson text. It cannot independently certify that all teachable detail has been captured.'},
        {'id': 'existing-content-unreviewed', 'kind': 'content-reuse', 'blocks': 'automatic-coverage-credit',
         'detail': 'Existing notes/cards have not been matched or verified. Preserve them for review; no source-text similarity or presence check earns coverage credit.'},
    ]
    bank = {
        'schemaVersion': 1, 'subject': 'pe', 'requirementsVersion': 'pe-three-strand-v1',
        'createdAt': '2026-09-17', 'status': 'source-reconciled-editorial-draft',
        'profile': {
            'specificationId': SOURCE_ID, 'strandCount': 3, 'officialOutcomeCount': 32,
            'selectionBasis': 'User explicitly selected the three-strand course they are studying.',
            'examYear': None, 'examYearVerified': False,
            'levels': ['Higher', 'Ordinary'], 'editorialDepth': 'Higher',
            'levelPolicy': 'All official outcomes apply at both levels. Adjust cognitive depth and scaffolding, not the outcome inventory (PDF pp. 11–12).',
            'prescribedTopicFilter': None,
            'assessment': {'specificationOnly': True, 'projectPercent': 50, 'writtenPercent': 50,
                           'annualBrief': None, 'sourceRefs': [source_ref(22, 'Assessment components'), source_ref(23, 'Project brief')]},
            'scope': 'Full three-strand learning requirements plus practical and project capabilities; no arbitrary card quota.',
        },
        'sources': [{
            'id': SOURCE_ID, 'role': 'scope-authority', 'title': 'Curriculum Specification for Leaving Certificate Physical Education — introduction September 2026',
            'path': 'pipeline/requirements/pe/sources/specification-2026.pdf', 'url': SOURCE_URL,
            'landingUrl': LANDING_URL, 'checkedAt': '2026-09-17', 'sha256': extracted['sha256'], 'pageCount': len(extracted['pages']),
        }, {
            'id': 'local-pe-guide', 'role': 'secondary-taxonomy-only', 'path': 'pipeline/resources/pe/guide-simplestudy.md',
            'limitation': 'Older two-strand/ten-topic structure; context and cross-check candidates only.',
        }, {
            'id': 'existing-pe-notes', 'role': 'unverified-content-candidates', 'path': 'pe-content.js',
            'limitation': 'Not a scope authority; not used to claim a requirement is already covered.',
        }],
        'strands': [
            {'id': 'S1', 'title': 'Skill learning, participation and performance'},
            {'id': 'S2', 'title': 'Physical and psychological demands of performance'},
            {'id': 'S3', 'title': 'Factors influencing participation in physical activity'},
        ],
        'outcomes': outcomes, 'learningPoints': points,
        'sourceContentReconciliation': reconciled, 'namedContentChecks': named_checks,
        'activityAreas': ['Games', 'Athletics', 'Dance', 'Gymnastics', 'Aquatics', 'Adventure'],
        'eligibleProjectActivities': {'sourceRefs': [source_ref(29, 'Appendix 2')], 'selection': 'conditional-on-annual-brief',
                                      'categories': ELIGIBLE_ACTIVITIES},
        'sourcePageAccounting': source_accounting(), 'openIssues': issues,
        'coveragePolicy': {
            'cardCountTargets': None,
            'requiredEvidence': 'Each acceptance criterion must have reviewed supporting content or assessed practical evidence.',
            'matchingStates': ['unassessed', 'candidate', 'partial', 'reviewed-covered', 'review-required', 'out-of-scope-for-profile'],
            'automaticCredit': False,
            'unmatchedExistingContent': 'Retain for review; never delete or mark irrelevant solely because a match was not found.',
            'pointIds': 'Stable identifiers. Revise a point explicitly; never regenerate IDs by list position.',
            'practicalEvidence': 'Knowing or recalling a description is not proof of a performance, investigation or project capability.',
            'completionClaim': 'Source mapping completeness only; not verified content coverage or independent certification of exhaustive teaching depth.',
        },
    }
    from validate import check_bank
    errors = check_bank(bank, extracted)
    if errors:
        raise ValueError('\n'.join(errors))
    write_json('requirements.json', bank)
    audit = {
        'status': 'structural-checks-passed-editorial-review-open',
        'specificationId': SOURCE_ID, 'sourceSha256': extracted['sha256'],
        'officialOutcomes': len(original), 'mappedOfficialOutcomes': len([o for o in outcomes if o['id'] in original]),
        'sourceContentBullets': len(extracted['contentUnits']), 'mappedSourceContentBullets': len(reconciled),
        'namedContentChecks': len(named_checks), 'learningPoints': len(points),
        'pointsByGroup': dict(Counter(p['outcomeIds'][0].split('.')[0] for p in points)),
        'requirementStatusCounts': dict(Counter(p['requirementStatus'] for p in points)),
        'sourcePagesAccountedFor': len(bank['sourcePageAccounting']),
        'existingCoverageAccepted': 0, 'independentlyCertifiedExhaustive': False,
        'openIssues': issues,
    }
    write_json('audit.json', audit)
    render_markdown(bank, audit)
    print(json.dumps({k: audit[k] for k in ['status', 'officialOutcomes', 'sourceContentBullets', 'namedContentChecks', 'learningPoints', 'pointsByGroup']}, indent=2))


def render_markdown(bank, audit):
    out = ['# PE required learning points — three-strand course', '',
           '**Status: source-reconciled editorial draft.** All numbered outcomes and all detailed content bullets have been accounted for. This is not a claim that the current flashcards cover them, or that an independent teacher has certified the teaching depth.', '',
           f"There are **{audit['learningPoints']} learning points** across the three strands and cross-course practical/project capabilities. These are not flashcard quotas.", '',
           '## Scope', '',
           'The user-selected three-strand specification is the source of scope. Its official publication label is “for introduction September 2026”; no exam-year profile has been activated. All outcomes apply at both levels. Acceptance criteria aim at Higher Level depth and can be scaffolded for Ordinary Level.', '',
           '[Official specification](sources/specification-2026.pdf) · [NCCA specification page](' + LANDING_URL + ')', '',
           'Each point states what must be demonstrated and what sufficient coverage should include. **Explicit** points are directly named/requested by the specification. **Decomposition** points are editorial breakdowns of a broader requirement and need depth review. All acceptance criteria are authored rubrics, not quotations or official marking schemes.', '',
           'Evidence labels matter: a card may support a practical skill, but it cannot establish that the learner has performed it. Investigation and project requirements need appropriate evidence beyond recall.', '',
           '## Source reconciliation', '',
           '| Check | Result |', '|---|---:|',
           f"| Official outcomes mapped | {audit['mappedOfficialOutcomes']}/{audit['officialOutcomes']} |",
           f"| Detailed source bullets mapped | {audit['mappedSourceContentBullets']}/{audit['sourceContentBullets']} |",
           f"| Named-item source checks | {audit['namedContentChecks']} |",
           '| Existing content credited as covered | 0 — matching has not started |', '',
           '## Items requiring review', '']
    for issue in bank['openIssues']:
        out.append(f"- **{issue['id']}**: {issue['detail']}")
    out.extend(['', '## Learning-point list', ''])
    points = {p['id']: p for p in bank['learningPoints']}
    for o in bank['outcomes']:
        out.extend([f"### {o['id']} — {o['title']}", '', o['requirement'], '',
                    f"Source: PDF page {o['pdfPage']} (printed page {o['printedPage']}).", ''])
        for pid in o['learningPointIds']:
            p = points[pid]
            basis = 'Explicit' if p['requirementStatus'] == 'syllabus-explicit' else 'Decomposition'
            evidence = ', '.join(p['evidenceModes'])
            out.extend([f"**{p['id']} — {p['statement']}**", '',
                        f"{basis} · Evidence: {evidence}" + (' · Requires current factual sources' if p['requiresCurrentSource'] else ''), ''])
            out.extend(f'- {x}' for x in p['acceptanceCriteria'])
            if any(ref['pdfPage'] != o['pdfPage'] for ref in p['sourceRefs']):
                out.extend(['', 'Specific source: ' + '; '.join(f"PDF p. {r['pdfPage']} — {r['locator']}" for r in p['sourceRefs'])])
            out.append('')
    out.extend(['## Eligible project activities', '',
                'This is the Appendix 2 eligibility catalogue, not a requirement that every student master every activity. The applicable annual SEC brief remains controlling.', '',
                '| Category | Eligible activities |', '|---|---|'])
    for category, activities in ELIGIBLE_ACTIVITIES.items():
        out.append(f"| {category} | {'; '.join(activities)} |")
    out.extend(['', '## Complete content-bullet reconciliation', '',
                'Source wording below is retained to make omissions inspectable. Mappings indicate requirement coverage, not card coverage.', ''])
    for u in bank['sourceContentReconciliation']:
        out.extend([f"**{u['id']} · PDF p. {u['pdfPage']}**: {u['text']}", '',
                    'Mapped points: ' + ', '.join(u['learningPointIds']), ''])
    (HERE / 'requirements.md').write_text('\n'.join(out))


if __name__ == '__main__':
    build()
