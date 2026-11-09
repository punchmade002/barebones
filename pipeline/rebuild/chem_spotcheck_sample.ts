// Write spot-check batches: per paper, a deterministic sample of kept and written parts.
// deno run -A pipeline/rebuild/chem_spotcheck_sample.ts [keptPerPaper=6] [writtenPerPaper=3]
const A = "pipeline/_data/rebuild/chemistry-audit";
const KEPT = Number(Deno.args[0] ?? 6), WRITTEN = Number(Deno.args[1] ?? 3);
const w: any = {}; new Function("window", await Deno.readTextFile("chemistry-exam-questions.js"))(w);
const db = w.EXAM_QUESTIONS_DB;
const byPaper: Record<string, any[]> = {};
db.forEach((q: any, qi: number) => q.parts.forEach((p: any, pi: number) => {
  if (p.answerStatus === "flagged") return;
  (byPaper[`${q.year}-${q.level}`] ??= []).push({ qi, pi, status: p.answerStatus, qref: p.qref, question: p.question, marks: p.marks, model: p.model });
}));
// deterministic spread: every k-th item
const spread = (a: any[], n: number) => a.length <= n ? a : Array.from({ length: n }, (_, i) => a[Math.floor((i + 0.5) * a.length / n)]);
await Deno.mkdir(`${A}/spotcheck`, { recursive: true });
for (const f of Deno.readDirSync(`${A}/spotcheck`)) Deno.removeSync(`${A}/spotcheck/${f.name}`);
const names: string[] = []; let total = 0;
Object.keys(byPaper).sort().forEach((k, i) => {
  const items = spread(byPaper[k].filter(x => x.status === "kept"), KEPT).concat(spread(byPaper[k].filter(x => x.status === "written"), WRITTEN));
  const name = `s${i + 1}_${k}`; names.push(name); total += items.length;
  Deno.writeTextFileSync(`${A}/spotcheck/${name}.json`, JSON.stringify(items.map(({ status, ...x }) => x), null, 1));
});
console.log(JSON.stringify(names)); console.error("batches", names.length, "items", total);
