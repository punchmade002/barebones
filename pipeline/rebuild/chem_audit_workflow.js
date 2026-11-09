export const meta = {
  name: 'chem-answer-audit',
  description: 'Two Haiku auditors per chapter-group packet check chemistry answers vs the marking scheme; Sonnet rewrites flagged ones; Haiku re-checks',
  phases: [
    { title: 'Audit', detail: 'two independent Haiku auditors per packet (2-3 chapters of one paper)', model: 'haiku' },
    { title: 'Rewrite', detail: 'Sonnet arbitrates flags and rewrites for full marks', model: 'sonnet' },
    { title: 'Check', detail: 'Haiku re-checks every rewrite / keep against the scheme', model: 'haiku' },
  ],
}

const BASE = args.base
const ROOT = '/Users/gabrielwhelan/barebones'
const P = n => `${BASE}/packets/${n}.json`

const GROUPS = [['chem1','chem2'],['chem3','chem4','chem5'],['chem6','chem7','chem8'],['chem9','chem10','chem11'],['chem12','chem14'],['chem15','chem17'],['chem18','chem19','chem20'],['chem21','chem22','chem23'],['chem24','chem25','chem26']]
// args.packets: { "g1-3-2003o_2004h": "289:4,290:10" } -> name, chapters, papers, part keys
const PACKETS = Object.entries(args.packets).map(([name, counts]) => {
  const [g, , paperStr] = name.split('-')
  const papers = paperStr.split('_').map(p => {
    const year = Number(p.slice(0, 4)), level = p[4] === 'h' ? 'higher' : 'ordinary'
    const ref = year === 2001 ? '-REF' : ''
    const scheme = (year === 2001 || (year === 2002 && level === 'ordinary')) ? 'images' : year === 2008 ? 'none' : 'text'
    return { year, level, paper: `${BASE}/text/${year}-${level}-EV-papers${ref}.txt`, scheme,
      schemePath: scheme === 'images' ? `${BASE}/scheme-png/${year}-${level}-EV-scheme${ref}/` : `${BASE}/text/${year}-${level}-EV-scheme${ref}.txt` }
  })
  const keys = counts.split(',').flatMap(c => { const [qi, n] = c.split(':').map(Number); return Array.from({ length: n }, (_, pi) => `${qi}:${pi}`) })
  return { name, chapters: GROUPS[Number(g.slice(1)) - 1].join(', '), papers, keys, parts: keys.length }
})
const desc = pk => pk.papers.map(p => `${p.year} ${p.level}`).join(' + ')
function paperLine(p) {
  const s = p.scheme === 'images' ? `marking scheme is a scanned PDF: read the page images p-*.png in ${p.schemePath} with the Read tool (only the pages covering this packet's questions)`
    : p.scheme === 'none' ? `NO marking scheme exists: judge against correct Leaving Certificate Chemistry and what a full-marks answer for the marks shown needs, and give schemePoints as the points an examiner would require`
    : `marking scheme text: ${p.schemePath} (grep it for the question numbers you need rather than reading all of it)`
  return `- ${p.year} ${p.level}: paper text ${p.paper}; ${s}.`
}
const files = pk => `Packet: ${P(pk.name)} — entries[] each with qi, source, paper ("<year>-<level>"), parts[] with pi, label, question, marks, model.
Papers in this packet:
${pk.papers.map(paperLine).join('\n')}
Do not explore the repo beyond these files.`

const VERDICT = { type: 'object',
  required: ['qi', 'pi', 'verdict', 'questionNumber', 'partLabel', 'questionMatchesPaper', 'schemePoints', 'reason'],
  properties: {
    qi: { type: 'integer' }, pi: { type: 'integer' },
    verdict: { type: 'string', enum: ['correct', 'wrong'] },
    questionNumber: { type: 'string', description: 'question number on the paper, digits only, e.g. "4"' },
    partLabel: { type: 'string', description: 'exact printed part label in brackets, e.g. "(a)(i)", "(c)(B)(iv)", "(e)"' },
    questionMatchesPaper: { type: 'boolean' },
    schemeMarks: { type: ['integer', 'null'] },
    schemePoints: { type: 'array', items: { type: 'string' } },
    reason: { type: 'string', description: 'short; for wrong say exactly what is missing or wrong' } } }
const AUDIT_SCHEMA = { type: 'object', required: ['verdicts'], properties: { verdicts: { type: 'array', items: VERDICT } } }

