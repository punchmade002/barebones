// Builds each subject's chapter → subsection → flashcard structure from COURSE_DATA
// (data.js plus whatever subject files have been loaded on top of it).
//
// Kept apart from app.js so scripts/build_subject_index.ts can run the exact same
// logic at build time to produce subject-index.js (the first card of every topic),
// which is what the app shows before a subject's full files are loaded.
// Pure functions only: nothing in here may touch the DOM.

const FALLBACK_CHAPTERS = [
  { id: "ch1", title: "1. Key Stakeholders", learningOutcomes: buildOutcomes("1") },
  { id: "ch6", title: "6. Enterprise", learningOutcomes: buildOutcomes("6") },
  { id: "ch7", title: "7. Idea Development", learningOutcomes: buildOutcomes("7") },
  { id: "ch8", title: "8. Business Planning", learningOutcomes: buildOutcomes("8") },
  { id: "ch9", title: "9. Target Market", learningOutcomes: buildOutcomes("9") },
  { id: "ch10", title: "10. Operations and Finance", learningOutcomes: buildOutcomes("10") },
  { id: "ch11", title: "11. Growth and Development", learningOutcomes: buildOutcomes("11") },
  { id: "ch12", title: "12. Managing Risk", learningOutcomes: buildOutcomes("12") },
  { id: "ch16", title: "16. The Rationale for Planning", learningOutcomes: buildOutcomes("16") },
  { id: "ch17", title: "17. Consumer", learningOutcomes: buildOutcomes("17") },
];

function buildOutcomes(ch) {
  const vocab = chapterVocabulary(ch);
  return [
    {
      id: `lo-${ch}-1`,
      code: `${ch}.1`,
      title: "Foundation knowledge",
      keyTerms: vocab.slice(0, 2),
    },
    {
      id: `lo-${ch}-2`,
      code: `${ch}.2`,
      title: "Understanding and analysis",
      keyTerms: vocab.slice(2, 4),
    },
    {
      id: `lo-${ch}-3`,
      code: `${ch}.3`,
      title: "Application and judgement",
      keyTerms: vocab.slice(4),
    },
  ];
}

