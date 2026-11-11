// Each subject's notes, flashcards and written questions are most of the app's
// download (~12 MB), so they load only when a student opens one of that subject's
// topics. Until then the app shows every topic from subject-index.js (its first
// flashcard and a card count).
//
// Files load in the order listed, which is the order the old <script> tags used:
// some files build on the one before (e.g. biology-test-questions.js needs
// bio-content.js). Bump a file's ?v= when it changes, as with the tags in app.html.
// After adding, removing or renaming topics, re-run: deno run -A scripts/build_subject_index.ts
(function () {
  var PACKS = {
    business: ["./business-notes.js?v=2"],
    pe: [
      "./pe-content.js?v=1",
      "./pe-flashcards.js?v=3",
      "./pe-pipeline-content.js?v=4",
      "./pe-test-questions.js?v=3",
      "./pe-notes.js?v=3",
    ],
    biology: [
      "./bio-content.js?v=3",
      "./biology-test-questions.js?v=2",
      "./biology-notes.js?v=4",
    ],
    chemistry: [
      "./chemistry-content.js?v=5",
      "./chemistry-test-questions.js?v=4",
      "./chemistry-notes.js?v=3",
    ],
    history: [
      "./history-test-questions.js?v=3",
      "./history-notes.js?v=1",
    ],
    "home-economics": [
      "./home-economics-flashcards.js?v=4",
      "./home-economics-test-questions.js?v=2",
      "./home-economics-notes.js?v=4",
    ],
    geography: [
      "./geography-test-questions.js?v=1",
      "./geography-notes.js?v=23",
    ],
  };
  var loaded = new Set();
  var pending = new Map();

  function has(subjectId) {
    return Object.prototype.hasOwnProperty.call(PACKS, subjectId);
  }

  function isLoaded(subjectId) {
    return !has(subjectId) || loaded.has(subjectId);
  }

  // Files that already ran are never fetched again, so retrying after a network
  // error doesn't apply a file's data to COURSE_DATA twice.
  var ranFiles = new Set();

  function loadScript(src) {
    if (ranFiles.has(src)) return Promise.resolve();
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = src;
      script.onload = function () {
        ranFiles.add(src);
        resolve();
      };
      script.onerror = function () {
        script.remove();
        reject(new Error("Could not load " + src));
      };
      document.head.appendChild(script);
    });
  }

  function load(subjectId) {
    if (isLoaded(subjectId)) return Promise.resolve();
    if (pending.has(subjectId)) return pending.get(subjectId);
    var promise = PACKS[subjectId].reduce(function (chain, src) {
      return chain.then(function () { return loadScript(src); });
    }, Promise.resolve()).then(function () {
      if (typeof globalThis.buildGeneratedNotes === "function") {
        globalThis.buildGeneratedNotes(subjectId);
      }
      loaded.add(subjectId);
      pending.delete(subjectId);
    }, function (error) {
      pending.delete(subjectId);
      throw error;
    });
    pending.set(subjectId, promise);
    return promise;
  }

  globalThis.SubjectPacks = { has: has, isLoaded: isLoaded, load: load, files: PACKS };
})();
