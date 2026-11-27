const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// Crunch's slider (app.js): cut the least-needed points until the chosen share of study time is gone,
// and report the paper mark what's left is worth.
const src = fs.readFileSync(path.join(__dirname, "..", "app.js"), "utf8");
const grab = (from, to) => { const i = src.indexOf(from); return src.slice(i, src.indexOf(to, i)); };
const context = {};
vm.runInNewContext(`${grab("const crunchMarkGrade", "\n")}
${grab("function crunchPicks", "\n\n// The cut and what it leaves")}
this.api = { crunchAt, crunchMaxCut, crunchCutOf, crunchMarkGrade };`, context);
const { crunchAt, crunchMaxCut, crunchCutOf, crunchMarkGrade } = context.api;

// Ten 6-minute points with levels 100, 90, ..., 10: each is 10% of the study time
const data = { subject: "t", levels: { s1: Object.fromEntries([100, 90, 80, 70, 60, 50, 40, 30, 20, 10].map((l, i) => [`0.${i}`, [l, 6]])) } };

test("no cut keeps everything", () => {
  assert.equal(crunchAt(data, { cut: 0 }).mark, Infinity);
});

test("a cut drops the least-needed points first", () => {
  assert.deepEqual({ ...crunchAt(data, { cut: 30 }) }, { mark: 80, cut: 30 });
  assert.equal(crunchAt(data, { cut: 50 }).mark, 60);
});

test("the slider stops before the mark falls under 30%", () => {
  assert.equal(crunchMaxCut(data, {}), 80);
  assert.equal(crunchCutOf(data, { cut: 95 }), 80);
});

test("grades follow the paper mark", () => {
  assert.deepEqual([100, 90, 89.9, 30, 29, 0].map(crunchMarkGrade), ["H1", "H1", "H2", "H7", "H8", "H8"]);
});
