# Prompt: fill and check a subject's exam answer bank cheaply

Paste everything below the line into a new Claude Code session in `~/barebones`, replacing
`<SUBJECT>` (e.g. `geography`). It reproduces the Chemistry run of Nov 2026: 5,279 parts,
every part answered and scheme-checked for roughly 60 agents, almost all Haiku.

**Quality it achieved:**
- The Sonnet sample found 0 content errors in 287 Haiku answers.
- In the riskiest category (parts that use a figure), Sonnet checked 354 parts against the printed crops. It found 3 content errors (about 1%) and 15 formatting slips.

Long-answer questions are deliberately carved out (step 3), because those numbers don't carry over to them.

---

You are filling the `<SUBJECT>` exam answer bank of the barebones study app with full-marks model answers, cheaply. Cost is the top constraint after correctness:

- Never use Opus subagents.
- Never run more than one workflow at a time.
- Ask me before any step that would spawn more than about 15 agents.

Use the Workflow tool for fan-outs, and Haiku for writing. Use Sonnet only for checking, and for parts that need an image.

## 0. Read first, then ask me before spending anything
- `pipeline/EXAM_BANK_REBUILD.md`: the bank spec, built from the Biology blueprint. Read it for the record shape, the off-spec, legacy, type and diagramRelation tags, and how question crops ship in place of text.
- The Chemistry implementation, to copy and generalise. These scripts hardcode `chemistry`, so parameterise them by subject; don't fork them blindly:
  - `pipeline/rebuild/chem_fill_packages.py`: builds the packages.
  - `pipeline/rebuild/chem_fill_workflow.js`: the Haiku writers, Sonnet for figure parts, and the Sonnet sample check.
  - `pipeline/rebuild/chem_figcheck_workflow.js`: Sonnet checks figure parts against the crops.
  - `pipeline/rebuild/chem_tidy_workflow.js`: Haiku strips examiner notation.
  - `pipeline/rebuild/chem_assemble.py`: builds `<subject>-exam-questions.js`, with override layers.
  - `tests/chemistry-exam-bank-integrity.test.cjs`.
- Take stock of what already exists for `<SUBJECT>` under `pipeline/_data/rebuild/<SUBJECT>/`:
  - `crops.json` and `exam-images/`;
  - `state/<key>.json`: scanned parts with text, marks, schemePoints, fullMarksRule, type, diagramRelation, loIds and offSpec;
  - `old-answers/`: audited answers.
  If there are no crops or scans, the subject needs the earlier stages first (crops.py, then the Haiku scan/scheme workflow, then state.py, as in the spec). Stop and tell me what's missing.
- Report the counts: questions, parts, on-spec parts with an audited old answer under the exact same label, parts needing an answer, off-spec parts, and long-answer parts (step 3). Then ask me what's unclear before launching anything. For example: should off-spec parts get answers? (Chemistry: yes, kept with the offSpec tag.)

## 1. Split off long-answer parts
A long-answer part is one whose full-marks answer runs to more than a paragraph. Examples:
- essays, and "discuss" or "evaluate" questions;
- History document and essay questions;
- Geography long questions marked by significant relevant points (SRPs);
- English comprehension and composition;
- any part where the scheme expects about 6 or more developed points, or that is worth a lot of marks for its subject.

Decide this per subject from the `type` tags, the marks and the scheme points. Show me the rule and the counts, plus 5 examples on each side of the line, before going on.

Long-answer parts never go through step 2. They get their own pipeline in step 3.

## 2. Short-answer pipeline (the Chemistry recipe)
1. **Reuse audited answers.** For on-spec parts, use the audited old answer when its label matches exactly. Everything else (gaps, plus off-spec parts if I said yes) is a target.
2. **Package locally with Python, not agents.**
   - Sort the target questions by paper (year, level, number) and cut them into packages of 10 questions, so a package spans one or two papers.
   - Also cap each package at about 50 parts and about 50 KB. A 102-part Chemistry package made Haiku drop 25 answers.
   - Each item carries:
     - the id `<key>|<label>`, the scanned text, marks, scheme points and rule;
     - the figure tag, if it has one;
     - a hint: an audited old answer whose label contains, or is contained by, this part's label, capped at 500 characters.
   - Write each package as a JSON array with one item per line. Read truncates lines over 2,000 characters, so keep every line under that.
