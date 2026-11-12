# Exam bank rebuild — agreed spec (2026-11-02)

Replaces the OCR-text exam bank, one subject at a time. Biology goes first, then the rest of
the subjects follow the same process.

## Decisions

| Topic | Decision |
|---|---|
| Order | Biology first. Pilot on the 2025 Higher (Sections A+B answerbook + Section C) and 2025 Ordinary papers, review the result, then scale up. |
| Cutover | Each subject's old bank stays live until its new bank passes validation, then both are swapped in one step. |
| Years | Every available paper, with questions set before the current syllabus tagged `legacy`. All Biology papers (2015–2025) are legacy, because the 2025 spec is first examined in June 2027. |
| Rescan | An agent reads the page images. The PDF text layer is used only to cross-check spelling and numbers. |
| Off-spec parts | Tagged `offSpec` with no generated answer, and hidden by default in the app. Checked against `course-outlines/<subject>.md` and the spec. |
| Answer source | The app's notes for the subject plus the official syllabus spec, and nothing else. A scheme point the notes don't cover is logged as a notes gap. |
| Answer style | Concise and scheme-complete: every scoring point the scheme needs for full marks, and nothing beyond that. |
| Old answers | Kept only if the old answer actually answers the newly scanned part *and* earns full marks against the scheme. |
| Write/check | A writer agent and a checker agent work on each part. After 3 rounds without agreement, the part goes into a review list for the user and is left out of the bank. |
| Type tags | Minimal set: `short-answer`, `long-answer`, `calculation`, `diagram`, `experiment` (more than one allowed). |
| Question display | **Students see the original paper, never a transcription.** Each question is cropped straight from the PDF, with every part, figure, table and answer box exactly as printed, so students read the data off the paper the way they will in the exam. The crops are `exam-images/<subject>/<year>/<level>-q<N>-<k>.webp`, made by `pipeline/rebuild/crops.py`. Transcribed question text is for internal use by the agents only. It stays in `~/barebones/pipeline/_data/rebuild/` (gitignored) and is never shipped in app JS. |
| Diagrams | Figures appear inside the question crop. Each part gets a `diagramRelation` tag: `refers-to-figure`, `label-the-figure`, `draw-a-diagram` or `none`. |

## Record shape (additions to the current schema)

Question: `level` (`higher`/`ordinary`), `paper` (e.g. `A+B`, `C`), `questionNumber`, `legacy`,
`images[]` (the question crops). Parts have **no `question` text** in the shipped file.
Part: `type[]`, `diagramRelation`, `offSpec`, `schemePoints[]` (full-marks scoring points taken
from the scheme), `answerStatus` (`kept` / `written` / `flagged`), `notesRefs[]` (the notes
sections the answer draws on).

## Stages per subject

1. **Scan.** For each paper, read the pages and record questions, parts, labels, marks and
   figure boxes, then crop the figures.
2. **Tag.** Add year, level, paper, question number, marks, type, diagram relation, chapter,
   on-spec/off-spec and legacy.
3. **Scheme.** For each part, pull the scoring points that earn full marks from the marking
   scheme.
4. **Reuse.** Match old answers by year, level, question number and label. Keep one only if it
   answers this part and meets every scheme point.
5. **Write → check.** Write answers for the remaining on-spec parts from the notes and spec
   only, have them checked, and stop after at most 3 rounds.
6. **Assemble.** Build `<subject>-exam-questions.js`, validate it, and swap it in to replace
   the old entries.

## Running it (as done for Biology, Nov 2026)

1. `python3 pipeline/rebuild/crops.py <subject> <paper> ...` crops every question. Crops that are
   wrong get fixed in `<DATA>/<subject>/crop-overrides.json`.
2. Run a Haiku workflow for **scan** (transcribe and tag, from the crop PNG and the text layer)
   and **scheme** (marks and points per part, read from the scheme text). Keep the prompts
   short, with no repo exploration.
3. `python3 pipeline/rebuild/state.py <subject> <journals>` packs each question into
   `<DATA>/<subject>/state/<key>.json`.
4. Run a Sonnet workflow for **write → check** (at most 3 rounds). Each agent reads only its
   state file and the notes files it needs.
5. `python3 pipeline/rebuild/assemble.py <subject> <all journals>` builds
   `<subject>-exam-questions.js` and the review list in `pipeline/_data/rebuild-review/`.

