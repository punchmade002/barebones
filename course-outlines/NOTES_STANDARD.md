# Notes standard — instructions for the content model

This standard applies to every subject. Read it together with the subsection's information
package (`course-outlines/packages/<subject>/<loId>.md`, written by a higher model; see
`packages/README.md`). The package says **what** to cover and which facts and examples to use;
this file says **how** to write it. Where no package exists yet, use the subject's outline (e.g.
`course-outlines/geography.md`) for scope, but a package must be written before notes ship.

## The goal

Notes that read like a good teacher's handout: concise, but **taught**, not listed. A student
reading a block for the first time should understand every point in it, see why it is true,
and know how the exam will test it. The notes must still contain **everything that could be
examined**.

The test for every point: **could a student who has never studied this topic understand it
with only the block's heading and lead to go on?** If not, the point needs more context.

## Rules

Rules 1–6 are about how notes read. Rules 7–11 are about what they contain. Where a package
says "use the term without redefining it", "one phrase only" or "belongs to <other
subsection>", it is fencing scope: don't *teach* that topic here, but rules 2 and 3 still apply.
A short gloss of a term is not teaching the topic.

1. **Every block opens with a lead (`b`).** One to three sentences, in plain prose, that say what
   the block is about and why it matters, or how it follows from the block before. The lead
   is the "story" the bullets hang on. Bad: no lead, straight into bullets. Good: "Plants
   can't use glucose for everything. They turn it into three other carbohydrates, each built
   for a different job."
2. **Each point stands on its own.** If a point uses a technical term that this subsection
   hasn't already explained, gloss it in a few words in brackets or a clause: "the stroma
   (the fluid that fills the chloroplast)". Never rely on another subsection to explain a word
   the student needs to understand this point. A gloss is not repetition.
3. **Give the reason with the fact.** When a fact has a cause, purpose or consequence, put it
   in the same point with "because", "so", "which means" or "this is why". Aim for at least a
   third of points to explain why or give an example. Bad: "Starch is insoluble." Good:
   "Starch is insoluble, so it can be stored in large amounts without drawing water into the
   cell by osmosis."
4. **One idea per bullet.** An idea is a fact plus its reason or example, not a bare fact.
   Most bullets are 15–40 words; split anything over 50. Keep stages of a process as numbered
   bullets ("1. …", "2. …") in order.
5. **Write like a teacher, not a database.** Full sentences. Plain words before technical ones
   ("splits water, a step called photolysis", not "photolysis of water occurs"). Signposts are
   welcome where they help the reader follow: "first", "this is why", "in other words",
   "remember that", "in short". One everyday analogy per block at most, and only where a
   concept is abstract (e.g. ATP as a rechargeable battery); it must be accurate.
6. **Coach for the exam with `tip`.** Give a block a `tip` whenever the package has a trap or
   exam topic that fits it (usually more than half the blocks): one or two sentences, written to
   the student ("you"), saying what examiners ask about this block and how to get the marks,
   or the mistake students make. Take tips only from the package's "Traps" and "What exams
   ask" sections, and the marking schemes in `<subject>-exam-questions.js`. Never invent mark
   allocations, frequencies ("comes up every year") or examiner quotes. Good: "If asked where
   the oxygen comes from, say water, not carbon dioxide." Skip the tip rather than write a vague one ("learn this well").
7. **Cover every syllabus point in the subsection.** Work through the package's "Must cover"
   list item by item. Every item gets its own block or bullet. If a past exam question tagged
   to the chapter asks about something, the notes must contain the facts needed to answer it.
8. **Teach each fact fully once.** Don't re-teach a fact in a second block. A later block may
   remind the reader in a few words ("ATP, the energy carrier made in stage 1, …"), and
   should when it helps the point stand alone (rule 2).
9. **Cross-references point to more depth, never replace an explanation.** At most one per
   block, phrased as "There is more on this in <subsection name>." The point must make sense
   without it. Never write "described in the next block" or "explained in <X>" in place of
   saying the thing.
