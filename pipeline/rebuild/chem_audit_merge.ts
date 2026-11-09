// Apply chem-answer-audit workflow results to chemistry-exam-questions.js.
// deno run -A pipeline/rebuild/chem_audit_merge.ts <workflow-output.json> [...]
// Idempotent per part: a part is (qi, pi) in the bank's original order, which this script never changes.
const BANK = Deno.env.get("BANK") ?? "chemistry-exam-questions.js";
const A = Deno.env.get("AUDIT_DIR") ?? "pipeline/_data/rebuild/chemistry-audit";
const REVIEW = Deno.env.get("REVIEW_DIR") ?? "pipeline/_data/rebuild-review";

const src = await Deno.readTextFile(BANK);
const header = src.slice(0, src.indexOf("window.EXAM_QUESTIONS_DB"));
const w: any = {}; new Function("window", src)(w);
const db: any[] = w.EXAM_QUESTIONS_DB;
const before = JSON.stringify(db.map(q => [q.id, q.parts.length]));

const key = (v: any) => `${v.qi}:${v.pi}`;
const cleanLabel = (l: string) => { l = (l || "").replace(/\s+/g, ""); return l && !l.startsWith("(") ? `(${l.replace(/^\(?/, "").replace(/\)?$/, "")})` : l; };
const cleanNum = (n: any) => String(n ?? "").replace(/\D/g, "");

const log: any[] = [], review: any[] = [];
let kept = 0, written = 0, flagged = 0, marksFixed = 0, questionsFixed = 0;
const qnVotes: Record<number, string[]> = {};

for (const file of Deno.args) {
  const out = JSON.parse(await Deno.readTextFile(file));
  const results = (out.result ?? out).results;
  for (const r of results) {
    const A_ = new Map(r.A.map((v: any) => [key(v), v])), B_ = new Map(r.B.map((v: any) => [key(v), v]));
    const flaggedKeys = new Set(r.flagged);
    const allKeys = new Set([...A_.keys(), ...B_.keys(), ...flaggedKeys]) as Set<string>;
    for (const k of allKeys) {
      const [qi, pi] = k.split(":").map(Number);
      const q = db[qi], p = q?.parts?.[pi];
      if (!p) { console.warn("no part", k, r.pk); continue; }
      const va: any = A_.get(k), vb: any = B_.get(k);
      let status: string, qn: string, label: string, points: string[], note = "";
      if (!flaggedKeys.has(k)) {
        status = "kept"; qn = va.questionNumber; label = va.partLabel; points = va.schemePoints;
      } else {
        // latest round that mentions this part decides
        let last: any = null, check: any = null, firstRewrite: any = null;
        for (const rd of r.rounds) {
          const it = rd.items.find((i: any) => key(i) === k);
          if (it) { last = it; check = rd.checks.find((c: any) => key(c) === k) ?? null; if (it.action === "rewrite") firstRewrite ??= it; }
        }
        qn = last?.questionNumber || va?.questionNumber || vb?.questionNumber; label = last?.partLabel || va?.partLabel || vb?.partLabel;
        points = last?.schemePoints?.length ? last.schemePoints : (va?.schemePoints || vb?.schemePoints || []);
        if (last && check?.pass && last.action === "rewrite") { status = "written"; }
        else if (last && check?.pass && last.action === "keep") { status = "kept"; }
        else {
          status = "flagged";
          note = check?.issue || (last ? `action ${last.action}: ${last.note}` : "no rewrite returned");
          // best attempt: the latest Sonnet rewrite, since the stored answer was judged wrong
        }
        if (last?.action === "rewrite" && last.model) {
          p.model_prev = p.model_prev ?? p.model;
          p.model = last.model.trim();
          p.model_source = "audit-rewrite";
        }
        if (last?.question && last.question.trim() && last.question.trim() !== p.question) {
          p.question_prev = p.question_prev ?? p.question; p.question = last.question.trim(); questionsFixed++;
        }
        if (status === "flagged") review.push({ id: q.id, qi, pi, source: q.source, label: p.label, question: p.question, model: p.model, issue: note,
          auditA: va?.reason, auditB: vb?.reason });
      }
      // marks: change only when both auditors read the same, different figure off the scheme
      if (va?.schemeMarks && vb?.schemeMarks && va.schemeMarks === vb.schemeMarks && va.schemeMarks !== p.marks) {
        p.marks_prev = p.marks_prev ?? p.marks; p.marks = va.schemeMarks; marksFixed++;
      }
      const level = /Higher/i.test(q.source) ? "Higher" : "Ordinary";
      qn = cleanNum(qn); label = cleanLabel(label);
      p.qref = `${q.year} ${level} Q${qn}${label}`;
      p.answerStatus = status;
      p.scheme_points = Array.isArray(points) ? points.length : 0;
      (qnVotes[qi] ??= []).push(qn);
      status === "kept" ? kept++ : status === "written" ? written++ : flagged++;
      log.push({ qi, pi, id: q.id, qref: p.qref, status, schemePoints: points, auditA: va && { v: va.verdict, r: va.reason }, auditB: vb && { v: vb.verdict, r: vb.reason }, note });
    }
  }
}