function chapterVocabulary(ch) {
  const map = {
    "1": [
      t("Stakeholder", "A person or group affected by business decisions."),
      t("Internal stakeholder", "A stakeholder inside the business, such as staff or managers."),
      t("External stakeholder", "A stakeholder outside the business, such as customers or suppliers."),
      t("Stakeholder conflict", "A clash where two stakeholder groups want different outcomes."),
      t("Stakeholder mapping", "Ranking stakeholders by their power and level of interest."),
    ],
    "6": [
      t("Entrepreneurship", "Starting and growing a business while taking personal risk."),
      t("Intrapreneurship", "Creating new ideas from inside an existing company."),
      t("Innovation", "Improving a product, service, or process to create value."),
      t("Competitive advantage", "A strength that helps a firm outperform rivals."),
      t("Enterprise support", "Funding, mentoring, or training that helps firms grow."),
    ],
    "7": [
      t("Idea source", "Where a business idea comes from, such as customers or hobbies."),
      t("Market trend", "A direction of change in customer behaviour or demand."),
      t("Design thinking", "A user-focused method of solving problems in stages."),
      t("Prototype", "An early model used to test and improve an idea."),
      t("Feasibility study", "A check of whether an idea is practical and profitable."),
    ],
    "8": [
      t("Business plan", "A written plan of goals, strategy, and financial expectations."),
      t("Executive summary", "A short section explaining the core business idea."),
      t("Market analysis", "Research on customers, competitors, and demand size."),
      t("Cash flow forecast", "A prediction of money entering and leaving the business."),
      t("Operational plan", "How daily activities, staffing, and delivery will run."),
    ],
    "9": [
      t("Target market", "The specific group of customers a business chooses to serve."),
      t("Segmentation", "Dividing a market into groups with similar traits."),
      t("Positioning", "How a business wants customers to view its product."),
      t("Consumer profile", "A summary of customer needs, behaviour, and preferences."),
      t("Value proposition", "A clear reason why customers should choose this product."),
    ],
    "10": [
      t("Operations", "The processes used to produce and deliver goods or services."),
      t("Fixed cost", "A cost that stays the same regardless of output level."),
      t("Variable cost", "A cost that changes as output increases or decreases."),
      t("Break-even point", "The sales level where total revenue equals total costs."),
      t("Working capital", "Short-term money needed for day-to-day operations."),
    ],
    "11": [
      t("Business growth", "An increase in sales, output, market share, or staff."),
      t("Internal growth", "Growth funded from the business's own profits."),
      t("External growth", "Growth by joining with or buying another business."),
      t("Economies of scale", "Lower average costs when production volume increases."),
      t("Growth risk", "Problems that can appear when expanding too quickly."),
    ],
    "12": [
      t("Risk", "The chance that events will damage business performance."),
      t("Risk assessment", "Identifying threats and evaluating their likely impact."),
      t("Contingency plan", "A backup action plan for disruptions."),
      t("Insurance", "Paying a premium to protect against financial losses."),
      t("Compliance", "Following legal and regulatory rules for business activity."),
    ],
    "14": [
      t("Leadership", "Influencing people to achieve shared goals."),
      t("Management", "Planning, organizing, and controlling resources."),
      t("Delegation", "Giving responsibility for tasks to appropriate team members."),
      t("Motivation", "Encouraging people to perform effectively."),
      t("Communication", "Sharing clear information across the business."),
    ],
    "16": [
      t("Planning rationale", "The reason planning improves outcomes and reduces uncertainty."),
      t("Strategic objective", "A long-term target that guides major decisions."),
      t("Tactical plan", "A medium-term plan that supports strategic goals."),
      t("Operational target", "A short-term measurable goal for daily execution."),
      t("Performance review", "Checking results against plans and improving where needed."),
    ],
    "17": [
      t("Consumer right", "A legal protection for buyers of goods and services."),
      t("Redress", "A remedy such as repair, replacement, refund, or compensation."),
      t("Distance selling", "Buying by internet, phone, or mail rather than in-store."),
      t("GDPR", "EU law that protects personal data and privacy rights."),
      t("Informed decision", "A choice made after comparing quality, value, and risk."),
    ],
  };
  return map[ch] || map["1"];
}

function t(term, definition) {
  return { term, definition };
}

