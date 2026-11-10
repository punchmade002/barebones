// PE exam bank, rebuilt to the Biology blueprint (pipeline/EXAM_BANK_REBUILD.md): questions ship
// as crops of the original paper, every answer was written against the marking scheme (short
// answers by Haiku with a Sonnet sample check, long answers by Sonnet with every one checked), and
// each part is tagged with its exact paper question. As in Chemistry, off-spec parts (Topics 7
// and 8, Adventure Activities) keep a reference answer and stay tagged offSpec.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function rebuiltBank() {
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(root, "pe-exam-questions.js"), "utf8"), context);
  return context.window.EXAM_QUESTIONS_DB;
}

const bank = rebuiltBank();
const parts = bank.flatMap((q) => q.parts.map((p) => ({ q, p })));
const shipped = parts.filter(({ p }) => p.model);
const SECTION_MARKS = { "pe-sectionA": 8, "pe-sectionB": 50, "pe-sectionC": 40 };

function report(label, offenders) {
  const sample = offenders.slice(0, 5).map(({ q, p }) => `${q.id} [${p.label || "-"}]`);
  return `${offenders.length} part(s) with ${label}: ${sample.join(", ")}${offenders.length > 5 ? ", …" : ""}`;
}

test("rebuilt PE questions ship as paper crops, never as transcribed text", () => {
  assert.equal(bank.length, 180, "18 questions on each of the 10 papers");
  for (const q of bank) {
    assert.ok(q.images.length > 0, `${q.id} has no crops`);
    q.images.forEach((src) => assert.ok(fs.existsSync(path.join(root, src)), `${src} must exist`));
    for (const part of q.parts) {
      assert.ok(!("question" in part) && !("text" in part), `${q.id} ${part.label} ships question text`);
    }
  }
});

test("every question is tagged with its exact paper, level, number and section", () => {
  const ids = new Set();
  for (const q of bank) {
    assert.ok(!ids.has(q.id), `duplicate id ${q.id}`);
    ids.add(q.id);
    assert.match(q.id, /^pe-pp-\d{4}-(higher|ordinary)-q\d+$/);
    assert.equal(q.id, `pe-pp-${q.year}-${q.level}-q${q.questionNumber}`);
    const section = q.questionNumber <= 12 ? "A" : q.questionNumber === 13 ? "B" : "C";
    assert.equal(q.sectionId, `pe-section${section}`, `${q.id} section`);
    assert.equal(q.legacy, false, `${q.id}: 2022-2026 papers are set on the current (2018) specification`);
  }
  const papers = new Set(bank.map((q) => `${q.year}-${q.level}`));
  for (let y = 2022; y <= 2026; y++) {
    for (const level of ["higher", "ordinary"]) assert.ok(papers.has(`${y}-${level}`), `no ${level} ${y} paper`);
  }
});

test("part labels are the paper's own: (a), (a)(i) or blank for an unlettered question", () => {
  for (const q of bank) {
    const labels = q.parts.map((p) => p.label);
    assert.equal(new Set(labels).size, labels.length, `${q.id} repeats a label`);
    labels.forEach((l) => assert.match(l, /^(\([a-z]+\))*$/, `${q.id} label ${JSON.stringify(l)}`));
    if (labels.includes("")) assert.equal(labels.length, 1, `${q.id}: a blank label must be the only part`);
  }
});

test("part marks add up to the scheme's question total", () => {
  for (const q of bank) {
    assert.equal(q.totalMarks, SECTION_MARKS[q.sectionId], `${q.id} total`);
    const sum = q.parts.reduce((s, p) => s + (p.marks || 0), 0);
    assert.ok(Math.abs(sum - q.totalMarks) < 0.5, `${q.id}: parts sum to ${sum}, not ${q.totalMarks}`);
  }
});

test("only checked answers ship, and disputed parts carry none", () => {
  for (const { q, p } of parts) {
    const has = ["written", "kept"].includes(p.answerStatus);
    assert.equal(Boolean(p.model), has, `${q.id} ${p.label}: answer/status mismatch`);
    assert.ok(["kept", "written", "flagged"].includes(p.answerStatus), `${q.id} ${p.label}: ${p.answerStatus}`);
    if (has) assert.ok(p.notesRefs.length > 0, `${q.id} ${p.label} cites no notes`);
  }
  const flagged = parts.filter(({ p }) => p.answerStatus === "flagged");
  assert.ok(flagged.length <= parts.length * 0.03, report("no shipped answer (over 3%)", flagged));
});

test("answers read like a student's, not a marking scheme", () => {
  // Examiner phrasing only: PE prose legitimately says "socially accepted", "allow a player to
  // grip", "a free throw awarded after a foul" or "judges deduct marks for".
  const NOTATION = [
    /\(\s*\d{1,2}\s*(?:marks?)?\s*\)(?!\s*[\w(×])/i,
    /\/\//,
    /\[\s*(accept|allow)|\b(accept|allow)\s*:/i,
    /also (acceptable|accepted|correct)|would also (work|be accepted)/i,
    /\bcandidates?\b|\baward(?:ed)?\s+\d+\s*marks?\b|\bmarking scheme\b/i,
    /\*\*/,
  ];
  const bad = shipped.filter(({ p }) => NOTATION.some((rx) => rx.test(p.model)));
  assert.equal(bad.length, 0, report("examiner notation or markdown", bad));
});

test("answers are distinct — an answer written for one part is not reused under another", () => {
  const seen = new Set();
  const duplicates = [];
  for (const { q, p } of shipped) {
    const key = p.model.trim();
    if (key.length < 60) continue; // short factual answers legitimately repeat
    if (seen.has(key)) duplicates.push({ q, p });
    else seen.add(key);
  }
  assert.equal(duplicates.length, 0, report("an answer reused verbatim elsewhere", duplicates));
});