3. **Haiku writers.** One Haiku agent per package. It reads its one file and nothing else, and returns `{id, model, needsFigure}`. Tell it to write the answer in the student's own words:
   - cover every scheme point;
   - give one alternative, not "X or Y is also acceptable";
   - give a single value, never the scheme's accepted range;
   - no "(3)", "//", "[accept …]" or "allow";
   - show working for calculations.

   Haiku broke all of these in Chemistry even when told, so step 2.6 exists to catch them.
4. **Figure parts.** Parts Haiku marks `needsFigure` go to Sonnet with only those questions' crop PNGs, 8 questions per agent.
5. **Sonnet sample check.** Pick 5 packages at random (with a fixed seed, in Python). Each Sonnet agent checks 2 packages: it reads the package files and gets the answers inline, and returns `{id, fullMarks, issue, fixedModel}`. Sonnet fixes wrong answers in place.
   - If the sample has 0 errors, the other packages pass.
   - If it finds any error, Sonnet checks every remaining package, 2 per agent.
6. **Figure verification.** Every Haiku answer whose part refers to or labels a figure gets checked by Sonnet against the crop images, 20 questions per agent. These have the highest real error rate: a transcription can drop a value or a label.
7. **Notation scan and tidy.** Scan every shipped answer, old and new, with a regex for:
   - mark tallies like `(3)`;
   - `//`;
   - accept, allow, "also acceptable", "would also work";
   - scheme ranges;
   - `[Allow …]`;
   - the words candidate, award and scheme.

   Show me the counts. Then a Haiku tidy pass on only the flagged answers, about 45 per agent, changes the presentation only. Afterwards, check locally that every number in the old answer still appears in the new one, except where a range was collapsed to one value, and list any differences.
8. **Assemble and test.** Apply the layers in order: audited answers, then fill answers, then Sonnet fixes, then the tidy. Set `model_source` to `audited`, `haiku`, `sonnet-figure` or `sonnet-fix`. Each shipped part has to cite `notesRefs` (its loIds, or the question's chapter). Then:
   - adapt the subject's integrity test from the Chemistry one;
   - bump the `?v=` for that bank in `exam-packs.js`;
   - run `deno test -A tests/` (node isn't installed).

## 3. Long-answer pipeline (separate)
Long answers carry most of the marks and leave the most room for error, so the sampling shortcut doesn't apply. Propose a plan with agent counts and wait for my OK. The default:
- Sonnet writes, 3–5 questions per agent, with the scheme's SRPs or marking criteria inline.
- A second Sonnet agent checks every long answer against the scheme. It is not sampled.
- At most one fix round. Anything still failing is flagged for my review, not shipped.
- Answers are structured as the scheme rewards them (one point per paragraph or line, keywords bolded), at the length a student could write in the exam time.
- If the old bank already has a long answer, it is a hint only: it is still checked.

## 4. Quality bar and reporting
- **Bar:**
  - 0 content errors in the Sonnet sample, for short answers;
  - 2% or less content errors in the figure check;
  - no examiner notation left;
  - all tests passing.

  If the sample fails, check everything rather than shipping.
- **Your own check:** read 8–10 random unchecked Haiku answers next to their scheme points, especially calculations and graph readings, and report what you find.
- **Final report:**
  - counts by source and status;
  - what was checked and what passed unchecked on the strength of the sample;
  - the real errors found, quoted;
  - agent count and subagent tokens;
  - what is left.

  Do not commit or push unless I ask.

## Lessons from Chemistry
- **Running several heavy workflows at once hit the 5-hour usage limit.** Run one workflow at a time.
- **Haiku sometimes mangles ids** (for example it dropped the year prefix). Remap them locally, and diff the returned ids against the package ids every time.
- **Agents get CLAUDE.md automatically.** Keep prompts to what the stage needs.
- **Package size matters more than package count.** Ten questions of a long paper can be 100+ parts.