// question-level tags
for (const [qi, votes] of Object.entries(qnVotes)) {
  const q = db[Number(qi)];
  const counts: Record<string, number> = {}; votes.filter(Boolean).forEach(v => counts[v] = (counts[v] || 0) + 1);
  const best = Object.entries(counts).sort((a, b) => b[1] - a[1])[0]?.[0];
  q.level = /Higher/i.test(q.source) ? "higher" : "ordinary";
  if (best) q.questionNumber = Number(best);
}
// ids must be unique (2001 stored each Q1 item as its own group under one id)
const seen: Record<string, number> = {};
for (const q of db) seen[q.id] = (seen[q.id] || 0) + 1;
const dupFixed: string[] = [];
for (const q of db) {
  if (seen[q.id] > 1 && q.parts[0]?.qref) {
    const lab = (q.parts[0]?.qref || "").replace(/^.*Q\d+/, "").replace(/[()]/g, "");
    const nid = `chemistry-pp-${q.year}-${/Higher/.test(q.source) ? "HI" : "OR"}-Q${q.questionNumber ?? ""}${lab ? "-" + lab : ""}`;
    let uid = nid, n = 2; while (db.some(o => o !== q && o.id === uid)) uid = `${nid}-${n++}`;
    dupFixed.push(`${q.id} -> ${uid}`); q.id_prev = q.id_prev ?? q.id; q.id = uid;
  }
}
const ids = new Set(db.map(q => q.id));
if (ids.size !== db.length) console.warn("WARNING duplicate ids remain:", db.length - ids.size);
if (JSON.stringify(db.map(q => q.parts.length)) !== JSON.stringify(JSON.parse(before).map((x: any) => x[1]))) throw new Error("part counts changed");

// shipped file: drop the *_prev fields (kept in the audit log instead)
const prev = db.map((q, qi) => ({ qi, id_prev: q.id_prev, parts: q.parts.map((p: any) => ({ model_prev: p.model_prev, question_prev: p.question_prev, marks_prev: p.marks_prev })) }));
const prevFile = `${A}/prev-values.json`;
let prevStore: any = {}; try { prevStore = JSON.parse(await Deno.readTextFile(prevFile)); } catch { /* first run */ }
prev.forEach(x => { x.parts.forEach((pp: any, pi: number) => { for (const [k, v] of Object.entries(pp)) if (v !== undefined) (prevStore[`${x.qi}:${pi}`] ??= {})[k] ??= v; }); if (x.id_prev) (prevStore[`${x.qi}`] ??= {}).id_prev ??= x.id_prev; });
await Deno.writeTextFile(prevFile, JSON.stringify(prevStore, null, 1));
const shipped = db.map(q => { const { id_prev, ...rest } = q; return { ...rest, parts: q.parts.map((p: any) => { const { model_prev, question_prev, marks_prev, ...pr } = p; return pr; }) }; });
await Deno.writeTextFile(BANK, `${header}window.EXAM_QUESTIONS_DB = (window.EXAM_QUESTIONS_DB || []).concat(\n${JSON.stringify(shipped, null, 2)}\n);\n`);

// logs
const stamp = Deno.args.map(f => f.split("/").pop()).join("+");
await Deno.mkdir(REVIEW, { recursive: true });
const logFile = `${A}/audit-log.json`;
let prevLog: any[] = []; try { prevLog = JSON.parse(await Deno.readTextFile(logFile)); } catch { /* first */ }
const merged = new Map(prevLog.map((x: any) => [key(x), x])); log.forEach(x => merged.set(key(x), x));
await Deno.writeTextFile(logFile, JSON.stringify([...merged.values()], null, 1));
const revFile = `${REVIEW}/chemistry-audit-review.json`;
let prevRev: any[] = []; try { prevRev = JSON.parse(await Deno.readTextFile(revFile)); } catch { /* first */ }
const revMap = new Map(prevRev.map((x: any) => [key(x), x]));
log.forEach(x => revMap.delete(key(x))); review.forEach(x => revMap.set(key(x), x));
await Deno.writeTextFile(revFile, JSON.stringify([...revMap.values()], null, 1));
console.log(`merged ${stamp}: parts ${log.length} | kept ${kept} | written ${written} | flagged ${flagged} | question text fixed ${questionsFixed} | marks fixed ${marksFixed}`);
console.log(`audit log ${merged.size} parts total; review list ${revMap.size}`);
if (dupFixed.length) console.log("ids fixed:\n " + dupFixed.join("\n "));
