const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.join(__dirname, "..");
const subjectIds = [
  "business",
  "pe",
  "biology",
  "geography",
  "maths",
  "chemistry",
  "home-economics",
  "history",
];

function loadResources() {
  const window = {};
  const context = vm.createContext({ window });
  const source = fs.readFileSync(
    path.join(root, "relevant-resources", "relevant-resources.js"),
    "utf8"
  );
  vm.runInContext(source, context);
  return window.RELEVANT_RESOURCES;
}

test("every app subject has a valid local syllabus PDF", () => {
  const resources = loadResources();
  assert.deepEqual(Object.keys(resources.subjects), subjectIds);

  subjectIds.forEach((subjectId) => {
    const syllabus = resources.subjects[subjectId].syllabus;
    const relativePath = syllabus.path.replace(/^\.\//, "");
    const absolutePath = path.join(root, relativePath);
    assert.equal(fs.existsSync(absolutePath), true, `${subjectId} PDF is missing`);
    assert.equal(
      fs.readFileSync(absolutePath).subarray(0, 4).toString(),
      "%PDF",
      `${subjectId} is not a PDF`
    );
    assert.match(syllabus.sourceUrl, /^https:\/\/(www\.)?curriculumonline\.ie\//);
  });
});

test("the resource manifest validates without structural errors", () => {
  const resources = loadResources();
  assert.equal(resources.schemaVersion, 1);
  assert.deepEqual(resources.validate(), []);
});

test("SimpleStudy research uses explicit empty arrays until authenticated research is added", () => {
  const resources = loadResources();

  subjectIds.forEach((subjectId) => {
    const research = resources.subjects[subjectId].simpleStudy;
    assert.equal(research.status, "awaiting-authentication");
    assert.ok(Array.isArray(research.chapterStructure));
    assert.ok(Array.isArray(research.insights));
    assert.ok(Array.isArray(research.solvedExamples));
  });
});
