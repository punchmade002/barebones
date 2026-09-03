const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const appSource = fs.readFileSync(path.join(root, "app.js"), "utf8");

function mathsBank() {
  const context = { window: {}, COURSE_DATA: { chapters: [] } };
  vm.createContext(context);
  vm.runInContext(
    fs.readFileSync(path.join(root, "exam-questions-db.js"), "utf8"),
    context,
    { filename: "exam-questions-db.js" }
  );
  return context.window.EXAM_QUESTIONS_DB.filter((question) => question.subject === "maths");
}

function parserHarness() {
  const parserStart = appSource.indexOf("function parseMathsWorkedSolution");
  const guideStart = appSource.indexOf("function mathsGuideForStep", parserStart);
  const normaliserStart = appSource.indexOf("function normaliseMathsSolution", guideStart);
  assert.ok(parserStart > -1 && guideStart > parserStart && normaliserStart > guideStart);

  const context = {};
  vm.createContext(context);
  vm.runInContext(
    `${appSource.slice(parserStart, guideStart)}\n${appSource.slice(guideStart, normaliserStart)}`,
    context,
    { filename: "maths-worked-solution-functions.js" }
  );
  return context;
}

test("every Maths answer becomes a complete line-by-line solution", () => {
  const { parseMathsWorkedSolution } = parserHarness();
  const parts = mathsBank().flatMap((question) => question.parts);

  assert.equal(parts.length, 160);
  for (const part of parts) {
    const parsed = parseMathsWorkedSolution(part.model);
    assert.ok(parsed.steps.length > 0, `${part.label} must have at least one step`);
    assert.ok(parsed.steps.every((step) => step.title && step.work));
    assert.ok(parsed.finalAnswer, `${part.label} must retain its final answer`);
  }
});

test("the explorer preserves the detailed polynomial example", () => {
  const { parseMathsWorkedSolution, mathsGuideForStep } = parserHarness();
  const firstPart = mathsBank()[0].parts[0];
  const parsed = parseMathsWorkedSolution(firstPart.model);

  assert.equal(parsed.steps.length, 7);
  assert.equal(parsed.steps[0].title, "Use the given factor");
  assert.match(parsed.steps[1].work, /4x³ ÷ 2x = 2x²/);
  assert.match(parsed.finalAnswer, /x = −3\/2/);
  assert.equal(mathsGuideForStep(parsed.steps[1]).rule, "Algebraic division");
});

test("both exam views share the Maths renderer and accessible controls", () => {
  assert.equal(
    appSource.match(/\$\{renderExamAnswer\(group, part, partId\)\}/g)?.length,
    2
  );
  assert.match(appSource, /class="maths-step" tabindex="0" role="button" aria-pressed="false"/);
  assert.match(appSource, /document\.addEventListener\("pointerup", handleMathsSolutionSelection\)/);
  assert.match(appSource, /data-show-label="\$\{showLabel\}"/);
});

test("step explanations open inline without an empty explanation margin", () => {
  assert.match(appSource, /stepElement\.insertAdjacentElement\("afterend", panel\)/);
  assert.match(appSource, /class="maths-explanation-panel" aria-live="polite" hidden/);
  assert.doesNotMatch(appSource, /maths-panel-empty-mark/);
  assert.doesNotMatch(appSource, /Explanation margin/);
  assert.doesNotMatch(appSource, /maths-explanation-open/);
});
