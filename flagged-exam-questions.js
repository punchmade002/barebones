// flagged-exam-questions.js
// Questions that cannot display recommended timing because required data is missing.
// Two categories:
//   "marks-missing"  — the question parts have marks: 0; add real mark values to the question objects in the source file
//   (no second category needed — exam-breakdown entries for all subjects are now present)
//
// To fix a "marks-missing" question: find its id in exam-questions-db.js and set the correct
// marks value on each part object. Once marks > 0 and the subject has totalMarks + totalMinutes
// in exam-breakdown.js, the timing badge will appear automatically.

window.FLAGGED_EXAM_QUESTIONS = [

  // ── BIOLOGY (26 questions — all parts have marks: 0) ─────────────────

  { id: "biology-pp-2019-AB-q2",  subject: "biology",   source: "LC Biology HL 2019 — A+B — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2020-AB-q4",  subject: "biology",   source: "LC Biology HL 2020 — A+B — Q4 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2020-AB-q7",  subject: "biology",   source: "LC Biology HL 2020 — A+B — Q7 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2020-AB-q8",  subject: "biology",   source: "LC Biology HL 2020 — A+B — Q8 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2020-AB-q9",  subject: "biology",   source: "LC Biology HL 2020 — A+B — Q9 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2021-C-q1",   subject: "biology",   source: "LC Biology HL 2021 — C — Q1 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2021-C-q2",   subject: "biology",   source: "LC Biology HL 2021 — C — Q2 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2022-AB-q1",  subject: "biology",   source: "LC Biology HL 2022 — A+B — Q1 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2022-AB-q2",  subject: "biology",   source: "LC Biology HL 2022 — A+B — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2022-AB-q10", subject: "biology",   source: "LC Biology HL 2022 — A+B — Q10 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "biology-pp-2022-C-q1",   subject: "biology",   source: "LC Biology HL 2022 — C — Q1 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2022-C-q2",   subject: "biology",   source: "LC Biology HL 2022 — C — Q2 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2023-AB-q1",  subject: "biology",   source: "LC Biology HL 2023 — A+B — Q1 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2023-AB-q2",  subject: "biology",   source: "LC Biology HL 2023 — A+B — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2023-C-q1",   subject: "biology",   source: "LC Biology HL 2023 — C — Q1 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2023-C-q2",   subject: "biology",   source: "LC Biology HL 2023 — C — Q2 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q1",  subject: "biology",   source: "LC Biology HL 2024 — A+B — Q1 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q2",  subject: "biology",   source: "LC Biology HL 2024 — A+B — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q3",  subject: "biology",   source: "LC Biology HL 2024 — A+B — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q4",  subject: "biology",   source: "LC Biology HL 2024 — A+B — Q4 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q9",  subject: "biology",   source: "LC Biology HL 2024 — A+B — Q9 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2024-AB-q10", subject: "biology",   source: "LC Biology HL 2024 — A+B — Q10 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "biology-pp-2024-C-q1",   subject: "biology",   source: "LC Biology HL 2024 — C — Q1 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2024-C-q2",   subject: "biology",   source: "LC Biology HL 2024 — C — Q2 [⚠ may not match current course]",    reason: "marks-missing" },
  { id: "biology-pp-2025-AB-q2",  subject: "biology",   source: "LC Biology HL 2025 — A+B — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "biology-pp-2025-AB-q9",  subject: "biology",   source: "LC Biology HL 2025 — A+B — Q9 [⚠ may not match current course]",  reason: "marks-missing" },

  // ── GEOGRAPHY (45 questions — all parts have marks: 0) ───────────────

  { id: "geography-pp-2020-Part2-q1",  subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q1 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2020-Part2-q2",  subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2020-Part2-q3",  subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2020-Part2-q5",  subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q5 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2020-Part2-q20", subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2020-Part2-q21", subject: "geography", source: "LC Geography HL 2020 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2021-Part1-q2",  subject: "geography", source: "LC Geography HL 2021 — Part 1 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part1-q5",  subject: "geography", source: "LC Geography HL 2021 — Part 1 — Q5 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part1-q6",  subject: "geography", source: "LC Geography HL 2021 — Part 1 — Q6 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q1",  subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q1 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q2",  subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q3",  subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q19", subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q19 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q20", subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2021-Part2-q21", subject: "geography", source: "LC Geography HL 2021 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q2",  subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q3",  subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q5",  subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q5 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q19", subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q19 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q20", subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2022-Part2-q21", subject: "geography", source: "LC Geography HL 2022 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2023-Part2-q2",  subject: "geography", source: "LC Geography HL 2023 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2023-Part2-q3",  subject: "geography", source: "LC Geography HL 2023 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2023-Part2-q19", subject: "geography", source: "LC Geography HL 2023 — Part 2 — Q19 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2023-Part2-q20", subject: "geography", source: "LC Geography HL 2023 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2023-Part2-q21", subject: "geography", source: "LC Geography HL 2023 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2024-Part1-q2",  subject: "geography", source: "LC Geography HL 2024 — Part 1 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part1-q3",  subject: "geography", source: "LC Geography HL 2024 — Part 1 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part1-q4",  subject: "geography", source: "LC Geography HL 2024 — Part 1 — Q4 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part1-q5",  subject: "geography", source: "LC Geography HL 2024 — Part 1 — Q5 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part1-q6",  subject: "geography", source: "LC Geography HL 2024 — Part 1 — Q6 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q2",  subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q3",  subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q5",  subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q5 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q6",  subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q6 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q19", subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q19 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q20", subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2024-Part2-q21", subject: "geography", source: "LC Geography HL 2024 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2025-Part1-q6",  subject: "geography", source: "LC Geography HL 2025 — Part 1 — Q6 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q2",  subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q2 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q3",  subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q3 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q6",  subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q6 [⚠ may not match current course]",  reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q19", subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q19 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q20", subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q20 [⚠ may not match current course]", reason: "marks-missing" },
  { id: "geography-pp-2025-Part2-q21", subject: "geography", source: "LC Geography HL 2025 — Part 2 — Q21 [⚠ may not match current course]", reason: "marks-missing" },

  // ── PE (1 question — one part has marks: 0) ──────────────────────────

  { id: "pe-pp-2023-None-q2", subject: "pe", source: "LC PE HL 2023 — Q2 [⚠ may not match current course]", reason: "marks-missing" },

];
