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

**Target maths.**
- Coursework is subtracted first. For example, Biology 80% overall with 95%
  expected on the 40% investigation: written paper needs (80 − 0.4×95)/0.6 = 70%.
- Add a 5% margin → keep items covering 75% of expected written marks.
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
- Not under `content/<subject>/`: `build_notes.py` reads every `.json` there as a
  subsection.
