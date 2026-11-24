// Crunch Mode scoring (see CRUNCH_MODE.md). Plain script: defines globalThis.crunchScore.
// D = data.json from scripts/crunch_map.py.
// P = {decay, helpW, gapE, gapH, halfLife, newShare (null = its share of the course), choice (true/false)}.
//
// Exam value: every Higher Level past paper is re-marked as if set in the 2027 format. Old Section A is the
// compulsory Q1 (1/6 of the paper); old Sections B and C are the optional questions, of which the student
// answers 5 in 6 and drops the ones they're least prepared for. Papers are weighted by recency (half-life in
// years). Subsections the old papers never tested (new-course content) are assumed to carry course-average
// marks, newShare of the paper. Without D.papers, every point carries the same share.
(function () {
  function scc(N, needs) {
    // Tarjan, iterative. Components come out prerequisites-first: if v needs w, comp[w] <= comp[v].
    const idx = new Int32Array(N).fill(-1), low = new Int32Array(N), onS = new Uint8Array(N), comp = new Int32Array(N);
    const S = [];
    let index = 0, nc = 0;
    for (let s = 0; s < N; s++) {
      if (idx[s] !== -1) continue;
      idx[s] = low[s] = index++; S.push(s); onS[s] = 1;
      const work = [[s, 0]];
      while (work.length) {
        const top = work[work.length - 1], v = top[0];
        if (top[1] < needs[v].length) {
          const w = needs[v][top[1]++][0];
          if (idx[w] === -1) { idx[w] = low[w] = index++; S.push(w); onS[w] = 1; work.push([w, 0]); }
          else if (onS[w]) low[v] = Math.min(low[v], idx[w]);
        } else {
          work.pop();
          if (work.length) { const p = work[work.length - 1][0]; low[p] = Math.min(low[p], low[v]); }
          if (low[v] === idx[v]) { let w; do { w = S.pop(); onS[w] = 0; comp[w] = nc; } while (w !== v); nc++; }
        }
      }
    }
    return { comp, nc };
  }

  const less = (a, b) => a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]);
  function heapPush(h, e) {
    h.push(e); let i = h.length - 1;
    while (i > 0) { const p = (i - 1) >> 1; if (less(h[p], h[i])) break; [h[p], h[i]] = [h[i], h[p]]; i = p; }
  }
  function heapPop(h) {
    const top = h[0], last = h.pop();
    if (h.length) {
      h[0] = last; let i = 0;
      for (;;) {
        const l = 2 * i + 1, r = l + 1; let m = i;
        if (l < h.length && less(h[l], h[m])) m = l;
        if (r < h.length && less(h[r], h[m])) m = r;
        if (m === i) break; [h[m], h[i]] = [h[i], h[m]]; i = m;
      }
    }
    return top;
  }

  // Share of an optional question that counts: answer the best `K` questions; questions tied on coverage share the last places.
  function counted(qs, K) {
    const order = qs.slice().sort((a, b) => b.cov - a.cov);
    let cap = K, i = 0;
    while (i < order.length) {
      let j = i; while (j < order.length && Math.abs(order[j].cov - order[i].cov) < 1e-9) j++;
      const share = Math.max(0, Math.min(1, cap / (j - i)));
      for (let t = i; t < j; t++) order[t].inTop = share;
      cap -= j - i; i = j;
    }
  }

  // P(a subsection comes up next year): recency-weighted share of past papers it appeared on, with a light prior.
  globalThis.crunchChance = function (D, halfLife) {
    const years = (D.papers || []).map(p => p.year), last = Math.max(...years);
    const w = y => Math.pow(0.5, (last - y) / halfLife), W = years.reduce((a, y) => a + w(y), 0);
    return D.subs.map(s => (s[4].reduce((a, y) => a + w(y), 0) + 0.5) / (W + 1));
  };

  globalThis.crunchScore = function (D, P) {
    const N = D.items.length;
    const cost = D.items.map(r => r[2]);
    const needs = Array.from({ length: N }, () => []), deps = Array.from({ length: N }, () => []);
    for (const [a, b, ess] of D.links) { needs[a].push([b, ess]); deps[b].push([a, ess]); }

    // Loops become bundles: every item in a loop is kept or cut together and shares one value.
    const { comp, nc } = scc(N, needs);
    const members = Array.from({ length: nc }, () => []);
    for (let i = 0; i < N; i++) members[comp[i]].push(i);
    const inner = (i, j) => comp[i] === comp[j];

    // ---- exam model ----
    const papers = D.papers || [];
    const isNew = new Uint8Array(N);
    if (papers.length) D.items.forEach((r, i) => { if (!D.subs[r[1]][4].length) isNew[i] = 1; });
    else isNew.fill(1); // no papers: every point is "unknown", so every point carries the same share
    const nNew = isNew.reduce((a, b) => a + b, 0);
    const rho = papers.length ? (P.newShare == null ? nNew / N : P.newShare) : 1;
    const lastYear = Math.max(0, ...papers.map(p => p.year));
    const pw = papers.map(p => Math.pow(0.5, (lastYear - p.year) / P.halfLife));
    const pwSum = pw.reduce((a, b) => a + b, 0) || 1;
    const slots = [], questions = [], pointSlots = Array.from({ length: N }, () => []);
    const paperQs = papers.map(() => []);
    papers.forEach((p, pi) => {
      const comp_ = p.qs.filter(q => !q.opt), opt = p.qs.filter(q => q.opt);
      const attA = comp_.reduce((a, q) => a + q.slots.reduce((s, x) => s + x[0], 0), 0);
      const K = P.choice ? (5 / 6) * opt.length : opt.length;
      for (const q of p.qs) {
        const att = q.slots.reduce((s, x) => s + x[0], 0);
        const optShare = attA ? 5 / 6 : 1; // a paper with no short questions puts everything on the optional ones
        const w = q.opt ? optShare / K : (1 / 6) * (att / attA);
        const Q = { paper: pi, opt: q.opt, att, w, cov: 1, inTop: 1, slots: [], K };
        for (const [marks, k, opts] of q.slots) {
          const s = { marks, k, opts, G: opts.length, q: questions.length };
          Q.slots.push(slots.length);
          for (const o of opts) pointSlots[o].push(slots.length);
          slots.push(s);
        }
        questions.push(Q); paperQs[pi].push(Q);
      }
    });
    const setTop = pi => { const opt = paperQs[pi].filter(q => q.opt); if (opt.length) counted(opt, opt[0].K); };
    papers.forEach((_, pi) => setTop(pi));
    const slotCov = s => s.marks * Math.min(1, s.G / s.k);
    const rawScore = pi => paperQs[pi].reduce((a, q) => a + q.w * q.inTop * q.cov, 0);
    const paperMax = papers.map((_, pi) => rawScore(pi) || 1); // full marks, so each paper scores 0..1
    const paperScore = pi => rawScore(pi) / paperMax[pi];
    let Enew = 1; // share of new-course marks still covered

    const gf = new Float64Array(N).fill(1); // gap factor: 1, less a discount for each hidden prerequisite
    const score = new Float64Array(N), own = new Float64Array(N), cut = new Uint8Array(N);
    const w = ess => (ess ? 1 : P.helpW);
    const ownValue = u => {
      let v = isNew[u] && nNew ? (rho * gf[u]) / nNew : 0;
      for (const si of pointSlots[u]) {
        const s = slots[si], q = questions[s.q];
        const lose = s.marks * (Math.min(1, s.G / s.k) - Math.min(1, (s.G - gf[u]) / s.k));
        v += ((1 - rho) * (pw[q.paper] / pwSum) * q.w * q.inTop * lose) / q.att / paperMax[q.paper];
      }
      return v;
    };
    const rescore = u => {
      let s = (own[u] = ownValue(u));
      for (const [d, ess] of deps[u]) if (!cut[d] && !inner(u, d)) s += P.decay * w(ess) * score[d];
      score[u] = s;
    };
    const byDependentsFirst = Array.from({ length: N }, (_, i) => i).sort((a, b) => comp[b] - comp[a]);
    for (const u of byDependentsFirst) rescore(u);

    const bundleValue = b => {
      let s = 0, c = 0;
      for (const u of members[b]) { s += score[u]; c += cost[u]; }
      return s / c;
    };
    const initValue = new Float64Array(N);
    for (let b = 0; b < nc; b++) { const v = bundleValue(b); for (const u of members[b]) initValue[u] = v; }
    const initScore = Float64Array.from(score), initOwn = Float64Array.from(own);

    // ---- greedy cut: always cut the bundle with the least value per unit of study, then rescore what it touched ----
    const ver = new Int32Array(nc), heap = [];
    const tie = b => (b * 2654435761) % 4294967296; // spread equal-value cuts across the course
    for (let b = 0; b < nc; b++) heapPush(heap, [bundleValue(b), tie(b), b, 0]);
    const coverage = () => 100 * ((1 - rho) * papers.reduce((a, _, pi) => a + (pw[pi] / pwSum) * paperScore(pi), 0) + rho * Enew);
    const y = new Float64Array(N), order = new Int32Array(N), steps = [];
    let step = 0;
    while (heap.length) {
      const [, , b, v] = heapPop(heap);
      if (v !== ver[b]) continue;
      const touched = new Set(), dirtySlots = new Set();
      const lower = (u, by) => {
        for (const si of pointSlots[u]) { slots[si].G -= by; dirtySlots.add(si); }
        if (isNew[u] && nNew) Enew -= by / nNew;
      };
      for (const u of members[b]) { cut[u] = 1; lower(u, gf[u]); }
      for (const u of members[b]) {
        for (const [d, ess] of deps[u]) {
          if (cut[d] || inner(u, d)) continue;
          const before = gf[d];
          gf[d] *= 1 - (ess ? P.gapE : P.gapH);
          lower(d, before - gf[d]); touched.add(d);
        }
        for (const [j] of needs[u]) if (!cut[j] && !inner(u, j)) touched.add(j);
      }
      const dirtyQs = new Set();
      for (const si of dirtySlots) { for (const o of slots[si].opts) if (!cut[o]) touched.add(o); dirtyQs.add(slots[si].q); }
      const dirtyPapers = new Set();
      for (const qi of dirtyQs) {
        const q = questions[qi];
        q.cov = q.slots.reduce((a, si) => a + slotCov(slots[si]), 0) / q.att;
        dirtyPapers.add(q.paper);
      }
      for (const pi of dirtyPapers) {
        const before = paperQs[pi].map(q => q.inTop);
        setTop(pi);
        paperQs[pi].forEach((q, t) => {
          if (Math.abs(q.inTop - before[t]) > 1e-12) for (const si of q.slots) for (const o of slots[si].opts) if (!cut[o]) touched.add(o);
        });
      }
      const cov = coverage();
      for (const u of members[b]) { y[u] = cov - 5; order[u] = step; }
      steps.push(cov);
      step++;
      // everything upstream of a touched item passes value up through it, so rescore it too
      const stack = [...touched];
      while (stack.length) {
        const x = stack.pop();
        for (const [j] of needs[x]) if (!cut[j] && !touched.has(j)) { touched.add(j); stack.push(j); }
      }
      const redo = [...touched].sort((a, c) => comp[c] - comp[a]);
      for (const u of redo) rescore(u);
      const bs = new Set(redo.map(u => comp[u]));
      for (const c of bs) { ver[c]++; heapPush(heap, [bundleValue(c), tie(c), c, ver[c]]); }
    }
    const loops = members.filter(g => g.length > 1);
    // y[u]: the item is hidden when the target grade is at or below y[u] (cut while marks covered >= target + 5).
    return { y, order, initScore, initOwn, initValue, comp, members, loops, steps, needs, deps, isNew, rho };
  };
})();
