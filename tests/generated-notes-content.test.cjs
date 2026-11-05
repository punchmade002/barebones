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

test("generated subjects receive connected exam-ready notes without losing deck coverage", () => {
  const context = load([
    "data.js",
    "pe-content.js",
    "home-economics-exam-questions.js",
    "home-economics-flashcards.js",
    "pe-exam-questions.js",
    "pe-flashcards.js",
    "pe-pipeline-content.js",
    "generated-notes-content.js",
  ]);

  for (const subject of ["home-economics", "pe"]) {
    const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === subject);
    assert.ok(chapters.length > 0, `${subject} should have chapters`);

    for (const chapter of chapters) {
      const cards = context.FLASHCARDS_DB[chapter.id];
      const notes = chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []);
      assert.ok(cards?.length > 0, `${chapter.id} should have a generated deck`);
      assert.ok(notes.length >= 3, `${chapter.id} should have an overview, developed content and answer method`);
      assert.equal(notes[0].h, "Chapter overview and connections");
      assert.equal(notes.at(-1).h, "How to build a full-mark answer");
      assert.ok(notes.every((note) => note.h && note.b), `${chapter.id} notes should be complete`);
      assert.ok(
        notes.some((note) => note.b.length >= 250),
        `${chapter.id} should include developed explanation rather than definition-only notes`
      );
      if (subject === "pe") {
        const wordCount = notes
          .map((note) => `${note.h} ${note.b}`)
          .join(" ")
          .trim()
          .split(/\s+/).length;
        assert.ok(wordCount >= 450, `${chapter.id} should contain substantial PE revision depth`);
      }

      const corpus = notes.map((note) => `${note.h} ${note.b}`).join(" ").toLowerCase();
      cards.forEach((card) => {
        assert.ok(corpus.includes(card.term.toLowerCase()), `${chapter.id} should retain ${card.term}`);
        assert.ok(corpus.includes(card.definition.toLowerCase()), `${chapter.id} should retain the detail for ${card.term}`);
        assert.ok(
          !notes.some((note) => note.h === card.term && note.b === card.definition),
          `${chapter.id} must not copy a flashcard directly into a note`
        );
      });
    }
  }
});

test("Home Economics consumer notes identify the current Consumer Rights Act", () => {
  const context = load([
    "data.js",
    "home-economics-flashcards.js",
    "generated-notes-content.js",
  ]);
  const chapter = context.__courseData.chapters.find((item) => item.id === "hom-consumer-rights");
  const corpus = chapter.learningOutcomes.flatMap((outcome) => outcome.notes || [])
    .map((note) => note.b)
    .join(" ");
  assert.match(corpus, /Consumer Rights Act 2022/);
});

test("the generated adapter does not replace hand-written Chemistry notes", () => {
  const context = load([
    "data.js",
    "chemistry-content.js",
    "home-economics-flashcards.js",
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

test("past-paper notes match eager loading when the exam pack arrives after the adapter", () => {
  // JSON round-trip: each vm context has its own Array prototype, which deepEqual compares.
  const notesFor = (context) => JSON.parse(JSON.stringify(context.__courseData.chapters
    .filter((chapter) => chapter.subject === "home-economics")
    .map((chapter) => chapter.learningOutcomes.flatMap((outcome) => outcome.notes || []).map((note) => note.h))));

  const eager = load([
    "data.js",
    "home-economics-exam-questions.js",
    "home-economics-flashcards.js",
    "generated-notes-content.js",
  ]);
  const lazy = load([
    "data.js",
    "home-economics-flashcards.js",
    "generated-notes-content.js",
  ]);
  const withoutPack = notesFor(lazy);
  vm.runInContext(fs.readFileSync(path.join(root, "home-economics-exam-questions.js"), "utf8"), lazy);
  lazy.refreshGeneratedExamBlueprints("home-economics");

  assert.notDeepEqual(withoutPack, notesFor(eager), "the pack should add past-paper blocks");
  assert.deepEqual(notesFor(lazy), notesFor(eager));
  lazy.refreshGeneratedExamBlueprints("home-economics");
  assert.deepEqual(notesFor(lazy), notesFor(eager), "refreshing twice should not duplicate blocks");
});
