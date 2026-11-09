// Build audit packets for the chemistry exam bank: one packet per (chapter group x paper),
// never splitting a question, at most MAX parts each.
// deno run -A pipeline/rebuild/chem_audit_packets.ts
const A = "pipeline/_data/rebuild/chemistry-audit";
const GROUPS: string[][] = [
  ["chem1", "chem2"], ["chem3", "chem4", "chem5"], ["chem6", "chem7", "chem8"], ["chem9", "chem10", "chem11"],
  ["chem12", "chem14"], ["chem15", "chem17"], ["chem18", "chem19", "chem20"], ["chem21", "chem22", "chem23"],
  ["chem24", "chem25", "chem26"],
];
const HALF1 = new Set([0, 1, 2, 3, 4]);
const MAX = 30;
const src = await Deno.readTextFile("chemistry-exam-questions.js");
const w: any = {}; new Function("window", src)(w);
const db = w.EXAM_QUESTIONS_DB;
const exists = (p: string) => { try { Deno.statSync(p); return true; } catch { return false; } };
const groupOf = (ch: string) => GROUPS.findIndex(g => g.includes(ch));
for (const f of Deno.readDirSync(`${A}/packets`)) Deno.removeSync(`${A}/packets/${f.name}`);
const buckets: Record<string, any[]> = {};
db.forEach((q: any, qi: number) => {
  const gi = groupOf(q.chapterId); if (gi < 0) throw new Error("no group for " + q.chapterId);
  const level = /Higher/i.test(q.source) ? "higher" : "ordinary";
  (buckets[`g${gi + 1}|${q.year}-${level}`] ??= []).push({ qi, q });
});
const half1: Record<string, string> = {}, half2: Record<string, string> = {};
const paperInfo = (year: string, level: string) => {
  const ref = Number(year) === 2001 ? "-REF" : "";
  const schemeTxt = `${A}/text/${year}-${level}-EV-scheme${ref}.txt`;
  const pngDir = `${A}/scheme-png/${year}-${level}-EV-scheme${ref}`;
  const scheme = exists(pngDir) ? { kind: "images", path: pngDir } : exists(schemeTxt) ? { kind: "text", path: schemeTxt } : { kind: "none" };
  return { year: Number(year), level, paperText: `${A}/text/${year}-${level}-EV-papers${ref}.txt`, scheme };
};
const MIN = 15, MAXPAPERS = 3;
for (let gi = 0; gi < GROUPS.length; gi++) {
  const g = `g${gi + 1}`;
  const papers = Object.keys(buckets).filter(k => k.startsWith(g + "|")).map(k => k.split("|")[1]).sort();
  let chunk: any[] = [], n = 0, pset: string[] = [], ci = 0;
  const flush = () => {
    if (!chunk.length) return;
    const name = `${g}-${++ci}-${pset.map(p => p.replace(/-(h|o)\w+$/, "$1")).join("_")}`;
    const packet = { packet: name, chapters: GROUPS[gi], papers: pset.map(p => ({ key: p, ...paperInfo(...(p.split("-") as [string, string])) })), entries: chunk };
    Deno.writeTextFileSync(`${A}/packets/${name}.json`, JSON.stringify(packet, null, 1));
    const counts = chunk.map(e => `${e.qi}:${e.parts.length}`).join(",");
    (HALF1.has(gi) ? half1 : half2)[name] = counts;
    chunk = []; n = 0; pset = [];
  };
  for (const pk of papers) {
    const qs = buckets[`${g}|${pk}`];
    const pn = qs.reduce((s: number, x: any) => s + x.q.parts.length, 0);
    if (n && (n + pn > MAX || pset.length >= MAXPAPERS || n >= MIN)) flush();
    // a single paper bigger than MAX is split on question boundaries
    for (const { qi, q } of qs) {
      if (n && n + q.parts.length > MAX) flush();
      if (!pset.includes(pk)) pset.push(pk);
      chunk.push({ qi, id: q.id, source: q.source, paper: pk, chapterId: q.chapterId, parts: q.parts.map((p: any, pi: number) => ({ pi, label: p.label, question: p.question, marks: p.marks, model: p.model })) });
      n += q.parts.length;
    }
  }
  flush();
}
Deno.writeTextFileSync(`${A}/half1-min.json`, JSON.stringify(half1));
Deno.writeTextFileSync(`${A}/half2-min.json`, JSON.stringify(half2));
const tot = (m: Record<string, string>) => Object.values(m).reduce((s, v) => s + v.split(",").reduce((a, x) => a + Number(x.split(":")[1]), 0), 0);
console.log("half1 packets", Object.keys(half1).length, "parts", tot(half1), "| half2 packets", Object.keys(half2).length, "parts", tot(half2));
console.log("args bytes", JSON.stringify(half1).length, JSON.stringify(half2).length);
