export const meta = {
  name: 'chem-figcheck',
  description: 'Sonnet verifies figure-dependent chemistry answers against the printed question crops (20 questions per agent) and fixes wrong ones',
  phases: [{ title: 'Verify', detail: 'one Sonnet agent per 20 questions, reading only their crops', model: 'sonnet' }],
}
// args: { dir, crops, names: ['f00', ...] }   (batches built locally: each item = scanned part + Haiku answer)
const CHECK = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['id', 'fullMarks', 'issue', 'fixedModel'], properties: { id: { type: 'string' }, fullMarks: { type: 'boolean' },
    issue: { type: 'string' }, fixedModel: { type: 'string', description: 'if fullMarks is false: the corrected full-marks answer; else empty' } } } } } }
const out = await parallel(args.names.map(name => () => agent(
`You are a senior examiner checking model answers for Leaving Certificate Chemistry parts that depend on a figure, graph or table.
Read ${args.dir}/${name}.json (one item per line). Each item has: id ("<question>|<part>"); text = the part as transcribed (the figure may be summarised badly or missing); marks; scheme = official marking-scheme points; rule; figure; hint; answer = the model answer to check.
For each question, read its crop image(s) ${args.crops}/<question>-1.png (then -2.png etc. if they exist) to see the printed figure/table. Read nothing else.
For each item decide fullMarks: does the answer earn FULL marks for this exact part, judged against what the printed figure/table actually shows and the scheme (right values read from graphs/tables, right labels, every required point, calculations correct with units)? Be strict but fair.
If fullMarks=false: issue says what is wrong, fixedModel is a corrected full-marks answer (concise, student-facing, unicode formulae, points on new lines, no examiner notation such as "(3)", "//" or "accept", give a single value rather than the scheme's accepted range). Return one result per item.`,
  { label: `verify:${name}`, phase: 'Verify', model: 'sonnet', schema: CHECK })))
const results = out.filter(Boolean).flatMap(r => r.results)
log(`${results.length} checked, ${results.filter(r => !r.fullMarks).length} fixed, ${out.filter(r => !r).length} agents failed`)
return { results }