const REWRITE_SCHEMA = { type: 'object', required: ['items'], properties: { items: { type: 'array', items: { type: 'object',
  required: ['qi', 'pi', 'action', 'model', 'schemePoints', 'questionNumber', 'partLabel', 'note'],
  properties: {
    qi: { type: 'integer' }, pi: { type: 'integer' },
    action: { type: 'string', enum: ['rewrite', 'keep', 'cannot'], description: 'keep = stored answer already earns full marks; cannot = paper/scheme unreadable for this part' },
    model: { type: 'string', description: 'the new full-marks answer (empty for keep/cannot)' },
    question: { type: 'string', description: 'corrected question text ONLY if the stored text is not this part as printed; else empty' },
    schemePoints: { type: 'array', items: { type: 'string' } },
    questionNumber: { type: 'string' }, partLabel: { type: 'string' }, note: { type: 'string' } } } } } }

const CHECK_SCHEMA = { type: 'object', required: ['results'], properties: { results: { type: 'array', items: { type: 'object',
  required: ['qi', 'pi', 'pass', 'issue'],
  properties: { qi: { type: 'integer' }, pi: { type: 'integer' }, pass: { type: 'boolean' }, issue: { type: 'string' } } } } } }

const COMMON = `For EVERY part in the packet return one verdict:
- Find the exact question and part on the paper this answer belongs to: questionNumber (digits) and the printed partLabel in brackets, e.g. "(b)(ii)". questionMatchesPaper = false if the stored question text is not that part's question (wrong part, merged or garbled text, missing data the student needs).
- Find that part in the marking scheme: schemeMarks and the scoring points needed for FULL marks (schemePoints, short).`

const auditPromptA = pk => `You are auditing model answers in a Leaving Certificate Chemistry exam answer bank: ${desc(pk)}, chapters ${pk.chapters}.
${files(pk)}

${COMMON}
- verdict "correct" only if the model answer would earn full marks: it states every required scheme point (or an accepted alternative), any calculation reaches the scheme's answer with working, and nothing in it is chemically wrong. Terse mark-scheme style answers are fine.
- verdict "wrong" if any scheme point is missing, the answer is wrong, incomplete, for a different part or empty, or questionMatchesPaper is false. Be strict: when in doubt, "wrong".
Return all ${pk.parts} verdicts.`

const auditPromptB = pk => `You are a skeptical second examiner checking model answers in a Leaving Certificate Chemistry exam answer bank: ${desc(pk)}, chapters ${pk.chapters}.
${files(pk)}

${COMMON}
- Your job is to REFUTE each answer: look for chemical errors (wrong formula, equation not balanced, wrong colour/observation, wrong units or significant arithmetic), numbers that do not match the scheme, answers that respond to a different part or a different question, lists with fewer items than the question asks for, and extra statements that contradict the scheme.
- verdict "wrong" if you find any such problem or any scheme point is missing; "correct" only if an examiner using this scheme would award full marks. If uncertain, "wrong".
Return all ${pk.parts} verdicts.`

const rewritePrompt = (pk, items, round) => `You are fixing model answers for a Leaving Certificate Chemistry exam answer bank (${desc(pk)}) so each earns FULL marks under the official marking scheme.
${files(pk)}

${round === 1 ? 'Auditors flagged these parts (two independent auditors; their reasons and any disagreement over the question tag are included)' : 'Your previous fix of these parts failed an independent check'}. qi/pi identify the part: the stored question, marks and answer are in the packet at entries[] with that qi, parts[] with that pi.
${JSON.stringify(items)}

For each item:
- Locate the exact part on the paper and in the scheme; give the correct questionNumber (digits) and printed partLabel in brackets.
- If the stored answer already earns full marks and is chemically sound (auditor mistaken), action "keep".
- Otherwise action "rewrite": a concise, student-facing answer that hits EVERY scheme point needed for full marks and nothing irrelevant. Calculations show working and the final answer with units. Correct formulae and equations (unicode sub/superscripts, e.g. H₂SO₄, Cu²⁺). No examiner notation such as "[accept ...]" or "(6 marks)". Separate required points with new lines.
- If the stored question text is not this part as printed, put the correct text (with any data the student needs) in "question".
- "cannot" only if the paper or scheme for that part is genuinely unreadable.
Return one item per input item.`

const checkPrompt = (pk, items) => `You are checking model answers for a Leaving Certificate Chemistry exam bank (${desc(pk)}) against the official marking scheme.
${files(pk)}
The stored question text and marks for each item are in the packet (entries[] with that qi, parts[] with that pi); correctedQuestion, when present, replaces the stored text.
Items: ${JSON.stringify(items)}
For each, find that part in the scheme. pass = true only if the answer would get FULL marks: every required scheme point present (or an accepted alternative), calculations correct, nothing chemically wrong, and it answers that exact part. Otherwise issue = exactly what is missing or wrong. Be strict.`

