export const meta = {
  name: 'chem-tidy',
  description: 'Haiku strips examiner notation from chemistry model answers (format only, chemistry unchanged)',
  phases: [{ title: 'Tidy', detail: 'one Haiku agent per batch of flagged answers', model: 'haiku' }],
}
// args: { dir, names: ['t00', ...] }   (each batch file: [{id, answer, flags}] one per line)
const OUT = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model'], properties: { id: { type: 'string' }, model: { type: 'string' } } } } } }
const out = await parallel(args.names.map(name => () => agent(
`Rewrite Leaving Certificate Chemistry model answers so they read like a student's full-marks answer, not a marking scheme. Read ${args.dir}/${name}.json (one item per line: id, answer, flags = what was detected) and nothing else.
Fix only the presentation:
- remove mark tallies such as "(3)", "(6)" (keep genuine numbering like "Equation (2)")
- "a // b // c" or "a / b / c" listing alternatives: keep the single best standard alternative (or as many as the question needs if they are separate required points)
- remove "[Allow …]", "[Accept …]", "accept …", "… is also acceptable", "would also work" and similar examiner remarks
- an accepted range (e.g. "accept 2.1 to 2.5 min", "26.5–28.5 cm³") becomes one sensible value inside it; keep ranges that are real chemistry (e.g. heating to 20–30 °C)
Do NOT change the chemistry, numbers, working or meaning otherwise; keep unicode formulae and new lines. If an answer needs no change, return it unchanged. Return one answer per id.`,
  { label: `tidy:${name}`, phase: 'Tidy', model: 'haiku', schema: OUT })))
const answers = Object.fromEntries(out.filter(Boolean).flatMap(r => r.answers).map(a => [a.id, a.model]))
log(`${Object.keys(answers).length} answers tidied; ${out.filter(r => !r).length} agents failed`)
return { answers }
