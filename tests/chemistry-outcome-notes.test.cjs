const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function loadChemistry() {
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  for (const file of ["data.js", "chemistry-content.js"]) {
    vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context, { filename: file });
  }
  vm.runInContext("globalThis.__courseData = COURSE_DATA", context);
  return context.__courseData.chapters.filter((chapter) => chapter.subject === "chemistry");
}

test("every Chemistry learning outcome has substantive, outcome-level notes", () => {
  const chapters = loadChemistry();
  const outcomes = chapters.flatMap((chapter) => chapter.learningOutcomes);

  assert.equal(chapters.length, 26);
  outcomes.forEach((outcome) => {
    assert.ok(outcome.notes.length > 0, `${outcome.id} should have notes`);
    outcome.notes.forEach((note) => {
      assert.ok(note.h, `${outcome.id} should have a note heading`);
      assert.ok(note.b.length >= 120, `${outcome.id} should have substantive teaching text`);
    });
  });
});

test("cross-chapter organic and quantitative material is attached to its specification outcome", () => {
  const outcomes = new Map(
    loadChemistry().flatMap((chapter) => chapter.learningOutcomes).map((outcome) => [outcome.id, outcome])
  );
  const headings = (id) => outcomes.get(id).notes.map((note) => note.h);

  assert.ok(headings("chem8-2").includes("Relative atomic mass and the mass spectrometer"));
  assert.ok(headings("chem8-3").includes("Avogadro's Law and Molar Volume of a Gas"));
  assert.ok(headings("chem8-4").includes("Experiment 9.1: Measuring Mr of a Volatile Liquid"));
  assert.ok(headings("chem24-5").includes("Acidity of Alcohols and Carboxylic Acids"));
  assert.ok(headings("chem25-10").includes("Addition Polymers"));

  assert.ok(!headings("chem4-1").includes("Relative atomic mass and the mass spectrometer"));
  assert.ok(!headings("chem9-5").includes("Avogadro's Law and Molar Volume of a Gas"));
  assert.ok(!headings("chem24-1").includes("Addition Polymers"));
});
