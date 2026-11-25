# Crunch Mode — spec (decisions agreed 2026-11-23)

The student tells a subject what result they need (e.g. 80%). Crunch Mode hides
the lowest-value note points until what's left just covers that target.
This is the site's USP, so every number has to be explainable.

## Decided

**Unit: the individual note point.** The finer the net, the more the course can
be compressed. Each note item is scored, linked and cut on its own. An item is a
bullet point or a block's explanation paragraph, with id
`<subsection>.<block>.<point>` and `b` for the paragraph (e.g. `bio13-s3.2.b`,
`bio13-s3.2.4`). Exam tips follow their block and are not items. Biology has 35
chapters → 161 subsections (plus 2 acronym lists, which are not items) →
1,646 blocks → **10,583 items** (8,937 points + 1,646 paragraphs). Ids are
positional, so each item's text hash is stored; a changed note makes its ratings
and links stale and they are redone.

**Setup.** Per subject, from the subject page: target %, expected coursework %,
and LC mode or Test mode.

**AAC (built 2026-11-24).** Each map has an "Expected AAC result" box. The weights
are in `scripts/crunch_map.py` `AAC`, taken from `<subject>-exam-info.js`: Biology
in Practice Investigation 40%, Geographical Investigation 20%. The grade bar is the
overall grade. The cut targets the written paper (target − weight × AAC) ÷
(1 − weight), and the safety margin applies to the written paper. If the AAC alone
reaches the grade, everything is hidden. If the written paper would need over 100%,
everything is kept and the page says it's out of reach.

**Map view (2026-11-24).** The x-axis is the overall grade at which a point is
first needed (its calibrated written level, put through the AAC). A line counts
the points in each 5% grade bracket. The vertical bar is the target grade: points
to its left are kept, points to its right are hidden. Clicking a bracket lists its
points. Under the chart, a Chapters panel shows each chapter's kept and total
counts and how much it is cut at the target. Clicking a chapter filters the
chart, stats and lists to that chapter. The Biology line is very lopsided: with
an 80% AAC, most points sit at 85–90% overall, because they only matter for a
near-perfect written paper.

**Target maths.**
- Coursework is subtracted first. For example, Biology 80% overall with 95%
  expected on the 40% investigation: written paper needs (80 − 0.4×95)/0.6 = 70%.
- Safety margin (since 2026-11-24, replacing a flat +5%): keep enough that the written target would have been
  reached in about 4 past years in 5. See "Year-by-year backtest" below.
- Assume the student gets full marks on every item they keep.

**Pure scoring, no absolutes.** No item is ever force-kept. A 40% target can cut
~70% of the course. Foundations survive only because they score high.

**Score per item** (LC mode) = exam value + dependency value.
- *Exam value*: expected marks from past papers. **Formula deferred.** Build
  dependencies first. Exam parts are tagged to subsections, not points, so a
  subsection's exam value has to be shared out among its points.
- *Dependency value*: marks-weighted downstream. Everything that depends on the
  item, directly or through a chain, passes some of its exam value back to it.
  Essential links pass more than helpful ones, and the share fades with each hop
  (PageRank-like).
- *Gap discount*: if a kept item's prerequisite is cut, its expected marks are
  discounted (more for essential links than for helpful ones). The cut is greedy
  and recomputes after each removal, so it naturally prefers coherent bundles.

**Loops are bundles** (decided 2026-11-24). When points need each other (A needs B
and B needs A, or a longer loop), they are kept or cut together and share one
value: their combined score ÷ their combined cost. Links inside a bundle pass no
value and cause no gap discount. No link is dropped.

**Learning cost.** A simple item costs 1. A long or complicated item costs 2, the
same as two simple ones. The AI judges both "long" and "complicated" in one
rating per item (no word-count rule). The cut ranks items by score ÷ cost. When
two items are worth the same, the costlier one goes first, so the student keeps
the most marks for the least studying.

**Dependencies.** Within one subject only. Two kinds, stored separately:
- *Prerequisite*: item A uses an idea that item B teaches. Strength `essential`
  or `helpful`, with a short reason and a confidence. Drafted per item by AI;
  Gabriel spot-checks a sample plus every low-confidence link.
  The subsection graph (`content/crunch/<subject>-prerequisites.json`) is the
  coarse net: an item may link only to items in its own subsection or in a
  subsection its subsection needs. That keeps each agent's input small.
