// History exam bank, rebuilt to the Biology blueprint (pipeline/EXAM_BANK_REBUILD.md):
// questions ship as crops of the original paper (Later Modern, 2006-2026, both levels), every
// answer was written against the marking scheme and checked, and each part is tagged with its
// exact paper question. Section 1 is the documents-based question (q1), Section 2 Ireland
// (q2-q7), Section 3 Europe and the wider world (q8-q13); the DBQ's own topic is not set again,
// so a paper has 12 questions, plus the Ordinary "Alternative Instructions" Part A from 2023.
// Long answers (Higher essays, Higher DBQ question 4) come only from the Sonnet long run, where a
// second Sonnet checked every answer; until it lands, or if one still fails after a fix round,
// they ship flagged with no answer.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function rebuiltBank() {
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "history-exam-questions.js"), "utf8"), context);
  return context.window.EXAM_QUESTIONS_DB;
}

const isLong = (q, p) => q.level === "higher" && p.type.includes("long-answer") && (p.marks >= 100 || (p.label === "4" && p.marks >= 40));

test("rebuilt History questions ship as paper crops, never as transcribed text", () => {
  const bank = rebuiltBank();
  assert.equal(bank.length, 508, `expected 508 questions, got ${bank.length}`);
  for (const q of bank) {
    assert.ok(q.images.length > 0, `${q.id} has no crops`);
    q.images.forEach((src) => assert.ok(fs.existsSync(path.join(root, src)), `${src} must exist`));
    for (const part of q.parts) {
      assert.ok(!("question" in part) && !("text" in part), `${q.id} ${part.label} ships question text`);
    }
  }
});

test("every question is tagged with its exact paper, section, level and number", () => {
  const bank = rebuiltBank();
  const ids = new Set();
  for (const q of bank) {
    assert.ok(!ids.has(q.id), `duplicate id ${q.id}`);
    ids.add(q.id);
    const m = q.id.match(/^history-pp-(\d{4})-(higher|ordinary)-q(\d+)$/);
    assert.ok(m, `${q.id} id shape`);
    const n = Number(m[3]);
    assert.equal(q.year, Number(m[1]));
    assert.equal(q.level, m[2]);
    assert.equal(q.questionNumber, n);
    const section = n === 1 ? 1 : n <= 7 ? 2 : 3;
    assert.equal(q.sectionId, `hist-section${section}`, `${q.id} section`);
    assert.equal(q.paper, `Section ${section}`, `${q.id} paper`);
    assert.match(q.chapterId, /^hist-(ire|eur)[1-6]$/, `${q.id} chapter`);
    assert.equal(q.legacy, false, `${q.id}: the Later Modern syllabus is still examined`);
  }
  for (let y = 2006; y <= 2026; y++) {
    for (const level of ["higher", "ordinary"]) {
      const n = bank.filter((q) => q.year === y && q.level === level).length;
      assert.equal(n, level === "ordinary" && y >= 2023 ? 13 : 12, `${y} ${level}: ${n} questions`);
    }
  }
});

test("only checked answers ship, and every short part has one", () => {
  for (const q of rebuiltBank()) {
    assert.ok(q.totalMarks > 0, `${q.id} needs the scheme's question total`);
    for (const part of q.parts) {
      const shipped = ["written", "kept"].includes(part.answerStatus);
      assert.equal(Boolean(part.model), shipped, `${q.id} ${part.label}: answer/status mismatch`);
      assert.ok(["kept", "written", "flagged"].includes(part.answerStatus), `${q.id} ${part.label}: ${part.answerStatus}`);
      if (shipped) assert.ok(part.notesRefs.length > 0, `${q.id} ${part.label} cites no notes`);
      if (!isLong(q, part)) assert.ok(part.model, `${q.id} ${part.label}: short part with no answer`);
    }
  }
});

test("no examiner notation or markdown in any shipped answer", () => {
  const NOTATION = [/\(\d{1,2}m\)|\(\d+\s?marks?\)/i, /\/\//, /\*\*/, /\[(accept|allow)/i, /\bSRPs?\b/, /\b(CM|OE)\b/,
    // History content mentions "federal examiners" and the "Christian Examiner", so only the marker's voice is caught.
    /\bcore statements?\b/i, /\bthe examiner\b|\bcandidates? (must|should|may|will)\b/i, /(^|[.;]\s*)(accept|allow)\b/im];
  const bad = [];
  for (const q of rebuiltBank()) for (const p of q.parts) {
    if (p.model && NOTATION.some((rx) => rx.test(p.model))) bad.push(`${q.id} ${p.label}`);
  }
  assert.equal(bad.length, 0, `${bad.length} answers with notation: ${bad.slice(0, 5).join(", ")}`);
});

test("long answers came only from the checked Sonnet long run", () => {
  let long = 0;
  for (const q of rebuiltBank()) for (const p of q.parts) {
    if (!isLong(q, p)) {
      if (p.model) assert.doesNotMatch(p.model_source, /^sonnet-long/, `${q.id} ${p.label}`);
      continue;
    }
    long++;
    if (p.model) assert.match(p.model_source, /^sonnet-long/, `${q.id} ${p.label} source ${p.model_source}`);
  }
  assert.equal(long, 945, `expected 945 long parts, got ${long}`);
});
