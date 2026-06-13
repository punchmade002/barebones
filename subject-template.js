// Subject template — copy this file when adding a new subject.
//
// 1. Rename the chapter ids ("newsubj1" → "<your-subj><n>").
// 2. Set `subject` to the SUBJECTS id you added in app.js.
// 3. Paste this fragment into <subject>-content.js OR splice the chapter
//    object straight into COURSE_DATA.chapters in data.js.
//
// See SUBJECT_TEMPLATE.md for the full spec.

(function () {
  if (typeof COURSE_DATA === "undefined") return;

  COURSE_DATA.chapters.push({
    id: "newsubj1",
    number: 1,
    subject: "newsubj",
    title: "Chapter title",
    learningOutcomes: [
      {
        id: "newsubj1-1",
        code: "1.1",
        title: "Learning outcome title",
        notes: [
          { h: "Concept heading", b: "Concept body — one paragraph per heading." }
        ],
        keyTerms: [
          { term: "Term", definition: "Definition.", section: "1.1" }
        ],
        questions: []
      }
    ],
    examQuestions: []
  });
})();
