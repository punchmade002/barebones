// Loads maths skills one at a time from maths-skills/ (built by pipeline/requirements/maths/package.py).
// Needs maths-skills/index.js first. A skill's package holds its Learn phase and first practice problem;
// the other practice problems load once the student starts practising, and after a while on a skill
// the next one in the list loads too, so it opens instantly.
window.MathsPacks = (() => {
  const INDEX = window.MATHS_INDEX;
  const byId = Object.fromEntries(INDEX.skills.map(s => [s.id, s]));

  // the student's maths level from onboarding (app.js saves the whole state under this key); Higher until they choose
  const level = (() => {
    try {
      const app = JSON.parse(localStorage.getItem('bare-bones-app-v4')) || {};
      return app.usersByName?.[app.session?.currentUser]?.onboarding?.levels?.maths === 'ordinary' ? 'ordinary' : 'higher';
    } catch { return 'higher' }
  })();
  // Higher-only skills are not on the Ordinary course, so Ordinary students don't see them listed
  const list = INDEX.skills.filter(s => level === 'higher' || s.level !== 'HL');

  // each file is fetched once; a failed load can be retried
  const loading = new Map();
  function script(src) {
    if (!loading.has(src)) loading.set(src, new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = () => { s.remove(); loading.delete(src); reject(new Error(`Could not load ${src}`)) };
      document.head.append(s);
    }));
    return loading.get(src);
  }

  const skill = id => script(`maths-skills/${id}.js?v=${byId[id].v}`).then(() => window.MATHS_PACKS[id]);
  const more = id => byId[id].vm ? script(`maths-skills/${id}.more.js?v=${byId[id].vm}`).then(() => window.MATHS_MORE[id]) : Promise.resolve([]);

  function prefetchNext(id, afterMs = 20000) {
    setTimeout(() => {
      const next = list[list.findIndex(s => s.id === id) + 1];
      if (next) skill(next.id).catch(() => {});      // only a head start: the next page loads it again if this failed
    }, afterMs);
  }

  return { byId, level, list, chapters: INDEX.chapters, skill, more, prefetchNext };
})();
