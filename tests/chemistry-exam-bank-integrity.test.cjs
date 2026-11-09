// Chemistry exam bank, rebuilt to the Biology blueprint (pipeline/EXAM_BANK_REBUILD.md):
// questions ship as crops of the original paper, every answer is notes-only and checked
// against the marking scheme, and each part is tagged with its exact paper question.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function rebuiltBank() {
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "chemistry-exam-questions.js"), "utf8"), context);
  return context.window.EXAM_QUESTIONS_DB;
}

test("rebuilt Chemistry questions ship as paper crops, never as transcribed text", () => {
  const bank = rebuiltBank();
  assert.ok(bank.length > 500, `only ${bank.length} questions`);
  for (const q of bank) {
    assert.ok(q.images.length > 0, `${q.id} has no crops`);
    q.images.forEach((src) => assert.ok(fs.existsSync(path.join(root, src)), `${src} must exist`));
    for (const part of q.parts) {
      assert.ok(!("question" in part) && !("text" in part), `${q.id} ${part.label} ships question text`);
    }
  }
});

test("every question is tagged with its exact paper, level and number", () => {
  const bank = rebuiltBank();
  const ids = new Set();
  for (const q of bank) {
    assert.ok(!ids.has(q.id), `duplicate id ${q.id}`);
    ids.add(q.id);
    assert.match(q.id, /^chemistry-pp-\d{4}-(higher|ordinary)-q\d+$/);
    assert.ok(["higher", "ordinary"].includes(q.level), `${q.id} level`);
    assert.equal(q.id, `chemistry-pp-${q.year}-${q.level}-q${q.questionNumber}`);
    assert.ok(["chem-sectionA", "chem-sectionB"].includes(q.sectionId), `${q.id} section`);
    assert.equal(q.legacy, true, `${q.id}: every paper predates the 2027 specification`);
  }
  // every paper on disk (2001-2025) is represented
  const years = new Set(bank.map((q) => q.year));
  for (let y = 2001; y <= 2025; y++) assert.ok(years.has(y), `no questions from ${y}`);
});

test("only checked answers ship, and off-spec or disputed parts carry none", () => {
  for (const q of rebuiltBank()) {
    assert.ok(q.totalMarks > 0, `${q.id} needs the scheme's question total`);
    for (const part of q.parts) {
      const shipped = ["written", "kept"].includes(part.answerStatus);
      assert.equal(Boolean(part.model), shipped, `${q.id} ${part.label}: answer/status mismatch`);
      if (part.offSpec) assert.equal(part.answerStatus, "off-spec");
      if (shipped) assert.ok(part.notesRefs.length > 0, `${q.id} ${part.label} cites no notes`);
    }
  }
});
