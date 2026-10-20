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
const context = {};
context.window = context;
vm.createContext(context);
const file = path.join(__dirname, "..", `${subject}-exam-questions.js`);
vm.runInContext(fs.readFileSync(file, "utf8"), context);
const questions = (context.EXAM_QUESTIONS_DB || []).filter((q) => q.chapterId === chapterId);
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