10. **No padding or meta-text.** Every sentence teaches a fact, a reason, an example or an exam
    point. Banned: talk about the notes themselves ("This block explains…", "As described
    above"), generic urgency ("This topic is frequently examined"), and pasted templates. The
    build rejects the phrases in `BANNED_PHRASES` in `scripts/build_notes.py`.
11. **Never paste past-paper text.** Don't copy question wording or marking-scheme answers into
    the notes. Teach the content the question needs; a `tip` may say what a question asks for
    in your own words.
12. **Examples are specific, real and from the package.** Use only the named places, dates and
   figures in the package's "Checked facts" table; never add examples from memory. Name the place (e.g. "Powerscourt Waterfall, River
   Dargle, Co. Wicklow"), not "a waterfall in Ireland". Use the syllabus's own settings where it
   gives them. Never invent statistics. If unsure of a figure, leave it out.
13. **Accurate before complete.** If you aren't confident a fact is correct, omit it rather than
   guess. Copy every equation and formula character for character from the package or the
   old notes; never retype, shorten or rebalance one. Where the same equation appears in two
   forms, use the form the earlier subsection uses.
14. **Include the assumed knowledge.** Syllabus documents list outcomes, not the basics those
   outcomes rest on, but exam questions take the basics for granted and every textbook teaches
   them. Teach whatever a student needs in order to meet each outcome, even when the syllabus
   doesn't name it, e.g. the active site and activation energy for "explain how enzymes
   function", or the named heart chambers, valves and major vessels for "relate the structures
   of the heart to their functions". The package lists these items as "assumed" in its
   must-cover list. Keep them to what the outcome needs: assumed knowledge is not licence to
   add whole topics the syllabus has dropped.

## Output format

Write each subsection as one JSON file at `content/<subject>/<loId>.json`, where `loId` is the
subsection's id in `data.js` (for geography: `<chapter-id>-s<n>`, e.g. `geo-rivers-s1`, in the
same order as the outline's numbered subsections). The app shows `h` as the heading, `b` as a
short lead paragraph, `points` as a bulleted list, and `tip` as an "Exam tip" box under the
list. `b` is required on every block (rule 1); `tip` is optional (rule 6).

Then run `python3 scripts/build_notes.py <subject>`. It rejects files that break the rules
(missing fields, markdown, banned filler, repeated points, wrong ids) and compiles the valid
ones into `<subject>-notes.js`, which the app loads. A chapter switches from the old generated
notes to the new ones as soon as any of its subsections is written, so **write whole chapters
at a time**; the build warns about part-written chapters.

```json
{
  "loId": "geo-rivers-s1",
  "chapterId": "geo-rivers",
  "subsection": "1. Fluvial processes, patterns and associated landforms",
  "syllabusRef": "1.5",
  "notes": [
    { "h": "Heading", "b": "One to three sentence lead.", "points": ["Idea.", "Idea."], "tip": "Exam tip." }
  ],
  "keyTerms": [
    { "term": "Hydraulic action", "definition": "One-sentence definition." }
  ]
}
```

- `notes`: usually 4–10 blocks per subsection (investigations and other long subsections may
  need more), each with 3–8 points. A block with more than 8 points is usually two blocks.
- `keyTerms`: the subsection's essential vocabulary for flashcards, one sentence each. These
  can overlap with the notes, because flashcards are a separate study mode.
- `factCards` (optional): flashcards for what the key terms don't test: case-study facts,
  formation stages, named examples, key figures and the lists examiners ask for. Each is
  `{ "term": "Aswan High Dam: four benefits", "definition": "..." }`. The front is a specific
  cue or short question (it doubles as a test question); the back is one or two sentences.
  Use only facts from the subsection's package. The app shows them after the key terms.
- `questions` (optional): exam-style practice questions for the subsection, each
  `{ "marks": 30, "prompt": "...", "model": "..." }`, with the model answer as plain text.
- No markdown inside strings: no `**`, no headings, no line breaks. The app strips them.

## Block types to use

- **Process:** what drives it, then step-by-step how it works.
- **Landform / feature:** what it is; how it forms, in numbered stages; a named example; what
  to draw in a labelled diagram.
- **Case study:** place and context; specific facts, dates and figures; effects; responses or
  evaluation.
- **Comparison / evaluation:** advantages vs disadvantages, or A vs B, as paired points.
- **Skills:** the method step by step, with a worked example.
- **Structure and function** (sciences): each part, what it does, and how its structure suits
  that job; then what to draw and label.
- **Investigation** (sciences): aim or hypothesis; independent, dependent and controlled
  variables; control; method in numbered steps; measurement and repeats; safety; expected
  results and how they support the conclusion.

## Subject notes: biology

- **Higher Level only.** Where the outline or package marks an item [HL], end that block's
  heading with " (Higher Level only)". Put HL-only material in its own block so Ordinary Level
  students can skip it. Don't mark anything the package doesn't mark.
- **Formulas and symbols** are plain Unicode: CO₂, H₂O, C₆H₁₂O₆, NAD⁺, NADPH, Na⁺, Ca²⁺, R₀.
  Never use `$` (the app reads it as maths markup) or LaTeX.
- **Diagram cues:** every structure the syllabus names (organ, cell, organelle, system) gets
  one "Diagram:" bullet, last in its block: what to draw, then the labels. Keep it under 50
  words; list labels rather than describing the layout in prose.
- **Past papers** in the app are all from the previous syllabus. Packages list only the
  question topics that are still on the specification.

## Subject notes: chemistry

- **Higher Level only.** As for biology: where the package marks an item [HL], put it in its
  own block whose heading ends with " (Higher Level only)". Don't mark anything the package
  doesn't mark. Where an outcome is partly bold, the normal part stays in an unmarked block.
- **Formulas, equations and units** are plain Unicode: H₂SO₄, Na₂CO₃·10H₂O, Fe²⁺, SO₄²⁻, 1s² 2s²
  2p⁶, ⇌, →, ΔH, −log₁₀[H⁺], mol L⁻¹, g mol⁻¹, cm³, 25 °C. Never use `$` or LaTeX. State symbols
  (s), (l), (g), (aq) where they matter. Every equation is balanced.
- **Calculations** are worked step by step, one step per bullet: the relationship used, the
  numbers substituted with units, the answer with units and a sensible number of significant
  figures. Label invented numbers "sample data". Use the package's relative atomic masses.
- **Experiments and investigations** use the "Investigation" block type. Every piece of
  apparatus the method names gets a "Diagram:" bullet saying what to draw and label.
- **Past papers** in the app are from the previous (1999) syllabus. Packages list only the
  question topics that are still on the 2025 specification.

## Subject notes: history

- **Scope** comes from `course-outlines/history.md`: each subsection's Syllabus, Case study, Key
  personalities, Key concepts and Cover lists. Cover every item. Stay inside the topic's dates
  except for brief background the outline names.
- **Order** each block chronologically or as cause → events → results. Give exact dates (day,
  month, year) only when certain; otherwise give the year, or leave the date out.
- **Key personality block:** one per personality the outline assigns to the subsection, headed
  "Key personality: <name>". Its points cover: who they were; what they did, with dates; how they
  shaped events or were shaped by them; participant or witness; how contemporaries saw them; how
  historians judge them now. Where the outline splits a personality across subsections, each
  part covers only its own period.
- **Case study:** at least four blocks: background and causes; the events in order, with dates,
  places, people and numbers; outcomes; significance and differing views. A documents-based
  case study (the outline marks it "DBQ source") needs enough detail to place any document in
  context.
- **Assessment block:** end each subsection with a block headed "Assessment: …" giving the
  judgement material examiners reward: achievements vs limits, success vs failure, or
  contemporary vs later views, as paired points.
- **Quotations:** only short, famous, well-attested phrases (e.g. Bismarck's "blood and iron"),
  attributed to the speaker. Never invent or paraphrase a quotation inside quotation marks.
- **Figures** (casualties, votes, seats, money, emigration numbers): include one only if you are
  sure of it, and say "about" for estimates. If sources disagree, give the range or leave it
  out.
- **keyTerms:** every key concept the outline lists for the subsection, defined as used in the
  topic, plus the subsection's other essential terms (organisations, acts, treaties).
- **factCards:** at least 10 per subsection: one per key personality ("Charles Stewart Parnell:
  three achievements"), the case study's key facts and dates, the causes or results examiners
  list, and named acts and events. The front is a specific cue; the back is one or two
  sentences.
- **Cross-references:** refer to another subsection by its subject ("see the notes on the
  Treaty negotiations"), never by its id.

## Subject notes: home economics

- **Scope** is the subsection's entry in `course-outlines/homeeconomics.md`: every "Syllabus"
  item and every "Also examined" item gets a block or bullet. "Settings" are good default
  examples and practical contexts.
- **Higher Level only.** Where the outline marks an item [HL], put it in its own block whose
  heading ends with " (Higher Level only)". Don't mark anything the outline doesn't mark.
- **Legislation and public bodies:** use only the Acts, regulations and bodies the outline names
  (its Appendix A table gives the June 2027 name for each one the 2001 syllabus names). Never
  write notes on a superseded Act, even where a past-paper marking scheme names it (e.g. the Sale
  of Goods and Supply of Services Act 1980, the Consumer Information Act 1978, the Fire Safety
  (Domestic Furniture) Order 1988, the Family Law Act 1976 barring orders). Give an Act's year
  and what it provides; leave out section numbers you aren't sure of.
- **Figures that change** (tax rates, credits and bands, PRSI and USC rates, welfare payment
  amounts, thresholds, prices, grant amounts, interest rates): explain how they work and leave
  the amounts out. Stable figures are fine: the energy value of protein (17 kJ or 4 kcal per
  gram), carbohydrate (16 kJ or 3.75 kcal per gram), fat (37 kJ or 9 kcal per gram) and alcohol
  (29 kJ or 7 kcal per gram); boiling and freezing points; standard temperatures such as the
  danger zone (5–63 °C) and freezer storage at −18 °C. Give RDA or nutrient amounts only where a
  past-paper marking scheme states them.
- **Chemistry** is plain Unicode: C₆H₁₂O₆, H₂O, CO₂, –COOH, –NH₂, C=C. Never use `$` or LaTeX.
- **Diagram cues:** every structure the syllabus or a past paper asks students to draw (amino
  acid, peptide bond, glucose, triglyceride, the wheat grain, the egg, the digestive system, an
  appliance's working parts, a central heating system, a wiring circuit or plumbing layout) gets
  a "Diagram:" bullet saying what to draw and label.
- **Experiments** (food tests, protein and starch properties, sensory tests) use the
  "Investigation" block type.
- **Irish context:** name the Irish bodies the outline names (FSAI, safefood, CCPC, MABS,
  Citizens Information, SEAI, Bord Bia, Department of Health healthy eating guidelines and Food
  Pyramid) rather than generic ones.
- **Lists examiners ask for** ("four functions of…", "three effects of…") are good fact cards.
- **Past papers** are from this syllabus (2004–2026). Use the marking schemes in
  `home-economics-exam-questions.js` as a fact source for what to teach, but write in your own
  words; never copy question or answer wording.

## Subject notes: business

- **Scope** is the subsection's entry in `course-outlines/business.md`: the NCCA Leaving
  Certificate Business specification, first examined June 2027. Cover every "Syllabus" and
  "Cover" item. Never teach content only the old 1996 syllabus had (ratios, contract law,
  household management, the Applied Business Question; the outline's Appendix A4).
- **Exam source:** the SEC 2025 sample papers, as summarised in the outline's "Exam" lines.
  Every SEC paper from 1999 to 2026 is the old syllabus: a package may use one only as legacy
  practice, and only on a topic this specification also has.
- **No Higher Level only blocks.** The specification marks no outcome Higher Level only, so
  never end a heading with " (Higher Level only)".
- **The 7 Ps** are product/service, pricing, promotion, people, packaging, process and place.
  Never teach "physical evidence" as a P.
- **Glossary terms:** where the specification's Appendix 2 defines a term (the outline lists
  them per chapter), the notes and keyTerms define it consistently with that definition. The
  package quotes it.
- **Cross-cutting themes:** every subsection includes the ethical, sustainability and digital
  angle of its topic wherever the package gives one; the written exam assesses applying them.
- **Real named examples only from the package.** Name Irish firms, agencies, schemes, Acts and
  news stories only from the package's "Checked facts" table. Where it says "No checked example.
  Do not name one.", explain the point without a name or use "a sample business".
- **Figures that change** (tax and grant amounts, interest and inflation rates, the minimum
  wage, thresholds, prices, market shares, staff numbers): explain how they work and leave the
  amounts out, unless the package's "Checked facts" gives the figure with its date.
- **Applied tools** (stakeholder mapping, the power-interest grid, Porter's five forces,
  force-field analysis, cost-benefit analysis, SWOT, design thinking, the business model
  canvas) use the "Skills" block type: what the tool is for, the steps numbered, and a worked
  example from the package or labelled "sample business".
- **Depth for the command words** (identify, outline, explain, analyse, discuss, evaluate; the
  specification's Appendix 1): give enough distinct points on each topic to answer at
  discuss or evaluate depth, three or four developed points, each with its effect on the
  business or its stakeholders.
- **Choices the specification sets** (three government policies for three sectors, one EU
  regulation and one EU directive, a marketing mix for a product and for a service, leadership
  styles): teach more than one option, as the package lists them.
- **Cross-references:** refer to another subsection by its subject ("the notes on consumer
  protection"), never by its id.

## Worked example (biology)

The target standard is `content/biology/bio14-s1.json` (Ordinary and Higher Level) and
`content/biology/bio14-s3.json` (Higher Level only). Read one of them in full before writing.
The same block, before and after:

Before (stated, not taught: no lead, bare facts, the reader is sent elsewhere):

```json
{ "h": "Glucose converted to sucrose, starch and cellulose", "points": [
  "Starch suits storage because it is insoluble, so it does not affect osmosis, and it is compact.",
  "Plants also convert glucose to lipids, such as oils in seeds, and, with nitrates from the soil, to amino acids. Both conversions are explained in Biomolecules and metabolism."
] }
```

After (a lead that sets up the block, the reason spelled out, no hand-off, an exam tip):

```json
{ "h": "What glucose is turned into: sucrose, starch and cellulose",
  "b": "Glucose is a good fuel, but it isn't ideal for moving around the plant, storing or building with. So plants convert it into three other carbohydrates, each suited to one job.",
  "points": [
    "Starch suits storage because it is insoluble, so large amounts can be stored without drawing water into the cell by osmosis, and it is compact.",
    "Plants also use glucose to make lipids, such as the oils in seeds, and, combined with nitrates taken from the soil, amino acids for proteins."
  ],
  "tip": "Exams ask what happens to the glucose a plant makes. Give its use in respiration, then sucrose for transport in the phloem and starch for storage, each with its reason." }
```

## Rewriting existing notes

Most subsections already have notes whose facts were checked against the package. When
rewriting them, keep every fact and change how it is taught:

- Change only `notes`. Leave `keyTerms`, `factCards` and `questions` exactly as they are.
- Every must-cover item in the package must still be there after the rewrite. Don't drop a
  fact to make a block shorter.
- Don't add facts that are in neither the old notes nor the package. A gloss, a reason that
  follows from facts already given, or an everyday analogy is fine.
- **Stay information-dense.** Students use these notes to get top grades. Keep every fact,
  number, named example, list item, qualifier ("usually", "only in", "at least") and technical
  term from the old notes. Never merge two facts into one vaguer statement or swap a specific
  statement for a general one. The rewrite adds leads, glosses, reasons and tips around the
  facts, so it usually comes out 20–50% longer than the old notes, never shorter. Concise means
  no wasted words, not fewer facts.

## Quality checks before finishing a subsection

Go through these one at a time, and fix anything that fails before you finish.

1. Every block has a `b` lead of one to three sentences.
2. Read each bullet with only its block's heading and lead. Does every technical term in it
   have a gloss, or an explanation earlier in this subsection? If not, add a gloss. Watch for
   short everyday-looking words with a special meaning ("fixed", "reduced", "limiting").
   If a bullet says something must happen ("it must regain an electron"), it also says how.
3. At least a third of bullets contain "because", "so", "which means", "this is why", "for
   example", "such as" or another reason or example.
4. No bullet is over 50 words. No block has more than 8 points.
5. No bullet says "explained in", "described in", "covered in" or "see"; at most one "There is
   more on this in …" per block.
6. Every `tip` comes from the package's "Traps" or "What exams ask", and states no marks,
   frequencies or examiner quotes that aren't there.
7. Every must-cover item in the package has a block or bullet, and every "assumed" item has a
   bullet.
8. Higher Level blocks end their heading with " (Higher Level only)".
9. All strings are plain text: no markdown, no line breaks, no `$`.
10. The build passes: `python3 scripts/build_notes.py <subject>`.
