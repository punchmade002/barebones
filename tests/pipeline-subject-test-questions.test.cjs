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

for (const config of [
  {
    subject: "geography",
    chapters: 25,
    files: ["data.js", "geography-flashcards.js", "geography-test-questions.js"],
  },
  {
    subject: "home-economics",
    chapters: 31,
    files: ["data.js", "home-economics-flashcards.js", "home-economics-test-questions.js"],
  },
]) {
  test(`every ${config.subject} learning outcome has a distinct authored test set`, () => {
    const context = load(config.files);
    const chapters = context.__courseData.chapters.filter(
      (chapter) => chapter.subject === config.subject
    );
    const deckPrompts = new Set(
      Object.entries(context.FLASHCARDS_DB || {})
        .filter(([id]) => chapters.some((chapter) => chapter.id === id))
        .flatMap(([, cards]) => cards.map((card) => card.term.trim().toLowerCase()))
    );
    const testPrompts = [];

    assert.equal(chapters.length, config.chapters);
    chapters.forEach((chapter) => {
      chapter.learningOutcomes.forEach((outcome) => {
        assert.ok(outcome.questions.length >= 3, `${outcome.id} should have several questions`);
        outcome.questions.forEach((question) => {
          assert.equal(question.type, "short", `${outcome.id} should use written answers`);
          assert.ok(question.prompt.length >= 35, `${outcome.id} prompt should be exam-style`);
          assert.ok(question.model.length >= 140, `${outcome.id} should have marking content`);
          assert.ok(question.marks >= 8, `${outcome.id} should be challenging`);
          assert.ok(!deckPrompts.has(question.prompt.trim().toLowerCase()), `${outcome.id} should differ from flashcards`);
          testPrompts.push(question.prompt.trim().toLowerCase());
        });
      });
    });

    assert.equal(testPrompts.length, new Set(testPrompts).size, `${config.subject} prompts should be unique`);
  });
}
