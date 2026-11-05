// Checks the whole-paper archive that scripts/build_exam_papers.py writes: exam-papers.js holds
// one summary per subject (loaded with the app) and each subject's list sits in
// exam-papers/<subject>/papers.js (loaded when its archive is opened).

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function load(files) {
  const context = {};
  context.window = context;
  vm.createContext(context);
  for (const file of files) vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context);
  return context;
}

const summaries = load(["exam-papers.js"]).EXAM_PAPERS;

test("the app loads only a summary per subject, not the paper lists", () => {
  assert.ok(Object.keys(summaries).length > 0);
  for (const [subject, summary] of Object.entries(summaries)) {
    assert.deepEqual(Object.keys(summary).sort(),
      ["course", "firstExamined", "from", "list", "papers", "to"], subject);
    assert.match(summary.list, new RegExp(`^exam-papers/${subject}/papers\\.js\\?v=[0-9a-f]{8}$`));
  }
});

for (const [subject, summary] of Object.entries(summaries)) {
  test(`${subject}: the list matches its summary and every file is there`, () => {
    const listFile = summary.list.split("?")[0];
    const papers = load([listFile]).EXAM_PAPER_LISTS[subject];
    assert.ok(Array.isArray(papers) && papers.length, "list is empty");

    const years = papers.map((p) => p.year);
    assert.equal(Math.min(...years), summary.from);
    assert.equal(Math.max(...years), summary.to);
    assert.equal(papers.filter((p) => p.kind === "papers").length, summary.papers);

    const files = new Set();
    for (const p of papers) {
      assert.ok(["papers", "scheme"].includes(p.kind), p.file);
      assert.ok(["higher", "ordinary", "foundation", "common"].includes(p.level), p.file);
      assert.equal(p.oldCourse, p.year < summary.firstExamined, p.file);
      assert.ok(!files.has(p.file), `listed twice: ${p.file}`);
      files.add(p.file);
      const stat = fs.statSync(path.join(root, p.file));
      assert.ok(stat.size > 1000, `missing or empty: ${p.file}`);
    }

    // Nothing in the folder that the list doesn't show
    const onDisk = fs.readdirSync(path.join(root, "exam-papers", subject)).filter((f) => f.endsWith(".pdf"));
    assert.deepEqual(onDisk.map((f) => `exam-papers/${subject}/${f}`).sort(), [...files].sort());
  });
}
