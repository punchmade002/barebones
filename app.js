const storageKey = "bare-bones-app-v4";
const pendingAuthUsernameKey = "bb_pending_auth_username";
const pendingAuthEmailKey = "bb_pending_auth_email";
const legacyBackupKeyPrefix = "bb-legacy-account-backup-v1:";
const legacyAccountPriority = ["gabriel"];
const isLocalMathsPreview = ["localhost", "127.0.0.1"].includes(window.location.hostname)
  && new URLSearchParams(window.location.search).get("preview") === "maths";
// Localhost-only: ?preview=onboarding opens the first-run questionnaire without an account.
const isLocalOnboardingPreview = ["localhost", "127.0.0.1"].includes(window.location.hostname)
  && new URLSearchParams(window.location.search).get("preview") === "onboarding";
// Localhost-only: ?preview=test opens the Test tab with a throwaway profile.
const isLocalTestPreview = ["localhost", "127.0.0.1"].includes(window.location.hostname)
  && new URLSearchParams(window.location.search).get("preview") === "test";

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

const BUSINESS_SUBJECT = {
  id: "business",
  title: "Business",
  chapters: buildSubjectChapters("business"),
};

const PE_SUBJECT = {
  id: "pe",
  title: "PE",
  chapters: buildSubjectChapters("pe"),
};

const BIOLOGY_SUBJECT = {
  id: "biology",
  title: "Biology",
  chapters: buildSubjectChapters("biology"),
};

const GEOGRAPHY_SUBJECT = {
  id: "geography",
  title: "Geography",
  chapters: buildSubjectChapters("geography"),
};

const MATHS_SUBJECT = {
  id: "maths",
  title: "Maths",
  chapters: buildSubjectChapters("maths"),
};

const CHEMISTRY_SUBJECT = {
  id: "chemistry",
  title: "Chemistry",
  chapters: buildSubjectChapters("chemistry"),
};

const HOME_ECONOMICS_SUBJECT = {
  id: "home-economics",
  title: "Home Economics",
  chapters: buildSubjectChapters("home-economics"),
};

const HISTORY_SUBJECT = {
  id: "history",
  title: "History",
  chapters: buildSubjectChapters("history"),
};

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

const SUBJECTS = [
  BUSINESS_SUBJECT,
  PE_SUBJECT,
  BIOLOGY_SUBJECT,
  GEOGRAPHY_SUBJECT,
  MATHS_SUBJECT,
  CHEMISTRY_SUBJECT,
  HOME_ECONOMICS_SUBJECT,
  HISTORY_SUBJECT,
];

const SINGULAR_S_WORDS = new Set([
  "virus","axis","basis","crisis","thesis","nexus","status","campus","focus",
  "bonus","minus","calculus","stimulus","syllabus","apparatus","process",
  "success","class","glass","grass","mass","pass","boss","loss","cross",
  "address","access","business","consensus","genius","series","means","news",
  "physics","mathematics","economics","statistics","athletics","gymnastics",
  "politics","ethics","logistics","lens","canvas","bias","gas","atlas",
  "analysis","emphasis","diagnosis","hypothesis","synthesis","species",
  "diabetes","progress","stress","taxis","oasis","osis","asis",
]);

function isPersonTerm(term) {
  const stripped = term.replace(/\s*\(.*?\)\s*/g, "").trim();
  const words = stripped.split(/\s+/);
  const eventNouns = /\b(war|act|treaty|plan|policy|revolution|crisis|movement|system|agreement|election|bill|reform|conference|congress|council|commission|report|court|rising|rebellion|famine|massacre|partition|constitution|declaration|manifesto|league|union|society|party|organisation|organization)\b/i;
  return (
    words.length === 2 &&
    /^[A-Z]/.test(words[0]) &&
    /^[A-Z]/.test(words[1]) &&
    !eventNouns.test(stripped)
  );
}

function needsDefiniteArticle(term) {
  return /\b(war|plan|act|treaty|crisis|movement|revolution|policy|system|agreement|conference|report|question|uprising|scheme|programme|rising|rebellion|famine|massacre|partition|constitution|declaration|manifesto|troubles|curtain|state|race|deal|blockade|purge|offensive|doctrine|scandal|holocaust|depression)\b/i.test(term);
}

function isPluralTerm(term) {
  // Proper nouns (2+ title-case words) are never grammatically plural
  const titleCaseWords = term.match(/\b[A-Z][a-z]+/g) || [];
  if (titleCaseWords.length >= 2) return false;
  const cleaned = term.replace(/\s*\(.*?\)\s*/g, "").trim();
  const words = cleaned.split(/\s+/);
  const isWordPlural = (raw) => {
    const w = raw.toLowerCase().replace(/[^a-z]/g, "");
    if (w.length < 3) return false;
    if (/ss$/.test(w)) return false;
    if (/(us|is)$/.test(w)) return false;
    if (SINGULAR_S_WORDS.has(w)) return false;
    return /s$/.test(w);
  };
  return isWordPlural(words[0]) || isWordPlural(words[words.length - 1]);
}

function termForSentence(term) {
  const lettersOnly = term.replace(/[^A-Za-z]/g, "");
  if (lettersOnly.length >= 2 && lettersOnly === lettersOnly.toUpperCase()) return term;
  if (/'s\b/.test(term)) return term;
  if (/^[A-Za-z\-]+\s+[A-Z]/.test(term)) return term;
  return term.charAt(0).toLowerCase() + term.slice(1);
}

const SUBJECT_FALLBACK_QUESTION = {
  business: (term) => `Explain "${term}" and give one simple business example.`,
  pe: (term) => `Explain "${term}" and give one example from sport or physical activity.`,
  biology: (term) => `Explain "${term}" and describe its role in a biological context.`,
  geography: (term) => `Explain "${term}" and give a relevant geographical example.`,
  maths: (term) => `Define "${term}" and demonstrate it with a worked example.`,
};

const els = {
  authPanel: document.getElementById("authPanel"),
  authTitle: document.getElementById("authTitle"),
  authIntro: document.getElementById("authIntro"),
  authTabs: document.getElementById("authTabs"),
  showSignIn: document.getElementById("showSignIn"),
  showSignUp: document.getElementById("showSignUp"),
  signInForm: document.getElementById("signInForm"),
  signUpForm: document.getElementById("signUpForm"),
  legacySetupForm: document.getElementById("legacySetupForm"),
  forgotPasswordForm: document.getElementById("forgotPasswordForm"),
  newPasswordForm: document.getElementById("newPasswordForm"),
  accountDetails: document.getElementById("accountDetails"),
  signInEmail: document.getElementById("signInEmail"),
  signInPassword: document.getElementById("signInPassword"),
  signUpUsername: document.getElementById("signUpUsername"),
  signUpEmail: document.getElementById("signUpEmail"),
  signUpPassword: document.getElementById("signUpPassword"),
  signUpPasswordConfirm: document.getElementById("signUpPasswordConfirm"),
  legacyUsername: document.getElementById("legacyUsername"),
  legacyAccountChoice: document.getElementById("legacyAccountChoice"),
  legacyAccountSelect: document.getElementById("legacyAccountSelect"),
  legacyEmail: document.getElementById("legacyEmail"),
  legacyPassword: document.getElementById("legacyPassword"),
  legacyPasswordConfirm: document.getElementById("legacyPasswordConfirm"),
  legacySignIn: document.getElementById("legacySignIn"),
  forgotEmail: document.getElementById("forgotEmail"),
  newPassword: document.getElementById("newPassword"),
  newPasswordConfirm: document.getElementById("newPasswordConfirm"),
  accountDetailsUsername: document.getElementById("accountDetailsUsername"),
  accountDetailsEmail: document.getElementById("accountDetailsEmail"),
  closeAccountDetails: document.getElementById("closeAccountDetails"),
  openProgress: document.getElementById("openProgress"),
  closeProgress: document.getElementById("closeProgress"),
  progressScreen: document.getElementById("progressScreen"),
  progressBody: document.getElementById("progressBody"),
  profileAvatar: document.getElementById("profileAvatar"),
  profileLevel: document.getElementById("profileLevel"),
  subjectPicker: document.getElementById("subjectPicker"),
  profileMenu: document.getElementById("profileMenu"),
  profileMenuMain: document.getElementById("profileMenuMain"),
  profileMenuSubjects: document.getElementById("profileMenuSubjects"),
  openSubjectChoices: document.getElementById("openSubjectChoices"),
  openStudyPlan: document.getElementById("openStudyPlan"),
  studyPlanValue: document.getElementById("studyPlanValue"),
  closeSubjectChoices: document.getElementById("closeSubjectChoices"),
  subjectChoicesCount: document.getElementById("subjectChoicesCount"),
  accountIdentity: document.getElementById("accountIdentity"),
  signOutButton: document.getElementById("signOutButton"),
  subjectArea: document.getElementById("subjectArea"),
  sidebarToggle: document.getElementById("sidebarToggle"),
  accountStatus: document.getElementById("accountStatus"),
  subjectGraph: document.getElementById("subjectGraph"),
  subjectWorkbench: document.getElementById("subjectWorkbench"),
  studyContext: document.getElementById("studyContext"),
  flashcardList: document.getElementById("flashcardList"),
  flashcardStudy: document.getElementById("flashcardStudy"),
  outcomePicker: document.getElementById("outcomePicker"),
  openLiveReading: document.getElementById("openLiveReading"),
  liveReader: document.getElementById("liveReader"),
  liveReaderStage: document.getElementById("liveReaderStage"),
  liveReaderTrack: document.getElementById("liveReaderTrack"),
  liveReaderProgress: document.getElementById("liveReaderProgress"),
  liveReaderPlay: document.getElementById("liveReaderPlay"),
  liveReaderPrev: document.getElementById("liveReaderPrev"),
  liveReaderNext: document.getElementById("liveReaderNext"),
  liveReaderWpm: document.getElementById("liveReaderWpm"),
  liveReaderWpmLabel: document.getElementById("liveReaderWpmLabel"),
  openFullNotes: document.getElementById("openFullNotes"),
  fullNotesScreen: document.getElementById("fullNotesScreen"),
  fullNotesTitle: document.getElementById("fullNotesTitle"),
  fullNotesBody: document.getElementById("fullNotesBody"),
  closeFullNotes: document.getElementById("closeFullNotes"),
  hierarchyPanel: document.getElementById("hierarchyPanel"),
  testContainer: document.getElementById("testContainer"),
  testScreen: document.getElementById("testScreen"),
  tabs: Array.from(document.querySelectorAll(".tab")),
  flashcardsTab: document.getElementById("flashcardsTab"),
  testTab: document.getElementById("testTab"),
  examTab: document.getElementById("examTab"),
  examContainer: document.getElementById("examContainer"),
  subjectOverview: document.getElementById("subjectOverview"),
};

let state = loadState();
const accountAuth = window.BarebonesAuth;
let authSnapshot = null;
let activeAuthUserId = "";
let authSaveTimer = null;
let authSaveInFlight = null;
let authActivationPromise = null;
let activatingAuthUserId = "";
let _fullNotesReturnToBreakdown = null; // set when full notes opened from breakdown questions
let expandedSubjectId = "";
let selectedSubjectId = SUBJECTS[0].id;
let selectedChapterId = SUBJECTS[0].chapters[0].id;
let selectedOutcomeId = SUBJECTS[0].chapters[0].learningOutcomes[0].id;
let studyIndex = 0;
let showAnswer = false;
let viewMode = 'chapter';
let phoneHome = true; // phones open on the subject list; see "Phone navigation"
// True while a freshly opened chapter is showing its full-screen subsection picker.
let pickingOutcome = false;
// Live reading state lives up here because bindEvents() runs before the reader's code below.
const LIVE_READER_WPM_KEY = "bb-live-reader-wpm";
// The highlight moves a character at a time; the slider stays in words per
// minute using the usual five-characters-to-a-word convention.
const LIVE_READER_CHARS_PER_WORD = 5;
const liveReader = { lines: [], index: 0, pos: 0, playing: false, raf: 0, lastTs: 0, wpm: 220 };
const mathsSolutionStore = new Map();

// Test state. Declared up here because renderAll() runs before the Test section below.
const TEST_HISTORY_LIMIT = 30;
const TEST_SETTINGS_KEY = "bb-test-settings-v1";
const TEST_LENGTHS = [5, 10, 15, 20, 30, 45];
const TEST_MIXES = [
  { id: "flashcards", label: "Mostly flashcards" },
  { id: "balanced", label: "Balanced" },
  { id: "exam", label: "Mostly exam" },
];
const TEST_PASS_PERCENT = 70;
const TEST_KIND_LABELS = {
  "pick-term": "Name the term",
  "pick-definition": "Pick the description",
  cloze: "Fill the gap",
  recall: "Written recall",
  mcq: "Multiple choice",
  tf: "True or false",
  written: "Written answer",
};
const TEST_CHOICE_KINDS = new Set(["pick-term", "pick-definition", "mcq", "tf"]);
const testPoolCache = new Map();
let activeTest = null;

if (isLocalMathsPreview) {
  const previewUsername = "maths-preview";
  state.usersByName[previewUsername] = createEmptyStudyUser(previewUsername);
  state.session.currentUser = previewUsername;
  expandedSubjectId = "";
  selectedSubjectId = MATHS_SUBJECT.id;
  selectedChapterId = MATHS_SUBJECT.chapters[0]?.id || "";
  selectedOutcomeId = MATHS_SUBJECT.chapters[0]?.learningOutcomes[0]?.id || "";
  viewMode = "chapter";
}

if (isLocalOnboardingPreview) {
  const previewUsername = "onboarding-preview";
  state.usersByName[previewUsername] = createEmptyStudyUser(previewUsername);
  state.session.currentUser = previewUsername;
}

if (isLocalTestPreview) {
  const previewUsername = "test-preview";
  state.usersByName[previewUsername] = createEmptyStudyUser(previewUsername);
  state.session.currentUser = previewUsername;
  const previewSubject = SUBJECTS.find((s) => s.id === "biology") || SUBJECTS[0];
  selectedSubjectId = previewSubject.id;
  selectedChapterId = previewSubject.chapters[0]?.id || "";
  selectedOutcomeId = previewSubject.chapters[0]?.learningOutcomes[0]?.id || "";
}

bindEvents();
renderAll();
if (isLocalOnboardingPreview) {
  showOnboarding(getCurrentUser());
} else if (isLocalTestPreview) {
  switchTab("test");
} else if (!isLocalMathsPreview) {
  initializeAccounts();
}

function bindEvents() {
  renderAvatarPicker();
  els.openSubjectChoices.addEventListener("click", () => showProfilePane("subjects"));
  els.openStudyPlan.addEventListener("click", () => {
    const user = getCurrentUser();
    if (!user || !window.BarebonesOnboarding) return;
    els.profileMenu.classList.add("hidden");
    showOnboarding(user, { editing: true });
  });
  els.closeSubjectChoices.addEventListener("click", () => showProfilePane("main"));
  els.closeAccountDetails.addEventListener("click", hideAuthPanel);
  els.showSignIn.addEventListener("click", () => showAuthMode("signin"));
  els.showSignUp.addEventListener("click", () => showAuthMode("signup"));
  document.getElementById("showForgotPassword").addEventListener("click", () => {
    els.forgotEmail.value = els.signInEmail.value;
    showAuthMode("forgot");
  });
  document.querySelectorAll("[data-auth-back]").forEach((button) => {
    button.addEventListener("click", () => showAuthMode("signin"));
  });
  document.querySelectorAll("[data-password-toggle]").forEach((button) => {
    button.addEventListener("click", () => togglePasswordVisibility(button));
  });
  [els.signUpPasswordConfirm, els.legacyPasswordConfirm, els.newPasswordConfirm].forEach((input) => {
    input.addEventListener("input", () => input.setCustomValidity(""));
  });
  els.signInForm.addEventListener("submit", handleSignIn);
  els.signUpForm.addEventListener("submit", handleSignUp);
  els.legacySetupForm.addEventListener("submit", handleLegacySetup);
  els.legacySignIn.addEventListener("click", () => {
    showExistingAccountSignIn(els.legacyEmail.value);
  });
  els.forgotPasswordForm.addEventListener("submit", handleForgotPassword);
  els.newPasswordForm.addEventListener("submit", handleNewPassword);
  els.legacyAccountSelect.addEventListener("change", () => {
    const username = els.legacyAccountSelect.value;
    if (!username || !state.usersByName[username]) return;
    state.session.currentUser = username;
    persist({ sync: false });
    els.legacyUsername.textContent = username;
  });
  els.testContainer.addEventListener("click", handleTestSetupClick);
  els.testContainer.addEventListener("change", handleTestSetupChange);
  els.testScreen.addEventListener("click", handleTestScreenClick);
  els.testScreen.addEventListener("input", handleTestScreenInput);
  document.addEventListener("keydown", handleTestKeyboard);
  els.openFullNotes.addEventListener("click", openFullNotes);
  els.closeFullNotes.addEventListener("click", () => leavePhoneScreen("notes", closeFullNotes));
  bindLiveReader();
  els.openProgress.addEventListener("click", openProgress);
  document.addEventListener("click", (event) => {
    if (!expandedSubjectId || !isCompactLayout() || event.target.closest(".graph-subject")) return;
    expandedSubjectId = "";
    renderGraph();
  });
  els.closeProgress.addEventListener("click", () => leavePhoneScreen("progress", closeProgress));
  // A reload starts again from the subject list, so drop any phone screen entry it restored
  if (history.state?.bbScreen) history.replaceState(null, "", location.href);
  window.addEventListener("popstate", handlePhonePopState);
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    const openMathsPanel = document.querySelector(".maths-explanation-panel.is-open");
    if (openMathsPanel) {
      closeMathsExplanation(openMathsPanel);
    } else if (!els.liveReader.classList.contains("hidden")) {
      closeLiveReader();
    } else if (!document.getElementById("examBreakdownModal").classList.contains("hidden")) {
      closeExamBreakdown();
    } else if (!els.fullNotesScreen.classList.contains("hidden")) {
      leavePhoneScreen("notes", closeFullNotes);
    } else if (!els.progressScreen.classList.contains("hidden")) {
      leavePhoneScreen("progress", closeProgress);
    }
  });
  els.tabs.forEach((tab) => tab.addEventListener("click", () => switchTab(tab.dataset.tab)));
  els.profileAvatar.addEventListener("click", () => {
    if (!getCurrentUser()) return;
    const opening = els.profileMenu.classList.contains("hidden");
    els.profileMenu.classList.toggle("hidden");
    if (opening) showProfilePane("main");
    renderAccountIdentity();
  });
  bindSidebarCollapse();
  els.signOutButton.addEventListener("click", async () => {
    els.profileMenu.classList.add("hidden");
    try {
      await flushRemoteStudySave();
      await accountAuth?.signOut();
    } catch (error) {
      console.error(error);
    }
    activeAuthUserId = "";
    authSnapshot = null;
    state.session.currentUser = "";
    persist({ sync: false });
    renderAll();
    showAuthMode(getLegacyProfileNames().length ? "legacy" : "signin");
    setAuthStatus("Signed out.", "success");
  });
  document.addEventListener("click", (event) => {
    const target = event.target;
    // Toggling a subject re-renders the picker, so by the time this click
    // bubbles its target is detached. That is not a click outside the menu.
    if (target instanceof Node && !target.isConnected) return;
    if (
      target !== els.profileAvatar &&
      !els.profileMenu.contains(target) &&
      !els.profileMenu.classList.contains("hidden")
    ) {
      els.profileMenu.classList.add("hidden");
    }
  });
  document.addEventListener("click", handleMathsSolutionClick);
  document.addEventListener("pointerup", handleMathsSolutionSelection);
  document.addEventListener("keydown", handleMathsSolutionKeyboard);
}

function showProfilePane(pane) {
  const subjects = pane === "subjects";
  els.profileMenuMain.classList.toggle("hidden", subjects);
  els.profileMenuSubjects.classList.toggle("hidden", !subjects);
  els.profileMenu.classList.toggle("profile-menu-wide", subjects);
}

/* ── Sidebar collapse ──────────────────────────
   Two-finger horizontal trackpad swipe over the subject area hides the
   sidebar; swiping back (or the edge button) brings it in. Wheel deltas
   are accumulated so a lazy gesture still lands, and a run of vertical
   scrolling resets the tally so ordinary reading never trips it. */
const SIDEBAR_COLLAPSE_KEY = "bare-bones-sidebar-collapsed";
const SWIPE_THRESHOLD = 90;
let swipeAccum = 0;
let swipeResetTimer = null;

function isSidebarCollapsed() {
  return els.subjectArea?.classList.contains("sidebar-collapsed");
}

function setSidebarCollapsed(collapsed) {
  if (!els.subjectArea) return;
  els.subjectArea.classList.toggle("sidebar-collapsed", collapsed);
  if (els.sidebarToggle) {
    els.sidebarToggle.setAttribute("aria-expanded", String(!collapsed));
    els.sidebarToggle.setAttribute(
      "aria-label",
      collapsed ? "Show subject sidebar" : "Hide subject sidebar"
    );
  }
  swipeAccum = 0;
  try {
    localStorage.setItem(SIDEBAR_COLLAPSE_KEY, collapsed ? "1" : "0");
  } catch (e) {
    /* storage unavailable — collapse is session-only */
  }
}

function hasHorizontalScroll(node) {
  let el = node instanceof Element ? node : node?.parentElement;
  while (el && el !== els.subjectArea) {
    if (el.scrollWidth > el.clientWidth + 2) {
      const overflow = getComputedStyle(el).overflowX;
      if (overflow === "auto" || overflow === "scroll") return true;
    }
    el = el.parentElement;
  }
  return false;
}

