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
    assert.equal(notes.length, cards.length, `${chapter.id} should expose its generated deck`);
  });
});
