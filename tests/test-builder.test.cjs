const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const SKIP_SCRIPTS = new Set(["app.js", "timer.js", "onboarding.js", "auth.js", "auth-config.js"]);

// Loads every local data script app.html loads, in the same order, plus the builder.
function createContext() {
  const html = fs.readFileSync(path.join(root, "app.html"), "utf8");
  const files = [...html.matchAll(/<script src="\.\/([^"?]+)/g)]
    .map((m) => m[1])
    .filter((file) => !SKIP_SCRIPTS.has(file));
  const context = { console };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  files.forEach((file) => {
    vm.runInContext(fs.readFileSync(path.join(root, file), "utf8"), context, { filename: file });
  });
  vm.runInContext("globalThis.__courseData = COURSE_DATA", context);
  return context;
}

const context = createContext();
const TB = context.TestBuilder;
const courseData = context.__courseData;

// A light stand-in for app.js's buildSubjectChapters: one outcome per source
// outcome, falling back to the generated deck for chapters without keyTerms.
function chaptersFor(subject) {
  return courseData.chapters
    .filter((chapter) => chapter.subject === subject)
    .map((chapter) => ({
      id: chapter.id,
      title: chapter.title,
      learningOutcomes: chapter.learningOutcomes.map((lo, index) => ({
        id: `${lo.id}-core`,
        keyTerms: lo.keyTerms?.length ? lo.keyTerms : (index === 0 ? context.FLASHCARDS_DB?.[chapter.id] || [] : []),
      })),
    }));
}

function poolFor(subject, chapters = chaptersFor(subject)) {
  return TB.buildPool({
    subjectId: subject,
    breakdown: context.EXAM_BREAKDOWN?.[subject],
    chapters,
    subjectChapters: chaptersFor(subject),
    examGroupsFor: (chapter) => context.EXAM_QUESTIONS_DB.filter((group) => group.chapterId === chapter.id),
    authoredFor: (chapter) => courseData.chapters
      .find((c) => c.id === chapter.id)
      .learningOutcomes.flatMap((lo) => (lo.questions || []).map((question) => ({ outcomeId: `${lo.id}-core`, question }))),
    prompts: context.FLASHCARD_TEST_PROMPTS,
  });
}

function seeded(seed) {
  let t = seed >>> 0;
  return () => {
    t += 0x6d2b79f5;
    let r = Math.imul(t ^ (t >>> 15), 1 | t);
    r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
    return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
  };
}

const SUBJECTS = ["biology", "chemistry", "geography", "history", "home-economics", "pe"];

test("every written-recall prompt belongs to a real flashcard", () => {
  const prompts = context.FLASHCARD_TEST_PROMPTS;
  assert.ok(prompts && typeof prompts === "object", "prompts file should load");
  Object.entries(prompts).forEach(([chapterId, byTerm]) => {
    const chapter = courseData.chapters.find((c) => c.id === chapterId);
    assert.ok(chapter, `${chapterId} should be a real chapter`);
    const terms = new Set(chapter.learningOutcomes.flatMap((lo) => (lo.keyTerms || []).map((kt) => kt.term)));
    (context.FLASHCARDS_DB?.[chapterId] || []).forEach((kt) => terms.add(kt.term));
    Object.entries(byTerm).forEach(([term, prompt]) => {
      assert.ok(terms.has(term), `${chapterId}: "${term}" should match a card term exactly`);
      assert.ok(prompt.trim().length > 10, `${chapterId}: "${term}" needs a real prompt`);
      assert.doesNotMatch(prompt, /—/, `${chapterId}: "${term}" prompt should not use an em dash`);
    });
  });
});

for (const subject of SUBJECTS) {
  test(`${subject}: a whole-subject test fills the time asked for`, () => {
    const pool = poolFor(subject);
    [5, 10, 20, 45].forEach((minutes) => {
      ["flashcards", "balanced", "exam"].forEach((mix) => {
        const built = TB.assembleTest(pool, { minutes, mix, random: seeded(minutes * 7 + mix.length) });
        assert.ok(built.items.length > 0, `${minutes} min ${mix} should have questions`);
        assert.ok(built.plannedSeconds <= minutes * 60, `${minutes} min ${mix} should not overrun`);
        assert.ok(built.plannedSeconds >= minutes * 60 * 0.9, `${minutes} min ${mix} should fill at least 90% (got ${built.plannedSeconds}s)`);
        const ids = built.items.map((item) => item.id);
        assert.equal(ids.length, new Set(ids).size, "no question should repeat");
        const cards = built.items.filter((item) => item.cardId).map((item) => item.cardId);
        assert.equal(cards.length, new Set(cards).size, "no flashcard should be asked twice");
      });
    });
  });

  test(`${subject}: the mix setting shifts time between flashcards and exam questions`, () => {
    const pool = poolFor(subject);
    const share = (mix) => {
      const built = TB.assembleTest(pool, { minutes: 30, mix, random: seeded(11) });
      const flash = built.items.filter((i) => i.bucket === "flashcard").reduce((s, i) => s + i.seconds, 0);
      return flash / built.plannedSeconds;
    };
    assert.ok(share("flashcards") > share("balanced"));
    assert.ok(share("balanced") > share("exam"));
  });
}