function bindSidebarCollapse() {
  if (!els.subjectArea) return;
  try {
    if (localStorage.getItem(SIDEBAR_COLLAPSE_KEY) === "1") setSidebarCollapsed(true);
  } catch (e) {
    /* ignore */
  }

  els.sidebarToggle?.addEventListener("click", () => {
    setSidebarCollapsed(!isSidebarCollapsed());
  });

  els.subjectArea.addEventListener(
    "wheel",
    (event) => {
      // Only a deliberate horizontal gesture counts.
      if (Math.abs(event.deltaX) < Math.abs(event.deltaY) * 1.5) {
        swipeAccum = 0;
        return;
      }
      // Let genuinely scrollable content (wide tables, chapter strips) keep its gesture.
      if (hasHorizontalScroll(event.target)) {
        swipeAccum = 0;
        return;
      }
      swipeAccum += event.deltaX;
      clearTimeout(swipeResetTimer);
      swipeResetTimer = setTimeout(() => { swipeAccum = 0; }, 220);

      if (swipeAccum > SWIPE_THRESHOLD && !isSidebarCollapsed()) {
        setSidebarCollapsed(true);
      } else if (swipeAccum < -SWIPE_THRESHOLD && isSidebarCollapsed()) {
        setSidebarCollapsed(false);
      }
    },
    { passive: true }
  );
}

async function initializeAccounts() {
  const requestedMode = window.location.hash === "#signup" ? "signup" : "signin";

  if (!accountAuth?.configured) {
    if (!getCurrentUser() || window.location.hash === "#signin" || window.location.hash === "#signup") {
      showAuthMode(requestedMode);
      setAuthStatus("Account services need to be connected before sign-in and registration can go live.", "error");
    }
    return;
  }

  accountAuth.subscribe(handleAuthEvent);

  try {
    const session = await accountAuth.ready();
    if (session?.user) {
      await activateAuthenticatedSession(session, { animate: false });
    } else {
      const legacyUser = getCurrentUser();
      const legacyProfiles = getLegacyProfileNames();
      const pendingUsername = accountAuth.normalizeUsername(
        localStorage.getItem(pendingAuthUsernameKey)
      );
      const pendingProfileExists = legacyProfiles.some(
        (name) => accountAuth.normalizeUsername(name) === pendingUsername
      );
      if (pendingUsername && pendingProfileExists) {
        showExistingAccountSignIn();
      } else if ((legacyUser && !legacyUser.authUserId) || legacyProfiles.length) {
        showAuthMode("legacy");
      } else {
        state.session.currentUser = "";
        persist({ sync: false });
        renderAll();
        showAuthMode(requestedMode);
      }
    }
  } catch (error) {
    console.error(error);
    showAuthMode(requestedMode);
    setAuthStatus(friendlyAuthError(error), "error");
  } finally {
    if (window.location.hash === "#signin" || window.location.hash === "#signup") {
      history.replaceState(null, "", window.location.pathname);
    }
  }
}

async function handleAuthEvent(event, session) {
  if (event === "PASSWORD_RECOVERY") {
    showAuthMode("new-password");
    setAuthStatus("Your reset link is verified. Choose a new password.", "success");
    return;
  }

  if (event === "SIGNED_IN" && session?.user) {
    try {
      await activateAuthenticatedSession(session);
    } catch (error) {
      console.error(error);
      showAuthMode("signin");
      setAuthStatus(friendlyAuthError(error), "error");
    }
  }

  if (event === "SIGNED_OUT") {
    activeAuthUserId = "";
    authSnapshot = null;
    state.session.currentUser = "";
    persist({ sync: false });
    renderAll();
    showAuthMode(getLegacyProfileNames().length ? "legacy" : "signin");
  }
}

async function handleSignIn(event) {
  event.preventDefault();
  if (!els.signInForm.reportValidity()) return;
  await runAuthAction(els.signInForm, async () => {
    await accountAuth.signIn(els.signInEmail.value, els.signInPassword.value);
    setAuthStatus("Signing you in…", "neutral");
  });
}

async function handleSignUp(event) {
  event.preventDefault();
  if (!els.signUpForm.reportValidity()) return;
  if (!passwordsMatch(els.signUpPassword, els.signUpPasswordConfirm)) return;
  const username = accountAuth.normalizeUsername(els.signUpUsername.value);
  localStorage.setItem(pendingAuthUsernameKey, username);
  localStorage.setItem(
    pendingAuthEmailKey,
    String(els.signUpEmail.value || "").trim().toLowerCase()
  );

  await runAuthAction(els.signUpForm, async () => {
    const data = await accountAuth.signUp({
      username,
      email: els.signUpEmail.value,
      password: els.signUpPassword.value,
      origin: "self_service",
    });
    if (data.session) {
      await activateAuthenticatedSession(data.session);
    } else {
      setAuthStatus("Account created. Check your email to confirm it, then you’ll be signed in.", "success");
      els.signUpForm.reset();
    }
  });
}

async function handleLegacySetup(event) {
  event.preventDefault();
  if (!els.legacySetupForm.reportValidity()) return;
  if (!passwordsMatch(els.legacyPassword, els.legacyPasswordConfirm)) return;
  const current = getCurrentUser();
  if (!current || current.authUserId) {
    showAuthMode("signup");
    return;
  }

  const username = accountAuth.normalizeUsername(current.username);
  localStorage.setItem(pendingAuthUsernameKey, username);
  localStorage.setItem(
    pendingAuthEmailKey,
    String(els.legacyEmail.value || "").trim().toLowerCase()
  );

  await runAuthAction(els.legacySetupForm, async () => {
    let data;
    try {
      data = await accountAuth.signUp({
        username,
        email: els.legacyEmail.value,
        password: els.legacyPassword.value,
        origin: "legacy_migration",
      });
    } catch (error) {
      if (isUsernameTakenError(error)) {
        showExistingAccountSignIn(els.legacyEmail.value);
        return;
      }
      throw error;
    }
    if (data.session) {
      await activateAuthenticatedSession(data.session);
    } else {
      setAuthStatus("Nearly done. Confirm the email we sent you; your existing progress is waiting here.", "success");
      els.legacyEmail.disabled = true;
      els.legacyPassword.disabled = true;
      els.legacyPasswordConfirm.disabled = true;
      const submit = els.legacySetupForm.querySelector("[type='submit']");
      submit.disabled = true;
      submit.textContent = "Check your email";
      els.legacySetupForm.dataset.locked = "true";
    }
  });
}

async function handleForgotPassword(event) {
  event.preventDefault();
  if (!els.forgotPasswordForm.reportValidity()) return;
  await runAuthAction(els.forgotPasswordForm, async () => {
    await accountAuth.sendPasswordReset(els.forgotEmail.value);
    setAuthStatus("If an account exists for that email, a reset link is on its way.", "success");
    els.forgotPasswordForm.reset();
  });
}

async function handleNewPassword(event) {
  event.preventDefault();
  if (!els.newPasswordForm.reportValidity()) return;
  if (!passwordsMatch(els.newPassword, els.newPasswordConfirm)) return;
  await runAuthAction(els.newPasswordForm, async () => {
    await accountAuth.updatePassword(els.newPassword.value);
    els.newPasswordForm.reset();
    setAuthStatus("Password updated.", "success");
    const session = accountAuth.getSession();
    if (session) await activateAuthenticatedSession(session);
  });
}

async function runAuthAction(form, action) {
  if (!accountAuth?.configured) {
    setAuthStatus("Account services are not configured yet.", "error");
    return;
  }
  const submit = form.querySelector("[type='submit']");
  const originalText = submit?.textContent || "";
  if (submit) {
    submit.disabled = true;
    submit.textContent = "Working…";
  }
  setAuthStatus("", "neutral");
  try {
    await action();
  } catch (error) {
    console.error(error);
    setAuthStatus(friendlyAuthError(error), "error");
  } finally {
    if (submit && form.dataset.locked !== "true") {
      submit.disabled = false;
      submit.textContent = originalText;
    }
  }
}

function showAuthMode(mode) {
  const forms = {
    signin: els.signInForm,
    signup: els.signUpForm,
    legacy: els.legacySetupForm,
    forgot: els.forgotPasswordForm,
    "new-password": els.newPasswordForm,
    details: els.accountDetails,
  };
  Object.values(forms).forEach((form) => form.classList.add("hidden"));
  (forms[mode] || forms.signin).classList.remove("hidden");
  els.authPanel.classList.remove("hidden");
  document.body.classList.add("auth-open");
  setAuthBackgroundInert(true);
  els.authTabs.classList.toggle("hidden", !["signin", "signup"].includes(mode));
  els.showSignIn.classList.toggle("active", mode === "signin");
  els.showSignIn.setAttribute("aria-selected", String(mode === "signin"));
  els.showSignUp.classList.toggle("active", mode === "signup");
  els.showSignUp.setAttribute("aria-selected", String(mode === "signup"));
  setAuthStatus("", "neutral");

  const current = getCurrentUser();
  if (mode === "legacy") {
    const legacyProfiles = getLegacyProfileNames();
    let username = current && !current.authUserId ? current.username : legacyProfiles[0];
    if (username && state.usersByName[username]) {
      state.session.currentUser = username;
      persist({ sync: false });
    }
    username = username || "your existing account";
    els.authTitle.textContent = "Secure your account.";
    els.authIntro.textContent = "The old sign-in had no password. Add your details once and keep every bit of progress.";
    els.legacyUsername.textContent = username;
    els.legacyAccountSelect.innerHTML = legacyProfiles
      .map((name) => `<option value="${escapeHtml(name)}">${escapeHtml(name)}</option>`)
      .join("");
    els.legacyAccountSelect.value = username;
    els.legacyAccountChoice.classList.toggle("hidden", legacyProfiles.length < 2);
    els.legacyEmail.disabled = false;
    els.legacyPassword.disabled = false;
    els.legacyPasswordConfirm.disabled = false;
    const submit = els.legacySetupForm.querySelector("[type='submit']");
    submit.disabled = false;
    submit.textContent = "Secure my account";
    delete els.legacySetupForm.dataset.locked;
  } else if (mode === "signup") {
    els.authTitle.textContent = "Start from zero. Build from there.";
    els.authIntro.textContent = "Make an account to save progress across devices and recover your password.";
  } else if (mode === "details") {
    els.authTitle.textContent = "Your account.";
    els.authIntro.textContent = "The details connected to this study profile.";
    renderAccount();
  } else if (mode === "forgot") {
    els.authTitle.textContent = "Reset access.";
    els.authIntro.textContent = "";
  } else if (mode === "new-password") {
    els.authTitle.textContent = "Set a new password.";
    els.authIntro.textContent = "Use something you don’t reuse elsewhere.";
  } else {
    els.authTitle.textContent = "Welcome back.";
    els.authIntro.textContent = "Sign in to keep your progress safe and available on every device.";
  }

  const focusTarget = {
    signin: els.signInEmail,
    signup: els.signUpUsername,
    legacy: els.legacyEmail,
    forgot: els.forgotEmail,
    "new-password": els.newPassword,
  }[mode];
  window.setTimeout(() => focusTarget?.focus(), 40);
}

function hideAuthPanel() {
  if (!getCurrentUser() || !activeAuthUserId) return;
  els.authPanel.classList.add("hidden");
  document.body.classList.remove("auth-open");
  setAuthBackgroundInert(false);
  setAuthStatus("", "neutral");
}

function setAuthBackgroundInert(isInert) {
  [
    document.querySelector(".brand-mark"),
    document.querySelector(".profile-avatar-wrap"),
    document.querySelector(".subject-area"),
    document.getElementById("timerWidget"),
  ].forEach((element) => {
    if (!element) return;
    element.inert = isInert;
    if (isInert) {
      element.setAttribute("aria-hidden", "true");
    } else {
      element.removeAttribute("aria-hidden");
    }
  });
}

function setAuthStatus(message, type = "neutral") {
  els.accountStatus.textContent = message;
  els.accountStatus.dataset.type = type;
}

function togglePasswordVisibility(button) {
  const input = document.getElementById(button.dataset.passwordToggle);
  if (!input) return;
  const reveal = input.type === "password";
  input.type = reveal ? "text" : "password";
  button.textContent = reveal ? "Hide" : "Show";
  button.setAttribute("aria-label", reveal ? "Hide password" : "Show password");
}

function passwordsMatch(password, confirmation) {
  const matches = password.value === confirmation.value;
  confirmation.setCustomValidity(matches ? "" : "Passwords do not match.");
  if (!matches) confirmation.reportValidity();
  return matches;
}

function friendlyAuthError(error) {
  const message = String(error?.message || error || "");
  if (/invalid login credentials/i.test(message)) return "Email or password is incorrect.";
  if (/email not confirmed/i.test(message)) return "Confirm your email before signing in.";
  if (/already registered|already exists/i.test(message)) return "An account already exists for that email.";
  if (/username.*taken|duplicate key|profiles_username/i.test(message)) return "That username is already taken.";
  if (/password/i.test(message) && /weak|least|characters/i.test(message)) return "Use a password with at least 8 characters.";
  if (/rate limit|too many/i.test(message)) return "Too many attempts. Wait a moment and try again.";
  if (/failed to fetch|network/i.test(message)) return "Couldn’t reach account services. Check your connection and try again.";
  if (/not configured/i.test(message)) return "Account services are not configured yet.";
  return "Something went wrong with your account. Please try again.";
}

function isUsernameTakenError(error) {
  const message = String(error?.message || error || "");
  return error?.code === "username_taken" ||
    /username.*taken|duplicate key|profiles_username/i.test(message);
}

function showExistingAccountSignIn(email = "") {
  const rememberedEmail = String(
    email || localStorage.getItem(pendingAuthEmailKey) || ""
  ).trim().toLowerCase();
  if (rememberedEmail) els.signInEmail.value = rememberedEmail;
  els.signInPassword.value = "";
  showAuthMode("signin");
  setAuthStatus(
    "This profile is already secured. Sign in with the email and password you added; your saved progress will reconnect automatically.",
    "neutral"
  );
}

async function activateAuthenticatedSession(session, options = {}) {
  if (!session?.user || activeAuthUserId === session.user.id) {
    if (session?.user && getCurrentUser()) hideAuthPanel();
    return;
  }
  if (authActivationPromise && activatingAuthUserId === session.user.id) {
    return authActivationPromise;
  }

  activatingAuthUserId = session.user.id;
  authActivationPromise = (async () => {
    const snapshot = await accountAuth.getAccountSnapshot();
    if (!snapshot?.profile?.username) {
      throw new Error("Your account profile could not be loaded.");
    }

    const username = accountAuth.normalizeUsername(snapshot.profile.username);
    const existingKey = findLocalUsername(username);
    const localUser = existingKey ? state.usersByName[existingKey] : null;
    const isFirstLink = !localUser?.authUserId;
    if (isFirstLink && localUser) backupLegacyProfile(username, localUser);
    const merged = mergeStudyUser(localUser, snapshot.studyData, isFirstLink);

    merged.username = username;
    merged.authUserId = session.user.id;
    merged.email = session.user.email || "";
    merged.entitlements = snapshot.entitlements || [];

    if (existingKey && existingKey !== username) delete state.usersByName[existingKey];
    state.usersByName[username] = merged;
    state.session.currentUser = username;
    activeAuthUserId = session.user.id;
    authSnapshot = snapshot;
    localStorage.removeItem(pendingAuthUsernameKey);
    localStorage.removeItem(pendingAuthEmailKey);
    persist({ sync: false });
    await accountAuth.saveStudyData(serializeStudyUser(merged));
    renderAll();
    hideAuthPanel();

    if (needsOnboarding(merged, snapshot)) {
      showOnboarding(merged);
    } else if (options.animate !== false) {
      triggerLoginAnimation(username);
    }
  })();

  try {
    return await authActivationPromise;
  } finally {
    authActivationPromise = null;
    activatingAuthUserId = "";
  }
}

// New self-service accounts answer a short questionnaire once. Anyone who has
// already studied (or migrated a legacy profile) is never interrupted.
function needsOnboarding(user, snapshot) {
  if (!window.BarebonesOnboarding || user?.onboarding?.completedAt) return false;
  if (snapshot?.profile?.account_origin === "legacy_migration") return false;
  const hasStudied =
    Number(user?.testsCompleted || 0) > 0 ||
    Object.keys(user?.progressByOutcome || {}).length > 0 ||
    Object.keys(user?.learnedByOutcome || {}).length > 0;
  return !hasStudied;
}

function showOnboarding(user, { editing = false } = {}) {
  // When editing, start from the live subject list: it may have changed via
  // Subject choices since the plan was saved, or the account may predate plans.
  const initial = editing
    ? { ...(user.onboarding || {}), subjects: getEnabledSubjectIds(user) }
    : user.onboarding || {};
  window.BarebonesOnboarding.open({
    subjects: SUBJECTS.map((s) => ({ id: s.id, title: s.title })),
    username: user.username,
    initial,
    editing,
    onComplete(result) {
      if (!result) return;
      const current = getCurrentUser();
      if (!current) return;
      current.onboarding = result;
      current.disabledSubjects = SUBJECTS
        .map((s) => s.id)
        .filter((id) => !result.subjects.includes(id));
      const priority = SUBJECTS.find((s) => s.id === result.prioritySubject);
      if (priority && !editing) {
        selectedSubjectId = priority.id;
        expandedSubjectId = priority.id;
        selectedChapterId = priority.chapters[0]?.id || "";
        selectedOutcomeId = priority.chapters[0]?.learningOutcomes[0]?.id || "";
      }
      // The preview profile is throwaway; saving it would surface as a legacy account.
      if (!isLocalOnboardingPreview) persist();
      renderAll();
      if (!editing) window.setTimeout(() => triggerLoginAnimation(current.username), 420);
    },
  });
}

function findLocalUsername(username) {
  const normalized = String(username || "").toLowerCase();
  return Object.keys(state.usersByName).find((name) => name.toLowerCase() === normalized) || "";
}

function getLegacyProfileNames() {
  return Object.keys(state.usersByName)
    .filter((name) => !state.usersByName[name]?.authUserId)
    .sort((a, b) => {
      const aPriority = legacyAccountPriority.indexOf(a.toLowerCase());
      const bPriority = legacyAccountPriority.indexOf(b.toLowerCase());
      if (aPriority !== -1 || bPriority !== -1) {
        if (aPriority === -1) return 1;
        if (bPriority === -1) return -1;
        return aPriority - bPriority;
      }
      return a.localeCompare(b);
    });
}

function backupLegacyProfile(username, user) {
  const normalized = String(username || "").toLowerCase();
  const backupKey = `${legacyBackupKeyPrefix}${normalized}`;
  if (localStorage.getItem(backupKey)) return;
  localStorage.setItem(backupKey, JSON.stringify({
    username: normalized,
    backedUpAt: new Date().toISOString(),
    studyData: serializeStudyUser(user),
  }));
}

function createEmptyStudyUser(username = "") {
  return {
    username,
    testsCompleted: 0,
    viewedNotesByChapter: {},
    progressByOutcome: {},
    learnedByOutcome: {},
    disabledSubjects: [],
    testHistory: [],
  };
}

function mergeTestHistory(...lists) {
  const byId = new Map();
  lists.flat().forEach((entry) => {
    if (entry?.id && !byId.has(entry.id)) byId.set(entry.id, entry);
  });
  return Array.from(byId.values())
    .sort((a, b) => (b.at || 0) - (a.at || 0))
    .slice(0, TEST_HISTORY_LIMIT);
}

function mergeStudyUser(localValue, remoteValue, preferLocal) {
  const local = { ...createEmptyStudyUser(), ...(localValue || {}) };
  const remote = { ...createEmptyStudyUser(), ...(remoteValue || {}) };
  const progressKeys = new Set([
    ...Object.keys(local.progressByOutcome || {}),
    ...Object.keys(remote.progressByOutcome || {}),
  ]);
  const progressByOutcome = {};
  progressKeys.forEach((key) => {
    progressByOutcome[key] = Math.max(
      Number(local.progressByOutcome?.[key] || 0),
      Number(remote.progressByOutcome?.[key] || 0)
    );
  });

  const learnedKeys = new Set([
    ...Object.keys(local.learnedByOutcome || {}),
    ...Object.keys(remote.learnedByOutcome || {}),
  ]);
  const learnedByOutcome = {};
  learnedKeys.forEach((key) => {
    learnedByOutcome[key] = Array.from(new Set([
      ...(remote.learnedByOutcome?.[key] || []),
      ...(local.learnedByOutcome?.[key] || []),
    ]));
  });

  const viewedNotesByChapter = { ...(remote.viewedNotesByChapter || {}) };
  Object.entries(local.viewedNotesByChapter || {}).forEach(([key, value]) => {
    if (value) viewedNotesByChapter[key] = true;
  });

  return {
    ...remote,
    ...local,
    testsCompleted: Math.max(Number(local.testsCompleted || 0), Number(remote.testsCompleted || 0)),
    progressByOutcome,
    learnedByOutcome,
    viewedNotesByChapter,
    testHistory: mergeTestHistory(local.testHistory || [], remote.testHistory || []),
    disabledSubjects: preferLocal
      ? [...(local.disabledSubjects || [])]
      : [...(remote.disabledSubjects?.length ? remote.disabledSubjects : local.disabledSubjects || [])],
    onboarding: local.onboarding || remote.onboarding || null,
  };
}

function serializeStudyUser(user) {
  return {
    testsCompleted: Number(user?.testsCompleted || 0),
    viewedNotesByChapter: user?.viewedNotesByChapter || {},
    progressByOutcome: user?.progressByOutcome || {},
    learnedByOutcome: user?.learnedByOutcome || {},
    disabledSubjects: Array.isArray(user?.disabledSubjects) ? user.disabledSubjects : [],
    onboarding: user?.onboarding || null,
    testHistory: Array.isArray(user?.testHistory) ? user.testHistory : [],
  };
}

