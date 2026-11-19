// One page per subject at /app/<subject>/, built from app.html so each has its own
// URL, title, description and crawlable header. app.js reads <body data-subject>
// and shows that subject; the rest of the page is app.html unchanged.
//
//     deno run -A scripts/build_subject_pages.ts
//
// tests/subject-pages.test.cjs fails when a page is out of date with app.html.
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const ROOT = path.join(__dirname, "..");
const SITE = "https://barebones.ie";

const SUBJECTS = [
  { id: "biology", name: "Biology", covers: "cells, biomolecules, genetics, human biology, plants and ecology" },
  { id: "chemistry", name: "Chemistry", covers: "atomic structure, bonding, stoichiometry, rates, equilibrium and organic chemistry" },
  { id: "geography", name: "Geography", covers: "physical geography, regions, economic activity and the options" },
  { id: "history", name: "History", covers: "the Irish and European topics, documents-based study and essay writing" },
  { id: "business", name: "Business", covers: "people in business, enterprise, management and the domestic and international environment" },
  { id: "home-economics", name: "Home Economics", covers: "food science, nutrition, the family and resource management" },
  { id: "pe", name: "PE", covers: "physiology, skill learning, sport psychology and physical activity" },
  {
    id: "maths", name: "Maths",
    title: "Leaving Cert Maths: Past Paper Questions & Paper Guide",
    description: "Leaving Cert Maths past exam questions with worked solutions, sorted by chapter and by type, plus whole past papers and a guide to both papers.",
  },
  // Papers-only subjects (PAPERS_ONLY_SUBJECTS in dashboard.js), each paged once its archive is built
  ...papersOnly([
    ["english", "English"], ["irish", "Irish"], ["french", "French"], ["construction-studies", "Construction Studies"],
    ["spanish", "Spanish"], ["art", "Art"], ["physics", "Physics"],
  ]),
];

function papersOnly(subjects) {
  const archive = fs.readFileSync(path.join(ROOT, "exam-papers.js"), "utf8");
  return subjects.filter(([id]) => archive.includes(`"${id}": {`)).map(([id, name]) => ({
    id, name,
    title: `Leaving Cert ${name}: Past Exam Papers & Marking Schemes`,
    description: `Every Leaving Cert ${name} exam paper and marking scheme from the SEC archive, by year and level, to open and write on.`,
  }));
}

const escapeHtml = (value) => String(value)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function pageMeta(subject) {
  const title = subject.title || `Leaving Cert ${subject.name}: Flashcards, Notes & Past Papers`;
  const description = subject.description
    || `Leaving Cert ${subject.name} study: flashcards, notes, timed tests and past exam questions by chapter and type, covering ${subject.covers}.`;
  return { title: `${title} | barebones`, description, url: `${SITE}/app/${subject.id}/` };
}

// The section tiles are drawn by app.js; the description stays in the page's meta tags.
// "Leaving Cert" stays in the heading for search engines and screen readers, hidden on screen.
function renderHead(subject) {
  // Links are written from the site root: the page sets <base href="/">
  return `<header class="subject-head">
            <h1><a class="subject-head-back" href="app.html"><span class="sr-only">Leaving Cert </span>${escapeHtml(subject.name)}</a></h1>
            <p id="subjectSectionTitle" class="subject-section-title"></p>
          </header>`;
}

// The subject's chapters as its notes hub lists them (written by scripts/build_seo_pages.ts)
function notesChapters(subject) {
  const hub = path.join(ROOT, `leaving-cert-${subject.id}`, "index.html");
  if (!fs.existsSync(hub)) return [];
  const re = new RegExp(`<a href="(/leaving-cert-${subject.id}/[^"/]+/)">([^<]+)<`, "g");
  const seen = new Set();
  return [...fs.readFileSync(hub, "utf8").matchAll(re)]
    .filter(([, href]) => !seen.has(href) && seen.add(href))
    .map(([, href, title]) => ({ href, title: title.trim() })); // title is already escaped HTML
}

// Plain text about the subject for search engines and signed-out visitors, linking each chapter
// to its notes. app.js moves it under the section tiles while signed out; signed-in users never
// see it (the head script marks <html class="bb-signed-in"> before first paint).
function renderAbout(subject) {
  const chapters = notesChapters(subject);
  return `<section id="subjectAbout" class="subject-about" aria-labelledby="subjectAboutTitle">
            <h2 id="subjectAboutTitle">Leaving Cert ${escapeHtml(subject.name)} on barebones</h2>
            <p>${escapeHtml(pageMeta(subject).description)}</p>${chapters.length ? `
            <h3>${escapeHtml(subject.name)} chapters</h3>
            <ol class="subject-about-chapters">
              ${chapters.map((c) => `<li><a href="${c.href}">${c.title}</a></li>`).join("\n              ")}
            </ol>` : ""}
          </section>`;
}

