// Crunch Mode scoring (see CRUNCH_MODE.md). Plain script: defines globalThis.crunchScore.
// D = data.json from scripts/crunch_map.py. P = {decay, helpW, gapE, gapH}.
// Exam value isn't in yet, so every point carries 1 mark (shortcut: swap `base` for real exam value once its formula is agreed).
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
  const less = (a, b) => a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]);

  globalThis.crunchScore = function (D, P) {
    const N = D.items.length;
    const cost = D.items.map(r => r[2]);
    const needs = Array.from({ length: N }, () => []), deps = Array.from({ length: N }, () => []);
    for (const [a, b, ess] of D.links) { needs[a].push([b, ess]); deps[b].push([a, ess]); }

    // Loops become bundles: every item in a loop is kept or cut together and shares one value.
    const { comp, nc } = scc(N, needs);
    const members = Array.from({ length: nc }, () => []);
    for (let i = 0; i < N; i++) members[comp[i]].push(i);
    const inner = (i, j) => comp[i] === comp[j]; // links inside a bundle carry no value or gap

    const m = new Float64Array(N).fill(1); // marks the item still earns (1, minus gap discounts)
    const score = new Float64Array(N), cut = new Uint8Array(N);
    const w = ess => (ess ? 1 : P.helpW);
    const rescore = u => {
      let s = m[u];
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
    const initScore = Float64Array.from(score);

    // Greedy cut: always cut the bundle with the least value per unit of study, then rescore what it touched.
    const ver = new Int32Array(nc), heap = [];
    const tie = b => (b * 2654435761) % 4294967296; // spread equal-value cuts across the course
    for (let b = 0; b < nc; b++) heapPush(heap, [bundleValue(b), tie(b), b, 0]);
    let covered = N;
    const y = new Float64Array(N), order = new Int32Array(N), steps = [];
    let step = 0;
    while (heap.length) {
      const [, , b, v] = heapPop(heap);
      if (v !== ver[b]) continue;
      const touched = new Set();
      for (const u of members[b]) { cut[u] = 1; covered -= m[u]; }
      for (const u of members[b]) {
        for (const [d, ess] of deps[u]) {
          if (cut[d] || inner(u, d)) continue;
          const after = m[d] * (1 - (ess ? P.gapE : P.gapH));
          covered -= m[d] - after; m[d] = after; touched.add(d);
        }
        for (const [j] of needs[u]) if (!cut[j] && !inner(u, j)) touched.add(j);
      }
      const cov = (100 * covered) / N;
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
    return { y, order, initScore, initValue, comp, members, loops, steps, needs, deps };
  };
})();