function switchTab(tab) {
  els.tabs.forEach((btn) => btn.classList.toggle("active", btn.dataset.tab === tab));
  els.flashcardsTab.classList.toggle("active", tab === "flashcards");
  els.testTab.classList.toggle("active", tab === "test");
  els.examTab.classList.toggle("active", tab === "exam");
  els.subjectWorkbench?.classList.toggle("learn-mode", tab === "flashcards");
  if (tab === "exam") renderExamSection();
}

function reconcileSelection() {
  const enabled = getEnabledSubjects();
  if (!enabled.length) return;
  if (!enabled.some((s) => s.id === selectedSubjectId)) {
    const first = enabled[0];
    selectedSubjectId = first.id;
    selectedChapterId = first.chapters[0]?.id || "";
    selectedOutcomeId = first.chapters[0]?.learningOutcomes[0]?.id || "";
    expandedSubjectId = "";
  }
}

function triggerLoginAnimation(name) {
  const overlay = document.getElementById("loginOverlay");
  if (!overlay) return;
  const asciiEl = overlay.querySelector(".login-ascii");
  const welcomeEl = overlay.querySelector(".login-welcome");
  const src = document.getElementById("asciiHeader");
  if (asciiEl && src) asciiEl.textContent = src.textContent;
  if (welcomeEl) welcomeEl.textContent = "welcome, " + name.toLowerCase();
  overlay.classList.remove("is-visible", "is-exiting");
  void overlay.offsetWidth;
  overlay.setAttribute("aria-hidden", "false");
  overlay.classList.add("is-visible");
  setTimeout(() => {
    overlay.classList.add("is-exiting");
    setTimeout(() => {
      overlay.classList.remove("is-visible", "is-exiting");
      overlay.setAttribute("aria-hidden", "true");
    }, 600);
  }, 2500);
}

function renderTabVisibility() {
  const isMaths = selectedSubjectId === "maths";
  els.tabs.forEach((btn) => {
    const tab = btn.dataset.tab;
    if (tab === "flashcards" || tab === "test") {
      btn.classList.toggle("hidden", isMaths);
    }
  });
  if (isMaths && !els.examTab.classList.contains("active")) {
    switchTab("exam");
  }
}

function renderAll() {
  reconcileSelection();
  renderAccount();
  renderProfileAvatar();
  renderAccountIdentity();
  renderAvatarPicker();
  renderSubjectPicker();
  renderGraph();
  renderSubjectOverview();
  renderOutcomePicker();
  renderStudyContext();
  renderTabVisibility();
  els.subjectWorkbench?.classList.toggle("learn-mode", els.flashcardsTab.classList.contains("active"));
  renderOutcomes();
  renderTestOverview();
  if (els.examTab?.classList.contains("active")) renderExamSection();
  const timerWidget = document.getElementById("timerWidget");
  if (timerWidget) timerWidget.classList.toggle("hidden", !getCurrentUser());
  // responsive.css shows only this screen on phones
  els.subjectArea.dataset.screen = phoneScreen();
}

function getEnabledSubjectIds(user) {
  if (!user) return SUBJECTS.map((s) => s.id);
  const allIds = SUBJECTS.map((s) => s.id);
  // New model: disabledSubjects stores explicit opt-outs; new subjects auto-appear.
  const disabled = new Set(Array.isArray(user.disabledSubjects) ? user.disabledSubjects : []);
  return allIds.filter((id) => !disabled.has(id));
}

function getEnabledSubjects() {
  const ids = getEnabledSubjectIds(getCurrentUser());
  return SUBJECTS.filter((s) => ids.includes(s.id));
}

function renderSubjectPicker() {
  if (!els.subjectPicker) return;
  const user = getCurrentUser();
  if (!user) {
    els.subjectPicker.innerHTML = "";
    return;
  }
  const disabled = new Set(Array.isArray(user.disabledSubjects) ? user.disabledSubjects : []);
  els.subjectPicker.innerHTML = SUBJECTS.map((s) => {
    const on = !disabled.has(s.id);
    const chapters = (s.chapters || []).length;
    return `
      <label class="subject-setting">
        <span class="subject-setting-text">
          <span class="subject-setting-name">${escapeHtml(s.title)}</span>
          <span class="subject-setting-meta">${chapters} chapter${chapters === 1 ? "" : "s"}</span>
        </span>
        <input type="checkbox" class="subject-setting-input" data-subject="${escapeHtml(s.id)}" ${on ? "checked" : ""} />
        <span class="subject-setting-switch" aria-hidden="true"></span>
      </label>`;
  }).join("");

  if (els.subjectChoicesCount) {
    const on = SUBJECTS.length - disabled.size;
    els.subjectChoicesCount.textContent = `${on} of ${SUBJECTS.length}`;
  }

  if (els.studyPlanValue) {
    const year = { ty: "TY", "5th": "5th Year", "6th": "6th Year" }[user.onboarding?.year];
    els.studyPlanValue.textContent = year || "Set up";
  }

  els.subjectPicker.querySelectorAll("input[type=checkbox]").forEach((cb) => {
    cb.addEventListener("change", () => {
      const u = getCurrentUser();
      if (!u) return;
      const unchecked = Array.from(
        els.subjectPicker.querySelectorAll("input[type=checkbox]:not(:checked)")
      ).map((el) => el.dataset.subject);
      // Keep at least one subject on, otherwise the app has nothing to show.
      if (unchecked.length === SUBJECTS.length) {
        cb.checked = true;
        return;
      }
      u.disabledSubjects = unchecked;
      const enabledIds = getEnabledSubjectIds(u);
      if (!enabledIds.includes(selectedSubjectId)) {
        const first = SUBJECTS.find((s) => enabledIds.includes(s.id));
        if (first) {
          selectedSubjectId = first.id;
          selectedChapterId = first.chapters[0]?.id || "";
          selectedOutcomeId = first.chapters[0]?.learningOutcomes[0]?.id || "";
          expandedSubjectId = "";
        }
      }
      persist();
      renderAll();
    });
  });
}

function renderAccount() {
  const current = getCurrentUser();
  if (!current) return;
  els.accountDetailsUsername.textContent = current.username || "";
  els.accountDetailsEmail.textContent = current.email || authSnapshot?.user?.email || "";
}

function renderAccountIdentity() {
  const current = getCurrentUser();
  if (!current) {
    els.accountIdentity.innerHTML = "";
    return;
  }
  const email = current.email || authSnapshot?.user?.email || "";
  els.accountIdentity.innerHTML = `
    <strong class="account-username">${escapeHtml(current.username)}</strong>
    ${email ? `<span class="account-email">${escapeHtml(email)}</span>` : ""}
  `;
}

function renderAvatarPicker() {
  // Color pickers removed — avatar is always the fixed orange accent.
}

function renderProfileAvatar() {
  if (!els.profileAvatar) return;
  const current = getCurrentUser();
  els.profileAvatar.textContent = current ? current.username[0].toUpperCase() : "";
  els.profileAvatar.title = current ? `${current.username}'s profile` : "Profile";
  els.profileAvatar.disabled = !current;
  if (!current) els.profileMenu.classList.add("hidden");
  renderProfileLevel();
}

function renderProfileLevel() {
  if (!els.profileLevel) return;
  const current = getCurrentUser();
  if (!current) {
    els.profileLevel.classList.add("hidden");
    return;
  }
  const { percent } = computeUserProgress(current);
  els.profileLevel.textContent = `${percent}%`;
  els.profileLevel.classList.remove("hidden");
}

function computeUserProgress(user) {
  const progress = user?.progressByOutcome || {};
  const learned = user?.learnedByOutcome || {};
  let earned = 0;
  let total = 0;
  const enabledIds = getEnabledSubjectIds(user);
  SUBJECTS.filter((s) => enabledIds.includes(s.id)).forEach((subject) => {
    (subject.chapters || []).forEach((ch) => {
      (ch.learningOutcomes || []).forEach((lo) => {
        const concepts = (lo.keyTerms || []).length;
        total += concepts;
        if ((progress[lo.id] || 0) >= 1) {
          earned += concepts;
        } else {
          earned += (learned[lo.id] || []).length;
        }
      });
    });
  });
  const percent = total ? Math.round((earned / total) * 100) : 0;
  return { earned, total, percent };
}


// ── Phone navigation ─────────────────────────────
// Phones show one screen at a time: subjects (and Progress), then chapters, then a
// chapter's subsections where it has them, then study. Each step down is a history
// entry, so the back gesture steps up a level instead of leaving the app.
function isPhoneLayout() {
  return window.matchMedia("(max-width: 640px)").matches;
}

function phoneScreen() {
  if (phoneHome) return "home";
  if (viewMode === "subject-overview") return "subject";
  return chapterHasSubsections(getSelectedChapter()) && !isPickingOutcome() ? "study" : "chapter";
}

function pushPhoneScreen(screen) {
  if (!isPhoneLayout() || history.state?.bbScreen === screen) return;
  history.pushState({ bbScreen: screen }, "", location.href);
}

// A screen that was pushed is left through history, so its entry doesn't linger
function leavePhoneScreen(screen, close) {
  if (history.state?.bbScreen === screen) history.back();
  else close();
}

function navigateUp() {
  if (isPhoneLayout() && history.state?.bbScreen) {
    history.back();
    return;
  }
  if (viewMode === "chapter") viewMode = "subject-overview";
  else phoneHome = true;
  renderAll();
}

function handlePhonePopState(event) {
  if (!isPhoneLayout()) return;
  // A running test sits on top of everything; keep the screen under it and restore the entry
  if (document.body.classList.contains("test-open")) {
    if (phoneScreen() !== "home") history.pushState({ bbScreen: phoneScreen() }, "", location.href);
    return;
  }
  const screen = event.state?.bbScreen || "home";
  if (screen !== "notes" && !els.fullNotesScreen.classList.contains("hidden")) closeFullNotes();
  if (screen !== "progress" && !els.progressScreen.classList.contains("hidden")) closeProgress();
  if (screen === "home") phoneHome = true;
  if (screen === "subject" || screen === "chapter" || screen === "study") {
    phoneHome = false;
    viewMode = screen === "subject" ? "subject-overview" : "chapter";
    // Stepping back onto a chapter with subsections lands on its subsection grid
    pickingOutcome = screen === "chapter" && chapterHasSubsections(getSelectedChapter());
  }
  renderAll();
}

function isCompactLayout() {
  return window.matchMedia("(max-width: 980px)").matches;
}

function renderGraph() {
  els.subjectGraph.innerHTML = "";
  getEnabledSubjects().forEach((subject) => {
    const block = document.createElement("div");
    block.className = "graph-subject";
    const hasBreakdown = !!window.EXAM_BREAKDOWN?.[subject.id];
    const expanded = expandedSubjectId === subject.id;
    block.classList.toggle("expanded", expanded);
    block.classList.toggle("selected", selectedSubjectId === subject.id);
    block.innerHTML = `
      <div class="graph-subject-header">
        <button class="graph-subject-name" aria-expanded="${expanded}">
          <span class="graph-subject-chevron" aria-hidden="true">›</span>
          <span class="graph-subject-title">${escapeHtml(subject.title)}</span>
          <span class="graph-subject-count" aria-label="${subject.chapters.length} chapters">${subject.chapters.length}</span>
        </button>
        ${hasBreakdown ? `<button class="graph-subject-exam" title="Marks, timing and structure for the ${escapeHtml(subject.title)} paper">Paper guide</button>` : ""}
      </div>
      <div class="graph-chapters ${expanded ? "" : "hidden"}" aria-label="${escapeHtml(subject.title)} chapters"></div>
    `;
    const openSubject = () => {
      // Phones show the chapter list as its own screen rather than the overlay sheet
      expandedSubjectId = isPhoneLayout() || expandedSubjectId === subject.id ? "" : subject.id;
      selectedSubjectId = subject.id;
      viewMode = 'subject-overview';
      phoneHome = false;
      pushPhoneScreen("subject");
      renderAll();
    };
    block.querySelector(".graph-subject-name").addEventListener("click", openSubject);
    block.querySelector(".graph-subject-exam")?.addEventListener("click", (event) => {
      event.stopPropagation();
      openExamBreakdown(subject.id);
    });
    const chaptersWrap = block.querySelector(".graph-chapters");
    subject.chapters.forEach((chapter) => {
      const chapterButton = document.createElement("button");
      chapterButton.className = `graph-chapter subject-open ${chapter.id === selectedChapterId ? "active" : ""}`;
      chapterButton.textContent = chapter.title;
      chapterButton.addEventListener("click", () => {
        selectedSubjectId = subject.id;
        selectedChapterId = chapter.id;
        selectedOutcomeId = chapter.learningOutcomes[0].id;
        // Below 980px the chapter list is an overlay, so picking a chapter closes it
        expandedSubjectId = isCompactLayout() ? "" : subject.id;
        studyIndex = 0;
        showAnswer = false;
        viewMode = 'chapter';
        pickingOutcome = chapterHasSubsections(chapter);
        renderAll();
      });
      chaptersWrap.appendChild(chapterButton);
    });
    els.subjectGraph.appendChild(block);
  });
  if (isCompactLayout()) {
    requestAnimationFrame(() => {
      els.subjectGraph.scrollLeft = 0;
    });
  }
  els.subjectWorkbench.classList.toggle("hidden", !getCurrentUser());
}

function renderStudyContext() {
  if (!els.studyContext) return;
  const subject = SUBJECTS.find((item) => item.id === selectedSubjectId);
  const chapter = getSelectedChapter();
  const isOverview = viewMode === "subject-overview";

  if (!subject || isOverview) {
    els.studyContext.innerHTML = "";
    return;
  }

  const outcome = getSelectedOutcome();
  if (chapterHasSubsections(chapter) && !isPickingOutcome() && outcome) {
    els.studyContext.innerHTML = `
      <button class="study-context-back" type="button" title="Choose another subsection">
        <span aria-hidden="true">‹</span>
        <span>${escapeHtml(subject.title)} · ${escapeHtml(chapter.title)}</span>
      </button>
      <strong title="${escapeHtml(compactText(outcome.title || ""))}">${escapeHtml(compactText(outcome.title || ""))}</strong>
    `;
    els.studyContext.querySelector(".study-context-back").addEventListener("click", () => {
      leavePhoneScreen("study", () => {
        pickingOutcome = true;
        renderAll();
      });
    });
    return;
  }

  els.studyContext.innerHTML = `
    <button class="nav-up" type="button" onclick="navigateUp()" aria-label="Back to ${escapeHtml(subject.title)} chapters">${escapeHtml(subject.title)}</button>
    <strong title="${escapeHtml(chapter?.title || "")}">${escapeHtml(chapter?.title || "")}</strong>
  `;
}

function chapterHasSubsections(chapter) {
  return (chapter?.learningOutcomes || []).length > 1;
}

function isPickingOutcome() {
  return pickingOutcome && viewMode !== "subject-overview" && chapterHasSubsections(getSelectedChapter());
}

// A chapter can hold many subsections. Opening one shows them all as a full
// screen grid; the study tabs and Full notes stay hidden until one is chosen.
function renderOutcomePicker() {
  const picker = els.outcomePicker;
  if (!picker) return;
  const picking = isPickingOutcome() && Boolean(getCurrentUser());
  els.subjectWorkbench.classList.toggle("picker-mode", picking);
  picker.classList.toggle("hidden", !picking);
  if (!picking) {
    picker.innerHTML = "";
    return;
  }

  const chapter = getSelectedChapter();
  const learnedByOutcome = getLearnedByOutcome();
  const cardsHtml = chapter.learningOutcomes.map((lo, idx) => {
    const cards = cardsForOutcome(lo, selectedSubjectId);
    const learned = new Set(learnedByOutcome[lo.id] || []);
    const done = cards.filter((c) => learned.has(c.id)).length;
    const pct = cards.length ? Math.round((done / cards.length) * 100) : 0;
    return `
      <button class="outcome-card ${pct === 100 ? "is-done" : ""}" type="button" data-outcome-id="${escapeHtml(lo.id)}">
        <span class="outcome-card-index">${String(idx + 1).padStart(2, "0")}</span>
        <span class="outcome-card-title">${escapeHtml(compactText(lo.title || `Subsection ${idx + 1}`))}</span>
        <span class="outcome-card-meta">
          <span class="outcome-card-bar"><span style="width:${pct}%"></span></span>
          <span>${done}/${cards.length}</span>
        </span>
      </button>`;
  }).join("");

  picker.innerHTML = `
    <header class="outcome-picker-head">
      <p>Choose a subsection · ${chapter.learningOutcomes.length} in this chapter</p>
    </header>
    <div class="outcome-picker-grid">${cardsHtml}</div>
  `;

  picker.querySelectorAll(".outcome-card").forEach((btn) => {
    btn.addEventListener("click", () => {
      selectedOutcomeId = btn.dataset.outcomeId;
      pickingOutcome = false;
      studyIndex = 0;
      showAnswer = false;
      pushPhoneScreen("study");
      renderAll();
    });
  });
}

function renderSubjectOverview() {
  const overviewEl = els.subjectOverview;
  if (!overviewEl) return;

  const isOverview = viewMode === 'subject-overview' && Boolean(getCurrentUser());
  els.subjectWorkbench.classList.toggle('overview-mode', isOverview);
  overviewEl.classList.toggle('hidden', !isOverview);

  if (!isOverview) return;

  const user = getCurrentUser();
  const subjectStats = buildProgressSubjectStats(user);
  const ss = subjectStats.find(s => s.subject.id === selectedSubjectId);
  if (!ss) { overviewEl.innerHTML = ''; return; }

  const rows = ss.chStats.map(s => {
    const pct = Math.round(s.ratio * 100);
    return `
      <button class="overview-chapter-row" onclick="selectChapterFromOverview('${escapeHtml(s.ch.id)}')">
        <div class="overview-chapter-text">
          <span class="overview-chapter-title">${escapeHtml(s.ch.title)}</span>
          <span class="overview-chapter-score">${s.earned}/${s.total}</span>
        </div>
        <div class="overview-progress-bar">
          <div class="overview-progress-fill" style="width:${pct}%"></div>
        </div>
      </button>`;
  }).join('');

  const hasBreakdown = !!window.EXAM_BREAKDOWN?.[ss.subject.id];
  overviewEl.innerHTML = `
    <div class="overview-nav">
      <button class="nav-up" type="button" onclick="navigateUp()" aria-label="Back to subjects">Subjects</button>
      ${hasBreakdown ? `<button class="overview-paper-guide" type="button" onclick="openExamBreakdown('${escapeHtml(ss.subject.id)}')">Paper guide</button>` : ""}
    </div>
    <div class="overview-header">
      <div class="overview-header-text">
        <h3>${escapeHtml(ss.subject.title)}</h3>
        <span class="muted small">${ss.pct}% · ${ss.earned}/${ss.total} concepts</span>
      </div>
      <div class="overview-total-bar">
        <div class="overview-total-fill" style="width:${ss.pct}%"></div>
      </div>
    </div>
    <div class="overview-chapter-list">${rows}</div>
  `;
}

function selectChapterFromOverview(chapterId) {
  const subject = SUBJECTS.find(s => s.id === selectedSubjectId);
  if (!subject) return;
  const chapter = subject.chapters.find(c => c.id === chapterId);
  if (!chapter) return;
  selectedChapterId = chapterId;
  selectedOutcomeId = chapter.learningOutcomes[0]?.id || '';
  studyIndex = 0;
  showAnswer = false;
  viewMode = 'chapter';
  pickingOutcome = chapterHasSubsections(chapter);
  // On phones a chapter opens on its flashcards (Maths has none; renderTabVisibility moves it to Exam)
  if (isPhoneLayout()) switchTab("flashcards");
  pushPhoneScreen("chapter");
  renderAll();
}

