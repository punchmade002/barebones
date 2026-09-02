// Replace the legacy PE chapter shell with the pipeline chapter taxonomy.
//
// The generated PE questions and flashcards use stable `pe-*` chapter ids.
// app.js builds its visible subject tree from COURSE_DATA, so those ids must be
// present there before app.js initializes.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  var decks = globalThis.FLASHCARDS_DB || {};
  var legacyChapters = new Map(
    COURSE_DATA.chapters
      .filter(function (chapter) { return chapter.subject === "pe"; })
      .map(function (chapter) { return [chapter.id, chapter]; })
  );
  var legacySources = {
    "pe-learning-skill-technique": ["pe5", "pe6"],
    "pe-performance-demands": ["pe1", "pe3", "pe4"],
    "pe-structures-strategies-roles-conventions": ["pe7", "pe9"],
    "pe-planning-optimum-performance": ["pe2", "pe-casestudy"],
    "pe-ethics-fair-play": ["pe9"],
    "pe-adventure-activities": ["pe8"],
    "pe-aquatics": ["pe8"],
    "pe-artistic-aesthetic-movement": ["pe7"],
    "pe-athletics": ["pe1", "pe6"],
    "pe-games": ["pe7", "pe9"],
    "pe-personal-exercise-fitness": ["pe2", "pe4"],
  };
  // A legacy chapter may inform notes in several syllabus chapters, but each
  // practice question needs one canonical home. Copying questions through
  // `legacySources` attached every question from shared sources (for example
  // all of pe6) to multiple chapters. Keep ownership positional and exclusive;
  // if a new question is appended later, the first owner remains its safe,
  // single fallback until this table is reviewed.
  var legacyQuestionOwners = {
    pe1: [
      "pe-personal-exercise-fitness",
      "pe-personal-exercise-fitness",
      "pe-personal-exercise-fitness",
      "pe-personal-exercise-fitness",
    ],
    pe2: [
      "pe-planning-optimum-performance",
      "pe-planning-optimum-performance",
      "pe-personal-exercise-fitness",
      "pe-ethics-fair-play",
      "pe-planning-optimum-performance",
    ],
    pe3: [
      "pe-performance-demands",
      "pe-performance-demands",
      "pe-performance-demands",
      "pe-performance-demands",
    ],
    pe4: [
      "pe-personal-exercise-fitness",
      "pe-athletics",
      "pe-aquatics",
      "pe-aquatics",
    ],
    pe5: [
      "pe-learning-skill-technique",
      "pe-learning-skill-technique",
      "pe-learning-skill-technique",
      "pe-games",
    ],
    pe6: [
      "pe-artistic-aesthetic-movement",
      "pe-artistic-aesthetic-movement",
      "pe-athletics",
      "pe-athletics",
    ],
    pe7: [
      "pe-artistic-aesthetic-movement",
      "pe-games",
      "pe-structures-strategies-roles-conventions",
    ],
    pe8: [
      "pe-adventure-activities",
      "pe-adventure-activities",
      "pe-adventure-activities",
      "pe-aquatics",
    ],
    pe9: [
      "pe-structures-strategies-roles-conventions",
      "pe-games",
      "pe-ethics-fair-play",
      "pe-structures-strategies-roles-conventions",
    ],
    "pe-casestudy": ["pe-planning-optimum-performance"],
  };
  var chapterDefinitions = [
    ["pe-learning-skill-technique", "Learning and Improving Skill and Technique"],
    ["pe-performance-demands", "Physical and Psychological Demands of Performance"],
    ["pe-structures-strategies-roles-conventions", "Structures, Strategies, Roles and Conventions"],
    ["pe-planning-optimum-performance", "Planning for Optimum Performance"],
    ["pe-promoting-physical-activity", "Promoting Physical Activity"],
    ["pe-ethics-fair-play", "Ethics and Fair Play"],
    ["pe-physical-activity-inclusion", "Physical Activity and Inclusion"],
    ["pe-technology-media-sport", "Technology, Media and Sport"],
    ["pe-gender-physical-activity", "Gender and Physical Activity"],
    ["pe-business-enterprise-sport", "Business and Enterprise in Physical Activity and Sport"],
    ["pe-adventure-activities", "Adventure Activities"],
    ["pe-aquatics", "Aquatics"],
    ["pe-artistic-aesthetic-movement", "Artistic and Aesthetic Movement"],
    ["pe-athletics", "Athletics"],
    ["pe-games", "Games"],
    ["pe-personal-exercise-fitness", "Personal Exercise and Fitness Activities"],
  ];

  // Keep the hand-authored PE chapters as a safe fallback if the generated
  // deck failed to load for any reason.
  if (!chapterDefinitions.some(function (chapter) {
    return Array.isArray(decks[chapter[0]]) && decks[chapter[0]].length > 0;
  })) return;

  var pipelineChapters = chapterDefinitions.map(function (chapter, index) {
    var id = chapter[0];
    var title = chapter[1];
    var cards = Array.isArray(decks[id]) ? decks[id] : [];
    var sourceOutcomes = (legacySources[id] || []).flatMap(function (sourceId) {
      var source = legacyChapters.get(sourceId);
      return source && Array.isArray(source.learningOutcomes) ? source.learningOutcomes : [];
    });
    var authoredNotes = sourceOutcomes.flatMap(function (outcome) { return outcome.notes || []; });
    var authoredQuestions = Object.keys(legacyQuestionOwners).flatMap(function (sourceId) {
      var source = legacyChapters.get(sourceId);
      var questions = source && Array.isArray(source.learningOutcomes)
        ? source.learningOutcomes.flatMap(function (outcome) { return outcome.questions || []; })
        : [];
      var owners = legacyQuestionOwners[sourceId];
      return questions.filter(function (_question, questionIndex) {
        return (owners[questionIndex] || owners[0]) === id;
      });
    });
    return {
      id: id,
      number: index + 1,
      subject: "pe",
      title: title,
      examQuestions: [],
      learningOutcomes: [
        {
          id: id + "-core",
          code: (index + 1) + ".0",
          title: "Core Concepts",
          // Preserve relevant hand-authored depth from the original PE taxonomy.
          // The final notes adapter adds the pipeline concepts and answer method.
          notes: authoredNotes.slice(),
          keyTerms: cards.slice(),
          questions: authoredQuestions.slice(),
        },
      ],
    };
  });

  COURSE_DATA.chapters = COURSE_DATA.chapters
    .filter(function (chapter) { return chapter.subject !== "pe"; })
    .concat(pipelineChapters);
})();
