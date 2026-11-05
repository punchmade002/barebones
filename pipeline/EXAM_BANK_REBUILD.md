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
