// Geography exam bank, rebuilt to the Biology blueprint (pipeline/EXAM_BANK_REBUILD.md):
// questions ship as crops of the original paper (2017-2026, both levels), every answer was
// written against the marking scheme and checked, and each part is tagged with its exact paper
// question. Part Two is keyed q101+ internally (Part One and Part Two both start at "1"), while
// questionNumber is the number printed on the paper. 30-mark essays were each checked by a
// second Sonnet; any still failing after one fix round ship flagged with no answer.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function rebuiltBank() {
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "geography-exam-questions.js"), "utf8"), context);
  return context.window.EXAM_QUESTIONS_DB;
}

const SECTIONS = { P1: "Part One", core: "Part Two", elective: "Part Two", option: "Part Two" };

test("rebuilt Geography questions ship as paper crops, never as transcribed text", () => {
  const bank = rebuiltBank();
  assert.equal(bank.length, 600, `expected 600 questions, got ${bank.length}`);
  for (const q of bank) {
    assert.ok(q.images.length > 0, `${q.id} has no crops`);
    q.images.forEach((src) => assert.ok(fs.existsSync(path.join(root, src)), `${src} must exist`));
    for (const part of q.parts) {
      assert.ok(!("question" in part) && !("text" in part), `${q.id} ${part.label} ships question text`);
    }
  }
});

test("every question is tagged with its exact paper, part, level and printed number", () => {
  const bank = rebuiltBank();
  const ids = new Set();
  for (const q of bank) {
    assert.ok(!ids.has(q.id), `duplicate id ${q.id}`);
    ids.add(q.id);
    const m = q.id.match(/^geography-pp-(\d{4})-(higher|ordinary)-q(\d+)$/);
    assert.ok(m, `${q.id} id shape`);
    const key = Number(m[3]);
    assert.equal(q.year, Number(m[1]));
    assert.equal(q.level, m[2]);
    assert.equal(q.questionNumber, key % 100, `${q.id} shows the printed number`);
    const section = q.sectionId.replace(/^geo-section/, "");
    assert.ok(section in SECTIONS, `${q.id} section ${q.sectionId}`);
    assert.equal(q.paper, SECTIONS[section], `${q.id} paper`);
    assert.equal(key > 100, q.paper === "Part Two", `${q.id} key and part disagree`);
    assert.equal(q.legacy, false, `${q.id}: the 2003 syllabus is examined to 2027`);
  }
  for (let y = 2017; y <= 2026; y++) {
    for (const level of ["higher", "ordinary"]) {
      const n = bank.filter((q) => q.year === y && q.level === level).length;
      assert.equal(n, level === "higher" ? 36 : 24, `${y} ${level}: ${n} questions`);
    }
  }
});

test("only checked answers ship, and disputed parts carry none", () => {
  for (const q of rebuiltBank()) {
    assert.ok(q.totalMarks > 0, `${q.id} needs the scheme's question total`);
    for (const part of q.parts) {
      const shipped = ["written", "kept"].includes(part.answerStatus);
      assert.equal(Boolean(part.model), shipped, `${q.id} ${part.label}: answer/status mismatch`);
      assert.ok(["kept", "written", "flagged"].includes(part.answerStatus), `${q.id} ${part.label}: ${part.answerStatus}`);
      if (shipped) assert.ok(part.notesRefs.length > 0, `${q.id} ${part.label} cites no notes`);
    }
  }
});

test("no examiner notation or markdown in any shipped answer", () => {
  const NOTATION = [/\(\d{1,2}m\)|\(\d+\s?marks?\)/i, /\/\//, /\*\*/, /\[(accept|allow)/i, /\bSRPs?\b/, /\bexaminers?\b|\bcandidates? (must|should|may|will)\b/i];
  const bad = [];
  for (const q of rebuiltBank()) for (const p of q.parts) {
    if (p.model && NOTATION.some((rx) => rx.test(p.model))) bad.push(`${q.id} ${p.label}`);
  }
  assert.equal(bad.length, 0, `${bad.length} answers with notation: ${bad.slice(0, 5).join(", ")}`);
});

test("30-mark essays came from the checked Sonnet run", () => {
  let essays = 0;
  for (const q of rebuiltBank()) for (const p of q.parts) {
    if (p.marks !== 30 || !p.type.includes("long-answer") || /^\d*A/.test(p.label)) continue;
    essays++;
    if (p.model) assert.match(p.model_source, /^sonnet-thirty/, `${q.id} ${p.label} source ${p.model_source}`);
  }
  assert.ok(essays >= 340, `only ${essays} 30-mark essays`);
});
