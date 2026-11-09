// Past-paper question banks are most of the app's download (~17 MB), so each
// subject's bank loads only when that subject is opened instead of on every visit.
// A pack appends its questions to window.EXAM_QUESTIONS_DB, like the old <script> tags did.
// Bump a pack's ?v= when its file changes, as with the tags in app.html.
(function () {
  var PACKS = {
    biology: "./biology-exam-questions.js?v=1",
    history: "./history-exam-questions.js?v=2",
    chemistry: "./chemistry-exam-questions.js?v=2",
    "home-economics": "./home-economics-exam-questions.js?v=2",
    geography: "./geography-exam-questions.js?v=2",
    pe: "./pe-exam-questions.js?v=4",
  };
  var loaded = new Set();
  var pending = new Map();

  function isLoaded(subjectId) {
    return !PACKS[subjectId] || loaded.has(subjectId);
  }

  function load(subjectId) {
    if (isLoaded(subjectId)) return Promise.resolve();
    if (pending.has(subjectId)) return pending.get(subjectId);
    var promise = new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = PACKS[subjectId];
      script.onload = function () {
        loaded.add(subjectId);
        pending.delete(subjectId);
        if (typeof window.refreshGeneratedExamBlueprints === "function") {
          window.refreshGeneratedExamBlueprints(subjectId);
        }
        resolve();
      };
      script.onerror = function () {
        pending.delete(subjectId);
        script.remove();
        reject(new Error("Could not load past-paper questions for " + subjectId));
      };
      document.head.appendChild(script);
    });
    pending.set(subjectId, promise);
    return promise;
  }

  window.ExamPacks = { isLoaded: isLoaded, load: load };
})();
