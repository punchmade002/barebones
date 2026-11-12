export const meta = {
  name: 'history-long',
  description: 'History long answers: Sonnet writes 3 similar essays per agent from the notes, a second Sonnet checks every one, one fix round, anything still failing is flagged',
  phases: [
    { title: 'Write', detail: 'one Sonnet agent per 3-question package', model: 'sonnet' },
    { title: 'Check', detail: 'one Sonnet checker per package, every answer', model: 'sonnet' },
    { title: 'Recheck', detail: 'one Sonnet re-check of fixed answers per package that had fixes', model: 'sonnet' },
  ],
}
// args: { subject: 'History', dir, crops, notesDir, names: ['h000', ...] }   (hist_long_packages.py)
// long_workflow.js with a History essay style and notes reading in place of the point-per-line style.
const SUBJ = args.subject
const STYLE = `Answer style (this matters as much as correctness):
- Higher essay (100 marks, CM 60 by paragraph + OE 40): about 6 paragraphs, 650-800 words, what a top student writes in the exam. Paragraph 1 answers the question directly in 2-3 sentences. Then 4-5 body paragraphs, each making one main point that answers the question as set, backed by specific accurate evidence (names, dates, places, figures, results) and a sentence of analysis tying it back to the question. A short final paragraph gives a clear judgement. Where the question has two elements (two topics, "and", causes and results, successes and failures, X and/or Y) cover each with real weight; where the scheme note says TWO elements, both must be developed.
- Higher DBQ question 4 (40 marks, CM 24 by paragraph + OE 16): 3-4 paragraphs, 350-450 words, same approach; cover both elements where asked.
- Separate paragraphs with a blank line. Plain prose: no headings, no labels with colons, no bold, no bullets, no "Introduction"/"Conclusion" words. Write as the student would. No mark tallies, no "//", no "[accept ...]", "allow" or "also acceptable".
- Accuracy first: use facts the notes support, or well-established facts you are certain of. Never invent quotations, statistics or dates; leave a detail out rather than guess.`
// Sonnet overestimates length (tranche 1 failed 49 essays of 615-807 words as "about 900"), so the script counts.
const wc = ans => Object.fromEntries(Object.entries(ans).map(([id, m]) => [id, m.split(/\s+/).filter(Boolean).length]))
const LENGTH = 'Judge length ONLY from the measured word counts given, never your own estimate: fail for length only above 900 words (DBQ question 4: above 550), never for being a little over the target.'
const NOTES = `Each package starts with a "notes for <chapter>" line listing that chapter's notes sections ("<loId> — [ref] title"); each section is the file ${args.notesDir}/<loId>.md. For each question read the two to four sections that cover it (each file at most once).`
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
`Write full-marks model answers for Leaving Certificate ${SUBJ} long-answer exam parts. Read ${file(name)} (one item per line). ${NOTES} A line with a case-study context carries the documents-based question's case study and documents. Read nothing else.
Each item has: ${ITEM_KEYS}.
${STYLE}
Return one answer per item with an id, using exactly the same ids.`,
    { label: `write:${name}`, phase: 'Write', model: 'sonnet', schema: WRITE }),
  (w, name) => {
    const ans = Object.fromEntries(((w && w.answers) || []).filter(a => a.model).map(a => [a.id, a.model]))
    return agent(
`You are a senior examiner checking model answers for a Leaving Certificate ${SUBJ} answer bank. The questions are in ${file(name)} (one item per line); read it. ${NOTES} Read the sections you need to judge accuracy, and nothing else.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(ans)}
MEASURED WORD COUNTS: ${JSON.stringify(wc(ans))}. ${LENGTH}
For each answer decide fullMarks: would it earn FULL marks under this part's scheme and rule (every element of the question covered with real weight, each paragraph accurate and developed enough for the excellent band, analysis that answers the exact question, a clear judgement; any factual error fails it)? Also fail it if it breaks the style below. Be strict but fair.
If fullMarks=false: issue says what is wrong; fixedModel is the corrected answer. ${STYLE}
Return one result per answer.`,
      { label: `check:${name}`, phase: 'Check', model: 'sonnet', schema: CHECK }).then(c => ({ ans, check: c }))
  },
  (r, name) => {
    const fixes = ((r.check && r.check.results) || []).filter(v => !v.fullMarks && v.fixedModel)
    if (!fixes.length) return { ...r, recheck: null }
    return agent(
`You are a senior examiner re-checking corrected model answers for a Leaving Certificate ${SUBJ} answer bank. The questions are in ${file(name)} (one item per line); read it, and notes sections only if needed (${NOTES}). Read nothing else.
Each item has: ${ITEM_KEYS}.
ANSWERS TO CHECK (id -> answer): ${JSON.stringify(Object.fromEntries(fixes.map(v => [v.id, v.fixedModel])))}
MEASURED WORD COUNTS: ${JSON.stringify(wc(Object.fromEntries(fixes.map(v => [v.id, v.fixedModel]))))}. ${LENGTH}
For each: fullMarks = would it earn FULL marks under the scheme and rule, and is it within the length rule? issue = what is still wrong (or ""). Leave fixedModel empty: this is the last check.
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
