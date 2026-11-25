// Export one subject's Crunch levels for the app (see CRUNCH_MODE.md, "Crunch Mode in the app").
//
//   deno run -A scripts/crunch_export.js biology     # → biology-crunch.js
//
// Each note point gets the written-paper level at which it is first hidden: it is kept while the student needs
// more than that on the written paper. The levels come from the Crunch map's scoring and year-by-year backtest
// (drafts/crunch/<subject>/map/crunch-score.js) at the map's default settings, so the app agrees with the map.
// The app works out the written paper needed from the target grade and the expected AAC result.
// Each point also carries its study time in minutes: words at STUDY_WPM of active learning (read, understand,
// recall), x1.5 for points rated long or complex. Biology's notes come to about 134 hours this way.
const ROOT = new URL("../", import.meta.url).pathname;
await import(ROOT + "drafts/crunch/biology/map/crunch-score.js");

const subject = Deno.args[0];
const STUDY_WPM = 40;
const P = { decay: 0.65, helpW: 0.5, gapE: 0.75, gapH: 0.35, halfLife: 8, newShare: 0.1, choice: true, exact: 0.5 };
const D = JSON.parse(await Deno.readTextFile(`${ROOT}drafts/crunch/${subject}/map/data.json`));
// Subjects with optional parts (Geography's elective, option and region; History's topics) get a course per
// combination of picks, and a point's level differs a little between them. The app can't ship every combination
// (History has 225), so each point takes the mean of its level over every combination that includes it.
// shortcut: averaged levels, error measured below against exact runs; upgrade to per-combination levels (or live
// scoring in a worker) if that error grows.
const PICK_COUNTS = { history: { ire: 2, eur: 2 } }; // how many tracks a student picks per kind (default 1)
const KIND_LABELS = {
  geography: { elective: "Elective", option: "Option", region: "Region" },
  history: { ire: "Irish topics", eur: "European topics" },
};
const hasPicks = D.picks && Object.keys(D.picks).length;
const choose = (arr, k) => (k === 0 ? [[]] : arr.flatMap((x, i) => choose(arr.slice(i + 1), k - 1).map((rest) => [x, ...rest])));
const combos = !hasPicks ? [null] : Object.entries(D.picks).reduce((acc, [kind, opts]) => {
  const k = PICK_COUNTS[subject]?.[kind] || 1;
  const choices = choose(opts.map(([t]) => t), k).map((c) => (k === 1 ? c[0] : c));
  return acc.flatMap((picks) => choices.map((c) => ({ ...picks, [kind]: c })));
}, [{}]);
const levelSum = new Map(), levelN = new Map();
let years = [];
const runs = [];
const started = performance.now();
for (const picks of combos) {
  const C = picks ? crunchCourse(D, picks) : D;
  const R = crunchScore(C, P), bt = crunchBacktest(C, P);
  years = bt.years;
  const exact = new Map();
  C.items.forEach((item, i) => {
    const v = bt.safe(R.y[i]);
    exact.set(item[0], v);
    levelSum.set(item[0], (levelSum.get(item[0]) || 0) + v);
    levelN.set(item[0], (levelN.get(item[0]) || 0) + 1);
  });
  runs.push([picks, C.items, exact]);
  if (combos.length > 1 && runs.length % 25 === 0) console.log(`  ${runs.length} of ${combos.length} courses scored (${Math.round((performance.now() - started) / 1000)} s)`);
}
// {subsection: {"block.point": [level, minutes]}}, "b" = the block's paragraph. Both to 0.1.
const levels = {};
const minutesOf = ([, , cost, text]) => (text.split(/\s+/).filter(Boolean).length / STUDY_WPM) * (cost === 2 ? 1.5 : 1);
D.items.forEach((item) => {
  if (!levelN.get(item[0])) return;
  const id = item[0], [sid, rest] = [id.slice(0, id.indexOf(".")), id.slice(id.indexOf(".") + 1)];
  // item[4], when present, is a study time worked out upstream (Maths: from the skill's lesson pack)
  (levels[sid] ||= {})[rest] = [Math.round((10 * levelSum.get(id)) / levelN.get(id)) / 10, Math.max(0.1, Math.round(10 * (item[4] ?? minutesOf(item))) / 10)];
});
// Which pick each subsection belongs to, and the choices the app offers
const tracks = {}, picks = {};
if (hasPicks) {
  D.items.forEach((r) => { const t = D.subs[r[1]][5]; if (t) tracks[r[0].slice(0, r[0].indexOf("."))] = t; });
  for (const [kind, opts] of Object.entries(D.picks)) picks[kind] = { label: KIND_LABELS[subject]?.[kind] || kind, count: PICK_COUNTS[subject]?.[kind] || 1, options: opts };
}
// Each course shifts the scale a little, so it also gets a correction curve: 21 matched quantiles mapping the
// averaged levels onto its exact ones. The app looks it up by the student's picks (crunchPickKey) and interpolates.
const pickKey = (p) => Object.values(p).flat().sort().join("|");
const QS = 20;
const quantile = (sorted, q) => sorted[Math.min(sorted.length - 1, Math.round(q * (sorted.length - 1)))];
const curves = {};
const mean = (id) => levelSum.get(id) / levelN.get(id);
const interp = (x, xs, ys) => {
  if (x <= xs[0]) return ys[0] + (x - xs[0]);
  if (x >= xs[xs.length - 1]) return ys[ys.length - 1] + (x - xs[xs.length - 1]);
  let i = 1; while (xs[i] < x) i++;
  return xs[i] === xs[i - 1] ? ys[i] : ys[i - 1] + ((x - xs[i - 1]) * (ys[i] - ys[i - 1])) / (xs[i] - xs[i - 1]);
};
if (combos.length > 1) {
  let worstAvg = 0, sumAvg = 0, worst = 0, sum = 0;
  for (const [p, items, exact] of runs) {
    const a = items.map((r) => mean(r[0])).sort((x, y) => x - y), e = items.map((r) => exact.get(r[0])).sort((x, y) => x - y);
    const xs = [], ys = [];
    for (let q = 0; q <= QS; q++) { xs.push(Math.round(10 * quantile(a, q / QS)) / 10); ys.push(Math.round(10 * quantile(e, q / QS)) / 10); }
    curves[pickKey(p)] = [xs, ys];
    const cost = items.reduce((t, r) => t + r[2], 0);
    const cutBy = (lv) => (100 * items.reduce((t, r) => t + (lv(r[0]) >= 72 ? r[2] : 0), 0)) / cost;
    const truth = cutBy((id) => exact.get(id));
    const errAvg = Math.abs(truth - cutBy(mean)), err = Math.abs(truth - cutBy((id) => interp(mean(id), xs, ys)));
    worstAvg = Math.max(worstAvg, errAvg); sumAvg += errAvg; worst = Math.max(worst, err); sum += err;
  }
  console.log(`${combos.length} courses, cut at written 72% vs exact: averaged ${(sumAvg / runs.length).toFixed(1)} pts off on average (${worstAvg.toFixed(1)} worst); with each course's curve ${(sum / runs.length).toFixed(1)} (${worst.toFixed(1)} worst)`);
}
// Flashcards are each subsection's key terms, not note points, so each card takes the level of the note point that
// teaches it: the point (with its block heading) sharing the most words with the card, the term's words counting
// triple. A card no point matches gets null and is never crunched.
const STOP = new Set("the and for are that this with from into its their they them than then also which what when where while been being have has had was were will can not but all any each other such these those more most some only very used use uses using one two how why does".split(" "));
const words = (t) => new Set((String(t).toLowerCase().match(/[a-z0-9]+/g) || []).filter((w) => w.length > 2 && !STOP.has(w)));
const shared = (a, b) => { let n = 0; for (const w of a) if (b.has(w)) n++; return n; };
const cards = {};
let matched = 0, unmatched = 0;
for (const sid of Object.keys(levels)) {
  let content;
  try { content = JSON.parse(await Deno.readTextFile(`${ROOT}content/${subject}/${sid}.json`)); } catch { continue; }
  if (!(content.keyTerms || []).length) continue;
  const pts = [];
  (content.notes || []).forEach((block, bi) => {
    if (block.b && String(block.b).trim()) pts.push([`${bi}.b`, words(`${block.h || ""} ${block.b}`)]);
    (block.points || []).forEach((pt, pi) => { if (String(pt).trim()) pts.push([`${bi}.${pi}`, words(`${block.h || ""} ${pt}`)]); });
  });
  // keyed by the card's term (lower case): some subjects' app flashcards aren't the content file's key terms in order
  cards[sid] = Object.fromEntries(content.keyTerms.map((kt) => {
    const term = words(kt.term), def = words(kt.definition);
    let best = null, bestScore = 0;
    for (const [key, pw] of pts) {
      if (!levels[sid][key]) continue;
      const score = 3 * shared(term, pw) + shared(def, pw);
      if (score > bestScore) { bestScore = score; best = key; }
    }
    best ? matched++ : unmatched++;
    return [String(kt.term).trim().toLowerCase(), best ? levels[sid][best][0] : null];
  }));
}
const out = { subject, aac: D.aac || null, years, studyWpm: STUDY_WPM, levels, cards, ...(hasPicks ? { tracks, picks, curves } : {}) };
const js = `// Generated by scripts/crunch_export.js. Do not edit by hand.\n// Crunch Mode: the written-paper level at which each note point (and flashcard) is hidden.\n` +
  `(window.CRUNCH = window.CRUNCH || {})[${JSON.stringify(subject)}] = ${JSON.stringify(out)};\n`;
await Deno.writeTextFile(`${ROOT}${subject}-crunch.js`, js);

// self-check: the share of study effort hidden at a few targets matches the map's numbers
const cost = D.items.map(r => r[2]), total = cost.reduce((a, b) => a + b, 0);
const cut = need => Math.round(100 - (100 * D.items.reduce((a, r, i) => a + (levels[r[0].split(".")[0]][r[0].slice(r[0].indexOf(".") + 1)][0] < need ? cost[i] : 0), 0)) / total);
console.log(`${subject}: ${D.items.length} points → ${subject}-crunch.js (${Math.round(js.length / 1024)} KB); written 88/72/55/38% cuts ${[88, 72, 55, 38].map(cut).join(" / ")}%`);
const hours = Object.values(levels).flatMap(Object.values).reduce((a, [, m]) => a + m, 0) / 60;
console.log(`study time for all notes: ${hours.toFixed(0)} h at ${STUDY_WPM} words a minute`);
console.log(`flashcards: ${matched} matched to a note point, ${unmatched} unmatched (never crunched)`);
