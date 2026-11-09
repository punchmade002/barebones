export const meta = {
  name: 'chemistry-scan-scheme',
  description: 'Haiku: scan (transcribe + tag) each Chemistry question crop and pull its marking-scheme points',
  phases: [
    { title: 'Scan', detail: 'haiku transcribes + tags questions not yet scanned', model: 'haiku' },
    { title: 'Scheme', detail: 'haiku extracts full-marks scheme points per part', model: 'haiku' },
  ],
}

const D = '/Users/gabrielwhelan/barebones/pipeline/_data/rebuild/chemistry'
const OFFSPEC = 'radioactivity and nuclear equations; the mass spectrometer; instrumental analysis (AAS, IR, UV, GC, HPLC, TLC as analysis); the ozone layer and CFCs; the nitrogen cycle; fuels and octane numbers (cracking, reforming, isomerisation, oxygenates, petrol blending); the bomb calorimeter; ethyne preparation from calcium carbide; Tollens\' reagent; transition metals and variable valency; industrial chemistry case studies; metal extraction (blast furnace, aluminium, Downs cell); alloys and anodising; X-ray crystallography and crystal types; water-analysis methods (EDTA hardness titration, Winkler dissolved oxygen, free chlorine by colorimeter, suspended and dissolved solids); stages of sewage treatment'

const SCAN = { type: 'object', properties: {
  cropOk: { type: 'boolean' }, cropIssues: { type: 'string' }, attemptRule: { type: 'string' },
  parts: { type: 'array', items: { type: 'object', properties: {
    label: { type: 'string' }, text: { type: 'string' },
    type: { type: 'array', items: { type: 'string', enum: ['short-answer', 'long-answer', 'calculation', 'diagram', 'experiment'] } },
    diagramRelation: { type: 'string', enum: ['refers-to-figure', 'label-the-figure', 'draw-a-diagram', 'none'] },
    chapterId: { type: 'string' }, loIds: { type: 'array', items: { type: 'string' } },
    offSpec: { type: 'boolean' }, offSpecReason: { type: 'string' },
  }, required: ['label', 'text', 'type', 'diagramRelation', 'chapterId', 'loIds', 'offSpec', 'offSpecReason'] } },
}, required: ['cropOk', 'cropIssues', 'attemptRule', 'parts'] }

const SCHEME = { type: 'object', properties: {
  schemePages: { type: 'array', items: { type: 'integer' } }, questionMarks: { type: 'number' }, note: { type: 'string' },
  parts: { type: 'array', items: { type: 'object', properties: {
    label: { type: 'string' }, marks: { type: 'number' },
    schemePoints: { type: 'array', items: { type: 'string' } }, fullMarksRule: { type: 'string' },
  }, required: ['label', 'marks', 'schemePoints', 'fullMarksRule'] } },
}, required: ['schemePages', 'questionMarks', 'parts', 'note'] }

// args: "2001h1 2001h7 2024o10 ..." (year, h/o, question number)
// a trailing "s" means the scan is already saved in state/<key>.scan.json: only the scheme is needed
function info(code) {
  const hasScan = code.endsWith('s'), c = hasScan ? code.slice(0, -1) : code
  const year = c.slice(0, 4), level = c[4] === 'h' ? 'higher' : 'ordinary', number = Number(c.slice(5))
  const key = `${year}-${level}-q${number}`
  return { key, section: number <= 3 ? 'A' : 'B', hasScan, year, level, number }
}

function scanPrompt(it) {
  return `Transcribe and tag Leaving Cert Chemistry ${it.year} ${it.level} level, Section ${it.section}, question ${it.number}.
Read ONLY: the crop image(s) ${D}/crops-png/${it.key}-1.png (and -2.png, -3.png if they exist), and ${D}/text/${it.key}.txt (text layer: use only to fix spelling/numbers). Do not modify files.
1. cropOk: true if the crop shows the whole question and nothing from another question; otherwise describe the problem in cropIssues.
2. Split into parts at the finest separately answerable level, labels like "(a)", "(b)(ii)", "(c)(iii)2". text = faithful transcription incl. the stem it depends on; describe any figure/table briefly in [brackets].
3. type (short-answer/long-answer/calculation/diagram/experiment), diagramRelation, chapterId (chemN) and loIds: pick from ${D}/notes/INDEX.md (read it once).
4. offSpec = true only if the topic is not on the 2025 Chemistry specification (first examined 2027). Not on the spec: ${OFFSPEC}. Anything else is on-spec. Give a one-line reason.
attemptRule = the paper's instruction like "Answer any two of (a), (b), (c)" or "".`
}

function schemePrompt(it, fresh) {
  const parts = fresh
    ? JSON.stringify(fresh.parts.map(p => p.label))
    : `the "label" values in ${D}/state/${it.key}.scan.json`
  return `From the marking scheme, extract how Leaving Cert Chemistry ${it.year} ${it.level} question ${it.number} (Section ${it.section}) is marked.
Scheme: ${D}/scheme/${it.year}-${it.level}/scheme.txt (pages separated by "===== PAGE n ====="; the question number appears as e.g. "QUESTION 4" or "Question 4"). Grep to find it and read only those pages; open ${D}/scheme/${it.year}-${it.level}/pNN.png if the text is empty or scrambled (some older schemes are scans). If scheme.txt says no scheme was published, give the points a Leaving Cert examiner would require for the marks printed on the paper and say so in note. Do not modify files.
Use exactly these part labels, one entry each: ${parts}.
For each: marks, every creditable point/alternative the scheme accepts (short), and the full-marks rule (e.g. "any 2 x 3 marks"). If marks are only given for a group of parts, split them as the scheme implies and say so in note. questionMarks = the question total.`
}

const items = args.trim().split(/\s+/).map(info)
const results = await pipeline(
  items,
  it => it.hasScan ? { saved: true } : agent(scanPrompt(it), { label: `scan:${it.key}`, phase: 'Scan', schema: SCAN, model: 'haiku', effort: 'low' }),
  (scan, it) => scan
    ? agent(schemePrompt(it, scan.saved ? null : scan), { label: `scheme:${it.key}`, phase: 'Scheme', schema: SCHEME, model: 'haiku' })
    : null,
)
const missing = items.filter((it, i) => !results[i]).map(it => it.key)
return { done: results.filter(Boolean).length, missing }