function renderOutcomes() {
  const chapter = getSelectedChapter();
  if (!chapter) return;
  let outcome = getSelectedOutcome();
  if (!outcome) {
    // Stale selection (e.g. chapter changed underneath) — fall back to its first outcome.
    selectedOutcomeId = chapter.learningOutcomes[0]?.id || "";
    outcome = getSelectedOutcome();
  }
  if (!outcome) return;

  els.flashcardList.innerHTML = "";
  const allPoints = outcome.keyTerms || [];
  allPoints.forEach((point, index) => {
    const li = document.createElement("li");
    li.className = "resource-item";
    li.innerHTML = `
      <div class="resource-item-main">
        <strong>${index + 1}. ${escapeHtml(compactText(point.term))}</strong>
        <p class="muted small">${escapeHtml(point.section || "")}</p>
        <p class="muted definition">${escapeHtml(compactText(point.definition))}</p>
      </div>
    `;
    els.flashcardList.appendChild(li);
  });

  const cards = cardsForOutcome(outcome, selectedSubjectId);
  if (studyIndex >= cards.length) studyIndex = 0;
  const card = cards[studyIndex] || { term: "No content", definition: "No chapter concepts loaded." };
  const learnedByOutcome = getLearnedByOutcome();
  const learnedSet = new Set(learnedByOutcome[outcome.id] || []);
  let chapterTotalCards = 0;
  let chapterLearnedCards = 0;
  chapter.learningOutcomes.forEach(lo => {
    const loCards = cardsForOutcome(lo, selectedSubjectId);
    chapterTotalCards += loCards.length;
    const loLearned = new Set(learnedByOutcome[lo.id] || []);
    chapterLearnedCards += loCards.filter(c => loLearned.has(c.id)).length;
  });
  const chapterPct = chapterTotalCards > 0 ? Math.round((chapterLearnedCards / chapterTotalCards) * 100) : 0;

  els.flashcardStudy.innerHTML = `
    <header class="study-card-head">
      <div class="study-progress" title="${chapterLearnedCards} of ${chapterTotalCards} concepts learned">
        <div class="progress-bar"><span style="width:${chapterPct}%"></span></div>
        <span>${chapterPct}%</span>
      </div>
      <span class="study-card-count">${cards.length ? studyIndex + 1 : 0}/${cards.length}</span>
    </header>
    <div class="study-face">${showAnswer ? escapeHtml(card.definition) : `<strong>${escapeHtml(card.term)}</strong>`}</div>
    <div class="study-card-footer">
      <div class="study-controls">
        <button id="prevCard" class="button-secondary study-step" aria-label="Previous concept">←</button>
        <button id="flipCard" class="button-primary">${showAnswer ? "Question" : "Reveal"}</button>
        <button id="nextCard" class="button-secondary study-step" aria-label="Next concept">→</button>
        <button id="markLearned" class="button-secondary study-learned" aria-label="${learnedSet.has(card.id) ? "Mark concept unlearned" : "Mark concept learned"}" title="${learnedSet.has(card.id) ? "Press again to mark unlearned" : "Mark this concept learned"}">${learnedSet.has(card.id) ? "✓ Learned" : "Mark learned"}</button>
      </div>
      ${showAnswer && card.keywords?.length ? `
        <details class="study-keywords">
          <summary>Key words</summary>
          <div class="study-keywords-panel">
            ${renderKeywordRow(card.keywords)}
            <p>Worth using in a written answer.</p>
          </div>
        </details>` : ""}
    </div>
  `;

  document.getElementById("prevCard").addEventListener("click", () => {
    studyIndex = (studyIndex - 1 + cards.length) % cards.length;
    showAnswer = false;
    renderOutcomes();
  });
  document.getElementById("nextCard").addEventListener("click", () => {
    studyIndex = (studyIndex + 1) % cards.length;
    showAnswer = false;
    renderOutcomes();
  });
  document.getElementById("flipCard").addEventListener("click", () => {
    showAnswer = !showAnswer;
    renderOutcomes();
  });
  els.flashcardStudy.querySelector(".study-face").addEventListener("click", () => {
    if (window.getSelection()?.toString()) return;
    showAnswer = !showAnswer;
    renderOutcomes();
  });
  document.getElementById("markLearned").addEventListener("click", () => {
    const learnedByOutcome = getLearnedByOutcome();
    if (!learnedByOutcome[outcome.id]) learnedByOutcome[outcome.id] = [];
    const set = new Set(learnedByOutcome[outcome.id]);
    if (set.has(card.id)) {
      set.delete(card.id);
    } else {
      set.add(card.id);
    }
    learnedByOutcome[outcome.id] = Array.from(set);
    persist();
    renderProfileLevel();
    renderOutcomes();
    renderTestOverview();
  });

  els.hierarchyPanel.classList.add("hidden");
}

function renderHierarchy(chapter) {
  els.hierarchyPanel.classList.remove("hidden");
  const allPoints = chapter.learningOutcomes.flatMap((lo) => lo.keyTerms || []);
  els.hierarchyPanel.innerHTML = `
    <h4>Chapter Notes</h4>
    <ul>${allPoints.map((p) => `<li><strong>${escapeHtml(compactText(p.term))}:</strong> ${escapeHtml(compactText(p.definition))}</li>`).join("")}</ul>
  `;
}

// ── Test ──────────────────────────────────────────────────────
// A test is a scope (this chapter, the whole subject, or chosen chapters), a
// length in minutes and a mix of flashcard and exam questions. test-builder.js
// picks the questions; this section renders setup, the timed run, marking and
// results on the full-screen #testScreen. Its constants and state live up with
// the other top-level state (search "Test state").

function getTestSettings() {
  let saved = {};
  try {
    saved = JSON.parse(localStorage.getItem(TEST_SETTINGS_KEY) || "{}") || {};
  } catch (error) {
    saved = {};
  }
  return {
    scope: ["chapter", "subject", "custom"].includes(saved.scope) ? saved.scope : "chapter",
    minutes: TEST_LENGTHS.includes(saved.minutes) ? saved.minutes : 10,
    mix: TEST_MIXES.some((mix) => mix.id === saved.mix) ? saved.mix : "balanced",
    customChapters: saved.customChapters && typeof saved.customChapters === "object" ? saved.customChapters : {},
  };
}

function saveTestSettings(settings) {
  try {
    localStorage.setItem(TEST_SETTINGS_KEY, JSON.stringify(settings));
  } catch (error) {
    // Settings are a per-device convenience; the defaults are fine without them.
  }
}

function getTestScope(settings = getTestSettings()) {
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  if (!subject) return { subject: null, chapters: [], label: "" };
  if (settings.scope === "subject") {
    return { subject, chapters: subject.chapters, label: `All of ${subject.title}` };
  }
  if (settings.scope === "custom") {
    const ids = new Set(settings.customChapters[subject.id] || []);
    const chapters = subject.chapters.filter((c) => ids.has(c.id));
    const label = chapters.length === 1 ? chapters[0].title : `${chapters.length} ${subject.title} chapters`;
    return { subject, chapters, label };
  }
  const chapter = getSelectedChapter();
  return { subject, chapters: chapter ? [chapter] : [], label: chapter?.title || "" };
}

function getTestPool(subject, chapters) {
  const key = `${subject.id}|${chapters.map((c) => c.id).join(",")}`;
  if (!testPoolCache.has(key)) {
    testPoolCache.set(key, TestBuilder.buildPool({
      subjectId: subject.id,
      breakdown: window.EXAM_BREAKDOWN?.[subject.id],
      chapters,
      subjectChapters: subject.chapters,
      examGroupsFor: getExamQuestionsForChapter,
      authoredFor: authoredQuestionsForChapter,
      prompts: window.FLASHCARD_TEST_PROMPTS || {},
    }));
  }
  return testPoolCache.get(key);
}

// Hand-written outcome questions (the *-test-questions.js packs), tagged with
// the outcome id the flashcard view uses for the same content.
function authoredQuestionsForChapter(chapter) {
  const source = getOriginalChapter(chapter.id);
  if (!source) return [];
  const outcomeIds = new Set(chapter.learningOutcomes.map((lo) => lo.id));
  const fallbackId = chapter.learningOutcomes[0]?.id || "";
  return (source.learningOutcomes || []).flatMap((lo) => {
    const outcomeId = outcomeIds.has(`${lo.id}-core`) ? `${lo.id}-core` : fallbackId;
    return (lo.questions || []).map((question) => ({ outcomeId, question }));
  });
}

// Deterministic random so the setup preview does not reshuffle on every render.
function seededRandom(seed) {
  let t = seed >>> 0;
  return () => {
    t += 0x6d2b79f5;
    let r = Math.imul(t ^ (t >>> 15), 1 | t);
    r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
    return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
  };
}

function plural(count, word, pluralWord = `${word}s`) {
  return `${count} ${count === 1 ? word : pluralWord}`;
}

function formatClock(ms) {
  const total = Math.max(0, Math.ceil(ms / 1000));
  return `${Math.floor(total / 60)}:${String(total % 60).padStart(2, "0")}`;
}

function formatRelativeDay(timestamp) {
  const days = Math.floor((Date.now() - timestamp) / 86400000);
  if (days <= 0) return "Today";
  if (days === 1) return "Yesterday";
  if (days < 7) return `${days} days ago`;
  return new Date(timestamp).toLocaleDateString(undefined, { day: "numeric", month: "short" });
}

function testSourceTag(item) {
  const source = String(item.source || "");
  const level = /ordinary/i.test(source) ? "Ordinary" : /higher/i.test(source) ? "Higher" : "";
  const oldSyllabus = /\[(?:LEGACY|REFERENCE)\b/i.test(source) ? "old syllabus" : "";
  // Undated chapter questions ("LC Biology Past Paper — Q2 (Scientific Method)")
  // carry their topic in the source, so keep it rather than truncating.
  const tag = item.year || /\b(?:19|20)\d{2}\b/.test(source)
    ? compactExamSource({ source, year: item.year, id: item.groupId })
    : source.replace(/\[.*?\]/g, "").replace(/^LC\s+.+?\s+(?=Past Paper)/i, "").replace(/\s*[—–]\s*/g, " · ").trim();
  return [tag, level, oldSyllabus].filter(Boolean).join(" · ");
}

function testMultiline(text) {
  return escapeHtml(String(text || "").trim()).replace(/\n/g, "<br>");
}

// ── Setup (inside the Test tab) ──

function renderTestOverview() {
  if (!els.testContainer) return;
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  if (!subject) return;
  const settings = getTestSettings();
  const scope = getTestScope(settings);
  const pool = scope.chapters.length ? getTestPool(subject, scope.chapters) : null;
  const preview = pool
    ? TestBuilder.assembleTest(pool, { minutes: settings.minutes, mix: settings.mix, random: seededRandom(7) })
    : null;
  const chosen = new Set(settings.customChapters[subject.id] || []);

  const choice = (attr, value, label, active) => `
    <button type="button" class="test-choice${active ? " is-active" : ""}" role="radio" aria-checked="${active}" ${attr}="${escapeHtml(value)}">${label}</button>`;

  const chapterPicker = settings.scope === "custom" ? `
    <div class="test-chapter-picker">
      <div class="test-chapter-picker-head">
        <span>${plural(chosen.size, "chapter")} chosen</span>
        <button type="button" class="test-link" data-test-chapters="all">Select all</button>
        <button type="button" class="test-link" data-test-chapters="none">Clear</button>
      </div>
      <ul class="test-chapter-list">
        ${subject.chapters.map((chapter) => `
          <li>
            <label class="test-chapter-option">
              <input type="checkbox" data-test-chapter="${escapeHtml(chapter.id)}" ${chosen.has(chapter.id) ? "checked" : ""} />
              <span>${escapeHtml(chapter.title)}</span>
            </label>
          </li>`).join("")}
      </ul>
    </div>` : "";

  els.testContainer.innerHTML = `
    <div class="test-setup">
      <div class="test-setup-row">
        <span class="test-setup-label" id="testScopeLabel">Cover</span>
        <div class="test-choices" role="radiogroup" aria-labelledby="testScopeLabel">
          ${choice("data-test-scope", "chapter", "This chapter", settings.scope === "chapter")}
          ${choice("data-test-scope", "subject", `All of ${escapeHtml(subject.title)}`, settings.scope === "subject")}
          ${choice("data-test-scope", "custom", "Choose chapters", settings.scope === "custom")}
        </div>
      </div>
      ${chapterPicker}
      <div class="test-setup-row">
        <span class="test-setup-label" id="testLengthLabel">Time</span>
        <div class="test-choices" role="radiogroup" aria-labelledby="testLengthLabel">
          ${TEST_LENGTHS.map((m) => choice("data-test-minutes", m, `${m} min`, settings.minutes === m)).join("")}
        </div>
      </div>
      <div class="test-setup-row">
        <span class="test-setup-label" id="testMixLabel">Mix</span>
        <div class="test-choices" role="radiogroup" aria-labelledby="testMixLabel">
          ${TEST_MIXES.map((mix) => choice("data-test-mix", mix.id, mix.label, settings.mix === mix.id)).join("")}
        </div>
      </div>
      ${renderTestPreview(scope, preview, settings)}
      ${renderTestHistory(subject)}
    </div>
  `;
}

function renderTestPreview(scope, preview, settings) {
  const signedIn = Boolean(getCurrentUser());
  let summary;
  let canStart = signedIn;
  if (!scope.chapters.length) {
    summary = "Choose at least one chapter.";
    canStart = false;
  } else if (!preview?.items.length) {
    summary = "There is nothing to test in this scope yet.";
    canStart = false;
  } else {
    const flashcards = preview.items.filter((i) => i.bucket === "flashcard").length;
    const exam = preview.items.length - flashcards;
    const parts = [
      flashcards ? plural(flashcards, "flashcard question") : "",
      exam ? plural(exam, "exam question") : "",
    ].filter(Boolean).join(" and ");
    const spread = preview.chapterIds.length > 1 ? `, drawn from ${plural(preview.chapterIds.length, "chapter")}` : "";
    const plannedMinutes = Math.ceil(preview.plannedSeconds / 60);
    const shortfall = plannedMinutes < settings.minutes - 1
      ? `<span class="test-preview-note">That fills about ${plannedMinutes} of your ${settings.minutes} minutes. Cover more chapters for a longer test.</span>`
      : "";
    summary = `About <strong>${plural(preview.items.length, "question")}</strong>: ${parts}${spread}. ${shortfall}`;
  }
  const minutesLabel = preview?.items.length
    ? Math.min(settings.minutes, Math.ceil(preview.plannedSeconds / 60))
    : settings.minutes;
  return `
    <div class="test-setup-start">
      <p class="test-preview">${summary}</p>
      <button type="button" class="button-primary test-start" data-test-action="start" ${canStart ? "" : "disabled"}>
        Start ${minutesLabel} minute test
      </button>
      ${signedIn ? "" : `<p class="test-preview-note">Log in to take tests and track your progress.</p>`}
    </div>`;
}

function renderTestHistory(subject) {
  const history = (getCurrentUser()?.testHistory || []).filter((entry) => entry.subjectId === subject.id).slice(0, 5);
  if (!history.length) return "";
  return `
    <section class="test-history" aria-label="Recent tests">
      <h4>Recent</h4>
      <ol>
        ${history.map((entry) => `
          <li>
            <strong class="${entry.percent >= TEST_PASS_PERCENT ? "is-pass" : ""}">${entry.percent}%</strong>
            <span>${escapeHtml(entry.label || "")} · ${entry.minutes} min</span>
            <time datetime="${new Date(entry.at).toISOString()}">${formatRelativeDay(entry.at)}</time>
          </li>`).join("")}
      </ol>
    </section>`;
}

function handleTestSetupClick(event) {
  const target = event.target.closest("button");
  if (!target || !els.testContainer.contains(target)) return;
  const settings = getTestSettings();
  if (target.dataset.testScope) {
    settings.scope = target.dataset.testScope;
    if (settings.scope === "custom" && !(settings.customChapters[selectedSubjectId] || []).length && selectedChapterId) {
      settings.customChapters[selectedSubjectId] = [selectedChapterId];
    }
  } else if (target.dataset.testMinutes) {
    settings.minutes = Number(target.dataset.testMinutes);
  } else if (target.dataset.testMix) {
    settings.mix = target.dataset.testMix;
  } else if (target.dataset.testChapters) {
    const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
    settings.customChapters[selectedSubjectId] = target.dataset.testChapters === "all"
      ? subject.chapters.map((c) => c.id)
      : [];
  } else if (target.dataset.testAction === "start") {
    startTest();
    return;
  } else {
    return;
  }
  saveTestSettings(settings);
  renderTestOverview();
}

function handleTestSetupChange(event) {
  const box = event.target.closest("[data-test-chapter]");
  if (!box) return;
  const settings = getTestSettings();
  const chosen = new Set(settings.customChapters[selectedSubjectId] || []);
  if (box.checked) chosen.add(box.dataset.testChapter);
  else chosen.delete(box.dataset.testChapter);
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  settings.customChapters[selectedSubjectId] = subject.chapters.map((c) => c.id).filter((id) => chosen.has(id));
  saveTestSettings(settings);
  renderTestOverview();
}

// ── Running a test ──

function startTest(retestItems) {
  if (!getCurrentUser()) return;
  const settings = getTestSettings();
  const scope = getTestScope(settings);
  if (!scope.subject || !scope.chapters.length) return;
  const pool = getTestPool(scope.subject, scope.chapters);
  const test = retestItems
    ? { items: retestItems, plannedSeconds: retestItems.reduce((s, i) => s + i.seconds, 0) }
    : TestBuilder.assembleTest(pool, { minutes: settings.minutes, mix: settings.mix });
  if (!test.items.length) return;

  // The clock is the chosen length, unless the scope cannot fill it.
  const budgetSeconds = Math.max(60, Math.min(settings.minutes * 60, Math.ceil(test.plannedSeconds / 60) * 60));
  activeTest = {
    id: `t${Date.now().toString(36)}`,
    subjectId: scope.subject.id,
    subjectTitle: scope.subject.title,
    label: retestItems ? `Retest: ${String(activeTest?.label || scope.label).replace(/^Retest: /, "")}` : scope.label,
    chapterTitles: { ...pool.chapterTitles, ...(activeTest?.chapterTitles || {}) },
    items: test.items,
    responses: {},
    index: 0,
    budgetSeconds,
    startedAt: Date.now(),
    endsAt: Date.now() + budgetSeconds * 1000,
    phase: "run",
    timeUp: false,
    confirmQuit: false,
    clock: null,
  };
  els.testScreen.classList.remove("hidden");
  document.body.classList.add("test-open");
  renderTestScreen();
  startTestClock();
}

function startTestClock() {
  stopTestClock();
  activeTest.clock = window.setInterval(tickTestClock, 250);
  tickTestClock();
}

function stopTestClock() {
  if (activeTest?.clock) window.clearInterval(activeTest.clock);
  if (activeTest) activeTest.clock = null;
}

function tickTestClock() {
  if (!activeTest || activeTest.phase !== "run") {
    stopTestClock();
    return;
  }
  const left = Math.max(0, activeTest.endsAt - Date.now());
  const clock = els.testScreen.querySelector("[data-test-clock]");
  if (clock) {
    clock.textContent = formatClock(left);
    clock.classList.toggle("is-low", left <= 60000);
  }
  const fill = els.testScreen.querySelector("[data-test-time-fill]");
  if (fill) fill.style.transform = `scaleX(${1 - left / (activeTest.budgetSeconds * 1000)})`;
  if (left <= 0) finishTest(true);
}

function renderTestScreen() {
  if (!activeTest) return;
  if (activeTest.phase === "run") {
    els.testScreen.innerHTML = renderTestRun();
    // Keep the current question in view on a long, horizontally scrolling map.
    const map = els.testScreen.querySelector(".test-map");
    const dot = map?.querySelector(".is-current");
    if (map && dot) {
      const mapBox = map.getBoundingClientRect();
      const dotBox = dot.getBoundingClientRect();
      map.scrollLeft += dotBox.left - mapBox.left - (mapBox.width - dotBox.width) / 2;
    }
  } else if (activeTest.phase === "review") {
    els.testScreen.innerHTML = renderTestReview();
  } else {
    els.testScreen.innerHTML = renderTestResults();
  }
  if (typeof renderMathInElement !== "undefined") {
    renderMathInElement(els.testScreen, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
      ],
      throwOnError: false,
    });
  }
}

function renderTestBar(right, extra = "") {
  return `
    <header class="test-bar">
      <div class="test-bar-context">
        <span>${escapeHtml(activeTest.subjectTitle)}</span>
        <strong title="${escapeHtml(activeTest.label)}">${escapeHtml(activeTest.label)}</strong>
      </div>
      <div class="test-bar-actions">${right}</div>
      ${extra}
    </header>`;
}

function isItemAnswered(item) {
  const response = activeTest.responses[item.id];
  if (!response) return false;
  if (TEST_CHOICE_KINDS.has(item.kind)) return Number.isInteger(response.choice);
  if (item.kind === "cloze") return (response.blanks || []).some((b) => String(b || "").trim());
  return Boolean(String(response.text || "").trim());
}

function renderTestRun() {
  const { items, index } = activeTest;
  const item = items[index];
  const isLast = index === items.length - 1;
  const barActions = activeTest.confirmQuit
    ? `<span class="test-quit-ask">Quit without saving?</span>
       <button type="button" class="button-secondary" data-test-action="quit-confirm">Quit</button>
       <button type="button" class="button-primary" data-test-action="quit-cancel">Keep going</button>`
    : `<button type="button" class="test-link" data-test-action="quit">Quit</button>
       <span class="test-clock" data-test-clock role="timer" aria-label="Time left">${formatClock(activeTest.endsAt - Date.now())}</span>
       <button type="button" class="button-secondary" data-test-action="finish">Finish</button>`;
  const map = items.map((entry, i) => `
    <button type="button" class="test-map-dot${i === index ? " is-current" : ""}${isItemAnswered(entry) ? " is-answered" : ""}"
      data-test-goto="${i}" aria-label="Question ${i + 1}${isItemAnswered(entry) ? ", answered" : ""}"${i === index ? ' aria-current="step"' : ""}>${i + 1}</button>`).join("");

  return `
    <div class="test-run">
      ${renderTestBar(barActions, `<div class="test-time-track" aria-hidden="true"><span data-test-time-fill></span></div>`)}
      <main class="test-stage">
        <p class="test-question-meta">
          <span class="test-kind">${TEST_KIND_LABELS[item.kind]}</span>
          <span>Question ${index + 1} of ${items.length}</span>
          <span>${escapeHtml(activeTest.chapterTitles[item.chapterId] || "")}</span>
        </p>
        ${renderTestQuestion(item)}
      </main>
      <footer class="test-foot">
        <button type="button" class="button-secondary test-step" data-test-action="prev" ${index === 0 ? "disabled" : ""}>Back</button>
        <nav class="test-map" aria-label="Questions">${map}</nav>
        <button type="button" class="button-primary test-step" data-test-action="${isLast ? "finish" : "next"}">${isLast ? "Finish" : "Next"}</button>
      </footer>
    </div>`;
}

function renderTestOptions(item, response) {
  const keys = ["A", "B", "C", "D", "E", "F"];
  return `
    <div class="test-options" role="radiogroup" aria-label="Answers">
      ${item.options.map((option, i) => {
        const picked = response?.choice === i;
        return `
          <button type="button" class="test-option${picked ? " is-picked" : ""}" role="radio" aria-checked="${picked}" data-test-choice="${i}">
            <kbd>${keys[i]}</kbd><span>${escapeHtml(option)}</span>
          </button>`;
      }).join("")}
    </div>`;
}

