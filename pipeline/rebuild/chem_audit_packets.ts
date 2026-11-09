// Build Haiku audit packets for the chemistry exam bank: one packet per paper chunk.
// deno run -A pipeline/rebuild/chem_audit_packets.ts
const A = "pipeline/_data/rebuild/chemistry-audit";
const src = await Deno.readTextFile("chemistry-exam-questions.js");
const w: any = {}; new Function("window", src)(w);
const db = w.EXAM_QUESTIONS_DB;
const exists = (p: string) => { try { Deno.statSync(p); return true; } catch { return false; } };
const papers: Record<string, any[]> = {};
db.forEach((q: any, qi: number) => {
  const level = /Higher/i.test(q.source) ? "higher" : "ordinary";
  (papers[`${q.year}-${level}`] ??= []).push({ qi, q });
});
const MAX = 40; const index: any[] = [];
for (const [key, qs] of Object.entries(papers).sort()) {
  const [year, level] = key.split("-");
  const ref = Number(year) === 2001 ? "-REF" : "";
  const paperTxt = `${A}/text/${year}-${level}-EV-papers${ref}.txt`;
  const schemeTxt = `${A}/text/${year}-${level}-EV-scheme${ref}.txt`;
  const pngDir = `${A}/scheme-png/${year}-${level}-EV-scheme${ref}`;
  const scheme = exists(pngDir) ? { kind: "images", path: pngDir } : exists(schemeTxt) ? { kind: "text", path: schemeTxt } : { kind: "none" };
  let chunk: any[] = [], n = 0, ci = 0;
  const flush = () => {
    if (!chunk.length) return;
    const name = `${key}-${++ci}`;
    const packet = { packet: name, year: Number(year), level, paperText: paperTxt, scheme, entries: chunk };
    Deno.writeTextFileSync(`${A}/packets/${name}.json`, JSON.stringify(packet, null, 1));
    index.push({ name, year: Number(year), level, parts: n, scheme: scheme.kind });
    chunk = []; n = 0;
  };
  for (const { qi, q } of qs) {
    if (n && n + q.parts.length > MAX) flush();
    chunk.push({ qi, id: q.id, source: q.source, parts: q.parts.map((p: any, pi: number) => ({ pi, label: p.label, question: p.question, marks: p.marks, model: p.model })) });
    n += q.parts.length;
  }
  flush();
}
Deno.writeTextFileSync(`${A}/packets/index.json`, JSON.stringify(index, null, 1));
const h1 = index.filter(p => p.year <= 2012), h2 = index.filter(p => p.year > 2012);
const sum = (a: any[]) => a.reduce((s, p) => s + p.parts, 0);
console.log("packets", index.length, "half1", h1.length, sum(h1), "half2", h2.length, sum(h2));
console.log(index.filter(p => p.scheme !== "text").map(p => p.name + ":" + p.scheme).join(" "));
