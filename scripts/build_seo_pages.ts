// Builds the public, crawlable notes pages for barebones.ie from the authored notes in
// content/<subject>/*.json, plus the matching entries in sitemap.xml.
//
//     deno run -A scripts/build_seo_pages.ts
//
// Output (all static HTML, nothing rendered by JS):
//   /leaving-cert-notes/                                   hub listing every subject
//   /leaving-cert-<subject>/                               one page per subject
//   /leaving-cert-<subject>/<chapter>/                     one page per chapter
//   /leaving-cert-<subject>/<chapter>/<subsection>/        full notes for one subsection
//
// What goes public: the notes and key terms the user authored, and up to two practice
// question prompts per subsection (marks only, no model answers). Fact cards, model answers,
// SEC exam questions, test mode and progress stay inside app.html.
//
// Re-running is safe: generated folders (marked by the generator meta tag) are removed and
// rebuilt, and sitemap.xml keeps every entry that isn't a generated page.

const ROOT = new URL("..", import.meta.url).pathname;
const SITE = "https://barebones.ie";
const GENERATOR = "barebones-seo-pages";
const ORG_ID = `${SITE}/#org`;
const HUB_SLUG = "leaving-cert-notes";
const SAMPLE_QUESTIONS = 2;
// Hand-made pages that share the /leaving-cert-* prefix: keep their sitemap entries.
const HAND_MADE = new Set(["/leaving-cert-points-calculator/"]);

// Subjects to publish, in display order. Remove a line to take a subject offline.
const SUBJECTS = [
  {
    id: "biology", slug: "leaving-cert-biology", name: "Biology",
    blurb: "Leaving Cert Biology notes for every chapter of the course, from scientific method and biomolecules to genetics, human systems and ecology, written to the current specification.",
  },
  {
    id: "chemistry", slug: "leaving-cert-chemistry", name: "Chemistry",
    blurb: "Leaving Cert Chemistry notes covering atomic structure, bonding, stoichiometry, rates, equilibrium, organic chemistry and the mandatory experiments.",
  },
  {
    id: "history", slug: "leaving-cert-history", name: "History",
    blurb: "Leaving Cert History notes for the Irish and European topics, with the key personalities, case studies, dates and terms you need for document and essay questions.",
  },
  {
    id: "geography", slug: "leaving-cert-geography", name: "Geography",
    blurb: "Leaving Cert Geography notes on physical, regional and human geography, with landform formation, case studies, named examples and map and photo skills.",
  },
  {
    id: "business", slug: "leaving-cert-business", name: "Business",
    blurb: "Leaving Cert Business notes for every strand of the course: stakeholders, the economy, enterprise, management, and informed decisions as a consumer and employee.",
  },
  {
    id: "home-economics", slug: "leaving-cert-home-economics", name: "Home Economics",
    blurb: "Leaving Cert Home Economics notes on food science and nutrition, resource management, family and social studies, and the electives.",
  },
  {
    id: "pe", slug: "leaving-cert-pe", name: "PE",
    blurb: "Leaving Cert Physical Education notes on learning skills, performance demands, planning for optimum performance, promoting physical activity and the physical activity areas.",
  },
];

// ---------------------------------------------------------------- data

type Block = { h: string; b?: string; points?: string[] };
type Term = { term: string; definition: string };
type Question = { marks: number; prompt: string; model: string };
type Entry = {
  loId: string; chapterId: string; subsection: string; syllabusRef?: string;
  notes: Block[]; keyTerms: Term[]; factCards?: Term[]; questions?: Question[];
};
type Sub = Entry & { title: string; slug: string; url: string; path: string; mtime: Date };
type Chapter = {
  id: string; title: string; slug: string; url: string; path: string;
  subs: Sub[]; examCount: number;
};
type Subject = (typeof SUBJECTS)[number] & { url: string; chapters: Chapter[] };

// deno-lint-ignore no-explicit-any
type Any = any;

function loadCourseData(): Any {
  const text = Deno.readTextFileSync(`${ROOT}data.js`);
  return new Function(`${text}; return COURSE_DATA;`)();
}

