export const meta = {
  name: 'bank-tidy',
  description: 'Haiku strips examiner notation from flagged model answers (presentation only, content unchanged)',
  phases: [{ title: 'Tidy', detail: 'one Haiku agent per batch of flagged answers', model: 'haiku' }],
}
// args: { subject: 'Physical Education', dir, names: ['t00', ...] }   (tidy_scan.py --batch)
const OUT = { type: 'object', required: ['answers'], properties: { answers: { type: 'array', items: { type: 'object',
  required: ['id', 'model'], properties: { id: { type: 'string' }, model: { type: 'string' } } } } } }
const out = await parallel(args.names.map(name => () => agent(
`Rewrite Leaving Certificate ${args.subject} model answers so they read like a student's full-marks answer, not a marking scheme. Read ${args.dir}/${name}.json (one item per line: id, answer, flags = what was detected) and nothing else.
Fix only the presentation:
- remove mark tallies such as "(3)", "(6 marks)" (keep genuine numbering)
- "a // b // c" or "a / b / c" listing alternatives: keep the single best alternative (or as many as the question needs if they are separate required points)
- remove "[Allow …]", "[Accept …]", "accept …", "… is also acceptable", "would also work" and similar examiner remarks, and words like candidate, award, scheme
- an accepted range becomes one sensible value inside it; keep ranges that are real content (e.g. a heart-rate zone of 120–150 bpm)
- remove markdown: "**" and leading bullet symbols ("-", "•", "*"); keep one point per line
Do NOT change the content, numbers or meaning otherwise; keep new lines and any "Label:" at the start of a line. If an answer needs no change, return it unchanged. Return one answer per id.`,
  { label: `tidy:${name}`, phase: 'Tidy', model: 'haiku', schema: OUT })))
const answers = Object.fromEntries(out.filter(Boolean).flatMap(r => r.answers).map(a => [a.id, a.model]))
log(`${Object.keys(answers).length} answers tidied; ${out.filter(r => !r).length} agents failed`)
return { answers }
