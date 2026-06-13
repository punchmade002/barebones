# Subject template

How to add a new subject (or a new chapter to an existing one) without breaking the app.

The reference subject is **maths** (`maths1`..`maths26` in [data.js](data.js)). Copy its shape; everything else follows.

---

## 1. Where things live

```
data.js                  Source of truth: chapter list, learning outcomes, notes, keyTerms
<subject>-content.js     Optional sidecar — bulk content injected via ch("id").learningOutcomes = [...]
past-papers.js           Exam questions injected via ch("id").examQuestions.push(...)
flashcards-<subject>.js  Pre-baked atomic flashcards (Step 3, not yet built)
index.html               Script tags decide load order (data.js must come first)
```

Rule: **`data.js` is the chapter list of record.** Every chapter id the app knows about must exist there. Bulk content (long notes, lots of keyTerms) lives in sidecars to keep `data.js` scannable. Past-paper questions are *always* injected from `past-papers.js` — never inlined into `data.js`.

---

## 2. Chapter shape (canonical)

```js
{
  id: "<subj><n>",        // "bio1", "geo7", "newsubj1". Stable, kebabbed if needed.
  number: 1,              // Ordinal. Drives display ordering and the "1. Title" prefix.
  subject: "biology",     // REQUIRED for non-business. Gates filtering in app.js.
                          //   Omit for business (default), otherwise must match a SUBJECTS id.
  title: "Scientific Knowledge",
  learningOutcomes: [
    {
      id: "<subj><n>-<m>",      // "bio1-1", "geo7-3"
      code: "1.1",              // Curriculum code as text, displayed as-is
      title: "Outline the scientific method",
      notes: [                  // Rich-text concept blocks, one heading per block
        { h: "Hypothesis", b: "A testable prediction about ..." }
      ],
      keyTerms: [               // Flashcard source today (will become baked cards in Step 3)
        { term: "Hypothesis", definition: "...", section: "1.1" }
      ],
      questions: [              // Optional — short/MCQ/true-false practice items
        { type: "short", marks: 6, prompt: "...", model: "..." },
        { type: "mcq",   marks: 2, prompt: "...", options: ["a","b"], correct: 0, model: "..." },
        { type: "tf",    marks: 2, prompt: "...", correct: true, model: "..." }
      ]
    }
  ],
  examQuestions: []              // Always present (even empty). Past-papers.js .push()es into it.
}
```

**Required fields:** `id`, `number`, `title`, `learningOutcomes[].id`, `learningOutcomes[].code`, `learningOutcomes[].title`. Everything else can be empty.

**`subject` field:** required for biology, geography, PE, maths. Business chapters omit it (the runtime defaults to `"business"` — see [app.js:179](app.js#L179)).

---

## 3. Runtime flattening (important caveat)

[app.js:174 buildSubjectChapters](app.js#L174) **collapses every chapter's multi-LO structure into a single "Core Concepts" learning outcome at display time**, taking each `note.h` as the `term` and `note.b` as the `definition`. The multi-LO source structure is *kept in `data.js`* for clarity and future use, but the UI does not currently surface separate outcomes.

What this means in practice:
- Author content with multiple LOs if it makes editorial sense — they all render flattened together.
- The fields that drive flashcards today are `notes[].h` and `notes[].b` (via the flattening), plus any explicit `keyTerms[]`.
- Don't waste effort on different `code` values across LOs in the same chapter — they don't show up yet.

---

## 4. Adding a new subject — step by step

1. **Register the subject** in `SUBJECTS` at the top of [app.js](app.js) (id + title + colour).
2. **Add chapter shells** to `data.js` — one object per chapter, `subject` field set, `learningOutcomes` allowed to be a single placeholder.
3. **Optionally create `<subject>-content.js`** for bulk content; load it after `data.js` in [index.html](index.html). Sidecar uses the standard injector:
   ```js
   (function () {
     function ch(id) { return COURSE_DATA.chapters.find(c => c.id === id); }
     ch("newsubj1").learningOutcomes = [/* ... */];
   })();
   ```
4. **Map any past-paper questions** in `transform_papers.py` and re-run; `past-papers.js` will inject them.
5. **(Step 3, future)** Run the flashcard generator to produce `flashcards-<subject>.js`.

---

## 5. Cross-applicability (`appliesTo`)

Used today only by geography. Lives at the **exam-question level**, not the chapter level:

```js
examQuestions: [
  {
    id: "geo1-eq-1",
    source: "...",
    appliesTo: [
      { chapterId: "geo2", questionTitle: "Explain volcano distribution" },
      { chapterId: "geo3", questionTitle: "Impact of tectonic activity on Ireland" }
    ],
    parts: [/* ... */]
  }
]
```

Rendered as chips by [app.js:956](app.js#L956). Use it when one model answer doubles as practice for related chapters. Optional.

---

## 6. Reference example

[subject-template.js](subject-template.js) is a runnable empty skeleton. Drop it in, change the ids/titles, and the app boots a fresh subject with one chapter and one learning outcome. Build outwards from there.
