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

  // Signed in the way app.html decides it. A signed-out student gets one skill free (its lesson and its practice);
  // any other skill asks them to sign in. shortcut: the packages stay public, so this is a nudge, not a lock;
  // checking the account server side would need the packages behind auth.
  const FREE = 'bb_maths_free_skill';
  const signedIn = (() => {
    try {
      return !!JSON.parse(localStorage.getItem('bare-bones-app-v4'))?.session?.currentUser || localStorage.getItem('bb_has_auth_session') === '1';
    } catch { return false }
  })();
  function mayOpen(id) {
    if (signedIn) return true;
    try {
      const free = localStorage.getItem(FREE);
      if (!free) localStorage.setItem(FREE, id);
      return !free || free === id;
    } catch { return true }            // no storage (private browsing): nothing to count with, so let them in
  }
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  function gateHtml() {
    let free = null;
    try { free = byId[localStorage.getItem(FREE)] } catch {}
    return `<section class="gate" style="max-width:520px;margin:48px auto;padding:32px;background:#fff;border-radius:22px;text-align:center">
      <h1 style="font-size:1.7rem;line-height:1.15;margin:0 0 12px">Sign in to open this skill</h1>
      <p style="margin:0 0 22px;color:#4a4540">${free ? `You’ve had your free skill, <b>${esc(free.title)}</b>. ` : ''}Make an account to open all ${list.length} skills, each with a short lesson and exam problems to work through.</p>
      <p style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:0 0 18px">
        <a href="app.html#signup" style="padding:12px 22px;border-radius:999px;background:#fa4c06;color:#fff;font-weight:700;text-decoration:none">Make an account</a>
        <a href="app.html#signin" style="padding:12px 22px;border-radius:999px;border:1.5px solid #1A1916;color:#1A1916;font-weight:700;text-decoration:none">Sign in</a></p>
      ${free ? `<a href="maths-learn.html?skill=${encodeURIComponent(free.id)}" style="color:#7A7870">Back to ${esc(free.title)}</a>` : ''}
    </section>`;
  }

  // Search tags for a skill's page: title, description, keywords and schema.org data, from its package.
  // Crawlers keep no storage, so they always get the free skill and see these.
  const plain = t => String(t).replace(/\*\*/g, '').replace(/\$([^$]+)\$/g, (_, m) => m.replace(/\\(left|right|,|;|quad)/g, ' ')
    .replace(/\\([a-zA-Z]+)/g, '$1').replace(/[{}]/g, '').replace(/\^/g, '^')).replace(/\s+/g, ' ').trim();
  function meta(name, content) {
    let m = document.head.querySelector(`meta[name="${name}"]`);
    if (!m) { m = document.createElement('meta'); m.name = name; document.head.append(m) }
    m.content = content;
  }
  function tagPage(L, kind) {
    const description = `${L.title}: ${kind === 'practice' ? 'Leaving Cert exam problems to work through, with full worked solutions' : 'a short Leaving Cert maths lesson with a worked example and exam tips'}. ${plain(L.what.say[0])}`;
    document.title = `${L.title}${kind === 'practice' ? ' – practice' : ''} | Leaving Cert Maths | barebones`;
    meta('description', description.slice(0, 300));
    meta('keywords', (L.keywords || []).join(', '));
    let ld = document.getElementById('skill-ld');
    if (!ld) { ld = document.createElement('script'); ld.type = 'application/ld+json'; ld.id = 'skill-ld'; document.head.append(ld) }
    ld.textContent = JSON.stringify({
      '@context': 'https://schema.org', '@type': 'LearningResource', name: L.title, description,
      keywords: (L.keywords || []).join(', '), about: L.chapter, inLanguage: 'en-IE',
      learningResourceType: kind === 'practice' ? 'Practice problems' : 'Lesson',
      educationalLevel: L.level === 'HL' ? 'Leaving Certificate Higher Level' : 'Leaving Certificate Higher and Ordinary Level',
      isPartOf: { '@type': 'Course', name: 'Leaving Certificate Mathematics' },
    });
  }

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
    if (!signedIn) return;                             // the next skill would only show the sign-in prompt
    setTimeout(() => {
      const next = list[list.findIndex(s => s.id === id) + 1];
      if (next) skill(next.id).catch(() => {});      // only a head start: the next page loads it again if this failed
    }, afterMs);
  }

  return { byId, level, list, chapters: INDEX.chapters, skill, more, prefetchNext, signedIn, mayOpen, gateHtml, tagPage };
})();
