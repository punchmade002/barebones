// Print the past exam questions tagged to one chapter, for writing information packages.
//   node scripts/chapter_questions.cjs <subject> <chapterId>
const vm = require("node:vm");
const fs = require("node:fs");
const path = require("node:path");

const [subject, chapterId] = process.argv.slice(2);
if (!subject || !chapterId) {
  console.error("usage: node scripts/chapter_questions.cjs <subject> <chapterId>");
  process.exit(1);
}
const context = { COURSE_DATA: { chapters: [] } };
context.window = context;
vm.createContext(context);
// Most subjects have their own bank; biology's lives in the shared exam-questions-db.js.
const own = path.join(__dirname, "..", `${subject}-exam-questions.js`);
const file = fs.existsSync(own) ? own : path.join(__dirname, "..", "exam-questions-db.js");
vm.runInContext(fs.readFileSync(file, "utf8"), context);
const questions = (context.EXAM_QUESTIONS_DB || []).filter(
  (q) => q.chapterId === chapterId && (!q.subject || q.subject === subject)
);
questions.forEach((q) => {
  console.log(`== ${q.source}`);
  (q.parts || []).forEach((part) => {
    const text = (part.question || part.prompt || "").replace(/\s+/g, " ");
    const model = (part.model || "").replace(/\s+/g, " ");
    console.log(`- [${part.marks} marks] ${text}`);
    if (model) console.log(`  answer: ${model}`);
  });
});
console.log(`${questions.length} question(s)`);
