You grade Leaving Cert maths skills by difficulty. Do not explore the repo; read only the file named here. BATCH is in your prompt (P1 or P2).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/difficulty/in/BATCH.json: a list of chapters, each with its skills. A skill turns an input into an output (`io`, `example`). `level` is JC (assumed from Junior Cycle), OL (Ordinary and Higher) or HL (Higher only). `needs` lists its prerequisite skills. `exam` is evidence from 2015–2025 papers: how many exam parts use it (`examParts`, `asMainSkill`), the share on Higher papers (`shareHigher`), and the usual part letter where it is the main skill (`typicalPart`; a is early and easy, c/d is late and hard). No exam evidence just means it rarely comes up.

For every skill decide a **grade**, judged across the whole course and not relative to its chapter:
- **Beginner**: one routine move, or a rule or formula applied directly. A student who has done the prerequisites can do it after one worked example. Most JC skills and simple OL skills.
- **Intermediate**: several steps, or choosing and combining 2–3 skills, in familiar exam form. Typical OL (b)/(c) and HL (a)/(b) parts.
- **Advanced**: long chains, proofs and derivations, unknowns in awkward places, or unfamiliar contexts. Typical late HL parts. Most HL-only skills that build on other HL skills.

Then **rank** the skills in each chapter from least to most difficult for a student meeting them in this course. Rules:
- A skill always comes after any of its `needs` in the same chapter.
- A skill's grade is never easier than any of its `needs`' grades (including needs in other chapters in this file).
- Grades go up (or stay level) along the chapter's order: no Advanced before a Beginner in the same chapter.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/difficulty/out/BATCH.json: the same chapters in the same order, each as
`{"chapter": "<id>", "skills": [{"id": "<skill id>", "grade": "Beginner"|"Intermediate"|"Advanced", "why": "<under 12 words>"}, ...]}`
with the skills listed in your ranked order (easiest first). Every input skill must appear exactly once, in its own chapter. Valid JSON only.

Reply with just "graded N skills".
