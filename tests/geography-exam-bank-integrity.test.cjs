// Regression tests for the geography exam bank.
//
// Each assertion below corresponds to a defect class that was measured in the
// geography bank on 2 September 2026 and then fixed. They are cheap, run over
// 100% of the bank, and exist so that a future pipeline run cannot reintroduce
// any of them silently.
//
//   defect                                         before   after
//   part with no model answer at all                  154        0
//   answer describing a method instead of answering   106        0
//   answer lifted from marking-scheme scaffolding       7        0
//   bare letter sequence with no mapping given         45        0
//   answer written for a different question            38        0
//   two parts of one question sharing an answer         1        0
//   paper question filed under an ambiguous label     119        0
//   unreferenced full-page scan on disk               280        0
//   crop whose top edge cuts through a line of text   187       43
//
// The crop figures are geometry, not judgement: "ink touching the top edge" is
// a screen, and after the rebuild most of what it flags is a chart border or an
// attribution line sitting legitimately close to the edge. The test below caps
// it at the measured level so a regression would show up, and no lower.

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
  for (const file of ["exam-questions-db.js", "geography-exam-questions.js"]) {
    const source = fs.readFileSync(path.join(root, file), "utf8");
    // exam-questions-db.js ends by indexing against COURSE_DATA, which we do not load here.
    vm.runInContext(source.replace(/\n\(function \(\) \{[\s\S]*$/, "\n"), context, { filename: file });
  }
  return context.EXAM_QUESTIONS_DB.filter((q) => q.subject === "geography");
}

const questions = loadExamBank();
const parts = questions.flatMap((q) => q.parts.map((p, i) => ({ q, p, i })));

// An answer that tells you how to approach the question instead of answering it.
const METHOD_ONLY = /^\s*(WORKED METHOD|Worked method|CASE \d+ - WORKED)/;
// Marking schemes say "Two valid countries" where the candidate supplies the content.
const SCHEME_SCAFFOLD = /^(any |two |three |four |one )?(valid|named|correct|relevant|suitable|appropriate|stated|identified)\b/i;
// "C, A, D, B" is the scheme's shorthand; on its own it tells a student nothing.
const BARE_LETTER_SEQUENCE = /^[A-Z](,\s*[A-Z]){1,5}\.?$/;

function report(label, offenders) {
  const sample = offenders.slice(0, 5).map(({ q, p }) => `${q.id} [${p.label || "-"}]`);
  return `${offenders.length} part(s) with ${label}: ${sample.join(", ")}${offenders.length > 5 ? ", …" : ""}`;
}

test("every part carries a model answer", () => {
  const bad = parts.filter(({ p }) => !String(p.model || "").trim());
  assert.equal(bad.length, 0, report("no model answer", bad));
});

test("no answer describes a method instead of answering the question", () => {
  const bad = parts.filter(({ p }) => METHOD_ONLY.test(p.model || ""));
  assert.equal(bad.length, 0, report("a method-only answer", bad));
});

test("no answer is marking-scheme scaffolding", () => {
  const bad = parts.filter(({ p }) => SCHEME_SCAFFOLD.test(String(p.model || "").trim()));
  assert.equal(bad.length, 0, report("an answer lifted from scheme scaffolding", bad));
});

test("a matching answer gives the mapping, not just the letters", () => {
  const bad = parts.filter(({ p }) => BARE_LETTER_SEQUENCE.test(String(p.model || "").trim()));
  assert.equal(bad.length, 0, report("a bare letter sequence", bad));
});

test("no long answer is reused verbatim under another question", () => {
  const seen = new Map();
  const duplicates = [];
  for (const { q, p } of parts) {
    const key = String(p.model || "").trim();
    if (key.length < 400) continue; // short factual answers, and shared essay material, legitimately repeat
    if (seen.has(key)) duplicates.push({ q, p });
    else seen.set(key, q.id);
  }
  assert.equal(duplicates.length, 0, report("a long answer reused verbatim elsewhere", duplicates));
});

test("no two parts of the same question share an answer", () => {
  // Caught a real defect: part (i) "What will the ratio be in 2024?" was carrying
  // part (ii)'s answer, so both parts of the question said the same thing.
  const duplicates = [];
  for (const q of questions) {
    const seen = new Map();
    for (const p of q.parts) {
      const key = String(p.model || "").trim();
      if (key.length < 80) continue;
      if (seen.has(key)) duplicates.push({ q, p });
      else seen.set(key, p.label);
    }
  }
  assert.equal(duplicates.length, 0, report("an answer shared with another part of the same question", duplicates));
});

test("every question text is a readable question", () => {
  const bad = parts.filter(({ p }) => String(p.question || "").replace(/[^A-Za-z]/g, "").length < 10);
  assert.equal(bad.length, 0, report("empty or fragment question text", bad));
});

test("question text carries no page furniture", () => {
  const FURNITURE = [/continues on the next page/i, /do not write|blank page/i, /Acknowledge?ments/i, /https?:\/\//];
  const bad = parts.filter(({ p }) => FURNITURE.some((rx) => rx.test(p.question || "")));
  assert.equal(bad.length, 0, report("page furniture in the question text", bad));
});

test("every referenced diagram exists on disk", () => {
  const bad = parts.filter(({ p }) => p.diagram && !fs.existsSync(path.join(root, p.diagram)));
  assert.equal(bad.length, 0, report("a missing diagram file", bad));
});

test("no diagram is an uncropped full page", () => {
  // The source papers render at 1310x1853 at the zoom the crops use, so a diagram
  // anywhere near that tall is the whole scanned page rather than a crop of the figure.
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
    return height >= 1200 && width >= 1200;
  });
  assert.equal(bad.length, 0, report("an uncropped full-page diagram", bad));
});

test("no unreferenced image is left in the geography image directory", () => {
  const referenced = new Set(parts.map(({ p }) => p.diagram).filter(Boolean).map((d) => path.basename(d)));
  const dir = path.join(root, "exam-images", "geography");
  const orphans = fs.readdirSync(dir).filter((f) => !referenced.has(f));
  assert.equal(orphans.length, 0, `${orphans.length} unreferenced image(s): ${orphans.slice(0, 5).join(", ")}`);
});

test("every paper question carries a label that identifies it uniquely", () => {
  const seen = new Map();
  const duplicates = [];
  for (const q of questions) {
    if (seen.has(q.source)) duplicates.push(`${q.source} (${seen.get(q.source)} and ${q.id})`);
    else seen.set(q.source, q.id);
  }
  assert.equal(duplicates.length, 0, `ambiguous source labels: ${duplicates.slice(0, 5).join("; ")}`);
});

test("the bank still covers every paper it is meant to", () => {
  const papers = new Set(
    questions.map((q) => {
      const m = /LC Geography (Higher|Ordinary) (\d{4})(?: (Paper \d|Part (?:One|Two)))?/.exec(q.source);
      return `${m[2]}-${m[1]}-${m[3] || ""}`;
    })
  );
  assert.ok(papers.size >= 30, `expected at least 30 paper slots, found ${papers.size}`);
  assert.ok(questions.length >= 715, `expected at least 715 questions, found ${questions.length}`);
  assert.ok(parts.length >= 1930, `expected at least 1930 parts, found ${parts.length}`);
});