function renderTestQuestion(item) {
  const response = activeTest.responses[item.id] || {};
  if (item.kind === "pick-term") {
    return `
      <p class="test-instruction">Which term does this describe?</p>
      <blockquote class="test-description">${escapeHtml(item.prompt)}</blockquote>
      ${renderTestOptions(item, response)}`;
  }
  if (item.kind === "pick-definition") {
    return `
      <p class="test-instruction">Choose the description that fits.</p>
      <h2 class="test-prompt">${escapeHtml(item.prompt)}</h2>
      ${renderTestOptions(item, response)}`;
  }
  if (item.kind === "mcq" || item.kind === "tf") {
    return `
      <h2 class="test-prompt">${testMultiline(item.prompt)}</h2>
      ${renderTestOptions(item, response)}`;
  }
  if (item.kind === "cloze") {
    const blanks = response.blanks || [];
    const sentence = item.segments.map((segment) => {
      if (segment.blank === undefined) return escapeHtml(segment.text);
      return `<input class="test-blank" type="text" autocomplete="off" autocapitalize="off" spellcheck="false"
        data-test-blank="${segment.blank}" value="${escapeHtml(blanks[segment.blank] || "")}"
        aria-label="Missing word ${segment.blank + 1}" />`;
    }).join("");
    return `
      <p class="test-instruction">Fill in the missing ${item.answers.length === 1 ? "word" : "words"}.</p>
      <h2 class="test-prompt">${escapeHtml(item.prompt)}</h2>
      <p class="test-cloze">${sentence}</p>`;
  }
  if (item.kind === "recall") {
    return `
      <p class="test-instruction">Answer from memory. You will check it against the flashcard at the end.</p>
      <h2 class="test-prompt">${escapeHtml(item.prompt)}</h2>
      <textarea class="test-answer" data-test-text rows="4" placeholder="Your answer">${escapeHtml(response.text || "")}</textarea>`;
  }
  // Exam part or exam-style written question.
  const minutes = Math.max(1, Math.round(item.seconds / 60));
  const source = item.groupId ? testSourceTag(item) : item.source;
  return `
    <p class="test-instruction test-exam-meta">
      <span class="test-source">${escapeHtml(source)}${item.label ? ` · ${escapeHtml(item.label)}` : ""}${item.continuation ? " (continued)" : ""}</span>
      <span>${plural(item.marks, "mark")} · about ${minutes} min</span>
    </p>
    ${item.context ? `<div class="test-context">${testMultiline(item.context)}</div>` : ""}
    <h2 class="test-prompt test-prompt--exam">${testMultiline(item.prompt)}</h2>
    ${item.diagram ? `<button type="button" class="button-secondary test-diagram" data-test-diagram="${escapeHtml(item.diagram)}">Show diagram</button>` : ""}
    <textarea class="test-answer" data-test-text rows="${item.marks >= 20 ? 10 : 6}" placeholder="Your answer">${escapeHtml(response.text || "")}</textarea>`;
}

function goToTestQuestion(index) {
  if (!activeTest || index < 0 || index >= activeTest.items.length) return;
  activeTest.index = index;
  renderTestScreen();
  tickTestClock();
  // Only text fields take focus; a focus ring on an option would read as a pick.
  const field = els.testScreen.querySelector(".test-blank, .test-answer");
  if (field) field.focus({ preventScroll: true });
  else if (els.testScreen.contains(document.activeElement)) document.activeElement.blur();
  els.testScreen.scrollTop = 0;
}

function finishTest(timeUp = false) {
  if (!activeTest || activeTest.phase !== "run") return;
  stopTestClock();
  activeTest.phase = "review";
  activeTest.timeUp = timeUp;
  activeTest.finishedAt = Date.now();
  renderTestScreen();
  els.testScreen.scrollTop = 0;
}

function closeTestScreen() {
  stopTestClock();
  activeTest = null;
  els.testScreen.classList.add("hidden");
  els.testScreen.innerHTML = "";
  document.body.classList.remove("test-open");
  renderTestOverview();
}

// ── Marking ──

function renderTestReview() {
  const summary = TestBuilder.scoreTest(activeTest, activeTest.responses);
  const pending = summary.pendingSelfMarks;
  const saveLabel = pending ? `Save result (${plural(pending, "answer")} unmarked)` : "Save result";
  const used = formatClock((activeTest.finishedAt - activeTest.startedAt));
  const intro = activeTest.timeUp
    ? "Time ran out. Anything you left blank scores zero."
    : `You finished in ${used}.`;
  const hasSelfMarked = activeTest.items.some((item) => item.kind === "recall" || item.kind === "written");

  return `
    <div class="test-review">
      ${renderTestBar(`
        <span class="test-live-score">${summary.percent}% so far</span>
        <button type="button" class="button-primary" data-test-action="save">${saveLabel}</button>`)}
      <main class="test-sheet">
        <header class="test-sheet-head">
          <h1>Mark your answers</h1>
          <p>${intro} ${hasSelfMarked ? "Quick questions are marked for you. For written answers, compare yours with the answer shown and give yourself the marks an examiner would." : "Every answer here was marked for you."}</p>
        </header>
        <ol class="test-review-list">
          ${activeTest.items.map((item, i) => renderTestReviewItem(item, i)).join("")}
        </ol>
        <div class="test-sheet-foot">
          <button type="button" class="button-primary" data-test-action="save">${saveLabel}</button>
          <button type="button" class="test-link" data-test-action="quit-confirm">Discard this test</button>
        </div>
      </main>
    </div>`;
}

function renderTestReviewItem(item, index) {
  const response = activeTest.responses[item.id] || {};
  const result = TestBuilder.markItem(item, response);
  let verdict;
  if (result.needsSelfMark) verdict = `<span class="test-verdict is-pending">To mark</span>`;
  else if (item.kind === "recall" || item.kind === "written" || item.kind === "cloze") {
    verdict = `<span class="test-verdict${result.earned === item.marks ? " is-right" : result.earned ? " is-part" : " is-wrong"}">${result.earned}/${plural(item.marks, "mark")}</span>`;
  } else {
    verdict = `<span class="test-verdict ${result.correct ? "is-right" : "is-wrong"}">${result.correct ? "Right" : "Wrong"}</span>`;
  }

  return `
    <li class="test-review-item" id="review-${escapeHtml(item.id)}">
      <div class="test-review-head">
        <span class="test-review-num">${index + 1}</span>
        <span class="test-kind">${TEST_KIND_LABELS[item.kind]}</span>
        <span class="test-review-chapter">${escapeHtml(activeTest.chapterTitles[item.chapterId] || "")}</span>
        ${verdict}
      </div>
      ${renderTestReviewBody(item, response, result)}
    </li>`;
}

function renderTestReviewBody(item, response, result) {
  if (TEST_CHOICE_KINDS.has(item.kind)) {
    const given = Number.isInteger(response.choice) ? item.options[response.choice] : null;
    const prompt = item.kind === "pick-term"
      ? `<p class="test-review-prompt test-review-prompt--quote">${escapeHtml(item.prompt)}</p>`
      : `<p class="test-review-prompt">${testMultiline(item.prompt)}</p>`;
    return `
      ${prompt}
      <dl class="test-review-answers">
        <dt>You said</dt>${given === null ? `<dd class="is-empty">No answer</dd>` : `<dd class="${result.correct ? "is-right" : "is-wrong"}">${escapeHtml(given)}</dd>`}
        ${result.correct ? "" : `<dt>Answer</dt><dd class="is-right">${escapeHtml(item.options[item.correctIndex])}</dd>`}
      </dl>
      ${item.model && !result.correct ? `<p class="test-review-why">${escapeHtml(compactText(item.model))}</p>` : ""}`;
  }

  if (item.kind === "cloze") {
    const blanks = response.blanks || [];
    const sentence = item.segments.map((segment) => {
      if (segment.blank === undefined) return escapeHtml(segment.text);
      const i = segment.blank;
      const given = String(blanks[i] || "").trim();
      const answer = item.answers[i];
      if (result.blanks[i]) return `<mark class="test-fill is-right">${escapeHtml(given || answer)}</mark>`;
      const countIt = given
        ? `<button type="button" class="test-link test-count-it" data-test-override="${i}">I was right</button>`
        : "";
      return `<span class="test-fill-wrong">${given ? `<s>${escapeHtml(given)}</s> ` : ""}<mark class="test-fill">${escapeHtml(answer)}</mark>${countIt}</span>`;
    }).join("");
    return `
      <p class="test-review-prompt"><strong>${escapeHtml(item.prompt)}</strong></p>
      <p class="test-cloze test-cloze--review">${sentence}</p>`;
  }

  const answerBox = `
    <div class="test-review-yours">
      <span class="test-review-label">Your answer</span>
      <p>${response.text?.trim() ? testMultiline(response.text) : `<em>No answer</em>`}</p>
    </div>`;

  if (item.kind === "recall") {
    const marks = response.selfMarks;
    const choices = [
      { value: 0, label: "Missed it" },
      { value: 1, label: "Partly" },
      { value: 2, label: "Got it" },
    ];
    return `
      <p class="test-review-prompt">${escapeHtml(item.prompt)}</p>
      ${answerBox}
      <div class="test-review-model">
        <span class="test-review-label">The flashcard</span>
        <p><strong>${escapeHtml(item.term)}</strong> ${escapeHtml(item.definition)}</p>
      </div>
      <div class="test-selfmark" role="radiogroup" aria-label="How did you do?">
        ${choices.map((c) => `<button type="button" class="test-choice${marks === c.value ? " is-active" : ""}" role="radio" aria-checked="${marks === c.value}" data-test-selfmark="${c.value}">${c.label}</button>`).join("")}
      </div>`;
  }

  // Written exam answer: model answer plus a marks picker.
  const marks = response.selfMarks;
  const picker = item.marks <= 12
    ? `<div class="test-selfmark test-selfmark--marks" role="radiogroup" aria-label="Marks out of ${item.marks}">
        ${Array.from({ length: item.marks + 1 }, (_, m) => `<button type="button" class="test-choice${marks === m ? " is-active" : ""}" role="radio" aria-checked="${marks === m}" data-test-selfmark="${m}">${m}</button>`).join("")}
       </div>`
    : `<label class="test-selfmark test-selfmark--range">
        <input type="range" min="0" max="${item.marks}" step="1" value="${Number.isFinite(marks) ? marks : 0}" data-test-selfmark-range />
        <output>${Number.isFinite(marks) ? `${marks} / ${item.marks}` : "Drag to mark"}</output>
       </label>`;
  const scheme = item.schemePoints ? `<span class="test-review-hint">The marking scheme looks for ${plural(item.schemePoints, "point")}.</span>` : "";
  return `
    <p class="test-review-prompt">${testMultiline(item.prompt)}</p>
    ${answerBox}
    <div class="test-review-model">
      <span class="test-review-label">${item.groupId ? "Marking scheme answer" : "Model answer"}</span>
      <div class="exam-answer-text">${item.groupId ? formatModelAnswer(item.model) : formatAuthoredModel(item.model)}</div>
      ${scheme}
    </div>
    <div class="test-selfmark-row">
      <span class="test-review-label">Your marks</span>
      ${picker}
    </div>`;
}

// Hand-written outcome questions write model answers in light Markdown
// (**bold** labels, one point per line); past-paper answers use formatModelAnswer.
function formatAuthoredModel(text) {
  return String(text || "")
    .split(/\n+/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => `<p class="model-srp">${escapeHtml(line).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")}</p>`)
    .join("");
}

// ── Saving and results ──

function findOutcomeById(outcomeId) {
  for (const subject of SUBJECTS) {
    for (const chapter of subject.chapters || []) {
      const outcome = chapter.learningOutcomes.find((lo) => lo.id === outcomeId);
      if (outcome) return outcome;
    }
  }
  return null;
}

// A right answer in a test is proof the card is known, so it counts as learned.
// An outcome moves up a step only when the test covered a fair share of it.
function applyTestProgress(summary) {
  const user = getCurrentUser();
  const learned = getLearnedByOutcome();
  const progress = getProgressByOutcome();
  let newlyLearned = 0;
  Object.entries(summary.byOutcome).forEach(([outcomeId, stats]) => {
    if (!stats.correctCards.length) return;
    const known = new Set(learned[outcomeId] || []);
    stats.correctCards.forEach((cardId) => {
      if (!known.has(cardId)) newlyLearned += 1;
      known.add(cardId);
    });
    learned[outcomeId] = Array.from(known);
    const size = findOutcomeById(outcomeId)?.keyTerms?.length || 0;
    const coveredEnough = stats.count >= Math.max(3, Math.ceil(size / 2));
    if (coveredEnough && stats.correct / stats.count >= TEST_PASS_PERCENT / 100) {
      progress[outcomeId] = Math.min(3, (progress[outcomeId] || 0) + 1);
    }
  });
  if (summary.percent >= TEST_PASS_PERCENT && user) user.testsCompleted = (user.testsCompleted || 0) + 1;
  return newlyLearned;
}

function saveTestResult() {
  if (!activeTest || activeTest.phase !== "review") return;
  const summary = TestBuilder.scoreTest(activeTest, activeTest.responses);
  const user = getCurrentUser();
  const newlyLearned = applyTestProgress(summary);
  if (user) {
    user.testHistory = mergeTestHistory([{
      id: activeTest.id,
      at: Date.now(),
      subjectId: activeTest.subjectId,
      label: activeTest.label,
      minutes: Math.round(activeTest.budgetSeconds / 60),
      usedSeconds: Math.round((activeTest.finishedAt - activeTest.startedAt) / 1000),
      percent: summary.percent,
      flashcards: { correct: summary.buckets.flashcard.correct, count: summary.buckets.flashcard.count },
      exam: { earned: summary.buckets.exam.earned, total: summary.buckets.exam.total },
    }], user.testHistory || []);
  }
  // The preview profile is throwaway; saving it would surface as a legacy account.
  if (!isLocalTestPreview) persist();
  activeTest.phase = "results";
  activeTest.summary = summary;
  activeTest.newlyLearned = newlyLearned;
  renderOutcomes();
  renderProfileLevel();
  renderTestScreen();
  els.testScreen.scrollTop = 0;
}

function missedTestItems() {
  return activeTest.items.filter((item) => !TestBuilder.markItem(item, activeTest.responses[item.id]).correct);
}

function renderTestResults() {
  const { summary } = activeTest;
  const { flashcard, exam } = summary.buckets;
  const passed = summary.percent >= TEST_PASS_PERCENT;
  const facts = [
    flashcard.count ? `${flashcard.correct} of ${plural(flashcard.count, "flashcard question")} right` : "",
    exam.count ? `${exam.earned} of ${plural(exam.total, "exam mark")}` : "",
    `${formatClock(activeTest.finishedAt - activeTest.startedAt)} taken`,
  ].filter(Boolean).join(" · ");

  const chapters = Object.entries(summary.byChapter)
    .map(([chapterId, stats]) => ({ title: activeTest.chapterTitles[chapterId] || chapterId, ...stats }))
    .sort((a, b) => a.percent - b.percent);
  const chapterRows = chapters.length > 1 ? `
    <section class="test-results-section">
      <h2>By chapter, weakest first</h2>
      <ul class="test-chapter-scores">
        ${chapters.map((ch) => `
          <li>
            <span class="test-chapter-scores-title">${escapeHtml(ch.title)}</span>
            <span class="test-chapter-scores-bar" aria-hidden="true"><span style="transform:scaleX(${ch.percent / 100})"></span></span>
            <span class="test-chapter-scores-value">${ch.percent}%</span>
          </li>`).join("")}
      </ul>
    </section>` : "";

  const missedCards = activeTest.items.filter((item) =>
    item.bucket === "flashcard" && !TestBuilder.markItem(item, activeTest.responses[item.id]).correct
  );
  const missedList = missedCards.length ? `
    <section class="test-results-section">
      <h2>Flashcards to go back over</h2>
      <ul class="test-missed">
        ${missedCards.map((item) => `<li><strong>${escapeHtml(item.term)}</strong><span>${escapeHtml(item.definition)}</span></li>`).join("")}
      </ul>
    </section>` : "";

  const missed = missedTestItems();
  const learnedNote = activeTest.newlyLearned
    ? `<p class="test-results-note">${plural(activeTest.newlyLearned, "flashcard")} newly marked as learned.</p>`
    : "";

  return `
    <div class="test-results">
      ${renderTestBar(`<button type="button" class="button-secondary" data-test-action="close">Back to studying</button>`)}
      <main class="test-sheet">
        <header class="test-results-head">
          <p class="test-results-score${passed ? " is-pass" : ""}">${summary.percent}%</p>
          <div>
            <h1>${passed ? "Passed." : summary.percent >= 40 ? "Getting there." : "Keep at it."}</h1>
            <p>${facts}</p>
            ${learnedNote}
          </div>
        </header>
        <div class="test-results-actions">
          ${missed.length ? `<button type="button" class="button-primary" data-test-action="retest">${missed.length === 1 ? "Retest the one I missed" : `Retest the ${missed.length} I missed`}</button>` : ""}
          <button type="button" class="${missed.length ? "button-secondary" : "button-primary"}" data-test-action="again">New test</button>
        </div>
        ${chapterRows}
        ${missedList}
      </main>
    </div>`;
}

// ── Test screen events ──

function setTestResponse(item, patch) {
  activeTest.responses[item.id] = { ...(activeTest.responses[item.id] || {}), ...patch };
}

function rerenderReviewKeepingScroll() {
  const scroll = els.testScreen.scrollTop;
  renderTestScreen();
  els.testScreen.scrollTop = scroll;
}

function handleTestScreenClick(event) {
  if (!activeTest) return;
  const target = event.target.closest("button");
  if (!target) return;
  const item = activeTest.items[activeTest.index];
  const reviewItem = target.closest(".test-review-item");
  const reviewed = reviewItem ? activeTest.items.find((i) => `review-${i.id}` === reviewItem.id) : null;
  const action = target.dataset.testAction;

  if (target.dataset.testChoice !== undefined && activeTest.phase === "run") {
    setTestResponse(item, { choice: Number(target.dataset.testChoice) });
    renderTestScreen();
    tickTestClock();
    els.testScreen.querySelector(".test-option.is-picked")?.focus({ preventScroll: true });
  } else if (target.dataset.testGoto !== undefined) {
    goToTestQuestion(Number(target.dataset.testGoto));
  } else if (target.dataset.testDiagram) {
    openDiagramModal(target.dataset.testDiagram);
  } else if (target.dataset.testSelfmark !== undefined && reviewed) {
    setTestResponse(reviewed, { selfMarks: Number(target.dataset.testSelfmark) });
    rerenderReviewKeepingScroll();
  } else if (target.dataset.testOverride !== undefined && reviewed) {
    const overrides = [...(activeTest.responses[reviewed.id]?.overrides || [])];
    overrides[Number(target.dataset.testOverride)] = true;
    setTestResponse(reviewed, { overrides });
    rerenderReviewKeepingScroll();
  } else if (action === "prev") {
    goToTestQuestion(activeTest.index - 1);
  } else if (action === "next") {
    goToTestQuestion(activeTest.index + 1);
  } else if (action === "finish") {
    finishTest(false);
  } else if (action === "quit") {
    activeTest.confirmQuit = true;
    renderTestScreen();
    tickTestClock();
  } else if (action === "quit-cancel") {
    activeTest.confirmQuit = false;
    renderTestScreen();
    tickTestClock();
  } else if (action === "quit-confirm" || action === "close") {
    closeTestScreen();
  } else if (action === "save") {
    saveTestResult();
  } else if (action === "retest") {
    const missed = missedTestItems().map((i) => ({ ...i, continuation: false }));
    startTest(missed);
  } else if (action === "again") {
    closeTestScreen();
    startTest();
  }
}

function handleTestScreenInput(event) {
  if (!activeTest) return;
  const target = event.target;
  if (activeTest.phase === "run") {
    const item = activeTest.items[activeTest.index];
    if (target.matches("[data-test-text]")) {
      setTestResponse(item, { text: target.value });
    } else if (target.matches("[data-test-blank]")) {
      const blanks = [...(activeTest.responses[item.id]?.blanks || [])];
      blanks[Number(target.dataset.testBlank)] = target.value;
      setTestResponse(item, { blanks });
    } else {
      return;
    }
    // Keep the question map honest without re-rendering the field being typed in.
    const dot = els.testScreen.querySelector(`[data-test-goto="${activeTest.index}"]`);
    dot?.classList.toggle("is-answered", isItemAnswered(item));
  } else if (activeTest.phase === "review" && target.matches("[data-test-selfmark-range]")) {
    const reviewItem = target.closest(".test-review-item");
    const reviewed = activeTest.items.find((i) => `review-${i.id}` === reviewItem?.id);
    if (!reviewed) return;
    setTestResponse(reviewed, { selfMarks: Number(target.value) });
    const output = target.parentElement.querySelector("output");
    if (output) output.textContent = `${target.value} / ${reviewed.marks}`;
    // Update the score without a full re-render, which would drop the slider mid-drag.
    const summary = TestBuilder.scoreTest(activeTest, activeTest.responses);
    const live = els.testScreen.querySelector(".test-live-score");
    if (live) live.textContent = `${summary.percent}% so far`;
    const verdict = reviewItem.querySelector(".test-verdict");
    if (verdict) {
      verdict.className = `test-verdict${Number(target.value) === reviewed.marks ? " is-right" : Number(target.value) ? " is-part" : " is-wrong"}`;
      verdict.textContent = `${target.value}/${plural(reviewed.marks, "mark")}`;
    }
    const pending = summary.pendingSelfMarks;
    els.testScreen.querySelectorAll('[data-test-action="save"]').forEach((button) => {
      button.textContent = pending ? `Save result (${plural(pending, "answer")} unmarked)` : "Save result";
    });
  }
}

