// Checks the CAO points scoring in points-calculator.js (the public points calculator page).

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const context = {};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.resolve(__dirname, "..", "points-calculator.js"), "utf8"), context);
const { score, rowPoints } = context.BBPoints;

const H = (subject, grade) => ({ subject, level: "H", grade: String(grade) });
const O = (subject, grade) => ({ subject, level: "O", grade: String(grade) });

test("common points scale values", () => {
  assert.deepEqual([1, 2, 3, 4, 5, 6, 7, 8].map((g) => rowPoints(H("English", g)).total), [100, 88, 77, 66, 56, 46, 37, 0]);
  assert.deepEqual([1, 2, 3, 4, 5, 6, 7, 8].map((g) => rowPoints(O("English", g)).total), [56, 46, 37, 28, 20, 12, 0, 0]);
  assert.equal(rowPoints({ subject: "Mathematics", level: "F", grade: "1" }).total, 20);
  assert.equal(rowPoints({ subject: "Mathematics", level: "F", grade: "2" }).total, 12);
  assert.equal(rowPoints({ subject: "Mathematics", level: "F", grade: "3" }).total, 0);
  assert.equal(rowPoints({ subject: "LCVP Link Modules", grade: "D" }).total, 66);
  assert.equal(rowPoints({ subject: "LCVP Link Modules", grade: "M" }).total, 46);
  assert.equal(rowPoints({ subject: "LCVP Link Modules", grade: "P" }).total, 28);
});

test("ungraded rows and Foundation for non-Maths subjects score nothing", () => {
  assert.equal(rowPoints(H("English", "")), null);
  assert.equal(rowPoints({ subject: "Irish", level: "F", grade: "1" }), null);
});

test("Higher Maths bonus: +25 for H1 to H6 only", () => {
  assert.equal(rowPoints(H("Mathematics", 1)).total, 125);
  assert.equal(rowPoints(H("Mathematics", 6)).total, 71);
  assert.equal(rowPoints(H("Mathematics", 7)).total, 37);
  assert.equal(rowPoints(O("Mathematics", 1)).total, 56);
  assert.equal(rowPoints(H("Applied Mathematics", 1)).total, 100);
});

test("maximum is 625", () => {
  const rows = ["English", "Irish", "Mathematics", "French", "Biology", "Chemistry", "Physics"].map((s) => H(s, 1));
  assert.equal(score(rows).total, 625);
});

test("only the best six count", () => {
  const rows = [H("English", 1), H("Irish", 2), H("French", 3), H("Biology", 4), H("Chemistry", 5), H("Physics", 6), H("History", 7)];
  const r = score(rows);
  assert.equal(r.total, 100 + 88 + 77 + 66 + 56 + 46);
  assert.equal(r.status[6].state, "dropped");
  assert.equal(r.counted.length, 6);
});

test("the bonus pulls H6 Maths into the best six (worked example on the page)", () => {
  const others = [H("English", 2), H("Irish", 2), H("French", 3), H("Biology", 3), H("Chemistry", 4), H("History", 5)];
  const r = score([...others, H("Mathematics", 6)]);
  assert.equal(r.total, 467);
  assert.equal(r.bonus, 25);
  assert.equal(r.status[5].state, "dropped"); // the H5
  assert.equal(r.status[6].state, "counted");
});

test("the bonus doesn't count when Maths misses the best six", () => {
  const rows = ["English", "Irish", "French", "Biology", "Chemistry", "Physics"].map((s) => H(s, 1));
  const r = score([...rows, H("Mathematics", 6)]);
  assert.equal(r.total, 600);
  assert.equal(r.bonus, 0);
});

test("a subject entered twice counts once, at its better result", () => {
  const r = score([H("English", 3), O("English", 1), H("Irish", 1)]);
  assert.equal(r.total, 77 + 100);
  assert.equal(r.status[1].state, "duplicate");
});

test("fewer than six graded subjects still add up", () => {
  const r = score([H("English", 1), { subject: "", level: "H", grade: "" }, O("Irish", 1)]);
  assert.equal(r.total, 156);
  assert.equal(r.status[1].state, "empty");
});

// ---------------------------------------------------------------- national grade ranking

const statsContext = { };
statsContext.window = statsContext;
vm.createContext(statsContext);
for (const f of ["grade-stats.js", "points-calculator.js"]) {
  vm.runInContext(fs.readFileSync(path.resolve(__dirname, "..", f), "utf8"), statsContext);
}
const STATS = statsContext.BB_GRADE_STATS;
const { rank, rankLabel } = statsContext.BBPoints;

test("grade-stats.js matches the SEC CSV it was built from", () => {
  const csv = fs.readFileSync(path.resolve(__dirname, "..", "data/sec-statistics/lc-2026-provisional-national.csv"), "utf8")
    .trim().split("\n").slice(1).map((l) => l.split(","));
  let checked = 0;
  for (const [, , level, , total, ...p] of csv) {
    const lv = { A: "H", G: "O", B: "F" }[level];
    const found = Object.values(STATS.subjects).find((s) => s[lv] && s[lv].n === Number(total) && s[lv].p.join() === p.map(Number).join());
    assert.ok(found, `missing row ${level} ${total}`);
    checked++;
  }
  assert.equal(checked, 86);
  assert.equal(STATS.year, 2026);
});

test("every subject in the stats is pickable in the calculator", () => {
  const src = fs.readFileSync(path.resolve(__dirname, "..", "points-calculator.js"), "utf8");
  for (const name of Object.keys(STATS.subjects)) {
    assert.ok(src.includes(`"${name}"`) || name === "Mathematics", `${name} is not in the subject list`);
  }
});

test("rank: Higher Biology H2 is the top 29.1%", () => {
  const r = rank(H("Biology", 2), STATS);
  assert.equal(r.top, 29.1);
  assert.equal(r.got, 16);
  assert.equal(r.n, 33046);
  assert.equal(rankLabel(r), "Top 29%");
});

test("rank: weaker grades say who you're ahead of", () => {
  const r = rank(H("Biology", 6), STATS); // 13.1+16+14.6+14.2+13.8+12.6 = 84.3
  assert.equal(r.top, 84.3);
  assert.equal(rankLabel(r), "Ahead of 16%");
});

test("rank: an H1 always reads as top, even in subjects where most get one", () => {
  assert.equal(rankLabel(rank(H("Mandarin Chinese", 1), STATS)), "Top 90%");
});

test("rank: Foundation Maths uses the Foundation figures; no data means no rank", () => {
  assert.equal(rank({ subject: "Mathematics", level: "F", grade: "1" }, STATS).n, 3781);
  assert.equal(rank({ subject: "LCVP Link Modules", grade: "D" }, STATS), null);
  assert.equal(rank(H("Ancient Greek", 1), STATS), null);
  assert.equal(rank(H("", 1), STATS), null);
  assert.equal(rank(H("Biology", ""), STATS), null);
});
