const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const context = {};
context.window = context;
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root, "aac-guides.js"), "utf8"), context);
const guides = context.AAC_GUIDES;

// One guide per coursework or oral component; Maths and English have none. A subject's second component is
// keyed "<subject>-<part>" (PE's Performance Assessment, Home Economics' Textiles).
const EXPECTED = ["biology", "chemistry", "business", "geography", "history", "home-economics", "home-economics-textiles", "pe", "pe-performance",
  "irish", "french", "spanish", "construction-studies", "construction-studies-practical", "art", "art-practical", "physics"];

test("every subject with an AAC has a guide", () => {
  assert.deepEqual(Object.keys(guides).sort(), [...EXPECTED].sort());
});

for (const id of EXPECTED) {
  test(`${id} AAC guide is complete`, () => {
    const g = guides[id];
    assert.equal(g.subject, id.replace(/-(textiles|performance|practical)$/, ""));
    // Two guides in one subject show as two tiles, named by their short titles
    if (EXPECTED.some((other) => other !== id && guides[other]?.subject === g.subject)) assert.ok(g.short, "needs a short tile name");
    for (const key of ["title", "subjectTitle", "weight", "level", "summary"]) assert.ok(g[key], `${key} missing`);
    assert.ok(g.brief?.task && g.brief.facts.length >= 3, "needs the year's brief: task and key facts");
    assert.ok(g.brief.facts.some(([k]) => /due/i.test(k)), "the brief states when the work is due");
    assert.match(g.brief.source.url, /^https:\/\//);
    // The guide screen links this PDF; rebuild with scripts/build_aac_ai_guides.py after editing guides
    const pdf = path.join(root, "aac-ai-guides", `${id}.pdf`);
    assert.ok(fs.existsSync(pdf), "AI review guide PDF missing");
    assert.ok(fs.statSync(pdf).mtimeMs >= fs.statSync(path.join(root, "aac-guides.js")).mtimeMs - 1000, "AI review guide PDF is older than aac-guides.js");
    assert.ok(g.sources.length >= 4, "pool at least four sources");
    g.sources.forEach((s) => assert.match(s.url, /^https:\/\//));
    assert.ok(g.stages.length >= 3 && g.stages.length <= 7, "3-7 stages fit the panel layout");

    const steps = g.stages.flatMap((s) => s.checklist);
    assert.ok(steps.length <= 16, `checklist should be minimal, got ${steps.length}`);
    assert.equal(new Set(steps).size, steps.length, "checklist steps double as tick keys, so must be unique");
    g.stages.forEach((s) => {
      assert.ok(s.name && s.checklist.length, `${s.name}: needs checklist steps`);
      const points = s.guide.reduce((n, sec) => n + sec.points.length, 0);
      assert.ok(points >= 5, `${s.name}: full guide too thin (${points} points)`);
    });
    // Stage marks, when given for every stage, must add up to the component total
    if (g.marks && g.stages.every((s) => s.marks)) {
      assert.equal(g.stages.reduce((n, s) => n + s.marks, 0), g.marks);
    }
  });
}
