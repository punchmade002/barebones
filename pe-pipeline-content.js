// Replace the legacy PE chapter shell with the pipeline chapter taxonomy.
//
// The generated PE questions and flashcards use stable `pe-*` chapter ids.
// app.js builds its visible subject tree from COURSE_DATA, so those ids must be
// present there before app.js initializes.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  var decks = globalThis.FLASHCARDS_DB || {};
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
          notes: cards.map(function (card) {
            return { h: card.term || "Key idea", b: card.definition || "" };
          }),
          keyTerms: cards.slice(),
          questions: [],
        },
      ],
    };
  });

  COURSE_DATA.chapters = COURSE_DATA.chapters
    .filter(function (chapter) { return chapter.subject !== "pe"; })
    .concat(pipelineChapters);
})();
