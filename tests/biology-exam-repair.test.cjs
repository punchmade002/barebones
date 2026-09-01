const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function biologyBank() {
  const context = { window: {}, COURSE_DATA: { chapters: [] } };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "exam-questions-db.js"), "utf8"), context, {
    filename: "exam-questions-db.js",
  });
  return context.window.EXAM_QUESTIONS_DB.filter((q) => q.subject === "biology");
}

test("Biology exam repair has complete answer and source-page coverage", () => {
  const questions = biologyBank();
  const parts = questions.flatMap((q) => q.parts);
  assert.equal(questions.length, 28);
  assert.equal(parts.length, 66);
  assert.ok(parts.every((p) => String(p.model || "").trim()));
  assert.equal(parts.filter((p) => p.model_source === "scheme").length, 63);
  assert.equal(parts.filter((p) => p.model_source === "ai-h1").length, 3);

  const diagrams = parts.map((p) => p.diagram).filter(Boolean);
  assert.equal(diagrams.length, 28);
  const hashes = diagrams.map((relative) => {
    const absolute = path.join(root, relative);
    assert.ok(fs.existsSync(absolute), `${relative} must exist`);
    return crypto.createHash("sha256").update(fs.readFileSync(absolute)).digest("hex");
  });
  assert.equal(new Set(hashes).size, 28);
});

test("the four formerly undated Biology pages have verified source records", () => {
  const questions = biologyBank();
  const byId = new Map(questions.map((q) => [q.id, q]));
  for (const [id, year] of [
    ["biology-pp-2015-A-q6", 2015],
    ["biology-pp-2015-C-q11", 2015],
    ["biology-pp-2016-C-q15", 2016],
    ["biology-pp-2017-B-q8", 2017],
  ]) {
    const question = byId.get(id);
    assert.ok(question, `${id} must be present`);
    assert.equal(question.year, year);
    assert.match(question.source, /LC Biology Higher/);
  }
});
