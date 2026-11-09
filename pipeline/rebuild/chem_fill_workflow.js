export const meta = {
  name: 'chem-fill',
  description: 'Haiku writes full-marks answers for unanswered chemistry parts (10 questions per agent, scheme inline in one file); Sonnet spot-checks 5 packages and checks the rest only if errors turn up',
  phases: [
    { title: 'Write', detail: 'one Haiku agent per 10-question package', model: 'haiku' },
    { title: 'Figures', detail: 'Sonnet answers parts Haiku could not do without the figure', model: 'sonnet' },
    { title: 'Check', detail: 'Sonnet checks 2 packages per agent: 5 sampled, the rest on any error', model: 'sonnet' },
  ],
}
// args: { dir, crops, names: ['p00', ...], sample: [i, ...] }   (built by chem_fill_packages.py)
const STYLE = `Answer style: concise and student-facing; cover every required scheme point (where the scheme lists alternatives, give the standard one; where it asks for N points, give N); calculations show working, units and the final value; unicode formulae (H₂SO₄, cm³, →); separate points with new lines; no examiner notation ("(3)", "//", "[accept …]"); for draw-a-diagram parts describe the labelled diagram in words.`
const ITEM_KEYS = 'id; text = the question part as transcribed from the paper ([Stem: …] gives shared context); marks; scheme = the official marking-scheme points; rule = how the scheme awards the marks; figure = how the part uses a figure (if it does); hint = an earlier checked answer to this part or the part containing it (reuse only what fits this exact part)'
const WRITE = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model', 'needsFigure'], properties: { id: { type: 'string' }, model: { type: 'string' }, needsFigure: { type: 'boolean' } } } } } }
const FIG = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model'], properties: { id: { type: 'string' }, model: { type: 'string' } } } } } }
const CHECK = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['id', 'fullMarks', 'issue', 'fixedModel'], properties: { id: { type: 'string' }, fullMarks: { type: 'boolean' },
    issue: { type: 'string' }, fixedModel: { type: 'string', description: 'if fullMarks is false: the corrected full-marks answer; else empty' } } } } } }
const file = name => `${args.dir}/${name}.json`
const N = args.names

phase('Write')
const written = await parallel(N.map(name => () => agent(
`Write full-marks model answers for Leaving Certificate Chemistry exam parts. Read ${file(name)} (one Read call; one item per line) and nothing else: no other files, no searching.
Each item has: ${ITEM_KEYS}.
${STYLE}
If a part truly cannot be answered without seeing a figure or table that the text does not describe, set needsFigure=true and model="". Otherwise needsFigure=false. Return one answer per item, same ids.`,
  { label: `write:${name}`, phase: 'Write', model: 'haiku', schema: WRITE })))

const answers = {}
const figure = {}                                   // question key -> [{id, pkg}]
written.forEach((w, i) => {
  for (const a of (w && w.answers) || []) {
    if (a.needsFigure) (figure[a.id.split('|')[0]] = figure[a.id.split('|')[0]] || []).push({ id: a.id, pkg: N[i] })
    else if (a.model) answers[a.id] = { model: a.model, by: 'haiku', pkg: i }
  }
})
const figKeys = Object.keys(figure)
log(`Haiku answered ${Object.keys(answers).length} parts; ${figKeys.reduce((n, k) => n + figure[k].length, 0)} parts in ${figKeys.length} questions need the figure; ${written.filter(w => !w).length} writer agents failed`)

// Figure parts: Sonnet with the question crops, 8 questions per agent.
const figBatches = []
for (let i = 0; i < figKeys.length; i += 8) figBatches.push(figKeys.slice(i, i + 8))
const figOut = await parallel(figBatches.map((keys, b) => () => {
  const ids = keys.flatMap(k => figure[k])
  const files = [...new Set(ids.map(x => file(x.pkg)))]
  return agent(
`Write full-marks model answers for Leaving Certificate Chemistry exam parts that depend on a figure or table.
The items are in ${files.join(' and ')} (one item per line); answer only these ids: ${JSON.stringify(ids.map(x => x.id))}.
For each question, read its crop image(s) ${args.crops}/<question>-1.png (then -2.png etc. if present), where question is the id before "|". Read nothing else.
Each item has: ${ITEM_KEYS}.
${STYLE}
Return one answer per id.`,
    { label: `figure:${b}`, phase: 'Figures', model: 'sonnet', schema: FIG })
}))
for (const f of figOut.filter(Boolean)) for (const a of f.answers) if (a.model) answers[a.id] = { model: a.model, by: 'sonnet-figure' }

// Sonnet check: 2 packages per agent. The sample first; the rest only if the sample has errors.
const checkPair = (idxs, tag) => {
  const toCheck = Object.fromEntries(Object.entries(answers).filter(([, a]) => a.by === 'haiku' && idxs.includes(a.pkg)).map(([id, a]) => [id, a.model]))
  return agent(
`You are a senior examiner checking model answers for a Leaving Certificate Chemistry answer bank.
The questions are in ${idxs.map(i => file(N[i])).join(' and ')} (one item per line). Read only those files.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(toCheck)}
For each answer decide fullMarks: would it earn FULL marks for that exact part under the scheme (every required point, correct chemistry, calculations right with units)? Be strict but fair: wording a teacher would accept is fine. If fullMarks=false, issue says what is wrong and fixedModel is a corrected full-marks answer. ${STYLE}
Return one result per answer.`,
    { label: `check:${tag}:${idxs.map(i => N[i]).join('+')}`, phase: 'Check', model: 'sonnet', schema: CHECK })
}
const pairs = list => { const out = []; for (let i = 0; i < list.length; i += 2) out.push(list.slice(i, i + 2)); return out }
const checks = []
const runChecks = async (list, tag) => {
  const res = await parallel(pairs(list).map(pr => () => checkPair(pr, tag)))
  let errors = 0
  for (const r of res.filter(Boolean)) for (const v of r.results) {
    checks.push({ ...v, round: tag })
    if (!v.fullMarks && answers[v.id]) { errors++; if (v.fixedModel) answers[v.id] = { model: v.fixedModel, by: 'sonnet-fix', pkg: answers[v.id].pkg, issue: v.issue } }
  }
  return { errors, failedAgents: res.filter(r => !r).length }
}
const s = await runChecks(args.sample, 'sample')
log(`Sample (${args.sample.map(i => N[i]).join(', ')}): ${s.errors} errors, ${s.failedAgents} failed agents`)
let rest = null
if (s.errors > 0 || s.failedAgents > 0) {
  rest = await runChecks(N.map((_, i) => i).filter(i => !args.sample.includes(i)), 'rest')
  log(`Remaining packages: ${rest.errors} errors fixed`)
}
return { answers, checks, checkedPkgs: rest ? N : args.sample.map(i => N[i]), sampleErrors: s.errors, restErrors: rest && rest.errors }
