// Home Economics Content — injects flashcard keyTerms from FLASHCARDS_DB into COURSE_DATA chapters.
// Requires: data.js (COURSE_DATA) and home-economics-flashcards.js (FLASHCARDS_DB) to be loaded first.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  var DB = window.FLASHCARDS_DB || {};
  var chapters = COURSE_DATA.chapters;

  [
    'hom-carbohydrates', 'hom-proteins', 'hom-lipids', 'hom-vitamins-minerals',
    'hom-digestion-metabolism', 'hom-energy-nutrition', 'hom-meat-preparation',
    'hom-fish-seafood', 'hom-dairy-eggs', 'hom-cereals-grains', 'hom-cooking-methods',
    'hom-food-preservation', 'hom-food-safety', 'hom-meal-planning', 'hom-food-additives',
    'hom-consumer-rights', 'hom-personal-finance', 'hom-housing', 'hom-textiles-fibres',
    'hom-clothing-selection', 'hom-environmental-issues', 'hom-appliances-equipment',
  ].forEach(function (id) {
    var ch = chapters.find(function (c) { return c.id === id; });
    if (!ch || !DB[id] || !ch.learningOutcomes.length) return;
    ch.learningOutcomes[0].keyTerms = DB[id].map(function (card) {
      return { term: card.term, definition: card.definition, section: id };
    });
  });
})();
