// Writes subject-index.js: every topic with its first flashcard and card count, which
// the app shows before a subject's full files load (see subject-packs.js).
//
//     deno run -A scripts/build_subject_index.ts
//
// Re-run after adding, removing or renaming topics or flashcards. The test
// tests/subject-lazy-load.test.cjs fails when the file is out of date.
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { ROOT, buildIndex, renderIndexFile } = require("./subject-index.cjs");

const out = `${ROOT}/subject-index.js`;
const source = renderIndexFile(buildIndex());
Deno.writeTextFileSync(out, source);
console.log(`Wrote subject-index.js (${(source.length / 1024).toFixed(0)} KB)`);
