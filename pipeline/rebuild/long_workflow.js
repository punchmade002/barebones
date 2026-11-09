export const meta = {
  name: 'bank-fill-long',
  description: 'Sonnet writes brief full-marks long answers (5 questions per agent), a second Sonnet checks every one, one fix round, anything still failing is flagged',
  phases: [
    { title: 'Write', detail: 'one Sonnet agent per 5-question package', model: 'sonnet' },
    { title: 'Check', detail: 'one Sonnet checker per package, every answer', model: 'sonnet' },
    { title: 'Recheck', detail: 'one Sonnet re-check of fixed answers per package that had fixes', model: 'sonnet' },
  ],
}
// args: { subject: 'Physical Education', dir, crops, names: ['l00', ...], wordsPerMark: 12 }   (fill_packages.py)
const SUBJ = args.subject
const WPM = args.wordsPerMark || 12
const STYLE = `Answer style (this matters as much as correctness): the shortest answer that still earns FULL marks, easy to read at a glance.
- Read the rule and scheme first. Give exactly the number of points or elements the scheme rewards (if it asks for two, give two) and make each one hit the top band: specific, accurate and applied to the question (and to the case study when the question says so). Top-band marks come from detail and accuracy, not length.
- One point per line. Start each line with a short label and a colon, then one or two plain sentences: the point, then why or how, with a concrete example. End each line with a full stop.
- Keep to about ${WPM} words per mark at most: what a strong student could write in the exam time. No introduction, no conclusion, no restating the question.
- Write as the student would. No markdown, no bullet symbols, no mark tallies such as "(6)", no "//", no "[accept …]", "allow" or "also acceptable"; give one alternative, not a list of them.`
const ITEM_KEYS = 'id; text = the question part as transcribed from the paper; marks; scheme = the official marking-scheme points or criteria; rule = how the scheme awards the marks; figure = how the part uses a figure (if it does); hint / hint_unchecked = an earlier answer to this part (a hint only: it may be wrong, padded or off-target). A line with a "context" field instead of an id carries shared material (case study, table) for that question\'s parts'
const WRITE = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model'], properties: { id: { type: 'string' }, model: { type: 'string' } } } } } }
const CHECK = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['id', 'fullMarks', 'issue', 'fixedModel'], properties: { id: { type: 'string' }, fullMarks: { type: 'boolean' },
    issue: { type: 'string' }, fixedModel: { type: 'string', description: 'if fullMarks is false: the corrected answer; else empty' } } } } } }
const file = name => `${args.dir}/${name}.json`
const crops = `${args.crops}/<question>-1.png (then -2.png etc.), where question is the id before "|"`

const results = await pipeline(args.names,
  name => agent(
`Write full-marks model answers for Leaving Certificate ${SUBJ} long-answer exam parts. Read ${file(name)} (one item per line). If a part uses a figure or the case study and the text/context lines do not give you enough, read that question's crop images ${crops}. Read nothing else.
Each item has: ${ITEM_KEYS}.
${STYLE}
Return one answer per item with an id, using exactly the same ids.`,
    { label: `write:${name}`, phase: 'Write', model: 'sonnet', schema: WRITE }),
  (w, name) => {
    const ans = Object.fromEntries(((w && w.answers) || []).filter(a => a.model).map(a => [a.id, a.model]))
    return agent(
`You are a senior examiner checking model answers for a Leaving Certificate ${SUBJ} answer bank. The questions are in ${file(name)} (one item per line); read it, and a question's crop images ${crops} only if you need the figure or case study. Read nothing else.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(ans)}
For each answer decide fullMarks: would it earn FULL marks under this part's scheme and rule (right number of points, each accurate, developed enough for the top band, answering the exact question, applied to the case study where asked)? Also fail it if it is clearly padded beyond what full marks need, or breaks the style below. Be strict but fair.
If fullMarks=false: issue says what is wrong; fixedModel is the corrected answer. ${STYLE}
Return one result per answer.`,
      { label: `check:${name}`, phase: 'Check', model: 'sonnet', schema: CHECK }).then(c => ({ ans, check: c }))
  },
  (r, name) => {
    const fixes = ((r.check && r.check.results) || []).filter(v => !v.fullMarks && v.fixedModel)
    if (!fixes.length) return { ...r, recheck: null }
    return agent(
`You are a senior examiner re-checking corrected model answers for a Leaving Certificate ${SUBJ} answer bank. The questions are in ${file(name)} (one item per line); read it, and a question's crop images ${crops} only if needed. Read nothing else.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(Object.fromEntries(fixes.map(v => [v.id, v.fixedModel])))}
For each: fullMarks = would it earn FULL marks under the scheme and rule, and is it no longer than full marks needs? issue = what is still wrong (or ""). Leave fixedModel empty: this is the last check.
${STYLE}
Return one result per answer.`,
      { label: `recheck:${name}`, phase: 'Recheck', model: 'sonnet', schema: CHECK }).then(rc => ({ ...r, recheck: rc }))
  })

const final = {}, flagged = [], log_ = { written: 0, passedFirst: 0, fixed: 0, flagged: 0, missingCheck: 0 }
results.forEach((r, i) => {
  if (!r) { flagged.push({ pkg: args.names[i], issue: 'package failed' }); return }
  const verdict = Object.fromEntries(((r.check && r.check.results) || []).map(v => [v.id, v]))
  const re = Object.fromEntries(((r.recheck && r.recheck.results) || []).map(v => [v.id, v]))
  for (const [id, model] of Object.entries(r.ans)) {
    log_.written++
    const v = verdict[id]
    if (!v) { log_.missingCheck++; flagged.push({ id, issue: 'no check verdict', model }); continue }
    if (v.fullMarks) { log_.passedFirst++; final[id] = { model, by: 'sonnet-long' }; continue }
    const rv = re[id]
    if (v.fixedModel && rv && rv.fullMarks) { log_.fixed++; final[id] = { model: v.fixedModel, by: 'sonnet-long-fix', issue: v.issue }; continue }
    log_.flagged++
    flagged.push({ id, issue: (rv && rv.issue) || v.issue, model: v.fixedModel || model })
  }
})
log(`written ${log_.written}; passed first check ${log_.passedFirst}; fixed ${log_.fixed}; flagged ${log_.flagged}; no verdict ${log_.missingCheck}`)
return { answers: final, flagged, stats: log_, checks: results.map(r => r && r.check), rechecks: results.map(r => r && r.recheck) }
