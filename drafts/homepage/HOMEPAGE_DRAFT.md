# Homepage redraft — structure and copy

Draft 2026-11-24. Replaces the copy in `index.html`. No visual design yet; run
`/impeccable` for that pass once the copy is agreed.

## The one job

Get a Leaving Cert student from a TikTok/Instagram link to **answering their
first real exam question** in under a minute.

- **Primary action (everywhere):** `Start studying — it's free`
- **Secondary (header only):** `Sign in`
- Remove "Open app", "See how it works" and "See the method" as buttons. One verb.

## What we lead with, and why

The current page sells "flashcards + practice". Every competitor sells that.
What only barebones has today:

1. **Real past-paper questions, marked against the official marking scheme**, in
   the browser, point by point. (Shipped. PRODUCT.md calls this the
   highest-value content.)
2. **Notes cut down to what the exam actually asks.** (Shipped.)
3. **Crunch Mode** — tell it the grade you need and it hides what you don't need
   for it. (Biology pilot, not in the app yet. Becomes the hero once it ships;
   see Variant C.)

So the hero leads with #1 now, and swaps to Crunch Mode on launch.

---

## Section 1 — Hero

**Eyebrow:** For Leaving Cert students · 8 subjects

**Headline (Variant A — recommended):**
> Every past exam question. Marked like the examiner would.

**Subhead:**
> Real Leaving Cert questions back to 2015, checked against the official
> marking scheme as you answer. Learn the notes, then prove it on the paper.

**Button:** `Start studying — it's free`
**Under the button (small):** No install · Works on your phone · Higher & Ordinary

**Visual:** a real phone screenshot of a Biology exam question with a written
answer marked — two scheme points ticked, one missed, "4 / 6 marks". Not a
multiple-choice mock. (Current mockups show MCQ; LC doesn't.)

### Headline variants to A/B test
- **B:** "Stop guessing what comes up. Practise what actually did."
- **C (on Crunch Mode launch):** "Need a H3? Study for a H3."
  Subhead: "Tell barebones the grade you're after. It cuts the course down to
  just what gets you there — and shows you exactly what it cut."

---

## Section 2 — Try one now (inline demo)

**Heading:** Try a real question
**Copy:** 2023 Higher Level Biology, Q8(b). Type your answer — we'll mark it
against the scheme.

- One real question, a text box, a `Mark it` button.
- Result shows which marking-scheme points were hit and missed.
- After marking: `Save your progress — sign up free` (this is the conversion
  moment: value first, account second).

*Build note:* reuse `answer-marker.js` with one hard-coded question so it works
without an account. Pick a question that keyword-marks cleanly.

---

## Section 3 — How it works (three steps, with screenshots)

**Heading:** Two steps. Then you know where you stand.

1. **Learn it.** Notes stripped to what the exam asks, plus flashcards that
   test you on the exact point — not vague "what is…" prompts.
2. **Test it.** Timed tests mix flashcard recall with real past-paper parts.
   Pick a chapter, a few chapters, or the whole subject.
3. **See it.** Every chapter shows what you've nailed and what's still shaky,
   so tonight's study goes where the marks are.

Each step gets one real screenshot from the app (notes view, test in progress,
progress screen).

---

## Section 4 — Proof by numbers

One strip, big numbers, small labels. **Verify every figure before launch.**

| Number | Label |
|---|---|
| 3,000+ | past exam questions with marking schemes |
| 8 | subjects, Higher and Ordinary |
| 2001–2026 | years of papers (varies by subject) |
| €0 | to start |

---

## Section 5 — Subjects

**Heading:** Your subjects are in here

A grid of 8 subject tiles, each with what's included:

- Biology — notes, flashcards, exam Qs 2015–2025
- Chemistry — notes, flashcards, exam Qs 2001–2025
- Maths — worked solutions, skill lessons, exam Qs 2019–2025
- Geography — notes, flashcards, exam Qs 2017–2026
- History — notes, exam Qs 2006–2026
- Home Economics — notes, flashcards, exam Qs 2004–2026
- PE — notes, flashcards, exam Qs 2022–2026
- Business — notes (exam Qs coming)

Each tile links to that subject's free notes page (keeps the SEO value the
footer links have today).

**Under the grid:** "Your subject not here yet? Tell us" → feedback link.

---

## Section 6 — Student proof

**Heading:** From students using it

2–3 short real quotes from the current cohort, first name + year + subject
("Aoife, 6th year, Biology"). **Collect these — don't invent them.** If none
yet, cut this section rather than fake it; swap in a TikTok embed instead.

---

## Section 7 — FAQ (answers the objections, in order)

- **Is it free?** Yes, to start. [Confirm what stays free once billing ships.]
- **Is it accurate?** Questions are from SEC papers and answers follow the
  official marking schemes. Spot something wrong? Flag it in one tap.
- **Higher or Ordinary?** Both, where the papers exist.
- **Do I need to download anything?** No. It runs in your browser on phone or
  laptop.
- **Is barebones made by the SEC?** No — we're independent, made in Ireland.

---

## Section 8 — Final call to action

**Heading:** The exam is in June. Start tonight.
**Button:** `Start studying — it's free`
**Small:** Already have an account? Sign in

---

## Footer

Keep as is (subject notes links, points calculator, contact, socials,
SEC disclaimer). Drop the "Method / Features" anchors.

---

## Also change

- **JSON-LD `description`** in `index.html` → "Leaving Cert study app: real past
  exam questions marked against the official marking scheme, plus notes and
  flashcards for 8 subjects."
- **`<title>` / meta description** to match the new headline.
- **Delete the stacked hero variants** in the current markup, or keep only the
  A/B slots actually being tested.
- **Remove "AI turns each topic into flashcards / drop in a topic"** — the app
  doesn't work like that any more.

## Measure

Before shipping, add tracking for: hero button clicks, demo "Mark it" clicks,
demo → sign-up, and sign-ups by traffic source (TikTok / Instagram / Google).
Success = sign-up rate from homepage visits, compared to the old page.

## Open questions

1. Is Crunch Mode close enough to launch to lead with it (Variant C) now?
2. What's the free tier once Stripe billing ships? The FAQ and "€0" depend on it.
3. Do we have real student quotes yet?