function handleTestKeyboard(event) {
  if (!activeTest || activeTest.phase !== "run" || els.testScreen.classList.contains("hidden")) return;
  if (document.getElementById("diagramModal")?.classList.contains("open")) return;
  const item = activeTest.items[activeTest.index];
  const typing = event.target.matches?.("textarea, input");
  if (event.key === "Enter" && !event.shiftKey && (!typing || event.target.matches("[data-test-blank]"))) {
    event.preventDefault();
    if (activeTest.index < activeTest.items.length - 1) goToTestQuestion(activeTest.index + 1);
    else finishTest(false);
    return;
  }
  if (typing || event.metaKey || event.ctrlKey || event.altKey) return;
  if (event.key === "ArrowRight") goToTestQuestion(activeTest.index + 1);
  else if (event.key === "ArrowLeft") goToTestQuestion(activeTest.index - 1);
  else if (TEST_CHOICE_KINDS.has(item.kind)) {
    const key = event.key.toLowerCase();
    const index = /^[1-6]$/.test(key) ? Number(key) - 1 : "abcdef".indexOf(key);
    if (index >= 0 && index < item.options.length) {
      setTestResponse(item, { choice: index });
      renderTestScreen();
      tickTestClock();
    }
  }
}

function cardsForOutcome(outcome, subjectId) {
  return (outcome.keyTerms || []).map((kt, idx) => ({
    id: `${outcome.id}-k-${idx + 1}`,
    term: kt.term,
    definition: compactText(kt.definition),
    keywords: extractKeywords(kt),
  }));
}

function getExamQuestionsForChapter(chapter) {
  const source = getOriginalChapter(chapter.id);
  const cached = source?.examQuestions || [];
  if (cached.length) return cached;
  // Fall back to live DB for chapters loaded via additive scripts after the initial push loop.
  return (window.EXAM_QUESTIONS_DB || []).filter(q => q.chapterId === chapter.id);
}

function compactExamSource(group) {
  const source = String(group?.source || group?.id || "");
  const year = String(group?.year || source.match(/\b20\d{2}\b/)?.[0] || group?.id?.match(/-((?:19|20)\d{2})-/)?.[1] || "");
  const paper = source.match(/\bPaper\s*([12])\b/i)?.[1] || source.match(/\bP([12])\b/i)?.[1] || "";
  const namedSection = source.match(/\bSection\s*([A-C]|\d+)\b/i)?.[1] || "";
  const letterSection = source.match(/[—–-]\s*([A-C])\s*[—–-]/i)?.[1] || "";
  const question = source.match(/\bQ(?:uestion)?\s*(\d+[A-Za-z]?)\b/i)?.[1] || group?.id?.match(/-q(\d+[a-z]?)/i)?.[1] || "";
  const section = namedSection
    ? (/^\d+$/.test(namedSection) ? `S${namedSection}` : namedSection.toUpperCase())
    : letterSection.toUpperCase();
  const pieces = [year, paper ? `P${paper}` : section, question ? `Q${question}` : ""].filter(Boolean);
  return pieces.length >= 2 ? pieces.join(" ") : compactText(source).slice(0, 32);
}

function getExamDisclaimer(subject) {
  const guidance = {
    business: {
      tone: "warning",
      status: "Use with care",
      body: "The Business course has changed significantly. Past papers may not reflect current course requirements, so use them for content practice rather than as a complete exam guide.",
    },
    biology: {
      tone: "info",
      status: "Mostly reliable",
      body: "The Biology course has minor differences from previous years. The core content is largely unchanged, so past papers remain useful.",
    },
    chemistry: {
      tone: "warning",
      status: "Old course",
      body: "Chemistry moved to a new specification in September 2025 and is first examined in 2027. These papers are from the previous syllabus: questions on topics not in the new specification have been removed, and the rest still help with content practice, but they do not show the new exam structure or Chemistry in Practice investigation.",
    },
    maths: {
      tone: "info",
      status: "Reliable",
      body: "LC Maths HL past papers are highly reliable because the course content and marking approach are consistent from year to year.",
    },
    geography: {
      tone: "info",
      status: "Check the year",
      body: "Geography was restructured in 2020. Questions marked old course may not match the current exam structure.",
    },
    pe: {
      tone: "info",
      status: "Questions only",
      body: "PE papers are available from 2020 onwards. Model answers are not yet available, so use these questions for practice and self-review.",
    },
  }[subject];

  if (!guidance) return "";
  return `<details class="exam-guidance exam-guidance--${guidance.tone}">
    <summary><span>Paper guidance</span><small>${guidance.status}</small></summary>
    <div class="exam-guidance-panel">${guidance.body}</div>
  </details>`;
}

function renderExamSection() {
  const chapter = getSelectedChapter();
  if (!chapter) return;
  const examGroups = getExamQuestionsForChapter(chapter);

  if (!examGroups.length) {
    els.examContainer.innerHTML = `
      <div class="exam-empty">
        <p class="muted">No past paper questions available for this chapter yet.</p>
      </div>`;
    return;
  }

  const disclaimer = getExamDisclaimer(selectedSubjectId);

  els.examContainer.innerHTML = disclaimer + examGroups.map((group) => {
    const parts = (group.parts || []).map((part, pIdx) => {
      const partId = `${group.id}-p${pIdx}`;
      const diagramBtn = part.diagram
        ? `<button class="button-secondary exam-diagram-btn" onclick="openDiagramModal('${escapeHtml(part.diagram)}')">Show Diagram</button>`
        : "";
      const partMins = getRecommendedMinutes(group.subject, part.marks);
      const timingStr = partMins ? ` · ~${partMins} min` : "";
      return `
        <div class="exam-part">
          <div class="exam-part-header">
            <span class="exam-part-label">${escapeHtml(part.label)}</span>
            <span class="exam-marks muted small">${part.marks} mark${part.marks === 1 ? "" : "s"}${timingStr}</span>
            ${diagramBtn}
          </div>
          <p class="exam-question-text">${escapeHtml(part.question)}</p>
          ${renderExamAnswer(group, part, partId)}
        </div>`;
    }).join("");

    const contextBox = group.caseStudy && group.context
      ? `<div class="exam-case-study-context">
          <div class="exam-case-study-context-label">Case Study — Read carefully before answering</div>
          <div class="exam-case-study-context-body">${escapeHtml(group.context).replace(/\n/g, "<br>")}</div>
        </div>`
      : "";

    const appliesToBlock = group.appliesTo && group.appliesTo.length
      ? `<div class="applies-to-block">
          <p class="muted small"><strong>This content also applies to:</strong></p>
          <div class="applies-to-chips">${group.appliesTo.map((a) => `<span class="applies-to-chip">${escapeHtml(a.questionTitle)}</span>`).join("")}</div>
        </div>`
      : "";

    const _sq = getSectionForQuestion(group.id);
    const totalQMarks = (group.parts || []).reduce(function(s, p) { return s + (p.marks || 0); }, 0);
    const totalQMins = getRecommendedMinutes(group.subject, totalQMarks);
    const meta = [
      totalQMarks ? `${totalQMarks} marks` : "",
      totalQMins ? `${totalQMins} min` : "",
      group.parts?.length > 1 ? `${group.parts.length} parts` : "",
    ].filter(Boolean).join(" · ");
    const fullSource = [group.source, _sq?.section?.name].filter(Boolean).join(" · ");
    const bodyId = `exam-body-${group.id}`;
    return `
      <div class="exam-group${group.caseStudy ? " exam-group--case-study" : ""}">
        <button class="exam-group-header" type="button" data-exam-toggle aria-expanded="false" aria-controls="${escapeHtml(bodyId)}" title="${escapeHtml(fullSource)}">
          <span class="exam-source-tag">${escapeHtml(compactExamSource(group))}</span>
          <span class="exam-group-meta">${escapeHtml(meta)}</span>
          <span class="exam-group-chevron" aria-hidden="true">⌄</span>
        </button>
        <div class="exam-group-body hidden" id="${escapeHtml(bodyId)}">
          ${contextBox}
          ${parts}
          ${appliesToBlock}
        </div>
      </div>`;
  }).join("");

  bindExamAccordions(els.examContainer);

  if (typeof renderMathInElement !== "undefined") {
    renderMathInElement(els.examContainer, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
      ],
      throwOnError: false,
    });
  }
}

function bindExamAccordions(container) {
  if (!container) return;
  container.querySelectorAll("[data-exam-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const body = document.getElementById(button.getAttribute("aria-controls"));
      if (!body) return;
      const opening = button.getAttribute("aria-expanded") !== "true";

      container.querySelectorAll("[data-exam-toggle][aria-expanded='true']").forEach((openButton) => {
        if (openButton === button) return;
        openButton.setAttribute("aria-expanded", "false");
        const openBody = document.getElementById(openButton.getAttribute("aria-controls"));
        openBody?.classList.add("hidden");
      });

      button.setAttribute("aria-expanded", String(opening));
      body.classList.toggle("hidden", !opening);
    });
  });
}

function renderExamAnswer(group, part, partId) {
  if (!part.model && !part.workedSolution) return "";

  const isMaths = group.subject === "maths";
  const answerLabel = isMaths ? "Worked solution" : "Model Answer";
  const answerHtml = isMaths
    ? renderMathsWorkedSolution(part, partId)
    : `<div class="exam-answer-text">${formatModelAnswer(part.model)}</div>`;
  const showLabel = isMaths ? "Explore worked solution" : "Show Model Answer";
  const hideLabel = isMaths ? "Hide worked solution" : "Hide Model Answer";

  return `
    <div class="exam-answer-wrap${isMaths ? " exam-answer-wrap--maths" : ""} hidden" id="ans-${escapeHtml(partId)}">
      <p class="exam-answer-label">${answerLabel}</p>
      ${answerHtml}
    </div>
    <button class="button-secondary exam-toggle-btn"
      data-show-label="${showLabel}"
      data-hide-label="${hideLabel}"
      onclick="toggleExamAnswer('${escapeHtml(partId)}', this)">${showLabel}</button>`;
}

function parseMathsWorkedSolution(rawText) {
  const raw = String(rawText || "").replace(/\r/g, "").trim();
  if (!raw) return { steps: [], finalAnswer: "" };

  const finalMarker = raw.match(/(?:^|\n{2,})Final Answer:\s*/i);
  const workText = finalMarker ? raw.slice(0, finalMarker.index).trim() : raw;
  let finalAnswer = finalMarker
    ? raw.slice(finalMarker.index + finalMarker[0].length).trim()
    : "";
  const stepPattern = /(?:^|\n{2,})Step\s+(\d+)\s*[—–-]\s*/g;
  const markers = Array.from(workText.matchAll(stepPattern));

  if (!markers.length) {
    return {
      steps: [{
        number: 1,
        title: "Work through the solution",
        work: workText,
      }],
      finalAnswer,
    };
  }

  const steps = markers.map((marker, index) => {
    const start = marker.index + marker[0].length;
    const end = markers[index + 1]?.index ?? workText.length;
    const content = workText.slice(start, end).trim();
    const titleMatch = content.match(/^([^\n:]{2,90}):\s*([\s\S]*)$/);
    return {
      number: Number(marker[1]) || index + 1,
      title: titleMatch ? titleMatch[1].trim() : `Step ${marker[1]}`,
      work: titleMatch ? titleMatch[2].trim() : content,
    };
  });

  if (!finalAnswer && steps.length) {
    const closingLines = steps.at(-1).work
      .split(/\n+/)
      .map((line) => line.trim())
      .filter(Boolean);
    finalAnswer = closingLines.at(-1) || steps.at(-1).work;
  }

  return { steps, finalAnswer };
}

function mathsGuideForStep(step) {
  const text = `${step.title || ""} ${step.work || ""}`.toLowerCase();
  const guides = [
    {
      test: /factor theorem/,
      rule: "Factor Theorem",
      why: "If (x − a) is a factor of a polynomial, substituting x = a must give zero. This turns a statement about a factor into a value you can calculate.",
      pitfall: "Use the value that makes the factor zero. For (x + 3), substitute x = −3, not 3.",
    },
    {
      test: /remainder theorem/,
      rule: "Remainder Theorem",
      why: "When a polynomial is divided by (x − a), its remainder is the single value f(a). Substitution avoids carrying out the full division.",
      pitfall: "Check the sign inside the divisor before choosing the value of a.",
    },
    {
      test: /bring down/,
      rule: "Algebraic long division",
      why: "After subtracting the previous product, copy the next unused term into the working. This creates the new expression whose leading terms determine the next quotient term.",
      pitfall: "Bring down the sign with the term; dropping a minus sign changes every later line.",
    },
    {
      test: /long division|divide|division|÷|quotient/,
      rule: "Algebraic division",
      why: "Work from the highest power down. Dividing the leading terms tells you the next quotient term; multiplying back and subtracting removes that power.",
      pitfall: "Keep every power of x aligned, including a zero placeholder for any missing power.",
    },
    {
      test: /quadratic formula/,
      rule: "Quadratic formula",
      why: "For ax² + bx + c = 0, the formula gives every real or complex root directly from the three coefficients.",
      pitfall: "Include the sign of b when identifying it, then use −b in the numerator.",
    },
    {
      test: /factoris|full factor/,
      rule: "Factorisation",
      why: "Factorisation rewrites a sum as a product. Once the product equals zero, the zero-product rule lets you solve each factor separately.",
      pitfall: "Multiply the factors back out briefly to check the middle term and signs.",
    },
    {
      test: /differentiat|derivative|f[′']/,
      rule: "Differentiation",
      why: "Differentiation measures instantaneous rate of change. Apply the relevant derivative rule term by term before substituting any requested value.",
      pitfall: "Reduce the power by one after multiplying by the original power.",
    },
    {
      test: /integrat|antiderivative|area under/,
      rule: "Integration",
      why: "Integration reverses differentiation and accumulates change. For a definite integral, evaluate the antiderivative at both limits and subtract.",
      pitfall: "Increase the power before dividing by the new power, and include + C for an indefinite integral.",
    },
    {
      test: /substitut|replace|put .* into/,
      rule: "Substitution",
      why: "A known value is being inserted into the formula so the remaining unknowns or numerical result can be found.",
      pitfall: "Put negative substituted values in brackets before applying powers.",
    },
    {
      test: /expand|multiply.*bracket/,
      rule: "Distributive law",
      why: "Every term outside a bracket must multiply every term inside it. This preserves equality while removing the brackets.",
      pitfall: "A negative sign outside a bracket changes the sign of every term inside.",
    },
    {
      test: /collect|simplif|common denominator/,
      rule: "Equivalent expressions",
      why: "The expression is being rewritten in an equivalent form by combining like terms or using a common denominator. Its value does not change.",
      pitfall: "Only like terms can be combined; their variable parts and powers must match exactly.",
    },
    {
      test: /complete.*square/,
      rule: "Completing the square",
      why: "Adding and subtracting the same quantity creates a perfect-square expression without changing the original quadratic.",
      pitfall: "When the coefficient of x² is not 1, factor it out before halving the x coefficient.",
    },
    {
      test: /gradient|slope/,
      rule: "Gradient",
      why: "Gradient compares vertical change with horizontal change: rise divided by run. It describes both direction and steepness.",
      pitfall: "Subtract the coordinates in the same order on the top and bottom.",
    },
    {
      test: /midpoint/,
      rule: "Midpoint formula",
      why: "The midpoint lies halfway between the endpoints, so its x- and y-coordinates are the averages of the corresponding endpoint coordinates.",
      pitfall: "Average x-values together and y-values together; do not cross-pair them.",
    },
    {
      test: /distance/,
      rule: "Distance formula",
      why: "The horizontal and vertical changes form a right triangle, so Pythagoras gives the straight-line distance.",
      pitfall: "Square each coordinate difference before adding, then take the square root at the end.",
    },
    {
      test: /probab|binomial distribution/,
      rule: "Probability model",
      why: "The calculation counts the required outcomes and weights them by their probabilities. The chosen formula depends on whether order and repetition matter.",
      pitfall: "Check whether the question asks for exactly, at least, or at most; those events contain different outcomes.",
    },
    {
      test: /sin|cos|tan|trigon|angle/,
      rule: "Trigonometric relationship",
      why: "The selected trigonometric relationship connects the known sides or angles to the unknown one while preserving the geometry of the triangle.",
      pitfall: "Confirm the calculator is in the required angle mode and label opposite, adjacent and hypotenuse from the chosen angle.",
    },
    {
      test: /log|exponential/,
      rule: "Logarithm laws",
      why: "Logarithms convert powers into multipliers, making exponential equations easier to rearrange and solve.",
      pitfall: "A logarithm is defined only for a positive argument, so check the final solution in the original equation.",
    },
    {
      test: /induction/,
      rule: "Mathematical induction",
      why: "The base case starts the chain, and the inductive step proves that whenever one case is true the next case must also be true.",
      pitfall: "In the inductive step, clearly state where the assumption for n = k is used.",
    },
    {
      test: /solve|set .*zero|each factor/,
      rule: "Solving an equation",
      why: "The same valid operation is applied while preserving equality, reducing the equation until the unknown is isolated or each factor can be set to zero.",
      pitfall: "Check candidate answers in the original equation, especially after squaring or clearing denominators.",
    },
  ];

  return guides.find((guide) => guide.test.test(text)) || {
    rule: "Equivalent mathematical step",
    why: "This line follows from the previous one using an operation that keeps the mathematical statement equivalent. Compare the terms that changed and identify the operation applied to them.",
    pitfall: "Change only the terms affected by the operation, and check that the next line can be reversed to recover the previous line.",
  };
}

function normaliseMathsSolution(part) {
  const parsed = part.workedSolution?.steps?.length
    ? {
        steps: part.workedSolution.steps.map((step, index) => ({
          number: step.number || index + 1,
          title: step.title || `Step ${index + 1}`,
          work: step.work || step.expression || step.explanation || "",
          reasoning: step.reasoning || step.explanation || "",
          rule: step.rule || "",
          pitfall: step.commonMistake || step.pitfall || "",
        })),
        finalAnswer: part.workedSolution.finalAnswer || "",
      }
    : parseMathsWorkedSolution(part.model);

  parsed.steps = parsed.steps.map((step) => {
    const guide = mathsGuideForStep(step);
    return {
      ...step,
      reasoning: step.reasoning || guide.why,
      rule: step.rule || guide.rule,
      pitfall: step.pitfall || guide.pitfall,
    };
  });
  return parsed;
}

function formatMathsText(text) {
  return String(text || "")
    .split(/\n+/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => `<p>${escapeHtml(line)}</p>`)
    .join("");
}

function renderMathsWorkedSolution(part, solutionKey) {
  const solution = normaliseMathsSolution(part);
  mathsSolutionStore.set(solutionKey, solution);
  const countLabel = `${solution.steps.length} ${solution.steps.length === 1 ? "move" : "moves"}`;
  const stepsHtml = solution.steps.map((step, index) => `
    <article class="maths-step" tabindex="0" role="button" aria-pressed="false"
      data-solution-key="${escapeHtml(solutionKey)}" data-step-index="${index}">
      <div class="maths-step-rail" aria-hidden="true">
        <span>${String(step.number).padStart(2, "0")}</span>
        <i></i>
      </div>
      <div class="maths-step-content">
        <div class="maths-step-heading">
          <h5>${escapeHtml(step.title)}</h5>
          <span class="maths-step-explain">Explain</span>
        </div>
        <div class="maths-step-work">${formatMathsText(step.work)}</div>
      </div>
    </article>`).join("");
  const finalHtml = solution.finalAnswer
    ? `<div class="maths-final-answer">
        <span>Final answer</span>
        <div>${formatMathsText(solution.finalAnswer)}</div>
      </div>`
    : "";

  return `
    <div class="maths-worked-solution" data-solution-key="${escapeHtml(solutionKey)}">
      <div class="maths-solution-toolbar">
        <div>
          <span class="maths-solution-kicker">Line-by-line</span>
          <strong>Tap any line to see why it works</strong>
        </div>
        <span class="maths-solution-count">${countLabel}</span>
      </div>
      <div class="maths-solution-layout">
        <div class="maths-step-list" aria-label="Worked solution steps">
          ${stepsHtml}
          ${finalHtml}
          <aside class="maths-explanation-panel" aria-live="polite" hidden></aside>
        </div>
      </div>
    </div>`;
}

function handleMathsSolutionClick(event) {
  const closeButton = event.target.closest(".maths-panel-close");
  if (closeButton) {
    closeMathsExplanation(closeButton.closest(".maths-explanation-panel"));
    return;
  }

  const stepElement = event.target.closest(".maths-step");
  if (!stepElement) return;
  const selection = window.getSelection?.();
  const selectedText = selection && !selection.isCollapsed
    ? selection.toString().trim()
    : "";
  openMathsStepExplanation(stepElement, selectedText);
}

function handleMathsSolutionSelection() {
  window.setTimeout(() => {
    const selection = window.getSelection?.();
    if (!selection || selection.isCollapsed || !selection.rangeCount) return;
    const range = selection.getRangeAt(0);
    const origin = range.commonAncestorContainer.nodeType === Node.TEXT_NODE
      ? range.commonAncestorContainer.parentElement
      : range.commonAncestorContainer;
    const stepElement = origin?.closest?.(".maths-step");
    if (!stepElement) return;
    openMathsStepExplanation(stepElement, selection.toString().trim());
  }, 0);
}

function handleMathsSolutionKeyboard(event) {
  if (event.key !== "Enter" && event.key !== " ") return;
  const stepElement = event.target.closest?.(".maths-step");
  if (!stepElement || event.target !== stepElement) return;
  event.preventDefault();
  openMathsStepExplanation(stepElement);
}

function openMathsStepExplanation(stepElement, selectedText = "") {
  const solutionElement = stepElement.closest(".maths-worked-solution");
  const panel = solutionElement?.querySelector(".maths-explanation-panel");
  const solutionKey = stepElement.dataset.solutionKey;
  const stepIndex = Number(stepElement.dataset.stepIndex);
  const step = mathsSolutionStore.get(solutionKey)?.steps?.[stepIndex];
  if (!panel || !step) return;

  solutionElement.querySelectorAll(".maths-step").forEach((candidate) => {
    const active = candidate === stepElement;
    candidate.classList.toggle("is-active", active);
    candidate.setAttribute("aria-pressed", String(active));
  });

  const quote = selectedText.replace(/\s+/g, " ").trim().slice(0, 260);
  panel.classList.remove("is-open");
  panel.innerHTML = `
    <header class="maths-panel-header">
      <div>
        <p class="maths-panel-eyebrow">Step ${escapeHtml(step.number)} explained</p>
        <h5>${escapeHtml(step.title)}</h5>
      </div>
      <button class="maths-panel-close" type="button" aria-label="Close step explanation">×</button>
    </header>
    ${quote ? `<blockquote><span>You highlighted</span>${escapeHtml(quote)}</blockquote>` : ""}
    <div class="maths-panel-grid">
      <section class="maths-panel-work-section">
        <span class="maths-panel-label">What happened</span>
        <div class="maths-panel-work">${formatMathsText(step.work)}</div>
      </section>
      <section class="maths-panel-reason">
        <span class="maths-panel-label">Why it works</span>
        <p>${escapeHtml(step.reasoning)}</p>
      </section>
      <section class="maths-panel-rule">
        <span class="maths-panel-label">Rule in use</span>
        <strong>${escapeHtml(step.rule)}</strong>
      </section>
      <section class="maths-panel-pitfall">
        <span class="maths-panel-label">Watch for</span>
        <p>${escapeHtml(step.pitfall)}</p>
      </section>
    </div>`;

  stepElement.insertAdjacentElement("afterend", panel);
  panel.hidden = false;
  void panel.offsetWidth;
  panel.classList.add("is-open");

  if (typeof renderMathInElement !== "undefined") {
    renderMathInElement(panel, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
      ],
      throwOnError: false,
    });
  }
}