- *Co-tested*: subsections marked together in the same past-paper part.
  Calculated by a script from `*-exam-questions.js` `notesRefs`, with no
  authoring.

**Test mode** (exam likelihood off, for mocks and class tests): the student ticks
the chapters their test covers. Everything else is hidden. No % target.

**What hides.** Cut items in notes. Each page ends with "x points hidden in
Crunch Mode". Tests, quizzes and the exam bank are *not* filtered. Once scores
exist, tests are *biased* towards the highest-scoring items.

**Progress.** The crunch progress bar shows by default. Detailed views can switch
to full-course progress.

**Pilot.** Biology prerequisites first (Gabriel knows it best). Chemistry is the
first full LC-mode test once exam value exists (25 years of tagged papers).

## Open questions
- Exam value formula (frequency vs marks, recency weighting, question choice such
  as "answer 5 of 6"), and how a subsection's value is shared among its points.
  Biology's bank is the old course (`legacy: true`), so its values will be weaker.
- Flashcards and key terms are tied to subsections, not points. When does a
  flashcard hide? Do they add learning cost?
- The exact numbers: hop decay, essential vs helpful weights, gap discount sizes.
  Tune these on Biology by eye.
- Home Ec and Maths exam banks have no `notesRefs` yet, so they have no co-tested
  links or exam value.

## Files
- `scripts/crunch_prereqs.py`: merges and checks the subsection graph →
  `content/crunch/<subject>-prerequisites.json`, review list in
  `drafts/crunch/<subject>/review.md`.
- `scripts/crunch_points.py`: item ids and one package per subsection →
  `drafts/crunch/<subject>/points/`. The agent prompt is
  `drafts/crunch/<subject>/point-prompt.md`.
- `python3 scripts/crunch_points.py <subject> merge`: checks every agent output
  against its package → `content/crunch/<subject>-points.json`
  (`{item: {hash, cost, needs:[{id, strength, why, confidence}]}}`), loops in
  `drafts/crunch/<subject>/point-cycles.json`, spot-check list in
  `drafts/crunch/<subject>/point-review.md`. `drafts/crunch/<subject>/audit.py`
  flags packages with an odd cost-2 rate, link density or default-filled runs.
