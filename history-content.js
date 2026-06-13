// History HL Content — injects flashcard keyTerms from FLASHCARDS_DB into COURSE_DATA chapters.
// Requires: data.js (COURSE_DATA) and history-flashcards.js (FLASHCARDS_DB) to be loaded first.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  var DB = window.FLASHCARDS_DB || {};
  var chapters = COURSE_DATA.chapters;

  [
    'hist-ire1', 'hist-ire2', 'hist-ire3', 'hist-ire4', 'hist-ire5', 'hist-ire6',
    'hist-eur1', 'hist-eur2', 'hist-eur3', 'hist-eur4', 'hist-eur5', 'hist-eur6',
  ].forEach(function (id) {
    var ch = chapters.find(function (c) { return c.id === id; });
    if (!ch || !DB[id] || !ch.learningOutcomes.length) return;
    ch.learningOutcomes[0].keyTerms = DB[id].map(function (card) {
      return { term: card.term, definition: card.definition, section: id };
    });
  });
})();
