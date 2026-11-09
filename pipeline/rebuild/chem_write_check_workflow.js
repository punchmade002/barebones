export const meta = {
  name: 'chemistry-write-check',
  description: 'Sonnet: write notes-only Chemistry model answers per question (reusing audited old answers where they meet the scheme), independent check, max 3 rounds',
  phases: [
    { title: 'Write', detail: 'sonnet writer reads one state file + listed notes', model: 'sonnet' },
    { title: 'Check', detail: 'sonnet checker verifies vs scheme points + notes by grep', model: 'sonnet' },
  ],
}

const D = '/Users/gabrielwhelan/barebones/pipeline/_data/rebuild/chemistry'

const WRITE = { type: 'object', properties: { parts: { type: 'array', items: { type: 'object', properties: {
  label: { type: 'string' }, status: { type: 'string', enum: ['answered', 'off-spec', 'notes-gap'] },
  answer: { type: 'string' }, notesRefs: { type: 'array', items: { type: 'string' } },
  reusedOld: { type: 'boolean' }, gap: { type: 'string' },
}, required: ['label', 'status', 'answer', 'notesRefs', 'reusedOld', 'gap'] } } }, required: ['parts'] }

const CHECK = { type: 'object', properties: { parts: { type: 'array', items: { type: 'object', properties: {
  label: { type: 'string' }, verdict: { type: 'string', enum: ['pass', 'fail'] },
  problems: { type: 'string' }, fix: { type: 'string' },
}, required: ['label', 'verdict', 'problems', 'fix'] } } }, required: ['parts'] }

const RULES = `Answers: concise and scheme-complete. Give every point the scheme needs for full marks (respect "any N" rules) and nothing that earns no marks; plain student sentences, single words where the question says name/state. Tick/true-false/matching: give the choices plainly. Draw/label: state what the diagram must show and list the labels. Show working for calculations, with the final answer and units. Write formulae and equations correctly (unicode sub/superscripts, e.g. H₂SO₄, Cu²⁺) and balance every equation.
Knowledge: every chemistry fact must be in the app notes (${D}/notes/<loId>.md) or be data printed on the question; cite loIds (or "question"). No outside knowledge. If a needed scheme point is not in the notes, status "notes-gap", still give the best notes-only answer, and name the missing point in "gap". Off-spec parts (offSpec true): status "off-spec", answer "" — unless the notes clearly cover it, then answer it.`

function writePrompt(key, prior) {
  return `Write model answers for Leaving Cert Chemistry question ${key}.
Everything about the question is in ${D}/state/${key}.json: each part's transcription, marks, schemePoints, fullMarksRule, loIds, offSpec. Read it first.
Then read only the notes files for those loIds (${D}/notes/<loId>.md); grep ${D}/notes for a term if a fact is elsewhere. Look at the crop images listed in "crops" only for parts whose diagramRelation is not "none" or whose text is unclear.
${RULES}
${prior ? `REVISION: rewrite only these parts, fixing every problem the checker found, and return entries only for them:\n${JSON.stringify(prior)}` : 'If "oldAnswer" is set, read it: each line is "<label> [kept|written]: <answer>", an earlier answer already audited against the marking scheme. Its labels may not match the scan exactly. Reuse a line for a part (set reusedOld) only if it answers that exact scanned part and meets every scheme point; its facts must still be in the notes. Return one entry per part label.'}
Do not modify files.`
}

function checkPrompt(key, answers) {
  return `You are a strict SEC examiner checking model answers for Leaving Cert Chemistry question ${key}.
The question parts, marks, schemePoints and fullMarksRule are in ${D}/state/${key}.json. Answers to check:
${JSON.stringify(answers)}
Pass a part only if: it answers the part as set (right command word and number of points); it would get full marks under the scheme; it is factually correct and has no padding; and its facts are in the notes. Check facts by grepping ${D}/notes for the key terms (do not read whole files unless needed). View a crop image (listed in "crops") only if the answer depends on a figure.
"off-spec": pass only if the topic really is not covered by the notes. "notes-gap": pass only if a grep of the notes confirms the point is missing.
Fail only for concrete problems and give the exact fix. One entry per label given. Do not modify files.`
}

const keys = typeof args === 'string' ? args.trim().split(/\s+/).map(c => `${c.slice(0, 4)}-${c[4] === 'h' ? 'higher' : 'ordinary'}-q${Number(c.slice(5))}`) : args
const results = await pipeline(keys, async (key) => {
  const first = await agent(writePrompt(key, null), { label: `write:${key}#1`, phase: 'Write', schema: WRITE, model: 'sonnet' })
  if (!first) return { key, failed: true }
  const answers = new Map(first.parts.map(a => [a.label, a]))
  let pending = [...answers.keys()], round = 1
  while (pending.length) {
    const v = await agent(checkPrompt(key, pending.map(l => answers.get(l))), { label: `check:${key}#${round}`, phase: 'Check', schema: CHECK, model: 'sonnet' })
    if (!v) break
    const fails = v.parts.filter(p => p.verdict === 'fail' && answers.has(p.label))
    pending = fails.map(f => f.label)
    if (!pending.length || round >= 3) break
    round++
    const rev = await agent(writePrompt(key, fails.map(f => ({ label: f.label, previous: answers.get(f.label).answer, problems: f.problems, fix: f.fix }))),
      { label: `write:${key}#${round}`, phase: 'Write', schema: WRITE, model: 'sonnet' })
    if (!rev) break
    rev.parts.forEach(a => { if (answers.has(a.label)) answers.set(a.label, a) })
  }
  return { key, flagged: pending.length }
})
const done = results.filter(r => r && !r.failed)
return { done: done.length, flaggedParts: done.reduce((s, r) => s + r.flagged, 0), failed: results.filter(r => !r || r.failed).length }