const key = v => `${v.qi}:${v.pi}`

async function rewriteAndCheck(pk, flagged, round) {
  const rw = await agent(rewritePrompt(pk, flagged, round), { label: `rewrite${round}:${pk.name}`, phase: 'Rewrite', model: 'sonnet', schema: REWRITE_SCHEMA })
  const items = ((rw && rw.items) || []).filter(i => flagged.some(f => key(f) === key(i)))
  const answered = new Set(items.map(key))
  const dropped = flagged.filter(f => !answered.has(key(f))).map(f => ({ qi: f.qi, pi: f.pi }))
  const toCheck = items.filter(i => i.action !== 'cannot').map(i => {
    const o = { qi: i.qi, pi: i.pi, questionNumber: i.questionNumber, partLabel: i.partLabel }
    if (i.action === 'keep') o.answer = '(the stored answer in the packet)'
    else o.answer = i.model
    if (i.question) o.correctedQuestion = i.question
    return o
  })
  let checks = []
  if (toCheck.length) {
    const ck = await agent(checkPrompt(pk, toCheck), { label: `check${round}:${pk.name}`, phase: 'Check', model: 'haiku', schema: CHECK_SCHEMA })
    checks = (ck && ck.results) || []
  }
  // an item the checker did not return counts as failed
  const checked = new Set(checks.map(key))
  toCheck.filter(t => !checked.has(key(t))).forEach(t => checks.push({ qi: t.qi, pi: t.pi, pass: false, issue: 'not checked' }))
  return { items, checks, dropped }
}

const results = await pipeline(PACKETS,
  pk => parallel([
    () => agent(auditPromptA(pk), { label: `auditA:${pk.name}`, phase: 'Audit', model: 'haiku', schema: AUDIT_SCHEMA }),
    () => agent(auditPromptB(pk), { label: `auditB:${pk.name}`, phase: 'Audit', model: 'haiku', schema: AUDIT_SCHEMA }),
  ]),
  async ([a, b], pk) => {
    const keys = pk.keys
    const A = new Map(((a && a.verdicts) || []).map(v => [key(v), v]))
    const B = new Map(((b && b.verdicts) || []).map(v => [key(v), v]))
    const flagged = []
    for (const k of keys) {
      const va = A.get(k), vb = B.get(k)
      const reasons = []
      if (!va) reasons.push('auditor A skipped it'); else if (va.verdict === 'wrong') reasons.push('A: ' + va.reason)
      if (!vb) reasons.push('auditor B skipped it'); else if (vb.verdict === 'wrong') reasons.push('B: ' + vb.reason)
      if (va && vb && (va.questionNumber !== vb.questionNumber || va.partLabel.replace(/\s/g, '') !== vb.partLabel.replace(/\s/g, '')))
        reasons.push(`tag disagreement: A says Q${va.questionNumber}${va.partLabel}, B says Q${vb.questionNumber}${vb.partLabel}`)
      if (reasons.length) {
        const [qi, pi] = k.split(':').map(Number)
        flagged.push({ qi, pi, reasons, schemePoints: (va && va.schemePoints) || (vb && vb.schemePoints) || [] })
      }
    }
    const out = { pk: pk.name, A: [...A.values()], B: [...B.values()], flagged: flagged.map(key), rounds: [] }
    if (!flagged.length) return out
    const r1 = await rewriteAndCheck(pk, flagged, 1)
    out.rounds.push(r1)
    const failed = r1.checks.filter(c => !c.pass).concat(r1.dropped)
    if (failed.length) {
      const again = failed.map(c => {
        const prev = r1.items.find(i => key(i) === key(c)) || {}
        const f = flagged.find(x => key(x) === key(c)) || { qi: c.qi, pi: c.pi }
        return { ...f, previousAction: prev.action, previousAnswer: prev.model, checkerIssue: c.issue || 'no answer returned' }
      })
      out.rounds.push(await rewriteAndCheck(pk, again, 2))
    }
    return out
  })

const ok = results.filter(Boolean)
const failedPackets = PACKETS.filter(p => !ok.find(r => r.pk === p.name)).map(p => p.name)
log(`${ok.length}/${PACKETS.length} packets finished${failedPackets.length ? '; failed: ' + failedPackets.join(', ') : ''}`)
return { results: ok, failedPackets }
