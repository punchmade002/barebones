// Regression tests for the PE exam bank.
//
// Each assertion below corresponds to a defect class that was measured in the PE bank
// on 1 September 2026 and then fixed. They are cheap, run over 100% of the bank, and
// exist so that a future pipeline run cannot reintroduce any of them silently.
//
//   defect                                    before   after
//   recycled template answer                     571        0
//   answer citing a non-existent part            398        0
//   generic non-answer                            87        0
//   question text carrying page furniture        302        0
//   two questions merged into one part            38        0
//   question text empty or a bare fragment        32        0
//   distinct model answers (of 543 parts)          35      543

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function loadExamBank() {
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  for (const file of ["exam-questions-db.js", "pe-exam-questions.js"]) {
    const source = fs.readFileSync(path.join(root, file), "utf8");
    // exam-questions-db.js ends by indexing against COURSE_DATA, which we do not load here.
    vm.runInContext(source.replace(/\n\(function \(\) \{[\s\S]*$/, "\n"), context, { filename: file });
  }
  return context.EXAM_QUESTIONS_DB.filter((q) => q.subject === "pe");
}

const questions = loadExamBank();
const parts = questions.flatMap((q) => q.parts.map((p, i) => ({ q, p, i })));

// Furniture the segmenter strips: running headers, page numbers, printed answer lines,
// and the "(40 marks)" heading that belongs to the question rather than to a part.
const FURNITURE = [
  /continues on the next page/i,
  /(^|\n)\s*\d{1,3}\s*(\n|$)/,
  /do not write|blank page/i,
  /^\s*\(\d+\s*marks?\)\s*[()a-zi\s]*$/i,
  /\n\s*\d\.\s*(\n|$)/,
];
// A second "Question N" heading at the start of a line means a neighbouring question was
// swept into this part. A mid-line "in Question 13 (a) (i)" is a legitimate cross-reference.
const MERGED = /(?:^|\n)\s*Question\s+\d{1,2}\b/;
const TEMPLATE_TAIL = /This addresses the requirement in part \d+/;
const GENERIC_STEM = /^Use the relevant Leaving Certificate/;

function report(label, offenders) {
  const sample = offenders.slice(0, 5).map(({ q, p }) => `${q.id} [${p.label || "-"}]`);
  return `${offenders.length} part(s) with ${label}: ${sample.join(", ")}${offenders.length > 5 ? ", …" : ""}`;
}

test("every part carries a model answer", () => {
  const bad = parts.filter(({ p }) => !String(p.model || "").trim());
  assert.equal(bad.length, 0, report("no model answer", bad));
});

test("no answer is recycled from a template pool", () => {
  const bad = parts.filter(({ p }) => TEMPLATE_TAIL.test(p.model || "") || GENERIC_STEM.test(p.model || ""));
  assert.equal(bad.length, 0, report("a templated or generic answer", bad));
});

test("answers are distinct — an answer written for one question is not reused under another", () => {
  const seen = new Map();
  const duplicates = [];
  for (const { q, p } of parts) {
    const key = String(p.model || "").trim();
    if (key.length < 60) continue; // short factual answers legitimately repeat
    if (seen.has(key)) duplicates.push({ q, p });
    else seen.set(key, q.id);
  }
  assert.equal(duplicates.length, 0, report("an answer reused verbatim elsewhere", duplicates));
});

test("question text carries no page furniture", () => {
  const bad = parts.filter(({ p }) => FURNITURE.some((rx) => rx.test(p.question || "")));
  assert.equal(bad.length, 0, report("page furniture in the question text", bad));
});

test("no part contains a second question", () => {
  const bad = parts.filter(({ p }) => MERGED.test(String(p.question || "").slice(15)));
  assert.equal(bad.length, 0, report("a merged neighbouring question", bad));
});

test("every question text is a readable question", () => {
  const bad = parts.filter(({ p }) => String(p.question || "").replace(/[^A-Za-z]/g, "").length < 10);
  assert.equal(bad.length, 0, report("empty or fragment question text", bad));
});

test("every referenced diagram exists on disk", () => {
  const bad = parts.filter(({ p }) => p.diagram && !fs.existsSync(path.join(root, p.diagram)));
  assert.equal(bad.length, 0, report("a missing diagram file", bad));
});

test("no diagram is an uncropped full page", () => {
  // The source papers render at 1241x1755 at the zoom the crops use, so a diagram anywhere
  // near that tall is the whole scanned page rather than a crop of the figure on it.
  const pngSize = (file) => {
    const head = Buffer.alloc(24);
    const fd = fs.openSync(file, "r");
    fs.readSync(fd, head, 0, 24, 0);
    fs.closeSync(fd);
    return { width: head.readUInt32BE(16), height: head.readUInt32BE(20) };
  };
  const bad = parts.filter(({ p }) => {
    if (!p.diagram) return false;
    const { width, height } = pngSize(path.join(root, p.diagram));
    return height >= 1200 || width >= 1200;
  });
  assert.equal(bad.length, 0, report("an uncropped full-page diagram", bad));
});

test("part marks sum to the marks available for the section", () => {
  const expected = { "pe-section-a": 8, "pe-section-b": 50, "pe-section-c": 40 };
  const bad = questions.filter((q) => {
    const target = expected[q.sectionId];
    if (!target) return false;
    return q.parts.reduce((sum, p) => sum + (p.marks || 0), 0) !== target;
  });
  assert.equal(bad.length, 0, `${bad.length} question(s) whose part marks do not sum correctly: ${bad.slice(0, 5).map((q) => q.id).join(", ")}`);
});

test("no question is filed twice against the same paper", () => {
  const seen = new Map();
  const duplicates = [];
  for (const q of questions) {
    const key = `${q.source}`;
    if (seen.has(key)) duplicates.push(q.id);
    else seen.set(key, q.id);
  }
  assert.equal(duplicates.length, 0, `duplicate paper questions: ${duplicates.join(", ")}`);
});

test("the bank still covers every paper it is meant to", () => {
  const papers = new Set(questions.map((q) => `${q.year}-${/Higher/.test(q.source) ? "HL" : "OL"}`));
  assert.equal(papers.size, 10, `expected 10 papers, found ${[...papers].sort().join(", ")}`);
  assert.ok(questions.length >= 155, `expected at least 155 questions, found ${questions.length}`);
  assert.ok(parts.length >= 530, `expected at least 530 parts, found ${parts.length}`);
});
