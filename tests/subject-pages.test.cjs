const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");

const { SUBJECTS, buildSubjectPage, readTemplate, pageFile, updateSitemap } = require("../scripts/subject-pages.cjs");

test("every /app/<subject>/ page is up to date with app.html (run: deno run -A scripts/build_subject_pages.ts)", () => {
  const template = readTemplate();
  for (const subject of SUBJECTS) {
    assert.equal(fs.readFileSync(pageFile(subject), "utf8"), buildSubjectPage(template, subject), subject.id);
  }
});

test("a subject page names its subject, links from the site root and has its own canonical URL", () => {
  const html = buildSubjectPage(readTemplate(), SUBJECTS.find((s) => s.id === "biology"));
  assert.match(html, /<body data-subject="biology">/);
  assert.match(html, /<base href="\/" \/>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/barebones\.ie\/app\/biology\/" \/>/);
  assert.match(html, /<h1>.*Biology.*<\/h1>/);
  // Crawlable text: the course description and each chapter linked to its notes page
  assert.match(html, /<section id="subjectAbout"/);
  assert.match(html, /<li><a href="\/leaving-cert-biology\/[a-z0-9-]+\/">[^<]+<\/a><\/li>/);
  // First paint, before the scripts load: the real section tiles, placeholders for what loads later
  assert.match(html, /<div id="sectionPanel" class="section-panel page-shell">/);
  assert.match(html, /<a class="section-tile" href="app\/biology\/#flashcards">/);
  assert.match(html, /class="skeleton-block"/);
  // With <base href="/">, a bare "#notes" would point at the landing page
  assert.doesNotMatch(html, /href="#/);
});

test("sitemap keeps other pages and lists each subject page once", () => {
  const before = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://barebones.ie/</loc>
    <lastmod>2026-11-06</lastmod>
  </url>
  <url>
    <loc>https://barebones.ie/app/biology/</loc>
    <lastmod>2026-01-01</lastmod>
  </url>
</urlset>
`;
  const after = updateSitemap(before, "2026-11-16");
  assert.ok(after.includes("<loc>https://barebones.ie/</loc>"));
  assert.equal(after.split("<loc>https://barebones.ie/app/biology/</loc>").length, 2);
  assert.equal((after.match(/\/app\//g) || []).length, SUBJECTS.length);
});
