// flagged-exam-questions.js
// Questions that cannot display recommended timing because required data is missing.
// Category:
//   "marks-missing"  — the question parts have marks: 0; add real mark values to the question objects in the source file
//
// To fix a "marks-missing" question: find its id in exam-questions-db.js and set the correct
// marks value on each part object. Once marks > 0 and the subject has totalMarks + totalMinutes
// in exam-breakdown.js, the timing badge will appear automatically.
//
// Currently empty. The 72 previously-flagged biology, geography and PE questions were given
// real mark values derived from the per-question allocations in exam-breakdown.js
// (bio A/B/C = 20/30/60, geo part1/part2 = 8/80, pe A/B/C = 8/50/40). Every subject also has
// totalMarks + totalMinutes, so the timing badge now resolves for the whole question bank.

window.FLAGGED_EXAM_QUESTIONS = [];