// Count past exam questions per chapter so the CTA can say what's waiting in the app.
// Only the count is used; no exam text reaches the public pages.
function examCounts(subject: string): Map<string, number> {
  const counts = new Map<string, number>();
  const file = `${ROOT}${subject}-exam-questions.js`;
  let text: string;
  try {
    text = Deno.readTextFileSync(file);
  } catch {
    return counts;
  }
  const window: Any = {};
  new Function("window", text)(window);
  for (const q of window.EXAM_QUESTIONS_DB || []) {
    if (q.chapterId) counts.set(q.chapterId, (counts.get(q.chapterId) || 0) + 1);
  }
  return counts;
}

function readEntries(subject: string): Map<string, Entry & { mtime: Date }> {
  const entries = new Map<string, Entry & { mtime: Date }>();
  const dir = `${ROOT}content/${subject}`;
  for (const file of Deno.readDirSync(dir)) {
    if (!file.name.endsWith(".json")) continue;
    const path = `${dir}/${file.name}`;
    try {
      const data = JSON.parse(Deno.readTextFileSync(path)) as Entry;
      if (!Array.isArray(data.notes) || !data.notes.length) continue;
      entries.set(data.loId, { ...data, mtime: Deno.statSync(path).mtime ?? new Date() });
    } catch (err) {
      console.warn(`skipping ${subject}/${file.name}: ${(err as Error).message}`);
    }
  }
  return entries;
}