function closeMathsExplanation(panel) {
  const solutionElement = panel?.closest(".maths-worked-solution");
  if (!panel || !solutionElement) return;
  solutionElement.querySelectorAll(".maths-step").forEach((step) => {
    step.classList.remove("is-active");
    step.setAttribute("aria-pressed", "false");
  });
  panel.classList.remove("is-open");
  panel.hidden = true;
  panel.innerHTML = "";
}

function toggleExamAnswer(partId, btn) {
  const wrap = document.getElementById(`ans-${partId}`);
  if (!wrap) return;
  const hidden = wrap.classList.toggle("hidden");
  if (hidden) {
    const openPanel = wrap.querySelector(".maths-explanation-panel.is-open");
    if (openPanel) closeMathsExplanation(openPanel);
  }
  btn.textContent = hidden
    ? (btn.dataset.showLabel || "Show Model Answer")
    : (btn.dataset.hideLabel || "Hide Model Answer");
}

function openDiagramModal(src) {
  let modal = document.getElementById("diagramModal");
  if (!modal) {
    modal = document.createElement("div");
    modal.id = "diagramModal";
    modal.className = "diagram-modal";
    modal.innerHTML = `
      <div class="diagram-modal-backdrop" onclick="closeDiagramModal()"></div>
      <div class="diagram-modal-box">
        <button class="diagram-modal-close" onclick="closeDiagramModal()" aria-label="Close">✕</button>
        <img class="diagram-modal-img" src="" alt="Exam diagram">
      </div>`;
    document.body.appendChild(modal);
  }
  modal.querySelector(".diagram-modal-img").src = src;
  modal.classList.add("open");
  document.body.classList.add("modal-open");
}

function closeDiagramModal() {
  const modal = document.getElementById("diagramModal");
  if (modal) {
    modal.classList.remove("open");
    document.body.classList.remove("modal-open");
  }
}

function shouldAskForExamples(kt) {
  if (!kt) return false;
  const text = `${kt.term || ""} ${kt.definition || ""}`.toLowerCase();
  if (/(e\.g\.|for example|such as|examples?\b|including|like\s)/.test(text)) return true;
  if (/\b(types|methods|forms|kinds|categories|sources|rights|groups|stakeholders|sectors|strategies|techniques|tools|channels|policies)\b/.test(text)) return true;
  return false;
}

function getKeywordStopwords() {
  if (getKeywordStopwords._cache) return getKeywordStopwords._cache;
  getKeywordStopwords._cache = new Set([
    "the","a","an","of","to","and","or","in","on","for","with","that","this","is","are","be","by","at","as","it","its","their","they","them","from","not","but","if","then","than","into","when","where","what","which","who","whom","how","why","you","your","we","our","us","my","his","her","he","she","also","such","each","any","all","more","most","may","can","will","would","should","has","have","had","do","does","did","one","two","over","under","very","much","many","some","other","another","both","etc","example","examples","eg","ie","like","while","because","so","just","new","old","high","low","good","bad","being","been","were","was","there","here","these","those","about","across","between","through","without","within","upon","onto","off","up","down","out","get","give","make","made","use","used","using","only","still","again","ever","never","often","always","sometimes",
    "explain","outline","describe","state","define","discuss","identify","list","give","provide","mention","note","show","demonstrate","illustrate","include","suggest",
    "answer","question","prompt","example","examples","point","points","item","items","matter","matters","things","thing","stuff","general","simple","simply","really","quite","rather","actually","mainly","mostly","mostly","often","usually","generally","typically",
    "business","businesses","company","companies","firm","firms","organisation","organization","industry","industries","market","markets",
    "must","need","needs","want","wants","make","makes","take","takes","keep","keeps","work","works","help","helps","mean","means","find","finds","look","looks","see","seem","feel","run","runs","done","goes","comes","sets","puts","gets",
    "each","every","both","either","neither","several","various","different","same","similar","wider","broader","further","first","second","third","next","last","prior","later","early","final","initial",
    "during","before","after","since","until","unless","whether","however","therefore","thus","hence","instead","despite","including","such","whereas","towards","onto","along","among","around","beyond","outside","inside","whilst","whilst"
  ]);
  return getKeywordStopwords._cache;
}

function extractKeywords(kt) {
  const stop = getKeywordStopwords();
  const out = [];
  const seen = new Set();
  const termTokens = compactText(kt.term || "")
    .toLowerCase()
    .split(/\s+/)
    .map((w) => w.replace(/[^a-z0-9\-]/g, ""))
    .filter(Boolean);
  const termStems = termTokens
    .filter((w) => w.length >= 4)
    .map((w) => w.slice(0, Math.min(5, w.length)));
  const isTermLike = (w) =>
    termTokens.includes(w) || termStems.some((s) => w.startsWith(s));
  const consider = (raw, minLen) => {
    const w = String(raw || "").toLowerCase().replace(/[^a-z0-9\-]/g, "");
    if (!w || w.length < minLen) return;
    if (stop.has(w) || seen.has(w) || isTermLike(w)) return;
    seen.add(w);
    out.push(w);
  };
  const definitionWords = compactText(kt.definition || "").split(/\s+/);
  definitionWords.forEach((w) => consider(w, 6));
  if (out.length < 3) definitionWords.forEach((w) => consider(w, 5));
  return out.slice(0, 4);
}

function renderKeywordRow(keywords, hits) {
  if (!keywords || !keywords.length) return "";
  const chips = keywords
    .map((kw) => {
      let cls = "keyword-chip";
      if (hits) cls += hits.includes(kw) ? " hit" : " miss";
      return `<span class="${cls}">${escapeHtml(kw)}</span>`;
    })
    .join("");
  return `<div class="keyword-row"><span class="kw-label">Key words</span>${chips}</div>`;
}

function buildPrompt(term, index, kt) {
  const cleanTerm = compactText(term);
  const type = kt && kt.type;

  // All-caps acronym: e.g. GDPR, ATP, ACE FACE, BREAKS
  const lettersOnly = cleanTerm.replace(/[^A-Za-z]/g, "");
  if (lettersOnly.length >= 2 && lettersOnly === lettersOnly.toUpperCase()) {
    return `What does ${cleanTerm} stand for?`;
  }

  // Numbered mnemonic: "3 Cs", "4 Ms", "6 Rs"
  if (/^\d+\s+[A-Z]/.test(cleanTerm)) {
    return `What do the ${cleanTerm} stand for?`;
  }

  // Named theorem / rule / law / formula / equation
  if (/\b(theorem|rule|law|formula|equation)\b/i.test(cleanTerm)) {
    return `What does the ${termForSentence(cleanTerm)} state?`;
  }

  // Person: type annotation when present; heuristic only as fallback for untyped terms
  const isPerson = type === "person" || (!type && isPersonTerm(cleanTerm));
  if (isPerson) {
    const pool = [
      () => `Who was ${cleanTerm}?`,
      () => `What role did ${cleanTerm} play?`,
      () => `Why is ${cleanTerm} historically significant?`,
    ];
    return pool[index % pool.length]();
  }

  // Named event: add definite article for unquoted variant
  // "event" type OR keyword match (policy/movement/concept: keyword match only, not type alone)
  const alreadyHasThe = /^the\s/i.test(cleanTerm);
  const hasArticle = !alreadyHasThe && (type === "event" || needsDefiniteArticle(cleanTerm));
  const article = hasArticle ? "the " : "";
  const inlineTerm = article + termForSentence(cleanTerm);
  const plural = isPluralTerm(cleanTerm);
  const pool = [
    () => plural ? `What are ${inlineTerm}?` : `What is ${inlineTerm}?`,
    () => `What is meant by "${cleanTerm}"?`,
    () => `What does "${cleanTerm}" mean?`,
    () => `How would you define "${cleanTerm}"?`,
  ];
  return pool[index % pool.length]();
}

function compactText(text) {
  return String(text || "")
    .replace(/\*\*/g, "")
    .replace(/—/g, "-")
    .replace(/\s+/g, " ")
    .replace(/\s*:\s*/g, ": ")
    .trim();
}

function getSelectedChapter() {
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  return subject?.chapters.find((c) => c.id === selectedChapterId) || null;
}

function getSelectedOutcome() {
  const ch = getSelectedChapter();
  return ch?.learningOutcomes.find((lo) => lo.id === selectedOutcomeId) || null;
}

function openFullNotes() {
  const chapter = getSelectedChapter();
  if (!chapter) return;
  const outcome = chapterHasSubsections(chapter) ? getSelectedOutcome() : null;
  const heading = outcome ? compactText(outcome.title || "") : chapter.title;
  els.fullNotesTitle.innerHTML = `
    <span class="full-notes-eyebrow">Full notes${outcome ? ` · ${escapeHtml(chapter.title)}` : ""}</span>
    <span class="full-notes-heading">${escapeHtml(heading)}</span>`;
  els.fullNotesBody.innerHTML = buildFullNotesHtml(chapter, outcome);
  els.openLiveReading.classList.remove("hidden");
  closeLiveReader();
  els.fullNotesScreen.classList.remove("hidden");
  els.fullNotesBody.scrollTop = 0;
  document.body.style.overflow = "hidden";
  pushPhoneScreen("notes");
  markNotesViewed(chapter.id);
}

function buildFullNotesHtml(chapter, outcome = null) {
  const source = getOriginalChapter(chapter.id);
  if (source && Array.isArray(source.learningOutcomes) && source.learningOutcomes.length) {
    // If chapter.id is an LO id (not the chapter's own id), show only that LO's notes.
    // Likewise when a subsection is chosen: its "-core" id maps onto the source outcome.
    const outcomeSourceId = String(outcome?.id || "").replace(/-core$/, "");
    const outcomeNotes = source.learningOutcomes
      .filter((lo) => lo.id === outcomeSourceId && ((lo.notes || []).length || (lo.keyTerms || []).length));
    const requestedOutcomes = outcomeNotes.length
      ? outcomeNotes
      : source.id === chapter.id
      ? source.learningOutcomes
      : source.learningOutcomes.filter((lo) => lo.id === chapter.id);
    // Several subjects intentionally store complete, consolidated chapter notes on
    // their first outcome while retaining the remaining curriculum outcomes as shells.
    // Empty shells are structure, not missing study material, so do not render a wall
    // of misleading "No notes for this outcome" messages after the real notes.
    const populatedOutcomes = (requestedOutcomes.length ? requestedOutcomes : source.learningOutcomes)
      .filter((lo) => (lo.notes || []).length || (lo.keyTerms || []).length);
    if (populatedOutcomes.length) return populatedOutcomes
      .map((lo) => {
        const points = (lo.notes || []).length
          ? lo.notes
          : (lo.keyTerms || []).map((point) => ({ h: point.term, b: point.definition }));
        const noteHtml = points
          .map(
            (n) => `
              <div class="note-block">
                <h5>${escapeHtml(compactText(n.h || ""))}</h5>
                ${n.b ? `<p>${escapeHtml(compactText(n.b))}</p>` : ""}
                ${Array.isArray(n.points) && n.points.length
                  ? `<ul class="note-points">${n.points
                      .map((pt) => `<li>${escapeHtml(compactText(pt))}</li>`)
                      .join("")}</ul>`
                  : ""}
              </div>`
          )
          .join("");
        return `
          <section class="lo-block">
            <h4>${escapeHtml(lo.code || "")} ${escapeHtml(lo.title || "")}</h4>
            ${noteHtml}
          </section>`;
      })
      .join("");
  }
  const allPoints = (outcome ? [outcome] : chapter.learningOutcomes).flatMap((lo) => lo.keyTerms || []);
  return `<section class="lo-block">${allPoints
    .map(
      (p) => `
        <div class="note-block">
          <h5>${escapeHtml(compactText(p.term))}</h5>
          <p>${escapeHtml(compactText(p.definition))}</p>
        </div>`
    )
    .join("")}</section>`;
}

function getOriginalChapter(chapterId) {
  const data = getExternalCourseData();
  if (!data) return null;
  const chapters = data.chapters || [];
  // Direct match (e.g. "geo1", "bio1")
  const direct = chapters.find((c) => c.id === chapterId);
  if (direct) return direct;
  // LO-based ID (e.g. "geo1-1") — return the parent chapter
  return chapters.find((c) =>
    (c.learningOutcomes || []).some((lo) => lo.id === chapterId)
  ) || null;
}

function closeFullNotes() {
  closeLiveReader();
  els.fullNotesScreen.classList.add("hidden");
  if (_fullNotesReturnToBreakdown) {
    openExamBreakdown(_fullNotesReturnToBreakdown);
    _fullNotesReturnToBreakdown = null;
  } else {
    document.body.style.overflow = "";
  }
}

/* ── Live reading ──────────────────────────────
   Lyrics-style reader for the open notes: one line is lit at a time, with
   the line before and after left visible but smaller. Words within the lit
   line fill in at the chosen words-per-minute, then the next line slides up. */

function bindLiveReader() {
  try {
    const saved = Number(localStorage.getItem(LIVE_READER_WPM_KEY));
    if (saved >= 80 && saved <= 600) liveReader.wpm = saved;
  } catch (e) {}
  els.liveReaderWpm.value = String(liveReader.wpm);
  renderLiveReaderWpm();

  els.openLiveReading.addEventListener("click", () => {
    if (els.liveReader.classList.contains("hidden")) openLiveReader();
    else closeLiveReader();
  });
  els.liveReaderPlay.addEventListener("click", toggleLiveReaderPlay);
  els.liveReaderPrev.addEventListener("click", () => goToLiveLine(liveReader.index - 1));
  els.liveReaderNext.addEventListener("click", () => goToLiveLine(liveReader.index + 1));
  els.liveReaderWpm.addEventListener("input", () => {
    liveReader.wpm = Number(els.liveReaderWpm.value);
    renderLiveReaderWpm();
    try { localStorage.setItem(LIVE_READER_WPM_KEY, String(liveReader.wpm)); } catch (e) {}
  });
  els.liveReaderTrack.addEventListener("click", (event) => {
    const line = event.target.closest(".lr-line");
    if (line) goToLiveLine(Number(line.dataset.index));
  });
  document.addEventListener("keydown", (event) => {
    if (els.liveReader.classList.contains("hidden")) return;
    if (event.target === els.liveReaderWpm && event.key.startsWith("Arrow")) return;
    if (event.key === " ") {
      event.preventDefault();
      toggleLiveReaderPlay();
    } else if (event.key === "ArrowDown" || event.key === "ArrowRight") {
      event.preventDefault();
      goToLiveLine(liveReader.index + 1);
    } else if (event.key === "ArrowUp" || event.key === "ArrowLeft") {
      event.preventDefault();
      goToLiveLine(liveReader.index - 1);
    }
  });
  window.addEventListener("resize", () => {
    if (!els.liveReader.classList.contains("hidden")) layoutLiveReader(false);
  });
}

function renderLiveReaderWpm() {
  els.liveReaderWpmLabel.textContent = `${liveReader.wpm} wpm`;
}