// The app's own tile and placeholder code (dashboard.js, with aac-guides.js for the coursework
// sections), run here so the page's first paint matches what app.js draws over it
function appKit() {
  const kit = {
    window: { BarebonesUsage: { localDay: () => "" } },
    accountAuth: { configured: true }, // study time not loaded yet: its placeholder
    escapeHtml: (value) => String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#39;"), // as in app.js
  };
  vm.createContext(kit);
  for (const file of ["aac-guides.js", "dashboard.js"]) {
    vm.runInContext(fs.readFileSync(path.join(ROOT, file), "utf8"), kit, { filename: file });
  }
  return kit;
}

// What the section panel shows before app.js runs: the subject's tiles with a placeholder for the
// study-time graph (signed in) or the sign-in buttons and about text (signed out). A link straight
// to a section (#flashcards…) gets placeholder rows instead (the head script marks <html>).
function renderShell(subject, kit) {
  return `<div id="sectionPanel" class="section-panel page-shell">
            <div class="shell-home">
              ${kit.sectionTilesHtml(subject.id)}
              <div class="shell-signed-in">${kit.studyTimeBlockHtml(subject.id)}</div>
              <div class="shell-signed-out">
                <div class="section-locked-actions">
                  <button class="button-primary" type="button" data-auth-mode="signup">Make an account</button>
                  <button class="button-secondary" type="button" data-auth-mode="signin">Sign in</button>
                </div>
                ${renderAbout(subject)}
              </div>
            </div>
            <div class="shell-section">${kit.skeletonHtml("rows")}</div>
          </div>`;
}

function replaceOnce(html, find, replacement) {
  if (html.split(find).length !== 2) throw new Error(`app.html should contain ${JSON.stringify(find)} exactly once`);
  return html.replace(find, () => replacement);
}

function buildSubjectPage(template, subject, kit = appKit()) {
  const { title, description, url } = pageMeta(subject);
  let html = template;
  html = replaceOnce(html, "<!doctype html>\n", "<!doctype html>\n<!-- Generated by scripts/build_subject_pages.ts from app.html. Edit app.html, then re-run it. -->\n");
  html = replaceOnce(html, '<meta charset="UTF-8" />', '<meta charset="UTF-8" />\n    <base href="/" />');
  html = replaceOnce(html, "<title>bare bones</title>", [
    `<title>${escapeHtml(title)}</title>`,
    `<meta name="description" content="${escapeHtml(description)}" />`,
    `<link rel="canonical" href="${url}" />`,
    `<meta property="og:type" content="website" />`,
    `<meta property="og:site_name" content="barebones" />`,
    `<meta property="og:url" content="${url}" />`,
    `<meta property="og:title" content="${escapeHtml(title)}" />`,
    `<meta property="og:description" content="${escapeHtml(description)}" />`,
  ].join("\n    "));
  html = replaceOnce(html, "<body>", `<body data-subject="${subject.id}">`);
  html = replaceOnce(html, "<!-- subject-head -->", renderHead(subject));
  html = replaceOnce(html, '<div id="sectionPanel" class="section-panel hidden"></div>', renderShell(subject, kit));
  return html;
}

function readTemplate() {
  return fs.readFileSync(path.join(ROOT, "app.html"), "utf8");
}

function pageFile(subject) {
  return path.join(ROOT, "app", subject.id, "index.html");
}

// Adds or refreshes the /app/<subject>/ entries, leaving every other entry alone
function updateSitemap(xml, today) {
  const kept = [...xml.matchAll(/<url>[\s\S]*?<\/url>/g)].map((m) => m[0])
    .filter((block) => !block.includes(`<loc>${SITE}/app/`));
  const ours = SUBJECTS.map((s) => `<url>\n    <loc>${SITE}/app/${s.id}/</loc>\n    <lastmod>${today}</lastmod>\n  </url>`);
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  ${[...kept, ...ours].join("\n  ")}
</urlset>
`;
}

module.exports = { ROOT, SUBJECTS, appKit, buildSubjectPage, readTemplate, pageFile, updateSitemap };