function slugify(text: string, max = 70): string {
  let slug = text
    .normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
    .replace(/[⁺]/g, "-plus").replace(/&/g, " and ")
    .toLowerCase().replace(/['’]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  if (slug.length > max) slug = slug.slice(0, max).replace(/-[^-]*$/, "");
  return slug || "notes";
}

function unique(slug: string, taken: Set<string>): string {
  let out = slug;
  for (let n = 2; taken.has(out); n++) out = `${slug}-${n}`;
  taken.add(out);
  return out;
}

function buildModel(): Subject[] {
  const course = loadCourseData();
  return SUBJECTS.map((meta) => {
    const entries = readEntries(meta.id);
    const exams = examCounts(meta.id);
    const subjectUrl = `/${meta.slug}/`;
    const chapterSlugs = new Set<string>();
    const chapters: Chapter[] = [];
    for (const ch of course.chapters) {
      if (ch.subject !== meta.id) continue;
      const los = (ch.learningOutcomes || []).filter((lo: Any) => entries.has(lo.id));
      if (!los.length) continue;
      const slug = unique(slugify(ch.title), chapterSlugs);
      const url = `${subjectUrl}${slug}/`;
      const subSlugs = new Set<string>();
      const subs: Sub[] = los.map((lo: Any) => {
        const entry = entries.get(lo.id)!;
        // Outline numbering ("3. Properties") means nothing out of context; the pages order them.
        const title = (entry.subsection || lo.title).replace(/^\d+[.)]\s+/, "");
        const s = unique(slugify(title), subSlugs);
        return { ...entry, title, slug: s, url: `${url}${s}/`, path: `${meta.slug}/${slug}/${s}` };
      });
      chapters.push({
        id: ch.id, title: ch.title, slug, url, path: `${meta.slug}/${slug}`, subs,
        examCount: exams.get(ch.id) || 0,
      });
    }
    return { ...meta, url: subjectUrl, chapters };
  }).filter((s) => s.chapters.length);
}

// ---------------------------------------------------------------- text helpers

function esc(text: string): string {
  return String(text)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function norm(text: string): string {
  return text.toLowerCase().replace(/[’']/g, "'").replace(/⁺/g, "+").replace(/[^a-z0-9+']+/g, " ").trim();
}

function truncate(text: string, max: number): string {
  if (text.length <= max) return text;
  const cut = text.slice(0, max - 1).replace(/[\s,;:.]+\S*$/, "");
  return `${cut}…`;
}

// "Leaving Cert Biology: Photosynthesis Notes" while it fits; longer topics go first so a
// truncated search result still shows what the page is about.
function pageTitle(subjectName: string, topic: string): string {
  const base = `Leaving Cert ${subjectName}: ${topic} Notes`;
  if (base.length <= 52) return `${base} | barebones`;
  if (base.length <= 66) return base;
  return `${topic} | Leaving Cert ${subjectName} Notes`;
}

// Short or repeated subsection names ("Properties", "Sources") need the chapter alongside.
function topicName(sub: Sub, ch: Chapter, repeated: Set<string>): string {
  const generic = repeated.has(norm(sub.title)) || sub.title.split(/\s+/).length <= 2;
  return generic && !norm(sub.title).includes(norm(ch.title)) ? `${ch.title} – ${sub.title}` : sub.title;
}

function plural(n: number, one: string, many = `${one}s`): string {
  return `${n} ${n === 1 ? one : many}`;
}

// The notes cross-reference other subsections by name in curly quotes, e.g. see “Models”.
// Turn those into internal links when the name matches a published subsection.
function inline(text: string, links: Map<string, string>, self: string): string {
  return esc(text).replace(/“([^“”]{2,120})”/g, (whole, name) => {
    const url = links.get(norm(name.replace(/&amp;/g, "&")));
    return url && url !== self ? `“<a href="${url}">${name}</a>”` : whole;
  });
}

function anchor(text: string, taken: Set<string>): string {
  return unique(slugify(text, 50), taken);
}

function isoDate(d: Date): string {
  return d.toISOString().slice(0, 10);
}

function latest(dates: Date[]): Date {
  return dates.reduce((a, b) => (b > a ? b : a), new Date(0));
}

// ---------------------------------------------------------------- page shell

type Crumb = { name: string; url: string };

function jsonLd(data: unknown): string {
  return `<script type="application/ld+json">${JSON.stringify(data, null, 1).replace(/</g, "\\u003c")}</script>`;
}

function breadcrumbLd(crumbs: Crumb[]) {
  return {
    "@type": "BreadcrumbList",
    itemListElement: crumbs.map((c, i) => ({
      "@type": "ListItem", position: i + 1, name: c.name, item: `${SITE}${c.url}`,
    })),
  };
}

function learningResourceLd(o: {
  url: string; name: string; description: string; about: string; modified: Date;
  partOf?: string; keywords?: string[]; teaches?: string[]; parts?: { name: string; url: string }[];
}) {
  return {
    "@type": "LearningResource",
    "@id": `${SITE}${o.url}#notes`,
    name: o.name,
    description: o.description,
    url: `${SITE}${o.url}`,
    inLanguage: "en-IE",
    learningResourceType: "Revision notes",
    educationalLevel: "Leaving Certificate",
    isAccessibleForFree: true,
    audience: { "@type": "EducationalAudience", educationalRole: "student" },
    about: { "@type": "Thing", name: o.about },
    ...(o.teaches?.length ? { teaches: o.teaches } : {}),
    ...(o.keywords?.length ? { keywords: o.keywords.join(", ") } : {}),
    ...(o.partOf ? { isPartOf: { "@id": `${SITE}${o.partOf}#notes` } } : {}),
    ...(o.parts?.length
      ? { hasPart: o.parts.map((p) => ({ "@type": "LearningResource", name: p.name, url: `${SITE}${p.url}` })) }
      : {}),
    dateModified: isoDate(o.modified),
    publisher: { "@id": ORG_ID },
  };
}

function crumbsHtml(crumbs: Crumb[]): string {
  const items = crumbs.map((c, i) =>
    i === crumbs.length - 1
      ? `<li aria-current="page">${esc(c.name)}</li>`
      : `<li><a href="${c.url}">${esc(c.name)}</a></li>`
  ).join("");
  return `<nav class="np-crumbs" aria-label="Breadcrumb"><ol>${items}</ol></nav>`;
}

function page(o: {
  title: string; description: string; url: string; crumbs: Crumb[]; ld: unknown[];
  body: string; subjects: Subject[];
}): string {
  const canonical = `${SITE}${o.url}`;
  const subjectLinks = o.subjects.map((s) => `<a href="${s.url}">${esc(s.name)} notes</a>`).join("\n          ");
  return `<!doctype html>
<html lang="en-IE">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<script>/* signed-in state: mirrors the app's own check */(function(){try{var s=localStorage.getItem("bb_has_auth_session")==="1";if(!s){var a=JSON.parse(localStorage.getItem("bare-bones-app-v4")||"null");s=!!(a&&a.session&&a.session.currentUser);}if(s)document.documentElement.classList.add("bb-signed-in");}catch(e){}})();</script>
<title>${esc(o.title)}</title>
<meta name="description" content="${esc(o.description)}" />
<link rel="canonical" href="${canonical}" />
<meta name="generator" content="${GENERATOR}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="barebones" />
<meta property="og:locale" content="en_IE" />
<meta property="og:url" content="${canonical}" />
<meta property="og:title" content="${esc(o.title)}" />
<meta property="og:description" content="${esc(o.description)}" />
<meta property="og:image" content="${SITE}/design_handoff_barebones_landing/assets/logo-bb.png" />
<meta property="og:image:alt" content="barebones logo" />
<meta name="twitter:card" content="summary" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg?v=3" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=3" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/design_handoff_barebones_landing/styles.css" />
<link rel="stylesheet" href="/seo-pages.css" />
${jsonLd({ "@context": "https://schema.org", "@graph": [breadcrumbLd(o.crumbs), ...o.ld] })}
<script>
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body class="np">

<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/" aria-label="barebones home">
      <img src="/design_handoff_barebones_landing/assets/logo-wordmark.png" alt="barebones" width="166" height="52" />
    </a>
    <nav class="nav-links" aria-label="Main">
      <a href="/${HUB_SLUG}/">Notes</a>
      <a href="/#method">Method</a>
      <a href="/#features">Features</a>
    </nav>
    <div class="nav-cta">
      <a href="/app.html#signin" class="btn btn-ghost np-signin auth-out">Sign in</a>
      <a href="/app.html#signup" class="btn btn-primary auth-out">Get started free</a>
      <a href="/app.html" class="btn btn-primary auth-in">Open app</a>
    </div>
  </div>
</header>

<main>
${o.body}
</main>

<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img class="fwm" src="/design_handoff_barebones_landing/assets/logo-wordmark.png" alt="barebones" />
        <p class="np-foot-line">The bare-bones way to study for the Leaving Cert.</p>
      </div>
      <div class="foot-cols">
        <div class="foot-col">
          <h4>Notes</h4>
          ${subjectLinks}
        </div>
        <div class="foot-col">
          <h4>Product</h4>
          <a href="/leaving-cert-points-calculator/">Points calculator</a>
          <a href="/#method">Method</a>
          <a href="/#features">Features</a>
          <a href="/app.html#signin" class="auth-out">Sign in</a>
          <a href="/app.html" class="auth-in">Open app</a>
        </div>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© ${new Date().getFullYear()} barebones. Made in Ireland.</span>
      <span>Not affiliated with the State Examinations Commission.</span>
    </div>
  </div>
</footer>
<script defer src="/_vercel/speed-insights/script.js"></script>
</body>
</html>
`;
}

function ctaBand(o: { heading: string; text: string; source: string }): string {
  return `<section class="np-cta-wrap">
  <div class="wrap">
    <div class="cta">
      <div class="dotfield"></div>
      <div>
        <h2>${esc(o.heading)}</h2>
        <p>${esc(o.text)}</p>
      </div>
      <div class="right">
        <a href="/app.html#signup" class="btn btn-primary signup-btn auth-out" data-cta="${esc(o.source)}">Get started free</a>
        <a href="/app.html" class="btn btn-primary signup-btn auth-in">Open the app</a>
        <p class="signin-note auth-out">Already have an account? <a href="/app.html#signin">Sign in</a></p>
      </div>
    </div>
  </div>
</section>`;
}

function chapterCtaText(subject: Subject, ch: Chapter): string {
  const cards = ch.subs.reduce((n, s) => n + s.keyTerms.length + (s.factCards?.length || 0), 0);
  const parts = [`${plural(cards, "flashcard")}`];
  if (ch.examCount) parts.push(`${plural(ch.examCount, "past exam question")} marked the way the examiner marks them`);
  return `Reading is step one. In the app, ${ch.title} becomes ${parts.join(" and ")}, with progress saved as you go. Free for Leaving Cert ${subject.name} students.`;
}

// ---------------------------------------------------------------- pages

function subsectionPage(subject: Subject, ch: Chapter, i: number, subjects: Subject[], links: Map<string, string>): string {
  const sub = ch.subs[i];
  const prev = ch.subs[i - 1];
  const next = ch.subs[i + 1];
  const lead = sub.notes.find((b) => b.b)?.b || sub.notes[0].points?.[0] || "";
  const seen = new Set<string>(), repeated = new Set<string>();
  for (const c of subject.chapters) for (const s of c.subs) {
    const key = norm(s.title);
    if (seen.has(key)) repeated.add(key);
    seen.add(key);
  }
  const topic = topicName(sub, ch, repeated);
  const title = pageTitle(subject.name, topic);
  const description = truncate(`Leaving Cert ${subject.name} notes: ${topic}. ${lead}`, 158);
  const crumbs: Crumb[] = [
    { name: "Home", url: "/" },
    { name: "Leaving Cert Notes", url: `/${HUB_SLUG}/` },
    { name: subject.name, url: subject.url },
    { name: ch.title, url: ch.url },
    { name: sub.title, url: sub.url },
  ];
  const ids = new Set<string>(["key-terms", "practice-questions"]);
  const blocks = sub.notes.map((b) => ({ ...b, id: anchor(b.h, ids) }));
  const cardCount = sub.keyTerms.length + (sub.factCards?.length || 0);

  const toc = blocks.length > 2
    ? `<nav class="np-toc" aria-label="On this page"><h2 class="np-label">On this page</h2><ol>${
      blocks.map((b) => `<li><a href="#${b.id}">${esc(b.h)}</a></li>`).join("")
    }<li><a href="#key-terms">Key terms</a></li></ol></nav>`
    : "";

  const midpoint = Math.ceil(blocks.length / 2);
  const blockHtml = blocks.map((b, n) => {
    const points = (b.points || []).map((p) => {
      const diagram = /^Diagram:\s*/.exec(p);
      if (diagram) {
        return `<li class="np-diagram"><span class="np-tag">Diagram</span> ${inline(p.slice(diagram[0].length), links, sub.url)}</li>`;
      }
      return `<li>${inline(p, links, sub.url)}</li>`;
    }).join("\n        ");
    const nudge = n === midpoint - 1 && blocks.length >= 4
      ? `\n    <aside class="np-nudge"><div><strong>Know this already?</strong> Prove it: ${plural(cardCount, "flashcard")} on ${esc(sub.title)} are waiting in the app.</div><a class="btn btn-dark" href="/app.html#signup" data-cta="nudge">Test yourself</a></aside>`
      : "";
    return `    <section class="np-block" id="${b.id}">
      <h2>${esc(b.h)}</h2>${b.b ? `\n      <p class="np-lead">${inline(b.b, links, sub.url)}</p>` : ""}${points ? `\n      <ul>\n        ${points}\n      </ul>` : ""}
    </section>${nudge}`;
  }).join("\n");

  const terms = `    <section class="np-terms" id="key-terms">
      <h2>Key terms</h2>
      <dl>
        ${sub.keyTerms.map((t) => `<div><dt>${esc(t.term)}</dt><dd>${inline(t.definition, links, sub.url)}</dd></div>`).join("\n        ")}
      </dl>
    </section>`;

  const qs = (sub.questions || []).slice(0, SAMPLE_QUESTIONS);
  const questions = qs.length
    ? `    <section class="np-questions" id="practice-questions">
      <h2>Practice questions</h2>
      <ol>
        ${qs.map((q) => `<li><p>${esc(q.prompt)}</p><span class="np-marks">${q.marks} marks</span></li>`).join("\n        ")}
      </ol>
      <p class="np-locked"><span aria-hidden="true">■</span> Model answers, marking and ${plural(Math.max((sub.questions || []).length, qs.length), "practice question")} for this section are in the app. <a href="/app.html#signup" data-cta="answers">See the answers</a></p>
    </section>`
    : "";

  const pager = `<nav class="np-pager" aria-label="Next and previous">
      ${prev ? `<a class="prev" href="${prev.url}"><span>Previous</span>${esc(prev.title)}</a>` : `<a class="prev" href="${ch.url}"><span>Chapter</span>${esc(ch.title)}</a>`}
      ${next ? `<a class="next" href="${next.url}"><span>Next</span>${esc(next.title)}</a>` : nextChapterLink(subject, ch)}
    </nav>`;

  const side = `<aside class="np-side">
      <div class="np-side-inner">
        <h2 class="np-label"><a href="${ch.url}">${esc(ch.title)}</a></h2>
        <ol class="np-sibs">
          ${ch.subs.map((s) => s === sub
            ? `<li aria-current="page"><span>${esc(s.title)}</span></li>`
            : `<li><a href="${s.url}">${esc(s.title)}</a></li>`).join("\n          ")}
        </ol>
        <div class="np-side-cta">
          <p><strong>${plural(cardCount, "flashcard")}</strong> for this section${ch.examCount ? ` and <strong>${plural(ch.examCount, "past exam question")}</strong> for the chapter` : ""}.</p>
          <a class="btn btn-primary" href="/app.html#signup" data-cta="sidebar">Drill them free</a>
        </div>
      </div>
    </aside>`;

  const body = `<div class="wrap np-page">
  ${crumbsHtml(crumbs)}
  <div class="np-grid">
    <article class="np-article">
      <header class="np-head">
        <h1><span class="np-kicker">Leaving Cert ${esc(subject.name)} · ${esc(ch.title)}</span>${esc(sub.title)}</h1>
        <p class="np-meta">${plural(blocks.length, "section")} · ${plural(sub.keyTerms.length, "key term")}${sub.syllabusRef ? ` · Syllabus ${esc(sub.syllabusRef)}` : ""}</p>
      </header>
      ${toc}
${blockHtml}
${terms}
${questions}
    ${pager}
    </article>
    ${side}
  </div>
</div>
${ctaBand({ heading: `Now drill ${ch.title}.`, text: chapterCtaText(subject, ch), source: "band" })}`;

  return page({
    title, description, url: sub.url, crumbs, body, subjects,
    ld: [learningResourceLd({
      url: sub.url, name: `${topic}: Leaving Cert ${subject.name} notes`, description,
      about: topic, modified: sub.mtime, partOf: ch.url,
      teaches: blocks.map((b) => b.h), keywords: sub.keyTerms.map((t) => t.term),
    })],
  });
}

function nextChapterLink(subject: Subject, ch: Chapter): string {
  const idx = subject.chapters.indexOf(ch);
  const nextCh = subject.chapters[idx + 1];
  return nextCh
    ? `<a class="next" href="${nextCh.url}"><span>Next chapter</span>${esc(nextCh.title)}</a>`
    : `<a class="next" href="${subject.url}"><span>All chapters</span>Leaving Cert ${esc(subject.name)}</a>`;
}

function chapterPage(subject: Subject, ch: Chapter, subjects: Subject[]): string {
  const title = pageTitle(subject.name, ch.title);
  const subNames = ch.subs.map((s) => s.title);
  const description = truncate(
    `Free Leaving Cert ${subject.name} notes on ${ch.title}: ${subNames.join(", ")}. Key terms, practice questions and flashcards.`,
    158,
  );
  const crumbs: Crumb[] = [
    { name: "Home", url: "/" },
    { name: "Leaving Cert Notes", url: `/${HUB_SLUG}/` },
    { name: subject.name, url: subject.url },
    { name: ch.title, url: ch.url },
  ];
  const cards = ch.subs.map((s, n) => {
    const lead = s.notes.find((b) => b.b)?.b || s.notes[0].points?.[0] || "";
    return `<li class="np-card">
        <a href="${s.url}">
          <span class="np-num">${String(n + 1).padStart(2, "0")}</span>
          <h2>${esc(s.title)}</h2>
          <p>${esc(truncate(lead, 200))}</p>
          <ul class="np-heads">${s.notes.slice(0, 6).map((b) => `<li>${esc(b.h)}</li>`).join("")}</ul>
          <span class="np-card-meta">${plural(s.keyTerms.length, "key term")} · Read notes →</span>
        </a>
      </li>`;
  }).join("\n      ");
  const others = subject.chapters.filter((c) => c !== ch)
    .map((c) => `<li><a href="${c.url}">${esc(c.title)}</a></li>`).join("");
  const body = `<div class="wrap np-page">
  ${crumbsHtml(crumbs)}
  <header class="np-head np-head-wide">
    <h1><span class="np-kicker">Leaving Cert ${esc(subject.name)} notes</span>${esc(ch.title)}</h1>
    <p class="np-standfirst">${plural(ch.subs.length, "section")} of notes on ${esc(ch.title)}, written for the Leaving Cert ${esc(subject.name)} course. Each one has the full notes, key terms and sample exam-style questions.</p>
  </header>
  <ol class="np-cards">
      ${cards}
  </ol>
  <nav class="np-more" aria-label="Other chapters">
    <h2 class="np-label">More Leaving Cert ${esc(subject.name)} notes</h2>
    <ul>${others}</ul>
  </nav>
</div>
${ctaBand({ heading: `Now drill ${ch.title}.`, text: chapterCtaText(subject, ch), source: "band-chapter" })}`;
  return page({
    title, description, url: ch.url, crumbs, body, subjects,
    ld: [learningResourceLd({
      url: ch.url, name: `${ch.title}: Leaving Cert ${subject.name} notes`, description, about: ch.title,
      modified: latest(ch.subs.map((s) => s.mtime)), partOf: subject.url,
      parts: ch.subs.map((s) => ({ name: s.title, url: s.url })),
    })],
  });
}

function subjectPage(subject: Subject, subjects: Subject[]): string {
  const title = `Leaving Cert ${subject.name} Notes | barebones`;
  const description = truncate(`${subject.blurb} Free, with flashcards and exam questions in the app.`, 158);
  const crumbs: Crumb[] = [
    { name: "Home", url: "/" },
    { name: "Leaving Cert Notes", url: `/${HUB_SLUG}/` },
    { name: subject.name, url: subject.url },
  ];
  const subCount = subject.chapters.reduce((n, c) => n + c.subs.length, 0);
  const chapters = subject.chapters.map((ch) => `<section class="np-chapter">
      <h2><a href="${ch.url}">${esc(ch.title)}</a></h2>
      <ul>${ch.subs.map((s) => `<li><a href="${s.url}">${esc(s.title)}</a></li>`).join("")}</ul>
    </section>`).join("\n    ");
  const body = `<div class="wrap np-page">
  ${crumbsHtml(crumbs)}
  <header class="np-head np-head-wide">
    <h1><span class="np-kicker">Free revision notes</span>Leaving Cert ${esc(subject.name)} notes</h1>
    <p class="np-standfirst">${esc(subject.blurb)}</p>
    <p class="np-meta">${plural(subject.chapters.length, "chapter")} · ${plural(subCount, "section")} of notes</p>
  </header>
  <div class="np-chapters">
    ${chapters}
  </div>
</div>
${ctaBand({
    heading: `Learn it. Then drill it.`,
    text: `Every section of Leaving Cert ${subject.name} has flashcards and a test mode in the app${subject.chapters.some((c) => c.examCount) ? ", plus past exam questions sorted by chapter" : ""}. Free to start.`,
    source: "band-subject",
  })}`;
  return page({
    title, description, url: subject.url, crumbs, body, subjects,
    ld: [learningResourceLd({
      url: subject.url, name: `Leaving Cert ${subject.name} notes`, description, about: `Leaving Certificate ${subject.name}`,
      modified: latest(subject.chapters.flatMap((c) => c.subs.map((s) => s.mtime))),
      parts: subject.chapters.map((c) => ({ name: c.title, url: c.url })),
    })],
  });
}

function hubPage(subjects: Subject[]): string {
  const url = `/${HUB_SLUG}/`;
  const title = "Leaving Cert Notes: Free Revision Notes by Subject | barebones";
  const description = `Free Leaving Cert revision notes for ${subjects.map((s) => s.name).join(", ")}. Every chapter, with key terms and practice questions.`;
  const crumbs: Crumb[] = [{ name: "Home", url: "/" }, { name: "Leaving Cert Notes", url }];
  const cards = subjects.map((s) => {
    const subCount = s.chapters.reduce((n, c) => n + c.subs.length, 0);
    return `<li class="np-card">
        <a href="${s.url}">
          <h2>Leaving Cert ${esc(s.name)}</h2>
          <p>${esc(s.blurb)}</p>
          <span class="np-card-meta">${plural(s.chapters.length, "chapter")} · ${plural(subCount, "section")} →</span>
        </a>
      </li>`;
  }).join("\n      ");
  const body = `<div class="wrap np-page">
  ${crumbsHtml(crumbs)}
  <header class="np-head np-head-wide">
    <h1><span class="np-kicker">Free revision notes</span>Leaving Cert notes</h1>
    <p class="np-standfirst">Clear, exam-focused notes for every chapter, written to the current Leaving Cert specifications. Read them here, then drill the flashcards and past exam questions in the app.</p>
  </header>
  <ol class="np-cards">
      ${cards}
  </ol>
</div>
${ctaBand({ heading: "The Leaving Cert, stripped back.", text: "Two steps: learn the content, then drill real exam questions. Free, in your browser.", source: "band-hub" })}`;
  return page({
    title, description, url, crumbs, body, subjects,
    ld: [learningResourceLd({
      url, name: "Leaving Cert notes", description, about: "Leaving Certificate",
      modified: latest(subjects.flatMap((s) => s.chapters.flatMap((c) => c.subs.map((x) => x.mtime)))),
      parts: subjects.map((s) => ({ name: `Leaving Cert ${s.name}`, url: s.url })),
    })],
  });
}

// ---------------------------------------------------------------- output

function removeGenerated(): void {
  for (const entry of Deno.readDirSync(ROOT)) {
    if (!entry.isDirectory || !entry.name.startsWith("leaving-cert-")) continue;
    try {
      const html = Deno.readTextFileSync(`${ROOT}${entry.name}/index.html`);
      if (html.includes(`name="generator" content="${GENERATOR}"`)) {
        Deno.removeSync(`${ROOT}${entry.name}`, { recursive: true });
      }
    } catch {
      // Not a generated folder; leave it alone.
    }
  }
}

function write(path: string, html: string): void {
  Deno.mkdirSync(`${ROOT}${path}`, { recursive: true });
  Deno.writeTextFileSync(`${ROOT}${path}/index.html`, html);
}

function updateSitemap(pages: { url: string; modified: Date }[]): void {
  const file = `${ROOT}sitemap.xml`;
  let kept: string[] = [];
  try {
    const xml = Deno.readTextFileSync(file);
    kept = [...xml.matchAll(/<url>[\s\S]*?<\/url>/g)].map((m) => m[0])
      .filter((block) => {
        const loc = /<loc>([^<]+)<\/loc>/.exec(block)?.[1] || "";
        return !loc.startsWith(`${SITE}/leaving-cert-`) || HAND_MADE.has(loc.slice(SITE.length));
      });
  } catch {
    kept = [];
  }
  const ours = pages.map((p) =>
    `<url>\n    <loc>${SITE}${p.url}</loc>\n    <lastmod>${isoDate(p.modified)}</lastmod>\n  </url>`
  );
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  ${[...kept, ...ours].join("\n  ")}
</urlset>
`;
  Deno.writeTextFileSync(file, xml);
}

function main(): void {
  const subjects = buildModel();
  removeGenerated();
  const sitemap: { url: string; modified: Date }[] = [];

  write(HUB_SLUG, hubPage(subjects));
  sitemap.push({ url: `/${HUB_SLUG}/`, modified: latest(subjects.flatMap((s) => s.chapters.flatMap((c) => c.subs.map((x) => x.mtime)))) });

  let count = 1;
  for (const subject of subjects) {
    const links = new Map<string, string>();
    for (const ch of subject.chapters) for (const s of ch.subs) if (!links.has(norm(s.title))) links.set(norm(s.title), s.url);

    write(subject.slug, subjectPage(subject, subjects));
    sitemap.push({ url: subject.url, modified: latest(subject.chapters.flatMap((c) => c.subs.map((s) => s.mtime))) });
    count++;
    for (const ch of subject.chapters) {
      write(ch.path, chapterPage(subject, ch, subjects));
      sitemap.push({ url: ch.url, modified: latest(ch.subs.map((s) => s.mtime)) });
      count++;
      ch.subs.forEach((sub, i) => {
        write(sub.path, subsectionPage(subject, ch, i, subjects, links));
        sitemap.push({ url: sub.url, modified: sub.mtime });
        count++;
      });
    }
    const subs = subject.chapters.reduce((n, c) => n + c.subs.length, 0);
    console.log(`${subject.name.padEnd(15)} ${String(subject.chapters.length).padStart(3)} chapters ${String(subs).padStart(4)} sections`);
  }
  updateSitemap(sitemap);
  console.log(`wrote ${count} pages and sitemap.xml (${sitemap.length} generated URLs)`);
}

main();
