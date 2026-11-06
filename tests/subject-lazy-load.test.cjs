const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const {
  ROOT,
  readPacks,
  loadEager,
  loadSubjectLazily,
  buildChapters,
  courseChapters,
  buildIndex,
  renderIndexFile,
} = require("../scripts/subject-index.cjs");

const packs = readPacks();

test("subject-index.js is up to date (run: deno run -A scripts/build_subject_index.ts)", () => {
  const current = fs.readFileSync(path.join(ROOT, "subject-index.js"), "utf8");
  assert.equal(current, renderIndexFile(buildIndex()));
});

test("every subject pack file exists and app.html no longer loads it up front", () => {
  const html = fs.readFileSync(path.join(ROOT, "app.html"), "utf8");
  for (const file of Object.values(packs).flat()) {
    assert.ok(fs.existsSync(path.join(ROOT, file)), `${file} should exist`);
    assert.ok(!html.includes(`src="./${file}`), `${file} should load lazily, not from app.html`);
  }
});

test("loading one subject on its own gives the same topics and notes as loading everything", () => {
  const eager = loadEager(packs);
  for (const subjectId of Object.keys(packs)) {
    const lazy = loadSubjectLazily(subjectId, packs);
    assert.deepEqual(
      buildChapters(lazy, subjectId),
      buildChapters(eager, subjectId),
      `${subjectId}: flashcard topics should match`,
    );
    assert.deepEqual(
      courseChapters(lazy, subjectId),
      courseChapters(eager, subjectId),
      `${subjectId}: notes and questions should match`,
    );
  }
});

test("the index keeps every topic with exactly its first flashcard", () => {
  const eager = loadEager(packs);
  const index = buildIndex();
  for (const subjectId of Object.keys(packs)) {
    const full = buildChapters(eager, subjectId);
    const stub = index[subjectId].chapters;
    assert.deepEqual(stub.map((c) => c.id), full.map((c) => c.id), `${subjectId}: same chapters`);
    full.forEach((chapter, i) => {
      chapter.learningOutcomes.forEach((lo, j) => {
        const entry = stub[i].learningOutcomes[j];
        assert.equal(entry.id, lo.id);
        assert.equal(entry.cardCount, lo.keyTerms.length);
        assert.deepEqual(entry.keyTerms, lo.keyTerms.slice(0, 1));
      });
    });
  }
});
