export const meta = {
  name: 'bank-fill-short',
  description: 'Haiku writes full-marks short answers (10 questions per agent, scheme inline in one file); Sonnet answers figure parts and spot-checks 5 packages, checking the rest only if errors turn up',
  phases: [
    { title: 'Write', detail: 'one Haiku agent per package', model: 'haiku' },
    { title: 'Figures', detail: 'Sonnet answers parts Haiku could not do without the figure', model: 'sonnet' },
    { title: 'Check', detail: 'Sonnet checks 2 packages per agent: 5 sampled, the rest on any error', model: 'sonnet' },
  ],
}
// args: { subject: 'Physical Education', dir, crops, names: ['p00', ...], sample: [i, ...] }   (fill_packages.py)
// Optional: extraStyle (subject-specific answer rules); resources (Geography: a dir holding
// <year>-os-map-*.png / <year>-aerial-photo-*.png and <year>-os-map-gazetteer.txt). Parts tagged
// with a "resource" skip Haiku and go straight to Sonnet with the map or photo.
// The Chemistry recipe (chem_fill_workflow.js) with the subject as a parameter.
const SUBJ = args.subject
const STYLE = `Answer style: write it as the student would, in their own words, short and easy to digest. Cover every scheme point and nothing more: where the question asks for N things give exactly N; where the scheme lists alternatives give one, never "X or Y is also acceptable"; give a single value, never the scheme's accepted range. Put each point on its own line and end it with a full stop; a point can start with a short label and a colon (e.g. "Short-term goal: …"). No markdown, no bullet symbols, no mark tallies such as "(3)", no "//", no "[accept …]" or "allow". Calculations show working, units and the final value.` + (args.extraStyle ? ' ' + args.extraStyle : '')
const ITEM_KEYS = 'id; text = the question part as transcribed from the paper; marks; scheme = the official marking-scheme points or criteria; rule = how the scheme awards the marks; figure = how the part uses a figure (if it does); hint = an earlier checked answer to this part or the part containing it (reuse only what fits this exact part); hint_unchecked = an earlier unchecked answer (may be wrong or padded: use only what is correct). resource = os-map or aerial-photo when the part uses the map or photograph supplied with the paper. A line with a "context" field instead of an id carries shared material (case study, table) for that question\'s parts'
const WRITE = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model', 'needsFigure'], properties: { id: { type: 'string' }, model: { type: 'string' }, needsFigure: { type: 'boolean' } } } } } }
const FIG = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model'], properties: { id: { type: 'string' }, model: { type: 'string' } } } } } }
const CHECK = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['id', 'fullMarks', 'issue', 'fixedModel'], properties: { id: { type: 'string' }, fullMarks: { type: 'boolean' },
    issue: { type: 'string' }, fixedModel: { type: 'string', description: 'if fullMarks is false: the corrected full-marks answer; else empty' } } } } } }
const file = name => `${args.dir}/${name}.json`
const N = args.names
// History: "n" packages hold one chapter's notes-based parts (scheme has no content points); their
// first line lists the chapter's notes sections, each in ${args.notesDir}/<loId>.md.
const notesPkg = name => args.notesDir && name.startsWith('n')
const NOTES_READ = `The first line of this file lists the notes sections for its chapter ("<loId> — title"); each section is the file ${args.notesDir}/<loId>.md. For each part, read the one or two sections that cover it (read each file at most once, and no other files) and write only what those notes support.`

phase('Write')
const written = await parallel(N.map(name => () => agent(
`Write full-marks model answers for Leaving Certificate ${SUBJ} exam parts. Read ${file(name)} (one Read call; one item per line)${notesPkg(name) ? '. ' + NOTES_READ : ' and nothing else: no other files, no searching.'}
Each item has: ${ITEM_KEYS}.
${STYLE}
If a part truly cannot be answered without seeing a figure or table that the text does not describe${args.resources ? ', or it has a "resource" field' : ''}, set needsFigure=true and model="". Otherwise needsFigure=false. Return one answer per item with an id, using exactly the same ids.`,
  { label: `write:${name}`, phase: 'Write', model: 'haiku', schema: WRITE })))

const answers = {}
const figure = {}                                   // question key -> [{id, pkg}]
written.forEach((w, i) => {
  for (const a of (w && w.answers) || []) {
    const k = a.id.split('|')[0]
    if (a.needsFigure) (figure[k] = figure[k] || []).push({ id: a.id, pkg: N[i] })
    else if (a.model) answers[a.id] = { model: a.model, by: 'haiku', pkg: i }
  }
})
const figKeys = Object.keys(figure)
log(`Haiku answered ${Object.keys(answers).length} parts; ${figKeys.reduce((n, k) => n + figure[k].length, 0)} parts in ${figKeys.length} questions need the figure; ${written.filter(w => !w).length} writer agents failed`)

const figBatches = []
for (let i = 0; i < figKeys.length; i += 8) figBatches.push(figKeys.slice(i, i + 8))
const figOut = await parallel(figBatches.map((keys, b) => () => {
  const ids = keys.flatMap(k => figure[k])
  const files = [...new Set(ids.map(x => file(x.pkg)))]
  return agent(
`Write full-marks model answers for Leaving Certificate ${SUBJ} exam parts that depend on a figure or table.
The items are in ${files.join(' and ')} (one item per line); answer only these ids: ${JSON.stringify(ids.map(x => x.id))}.
For each question, read its crop image(s) ${args.crops}/<question>-1.png (then -2.png etc. if present), where question is the id before "|".${args.resources ? ` For an item with resource os-map also read ${args.resources}/<year>-os-map-full.png and its four tiles -tile-00.png, -tile-01.png, -tile-10.png, -tile-11.png, plus ${args.resources}/<year>-os-map-gazetteer.txt if it exists (printed names with grid references taken from the map file: trust it over your reading of the image); for aerial-photo the same image names with aerial-photo. <year> is the first 4 characters of the id. Where the scheme lists the accepted answers (grid references, features, photo locations), use one of them.` : ''} Read nothing else.
Each item has: ${ITEM_KEYS}.
${STYLE}
Return one answer per id.`,
    { label: `figure:${b}`, phase: 'Figures', model: 'sonnet', schema: FIG })
}))
for (const f of figOut.filter(Boolean)) for (const a of f.answers) if (a.model) answers[a.id] = { model: a.model, by: 'sonnet-figure' }

const checkPair = (idxs, tag) => {
  const toCheck = Object.fromEntries(Object.entries(answers).filter(([, a]) => a.by === 'haiku' && idxs.includes(a.pkg)).map(([id, a]) => [id, a.model]))
  return agent(
`You are a senior examiner checking model answers for a Leaving Certificate ${SUBJ} answer bank.
The questions are in ${idxs.map(i => file(N[i])).join(' and ')} (one item per line). Read only those files${idxs.some(i => notesPkg(N[i])) ? `, plus, for a file whose first line lists notes sections, the sections in ${args.notesDir}/<loId>.md you need to judge accuracy` : ''}.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(toCheck)}
For each answer decide fullMarks: would it earn FULL marks for that exact part under the scheme (every required point, accurate content, answers the question actually asked)? Be strict but fair: wording a teacher would accept is fine, and brevity is wanted. If fullMarks=false, issue says what is wrong and fixedModel is a corrected full-marks answer. ${STYLE}
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
