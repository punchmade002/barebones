// Home Economics content — registers the subject's chapters into COURSE_DATA so the app can
// navigate them, and attaches the pipeline-built flashcards as each chapter's keyTerms.
// Past-paper exam questions live in home-economics-exam-questions.js (EXAM_QUESTIONS_DB).
// Chapters/ids come from the pipeline scaffold (pipeline/scaffold/home-economics.json).
(function () {
  if (typeof COURSE_DATA === 'undefined' || !COURSE_DATA.chapters) return;
  var fc = (typeof window !== 'undefined' && window.FLASHCARDS_DB) || {};

  // [chapterId, title] — order = display order. Ids match the scaffold + exam-question chapterIds.
  var CHAPTERS = [
    ['hom-nutrition-nutrients', 'Nutrition and Nutrients'],
    ['hom-digestion-food-science', 'Digestion and Food Science'],
    ['hom-food-choice-meal-planning', 'Food Choice and Meal Planning'],
    ['hom-food-preparation-cooking', 'Food Preparation and Cooking Methods'],
    ['hom-food-preservation', 'Food Preservation and Storage'],
    ['hom-food-safety', 'Food Safety and Hygiene'],
    ['hom-consumer-protection', 'Consumer Protection and Rights'],
    ['hom-budgeting-finance', 'Budgeting and Financial Planning'],
    ['hom-textiles-fabrics', 'Textiles and Fabric Properties'],
    ['hom-household-equipment', 'Household Equipment and Appliances'],
    ['hom-environment-sustainability', 'Environmental Awareness and Sustainability'],
    ['hom-housing-accommodation', 'Housing and Accommodation'],
    ['hom-health-wellbeing', 'Health and Wellbeing'],
    ['hom-food-additives-quality', 'Food Additives and Product Quality']
  ];

  CHAPTERS.forEach(function (pair, i) {
    var id = pair[0], title = pair[1];
    if (COURSE_DATA.chapters.some(function (c) { return c.id === id; })) return; // idempotent
    var keyTerms = (fc[id] || []).map(function (c) {
      return { term: c.term, definition: c.definition, section: c.section || title, type: c.type || 'concept' };
    });
    COURSE_DATA.chapters.push({
      id: id,
      number: i + 1,
      subject: 'home-economics',
      title: title,
      examQuestions: [],
      learningOutcomes: [
        { id: id + '-core', code: 'HE' + (i + 1), title: 'Core Concepts', notes: [], keyTerms: keyTerms, questions: [] }
      ]
    });
  });
})();
