const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function rebuiltBank() {
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "biology-exam-questions.js"), "utf8"), context);
  return context.window.EXAM_QUESTIONS_DB;
}

test("rebuilt Biology questions ship as paper crops, never as transcribed text", () => {
  const bank = rebuiltBank();
  assert.ok(bank.length > 0);
  for (const q of bank) {
    assert.ok(q.images.length > 0, `${q.id} has no crops`);
    q.images.forEach((src) => assert.ok(fs.existsSync(path.join(root, src)), `${src} must exist`));
    for (const part of q.parts) {
      assert.ok(!("question" in part) && !("text" in part), `${q.id} ${part.label} ships question text`);
    }
  }
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
