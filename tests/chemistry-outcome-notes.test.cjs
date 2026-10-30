const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const os = require("node:os");
const { spawnSync } = require("node:child_process");

const root = path.resolve(__dirname, "..");

function loadChemistry() {
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  for (const file of ["data.js", "chemistry-content.js", "chemistry-notes.js"]) {
    vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context, { filename: file });
  }
  vm.runInContext("globalThis.__courseData = COURSE_DATA", context);
  return context.__courseData.chapters.filter((chapter) => chapter.subject === "chemistry");
}

const isSplit = (chapter) => chapter.learningOutcomes.some((outcome) => /-s\d+$/.test(outcome.id));

test("every Chemistry chapter keeps a review outcome and has authored notes in every subsection", () => {
  const chapters = loadChemistry();
  assert.equal(chapters.length, 26);
  const split = chapters.filter(isSplit);
  assert.equal(split.length, 26);
  split.forEach((chapter) => {
    const [review, ...subsections] = chapter.learningOutcomes;
    assert.equal(review.id, `${chapter.id}-1`);
    assert.equal(review.notes.length, 0, `${review.id} holds only the chapter's test questions`);
    assert.ok(review.questions.length >= 1, `${review.id} keeps the chapter's test questions`);
    subsections.forEach((outcome, index) => {
      assert.equal(outcome.id, `${chapter.id}-s${index + 1}`);
      assert.ok(outcome.syllabusRef, `${outcome.id} needs its specification reference`);
      assert.ok(outcome.authored, `${outcome.id} should have authored notes`);
      assert.ok(outcome.notes.length >= 2, `${outcome.id} should have several note blocks`);
      assert.ok(outcome.keyTerms.length >= 3, `${outcome.id} should have flashcards`);
      assert.ok(outcome.questions.length >= 1, `${outcome.id} should have a practice question`);
    });
  });
});

test("the shipped chemistry notes file is up to date with content/chemistry", () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "notes-")), "chemistry-notes.js");
  const result = spawnSync("python3", [path.join(root, "scripts", "build_notes.py"), "chemistry", "--out", out], {
    encoding: "utf8",
  });
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.equal(fs.readFileSync(out, "utf8"), fs.readFileSync(path.join(root, "chemistry-notes.js"), "utf8"),
    "run python3 scripts/build_notes.py chemistry");
});