// Split one block of notes into reading lines, one sentence per line. A
// sentence only ends where the next word starts a new one, so "e.g. the" and
// "c. 1900" stay together; stray fragments like "1." join what follows.
function splitReadingLines(text) {
  const lines = [];
  let carry = [];
  String(text || "").split(/(?<=[.!?])\s+(?=["“'(]?[\p{Lu}\d])/u).forEach((part) => {
    const words = carry.concat(part.split(/\s+/).filter(Boolean));
    if (words.length < 3) carry = words;
    else { lines.push(words); carry = []; }
  });
  if (carry.length) {
    if (lines.length) lines[lines.length - 1].push(...carry);
    else lines.push(carry);
  }
  return lines;
}

function buildLiveReaderLines() {
  const lines = [];
  // Headings ride along as a small label on the first line of their section
  // rather than taking a line of their own. Short bullets ("Paris", "High
  // rainfall") aren't sentences either, so a run from one list shares a line.
  let label = "";
  let run = null;
  const push = (words, el) => {
    const line = { words, label, el };
    label = "";
    lines.push(line);
    return line;
  };
  els.fullNotesBody.querySelectorAll("h4, h5, p, li").forEach((el) => {
    const text = compactText(el.textContent);
    if (!text) return;
    if (el.tagName === "H4" || el.tagName === "H5") {
      label = label ? `${label} · ${text}` : text;
      run = null;
      return;
    }
    const words = text.split(/\s+/);
    if (el.tagName === "LI" && words.length < 5) {
      if (run && run.list === el.parentElement && !label) {
        run.line.words[run.line.words.length - 1] += " ·";
        run.line.words.push(...words);
      } else {
        run = { list: el.parentElement, line: push(words, el) };
      }
      return;
    }
    run = null;
    splitReadingLines(text).forEach((sentence) => push(sentence, el));
  });
  if (label) push(label.split(/\s+/), null);
  return lines;
}

function openLiveReader() {
  // Start from whatever the reader had scrolled to in the notes.
  const bodyTop = els.fullNotesBody.getBoundingClientRect().top;
  liveReader.lines = buildLiveReaderLines();
  liveReader.lines.forEach((line) => { line.text = line.words.join(" "); });
  if (!liveReader.lines.length) return;
  const firstVisible = liveReader.lines.findIndex((line) => line.el?.getBoundingClientRect().bottom > bodyTop + 8);
  liveReader.index = Math.max(0, firstVisible);
  liveReader.pos = 0;

  els.liveReaderTrack.innerHTML = liveReader.lines.map((line, idx) => `
    <p class="lr-line" data-index="${idx}">${line.label
      ? `<span class="lr-label">${escapeHtml(line.label)}</span>` : ""}<span class="lr-text"><span class="lr-read"></span><span class="lr-rest">${escapeHtml(line.text)}</span></span></p>`).join("");

  els.fullNotesBody.classList.add("hidden");
  els.liveReader.classList.remove("hidden");
  els.openLiveReading.textContent = "Back to notes";
  els.openLiveReading.classList.add("is-active");
  layoutLiveReader(false);
  playLiveReader();
}

function closeLiveReader() {
  if (!els.liveReader || els.liveReader.classList.contains("hidden")) return;
  pauseLiveReader();
  const line = liveReader.lines[liveReader.index];
  els.liveReader.classList.add("hidden");
  els.fullNotesBody.classList.remove("hidden");
  els.openLiveReading.textContent = "Live reading";
  els.openLiveReading.classList.remove("is-active");
  // Drop the reader back into the notes where they left off.
  line?.el?.scrollIntoView({ block: "center" });
}

function toggleLiveReaderPlay() {
  if (liveReader.playing) pauseLiveReader();
  else playLiveReader();
}

function playLiveReader() {
  if (liveReader.index >= liveReader.lines.length - 1
    && liveReader.pos >= liveReader.lines[liveReader.index].text.length) {
    goToLiveLine(0);
  }
  liveReader.playing = true;
  liveReader.lastTs = 0;
  els.liveReaderPlay.textContent = "Pause";
  els.liveReaderPlay.setAttribute("aria-label", "Pause");
  cancelAnimationFrame(liveReader.raf);
  liveReader.raf = requestAnimationFrame(tickLiveReader);
}

function pauseLiveReader() {
  liveReader.playing = false;
  cancelAnimationFrame(liveReader.raf);
  els.liveReaderPlay.textContent = "Play";
  els.liveReaderPlay.setAttribute("aria-label", "Play");
}

function tickLiveReader(ts) {
  if (!liveReader.playing) return;
  const dt = liveReader.lastTs ? Math.min(ts - liveReader.lastTs, 250) : 0;
  liveReader.lastTs = ts;
  liveReader.pos += dt / (60000 / (liveReader.wpm * LIVE_READER_CHARS_PER_WORD));
  const chars = liveReader.lines[liveReader.index].text.length;
  if (liveReader.pos >= chars) {
    if (liveReader.index < liveReader.lines.length - 1) {
      goToLiveLine(liveReader.index + 1);
    } else {
      liveReader.pos = chars;
      renderLiveReaderWords();
      pauseLiveReader();
      return;
    }
  }
  renderLiveReaderWords();
  liveReader.raf = requestAnimationFrame(tickLiveReader);
}

function goToLiveLine(index) {
  if (index < 0 || index >= liveReader.lines.length) return;
  liveReader.index = index;
  liveReader.pos = 0;
  layoutLiveReader(true);
  renderLiveReaderWords();
}

function setLiveLineClasses(index) {
  els.liveReaderTrack.querySelectorAll(".lr-line").forEach((el, idx) => {
    el.classList.toggle("is-current", idx === index);
    el.classList.toggle("is-past", idx === index - 1);
    el.classList.toggle("is-next", idx === index + 1);
  });
}

function liveReaderOffset(index) {
  const line = els.liveReaderTrack.children[index];
  if (!line) return 0;
  const stageHeight = els.liveReaderStage.clientHeight;
  return stageHeight / 2 - (line.offsetTop + line.offsetHeight / 2);
}

function layoutLiveReader(animate) {
  const track = els.liveReaderTrack;
  track.classList.toggle("lr-still", !animate);
  setLiveLineClasses(liveReader.index);
  track.style.transform = `translateY(${liveReaderOffset(liveReader.index)}px)`;
  if (!animate) {
    void track.offsetHeight;
    track.classList.remove("lr-still");
  }
}

function renderLiveReaderWords() {
  const lineEl = els.liveReaderTrack.children[liveReader.index];
  const line = liveReader.lines[liveReader.index];
  if (!lineEl || !line) return;
  // Both halves stay in one run of inline text, so moving the split never
  // changes where the line wraps.
  const lit = Math.min(line.text.length, Math.floor(liveReader.pos));
  const read = lineEl.querySelector(".lr-read");
  if (read.textContent.length !== lit) {
    read.textContent = line.text.slice(0, lit);
    lineEl.querySelector(".lr-rest").textContent = line.text.slice(lit);
  }
  const done = (liveReader.index + Math.min(1, liveReader.pos / line.text.length)) / liveReader.lines.length;
  els.liveReaderProgress.style.width = `${(done * 100).toFixed(2)}%`;
}

function buildProgressSubjectStats(user) {
  const progress = user?.progressByOutcome || {};
  const learned = user?.learnedByOutcome || {};
  return getEnabledSubjects().map((subject) => {
    let subEarned = 0, subTotal = 0;
    const chStats = (subject.chapters || []).map((ch) => {
      let chEarned = 0, chTotal = 0;
      (ch.learningOutcomes || []).forEach((lo) => {
        const concepts = (lo.keyTerms || []).length;
        chTotal += concepts;
        if ((progress[lo.id] || 0) >= 1) {
          chEarned += concepts;
        } else {
          chEarned += (learned[lo.id] || []).length;
        }
      });
      subEarned += chEarned;
      subTotal += chTotal;
      return { ch, earned: chEarned, total: chTotal, ratio: chTotal ? chEarned / chTotal : 0 };
    });
    const pct = subTotal ? Math.round((subEarned / subTotal) * 100) : 0;
    return { subject, earned: subEarned, total: subTotal, pct, chStats };
  });
}

function renderProgressOverview() {
  const user = getCurrentUser();
  const { earned, total, percent } = computeUserProgress(user);
  const testsCompleted = user?.testsCompleted || 0;
  const subjectStats = buildProgressSubjectStats(user);

  const subjectRows = subjectStats.map((ss) => {
    const started = ss.chStats.filter((c) => c.earned > 0).length;
    const complete = ss.chStats.filter((c) => c.ratio === 1).length;
    const chapters = ss.chStats.map((s) => {
      const pct = Math.round(s.ratio * 100);
      const num = (s.ch.title.match(/^(\d+)/) || [, ""])[1];
      const state = s.ratio === 1 ? "done" : s.earned > 0 ? "part" : "none";
      return `
        <div class="progress-chapter-cell ${state}" title="${escapeHtml(s.ch.title)} — ${s.earned}/${s.total} concepts">
          <div class="progress-chapter-track"><div class="progress-chapter-fill" style="height:${pct}%"></div></div>
          <span class="progress-chapter-label">${num ? escapeHtml(num) : "·"}</span>
        </div>`;
    }).join("");

    return `
      <article class="progress-subject-row">
        <div class="progress-subject-head">
          <div class="progress-subject-id">
            <h2 class="progress-subject-title">${escapeHtml(ss.subject.title)}</h2>
            <p class="progress-subject-sub">${started} of ${ss.chStats.length} chapters started &middot; ${complete} finished &middot; ${ss.earned}/${ss.total} concepts</p>
          </div>
          <div class="progress-subject-pct">${ss.pct}<span>%</span></div>
        </div>
        <div class="progress-subject-bar-wrap">
          <div class="progress-subject-bar-fill" style="width:${ss.pct}%"></div>
        </div>
        <div class="progress-chapter-strip">${chapters}</div>
        <button class="progress-subject-btn" onclick="renderProgressSubjectDetail('${escapeHtml(ss.subject.id)}')">Chapter detail ›</button>
      </article>`;
  }).join("");

  els.progressBody.innerHTML = `
    <div class="progress-summary">
      <div class="progress-percent">${percent}<span>%</span></div>
      <div class="progress-summary-meta">
        <strong>${earned} of ${total} concept points earned</strong>
        <span class="muted small">${testsCompleted} test${testsCompleted === 1 ? "" : "s"} passed across ${subjectStats.length} subject${subjectStats.length === 1 ? "" : "s"}</span>
      </div>
    </div>
    <div class="progress-subject-list">${subjectRows}</div>
  `;
}

function renderProgressSubjectDetail(subjectId) {
  const user = getCurrentUser();
  const subjectStats = buildProgressSubjectStats(user);
  const ss = subjectStats.find((s) => s.subject.id === subjectId);
  if (!ss) return;

  const bars = ss.chStats.map((s) => {
    const pct = Math.round(s.ratio * 100);
    const num = (s.ch.title.match(/^(\d+)/) || [, "?"])[1];
    return `
      <div class="progress-bar-item" title="${escapeHtml(s.ch.title)} — ${s.earned}/${s.total}">
        <div class="progress-bar-fill-wrap">
          <div class="progress-bar-fill" style="height:${pct}%"></div>
        </div>
        <div class="progress-bar-label">Ch ${escapeHtml(num)}</div>
        <div class="progress-bar-value">${s.earned}/${s.total}</div>
      </div>`;
  }).join("");

  const chapterRows = ss.chStats.map((s) => {
    const pct = Math.round(s.ratio * 100);
    return `
      <div class="progress-detail-row">
        <span class="progress-detail-name">${escapeHtml(s.ch.title)}</span>
        <div class="progress-detail-track"><div class="progress-detail-fill" style="width:${pct}%"></div></div>
        <span class="progress-detail-score">${s.earned}/${s.total}</span>
      </div>`;
  }).join("");

  els.progressBody.innerHTML = `
    <div class="progress-detail-header">
      <button class="button-secondary" onclick="renderProgressOverview()">← All subjects</button>
      <h2>${escapeHtml(ss.subject.title)}</h2>
      <span class="muted small">${ss.pct}% overall &middot; ${ss.earned}/${ss.total} concepts</span>
    </div>
    <div class="progress-chart progress-chart-detail">${bars}</div>
    <div class="progress-detail-list">${chapterRows}</div>
  `;
}

function openProgress() {
  renderProgressOverview();
  els.progressScreen.classList.remove("hidden");
  document.body.style.overflow = "hidden";
  pushPhoneScreen("progress");
}

function closeProgress() {
  els.progressScreen.classList.add("hidden");
  document.body.style.overflow = "";
}

function markNotesViewed(chapterId) {
  const user = getCurrentUser();
  if (!user || !chapterId) return;
  if (!user.viewedNotesByChapter) user.viewedNotesByChapter = {};
  user.viewedNotesByChapter[chapterId] = true;
  persist();
}

function hasViewedNotesForChapter(chapterId) {
  const user = getCurrentUser();
  if (!user || !chapterId) return false;
  return Boolean(user.viewedNotesByChapter?.[chapterId]);
}

function loadState() {
  try {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      const parsed = JSON.parse(saved);
      return {
        usersByName: parsed.usersByName || {},
        session: { currentUser: parsed.session?.currentUser || "" },
      };
    }
  } catch (error) {
    console.error(error);
  }
  return { usersByName: {}, session: { currentUser: "" } };
}

function persist(options = {}) {
  localStorage.setItem(storageKey, JSON.stringify(state));
  if (options.sync !== false) scheduleRemoteStudySave();
}

function scheduleRemoteStudySave() {
  const current = getCurrentUser();
  if (!accountAuth?.configured || !activeAuthUserId || current?.authUserId !== activeAuthUserId) return;
  window.clearTimeout(authSaveTimer);
  authSaveTimer = window.setTimeout(() => {
    authSaveInFlight = accountAuth
      .saveStudyData(serializeStudyUser(getCurrentUser()))
      .catch((error) => console.error("Could not sync study progress", error))
      .finally(() => {
        authSaveInFlight = null;
      });
  }, 500);
}

async function flushRemoteStudySave() {
  window.clearTimeout(authSaveTimer);
  const current = getCurrentUser();
  if (accountAuth?.configured && activeAuthUserId && current?.authUserId === activeAuthUserId) {
    authSaveInFlight = accountAuth.saveStudyData(serializeStudyUser(current));
  }
  if (authSaveInFlight) await authSaveInFlight;
}


function getCurrentUser() {
  const username = state.session.currentUser;
  return username ? state.usersByName[username] || null : null;
}

function getProgressByOutcome() {
  const current = getCurrentUser();
  if (!current) return {};
  if (!current.progressByOutcome) current.progressByOutcome = {};
  return current.progressByOutcome;
}

function getLearnedByOutcome() {
  const current = getCurrentUser();
  if (!current) return {};
  if (!current.learnedByOutcome) current.learnedByOutcome = {};
  return current.learnedByOutcome;
}

function formatModelAnswer(rawText) {
  if (!rawText) return '';

  // Match "Heading Text: " at the start of the string or immediately after a sentence-ending period
  const re = /([A-Z][A-Za-z0-9\s\-–—()\/&~]{1,60}?):\s+/g;
  const sections = [];
  let lastEnd = 0;
  let match;

  while ((match = re.exec(rawText)) !== null) {
    const before = rawText.slice(0, match.index);
    const isAtStart = match.index === 0;
    const afterSentence = /[.!?]\s+$/.test(before);

    if (isAtStart || afterSentence) {
      if (match.index > lastEnd) {
        const extra = rawText.slice(lastEnd, match.index).trim().replace(/\.$/, '').trim();
        if (extra && sections.length > 0) {
          sections[sections.length - 1].content += (sections[sections.length - 1].content ? ' ' : '') + extra;
        }
      }
      sections.push({ heading: match[1].trim(), content: '' });
      lastEnd = match.index + match[0].length;
    }
  }

  if (lastEnd < rawText.length) {
    const tail = rawText.slice(lastEnd).trim().replace(/\.$/, '');
    if (sections.length > 0) {
      sections[sections.length - 1].content += (sections[sections.length - 1].content ? ' ' : '') + tail;
    } else {
      sections.push({ heading: null, content: tail });
    }
  }

  if (!sections.length) return `<p class="model-srp">${escapeHtml(rawText)}</p>`;

  return sections.map(({ heading, content }) => {
    const srps = splitModelSRPs(content);
    const srpHtml = srps.map(s => `<p class="model-srp">${escapeHtml(s)}</p>`).join('');
    return heading
      ? `<h4 class="model-subheading">${escapeHtml(heading)}</h4>${srpHtml}`
      : srpHtml;
  }).join('');
}

function splitModelSRPs(text) {
  if (!text) return [];
  return text
    .split(/(?<=[a-zA-Z]{4,})\.\s+(?=[A-Z])/)
    .map(s => s.trim().replace(/\.$/, '').trim())
    .filter(s => s.length > 3);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

// ── Exam Breakdown Modal ──────────────────────────────────────

function getSectionForQuestion(questionId) {
  const q = window.EXAM_QUESTIONS_INDEX?.get(questionId);
  if (!q?.sectionId || !q?.subject) return null;
  const data = window.EXAM_BREAKDOWN?.[q.subject];
  const section = data?.sections?.find(function (s) { return s.id === q.sectionId; });
  return section ? { section, data } : null;
}

function getRecommendedMinutes(subjectId, marks) {
  if (!marks) return null;
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data?.totalMarks || !data?.totalMinutes) return null;
  const mins = Math.round((marks / data.totalMarks) * data.totalMinutes);
  return mins > 0 ? mins : null;
}

function examSectionBadge(section, data) {
  if (!section) return '';
  let mins = section.minutesPerQuestion;
  if (mins == null && data?.totalMarks && data?.totalMinutes) {
    mins = Math.round((section.marks / data.totalMarks) * data.totalMinutes);
  }
  const timeStr = mins != null ? ` · ~${mins} min` : '';
  const bg = section.color + '22';
  return `<span class="exam-section-badge" style="background:${bg};color:${section.color};border-color:${section.color}55">${escapeHtml(section.name)}${timeStr}</span>`;
}

function openExamBreakdown(subjectId) {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data) return;
  document.getElementById('examBreakdownContent').innerHTML = renderBreakdownModal(data);
  document.getElementById('examBreakdownModal').classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeExamBreakdown() {
  document.getElementById('examBreakdownModal').classList.add('hidden');
  document.body.style.overflow = '';
}

function renderBreakdownModal(data) {
  const subjectTitle = data.subject.charAt(0).toUpperCase() + data.subject.slice(1);
  if (data.notice) {
    return `
      <h2 style="font-size:1.1rem;font-weight:700;margin:0 2.5rem 0.75rem 0">${subjectTitle} — Exam Breakdown</h2>
      <div class="breakdown-tip-group" style="max-width:480px">
        <div class="breakdown-tip-label">Notice</div>
        <div class="breakdown-tip-text">${escapeHtml(data.notice)}</div>
      </div>`;
  }
  const timeStr = data.timingNote ? ` · ${data.timingNote}` : data.totalMinutes ? ` · ${Math.floor(data.totalMinutes / 60)}h ${data.totalMinutes % 60}m` : '';
  return `
    <h2 style="font-size:1.1rem;font-weight:700;margin:0 2.5rem 0 0">${subjectTitle} — Exam Breakdown</h2>
    <p style="font-size:0.82rem;color:var(--muted);margin:0.2rem 0 0">Total: ${data.totalMarks} marks${timeStr} — click a section to see tips and practice questions</p>
    <div class="breakdown-layout">
      <div>
        ${renderBreakdownPie(data.sections, data.subject)}
        <ul class="breakdown-section-list">
          ${data.sections.map((s, i) => `
            <li class="breakdown-section-item" onclick="selectBreakdownSection('${data.subject}', ${i})" data-idx="${i}">
              <span class="breakdown-dot" style="background:${s.color}"></span>
              <span>${s.name}</span>
              <span class="breakdown-marks">${s.marks} marks</span>
            </li>`).join('')}
        </ul>
      </div>
      <div id="breakdownDetail" class="breakdown-detail">
        <p class="breakdown-detail-empty">Select a section to see tips and practice questions.</p>
      </div>
    </div>`;
}

function renderBreakdownPie(sections, subjectId) {
  const total = sections.reduce((s, x) => s + x.marks, 0);
  const cx = 90, cy = 90, r = 78;
  let angle = -Math.PI / 2;
  const paths = sections.map((sec, i) => {
    const sweep = (sec.marks / total) * 2 * Math.PI;
    const x1 = cx + r * Math.cos(angle);
    const y1 = cy + r * Math.sin(angle);
    angle += sweep;
    const x2 = cx + r * Math.cos(angle);
    const y2 = cy + r * Math.sin(angle);
    const large = sweep > Math.PI ? 1 : 0;
    const pct = Math.round((sec.marks / total) * 100);
    const midAngle = angle - sweep / 2;
    const lx = cx + (r * 0.6) * Math.cos(midAngle);
    const ly = cy + (r * 0.6) * Math.sin(midAngle);
    return `<path class="breakdown-wedge" d="M${cx},${cy} L${x1.toFixed(2)},${y1.toFixed(2)} A${r},${r} 0 ${large},1 ${x2.toFixed(2)},${y2.toFixed(2)} Z"
              fill="${sec.color}" data-idx="${i}"
              onclick="selectBreakdownSection('${subjectId}', ${i})"
              title="${sec.name} — ${sec.marks} marks"/>
            <text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" text-anchor="middle" dominant-baseline="middle"
              style="font-size:11px;font-weight:700;fill:#fff;pointer-events:none">${pct}%</text>`;
  }).join('');
  return `<div class="breakdown-pie-wrap"><svg viewBox="0 0 180 180">${paths}</svg></div>`;
}

function selectBreakdownSection(subjectId, idx) {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data) return;
  const section = data.sections[idx];

  document.querySelectorAll('.breakdown-section-item').forEach((el, i) => {
    el.classList.toggle('active', i === idx);
    el.style.borderColor = i === idx ? section.color : '';
  });
  document.querySelectorAll('.breakdown-wedge').forEach((el) => {
    el.classList.toggle('active', parseInt(el.dataset.idx) === idx);
  });

  const questions = (window.EXAM_QUESTIONS_DB || []).filter(q => q.sectionId === section.id);

  const tips = section.tips;
  document.getElementById('breakdownDetail').innerHTML = `
    <div class="breakdown-tip-group">
      <div class="breakdown-tip-label">Timing</div>
      <div class="breakdown-tip-text">${tips.timing}</div>
    </div>
    <div class="breakdown-tip-group">
      <div class="breakdown-tip-label">Answer Structure</div>
      <div class="breakdown-tip-text">${tips.structure}</div>
    </div>
    <div class="breakdown-tip-group">
      <div class="breakdown-tip-label">Reminders</div>
      <ul class="breakdown-reminders">
        ${tips.reminders.map(r => `<li>${escapeHtml(r)}</li>`).join('')}
      </ul>
    </div>
    ${questions.length
      ? `<button class="button-primary" style="margin-top:0.25rem;align-self:flex-start"
           onclick="openSectionQuestions('${subjectId}',${idx})">
           Exam Questions (${questions.length})
         </button>`
      : '<p class="breakdown-detail-empty">No past-paper questions indexed for this section yet.</p>'
    }`;
}

function openSectionQuestions(subjectId, sectionIdx) {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data) return;
  const section = data.sections[sectionIdx];

  const questions = (window.EXAM_QUESTIONS_DB || []).filter(q => q.sectionId === section.id);

  const questionsHtml = questions.map((group, qi) => {
    const parts = (group.parts || []).map((part, pIdx) => {
      const partId = `bq-${qi}-p${pIdx}`;
      const diagramHtml = part.diagram
        ? `<div class="exam-diagram-inline">
            <div class="exam-diagram-label">Diagram</div>
            <img src="${escapeHtml(part.diagram)}" alt="Exam diagram" />
           </div>`
        : '';
      return `
        <div class="exam-part">
          <div class="exam-part-header">
            <span class="exam-part-label">${escapeHtml(part.label || '')}</span>
            ${part.marks ? `<span class="exam-marks muted small">${part.marks} mark${part.marks === 1 ? '' : 's'}</span>` : ''}
          </div>
          <p class="exam-question-text">${escapeHtml(part.question || '')}</p>
          ${diagramHtml}
          ${renderExamAnswer(group, part, partId)}
        </div>`;
    }).join('');

    const totalMarks = (group.parts || []).reduce((sum, part) => sum + (part.marks || 0), 0);
    const bodyId = `breakdown-exam-body-${qi}`;

    return `
      <div class="exam-group">
        <button class="exam-group-header" type="button" data-exam-toggle aria-expanded="false" aria-controls="${bodyId}" title="${escapeHtml(group.source || group.id)}">
          <span class="exam-source-tag">${escapeHtml(compactExamSource(group))}</span>
          <span class="exam-group-meta">${totalMarks ? `${totalMarks} marks` : ""}${group.parts?.length > 1 ? ` · ${group.parts.length} parts` : ""}</span>
          <span class="exam-group-chevron" aria-hidden="true">⌄</span>
        </button>
        <div class="exam-group-body hidden" id="${bodyId}">${parts}</div>
      </div>`;
  }).join('');

  // Hide the breakdown modal so the full-screen questions view is unobstructed
  document.getElementById('examBreakdownModal').classList.add('hidden');
  _fullNotesReturnToBreakdown = subjectId;

  // Populate and open the full-notes screen (true full-screen overlay)
  document.getElementById('fullNotesTitle').textContent = `${section.name}: Practice questions`;
  closeLiveReader();
  els.openLiveReading.classList.add('hidden');
  document.getElementById('fullNotesBody').innerHTML = `<div class="exam-container exam-container--fullscreen">${questionsHtml}</div>`;
  bindExamAccordions(document.getElementById('fullNotesBody'));
  els.fullNotesScreen.classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(els.fullNotesScreen, {
      delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }],
      throwOnError: false,
    });
  }
}
