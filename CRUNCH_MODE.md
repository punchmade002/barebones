# Crunch Mode — spec (decisions agreed 2026-11-23)

The student tells a subject what result they need (e.g. 80%). Crunch Mode hides
the lowest-value learning outcomes until what's left just covers that target.
This is the site's USP, so every number has to be explainable.

## Decided

**Unit.** One learning outcome (`bio5-s2` etc.) is the thing that gets scored and
cut. Biology has 163. Notes, key terms and flashcards hang off outcomes already,
and past-paper parts are already tagged to them (`notesRefs`).

**Setup.** Per subject, from the subject page: target %, expected coursework %,
and LC mode or Test mode.

**Target maths.**
- Coursework is subtracted first. For example, Biology 80% overall with 95%
  expected on the 40% investigation: written paper needs (80 − 0.4×95)/0.6 = 70%.
- Add a 5% margin → keep outcomes covering 75% of expected written marks.
- Assume the student gets full marks on every outcome they keep.

**Pure scoring, no absolutes.** No outcome is ever force-kept. A 40% target can
cut ~70% of the course. Foundations survive only because they score high.

**Score per outcome** (LC mode) = exam value + dependency value.
- *Exam value*: expected marks from past papers. **Formula deferred.** Build
  dependencies first.
- *Dependency value*: marks-weighted downstream. Everything that depends on the
  outcome, directly or through a chain, passes some of its exam value back to it.
  Essential links pass more than helpful ones, and the share fades with each hop
  (PageRank-like).
- *Gap discount*: if a kept outcome's prerequisite is cut, its expected marks are
  discounted (more for essential links than for helpful ones). The cut is greedy
  and recomputes after each removal, so it naturally prefers coherent bundles.

**Dependencies.** Within one subject only. Two kinds, stored separately:
- *Prerequisite*: "can't understand A without B". Strength `essential` or
  `helpful`, with a one-line reason. AI drafts per subject; Gabriel spot-checks a
  sample plus every low-confidence link.
- *Co-tested*: outcomes marked together in the same past-paper part. Calculated
  by a script from `*-exam-questions.js` `notesRefs`, with no authoring.

**Test mode** (exam likelihood off, for mocks and class tests): the student ticks
the chapters their test covers. Everything else is hidden. No % target.

**What hides.** Notes and flashcards of cut outcomes. Each page ends with
"x points hidden in Crunch Mode". Tests, quizzes and the exam bank are *not*
filtered. Once scores exist, tests are *biased* towards the highest-scoring
outcomes.

**Progress.** The crunch progress bar shows by default. Detailed views can switch
to full-course progress.

**Pilot.** Biology prerequisites first (Gabriel knows it best). Chemistry is the
first full LC-mode test once exam value exists (25 years of tagged papers).

## Open questions
- Exam value formula (frequency vs marks, recency weighting, question choice such
  as "answer 5 of 6"). Biology's bank is the old course (`legacy: true`), so its
  values will be weaker.
- Should outcome *size* matter? Covering 75% of marks with the least content means
  dividing value by study effort (note count or word count), so a small 5-mark
  outcome beats a huge 6-mark one.
- The exact numbers: hop decay, essential vs helpful weights, gap discount sizes.
  Tune these on Biology by eye.
- Home Ec and Maths exam banks have no `notesRefs` yet, so they have no co-tested
  links or exam value.

## Proposed data shape
`content/<subject>/prerequisites.json`:
```json
{ "bio5-s2": [ { "needs": "bio3-s1", "strength": "essential", "why": "Enzyme action is how photosynthesis is controlled" } ] }
```