test("a single-chapter test only asks about that chapter", () => {
  const chapter = chaptersFor("biology").find((c) => c.id === "bio16");
  const built = TB.assembleTest(poolFor("biology", [chapter]), { minutes: 5, mix: "balanced", random: seeded(3) });
  assert.ok(built.items.length >= 4);
  built.items.forEach((item) => assert.equal(item.chapterId, "bio16"));
});

test("a scope too small for the time asked fills what it can without repeating", () => {
  const chapter = chaptersFor("biology").find((c) => c.id === "bio9");
  const built = TB.assembleTest(poolFor("biology", [chapter]), { minutes: 45, mix: "flashcards", random: seeded(5) });
  assert.ok(built.plannedSeconds < 45 * 60);
  const cards = built.items.filter((i) => i.cardId).map((i) => i.cardId);
  assert.equal(cards.length, new Set(cards).size);
});

test("flashcard questions quote the card's own content", () => {
  const pool = poolFor("biology");
  const built = TB.assembleTest(pool, { minutes: 45, mix: "flashcards", random: seeded(9) });
  const byKind = (kind) => built.items.filter((i) => i.kind === kind);
  ["pick-term", "pick-definition", "cloze"].forEach((kind) => {
    assert.ok(byKind(kind).length > 0, `a long biology test should include ${kind}`);
  });
  byKind("pick-term").forEach((item) => {
    assert.equal(item.options[item.correctIndex], item.answer);
    assert.equal(new Set(item.options).size, item.options.length, "options should be distinct");
  });
  byKind("pick-definition").forEach((item) => {
    assert.equal(item.options[item.correctIndex], item.definition);
  });
  byKind("cloze").forEach((item) => {
    item.answers.forEach((answer) => assert.ok(item.definition.includes(answer), `"${answer}" should come from the card`));
    const rebuilt = item.segments.map((s) => (s.blank === undefined ? s.text : item.answers[s.blank])).join("");
    assert.equal(rebuilt, item.definition, "blanks filled in should give back the card text");
  });
  byKind("recall").forEach((item) => {
    assert.notEqual(item.prompt, item.term, "recall should use the authored prompt, not the bare term");
  });
});

test("written recall is used exactly when a card has an authored prompt", () => {
  const chapter = chaptersFor("biology").find((c) => c.id === "bio11");
  const card = chapter.learningOutcomes.flatMap((lo) => lo.keyTerms)[0];
  const prompts = { bio11: { [card.term]: "A prompt written for this card." } };
  const pool = TB.buildPool({ subjectId: "biology", chapters: [chapter], subjectChapters: chaptersFor("biology"), prompts });
  assert.equal(pool.cards.filter((c) => c.recallPrompt).length, 1);
  const built = TB.assembleTest(pool, { minutes: 45, mix: "flashcards", random: seeded(2) });
  const recall = built.items.filter((i) => i.kind === "recall");
  assert.ok(recall.length <= 1);
  recall.forEach((item) => assert.equal(item.prompt, "A prompt written for this card."));
});

test("question-style card terms reduce to the thing being asked about", () => {
  assert.equal(TB.cardSubject("What is a ligament?"), "Ligament");
  assert.equal(TB.cardSubject("What are mitochondria?"), "Mitochondria");
  assert.equal(TB.cardSubject("Who was Otto von Bismarck and what was their role in Prussian history?"), "Otto von Bismarck");
  assert.equal(TB.cardSubject("What does 'macroscopic' mean?"), "Macroscopic");
  assert.equal(TB.cardSubject("How does natural selection work?"), "Natural selection");
  assert.equal(TB.cardSubject("Hot Desert Biome"), "Hot Desert Biome");
  assert.equal(TB.cardSubject("Distinguish between internal and external stakeholders."), "");
  assert.equal(TB.cardSubject("What are the roles of the rough ER and Golgi apparatus?"), "Roles of the rough ER and Golgi apparatus");
});

