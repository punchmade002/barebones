// Targeted exam-style questions for Chemistry outcomes lacking a written Test item.
// Requires chemistry-content.js to be loaded first. Existing authored questions are
// preserved; these additions only fill uncovered outcomes.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  function q(marks, prompt, model) {
    return { type: "short", marks: marks, prompt: prompt, model: model };
  }

  var ADDITIONS = {
  };

  Object.keys(ADDITIONS).forEach(function (outcomeId) {
    COURSE_DATA.chapters.some(function (chapter) {
      var outcome = (chapter.learningOutcomes || []).find(function (item) { return item.id === outcomeId; });
      if (!outcome) return false;
      outcome.questions = (outcome.questions || []).concat(ADDITIONS[outcomeId]);
      return true;
    });
  });
})();
