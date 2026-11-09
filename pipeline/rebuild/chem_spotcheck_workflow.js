export const meta = {
  name: 'chem-answer-spotcheck',
  description: 'Independent Sonnet re-marks a sample of audited chemistry answers; fixes any that miss full marks; Haiku confirms the fixes',
  phases: [
    { title: 'Verify', detail: 'Sonnet re-marks sampled answers against the scheme', model: 'sonnet' },
    { title: 'Confirm', detail: 'Haiku checks each correction', model: 'haiku' },
  ],
}
const BASE = args.base
function paperLine(key) {
  const [y, level] = key.split('-'); const year = Number(y)
  const ref = year === 2001 ? '-REF' : ''
  const scheme = (year === 2001 || (year === 2002 && level === 'ordinary')) ? `marking scheme is a scanned PDF: read page images p-*.png in ${BASE}/scheme-png/${year}-${level}-EV-scheme${ref}/`
    : year === 2008 ? 'NO marking scheme exists: judge by correct Leaving Certificate Chemistry for the marks shown'
    : `marking scheme text: ${BASE}/text/${year}-${level}-EV-scheme${ref}.txt (grep for the question numbers)`
  return `- ${year} ${level}: paper text ${BASE}/text/${year}-${level}-EV-papers${ref}.txt; ${scheme}.`
}
const RESULT = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['qi', 'pi', 'fullMarks', 'issue', 'fixedModel'],
  properties: { qi: { type: 'integer' }, pi: { type: 'integer' }, fullMarks: { type: 'boolean' }, issue: { type: 'string' },
    fixedModel: { type: 'string', description: 'if fullMarks is false: a concise student-facing answer that earns full marks; else empty' } } } } } }
const CHECK = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['qi', 'pi', 'pass', 'issue'], properties: { qi: { type: 'integer' }, pi: { type: 'integer' }, pass: { type: 'boolean' }, issue: { type: 'string' } } } } } }
const key = v => `${v.qi}:${v.pi}`

const out = await pipeline(args.batches,
  b => agent(`You are an independent senior examiner re-marking model answers from a Leaving Certificate Chemistry answer bank.
Items to re-mark (qi, pi, qref = exact paper question, question, marks, model answer) are in ${BASE}/spotcheck/${b}.json.
Papers:
${b.split('_').slice(1).map(paperLine).join('\n')}
Do not explore the repo beyond these files.
For each item, find that exact part in the marking scheme and decide whether the model answer would earn FULL marks: every required scheme point (or accepted alternative), calculations correct with working, nothing chemically wrong, answering that exact part. fullMarks=false => issue says what is missing/wrong, and fixedModel is a concise, student-facing full-marks answer (unicode formulae like H₂SO₄; no examiner notation like "[accept ...]"; separate points with new lines). Return one result per item.`,
    { label: `verify:${b}`, phase: 'Verify', model: 'sonnet', schema: RESULT }),
  async (v, b) => {
    const results = (v && v.results) || []
    const fixes = results.filter(r => !r.fullMarks && r.fixedModel)
    if (!fixes.length) return { batch: b, results, checks: [] }
    const ck = await agent(`Check corrected model answers for a Leaving Certificate Chemistry answer bank against the official marking scheme.
The questions (by qi/pi) are in ${BASE}/spotcheck/${b}.json. Papers:
${b.split('_').slice(1).map(paperLine).join('\n')}
Do not explore the repo beyond these files.
Corrected answers: ${JSON.stringify(fixes.map(f => ({ qi: f.qi, pi: f.pi, answer: f.fixedModel })))}
pass = true only if the answer earns FULL marks for that exact part under the scheme; otherwise issue says what is wrong. Be strict.`,
      { label: `confirm:${b}`, phase: 'Confirm', model: 'haiku', schema: CHECK })
    return { batch: b, results, checks: (ck && ck.results) || [] }
  })
return { results: out.filter(Boolean) }
