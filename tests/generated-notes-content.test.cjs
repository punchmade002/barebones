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

test("generated decks hydrate every Geography and Home Economics chapter with notes", () => {
  const context = load([
    "data.js",
    "home-economics-flashcards.js",
    "geography-flashcards.js",
    "generated-notes-content.js",
  ]);

  for (const subject of ["geography", "home-economics"]) {
    const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === subject);
    assert.ok(chapters.length > 0, `${subject} should have chapters`);

    for (const chapter of chapters) {
      const cards = context.FLASHCARDS_DB[chapter.id];
      const notes = chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []);
      assert.ok(cards?.length > 0, `${chapter.id} should have a generated deck`);
      assert.equal(notes.length, cards.length, `${chapter.id} should expose every card as a note`);
      assert.ok(notes.every((note) => note.h && note.b), `${chapter.id} notes should be complete`);
    }
  }
});

test("the generated adapter does not replace hand-written Chemistry notes", () => {
  const context = load([
    "data.js",
    "chemistry-content.js",
    "home-economics-flashcards.js",
    "geography-flashcards.js",
  ]);
  const before = context.__courseData.chapters
    .filter((chapter) => chapter.subject === "chemistry")
    .map((chapter) => chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []).length);

  vm.runInContext(fs.readFileSync(path.join(root, "generated-notes-content.js"), "utf8"), context, {
    filename: "generated-notes-content.js",
  });

  const after = context.__courseData.chapters
    .filter((chapter) => chapter.subject === "chemistry")
    .map((chapter) => chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []).length);
  assert.deepEqual(after, before);
});
