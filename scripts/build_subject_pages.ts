// Writes /app/<subject>/index.html for every subject (see scripts/subject-pages.cjs)
// and their sitemap.xml entries.
//
//     deno run -A scripts/build_subject_pages.ts
//
// Re-run after any change to app.html; tests/subject-pages.test.cjs fails until you do.
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { ROOT, SUBJECTS, buildSubjectPage, readTemplate, pageFile, updateSitemap } = require("./subject-pages.cjs");

const template = readTemplate();
for (const subject of SUBJECTS) {
  const file = pageFile(subject);
  Deno.mkdirSync(file.replace(/index\.html$/, ""), { recursive: true });
  Deno.writeTextFileSync(file, buildSubjectPage(template, subject));
}
const sitemap = `${ROOT}/sitemap.xml`;
Deno.writeTextFileSync(sitemap, updateSitemap(Deno.readTextFileSync(sitemap), new Date().toISOString().slice(0, 10)));
console.log(`Wrote ${SUBJECTS.length} subject pages under app/ and updated sitemap.xml`);