function buildSubjectChapters(subjectId) {
  const dataChapters = getExternalCourseData()?.chapters;
  if (!Array.isArray(dataChapters) || !dataChapters.length) {
    return subjectId === "business" ? FALLBACK_CHAPTERS : [];
  }
  const filtered = dataChapters.filter((c) => (c.subject || "business") === subjectId);
  if (!filtered.length) {
    return subjectId === "business" ? FALLBACK_CHAPTERS : [];
  }

  const results = [];
  for (const chapter of filtered) {
    const los = chapter.learningOutcomes || [];
    // Pipeline-generated subject packs populate FLASHCARDS_DB directly. A generated deck must
    // remain visible even when there is no hand-written *-content.js adapter for the subject.
    const generatedTerms = Array.isArray(globalThis.FLASHCARDS_DB?.[chapter.id])
      ? globalThis.FLASHCARDS_DB[chapter.id]
      : [];
    const hasInjected = generatedTerms.length > 0
      || los.some((lo) => lo.keyTerms && lo.keyTerms.length > 0);

    if (hasInjected && los.length > 1) {
      // A chapter holds many learning outcomes. Keep each LO as an outcome
      // inside its chapter — never promote one to a chapter of its own.
      const outcomes = los
        .map((lo, loIndex) => ({
          id: `${lo.id}-core`,
          code: lo.code,
          title: lo.title,
          keyTerms: (lo.keyTerms && lo.keyTerms.length)
            ? lo.keyTerms
            : ((lo.notes || []).length
                ? (lo.notes || []).map((note, idx) => ({
                    term: note.h || `${lo.title} ${idx + 1}`,
                    definition: note.b || (note.points || []).join(" "),
                    section: lo.title,
                  }))
                : (loIndex === 0 ? generatedTerms : [])),
        }))
        .filter((lo) => lo.keyTerms.length);

      if (outcomes.length) {
        results.push({
          id: chapter.id,
          title: `${chapter.number}. ${chapter.title}`,
          learningOutcomes: outcomes,
        });
        continue;
      }
      // Nothing usable on any outcome — fall through to the merged shape below.
    }

    // Single-LO chapters, or chapters without injected keyTerms: one merged outcome.
    results.push({
      id: chapter.id,
      title: `${chapter.number}. ${chapter.title}`,
      learningOutcomes: [
        {
          id: `${chapter.id}-core`,
          code: `${chapter.number}.0`,
          title: "Core Concepts",
          keyTerms: ensureMinimumConcepts(
            los.flatMap((lo, loIndex) =>
              (lo.keyTerms && lo.keyTerms.length)
                ? lo.keyTerms
                : ((lo.notes || []).length
                    ? (lo.notes || []).map((note, idx) => ({
                        term: note.h || `${lo.title} ${idx + 1}`,
                        definition: note.b || (note.points || []).join(" "),
                        section: lo.title || `Section ${loIndex + 1}`,
                      }))
                    : (loIndex === 0 ? generatedTerms : []))
            ),
            chapter
          ),
        },
      ],
    });
  }
  return results;
}

function getExternalCourseData() {
  try {
    // COURSE_DATA is declared in data.js as a top-level const.
    // It exists as a global lexical binding, not as globalThis.COURSE_DATA.
    if (typeof COURSE_DATA !== "undefined" && COURSE_DATA?.chapters) {
      return COURSE_DATA;
    }
  } catch (error) {
    // Ignore and fall back to local chapter data.
  }
  return null;
}

function ensureMinimumConcepts(points, chapter) {
  const base = Array.isArray(points) ? points.filter((p) => p.term || p.definition) : [];
  if (base.length >= 5) return base; // Keep all original notes when already sufficient.
  if (base.length === 0) return []; // No real content — don't generate placeholder fillers.

  const fillers = [];
  (chapter.learningOutcomes || []).forEach((lo, idx) => {
    fillers.push({
      term: lo.title || `Concept ${idx + 1}`,
      definition: `Explain ${lo.title || "this concept"} with one business example.`,
      section: lo.code || `Section ${idx + 1}`,
    });
  });

  let i = 0;
  while (base.length + fillers.length < 5) {
    fillers.push({
      term: `Core Review Point ${i + 1}`,
      definition: `Summarise one key idea from Chapter ${chapter.number} and apply it to a real business scenario.`,
      section: "Chapter Review",
    });
    i += 1;
  }

  return [...base, ...fillers].slice(0, 5);
}

// Until a subject's own files have loaded (subject-packs.js), its topics come from
// subject-index.js: the same chapters and subsections, each holding only its first
// flashcard plus a cardCount of how many it really has.
function initialSubjectChapters(subjectId) {
  const packs = globalThis.SubjectPacks;
  const index = globalThis.SUBJECT_INDEX?.[subjectId];
  if (index && packs?.has(subjectId) && !packs.isLoaded(subjectId)) {
    return index.chapters.map((chapter) => ({
      ...chapter,
      learningOutcomes: chapter.learningOutcomes.map((lo) => ({ ...lo, keyTerms: lo.keyTerms.slice() })),
    }));
  }
  return buildSubjectChapters(subjectId);
}

// How many flashcards a subsection has, including ones not downloaded yet.
function outcomeCardTotal(outcome) {
  return Number.isFinite(outcome?.cardCount) ? outcome.cardCount : (outcome?.keyTerms || []).length;
}