- `python3 scripts/crunch_map.py <subject>` → `drafts/crunch/<subject>/map/data.json`
  for the Crunch map (`drafts/crunch/biology/map/crunch-map.html`, published as
  https://claude.ai/artifact/NfUzpeCV4bVWn5yvDDsAq3). The scoring lives in
  `drafts/crunch/biology/map/crunch-score.js`: bundles loops, scores downstream,
  then makes a greedy cut with gap discounts. The map's tuning defaults are hop
  decay 0.5, helpful weight 0.5, gap discount 0.5 essential and 0.2 helpful.
  **Exam value (2026-11-24, user asked to bias for choice and recency):**
  - Every Higher Level paper (2015–2025) is re-marked as if it were the 2027 paper:
    old Section A is the compulsory Q1 (1/6), and the B and C questions are optional,
    with the student answering 5 in 6 and dropping the ones they're least ready for.
    Exact top-K, with ties sharing the last places.
  - Marking points are slots ("any k of these points"). Parts tagged to points use
    `content/crunch/<subject>-exam-tags.json`; untagged parts split their marks
    evenly across their subsections' points.
  - Recency: papers are weighted with a half-life (default 8 years).
  - Subsections no old paper tested (19 in Biology, all new-course content) get
    course-average value, defaulting to their share of the course (~10%).
  - Each subsection's chance of coming up is shown: a recency-weighted share of
    papers, with a light prior.
  - Biology results without tags: 55% cuts 75%, 35% cuts 87%. Choice adds about 5
    points; recency adds almost nothing.
  **Pattern backtest** (predicting 2019–2025 from earlier years, by subsection):
  there is no rotation or "it's due" effect. A subsection that came up last year is
  more likely to come up again (61% vs 37%), but that is just its base rate; adding
  a last-year factor made predictions worse. Subsections absent for 4+ years come up
  less (32%), not more. Long half-lives (8+ years) predicted best. The 2026 paper is
  in `exam-papers/biology/` but not yet in the bank.
- `python3 scripts/crunch_exam_tags.py <subject> [merge]`: one package per HL
  question (model answers + candidate points) → `drafts/crunch/<subject>/exam-tags/`,
  prompt `exam-tags/prompt.md`, audit `exam-tags/audit.py`. Pilot on 3 questions:
  Sonnet was precise (61k tokens/question), Haiku over-tagged (31 vs 21 marking
  points on one question).
  **Done 2026-11-24:** all 175 Biology HL questions tagged by Sonnet in two waves
  (35 batches) → `content/crunch/biology-exam-tags.json` (2,781 marking points,
  1,971 distinct points ever tested). 11% of marks are untaggable, almost all
  parts with no model answer in the exam bank.
  **Overfitting, and the fix.** Exact tags alone overfit badly: a set chosen from
  papers up to 2021 to cover 64% scored only 37% on 2022–2025. The cut now gives
  each part `exact` = 0.5 of its marks on its tagged points and spreads the rest
  over those points' subsections, which was the best blend in a backtest.
  (Replaced 2026-11-24 by `crunchBacktest`, see below.) The page also calibrated itself with `crunchCalibrate`: it re-cuts from papers
  up to 2019 and up to 2022, marks the later papers the 2027 way, and maps every
  point to the grade a student would really score. Calibrated Biology results:
  85% target cuts 46% of study effort, 75% cuts 67%, 55% cuts 90%, 35% cuts 96%.
  Only two folds with 3–6 test papers each, so the calibration is noisy.
- Not under `content/<subject>/`: `build_notes.py` reads every `.json` there as a
  subsection.

**Geography (2026-11-24, forked session).** Subsection graph: 98 subsections, 317 links. Point graph:
13,753 items, 8,726 links (23% essential), 1,822 cost-2 items, 63 two-way loops. The loops are almost all one
fact told in two subsections; bundling handles them. Geography packages built the Biology way were about 3×
too big for agents to read reliably, so `drafts/crunch/geography/parts.py` makes a grid instead. Each target chunk
(≤200 items) pairs with candidate groups (≤75 KB). Group 1 rates cost and links; later groups add links only.
`parts.py check` audits the packages, and `parts.py join` unions the groups into one file per subsection before
`crunch_points.py geography merge`. The run was 152 Sonnet jobs in 8 waves. Packages were sent back for:
- default-filled cost packages;
- raising cost to reach an expected cost-2 rate;
- keyword-scanning candidates;
- links from one target to another in links-only packages.
**Student picks.** Each Geography student studies 1 of 2 electives, 1 of 4 options and 1 of 2 continental study
regions (India or Brazil). The map asks for all three and drops the rest as "not your course". This is not a
crunch cut. In `crunch_map.py`, each subsection gets a track (e.g. `option:geoecology`), and elective and option
questions are tied to theirs. A part on India also counts for Brazil, because past papers tag only India.
**Paper structure** is per subject in `crunch_map.py` `SUBJECTS`, as `groups` {group: [share, best K]}:
- Geography: Part One is 1/5, best 10 of 12; physical, regional, elective and option are 1/5 each, best 1.
- Biology: Q1 is 1/6; the optional questions are 5/6, best 5 of 6.
`crunch-score.js` reads the groups (Biology's results are unchanged) and gives `crunchCourse(D, picks)`.
Geography Crunch map: https://claude.ai/artifact/L8iWBKKiqb1KqdsBfc7uU1. Results for Economic, Global
Interdependence and India, calibrated on 2017–2026 HL papers with no point tags: an 85% target cuts 48% of
study effort, 75% cuts 55%, 55% cuts 74% and 35% cuts 89%.
Not modelled: the "any two of three parts" choice inside long questions.

**Geography exam tags (cheap mode, started 2026-11-24).**
- `python3 scripts/crunch_exam_tags.py geography short` shows each question only a shortlist of note points: per
  model-answer line, the best idf-weighted word matches (8 per line for short parts, 4 for parts of 20+ marks).
- Tested on Biology's Sonnet tags: 91% of marking points keep at least one of their points, from 12% of the
  candidates. That makes ~50 KB batches small enough for Haiku.
- Prompt: `drafts/crunch/geography/exam-tags/prompt.md`. Sonnet spot-check prompt: `check-prompt.md`.
- Pilot plus wave 1 (22 batches, 146 of 360 HL questions): all 120 Part One questions and the 2017–18 long
  questions are tagged.
- Spot-check results: short parts about 4% wrong. Long parts had one systematic error, "needs both facts"
  written as k:1. It was fixed by rule (k = all ids in parts of 20+ marks), and the prompt now says so.
- Untagged marks: 34% of Part One (figure reads, and true/false statements, which the bank doesn't store)
  and 4% of long answers.
- Tagged India parts give Brazil the same share, spread over its points (`crunch_map.py`).
- Done 2026-11-24: all 360 HL questions (2015–2026) tagged, 118 Haiku batches. Untagged marks: 5% overall (34% of
  Part One, 39% of the long questions' A parts, ~0% of 20+ mark parts). No part over the marks ÷ 2 cap.
- Final Sonnet check on the lowest-count essays (batches 79, 98): 129 marking points, 1 WRONG, 3 MISSED. The
  low counts are notes gaps (monsoon mechanism, Peru upwelling, Hadley cell, Ophelia), not under-tagging.
- Cuts at a written-paper target with all tags (India / Brazil): 85% → 49% / 54%, 75% → 63% / 64%, 55% → 81% /
  80%. That's bigger than with wave 1 only (39% / 44% at 85%): precise tags put the marks on fewer points.
- Notes conflicts the taggers found, fixed 2026-11-24:
  - Kurdish ban: the notes now say public life until 1991 and broadcasting until the early 2000s, matching the
    model answers.
  - Convection: destructive boundaries now say convection pushes the plates together.
  - 2021 q105 5B (India tourism): its notesRefs pointed at `geo-economic-activities-s2`. Fixed in the bank and in
    the scan's `manual-fixes.json`, and tagged by hand (15 points).
  - The TFR "conflict" was a tagger mix-up (Japan 1.2 vs Ireland 1.5, both right).

## Status (2026-11-23)
Biology point graph drafted by Sonnet, one agent per subsection: 10,583 items,
8,389 links (3,590 essential), 2,113 cost-2 items (total cost 12,696), 29 two-way
loops. Four packages were re-run after their agents misbehaved (truncated reads,
confidence set to mean strength, default-filled items). Not yet reviewed by
Gabriel. The loops must be resolved before any scoring code runs.

**History (2026-11-24).**
- *Subsection graph:* 128 subsections, 205 links (4 Sonnet batches of 3 topics each). Links stay inside a topic, because students study and are examined on topics separately.
- *Point graph:* 9,504 items, 6,338 links, 2,088 cost-2 items, 32 two-way loops. That's 128 packages: 64 Sonnet jobs of 2 packages each, all clean on the first run (`drafts/crunch/history/parts.py`, copied from Geography's).
- *Student picks:* 2 Irish and 2 European topics (tracks `ire:hist-ire3`, `eur:hist-eur4`). `crunchCourse` now accepts a list of picks per kind.
- *Paper:* Q1 documents (1/4 of the paper) counts when it's on one of your topics. Essays are the other 3/4: the best 3 from your topics, which is legal under the alternative instructions. Each essay title is its own question (`split`).
- *No point tags, by choice.* The bank tags every essay to every subsection of its topic, so the exporter (`paragraph_slots`) sends each model-answer paragraph to the subsection it shares the most idf-weighted words with. The paragraph's share of the marks spreads over that subsection's points. Most essays land on 1–3 subsections, and every subsection is hit at least once.
- *Scoring fixes this needed (Biology and Geography results unchanged):*
  - The backtest marks spread-only questions by the share of points kept.
  - The new-course share is 0 when a subject has no never-examined subsections.
- *Results* for Ireland T2+T3 and Europe T3+T4, calibrated: an 85% written target cuts 70% of study effort, 75% cuts 76%, 55% cuts 87%, 35% cuts 93%.
- Map: https://claude.ai/artifact/Rf3zBxq8Bpe19xbMYBr5Ji (`drafts/crunch/history/map/`).
- Not modelled: the essay marking split (60 content + 40 overall evaluation); Q1's document-comprehension parts are treated like note-based marks.

## Per-subject tuning (2026-11-24)
`deno run -A scripts/crunch_tune.js <subject>` → `content/crunch/<subject>-tuning.json`. This is a rolling
backtest: each year from the 6th paper on is predicted from the papers before it. Each setting is scored by
the average real mark over study budgets (keeping 5–60% of study effort). Every `exact` × `halfLife` pair is
tried. The best pair is adopted only if it beats the defaults by 2 standard errors year by year.
- **Biology** (6 test years): best is exact 0.75 / half-life 16, +0.8 ± 0.7 points. Defaults kept.
- **Geography** (5 test years): best is exact 1 / half-life 8, +1.0 ± 2.8 points. The surface is flat and noisy.
  Defaults kept.
- **History** (16 test years): its own best is half-life 8. `exact` has no effect, because essays have no
  point tags. Defaults kept.
So each subject's own papers agree with the shared defaults, within noise.
Not tunable from past papers:
- decay, helpW, gapE, gapH: these are about how students learn.
- newShare: in a backtest, "new" means "not asked yet". Those subsections mostly stay unasked, so the
  backtest always says 0. That is a different thing from new-syllabus content.
These are hand-set judgements for every subject, Biology included.

## Year-by-year backtest and foundation weights (2026-11-24, user's call)
**Backtest.** `crunchBacktest(D, P, q = 0.2)` in `crunch-score.js` replaces the old two-fold `crunchCalibrate`.
For each past year after the first 5 papers, it cuts using only earlier papers and marks that year's real paper.
Each point's level is then the mark a student would get in a bad year: the 20th percentile across years, so the
target is reached in about 4 years in 5. There is no flat +5% margin any more. A subject whose papers swing more
gets a lower bad-year mark, so it keeps more. The maps' fourth stat shows the range of past-year marks for the
current plan and how many years it reached the target. Test years: Biology 2020–25 (6), Geography 2022–26 (5),
History 2011–26 (16). History scores about 6 s per change (16 re-cuts).
**Foundations.** Defaults raised to hop decay 0.65, gap discount 0.75 essential / 0.35 helpful (was 0.5 / 0.5 / 0.2).
At a 55% target, kept points missing an essential foundation fell from 2.7% to 0.7% (Biology). Off entirely it is
31%, and real marks at a 15% study budget were 2–5 points lower, so foundations do help exam marks.
**Results with both** (written-paper target, default picks):
- Biology: 85% → cut 54%, 75% → 70%, 55% → 91%, 35% → 96%.
- Geography: 85% → 53%, 75% → 61%, 55% → 84%, 35% → 94%.
- History: 85% → 51%, 75% → 77%, 55% → 85%, 35% → 92%.
History's past-year range is very wide (as low as about 20% in 3 of 16 years at most targets), because a whole
essay rides on one topic coming up.

## 2026 Biology paper (2026-11-24)
The exam-bank work (gap-filled model answers and the 2026 HL paper, 17 questions) was cherry-picked onto `uxtinker`
as a2e9c1a7. A full merge of `claude/zealous-banach-62c911` would also have brought in three unrelated master commits
and conflicted. `crunch_map.py` now flags a paper as `untagged` when a point-tagged subject has questions without
point tags. `crunchBacktest` trains on such a paper but doesn't test on it, because its fallback marking (every point
of the part's subsections) is far harsher: 2026 scored 16% where tagged years scored 45–66%.
Even in training, untagged 2026 acts like exact = 0 on the newest paper. It shrinks cuts (85% overall with AAC 80:
44% → 34%), and that is an artifact. Leaving 2026 out reproduces the pre-merge numbers exactly. The gap-filled answers
change nothing until their 30 parts (1.2% of marks, 20 questions) are re-tagged: their tags are still empty.
**Done (same day):** 8 Sonnet batches tagged the 17 questions from 2026 and re-tagged the 20 with filled-in answers
(`exam-tags/batches-2026/`). All 192 HL questions are now tagged. Re-tagging agreed with the old tags on 208 of 226 parts
(at least 50% of note points shared), and 13 of the 30 newly answered parts gained tags; the rest are graph readings or
not in the notes. 11.1% of marks are still untagged, almost all on parts with no model answer (dropped topics).
With 2026 tagged it scores like an ordinary year (56/72/88% at levels 40/60/80) and is a test year again (2020–2026).
Cuts at 85/75/65/55% overall (AAC 80): 46/75/91/95%, against 44/73/91/95% before the merge.
Published as Biology map v8. The Q2(b) "Prokaryotic" flag was a false alarm: the question asks for the non-eukaryotic term.

## Crunch Mode in the app (prototype, 2026-11-25, Biology only)
- `deno run -A scripts/crunch_export.js biology` → `biology-crunch.js` (187 KB). It holds each note point as
  `[level, study minutes]`, keyed `{outcome id: {"block.point": …}}`. The level is the written-paper mark at which the
  point is hidden, taken from the map's scoring and year-by-year backtest at the map defaults. Study minutes assume
  40 words a minute of active learning, ×1.5 for points costed 2 (Biology: 135 h in all). Re-run it after rebuilding
  the map data, and bump `?v=` in `CRUNCH_FILES` (app.js).
- The file loads with the subject page itself (`CRUNCH_FILES` in app.js), not the subject pack, because the subject
  home needs it.
- Subject home: whenever Crunch Mode is off (not set up yet, or switched off), a dark Crunch bar sits above the section tiles, headed "Study less. Score more." with "Only on" and the barebones wordmark under it
  in the landing hero's type (Archivo 800, caps). Its left side is the word CRUNCH in orange, an SVG stretched to
  fill the bar's height. Pressing it opens the setup inline: H1–H8, an AAC slider in 5% notches, and a live "N% of the
  course" readout (the share of study time cut) with the written mark needed.
  "Crunch Biology" saves `{set, on, grade, aac, hideAll}` to localStorage `bb-crunch`. The bar is then replaced by a
  "Crunch Mode" tile (e.g. "H3 · cuts 73%"), which opens `#crunch`, the settings section: an on/off switch plus
  the same controls, saved as they change. The default grade is H2, since H5 at an 80% AAC cuts 95% of the course.
- Flashcards (each subsection's key terms) have no points of their own, so the export also writes
  `cards: {subsection: [level per key term]}`. Each card takes the level of the note point sharing the most words with
  it, the term's words counting triple (Biology: 1,709 cards, all matched). A subject without `cards` (PE so far) never
  crunches its flashcards.
- When on, each point and card has one of three states, with need = (grade − w×AAC)/(1 − w):
  0 shown (level < core need), 1 crunched (hidden; "Show crunched points" brings it back, faded),
  2 gone (only with "Completely hide low-value points", off by default: level ≥ the target's need).
  Most marks first is automatic: for H1 and H2 the core need is H3's, so they start with the highest-value points and
  "Show crunched points" adds the rest for their grade. For H3–H8 core and target are the same.
- Notes: the page opens with "Crunch Mode hid X% of this page" and, when any are recoverable,
  Show/Hide crunched points. A block with nothing visible disappears, heading and exam tip included. Live reading
  skips faded points. Flashcards: crunched cards leave the deck; "Show crunched points (X%)" in the card tools puts
  them back with a "Crunched" tag (one switch shared with the notes). Progress totals still count every card.
  Tests and exam questions are untouched. Hidden amounts are shown as percentages, not counts.
- Feel check: at H5 with an 80% AAC the written paper needs 38%, so 95% of points go, and many pages are empty.
  At H2 (88% written), about 45% go.

## PE (2026-11-25)
- **Scope.** The five physical activity areas (Aquatics, Artistic, Athletics, Games, Personal Exercise) are left out:
  never scored, never hidden (`LEFT_OUT` in `scripts/crunch_points.py`, which `crunch_prereqs.py` also uses). They serve
  the Performance Assessment, and the 2022–2026 papers gave them 34 marks in all. The other 8 chapters: 39 subsections,
  2,221 points, about 22 hours of study.
- **Notes version.** Built on master's rewritten PE notes (7144af6a, 2026-11-23). uxtinker had an older, part-rewritten
  `content/pe`, so its `content/pe` and `pe-notes.js` were replaced with master's copies (`pe-notes.js?v=4`).
- **Graphs.** Subsections: 1 Sonnet agent, 48 links (`drafts/crunch/pe/prereq-prompt.md`, catalogue.txt). Points: Biology-style
  packages, 2–4 per Sonnet job (`drafts/crunch/pe/point-prompt.md`, jobs.json, jobs-v2.json for the re-run on master's
  notes; the first run's stale files are in point-links-v1/). Result: 1,144 links, 165 cost-2 items (7%, lower than
  Biology's 20%), 2 two-way loops.
- **Paper** (`crunch_map.py` "pe"): Section A best 10 of 12 (80/250), case study (50/250), Section C best 3 of 5
  (120/250). No point tags: each part's marks spread over its subsection's points, as for History. Only 5 HL papers
  (2022–2026), so the backtest has 3 test years, each trained on 2–4 papers: noisy.
- **Coursework** is the "AAC" at weight 0.5 (project 20% + performance 30%), with `short: "coursework"` for the UI labels.
- **Cuts** at a written-paper target of 88/72/55/38%: 18/38/53/75% of study effort. App: `pe-crunch.js`, registered in
  `CRUNCH_FILES`. All 2,221 point keys match the rendered notes. H3 with 80% coursework cuts 38%.
- Map: https://claude.ai/artifact/RSGnWjmh4CpJZcHLqBJrzZ (`drafts/crunch/pe/map/`, Biology's page with PE wording; crunch-score.js is a symlink).

## Maths: skills in place of note points (2026-11-25)
- `python3 scripts/crunch_maths.py higher|ordinary` → `drafts/crunch/maths[-ordinary]/map/data.json`, the same shape
  as crunch_map.py, so crunch-score.js and the map page score it unchanged. Then `deno run -A scripts/crunch_export.js
  maths` and `… maths-ordinary` → `maths-crunch.js` and `maths-ordinary-crunch.js`.
  - Items are the skills (pipeline/requirements/maths/skills.json): all 361 for Higher, and the 197 that aren't HL-only
    for Ordinary. Ids are "<chapter>.<skill id>". Links are the prereqs, all essential.
  - Papers are 2015–2026 from the exam bank's marks plus skill-tags.json, with every part tagged. Half a part's marks
    go to its primary skill and the other half are shared by its other skills, plus a spread slot over its chapters'
    skills. 2015–2020 questions are all compulsory; from 2021 it's Section A best 5 of 6 and B best 3 of 4 on each
    paper, at both levels.
  - Study time per skill comes from its lesson pack (maths-skills/): Learn-phase words at 40 a minute, plus every
    practice problem at 1 minute a mark (twice exam pace: 150 minutes for 300 marks). Higher totals 181 h against
    the syllabus's 180 hours. Ordinary is 93 h. cost = minutes / 30.
- The bank on this branch now covers 2015–2026 HL and OL (maths-older's finished 2026 work, committed there as
  71c4bf9f and brought in with its crops, 2026-11-25). Master still stops at 2025.
- 2026 out of sample: plans built from 2015–2025 only, marked on the real 2026 papers. Higher reaches H1 (95%),
  H2 (87%), H3 (80%) and H5 (57%), and misses H4 (64.6 for 65) and H6 (41 for 45). Ordinary reaches O1 (96%), O2 (87%),
  O3 (81%), O5 (56%) and O6 (48%), and misses O4 (62 for 65). Adding 2026 to training changes 3–17 skills a grade
  and the cut by 1% at most, so the plan is stable.
- Backtest (test years 2020–2026):
  - Higher: H1 cuts 29% of study time and 6 of 7 papers reach H1; H2 48%, 6/7; H3 60%, 5/7; H4 71%, 6/7.
  - Ordinary: O1 39%, 6/7; O2 58%, 5/7; O3 68%, 6/7; O4 75%, 6/7.
  - Null test (skills relabelled at random): the shuffled data cuts far fewer skills at the same scores
    (H1 57–76 vs 102 real), so the tags carry the signal.
- In the app:
  - The Maths page has the Crunch bar and tile, and a Skills tile linking maths-skill.html (ported from master).
  - The level is the student's onboarding choice (default Higher). Ordinary students get the Ordinary data and see
    O1–O8, stored as H1–H8. There's no AAC slider (Maths has no coursework), and the wording says skills.
  - maths-skill.html loads both files and applies the same rule as app.js crunchFilter: most marks first for H1/H2,
    and "Completely hide". It hides crunched skills, shows "N of M skills" per chapter, and has a Crunch line with
    Show crunched skills (faded) and Change (→ app/maths/#crunch).
