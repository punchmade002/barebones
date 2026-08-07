# Relevant resources

This directory is the subject-level reference layer for barebones. It sits beside the
existing chapter content rather than replacing it.

Every subject entry contains:

- one verified NCCA syllabus or curriculum specification PDF;
- the matching source URL and effective-date metadata;
- a SimpleStudy research record;
- SimpleStudy's chapter structure;
- concise research insights linked to a chapter where possible;
- original solved examples informed by the research, without copying subscription text.

## Data shape

Edit `relevant-resources.js`. Each subject follows this shape:

```js
{
  syllabus: {
    title: "",
    path: "./relevant-resources/syllabi/subject.pdf",
    sourceUrl: "",
    documentType: "Syllabus",
    effectiveFrom: "",
    status: "Current",
    authority: "National Council for Curriculum and Assessment (NCCA)",
    verifiedAt: "YYYY-MM-DD"
  },
  simpleStudy: {
    source: "SimpleStudy",
    status: "complete",
    researchedAt: "YYYY-MM-DD",
    courseUrl: "",
    chapterStructure: [
      { id: "stable-id", title: "Chapter title", sections: ["Section one"] }
    ],
    insights: [
      {
        id: "stable-id",
        chapterId: "local-chapter-id",
        title: "What the learner needs to know",
        summary: "A concise, original synthesis.",
        sourceLabel: "SimpleStudy",
        sourceUrl: ""
      }
    ],
    solvedExamples: [
      {
        id: "stable-id",
        chapterId: "local-chapter-id",
        title: "Example title",
        question: "An original exam-style question.",
        steps: ["First step", "Second step"],
        answer: "A concise final answer.",
        sourceLabel: "Original example informed by SimpleStudy research",
        sourceUrl: ""
      }
    ]
  }
}
```

Use stable IDs. Keep quotations out of this layer; synthesize notes and write fresh
worked examples. Preserve the source page URL for provenance.

## Runtime behavior

`app.html` loads this file after the subject content files and before `app.js`. The
Resources tab reads `window.RELEVANT_RESOURCES`. If SimpleStudy research has not been
completed yet, the UI shows the verified syllabus and the app's current chapter
structure with a clear research status rather than invented content.
