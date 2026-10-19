// Authored subsection notes: content/<subject>/<loId>.json -> <subject>-notes.js -> COURSE_DATA.
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const vm = require("node:vm");
const { spawnSync } = require("node:child_process");

const root = path.resolve(__dirname, "..");
const fixtures = path.join(__dirname, "fixtures", "notes", "geography");

function build(args) {
  return spawnSync("python3", [path.join(root, "scripts", "build_notes.py"), "geography", ...args], {
    encoding: "utf8",
  });
}

function load(files) {
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  files.forEach((file) => {
    const full = path.isAbsolute(file) ? file : path.join(root, file);
    vm.runInContext(fs.readFileSync(full, "utf8"), context, { filename: file });
  });
  vm.runInContext("globalThis.__courseData = COURSE_DATA", context);
  return context;
}

test("every geography chapter is split into its syllabus subsections", () => {
  const context = load(["data.js"]);
  const chapters = context.__courseData.chapters.filter((chapter) => chapter.subject === "geography");
  assert.equal(chapters.length, 25);
  let subsections = 0;
  chapters.forEach((chapter) => {
    const [review, ...rest] = chapter.learningOutcomes;
    assert.equal(review.id, `${chapter.id}-1`, `${chapter.id} keeps its review outcome for existing test questions`);
    assert.ok(rest.length >= 1, `${chapter.id} should have subsections`);
    rest.forEach((outcome, index) => {
      assert.equal(outcome.id, `${chapter.id}-s${index + 1}`);
      assert.ok(outcome.title.length > 3);
    });
    subsections += rest.length;
  });
  assert.equal(subsections, 97);
});

test("authored notes attach to their subsection and replace the generated chapter notes", () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "notes-")), "geography-notes.js");
  const result = build(["--content", fixtures, "--out", out]);
  assert.equal(result.status, 0, result.stdout + result.stderr);

  const context = load([
    "data.js",
    "geography-exam-questions.js",
    "geography-flashcards.js",
    "geography-test-questions.js",
    out,
    "generated-notes-content.js",
  ]);
  const chapters = context.__courseData.chapters;
  const rivers = chapters.find((chapter) => chapter.id === "geo-rivers");
  const authored = rivers.learningOutcomes.find((outcome) => outcome.id === "geo-rivers-s1");

  assert.ok(authored.authored);
  assert.ok(authored.notes.length >= 4);
  assert.ok(authored.notes.some((note) => Array.isArray(note.points) && note.points.length));
  assert.ok(authored.keyTerms.length > 0);
  assert.equal(authored.keyTerms[0].section, authored.title);
  assert.ok(authored.questions.length > 0, "authored practice questions are attached");

  const review = rivers.learningOutcomes[0];
  assert.ok(!review.notes.some((note) => note.h === "Chapter overview and connections"),
    "the generated overview must not sit alongside authored notes");
  assert.ok(review.questions.length >= 3, "existing chapter test questions stay on the review outcome");

  const untouched = chapters.find((chapter) => chapter.id === "geo-glaciation");
  assert.equal(untouched.learningOutcomes[0].notes[0].h, "Chapter overview and connections",
    "chapters without authored notes keep the generated notes for now");
});

test("the build rejects notes that break the standard", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "notes-bad-"));
  const good = JSON.parse(fs.readFileSync(path.join(fixtures, "geo-rivers-s1.json"), "utf8"));
  good.notes[0].points.push("These ideas should be used together in an answer.");
  good.notes[1].points.push(good.notes[0].points[0]);
  good.notes[2].h = "**Drainage patterns**";
  fs.writeFileSync(path.join(dir, "geo-rivers-s1.json"), JSON.stringify(good));
  fs.writeFileSync(path.join(dir, "geo-rivers-1.json"), JSON.stringify({ ...good, loId: "geo-rivers-1" }));

  const result = build(["--check", "--content", dir]);
  assert.notEqual(result.status, 0);
  assert.match(result.stdout, /filler/);
  assert.match(result.stdout, /repeats/);
  assert.match(result.stdout, /markdown/);
  assert.match(result.stdout, /subsections \(-s1, -s2/);
});

test("the shipped geography notes file is up to date with content/geography", () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "notes-")), "geography-notes.js");
  const result = build(["--out", out]);
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.equal(
    fs.readFileSync(out, "utf8"),
    fs.readFileSync(path.join(root, "geography-notes.js"), "utf8"),
    "run: python3 scripts/build_notes.py geography"
  );
});
