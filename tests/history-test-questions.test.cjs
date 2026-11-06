const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function load(files) {
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  files.forEach((file) => {
    vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context, { filename: file });
  });
  vm.runInContext("globalThis.__courseData = COURSE_DATA", context);
  return context;
}

test("every broad History learning outcome has several hand-authored test questions", () => {
  const context = load(["data.js", "history-test-questions.js"]);
  const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === "history");

  assert.equal(chapters.length, 12);
  chapters.forEach((chapter) => {
    // Chapters are split into outline subsections; the authored test set sits on each
    // chapter's review outcome (<chapter>-1), not on every subsection.
    chapter.learningOutcomes.filter((outcome) => outcome.id === `${chapter.id}-1`).forEach((outcome) => {
      assert.ok(outcome.questions.length >= 3, `${outcome.id} should have several questions`);
      outcome.questions.forEach((question) => {
        assert.equal(question.type, "short", `${outcome.id} should use written answers`);
        assert.ok(question.prompt.length >= 35, `${outcome.id} prompt should be exam-style`);
        assert.ok(question.model.length >= 150, `${outcome.id} should have a substantive model answer`);
        assert.ok(question.marks >= 8, `${outcome.id} question should be challenging`);
      });
    });
  });
});

test("History test prompts are not copied from the flashcard fronts", () => {
  const context = load(["data.js", "history-test-questions.js", "history-notes.js"]);
  const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === "history");
  const flashcardPrompts = new Set(
    chapters
      .flatMap((chapter) => chapter.learningOutcomes)
      .flatMap((outcome) => outcome.keyTerms || [])
      .map((card) => card.term.trim().toLowerCase())
  );
  assert.ok(flashcardPrompts.size > 1000, "authored history flashcards should load");
  const testPrompts = chapters
    .flatMap((chapter) => chapter.learningOutcomes)
    .flatMap((outcome) => outcome.questions)
    .map((question) => question.prompt.trim().toLowerCase());

  assert.equal(testPrompts.length, new Set(testPrompts).size, "test prompts should be unique");
  assert.ok(testPrompts.every((prompt) => !flashcardPrompts.has(prompt)), "test prompts should differ from flashcards");
});
