// Integrity tests for the chemistry exam bank after the Nov 2026 answer audit.
//
// Every model answer was audited against the official marking scheme by two
// independent Haiku agents; any part either flagged went to Sonnet, whose rewrite
// (or decision to keep the original) was re-checked by Haiku against the scheme.
// Each part is tagged with the exact paper question it answers (qref), its audit
// outcome (answerStatus) and the number of full-marks scheme points.
// Scripts: pipeline/rebuild/chem_audit_{packets.ts,workflow.js,merge.ts}.

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const context = {};
context.window = context;
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root, "chemistry-exam-questions.js"), "utf8"), context);
const questions = context.EXAM_QUESTIONS_DB;
const parts = questions.flatMap((q) => q.parts.map((p, i) => ({ q, p, i })));

function report(label, offenders) {
  const sample = offenders.slice(0, 5).map(({ q, p }) => `${q.id} [${p ? p.label : "-"}]`);
  return `${offenders.length} with ${label}: ${sample.join(", ")}${offenders.length > 5 ? ", …" : ""}`;
}

test("the bank keeps every question and part", () => {
  assert.equal(questions.length, 617);
  assert.equal(parts.length, 3701);
});

test("question ids are unique", () => {
  const seen = new Map();
  for (const q of questions) seen.set(q.id, (seen.get(q.id) || 0) + 1);
  const dups = [...seen].filter(([, n]) => n > 1).map(([id]) => id);
  assert.deepEqual(dups, []);
});

test("every question is tagged with its level and question number", () => {
  const bad = questions.filter((q) => !["higher", "ordinary"].includes(q.level) || !Number.isInteger(q.questionNumber) || q.questionNumber < 1 || q.questionNumber > 11);
  assert.equal(bad.length, 0, report("no level/questionNumber", bad.map((q) => ({ q }))));
});

test("every part is audited and tagged with the exact question it answers", () => {
  const bad = parts.filter(({ p }) => !["kept", "written", "flagged"].includes(p.answerStatus) || typeof p.qref !== "string" || !Number.isInteger(p.scheme_points));
  assert.equal(bad.length, 0, report("no audit tag", bad));
});

test("each part's tag matches its question's year, level and number", () => {
  const bad = parts.filter(({ q, p }) => {
    const m = /^(\d{4}) (Higher|Ordinary) Q(\d+)(\(.+\))$/.exec(p.qref || "");
    return !m || Number(m[1]) !== q.year || m[2].toLowerCase() !== q.level || Number(m[3]) !== q.questionNumber;
  });
  assert.equal(bad.length, 0, report("a qref that disagrees with its question", bad));
});

test("every part carries a model answer", () => {
  const bad = parts.filter(({ p }) => !String(p.model || "").trim());
  assert.equal(bad.length, 0, report("no model answer", bad));
});

test("rewritten answers carry no examiner notation", () => {
  const bad = parts.filter(({ p }) => p.model_source === "audit-rewrite" && /\[accept|\(\d+ marks?\)|\(\d+ ?× ?\d+\)/i.test(p.model));
  assert.equal(bad.length, 0, report("examiner notation in a rewrite", bad));
});