test("the described term is hidden from its own description", () => {
  assert.equal(
    TB.maskSubject("The grouping of organisms. The science of classifying is taxonomy.", "Classification"),
    "The grouping of organisms. The science of ____ is taxonomy."
  );
  assert.equal(
    TB.maskSubject("A pattern of exponential population growth.", "J-shaped population curve"),
    "A pattern of exponential population growth."
  );
});

test("typed answers forgive small slips but not wrong words", () => {
  assert.ok(TB.answerMatches("mitochondria", "mitochondria"));
  assert.ok(TB.answerMatches("Mitocondria", "mitochondria"));
  assert.ok(TB.answerMatches("organize", "organise"));
  assert.ok(TB.answerMatches("alleles", "allele"));
  assert.ok(TB.answerMatches(" Glycolysis. ", "glycolysis"));
  assert.ok(!TB.answerMatches("ribosomes", "mitochondria"));
  assert.ok(!TB.answerMatches("1846", "1847"), "years must be exact");
  assert.ok(!TB.answerMatches("", "xylem"));
});

test("exam parts that need a missing source or diagram are left out", () => {
  const group = { subject: "geography", source: "LC Geography Higher 2020" };
  const part = (question, extra = {}) => ({ question, marks: 4, model: "An answer.", ...extra });
  assert.ok(TB.isAnswerablePart(part("Explain briefly the term focus, in relation to earthquakes."), group));
  assert.ok(!TB.isAnswerablePart(part("Examine the photograph and identify two land uses."), group));
  assert.ok(TB.isAnswerablePart(part("Examine the photograph and identify two land uses.", { diagram: "exam-images/x.png" }), group));
  assert.ok(!TB.isAnswerablePart(part("Give a six-figure grid reference for the station."), group));
  assert.ok(!TB.isAnswerablePart(part("Explain the term focus.", { marks: 0 }), group), "a part needs marks to self-mark against");
  assert.ok(!TB.isAnswerablePart(part("Explain the term focus.", { model: "" }), group), "a part needs an answer to mark against");

  const ordinary = { subject: "history", source: "LC History Ordinary 2015 — Q11", sectionId: "hist-section2" };
  assert.ok(!TB.isAnswerablePart({ label: "A3", question: "How long did the ships' crossing take?", marks: 6, model: "Six weeks" }, ordinary));
  assert.ok(TB.isAnswerablePart({ label: "C", question: "What were the causes of the Great Famine?", marks: 40, model: "Blight." }, ordinary));
  const documents = { subject: "history", source: "LC History Higher 2022 — Q1", sectionId: "hist-section1" };
  assert.ok(!TB.isAnswerablePart({ label: "1(a)", question: "Why was the public meeting held?", marks: 5, model: "Protest." }, documents));
});

test("scores weight each question by the time it takes", () => {
  const items = [
    { id: "a", bucket: "flashcard", kind: "pick-term", marks: 1, seconds: 30, correctIndex: 0, chapterId: "c1", outcomeId: "o1", cardId: "o1-k-1" },
    { id: "b", bucket: "exam", kind: "written", marks: 10, seconds: 270, chapterId: "c2" },
  ];
  const allRight = TB.scoreTest({ items }, { a: { choice: 0 }, b: { selfMarks: 10 } });
  assert.equal(allRight.percent, 100);
  const quickOnly = TB.scoreTest({ items }, { a: { choice: 0 }, b: { selfMarks: 0 } });
  assert.equal(quickOnly.percent, 10, "30s of 300s answered right");
  // Arrays from the vm context have their own prototype, so compare a copy.
  assert.deepEqual([...quickOnly.byOutcome.o1.correctCards], ["o1-k-1"]);
  const unmarked = TB.scoreTest({ items }, { a: { choice: 1 } });
  assert.equal(unmarked.pendingSelfMarks, 1);
  assert.equal(unmarked.percent, 0);
});

test("a cloze blank can be overridden when the student's word was right", () => {
  const item = { kind: "cloze", answers: ["xylem", "phloem"], marks: 2 };
  assert.equal(TB.markItem(item, { blanks: ["xylem", "sieve tubes"] }).earned, 1);
  assert.equal(TB.markItem(item, { blanks: ["xylem", "sieve tubes"], overrides: [false, true] }).earned, 2);
});
