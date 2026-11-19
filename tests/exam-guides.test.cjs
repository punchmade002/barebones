const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const SUBJECTS = ["biology", "business", "chemistry", "geography", "history", "home-economics", "maths", "pe",
  "english", "irish", "french", "spanish", "construction-studies", "art", "physics"];

// The Paper guide data, loaded in app.html's order (later files replace earlier entries)
const context = {};
context.window = context;
vm.createContext(context);
const html = fs.readFileSync(path.join(root, "app.html"), "utf8");
for (const [, file] of html.matchAll(/<script (?:defer )?src="\.\/([\w-]*exam-(?:info|breakdown)\.js)/g)) {
  vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context, { filename: file });
}
const guides = context.EXAM_BREAKDOWN;

// Mirrors inBreakdownSection in app.js
const inSection = (q, s) => (s.bank
  ? s.bank.some((b) => b.sectionId === q.sectionId && (!b.numbers || b.numbers.includes(q.questionNumber)))
  : q.sectionId === s.id);

const toMinutes = (t) => Number(t.split(":")[0]) * 60 + Number(t.split(":")[1]);

for (const id of SUBJECTS) {
  test(`${id} has a full Paper guide`, () => {
    const g = guides[id];
    assert.ok(g?.sections?.length, "needs sections");
    assert.ok(g.timingNote && g.totalMarks && g.totalMinutes);
    const day = g.examDay;
    assert.ok(day?.task, "needs an exam-day summary");
    assert.equal(day.facts.length, 4, "four key rules");
    const end = day.timeline.reduce((t, b) => {
      assert.equal(toMinutes(b.start), t, `${b.label} starts when the block before it ends`);
      return t + b.minutes;
    }, toMinutes(day.timeline[0].start));
    assert.equal(toMinutes(day.end), end);
    for (const s of g.sections) {
      assert.ok(s.tips?.timing && s.tips.structure && s.tips.reminders.length, `${s.name}: tips`);
      assert.ok(s.questionTypes?.length, `${s.name}: question types`);
      for (const qt of s.questionTypes) {
        for (const key of ["name", "where", "see", "marked", "play"]) assert.ok(qt[key], `${s.name} › ${qt.name}: ${key}`);
        assert.ok(qt.traps?.length, `${s.name} › ${qt.name}: traps`);
      }
    }
    // New copy follows the house style: no em dashes
    assert.doesNotMatch(JSON.stringify(g), /—/);
  });

  const bankFile = path.join(root, `${id}-exam-questions.js`);
  if (!fs.existsSync(bankFile)) continue;
  test(`every ${id} past-paper question belongs to a guide section`, () => {
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(fs.readFileSync(bankFile, "utf8"), ctx);
    const lost = ctx.window.EXAM_QUESTIONS_DB.filter((q) => !guides[id].sections.some((s) => inSection(q, s)));
    assert.equal(lost.length, 0, `${lost.length} match no section, e.g. ${lost.slice(0, 3).map((q) => q.id).join(", ")}`);
  });
}
