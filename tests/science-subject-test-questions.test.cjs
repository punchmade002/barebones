const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function createContext(files) {
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

function shortQuestions(outcome) {
  return (outcome.questions || []).filter((question) => question.type === "short" && question.prompt);
}

for (const config of [
  {
    subject: "pe",
    chapters: 16,
    outcomes: 16,
    minimumPerOutcome: 3,
    added: 15,
    setup: ["data.js", "pe-content.js", "pe-flashcards.js", "pe-pipeline-content.js"],
    additions: "pe-test-questions.js",
  },
  {
    subject: "biology",
    chapters: 36,
    outcomes: 36,
    minimumPerOutcome: 3,
    added: 60,
    setup: ["data.js", "bio-content.js"],
    additions: "biology-test-questions.js",
  },
  {
    subject: "chemistry",
    chapters: 26,
    outcomes: 125,
    minimumPerOutcome: 1,
    added: 50,
    setup: ["data.js", "chemistry-content.js"],
    additions: "chemistry-test-questions.js",
  },
]) {
  test(`${config.subject} has authored written questions for every learning outcome`, () => {
    const context = createContext(config.setup);
    const chaptersBefore = context.__courseData.chapters.filter(
      (chapter) => chapter.subject === config.subject
    );
    const promptsBefore = new Set(
      chaptersBefore.flatMap((chapter) => chapter.learningOutcomes)
        .flatMap(shortQuestions)
        .map((question) => question.prompt.trim().toLowerCase())
    );
    const flashcardPrompts = new Set(
      chaptersBefore.flatMap((chapter) => chapter.learningOutcomes)
        .flatMap((outcome) => outcome.keyTerms || [])
        .map((card) => card.term.trim().toLowerCase())
    );

    vm.runInContext(fs.readFileSync(path.join(root, config.additions), "utf8"), context, {
      filename: config.additions,
    });

    const chapters = context.__courseData.chapters.filter(
      (chapter) => chapter.subject === config.subject
    );
    const outcomes = chapters.flatMap((chapter) => chapter.learningOutcomes);
    const allQuestions = outcomes.flatMap(shortQuestions);
    const addedQuestions = allQuestions.filter(
      (question) => !promptsBefore.has(question.prompt.trim().toLowerCase())
    );

    assert.equal(chapters.length, config.chapters);
    assert.equal(outcomes.length, config.outcomes);
    outcomes.forEach((outcome) => {
      assert.ok(
        shortQuestions(outcome).length >= config.minimumPerOutcome,
        `${outcome.id} should have at least ${config.minimumPerOutcome} written question(s)`
      );
    });
    assert.equal(addedQuestions.length, config.added);
    addedQuestions.forEach((question) => {
      assert.ok(question.prompt.length >= 35, "new prompt should be exam-style");
      assert.ok(question.model.length >= 140, "new question should have substantive marking content");
      assert.ok(question.marks >= 6, "new question should carry a meaningful mark allocation");
      assert.ok(
        !flashcardPrompts.has(question.prompt.trim().toLowerCase()),
        "new question should not copy a flashcard front"
      );
    });
    const newPrompts = addedQuestions.map((question) => question.prompt.trim().toLowerCase());
    assert.equal(newPrompts.length, new Set(newPrompts).size, "new prompts should be unique");
  });
}

test("the Test tab scopes multi-outcome chapters to the selected outcome", () => {
  const appSource = fs.readFileSync(path.join(root, "app.js"), "utf8");
  assert.match(appSource, /questionsForChapter\(chapter, outcome\)/);
  assert.match(appSource, /const matchingOutcome = source\.learningOutcomes\.find/);
  assert.match(appSource, /const outcomesToTest = matchingOutcome \? \[matchingOutcome\] : source\.learningOutcomes/);
});
