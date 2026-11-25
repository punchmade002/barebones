// Tune one subject's Crunch exam settings on its own past papers (see CRUNCH_MODE.md, "Per-subject tuning").
//
//   deno run -A scripts/crunch_tune.js biology            # → content/crunch/biology-tuning.json
//
// Rolling backtest: for each year Y (after the first 5 papers), cut using only papers before Y, then mark the
// paper of year Y the 2027 way. Score = average real mark across study budgets (keep 5%, 10% … 60% of the
// study effort), averaged over years: the most marks for the least study. Every pair on the grid is tried.
// Only settings past papers can judge are tuned: exact and halfLife. Not tuned:
// - decay, helpW, gapE, gapH: about how students learn, which old papers can't measure.
// - newShare: in a backtest, "new" means "not asked yet", and those subsections mostly stay unasked, so the
//   backtest always says 0. Real new-course content is on the 2027 syllabus, which is a different thing.
// The tuned pair is kept only if it beats the defaults by 2 standard errors across the test years; otherwise
// the subject's papers can't tell them apart and the defaults stay.
const ROOT = new URL("../", import.meta.url).pathname;
await import(ROOT + "drafts/crunch/biology/map/crunch-score.js");

const subject = Deno.args[0];
// one representative course per subject with picks (tuning on every pick combination would cost 8-36x)
const PICKS = {
  geography: { elective: "elective:economic", option: "option:global-interdependence", region: "region:geo-region-continental-s1" },
  history: { ire: ["ire:hist-ire2", "ire:hist-ire3"], eur: ["eur:hist-eur3", "eur:hist-eur4"] },
};
const BASE = { decay: 0.65, helpW: 0.5, gapE: 0.75, gapH: 0.35, halfLife: 8, newShare: 0.1, choice: true, exact: 0.5 };
const GRID = { exact: [0, 0.25, 0.5, 0.75, 1], halfLife: [2, 4, 8, 16, 50] };
const BUDGETS = [5, 10, 15, 20, 25, 30, 40, 50, 60];

let F = JSON.parse(await Deno.readTextFile(`${ROOT}drafts/crunch/${subject}/map/data.json`));
const D = PICKS[subject] ? crunchCourse(F, PICKS[subject]) : F;
const years = D.papers.map(p => p.year).sort((a, b) => a - b);
const testYears = years.slice(5);
const cost = D.items.map(r => r[2]), total = cost.reduce((a, b) => a + b, 0);

// Train sets don't depend on the settings, so build them once.
const folds = testYears.map(Y => ({
  test: D.papers.find(p => p.year === Y),
  train: { ...D, papers: D.papers.filter(p => p.year < Y), subs: D.subs.map(s => [s[0], s[1], s[2], s[3], s[4].filter(y => y < Y), s[5]]) },
}));

// per-year score: mean real mark (%) over the budgets, keeping the points the cut values most (lowest y first)
function foldScores(P) {
  return folds.map(({ train, test }) => {
    const r = crunchScore(train, P);
    const idx = [...cost.keys()].sort((a, b) => r.y[a] - r.y[b] || r.order[a] - r.order[b]);
    let s = 0;
    for (const b of BUDGETS) {
      const kept = new Uint8Array(cost.length);
      let c = 0;
      for (const i of idx) { if (c + cost[i] > (b / 100) * total) break; kept[i] = 1; c += cost[i]; }
      s += 100 * crunchRealScore(test, kept, P.choice, D);
    }
    return s / BUDGETS.length;
  });
}
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
const sd = a => Math.sqrt(mean(a.map(x => (x - mean(a)) ** 2)));

const t0 = performance.now();
const base = foldScores(BASE);
console.log(`${subject}: ${D.items.length} points, ${years.length} papers, test years ${testYears.join(" ")} (${Math.round(performance.now() - t0)} ms per setting)`);
console.log(`  Biology defaults: ${mean(base).toFixed(2)}% average real mark over budgets`);

let best = BASE, bestS = base;
const table = {};
for (const exact of GRID.exact) for (const halfLife of GRID.halfLife) {
  const P = { ...BASE, exact, halfLife }, s = (exact === BASE.exact && halfLife === BASE.halfLife) ? base : foldScores(P);
  table[`${exact}/${halfLife}`] = +mean(s).toFixed(2);
  if (mean(s) > mean(bestS) + 1e-9) { best = P; bestS = s; }
}
// paired comparison with the defaults, year by year: is the gain bigger than year-to-year noise?
const diff = bestS.map((s, i) => s - base[i]), se = sd(diff) / Math.sqrt(diff.length);
const adopt = mean(diff) >= 2 * se && mean(diff) > 0;
const use = adopt ? best : BASE;
const out = { subject, exact: use.exact, halfLife: use.halfLife,
  adopted: adopt, best: { exact: best.exact, halfLife: best.halfLife, score: +mean(bestS).toFixed(2) },
  defaultScore: +mean(base).toFixed(2), gain: +mean(diff).toFixed(2), gainSE: +se.toFixed(2),
  testYears, budgets: BUDGETS, picks: PICKS[subject] || null, grid: table, tuned: new Date().toISOString().slice(0, 10) };
console.log(`  best: exact ${best.exact}, half-life ${best.halfLife}: ${out.best.score}% (gain ${out.gain} ± ${out.gainSE} per year) → ${adopt ? "adopted" : "within noise, defaults kept"}`);
for (const e of GRID.exact) console.log(`  exact ${String(e).padEnd(4)}`, GRID.halfLife.map(h => `hl${h}: ${table[`${e}/${h}`].toFixed(2)}`).join("  "));
await Deno.writeTextFile(`${ROOT}content/crunch/${subject}-tuning.json`, JSON.stringify(out, null, 1) + "\n");