A workflow can run at most 1,000 agents, and cached replays count toward that. Split large
subjects into several runs instead of resuming a big one.

## Cheap fill for any subject (as done for PE, Nov 2026)

The Chemistry recipe, parameterised by subject. Answers come from the marking scheme (no audited
old answers existed for PE). One workflow at a time.

1. `crops.py <subject> <papers>` then `prep_inputs.py <subject>`. PE needed a "Question N" anchor
   and its Section B case-study pages attached to Q13 (both in `crops.py`).
2. One Haiku agent per paper section transcribes, tags and extracts scheme points in one pass
   (PE: 30 agents), converted to a journal for `state.py <subject>`. Check that every label is
   printed on the paper: one PE batch invented "(a)(i)/(ii)" splits, merged back by hand.
3. `fill_packages.py <subject> [--split]` sorts by paper and cuts short-answer packages (10
   questions, at most 50 parts and 50 KB) and long-answer packages (5 questions). The long rule
   is per subject in `is_long()`: for PE, 10+ marks, or 8-9 marks tagged long-answer.
4. `fill_workflow.js`: Haiku writes short answers, Sonnet answers figure parts and checks a
   fixed 5-package sample, then every package if the sample has any error.
   `fill_collect.py <subject> <output> short` remaps mangled ids.
5. `figcheck_batches.py` + `figcheck_workflow.js`: Sonnet checks every Haiku figure answer
   against the crops (fixes go to `fill/figcheck-fixes.json`).
6. `long_workflow.js`: Sonnet writes long answers, a second Sonnet checks every one, one fix
   round, anything still failing is flagged (`fill_collect.py ... long`).
7. `tidy_scan.py <subject> [--batch]` + `tidy_workflow.js` for examiner notation; read the hits
   first, since words like "accepted" and "awarded" are often plain prose.
8. `bank_assemble.py <subject>` layers fill, long, figure fixes, tidy and `fill/manual.json`
   (edits from the final read). Past-paper answers render through `formatModelAnswer`: a line
   starting "Label:" becomes a subheading, and `**bold**` would show literally, so none is used.

## History scan (Nov 2026)

Later Modern paper only (the app has no Early Modern chapters), 2006–2026, 42 papers. The papers
are regular, so most of the scan is local and only the documents-based question uses agents.

1. `crops.py history <year>-<level> ...` anchors on "SECTION 1: DOCUMENTS-BASED QUESTION" and the
   topic headers: q1 = DBQ, q2–q7 = Ireland topics 1–6, q8–q13 = Europe topics 1–6. The topic
   number comes from the printed title (2010 OL misprints one). The DBQ's own topic is not set
   again, so a paper has 12 crops, except that 2023–26 OL add an "Alternative Instructions" Part A
   in the DBQ topic's slot (`alternative: true`). Page-15 pictures ("Picture X on page 15",
   2006/2013/2014 OL) are attached in `crop-overrides.json`.
2. `prep_inputs.py history` keeps only the Later Modern block of each scheme (it always comes first).
3. `hist_scan_journal.py <out>` parses the topic blocks locally: HL essays 1–4 (100 marks, scheme
   = CM 60 + OE 40 plus any "TWO elements" note); OL A1–A5 (scheme answers, 6 marks; 2006–10
   sometimes set four), B1–B4 (CM 20 + OE 10) and C1–C4 (CM 30 + OE 10), all marked by Core
   Statements of 5 marks each.
4. A Haiku workflow (11 agents, 4 DBQs each) transcribes the DBQ parts and scheme points from
   `scan/dbq/<key>.paper.txt` + `.scheme.txt`; `hist_dbq_journal.py` converts it (context = the
   documents' text).
5. `state.py history scan/topics.jsonl scan/dbq.jsonl` gives 508 questions and 4,343 parts.

### History fill (Nov 2026)

Short parts: fill_workflow.js with notes packages (nNN, one chapter each) for Ordinary B/C and DBQ Q4, then a full Sonnet check after the sample failed. Long parts (Higher essays, Higher DBQ Q4), 2016–2026 only: hist_long_packages.py regroups them 3 per package by chapter; hist_long_workflow.js writes, checks every answer and gives one fix round. Checkers get script-measured word counts, because Sonnet's own estimates ran 100–300 words high and failed good essays. The 2006–2015 long parts ship flagged with no answer.
