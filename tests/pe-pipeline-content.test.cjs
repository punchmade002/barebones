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

test("PE pipeline chapters are visible and address every generated asset", () => {
  const context = load([
    "data.js",
    "pe-content.js",
    "pe-exam-questions.js",
    "pe-flashcards.js",
    "pe-pipeline-content.js",
  ]);

  const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === "pe");
  const chapterIds = new Set(chapters.map((chapter) => chapter.id));
  const deckIds = Object.keys(context.FLASHCARDS_DB || {}).filter((id) => id.startsWith("pe-"));
  const questionChapterIds = new Set(
    (context.EXAM_QUESTIONS_DB || [])
      .filter((question) => question.subject === "pe")
      .map((question) => question.chapterId)
  );

  assert.equal(chapters.length, 16);
  assert.deepEqual([...chapterIds].sort(), deckIds.sort());
  assert.ok([...questionChapterIds].every((id) => chapterIds.has(id)));
  chapters.forEach((chapter) => {
    const cards = context.FLASHCARDS_DB[chapter.id];
    const notes = chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []);
    assert.ok(cards.length > 0, `${chapter.id} should expose its generated deck`);
    assert.ok(
      !notes.some((note) => cards.some((card) => note.h === card.term && note.b === card.definition)),
      `${chapter.id} should not copy its generated deck into notes`
    );
  });
});

test("PE practice questions have one canonical chapter and retain full coverage", () => {
  const context = load([
    "data.js",
    "pe-content.js",
    "pe-exam-questions.js",
    "pe-flashcards.js",
    "pe-pipeline-content.js",
    "pe-test-questions.js",
  ]);

  const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === "pe");
  const questions = chapters.flatMap((chapter) =>
    chapter.learningOutcomes.flatMap((outcome) =>
      (outcome.questions || []).map((question) => ({ chapterId: chapter.id, question }))
    )
  );
  const normalise = (prompt) => String(prompt || "").trim().toLowerCase().replace(/\s+/g, " ");
  const prompts = questions.map(({ question }) => normalise(question.prompt));

  assert.equal(questions.length, 53, "all 52 original prompts and the ethics top-up should remain available");
  assert.equal(new Set(prompts).size, questions.length, "a practice prompt must not appear in two chapters");
  chapters.forEach((chapter) => {
    const count = chapter.learningOutcomes.reduce(
      (total, outcome) => total + (outcome.questions || []).length,
      0
    );
    assert.ok(count >= 3, `${chapter.id} should retain at least three practice questions`);
  });

  const newton = questions.filter(({ question }) =>
    normalise(question.prompt) === normalise("Explain Newton's three laws of motion using sporting examples.")
  );
  assert.equal(newton.length, 1);
  assert.equal(newton[0].chapterId, "pe-athletics");

  vm.runInContext(fs.readFileSync(path.join(root, "pe-test-questions.js"), "utf8"), context, {
    filename: "pe-test-questions.js",
  });
  const countAfterReload = context.__courseData.chapters
    .filter((chapter) => chapter.subject === "pe")
    .flatMap((chapter) => chapter.learningOutcomes)
    .flatMap((outcome) => outcome.questions || []).length;
  assert.equal(countAfterReload, questions.length, "reloading the top-up must not duplicate questions");
});
