// Written-recall prompts for flashcards in Test mode.
//
// In Learn mode a card's term is enough: the student knows the back holds a
// definition or a short fact. In a test that assumption does not hold, so a
// bare "What is a ligament?" leaves them guessing how much to write. Each
// prompt here names exactly what the card contains, e.g. "What does a ligament
// connect, and what does it do at a joint?", and the answer is marked against
// the card itself.
//
// Shape: FLASHCARD_TEST_PROMPTS[chapterId][card term exactly as in the data] = prompt.
// Cards without a prompt still appear in tests as multiple-choice and
// fill-the-gap questions built from the card's own wording.
//
// Each prompt is written against the card's current back. When a subject's
// cards are rewritten, its prompts must be rewritten too: the Biology set
// written for the pre-2027 cards was retired when Biology moved to the June
// 2027 specification (it is in git history, commit 2994f7c).
window.FLASHCARD_TEST_PROMPTS = Object.assign(window.FLASHCARD_TEST_PROMPTS || {}, {});
