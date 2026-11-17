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

const BUSINESS_SUBJECT = {
  id: "business",
  title: "Business",
  chapters: initialSubjectChapters("business"),
};

const PE_SUBJECT = {
  id: "pe",
  title: "PE",
  chapters: initialSubjectChapters("pe"),
};

const BIOLOGY_SUBJECT = {
  id: "biology",
  title: "Biology",
  chapters: initialSubjectChapters("biology"),
};

const GEOGRAPHY_SUBJECT = {
  id: "geography",
  title: "Geography",
  chapters: initialSubjectChapters("geography"),
};

const MATHS_SUBJECT = {
  id: "maths",
  title: "Maths",
  chapters: initialSubjectChapters("maths"),
};

const CHEMISTRY_SUBJECT = {
  id: "chemistry",
  title: "Chemistry",
  chapters: initialSubjectChapters("chemistry"),
};

const HOME_ECONOMICS_SUBJECT = {
  id: "home-economics",
  title: "Home Economics",
  chapters: initialSubjectChapters("home-economics"),
};

const HISTORY_SUBJECT = {
  id: "history",
  title: "History",
  chapters: initialSubjectChapters("history"),
};

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

// Set on the generated /app/<subject>/ pages (scripts/build_subject_pages.ts); "" on the dashboard (app.html).
const PAGE_SUBJECT = SUBJECTS.some((s) => s.id === document.body.dataset.subject) ? document.body.dataset.subject : "";
const SECTION_TABS = { flashcards: "flashcards", tests: "test", exam: "exam" };
// Signed-out visitors (often from Google) can read these; the rest ask them to sign in.
const PUBLIC_SECTIONS = new Set(["", "guide", "aac", "notes"]);
const isPublicSection = (id) => PUBLIC_SECTIONS.has(id) || isAacSection(id);
const EXAM_VIEWS = [["chapter", "By chapter"], ["type", "By type"], ["papers", "Full papers"]];
const EXAM_TYPE_LABELS = {
  "short-answer": "Short answer",
  "long-answer": "Long answer",
  experiment: "Experiments",
  diagram: "Diagrams",
  calculation: "Calculations",
  written: "Written",
  drawn: "Drawing",
};
let subjectSection = "";
let examView = "chapter"; // papers | chapter | type
let examTypeFilter = "";
let sectionPanelKey = "";
// Declared up here because a page opened on #guide draws the paper guide during startup.
let breakdownSelection = null; // { subjectId, idx } of the section open in the paper guide

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
  closeProgress: document.getElementById("closeProgress"),
  progressScreen: document.getElementById("progressScreen"),
  progressBody: document.getElementById("progressBody"),
  profileAvatar: document.getElementById("profileAvatar"),
  profileLevel: document.getElementById("profileLevel"),
  subjectPicker: document.getElementById("subjectPicker"),
  profileMenu: document.getElementById("profileMenu"),
  profileMenuMain: document.getElementById("profileMenuMain"),
  profileMenuSubjects: document.getElementById("profileMenuSubjects"),
  profileMenuFeedback: document.getElementById("profileMenuFeedback"),
  profileMenuInbox: document.getElementById("profileMenuInbox"),
  openFeedback: document.getElementById("openFeedback"),
  openFeedbackInbox: document.getElementById("openFeedbackInbox"),
  feedbackInboxCount: document.getElementById("feedbackInboxCount"),
  feedbackForm: document.getElementById("feedbackForm"),
  feedbackMessage: document.getElementById("feedbackMessage"),
  feedbackStatus: document.getElementById("feedbackStatus"),
  feedbackSubmit: document.getElementById("feedbackSubmit"),
  feedbackInboxList: document.getElementById("feedbackInboxList"),
  openUsageStats: document.getElementById("openUsageStats"),
  usageStatsCount: document.getElementById("usageStatsCount"),
  profileMenuUsage: document.getElementById("profileMenuUsage"),
  usageSummary: document.getElementById("usageSummary"),
  usageStatsList: document.getElementById("usageStatsList"),
  feedbackReplyModal: document.getElementById("feedbackReplyModal"),
  feedbackReplyList: document.getElementById("feedbackReplyList"),
  feedbackReplyDismiss: document.getElementById("feedbackReplyDismiss"),
  openSubjectChoices: document.getElementById("openSubjectChoices"),
  openStudyPlan: document.getElementById("openStudyPlan"),
  studyPlanValue: document.getElementById("studyPlanValue"),
  closeSubjectChoices: document.getElementById("closeSubjectChoices"),
  subjectChoicesCount: document.getElementById("subjectChoicesCount"),
  accountIdentity: document.getElementById("accountIdentity"),
  signOutButton: document.getElementById("signOutButton"),
  subjectArea: document.getElementById("subjectArea"),
  accountStatus: document.getElementById("accountStatus"),
  resendConfirmation: document.getElementById("resendConfirmation"),
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
  fullNotesPrev: document.getElementById("fullNotesPrev"),
  fullNotesNext: document.getElementById("fullNotesNext"),
  hierarchyPanel: document.getElementById("hierarchyPanel"),
  testContainer: document.getElementById("testContainer"),
  testScreen: document.getElementById("testScreen"),
  tabs: Array.from(document.querySelectorAll(".tab")),
  flashcardsTab: document.getElementById("flashcardsTab"),
  testTab: document.getElementById("testTab"),
  examTab: document.getElementById("examTab"),
  examContainer: document.getElementById("examContainer"),
  subjectOverview: document.getElementById("subjectOverview"),
  dashboard: document.getElementById("dashboard"),
  sectionPanel: document.getElementById("sectionPanel"),
  subjectSectionTitle: document.getElementById("subjectSectionTitle"),
  closeAuth: document.getElementById("closeAuth"),
};

let state = loadState();
const accountAuth = window.BarebonesAuth;
let authSnapshot = null;
let activeAuthUserId = "";
let isFeedbackAdmin = false;
let feedbackInboxItems = [];
let feedbackInboxFilter = "open";
let pendingFeedbackReplyIds = [];
let usageTracker = null;
let usageStatsRows = null;
let usageStatsRange = "7";
let usageStatsRequest = 0;
let authSaveTimer = null;
let authSaveInFlight = null;
let authActivationPromise = null;
let activatingAuthUserId = "";
let _fullNotesReturnToBreakdown = null; // set when full notes opened from breakdown questions
// The subsection whose notes are open; paging through notes leaves selectedOutcomeId alone.
let notesOutcomeId = "";
// Questions whose every part tests a topic dropped from the current course stay hidden
// unless the student asks to see them. Declared up here because renderAll() runs first.
let showOffSpecExamQuestions = false;
// Crops are full paper width, which reads too large on a wide screen. Each page gets its own
// size slider; the last size picked becomes the starting size for every page shown after it.
// Declared up here because renderAll() can draw the Exam tab first.
const EXAM_PAPER_SCALE_KEY = "bare-bones-exam-paper-scale";
const EXAM_PAPER_SCALE_MIN = 40;
const PAGE_SUBJECT_DATA = SUBJECTS.find((s) => s.id === PAGE_SUBJECT) || SUBJECTS[0];
let selectedSubjectId = PAGE_SUBJECT_DATA.id;
let selectedChapterId = PAGE_SUBJECT_DATA.chapters[0]?.id || "";
let selectedOutcomeId = PAGE_SUBJECT_DATA.chapters[0]?.learningOutcomes[0]?.id || "";
let studyIndex = 0;
let showAnswer = false;
let viewMode = 'subject-overview';
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
const TEST_MINUTES = { min: 5, max: 60, step: 5 };
// Ordered from all flashcards to all exam; ids are TestBuilder.MIX_FLASHCARD_SHARE keys.
const TEST_MIXES = [
  { id: "all-flashcards", label: "All flashcards", short: "All cards" },
  { id: "flashcards", label: "Mostly flashcards", short: "Mostly cards" },
  { id: "balanced", label: "Even split", short: "Even" },
  { id: "exam", label: "Mostly exam questions", short: "Mostly exam" },
  { id: "all-exam", label: "All exam questions", short: "All exam" },
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
const openedSubjects = new Set(); // subjects whose full data the student has asked for
let activeTest = null;

if (isLocalMathsPreview) {
  const previewUsername = "maths-preview";
  state.usersByName[previewUsername] = createEmptyStudyUser(previewUsername);
  state.session.currentUser = previewUsername;
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
  const previewSubject = PAGE_SUBJECT ? PAGE_SUBJECT_DATA : SUBJECTS.find((s) => s.id === "biology") || SUBJECTS[0];
  selectedSubjectId = previewSubject.id;
  selectedChapterId = previewSubject.chapters[0]?.id || "";
  selectedOutcomeId = previewSubject.chapters[0]?.learningOutcomes[0]?.id || "";
}


function bindEvents() {
  els.subjectWorkbench?.addEventListener("pointerdown", openShownSubjectData, { capture: true });
  document.addEventListener("keydown", openShownSubjectData, { capture: true });
  renderAvatarPicker();
  els.openSubjectChoices.addEventListener("click", () => showProfilePane("subjects"));
  els.openStudyPlan.addEventListener("click", () => {
    const user = getCurrentUser();
    if (!user || !window.BarebonesOnboarding) return;
    els.profileMenu.classList.add("hidden");
    showOnboarding(user, { editing: true });
  });
  els.closeSubjectChoices.addEventListener("click", () => showProfilePane("main"));
  bindFeedback();
  bindUsageStats();
  els.closeAccountDetails.addEventListener("click", hideAuthPanel);
  els.showSignIn.addEventListener("click", () => showAuthMode("signin"));
  els.closeAuth?.addEventListener("click", () => {
    els.authPanel.classList.add("hidden");
    document.body.classList.remove("auth-open");
    setAuthBackgroundInert(false);
  });
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
  els.resendConfirmation.addEventListener("click", handleResendConfirmation);
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
  els.testContainer.addEventListener("input", handleTestSetupInput);
  els.testContainer.addEventListener("keydown", handleTestSetupKeydown);
  els.testContainer.addEventListener("pointerdown", handleTestMixPointer);
  document.addEventListener("pointerdown", (event) => {
    if (!event.target.closest?.(".test-dropdown")) closeTestDropdown(false);
  });
  els.testScreen.addEventListener("click", handleTestScreenClick);
  els.testScreen.addEventListener("pointerdown", handleTestPointerDown);
  els.testScreen.addEventListener("input", handleTestScreenInput);
  document.addEventListener("keydown", handleTestKeyboard);
  els.openFullNotes.addEventListener("click", () => openFullNotes());
  els.closeFullNotes.addEventListener("click", () => leavePhoneScreen("notes", closeFullNotes));
  bindFullNotesPager();
  bindLiveReader();
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
  els.signOutButton.addEventListener("click", async () => {
    els.profileMenu.classList.add("hidden");
    try {
      await flushRemoteStudySave();
      await usageTracker?.flush();
      await accountAuth?.signOut();
    } catch (error) {
      console.error(error);
    }
    activeAuthUserId = "";
    authSnapshot = null;
    resetFeedbackState();
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
  const panes = {
    main: els.profileMenuMain,
    subjects: els.profileMenuSubjects,
    feedback: els.profileMenuFeedback,
    inbox: els.profileMenuInbox,
    usage: els.profileMenuUsage,
  };
  const active = panes[pane] ? pane : "main";
  Object.entries(panes).forEach(([name, el]) => el.classList.toggle("hidden", name !== active));
  els.profileMenu.classList.toggle("profile-menu-wide", active === "subjects" || active === "feedback");
  els.profileMenu.classList.toggle("profile-menu-inbox", active === "inbox");
  els.profileMenu.classList.toggle("profile-menu-usage", active === "usage");
}

/* ── Feedback ──────────────────────────────────
   Students send feedback from the profile menu. An admin (public.admins in
   Supabase) sees an inbox there too, and marks items addressed with an
   optional reply. Unseen replies pop up once, the next time the student
   opens the app. Schema: supabase/feedback.sql. */
function bindFeedback() {
  els.openFeedback.addEventListener("click", () => {
    showProfilePane("feedback");
    setFeedbackStatus("");
    els.feedbackMessage.focus();
  });
  els.openFeedbackInbox.addEventListener("click", () => {
    showProfilePane("inbox");
    loadFeedbackInbox();
  });
  document.querySelectorAll("[data-profile-back]").forEach((button) => {
    button.addEventListener("click", () => showProfilePane("main"));
  });
  els.feedbackMessage.addEventListener("input", () => setFeedbackStatus(""));
  els.feedbackForm.addEventListener("submit", handleFeedbackSubmit);
  els.profileMenuInbox.querySelectorAll("[data-inbox-filter]").forEach((button) => {
    button.addEventListener("click", () => {
      feedbackInboxFilter = button.dataset.inboxFilter;
      renderFeedbackInbox();
    });
  });
  els.feedbackInboxList.addEventListener("click", handleFeedbackInboxClick);
  els.feedbackReplyDismiss.addEventListener("click", dismissFeedbackReplies);
  els.feedbackReplyModal.addEventListener("keydown", (event) => {
    if (event.key === "Escape") dismissFeedbackReplies();
  });
}

function setFeedbackStatus(message, tone = "neutral") {
  els.feedbackStatus.textContent = message;
  els.feedbackStatus.dataset.tone = tone;
}

function feedbackErrorMessage(error) {
  const message = String(error?.message || error || "");
  if (/recently|empty|4000 characters|sign in/i.test(message)) return message;
  if (/failed to fetch|network/i.test(message)) return "Couldn’t reach the server. Check your connection and try again.";
  if (/function .* does not exist|could not find the function|schema cache/i.test(message)) {
    return "Feedback isn’t switched on yet. Try again later.";
  }
  return "That didn’t send. Please try again.";
}

async function handleFeedbackSubmit(event) {
  event.preventDefault();
  const message = els.feedbackMessage.value.trim();
  if (!message) {
    setFeedbackStatus("Write something first.", "error");
    els.feedbackMessage.focus();
    return;
  }
  if (!accountAuth?.configured || !activeAuthUserId) {
    setFeedbackStatus("Sign in to send feedback.", "error");
    return;
  }
  els.feedbackSubmit.disabled = true;
  els.feedbackSubmit.textContent = "Sending…";
  try {
    await accountAuth.submitFeedback(message);
    els.feedbackMessage.value = "";
    setFeedbackStatus("Sent. Thanks for telling us.", "success");
    if (isFeedbackAdmin) refreshFeedbackAdmin();
  } catch (error) {
    console.error(error);
    setFeedbackStatus(feedbackErrorMessage(error), "error");
  } finally {
    els.feedbackSubmit.disabled = false;
    els.feedbackSubmit.textContent = "Send feedback";
  }
}

async function refreshFeedbackAdmin() {
  isFeedbackAdmin = false;
  if (accountAuth?.configured && activeAuthUserId) {
    try {
      isFeedbackAdmin = await accountAuth.isAdmin();
    } catch (error) {
      isFeedbackAdmin = false;
    }
  }
  els.openFeedbackInbox.classList.toggle("hidden", !isFeedbackAdmin);
  els.openUsageStats.classList.toggle("hidden", !isFeedbackAdmin);
  if (!isFeedbackAdmin) {
    feedbackInboxItems = [];
    els.feedbackInboxCount.textContent = "";
    return;
  }
  await loadFeedbackInbox();
}

function resetFeedbackState() {
  isFeedbackAdmin = false;
  feedbackInboxItems = [];
  pendingFeedbackReplyIds = [];
  els.openFeedbackInbox.classList.add("hidden");
  els.feedbackInboxCount.textContent = "";
  els.openUsageStats.classList.add("hidden");
  usageStatsRows = null;
  els.feedbackMessage.value = "";
  setFeedbackStatus("");
  hideFeedbackReplies();
}

async function loadFeedbackInbox() {
  if (!isFeedbackAdmin) return;
  if (!feedbackInboxItems.length) {
    els.feedbackInboxList.innerHTML = `<p class="inbox-empty">Loading…</p>`;
  }
  try {
    feedbackInboxItems = await accountAuth.listFeedback();
  } catch (error) {
    console.error(error);
    els.feedbackInboxList.innerHTML = `<p class="inbox-empty">Couldn’t load feedback. ${escapeHtml(feedbackErrorMessage(error))}</p>`;
    return;
  }
  renderFeedbackInbox();
}

function formatFeedbackDate(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  return date.toLocaleDateString("en-IE", { day: "numeric", month: "short" }) +
    " · " + date.toLocaleTimeString("en-IE", { hour: "2-digit", minute: "2-digit" });
}

function renderFeedbackInbox() {
  const openCount = feedbackInboxItems.filter((item) => item.status === "open").length;
  els.feedbackInboxCount.textContent = openCount ? `${openCount} open` : "";
  els.profileMenuInbox.querySelectorAll("[data-inbox-filter]").forEach((button) => {
    const active = button.dataset.inboxFilter === feedbackInboxFilter;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
    if (button.dataset.inboxFilter === "open") button.textContent = openCount ? `Open (${openCount})` : "Open";
  });

  const items = feedbackInboxItems.filter((item) => item.status === feedbackInboxFilter);
  if (!items.length) {
    els.feedbackInboxList.innerHTML = `<p class="inbox-empty">${
      feedbackInboxFilter === "open" ? "Nothing open. You’re all caught up." : "Nothing addressed yet."
    }</p>`;
    return;
  }

  els.feedbackInboxList.innerHTML = items.map((item) => {
    const meta = `
      <div class="inbox-item-meta">
        <strong>${escapeHtml(item.username)}</strong>
        <span>${escapeHtml(formatFeedbackDate(item.created_at))}</span>
      </div>
      <p class="inbox-item-message">${escapeHtml(item.message)}</p>`;
    if (item.status === "open") {
      return `
        <article class="inbox-item" data-feedback-id="${escapeHtml(item.id)}">
          ${meta}
          <label class="inbox-reply-label" for="reply-${escapeHtml(item.id)}">Reply (optional, shown to ${escapeHtml(item.username)} next login)</label>
          <textarea id="reply-${escapeHtml(item.id)}" class="feedback-textarea inbox-reply-input" rows="3" maxlength="4000" placeholder="Fixed it, thanks!"></textarea>
          <p class="feedback-status inbox-item-status" role="status" aria-live="polite"></p>
          <button class="button-primary inbox-action" type="button" data-feedback-action="address">Mark addressed</button>
        </article>`;
    }
    const replyState = !item.reply
      ? "No reply sent"
      : item.reply_seen_at
        ? `Seen ${escapeHtml(formatFeedbackDate(item.reply_seen_at))}`
        : "Not seen yet";
    return `
      <article class="inbox-item is-addressed" data-feedback-id="${escapeHtml(item.id)}">
        ${meta}
        ${item.reply ? `<p class="inbox-item-reply"><span>Your reply</span>${escapeHtml(item.reply)}</p>` : ""}
        <div class="inbox-item-foot">
          <span>${replyState}</span>
          <button class="inbox-link" type="button" data-feedback-action="reopen">Reopen</button>
        </div>
        <p class="feedback-status inbox-item-status" role="status" aria-live="polite"></p>
      </article>`;
  }).join("");
}

async function handleFeedbackInboxClick(event) {
  const button = event.target.closest("[data-feedback-action]");
  if (!button) return;
  const itemEl = button.closest("[data-feedback-id]");
  const id = itemEl?.dataset.feedbackId;
  if (!id) return;
  const statusEl = itemEl.querySelector(".inbox-item-status");
  button.disabled = true;
  try {
    if (button.dataset.feedbackAction === "address") {
      const reply = itemEl.querySelector(".inbox-reply-input")?.value || "";
      await accountAuth.addressFeedback(id, reply);
    } else {
      await accountAuth.reopenFeedback(id);
    }
    await loadFeedbackInbox();
  } catch (error) {
    console.error(error);
    button.disabled = false;
    if (statusEl) {
      statusEl.textContent = feedbackErrorMessage(error);
      statusEl.dataset.tone = "error";
    }
  }
}

async function checkFeedbackReplies({ delay = 0 } = {}) {
  if (!accountAuth?.configured || !activeAuthUserId) return;
  let replies = [];
  try {
    replies = await accountAuth.getUnseenFeedbackReplies();
  } catch (error) {
    // Before supabase/feedback.sql is applied the table is missing; stay quiet.
    return;
  }
  if (!replies.length) return;
  const userId = activeAuthUserId;
  window.setTimeout(() => {
    if (activeAuthUserId !== userId) return;
    showFeedbackReplies(replies);
  }, delay);
}

function showFeedbackReplies(replies) {
  pendingFeedbackReplyIds = replies.map((item) => item.id);
  els.feedbackReplyList.innerHTML = replies.map((item) => `
    <article class="feedback-reply-item">
      <p class="feedback-reply-original"><span>You wrote${item.created_at ? ` on ${escapeHtml(formatFeedbackDate(item.created_at))}` : ""}</span>${escapeHtml(item.message)}</p>
      <p class="feedback-reply-text">${escapeHtml(item.reply)}</p>
    </article>`).join("");
  els.profileMenu.classList.add("hidden");
  els.feedbackReplyModal.classList.remove("hidden");
  document.body.classList.add("modal-open");
  els.feedbackReplyDismiss.focus();
}

function hideFeedbackReplies() {
  els.feedbackReplyModal.classList.add("hidden");
  document.body.classList.remove("modal-open");
}

async function dismissFeedbackReplies() {
  const ids = pendingFeedbackReplyIds;
  pendingFeedbackReplyIds = [];
  hideFeedbackReplies();
  try {
    await accountAuth?.markFeedbackRepliesSeen(ids);
  } catch (error) {
    // If this fails the reply simply shows again next time.
    console.error(error);
  }
}

/* ── Usage stats ───────────────────────────────
   usage-tracker.js counts active time per subject + screen and sends it to
   record_usage(). Admins see everyone's totals in Profile menu → User stats
   (admin_usage_stats()). Schema: supabase/usage.sql. */
const USAGE_SCREEN_LABELS = {
  home: "Subject list",
  learn: "Learn",
  test: "Test setup",
  "test-session": "Taking a test",
  exam: "Exam questions",
  notes: "Full notes",
  "live-reader": "Live reader",
  "exam-breakdown": "Exam breakdown",
  papers: "Exam papers",
  "paper-viewer": "Reading a paper",
  progress: "Progress",
  onboarding: "Onboarding",
};

function startUsageTracking() {
  if (!accountAuth?.configured || !window.BarebonesUsage) return;
  usageTracker = window.BarebonesUsage.startUsageTracker({
    getContext: currentUsageContext,
    send: (entries) => accountAuth.recordUsage(entries),
  });
}

// Where the student is right now, or null when nothing should be counted.
function currentUsageContext() {
  if (!activeAuthUserId || !getCurrentUser()) return null;
  const shown = (el) => Boolean(el) && !el.classList.contains("hidden");
  if (shown(els.authPanel)) return null;
  const userId = activeAuthUserId;
  const subject = selectedSubjectId || "general";
  const at = (screen, subjectId = subject) => ({ userId, subject: subjectId, screen });

  if (document.body.classList.contains("onboarding-open")) return at("onboarding", "general");
  if (shown(document.getElementById("paperViewer"))) return at("paper-viewer");
  if (shown(els.liveReader)) return at("live-reader");
  if (shown(els.fullNotesScreen)) return at("notes");
  if (shown(document.getElementById("examBreakdownModal"))) return at("exam-breakdown");
  if (shown(els.testScreen)) return at("test-session");
  if (shown(els.progressScreen)) return at("progress", "general");
  if (!PAGE_SUBJECT) return at("dashboard", "general");
  if (subjectSection === "exam" && examView === "papers") return at("papers");
  if (subjectSection === "notes") return at("notes-list");
  if (!subjectSection) return at("subject-home");
  if (els.examTab?.classList.contains("active")) return at("exam");
  if (els.testTab?.classList.contains("active")) return at("test");
  return at("learn");
}

function bindUsageStats() {
  els.openUsageStats.addEventListener("click", () => {
    showProfilePane("usage");
    loadUsageStats();
  });
  els.profileMenuUsage.querySelectorAll("[data-usage-range]").forEach((button) => {
    button.addEventListener("click", () => {
      if (usageStatsRange === button.dataset.usageRange) return;
      usageStatsRange = button.dataset.usageRange;
      usageStatsRows = null;
      loadUsageStats();
    });
  });
}

function usageSinceDay(range) {
  if (range === "all") return null;
  const since = new Date();
  since.setDate(since.getDate() - (Number(range) - 1));
  return window.BarebonesUsage.localDay(since.getTime());
}

async function loadUsageStats() {
  if (!isFeedbackAdmin) return;
  els.profileMenuUsage.querySelectorAll("[data-usage-range]").forEach((button) => {
    const active = button.dataset.usageRange === usageStatsRange;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
  });
  if (usageStatsRows) {
    renderUsageStats();
    return;
  }
  const request = ++usageStatsRequest;
  els.usageSummary.textContent = "";
  els.usageStatsList.innerHTML = `<p class="inbox-empty">Loading…</p>`;
  try {
    // Send this browser's pending time first so your own row is current.
    await usageTracker?.flush();
    const rows = await accountAuth.adminUsageStats(usageSinceDay(usageStatsRange));
    if (request !== usageStatsRequest) return;
    usageStatsRows = rows;
  } catch (error) {
    if (request !== usageStatsRequest) return;
    console.error(error);
    const missing = /admin_usage_stats|schema cache|does not exist/i.test(error?.message || "");
    els.usageStatsList.innerHTML = `<p class="inbox-empty">${
      missing
        ? "Stats aren’t switched on yet. Run supabase/usage.sql in the Supabase SQL editor."
        : `Couldn’t load stats. ${escapeHtml(error?.message || "")}`
    }</p>`;
    return;
  }
  renderUsageStats();
}

// One entry per student: { username, total, days, lastActive, subjects, screens }.
function summarizeUsage(rows) {
  const byUser = new Map();
  rows.forEach((row) => {
    let user = byUser.get(row.user_id);
    if (!user) {
      user = {
        id: row.user_id,
        username: row.username || "unknown",
        joinedAt: row.joined_at,
        total: 0,
        days: Number(row.active_days) || 0,
        lastActive: row.last_active || null,
        subjects: new Map(),
        screens: new Map(),
      };
      byUser.set(row.user_id, user);
    }
    const seconds = Number(row.seconds) || 0;
    if (!seconds || !row.subject || !row.screen) return;
    user.total += seconds;
    user.subjects.set(row.subject, (user.subjects.get(row.subject) || 0) + seconds);
    user.screens.set(row.screen, (user.screens.get(row.screen) || 0) + seconds);
  });
  return [...byUser.values()].sort((a, b) =>
    b.total - a.total || String(b.lastActive || "").localeCompare(String(a.lastActive || "")) || a.username.localeCompare(b.username)
  );
}

function formatUsageDuration(seconds) {
  const minutes = Math.floor(seconds / 60);
  if (minutes < 1) return seconds > 0 ? "<1m" : "0m";
  const hours = Math.floor(minutes / 60);
  if (!hours) return `${minutes}m`;
  return `${hours}h ${String(minutes % 60).padStart(2, "0")}m`;
}

function formatUsageLastActive(value) {
  if (!value) return "Never active";
  const diff = Date.now() - new Date(value).getTime();
  if (!Number.isFinite(diff)) return "";
  const minutes = Math.round(diff / 60000);
  if (minutes < 2) return "Active now";
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.round(minutes / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.round(hours / 24);
  if (days < 14) return `${days}d ago`;
  return formatFeedbackDate(value);
}

function usageSubjectLabel(id) {
  if (id === "general") return "General";
  return SUBJECTS.find((s) => s.id === id)?.title || id;
}

function usageScreenLabel(id) {
  return USAGE_SCREEN_LABELS[id] || id;
}

function renderUsageBreakdown(title, entries, labelFor) {
  const sorted = [...entries].sort((a, b) => b[1] - a[1]);
  const max = sorted[0]?.[1] || 1;
  return `
    <div class="usage-group">
      <p class="usage-group-title">${escapeHtml(title)}</p>
      ${sorted.map(([id, seconds]) => `
        <div class="usage-bar-row">
          <span class="usage-bar-label">${escapeHtml(labelFor(id))}</span>
          <span class="usage-bar-track" aria-hidden="true"><span class="usage-bar-fill" style="width:${Math.max(2, Math.round((seconds / max) * 100))}%"></span></span>
          <span class="usage-bar-value">${escapeHtml(formatUsageDuration(seconds))}</span>
        </div>`).join("")}
    </div>`;
}

function renderUsageStats() {
  const users = summarizeUsage(usageStatsRows || []);
  const active = users.filter((u) => u.total > 0);
  const total = active.reduce((sum, u) => sum + u.total, 0);
  els.usageStatsCount.textContent = users.length ? `${users.length}` : "";
  els.usageSummary.innerHTML = users.length
    ? `<span><strong>${users.length}</strong> ${users.length === 1 ? "student" : "students"}</span>
       <span><strong>${active.length}</strong> active</span>
       <span><strong>${escapeHtml(formatUsageDuration(total))}</strong> total</span>`
    : "";
  if (!users.length) {
    els.usageStatsList.innerHTML = `<p class="inbox-empty">No accounts yet.</p>`;
    return;
  }
  els.usageStatsList.innerHTML = users.map((user) => {
    const meta = user.total
      ? `${escapeHtml(formatUsageLastActive(user.lastActive))} · ${user.days} ${user.days === 1 ? "day" : "days"}`
      : "No time in this range";
    const head = `
      <span class="usage-user-name">${escapeHtml(user.username)}</span>
      <span class="usage-user-total">${escapeHtml(formatUsageDuration(user.total))}</span>
      <span class="usage-user-meta">${meta}</span>`;
    if (!user.total) {
      return `<div class="usage-user is-idle"><div class="usage-user-head">${head}</div></div>`;
    }
    return `
      <details class="usage-user">
        <summary class="usage-user-head">${head}</summary>
        <div class="usage-user-body">
          ${renderUsageBreakdown("By subject", user.subjects, usageSubjectLabel)}
          ${renderUsageBreakdown("By screen", user.screens, usageScreenLabel)}
        </div>
      </details>`;
  }).join("");
}

async function initializeAccounts() {
  const requestedMode = window.location.hash === "#signup" ? "signup" : "signin";

  const askedForAuth = window.location.hash === "#signin" || window.location.hash === "#signup";
  if (!accountAuth?.configured) {
    if ((!getCurrentUser() && !PAGE_SUBJECT) || askedForAuth) {
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
        // A subject page is a public preview; it only asks to sign in when a locked section is opened
        if (!PAGE_SUBJECT || askedForAuth) showAuthMode(requestedMode);
      }
    }
  } catch (error) {
    console.error(error);
    showAuthMode(requestedMode);
    setAuthStatus(friendlyAuthError(error), "error");
  } finally {
    const linkError = accountAuth.urlAuthError;
    if (linkError) {
      history.replaceState(null, "", window.location.pathname);
      if (!accountAuth.getSession()) {
        showAuthMode("signin");
        setAuthStatus(friendlyLinkError(linkError), "error");
        showResendConfirmation(true);
      }
    } else if (window.location.hash === "#signin" || window.location.hash === "#signup") {
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
    resetFeedbackState();
    state.session.currentUser = "";
    persist({ sync: false });
    renderAll();
    showAuthMode(getLegacyProfileNames().length ? "legacy" : "signin");
  }
}

async function handleSignIn(event) {
  event.preventDefault();
  if (!els.signInForm.reportValidity()) return;
  localStorage.setItem(
    pendingAuthEmailKey,
    String(els.signInEmail.value || "").trim().toLowerCase()
  );
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
      marketingOptIn: Boolean(document.getElementById("signUpMarketing")?.checked),
    });
    if (data.session) {
      await activateAuthenticatedSession(data.session);
    } else {
      setAuthStatus("Account created! Check your inbox (and spam folder) for a confirmation link, then you’ll be signed in.", "success");
      els.signUpForm.reset();
      showResendConfirmation(true);
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
        marketingOptIn: Boolean(document.getElementById("legacyMarketing")?.checked),
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
      setAuthStatus("Nearly done. Confirm the email we sent you (check spam too); your existing progress is waiting here.", "success");
      showResendConfirmation(true);
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
    if (/email not confirmed/i.test(String(error?.message || ""))) showResendConfirmation(true);
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
  showResendConfirmation(false);

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

function showResendConfirmation(show) {
  els.resendConfirmation.classList.toggle("hidden", !show);
}

let resendCooldownTimer = 0;

async function handleResendConfirmation() {
  const button = els.resendConfirmation;
  const email = String(
    localStorage.getItem(pendingAuthEmailKey) || els.signInEmail.value || ""
  ).trim().toLowerCase();
  if (!email) {
    showAuthMode("signin");
    setAuthStatus("Enter your email and password, then press Sign in. We’ll offer to resend the link from there.", "neutral");
    els.signInEmail.focus();
    return;
  }
  const label = button.textContent;
  button.disabled = true;
  button.textContent = "Sending…";
  try {
    await accountAuth.resendConfirmation(email);
    setAuthStatus(`Sent a fresh confirmation link to ${email}. It can take a minute, so check spam too.`, "success");
    // Supabase only allows one resend a minute per address; match it in the UI.
    let seconds = 60;
    button.textContent = `Send again in ${seconds}s`;
    clearInterval(resendCooldownTimer);
    resendCooldownTimer = setInterval(() => {
      seconds -= 1;
      if (seconds > 0) {
        button.textContent = `Send again in ${seconds}s`;
        return;
      }
      clearInterval(resendCooldownTimer);
      button.disabled = false;
      button.textContent = label;
    }, 1000);
  } catch (error) {
    console.error(error);
    setAuthStatus(friendlyAuthError(error), "error");
    button.disabled = false;
    button.textContent = label;
  }
}

function friendlyLinkError(linkError) {
  const text = `${linkError.code} ${linkError.message}`;
  if (/otp_expired|expired|invalid/i.test(text)) {
    return "That link has expired or was already used. If you’ve already confirmed, just sign in. Otherwise, send yourself a fresh link below.";
  }
  if (/access_denied/i.test(text)) {
    return "That link didn’t work. Sign in below, or send yourself a fresh confirmation link.";
  }
  return "That link didn’t work. Please sign in, or request a new link below.";
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
  if (/error sending|sending (confirmation|recovery|magic link)|smtp|not authorized|email_address_not_authorized/i.test(message)) {
    return "We couldn’t send your confirmation email just now. Please try again in a few minutes.";
  }
  if (/email rate limit|over_email_send_rate_limit|only request this after/i.test(message)) {
    return "We’ve just sent you an email. Give it a minute (check spam), then try again if it hasn’t arrived.";
  }
  if (/email address.*invalid|invalid.*email/i.test(message)) return "That email address doesn’t look right. Check it and try again.";
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
    loadStudyRows(session.user.id);
    authSnapshot = snapshot;
    localStorage.removeItem(pendingAuthUsernameKey);
    localStorage.removeItem(pendingAuthEmailKey);
    persist({ sync: false });
    await accountAuth.saveStudyData(serializeStudyUser(merged));
    renderAll();
    hideAuthPanel();

    refreshFeedbackAdmin();
    if (needsOnboarding(merged, snapshot)) {
      showOnboarding(merged);
    } else if (options.animate !== false) {
      triggerLoginAnimation(username);
      // Let the welcome animation (2.5s + 0.6s exit) finish first.
      checkFeedbackReplies({ delay: 3200 });
    } else {
      checkFeedbackReplies();
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

// ── On-demand assets ───────────────────────────────────────────
// KaTeX (~270 KB) and the Test kit (~190 KB) are only fetched when something on screen needs them.
const assetLoads = new Map();
function loadAsset(url, { cors = false } = {}) {
  if (!assetLoads.has(url)) {
    assetLoads.set(url, new Promise((resolve, reject) => {
      const isCss = url.split("?")[0].endsWith(".css");
      const el = document.createElement(isCss ? "link" : "script");
      if (isCss) { el.rel = "stylesheet"; el.href = url; } else { el.src = url; el.async = false; }
      if (cors) el.crossOrigin = "anonymous";
      el.onload = resolve;
      el.onerror = () => { assetLoads.delete(url); el.remove(); reject(new Error(`Could not load ${url}`)); };
      document.head.appendChild(el);
    }));
  }
  return assetLoads.get(url);
}

const KATEX_BASE = "https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/";
function loadKatex() {
  return Promise.all([
    loadAsset(`${KATEX_BASE}katex.min.css`, { cors: true }),
    loadAsset(`${KATEX_BASE}katex.min.js`, { cors: true }),
  ]).then(() => loadAsset(`${KATEX_BASE}contrib/auto-render.min.js`, { cors: true }));
}

function loadTestKit() {
  return Promise.all([
    loadAsset("./flashcard-test-prompts.js?v=2"),
    loadAsset("./answer-marker.js?v=2"),
  ]).then(() => loadAsset("./test-builder.js?v=4"));
}

// Typeset $…$ maths inside node, fetching KaTeX first only if there is any
function typesetMath(node) {
  if (!node || !node.textContent.includes("$")) return;
  loadKatex().then(() => {
    window.renderMathInElement?.(node, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
      ],
      throwOnError: false,
    });
  }, (error) => console.error(error));
}

function switchTab(tab) {
  els.tabs.forEach((btn) => btn.classList.toggle("active", btn.dataset.tab === tab));
  els.flashcardsTab.classList.toggle("active", tab === "flashcards");
  els.testTab.classList.toggle("active", tab === "test");
  els.examTab.classList.toggle("active", tab === "exam");
  els.subjectWorkbench?.classList.toggle("learn-mode", tab === "flashcards");
  if (tab === "exam") renderExamSection();
  if (tab === "test") renderTestOverview();
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

function renderAll() {
  if (openedSubjects.has(selectedSubjectId)) {
    requestSubjectPack(selectedSubjectId).catch((error) => console.error(error));
    requestExamPack(selectedSubjectId);
  }
  renderAccount();
  renderProfileAvatar();
  renderAccountIdentity();
  renderAvatarPicker();
  renderSubjectPicker();
  renderSubjectPage();
  renderSubjectOverview();
  renderOutcomePicker();
  renderStudyContext();
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
        const concepts = outcomeCardTotal(lo);
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
// Phones show one screen at a time: a section's chapter list, then a chapter's
// subsections where it has them, then study. Each step down is a history entry,
// so the back gesture steps up a level instead of leaving the page.
function isPhoneLayout() {
  return window.matchMedia("(max-width: 640px)").matches;
}

function phoneScreen() {
  if (!PAGE_SUBJECT) return "home";
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
  viewMode = "subject-overview";
  renderAll();
}

function handlePhonePopState(event) {
  if (!isPhoneLayout()) return;
  // A running test sits on top of everything; keep the screen under it and restore the entry
  if (document.body.classList.contains("test-open")) {
    history.pushState({ bbScreen: phoneScreen() }, "", location.href);
    return;
  }
  const screen = event.state?.bbScreen || "subject";
  if (screen !== "notes" && !els.fullNotesScreen.classList.contains("hidden")) closeFullNotes();
  if (screen !== "progress" && !els.progressScreen.classList.contains("hidden")) closeProgress();
  if (screen !== "paper") closePaperViewer();
  if (screen === "subject" || screen === "chapter" || screen === "study") {
    viewMode = screen === "subject" ? "subject-overview" : "chapter";
    // Stepping back onto a chapter with subsections lands on its subsection grid
    pickingOutcome = screen === "chapter" && chapterHasSubsections(getSelectedChapter());
  }
  renderAll();
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

  // The subject heading above steps back to the chapter list; the section's name moves under the chapter's
  els.studyContext.innerHTML = `
    <strong title="${escapeHtml(chapter?.title || "")}">${escapeHtml(chapter?.title || "")}</strong>
    <span class="study-context-section">${escapeHtml(SECTION_LABELS[subjectSection] || "")}</span>
  `;
}

// Inside a chapter the heading steps back one screen: subsection → subsection grid → chapter list.
// Elsewhere the link's own href (subject tiles, then your subjects) does the job.
function stepBackFromHeading(event) {
  if (els.subjectWorkbench.classList.contains("hidden") || viewMode !== "chapter" || subjectSection === "tests") return;
  event.preventDefault();
  const toGrid = els.studyContext.querySelector(".study-context-back");
  if (toGrid) toGrid.click();
  else navigateUp();
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
    const total = outcomeCardTotal(lo);
    const pct = total ? Math.round((done / total) * 100) : 0;
    return `
      <button class="outcome-card ${pct === 100 ? "is-done" : ""}" type="button" data-outcome-id="${escapeHtml(lo.id)}">
        <span class="outcome-card-index">${String(idx + 1).padStart(2, "0")}</span>
        <span class="outcome-card-title">${escapeHtml(compactText(lo.title || `Subsection ${idx + 1}`))}</span>
        <span class="outcome-card-meta">
          <span class="outcome-card-bar"><span style="width:${pct}%"></span></span>
          <span>${done}/${total}</span>
        </span>
      </button>`;
  }).join("");

  picker.innerHTML = `
    <div class="outcome-picker-grid">${cardsHtml}</div>
    <button class="outcome-picker-notes" type="button">Full notes</button>
  `;

  // From the grid the notes open on the first subsection and page on from there
  picker.querySelector(".outcome-picker-notes").addEventListener("click", () => {
    openFullNotes(chapter.learningOutcomes[0].id);
  });

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

// ── Subject pages ─────────────────────────────
// /app/<subject>/ shows one subject; the hash picks the section (#flashcards, #exam…).
// Flashcards and Exam › By chapter list the chapters first, then use the study
// workbench below; Notes and the other Exam views draw into #sectionPanel.
function sectionFromHash() {
  const id = location.hash.slice(1);
  return sectionsFor(PAGE_SUBJECT).includes(id) ? id : "";
}

function enterSection() {
  if (!PAGE_SUBJECT) return;
  subjectSection = sectionFromHash();
  viewMode = "subject-overview";
  pickingOutcome = false;
  if (SECTION_TABS[subjectSection]) switchTab(SECTION_TABS[subjectSection]);
  if (subjectSection === "guide") openExamBreakdown(PAGE_SUBJECT);
  if (isAacSection(subjectSection)) openAacGuide(PAGE_SUBJECT, subjectSection);
  if (subjectSection) openSubjectData(PAGE_SUBJECT);
  renderAll();
  els.subjectArea.querySelectorAll(".section-panel, .workbench, .guide-inline").forEach((el) => { el.scrollTop = 0; });
}

function subjectStats(subject, user) {
  const progress = user?.progressByOutcome || {};
  const learned = user?.learnedByOutcome || {};
  let subEarned = 0, subTotal = 0;
  const chStats = (subject.chapters || []).map((ch) => {
    let chEarned = 0, chTotal = 0;
    (ch.learningOutcomes || []).forEach((lo) => {
      const concepts = outcomeCardTotal(lo);
      chTotal += concepts;
      chEarned += (progress[lo.id] || 0) >= 1 ? concepts : (learned[lo.id] || []).length;
    });
    subEarned += chEarned;
    subTotal += chTotal;
    return { ch, earned: chEarned, total: chTotal, ratio: chTotal ? chEarned / chTotal : 0 };
  });
  const pct = subTotal ? Math.round((subEarned / subTotal) * 100) : 0;
  return { subject, earned: subEarned, total: subTotal, pct, chStats };
}

function renderSubjectPage() {
  const user = getCurrentUser();
  const area = els.subjectArea;
  els.dashboard.classList.toggle("hidden", Boolean(PAGE_SUBJECT) || !user);
  if (!PAGE_SUBJECT) {
    els.subjectWorkbench.classList.add("hidden");
    els.sectionPanel.classList.add("hidden");
    if (user) renderDashboard();
    return;
  }
  // Tests pick their own chapters in the setup, so there is no chapter list first
  if (subjectSection === "tests") {
    viewMode = "chapter";
    pickingOutcome = false;
  }
  const locked = !user && !isPublicSection(subjectSection);
  const workbench = !locked && (subjectSection === "flashcards" || subjectSection === "tests"
    || (subjectSection === "exam" && examView === "chapter"));
  els.subjectWorkbench.classList.toggle("hidden", !workbench);
  // The paper guide and the AAC guide draw into the same element
  document.getElementById("examBreakdownModal").classList.toggle("hidden", subjectSection !== "guide" && !isAacSection(subjectSection));
  area.dataset.section = subjectSection || "home";
  area.dataset.examView = subjectSection === "exam" && !locked ? examView : "";
  // The subject heading is the back link: inside a section it steps back to the subject's tiles
  const back = document.querySelector(".subject-head-back");
  if (back) {
    back.title = subjectSection ? `Back to ${PAGE_SUBJECT_DATA.title}` : "Back to your subjects";
    // Same path and query, empty hash: a hash change, not a reload
    back.setAttribute("href", subjectSection ? `${location.pathname}${location.search}#` : "app.html");
    if (!back.dataset.wired) {
      back.dataset.wired = "1";
      back.addEventListener("click", stepBackFromHeading);
    }
  }
  // The guides carry their own big title, so they skip the subheading (it's empty, so CSS hides it)
  const ownTitle = subjectSection === "guide" || isAacSection(subjectSection);
  if (els.subjectSectionTitle) els.subjectSectionTitle.textContent = ownTitle ? "" : sectionLabel(PAGE_SUBJECT, subjectSection);
  renderSectionPanel(locked);
}

function renderSectionPanel(locked) {
  const panel = els.sectionPanel;
  panel.classList.remove("page-shell"); // the page's prebuilt placeholder (scripts/subject-pages.cjs) is drawn over below
  const show = locked || !subjectSection || subjectSection === "notes" || subjectSection === "exam";
  panel.classList.toggle("hidden", !show);
  if (!show) {
    sectionPanelKey = "";
    return;
  }
  const user = getCurrentUser();
  // Rebuilding resets open questions and scroll, so only redraw when what it shows has changed
  const key = [subjectSection, examView, examTypeFilter, locked, user?.username || "",
    subjectPackReady(PAGE_SUBJECT), examPackReady(PAGE_SUBJECT), typeof hasExamPapers, // paper-archive.js loads after app.js
    Object.keys(user?.viewedNotesByChapter || {}).length, user?.onboarding?.levels?.[PAGE_SUBJECT] || "",
    studyRange, studyRows?.length ?? studyRowsError].join("|");
  if (key === sectionPanelKey) return;
  sectionPanelKey = key;

  if (locked) {
    panel.innerHTML = `
      <div class="section-card section-locked">
        <h2>Sign in to use ${escapeHtml(sectionLabel(PAGE_SUBJECT, subjectSection).toLowerCase())}</h2>
        <p>Your progress saves to your account, so you can pick up on any device.</p>
        <div class="section-locked-actions">
          <button class="button-primary" type="button" data-auth-mode="signup">Make an account</button>
          <button class="button-secondary" type="button" data-auth-mode="signin">Sign in</button>
        </div>
      </div>`;
  } else if (!subjectSection) {
    panel.innerHTML = subjectHomeHtml();
  } else if (subjectSection === "notes") {
    panel.innerHTML = `<div class="section-card">${notesListHtml()}</div>`;
  } else {
    panel.innerHTML = examViewsHtml();
  }
  panel.querySelectorAll("[data-auth-mode]").forEach((btn) => {
    btn.addEventListener("click", () => showAuthMode(btn.dataset.authMode));
  });
  if (subjectSection === "exam" && examView === "papers") openExamPapers(PAGE_SUBJECT);
  if (subjectSection === "exam" && examView === "type") {
    bindExamAccordions(panel);
    typesetMath(panel);
  }
}

// The page's static "about" text (scripts/subject-pages.cjs): lifted out of the page at startup
// and shown under the section tiles only while signed out
const SUBJECT_ABOUT_HTML = (() => {
  const el = document.getElementById("subjectAbout");
  el?.remove();
  return el?.outerHTML || "";
})();

function subjectHomeHtml() {
  const subject = PAGE_SUBJECT_DATA;
  const below = getCurrentUser() ? studyTimeBlockHtml(subject.id) : `
    <div class="section-locked-actions">
      <button class="button-primary" type="button" data-auth-mode="signup">Make an account</button>
      <button class="button-secondary" type="button" data-auth-mode="signin">Sign in</button>
    </div>${SUBJECT_ABOUT_HTML}`;
  return `${sectionTilesHtml(subject.id)}${below}`;
}

// A chapter with subsections folds open to list them, each opening the notes on its own page;
// a one-subsection chapter opens its notes straight away
function notesListHtml() {
  const rows = PAGE_SUBJECT_DATA.chapters.map((ch) => {
    const outcomes = ch.learningOutcomes || [];
    const read = hasViewedNotesForChapter(ch.id);
    const id = escapeHtml(ch.id);
    const meta = `<span class="chapter-row-meta">${read ? `<span class="chapter-row-done">Read</span>` : outcomes.length > 1 ? plural(outcomes.length, "subsection") : ""}</span>`;
    if (outcomes.length < 2) return `
      <li>
        <button class="chapter-row" type="button" onclick="openChapterNotes('${id}')">
          <span class="chapter-row-title">${escapeHtml(ch.title)}</span>${meta}
        </button>
      </li>`;
    return `
      <li>
        <details class="chapter-fold">
          <summary class="chapter-row"><span class="chapter-row-title">${escapeHtml(ch.title)}</span>${meta}</summary>
          <ol class="chapter-subs">${outcomes.map((lo) => `
            <li><button type="button" onclick="openChapterNotes('${id}','${escapeHtml(lo.id)}')">${escapeHtml(compactText(lo.title || ""))}</button></li>`).join("")}
          </ol>
        </details>
      </li>`;
  }).join("");
  return `<ol class="chapter-rows">${rows}</ol>`;
}

function openChapterNotes(chapterId, outcomeId = "") {
  const chapter = PAGE_SUBJECT_DATA.chapters.find((c) => c.id === chapterId);
  if (!chapter) return;
  selectedChapterId = chapter.id;
  selectedOutcomeId = chapter.learningOutcomes.some((lo) => lo.id === outcomeId) ? outcomeId : chapter.learningOutcomes[0]?.id || "";
  // The notes text is in the subject pack; open once it has arrived
  requestSubjectPack(PAGE_SUBJECT).then(() => openFullNotes(selectedOutcomeId), (error) => console.error(error));
}

function setExamView(view) {
  examView = view;
  if (view === "chapter") viewMode = "subject-overview";
  renderAll();
}

function examViewsHtml() {
  // Only offer "By type" once the bank has tagged its questions (Maths' current bank hasn't)
  const typed = !examPackReady(PAGE_SUBJECT) || examTypeCounts(subjectExamGroups()).length > 0;
  const views = EXAM_VIEWS.filter(([id]) => (id !== "papers" || (typeof hasExamPapers === "function" && hasExamPapers(PAGE_SUBJECT)))
    && (id !== "type" || typed));
  if (!views.some(([id]) => id === examView)) examView = "chapter";
  const nav = `<div class="exam-views" role="tablist" aria-label="Exam questions">${views.map(([id, label]) => `
    <button type="button" role="tab" class="exam-view ${examView === id ? "active" : ""}" aria-selected="${examView === id}" onclick="setExamView('${id}')">${label}</button>`).join("")}
  </div>`;
  if (examView === "papers") return `${nav}<div class="section-card"><div id="papersBody" class="papers-body"></div></div>`;
  if (examView === "type") return `${nav}<div class="section-card">${examTypeHtml()}</div>`;
  return nav;
}

// Every past-paper question for the subject once, each tagged with the kinds of answer its parts ask for
function subjectExamGroups() {
  const seen = new Set();
  return PAGE_SUBJECT_DATA.chapters.flatMap(getExamQuestionsForChapter).filter((group) => {
    if (seen.has(group.id) || isOffSpecExamGroup(group) || hiddenByMathsPilot(group)) return false;
    seen.add(group.id);
    return true;
  });
}

function examGroupTypes(group) {
  return new Set((group.parts || []).flatMap((part) => [].concat(part.type || [])));
}

// A type with only a handful of questions isn't worth its own filter
const MIN_TYPE_QUESTIONS = 4;

// [[type, count]] for each labelled type with at least MIN_TYPE_QUESTIONS questions
function examTypeCounts(groups) {
  return Object.keys(EXAM_TYPE_LABELS)
    .map((type) => [type, groups.filter((g) => examGroupTypes(g).has(type)).length])
    .filter(([, n]) => n >= MIN_TYPE_QUESTIONS);
}

function examTypeHtml() {
  if (!examPackReady(PAGE_SUBJECT)) return skeletonHtml("rows");
  const groups = subjectExamGroups();
  const counts = examTypeCounts(groups);
  if (!counts.some(([type]) => type === examTypeFilter)) examTypeFilter = counts[0][0];
  const chips = counts.map(([type, n]) => `
    <button type="button" class="exam-type-chip" aria-pressed="${type === examTypeFilter}" onclick="examTypeFilter='${type}'; renderAll()">
      ${EXAM_TYPE_LABELS[type]} <span>${n}</span>
    </button>`).join("");
  const shown = groups.filter((g) => examGroupTypes(g).has(examTypeFilter))
    .sort((a, b) => (b.year || 0) - (a.year || 0) || (a.questionNumber || 0) - (b.questionNumber || 0));
  return `
    <div class="exam-type-chips" aria-label="Question type">${chips}</div>
    <p class="exam-type-note muted small">Newest first. A question is listed when any of its parts is ${escapeHtml(EXAM_TYPE_LABELS[examTypeFilter].toLowerCase())}.</p>
    <div class="exam-container">${shown.map(examGroupHtml).join("")}</div>`;
}

// The chapter list a section opens on (Flashcards, Exam › By chapter)
function renderSubjectOverview() {
  const overviewEl = els.subjectOverview;
  if (!overviewEl) return;

  const user = getCurrentUser();
  const isOverview = viewMode === 'subject-overview' && Boolean(user);
  els.subjectWorkbench.classList.toggle('overview-mode', isOverview);
  overviewEl.classList.toggle('hidden', !isOverview);
  if (!isOverview) return;

  const ss = subjectStats(PAGE_SUBJECT_DATA, user);
  const forExam = subjectSection === "exam";
  const rows = ss.chStats.map(s => {
    const pct = Math.round(s.ratio * 100);
    const examCount = forExam && examPackReady(PAGE_SUBJECT)
      ? getExamQuestionsForChapter(s.ch).filter((g) => !isOffSpecExamGroup(g)).length : null;
    return `
      <button class="overview-chapter-row" onclick="selectChapterFromOverview('${escapeHtml(s.ch.id)}')">
        <div class="overview-chapter-text">
          <span class="overview-chapter-title">${escapeHtml(s.ch.title)}</span>
          <span class="overview-chapter-score">${forExam ? (examCount === null ? "" : plural(examCount, "question")) : `${s.earned}/${s.total}`}</span>
        </div>
        ${forExam ? "" : `<div class="overview-progress-bar"><div class="overview-progress-fill" style="width:${pct}%"></div></div>`}
      </button>`;
  }).join('');

  overviewEl.innerHTML = `<div class="overview-chapter-list">${rows}</div>`;
}

function selectChapterFromOverview(chapterId) {
  const subject = SUBJECTS.find(s => s.id === selectedSubjectId);
  if (!subject) return;
  const chapter = subject.chapters.find(c => c.id === chapterId);
  if (!chapter) return;
  openSubjectData(subject.id);
  selectedChapterId = chapterId;
  selectedOutcomeId = chapter.learningOutcomes[0]?.id || '';
  studyIndex = 0;
  showAnswer = false;
  viewMode = 'chapter';
  // Exam questions are per chapter; flashcards go on to the chapter's subsections
  pickingOutcome = subjectSection === "flashcards" && chapterHasSubsections(chapter);
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

  // The subject's flashcards are still downloading: show a placeholder, not a half-filled card
  if (openedSubjects.has(selectedSubjectId) && !subjectPackReady(selectedSubjectId)) {
    els.flashcardList.innerHTML = "";
    els.flashcardStudy.innerHTML = skeletonHtml("card");
    return;
  }

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
    chapterTotalCards += outcomeCardTotal(lo);
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
      <span class="study-card-count">${cards.length ? studyIndex + 1 : 0}/${outcomeCardTotal(outcome)}</span>
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
    minutes: Number.isFinite(Number(saved.minutes)) ? snapTestMinutes(saved.minutes) : 10,
    mix: TEST_MIXES.some((mix) => mix.id === saved.mix) ? saved.mix : "balanced",
    customChapters: saved.customChapters && typeof saved.customChapters === "object" ? saved.customChapters : {},
  };
}

function snapTestMinutes(value) {
  const { min, max, step } = TEST_MINUTES;
  return Math.min(max, Math.max(min, Math.round(Number(value) / step) * step));
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
  // the level is in the key because the pool's exam questions are filtered by it
  const level = getCurrentUser()?.onboarding?.levels?.[subject.id] || "";
  const key = `${subject.id}|${level}|${chapters.map((c) => c.id).join(",")}`;
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
  // Only the Test tab needs this, and only then is the Test kit downloaded
  if (!els.testTab?.classList.contains("active")) return;
  if (!window.TestBuilder) {
    els.testContainer.innerHTML = skeletonHtml("rows");
    loadTestKit().then(renderTestOverview, (error) => {
      console.error(error);
      els.testContainer.innerHTML = `<p class="muted">The test could not be loaded. Check your connection and try again.</p>`;
    });
    return;
  }
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  if (!subject) return;
  const settings = getTestSettings();
  const scope = getTestScope(settings);
  const covered = new Set(scope.chapters.map((c) => c.id));
  const mixIndex = TEST_MIXES.findIndex((mix) => mix.id === settings.mix);
  const share = TestBuilder.MIX_FLASHCARD_SHARE[settings.mix] ?? 0.5;
  const minutesP = (settings.minutes - TEST_MINUTES.min) / (TEST_MINUTES.max - TEST_MINUTES.min);
  const scopeOption = (value, title, meta) => `
    <button type="button" class="test-dropdown-option" role="radio" aria-checked="${settings.scope === value}" data-test-scope="${value}">
      <span>${title}</span><small>${meta}</small>
    </button>`;

  els.testContainer.innerHTML = `
    <div class="test-setup">
      <div class="test-setup-row">
        <span class="test-setup-label" id="testScopeLabel">Cover</span>
        <details class="test-dropdown">
          <summary class="test-dropdown-toggle" aria-describedby="testScopeLabel">
            <span class="test-dropdown-value">${escapeHtml(scope.label || "Choose chapters")}</span>
            <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="test-dropdown-menu">
            <div role="radiogroup" aria-labelledby="testScopeLabel">
              ${scopeOption("chapter", "This chapter", escapeHtml(getSelectedChapter()?.title || "None selected"))}
              ${scopeOption("subject", `All of ${escapeHtml(subject.title)}`, plural(subject.chapters.length, "chapter"))}
            </div>
            <p class="test-dropdown-head">Or pick chapters</p>
            <ul class="test-chapter-list">
              ${subject.chapters.map((chapter) => `
                <li>
                  <label class="test-chapter-option">
                    <input type="checkbox" data-test-chapter="${escapeHtml(chapter.id)}" ${covered.has(chapter.id) ? "checked" : ""} />
                    <span>${escapeHtml(chapter.title)}</span>
                  </label>
                </li>`).join("")}
            </ul>
          </div>
        </details>
      </div>
      <div class="test-setup-row">
        <label class="test-setup-label" for="testMinutes">Time</label>
        <div class="test-time" style="--p: ${minutesP}">
          <output class="test-time-value" for="testMinutes"><strong>${settings.minutes}</strong> min</output>
          <input type="range" id="testMinutes" class="test-range" min="${TEST_MINUTES.min}" max="${TEST_MINUTES.max}" step="${TEST_MINUTES.step}" value="${settings.minutes}" aria-valuetext="${settings.minutes} minutes" data-test-minutes />
          <div class="test-time-scale" aria-hidden="true">
            ${[5, 15, 30, 45, 60].map((m) => `<span style="--p: ${(m - TEST_MINUTES.min) / (TEST_MINUTES.max - TEST_MINUTES.min)}">${m}</span>`).join("")}
          </div>
        </div>
      </div>
      <div class="test-setup-row">
        <span class="test-setup-label" id="testMixLabel">Mix</span>
        <div class="test-mix" style="--mix-i: ${mixIndex}; --mix-share: ${share}">
          <div class="test-mix-track" role="radiogroup" aria-labelledby="testMixLabel">
            <span class="test-mix-thumb" aria-hidden="true"></span>
            ${TEST_MIXES.map((mix, i) => `
              <button type="button" class="test-mix-stop" role="radio" aria-checked="${i === mixIndex}" tabindex="${i === mixIndex ? 0 : -1}" aria-label="${mix.label}" data-test-mix="${mix.id}">${mix.short}</button>`).join("")}
          </div>
          <div class="test-mix-ratio" aria-hidden="true">
            <span>Flashcards <b data-mix-cards>${Math.round(share * 100)}%</b></span>
            <span class="test-mix-bar"><i class="is-cards"></i><i class="is-exam"></i></span>
            <span><b data-mix-exam>${Math.round((1 - share) * 100)}%</b> Exam Qs</span>
          </div>
        </div>
      </div>
      ${renderTestPreview(scope, previewTest(subject, scope, settings), settings)}
      ${renderTestHistory(subject)}
    </div>
  `;
}

function previewTest(subject, scope, settings) {
  if (!scope.chapters.length) return null;
  return TestBuilder.assembleTest(getTestPool(subject, scope.chapters), { minutes: settings.minutes, mix: settings.mix, random: seededRandom(7) });
}

// Controls update in place rather than re-rendering, so the slider keeps its
// drag, the chapter list keeps its scroll and the mix thumb can glide.
function refreshTestSetup() {
  const root = els.testContainer.querySelector(".test-setup");
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  if (!root || !subject) return renderTestOverview();
  const settings = getTestSettings();
  const scope = getTestScope(settings);
  const covered = new Set(scope.chapters.map((c) => c.id));
  root.querySelector(".test-dropdown-value").textContent = scope.label || "Choose chapters";
  root.querySelectorAll("[data-test-scope]").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.testScope === settings.scope)));
  root.querySelectorAll("[data-test-chapter]").forEach((box) => { box.checked = covered.has(box.dataset.testChapter); });

  const share = TestBuilder.MIX_FLASHCARD_SHARE[settings.mix] ?? 0.5;
  const mix = root.querySelector(".test-mix");
  mix.style.setProperty("--mix-i", TEST_MIXES.findIndex((m) => m.id === settings.mix));
  mix.style.setProperty("--mix-share", share);
  mix.querySelectorAll("[data-test-mix]").forEach((b) => {
    const on = b.dataset.testMix === settings.mix;
    b.setAttribute("aria-checked", String(on));
    b.tabIndex = on ? 0 : -1;
  });
  mix.querySelector("[data-mix-cards]").textContent = `${Math.round(share * 100)}%`;
  mix.querySelector("[data-mix-exam]").textContent = `${Math.round((1 - share) * 100)}%`;

  root.querySelector(".test-setup-start").outerHTML = renderTestPreview(scope, previewTest(subject, scope, settings), settings);
}

// A small pop and haptic tick when a control lands on a new value.
function nudgeTestControl(el) {
  navigator.vibrate?.(6);
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  el?.animate([{ transform: "scale(1.14)" }, { transform: "none" }], { duration: 320, easing: "cubic-bezier(0.22, 1, 0.36, 1)" });
}

function setTestMix(id) {
  const settings = getTestSettings();
  if (settings.mix === id) return;
  settings.mix = id;
  saveTestSettings(settings);
  refreshTestSetup();
  nudgeTestControl(els.testContainer.querySelector(`[data-test-mix="${id}"]`));
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
  if (target.dataset.testMix) {
    setTestMix(target.dataset.testMix);
  } else if (target.dataset.testScope) {
    const settings = getTestSettings();
    settings.scope = target.dataset.testScope;
    saveTestSettings(settings);
    refreshTestSetup();
    closeTestDropdown(true);
  } else if (target.dataset.testAction === "start") {
    startTest();
  }
}

// Ticking a chapter starts from whatever is covered now, so "This chapter"
// plus one more tick is two chapters, not one.
function handleTestSetupChange(event) {
  const box = event.target.closest("[data-test-chapter]");
  if (!box) return;
  const settings = getTestSettings();
  const subject = SUBJECTS.find((s) => s.id === selectedSubjectId);
  const chosen = new Set(getTestScope(settings).chapters.map((c) => c.id));
  if (box.checked) chosen.add(box.dataset.testChapter);
  else chosen.delete(box.dataset.testChapter);
  settings.scope = "custom";
  settings.customChapters[selectedSubjectId] = subject.chapters.map((c) => c.id).filter((id) => chosen.has(id));
  saveTestSettings(settings);
  refreshTestSetup();
}

function handleTestSetupInput(event) {
  const range = event.target.closest("[data-test-minutes]");
  if (!range) return;
  const settings = getTestSettings();
  const minutes = snapTestMinutes(range.value);
  if (minutes === settings.minutes) return;
  settings.minutes = minutes;
  saveTestSettings(settings);
  range.setAttribute("aria-valuetext", `${minutes} minutes`);
  const time = range.closest(".test-time");
  time.style.setProperty("--p", (minutes - TEST_MINUTES.min) / (TEST_MINUTES.max - TEST_MINUTES.min));
  time.querySelector(".test-time-value strong").textContent = minutes;
  nudgeTestControl(time.querySelector(".test-time-value strong"));
  refreshTestSetup();
}

function handleTestSetupKeydown(event) {
  if (event.key === "Escape" && event.target.closest(".test-dropdown[open]")) {
    closeTestDropdown(true);
    return;
  }
  const stop = event.target.closest("[data-test-mix]");
  const step = { ArrowLeft: -1, ArrowUp: -1, ArrowRight: 1, ArrowDown: 1 }[event.key];
  if (!stop || !step) return;
  event.preventDefault();
  const i = Math.min(TEST_MIXES.length - 1, Math.max(0, TEST_MIXES.findIndex((m) => m.id === stop.dataset.testMix) + step));
  setTestMix(TEST_MIXES[i].id);
  els.testContainer.querySelector(`[data-test-mix="${TEST_MIXES[i].id}"]`)?.focus();
}

// Press anywhere on the mix track and drag: the thumb follows, snapping to each stop.
function handleTestMixPointer(event) {
  const track = event.target.closest(".test-mix-track");
  if (!track) return;
  const pick = (e) => {
    const box = track.getBoundingClientRect();
    const i = Math.floor(((e.clientX - box.left) / box.width) * TEST_MIXES.length);
    setTestMix(TEST_MIXES[Math.min(TEST_MIXES.length - 1, Math.max(0, i))].id);
  };
  track.setPointerCapture(event.pointerId);
  track.classList.add("is-dragging");
  pick(event);
  track.onpointermove = pick;
  track.onpointerup = track.onpointercancel = () => {
    track.onpointermove = track.onpointerup = track.onpointercancel = null;
    track.classList.remove("is-dragging");
  };
}

function closeTestDropdown(refocus) {
  const menu = els.testContainer.querySelector(".test-dropdown[open]");
  if (!menu) return;
  menu.open = false;
  if (refocus) menu.querySelector("summary").focus();
}

// ── Running a test ──

function startTest(retestItems) {
  if (!getCurrentUser()) return;
  // Tests draw on the subject's notes, flashcards and questions: wait for them first.
  if (!subjectPackReady(selectedSubjectId)) {
    openSubjectData(selectedSubjectId);
    requestSubjectPack(selectedSubjectId).then(() => startTest(retestItems), (error) => console.error(error));
    return;
  }
  // Tests draw on past-paper questions, so wait for the subject's bank first.
  if (!examPackReady(selectedSubjectId)) {
    requestExamPack(selectedSubjectId).then(() => startTest(retestItems));
    return;
  }
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
  typesetMath(els.testScreen);
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
  if (item.kind === "cloze" && item.bank) return renderClozeBank(item, response);
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
    ${item.images?.length ? renderExamPaperImages({ images: item.images, year: item.year, questionNumber: item.questionNumber, level: item.level }) : ""}
    <h2 class="test-prompt test-prompt--exam">${testMultiline(item.prompt)}</h2>
    ${item.diagram ? `<button type="button" class="button-secondary test-diagram" data-test-diagram="${escapeHtml(item.diagram)}">Show diagram</button>` : ""}
    <textarea class="test-answer" data-test-text rows="${item.marks >= 20 ? 10 : 6}" placeholder="Your answer">${escapeHtml(response.text || "")}</textarea>`;
}

// Fill-the-gap with a word bank: gaps are drop targets, the bank's chips are
// dragged (or tapped) into them. A used chip leaves a placeholder so the bank
// does not reflow under the student's finger.
function clozeTargetGap(item) {
  const blanks = activeTest.responses[item.id]?.blanks || [];
  const target = activeTest.gapTarget;
  if (target?.itemId === item.id && target.gap < item.answers.length) return target.gap;
  const empty = item.answers.findIndex((_, i) => !blanks[i]);
  return empty >= 0 ? empty : item.answers.length - 1;
}

function renderClozeBank(item, response) {
  const blanks = response.blanks || [];
  const target = clozeTargetGap(item);
  const sentence = item.segments.map((segment) => {
    if (segment.blank === undefined) return escapeHtml(segment.text);
    const i = segment.blank;
    const word = blanks[i] || "";
    const state = `${word ? " is-filled" : ""}${i === target ? " is-target" : ""}`;
    return `<button type="button" class="test-gap${state}" data-test-gap="${i}"
      aria-label="Gap ${i + 1}${word ? `: ${escapeHtml(word)}. Tap to clear` : ", empty"}">${word ? escapeHtml(word) : `<span aria-hidden="true">${i + 1}</span>`}</button>`;
  }).join("");
  const used = new Set(blanks.filter(Boolean));
  const chips = item.bank.map((word, k) => used.has(word)
    ? `<span class="test-chip is-used" aria-hidden="true">${escapeHtml(word)}</span>`
    : `<button type="button" class="test-chip" data-test-chip="${k}">${k < 9 ? `<kbd>${k + 1}</kbd>` : ""}${escapeHtml(word)}</button>`).join("");
  const gaps = item.answers.length === 1 ? "the gap" : "each gap";
  return `
    <p class="test-instruction">Drag a word into ${gaps}, or tap a word to drop it in the highlighted gap.</p>
    <h2 class="test-prompt">${escapeHtml(item.prompt)}</h2>
    <p class="test-cloze">${sentence}</p>
    <div class="test-bank" role="group" aria-label="Word bank">${chips}</div>`;
}

function placeClozeWord(item, word, gap) {
  const blanks = Array.from({ length: item.answers.length }, (_, i) => activeTest.responses[item.id]?.blanks?.[i] || "");
  const from = blanks.indexOf(word);
  if (from >= 0) blanks[from] = blanks[gap]; // moving a placed word swaps it with the gap's word
  blanks[gap] = word;
  setTestResponse(item, { blanks });
  const next = blanks.findIndex((b) => !b);
  activeTest.gapTarget = { itemId: item.id, gap: next >= 0 ? next : gap };
}

function clearClozeGap(item, gap) {
  const blanks = [...(activeTest.responses[item.id]?.blanks || [])];
  blanks[gap] = "";
  setTestResponse(item, { blanks });
  activeTest.gapTarget = { itemId: item.id, gap };
}

function redrawTestQuestion() {
  renderTestScreen();
  tickTestClock();
}

// Pointer-driven drag so it works the same with a mouse, a pen or a finger.
let clozeDrag = null;
let suppressTestClick = false;

function handleTestPointerDown(event) {
  if (!activeTest || activeTest.phase !== "run" || event.button > 0) return;
  const item = activeTest.items[activeTest.index];
  if (item?.kind !== "cloze" || !item.bank) return;
  const chip = event.target.closest("button.test-chip");
  const gap = event.target.closest(".test-gap.is-filled");
  if (!chip && !gap) return;
  const blanks = activeTest.responses[item.id]?.blanks || [];
  const word = chip ? item.bank[Number(chip.dataset.testChip)] : blanks[Number(gap.dataset.testGap)];
  if (!word) return;
  clozeDrag = { item, word, source: chip || gap, fromGap: gap ? Number(gap.dataset.testGap) : null, x: event.clientX, y: event.clientY, ghost: null };
  window.addEventListener("pointermove", handleTestPointerMove, { passive: false });
  window.addEventListener("pointerup", handleTestPointerUp);
  window.addEventListener("pointercancel", endClozeDrag);
}

function gapUnderPointer(event) {
  return document.elementFromPoint(event.clientX, event.clientY)?.closest(".test-gap") || null;
}

function handleTestPointerMove(event) {
  const drag = clozeDrag;
  if (!drag) return;
  if (!drag.ghost) {
    if (Math.hypot(event.clientX - drag.x, event.clientY - drag.y) < 6) return;
    const box = drag.source.getBoundingClientRect();
    drag.offsetX = drag.x - box.left;
    drag.offsetY = drag.y - box.top;
    drag.ghost = document.createElement("span");
    drag.ghost.className = "test-chip is-ghost";
    drag.ghost.textContent = drag.word;
    document.body.appendChild(drag.ghost);
    drag.source.classList.add("is-lifted");
    els.testScreen.classList.add("is-dragging");
  }
  event.preventDefault();
  drag.ghost.style.transform = `translate(${event.clientX - drag.offsetX}px, ${event.clientY - drag.offsetY}px)`;
  const over = gapUnderPointer(event);
  els.testScreen.querySelectorAll(".test-gap.is-over").forEach((g) => g !== over && g.classList.remove("is-over"));
  over?.classList.add("is-over");
}

function handleTestPointerUp(event) {
  const drag = clozeDrag;
  if (!drag) return;
  const dragged = Boolean(drag.ghost);
  endClozeDrag();
  if (!dragged) return; // a tap: the click handler places the word
  suppressTestClick = true;
  window.setTimeout(() => { suppressTestClick = false; }, 0);
  const over = gapUnderPointer(event);
  if (over) placeClozeWord(drag.item, drag.word, Number(over.dataset.testGap));
  else if (drag.fromGap !== null) clearClozeGap(drag.item, drag.fromGap); // dragged out of its gap
  else return;
  redrawTestQuestion();
}

function endClozeDrag() {
  window.removeEventListener("pointermove", handleTestPointerMove);
  window.removeEventListener("pointerup", handleTestPointerUp);
  window.removeEventListener("pointercancel", endClozeDrag);
  if (clozeDrag?.ghost) clozeDrag.ghost.remove();
  clozeDrag?.source?.classList.remove("is-lifted");
  els.testScreen.classList.remove("is-dragging");
  els.testScreen.querySelectorAll(".test-gap.is-over").forEach((g) => g.classList.remove("is-over"));
  clozeDrag = null;
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
  const results = activeTest.items.map((item) => TestBuilder.markItem(item, activeTest.responses[item.id]));
  const hasAutoMarked = results.some((result) => result.auto);
  const note = pending
    ? "Most answers are marked for you. Where no marking points could be found, compare your answer with the one shown and give yourself the marks an examiner would."
    : hasAutoMarked
      ? "Everything is marked. Written answers are checked against the marking scheme's points: look over each one, and change the mark if it missed something you said another way."
      : "Every answer here was marked for you.";

  return `
    <div class="test-review">
      ${renderTestBar(`
        <span class="test-live-score">${summary.percent}% so far</span>
        <button type="button" class="button-primary" data-test-action="save">${saveLabel}</button>`)}
      <main class="test-sheet">
        <header class="test-sheet-head">
          <h1>${pending ? "Mark your answers" : "Check your marks"}</h1>
          <p>${intro} ${note}</p>
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
    if (result.auto?.confidence === "low" && !result.overridden) verdict = `<span class="test-verdict-check">Worth a check</span>${verdict}`;
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
      // A word picked from the bank is exactly right or wrong; only typed words can be argued.
      const countIt = given && !item.bank
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

  // With an automatic mark the picker shows it, and choosing another overrides it.
  const shown = result.needsSelfMark ? response.selfMarks : result.earned;
  const resetLink = result.overridden && result.auto
    ? `<button type="button" class="test-link" data-test-selfmark-reset>Use the automatic mark (${result.auto.earned})</button>`
    : "";
  const markLabel = result.needsSelfMark ? "Your marks" : result.overridden ? "Your mark" : "Mark";

  if (item.kind === "recall") {
    const choices = [
      { value: 0, label: "Missed it" },
      { value: 1, label: "Partly" },
      { value: 2, label: "Got it" },
    ];
    const card = result.auto
      ? `<p><strong>${escapeHtml(item.term)}</strong> ${result.auto.points.map(renderMarkedPointText).join(" ")}</p>`
      : `<p><strong>${escapeHtml(item.term)}</strong> ${escapeHtml(item.definition)}</p>`;
    return `
      <p class="test-review-prompt">${escapeHtml(item.prompt)}</p>
      ${answerBox}
      <div class="test-review-model">
        <span class="test-review-label">The flashcard</span>
        ${card}
        ${result.auto && response.text?.trim() ? `<span class="test-review-hint">Highlighted: the card's key words you used.</span>` : ""}
      </div>
      <div class="test-selfmark-row">
        <div class="test-selfmark" role="radiogroup" aria-label="How did you do?">
          ${choices.map((c) => `<button type="button" class="test-choice${shown === c.value ? " is-active" : ""}" role="radio" aria-checked="${shown === c.value}" data-test-selfmark="${c.value}">${c.label}</button>`).join("")}
        </div>
        ${resetLink}
      </div>`;
  }

  // Written exam answer: marking points (or the model answer) plus a marks picker.
  const marks = shown;
  const picker = item.marks <= 12
    ? `<div class="test-selfmark test-selfmark--marks" role="radiogroup" aria-label="Marks out of ${item.marks}">
        ${Array.from({ length: item.marks + 1 }, (_, m) => `<button type="button" class="test-choice${marks === m ? " is-active" : ""}" role="radio" aria-checked="${marks === m}" data-test-selfmark="${m}">${m}</button>`).join("")}
       </div>`
    : `<label class="test-selfmark test-selfmark--range">
        <input type="range" min="0" max="${item.marks}" step="1" value="${Number.isFinite(marks) ? marks : 0}" data-test-selfmark-range />
        <output>${Number.isFinite(marks) ? `${marks} / ${item.marks}` : "Drag to mark"}</output>
       </label>`;
  const scheme = item.schemePoints ? `<span class="test-review-hint">The marking scheme looks for ${plural(item.schemePoints, "point")}.</span>` : "";
  const answered = Boolean(response.text?.trim());
  const model = result.auto && answered
    ? `<div class="test-review-model">
        <span class="test-review-label">${item.groupId ? "Marking scheme points" : "Model answer points"}</span>
        ${renderMarkingPoints(result.auto)}
        <span class="test-review-hint">${markingSummary(result.auto)}</span>
      </div>`
    : `<div class="test-review-model">
        <span class="test-review-label">${item.groupId ? "Marking scheme answer" : "Model answer"}</span>
        <div class="exam-answer-text">${item.groupId ? formatModelAnswer(item.model, item.subject) : formatAuthoredModel(item.model)}</div>
        ${scheme}
      </div>`;
  return `
    <p class="test-review-prompt">${testMultiline(item.prompt)}</p>
    ${answerBox}
    ${model}
    <div class="test-selfmark-row">
      <span class="test-review-label">${markLabel}</span>
      ${picker}
      ${resetLink}
    </div>`;
}

// A marking point's text with the words the student matched highlighted, and
// (on a missed point) the key words they needed in bold.
function renderMarkedPointText(point) {
  const made = point.credit >= 1;
  return point.parts.map((part) => {
    const text = escapeHtml(part.text);
    if (part.matched) return `<mark class="test-hit">${text}</mark>`;
    if (part.key && !made) return `<strong>${text}</strong>`;
    return text;
  }).join("");
}

const POINT_STATES = {
  made: { glyph: "✓", label: "Made" },
  part: { glyph: "½", label: "Partly made" },
  missed: { glyph: "", label: "Missed" },
};

function renderMarkingPoints(auto) {
  return `<ol class="test-points">${auto.points.map((point) => {
    const state = point.credit >= 1 ? "made" : point.credit > 0 ? "part" : "missed";
    return `<li class="test-point is-${state}">
      <span class="test-point-mark" aria-hidden="true">${POINT_STATES[state].glyph}</span>
      <span class="sr-only">${POINT_STATES[state].label}:</span>
      <span class="test-point-text">${renderMarkedPointText(point)}</span>
    </li>`;
  }).join("")}</ol>`;
}

function markingSummary(auto) {
  const made = auto.points.filter((p) => p.credit >= 1).length;
  const part = auto.points.filter((p) => p.credit > 0 && p.credit < 1).length;
  const found = `You made ${made}${part ? ` (and partly ${part})` : ""} of ${plural(auto.points.length, "point")}`;
  const needed = auto.points.length > 1 && auto.needed < auto.points.length ? `; full marks needs ${auto.needed}` : "";
  const check = auto.confidence === "low"
    ? " The scheme's answer is a sample, so check for points you made in your own words."
    : "";
  return `${found}${needed}.${check}`;
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
  if (!target || suppressTestClick) return;
  const item = activeTest.items[activeTest.index];
  const reviewItem = target.closest(".test-review-item");
  const reviewed = reviewItem ? activeTest.items.find((i) => `review-${i.id}` === reviewItem.id) : null;
  const action = target.dataset.testAction;

  if (target.dataset.testChoice !== undefined && activeTest.phase === "run") {
    setTestResponse(item, { choice: Number(target.dataset.testChoice) });
    renderTestScreen();
    tickTestClock();
    els.testScreen.querySelector(".test-option.is-picked")?.focus({ preventScroll: true });
  } else if (target.dataset.testChip !== undefined && activeTest.phase === "run") {
    placeClozeWord(item, item.bank[Number(target.dataset.testChip)], clozeTargetGap(item));
    redrawTestQuestion();
  } else if (target.dataset.testGap !== undefined && activeTest.phase === "run") {
    const gap = Number(target.dataset.testGap);
    if (activeTest.responses[item.id]?.blanks?.[gap]) clearClozeGap(item, gap);
    else activeTest.gapTarget = { itemId: item.id, gap };
    redrawTestQuestion();
  } else if (target.dataset.testSelfmarkReset !== undefined && reviewed) {
    const { selfMarks, ...rest } = activeTest.responses[reviewed.id] || {};
    activeTest.responses[reviewed.id] = rest;
    rerenderReviewKeepingScroll();
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
  else if (item.kind === "cloze" && item.bank && /^[1-9]$/.test(event.key)) {
    const word = item.bank[Number(event.key) - 1];
    const placed = (activeTest.responses[item.id]?.blanks || []).includes(word);
    if (word && !placed) {
      placeClozeWord(item, word, clozeTargetGap(item));
      redrawTestQuestion();
    }
  } else if (TEST_CHOICE_KINDS.has(item.kind)) {
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

// ── Lazy subject data ──
// Opening the app downloads no notes and no past-paper banks: every topic is drawn
// from subject-index.js (its first flashcard and card count). The first time the
// student opens one of a subject's topics, that subject's notes and flashcards
// (subject-packs.js) and its past-paper bank (exam-packs.js) load, and the views
// redraw from the full data. (openedSubjects is declared with the other state above.)

function openSubjectData(subjectId) {
  if (subjectId) openedSubjects.add(subjectId);
}

function subjectPackReady(subjectId) {
  return !window.SubjectPacks || window.SubjectPacks.isLoaded(subjectId);
}

function requestSubjectPack(subjectId) {
  if (subjectPackReady(subjectId)) return Promise.resolve();
  return window.SubjectPacks.load(subjectId).then(() => {
    const subject = SUBJECTS.find((s) => s.id === subjectId);
    if (!subject) return;
    subject.chapters = buildSubjectChapters(subjectId);
    testPoolCache.clear();
    if (selectedSubjectId === subjectId) keepSelectionInSubject(subject);
    renderAll();
  });
}

// subject-index.js mirrors the full data, but if it's out of date a selected topic
// may not exist once the real files arrive: fall back to the first one.
function keepSelectionInSubject(subject) {
  const chapter = subject.chapters.find((c) => c.id === selectedChapterId) || subject.chapters[0];
  selectedChapterId = chapter?.id || "";
  const outcomes = chapter?.learningOutcomes || [];
  if (!outcomes.some((lo) => lo.id === selectedOutcomeId)) {
    selectedOutcomeId = outcomes[0]?.id || "";
    studyIndex = 0;
    showAnswer = false;
  }
}

// Using the study area on a topic that is on screen but not downloaded yet (the
// default topic shown after signing in) counts as opening it. This only starts the
// download; it never redraws mid-click.
function openShownSubjectData(event) {
  if (openedSubjects.has(selectedSubjectId)) return;
  if (event.type === "keydown" && event.target.closest?.("input, textarea, select, [contenteditable]")) return;
  if (event.type === "keydown" && els.subjectWorkbench?.classList.contains("hidden")) return;
  openSubjectData(selectedSubjectId);
  requestSubjectPack(selectedSubjectId).catch((error) => console.error(error));
  requestExamPack(selectedSubjectId);
}

// Past-paper banks load per subject (exam-packs.js) rather than with the page.
// Opening a subject asks for its bank, and the views redraw when it arrives.
function examPackReady(subjectId) {
  return !window.ExamPacks || window.ExamPacks.isLoaded(subjectId);
}

function requestExamPack(subjectId) {
  if (examPackReady(subjectId)) return Promise.resolve();
  return window.ExamPacks.load(subjectId).then(() => {
    testPoolCache.clear();
    if (selectedSubjectId === subjectId) renderAll();
    const breakdown = document.getElementById("examBreakdownModal");
    if (breakdownSelection?.subjectId === subjectId && breakdown && !breakdown.classList.contains("hidden")) {
      selectBreakdownSection(subjectId, breakdownSelection.idx);
    }
  }, (error) => {
    console.error(error);
    if (selectedSubjectId === subjectId && els.examTab?.classList.contains("active")) renderExamSection();
  });
}

function getExamQuestionsForChapter(chapter) {
  return examGroupsForChapter(chapter).filter((group) => !hiddenByUserLevel(group));
}

function examGroupsForChapter(chapter) {
  const source = getOriginalChapter(chapter.id);
  const cached = source?.examQuestions || [];
  // Rebuilt (paper-crop) questions load after the push loop, so list them ahead of the cache.
  // A rebuilt question is listed under its own chapter and every chapter one of its parts is tagged with.
  const rebuilt = (window.EXAM_QUESTIONS_DB || []).filter(q => q.images?.length
    && (q.chapterId === chapter.id || q.parts?.some(part => part.topics?.includes(chapter.id))));
  // Maths pilot preview shows only the rebuilt questions, not the old maths bank.
  if (window.MATHS_BANK_PILOT && chapter.id?.startsWith("maths")) return rebuilt;
  if (rebuilt.length) return [...rebuilt, ...cached.filter(q => !rebuilt.includes(q))];
  if (cached.length) return cached;
  // Fall back to live DB for chapters loaded via additive scripts after the initial push loop.
  return (window.EXAM_QUESTIONS_DB || []).filter(q => q.chapterId === chapter.id);
}

// Exam questions follow the level picked in onboarding for their subject; a question with no
// known level, or a user with no level for that subject, shows everything.
function hiddenByUserLevel(group) {
  const level = getCurrentUser()?.onboarding?.levels?.[group?.subject];
  const groupLevel = examGroupLevel(group);
  return Boolean(level && groupLevel) && groupLevel !== level;
}

// Home Economics records the level only in its source line ("LC Home Economics Ordinary 2025 …").
function examGroupLevel(group) {
  return group?.level || /\b(Higher|Ordinary)\b/.exec(group?.source || "")?.[1].toLowerCase() || "";
}

// During the maths pilot preview the old (text-only) maths questions are hidden everywhere.
function hiddenByMathsPilot(group) {
  return Boolean(window.MATHS_BANK_PILOT && group?.subject === "maths" && !group.images?.length);
}

function isOffSpecExamGroup(group) {
  const parts = group?.parts || [];
  return parts.length > 0 && parts.every((part) => part.offSpec);
}

// Rebuilt banks show the question exactly as printed on the paper (cropped from the PDF),
// so students read the stem, data and figures the way they will in the exam.
function renderExamPaperImages(group) {
  if (!group.images?.length) return "";
  const where = [group.year, group.level === "ordinary" ? "Ordinary Level" : group.level === "higher" ? "Higher Level" : "", group.questionNumber ? `Question ${group.questionNumber}` : ""].filter(Boolean).join(" ");
  const scale = getExamPaperScale();
  return `<div class="exam-paper">${group.images.map((src, i) => `
    <div class="exam-paper-sheet" style="--paper-scale: ${scale}%">
      <button type="button" class="exam-paper-page" onclick="openDiagramModal('${escapeHtml(src)}')" aria-label="Enlarge page ${i + 1} of ${group.images.length}">
        <img src="${escapeHtml(src)}" alt="${escapeHtml(`${where} as printed on the paper${group.images.length > 1 ? `, page ${i + 1} of ${group.images.length}` : ""}`)}" loading="lazy" />
      </button>
      <input type="range" class="exam-paper-size" min="${EXAM_PAPER_SCALE_MIN}" max="100" step="5" value="${scale}" oninput="setExamPaperScale(this)" aria-label="Page size" aria-valuetext="${scale}%" title="Page size" />
    </div>`).join("")}
  </div>`;
}

function getExamPaperScale() {
  try {
    const saved = Number(localStorage.getItem(EXAM_PAPER_SCALE_KEY));
    if (saved >= EXAM_PAPER_SCALE_MIN && saved <= 100) return saved;
  } catch {}
  return 100;
}

function setExamPaperScale(input) {
  input.closest(".exam-paper-sheet")?.style.setProperty("--paper-scale", `${input.value}%`);
  input.setAttribute("aria-valuetext", `${input.value}%`);
  try {
    localStorage.setItem(EXAM_PAPER_SCALE_KEY, input.value);
  } catch {}
}

// Part rows for image-based questions carry no question text, only what the paper can't show.
function renderExamPartStatus(group, part) {
  if (!group.images?.length) return "";
  if (part.offSpec) {
    return part.model || part.workedSolution
      ? `<p class="exam-part-note muted small">Not on the current course. The model answer is kept for reference.</p>`
      : `<p class="exam-part-note muted small">Not on the current course, so there is no model answer.</p>`;
  }
  if (!part.model && !part.workedSolution) return `<p class="exam-part-note muted small">Model answer under review.</p>`;
  return "";
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
  const level = group?.level === "higher" ? "HL" : group?.level === "ordinary" ? "OL" : "";
  const pieces = [year, level, paper ? `P${paper}` : section, question ? `Q${question}` : ""].filter(Boolean);
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
      status: "Previous course",
      body: "These papers (2015 to 2025) were set on the previous Biology course; the new course is first examined in 2027. Most of the content carries over. Parts on dropped topics have no model answer, and questions made up entirely of dropped topics are hidden.",
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
  const allGroups = getExamQuestionsForChapter(chapter);
  const hiddenCount = allGroups.filter(isOffSpecExamGroup).length;
  const examGroups = showOffSpecExamQuestions ? allGroups : allGroups.filter((group) => !isOffSpecExamGroup(group));
  const offSpecToggle = hiddenCount
    ? `<button type="button" class="button-secondary exam-offspec-toggle" onclick="showOffSpecExamQuestions = !showOffSpecExamQuestions; renderExamSection();">${showOffSpecExamQuestions ? "Hide" : "Show"} ${plural(hiddenCount, "question")} not on the current course</button>`
    : "";

  if (!examGroups.length) {
    const emptyMessage = examPackReady(selectedSubjectId)
      ? "No past paper questions available for this chapter yet."
      : "Loading past paper questions…";
    els.examContainer.innerHTML = (examPackReady(selectedSubjectId)
      ? `<div class="exam-empty"><p class="muted">${emptyMessage}</p></div>${offSpecToggle}`
      : skeletonHtml("rows"));
    return;
  }

  const disclaimer = getExamDisclaimer(selectedSubjectId);

  els.examContainer.innerHTML = disclaimer + examGroups.map(examGroupHtml).join("") + offSpecToggle;

  bindExamAccordions(els.examContainer);

  typesetMath(els.examContainer);
}

function examGroupHtml(group) {
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
          ${part.question ? `<p class="exam-question-text">${escapeHtml(part.question)}</p>` : ""}
          ${renderExamPartStatus(group, part)}
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
    const totalQMarks = group.totalMarks || (group.parts || []).reduce(function(s, p) { return s + (p.marks || 0); }, 0);
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
          ${renderExamPaperImages(group)}
          ${parts}
          ${appliesToBlock}
        </div>
      </div>`;
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
    : `<div class="exam-answer-text">${formatModelAnswer(part.model, group.subject)}</div>`;
  const staticMaths = isMaths && isStaticMathsSolution(part);
  const showLabel = staticMaths ? "Show worked solution" : isMaths ? "Explore worked solution" : "Show Model Answer";
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

// Rebuilt maths bank (pipeline/MATHS_REBUILD.md): steps carry KaTeX lines, shown all at once.
function isStaticMathsSolution(part) {
  return Boolean(part.workedSolution?.steps?.some((step) => Array.isArray(step.lines)));
}

function renderKatexBlock(tex, displayMode = true) {
  if (typeof katex === "undefined") return `<p>${escapeHtml(displayMode ? `$$${tex}$$` : `$${tex}$`)}</p>`;
  return katex.renderToString(tex, { displayMode, throwOnError: false, strict: "ignore" });
}

function renderStaticMathsLines(lines) {
  const html = [];
  let texRun = [];
  const flush = () => {
    if (!texRun.length) return;
    const aligned = texRun.some((tex) => tex.includes("&"));
    const body = aligned ? `\\begin{aligned}${texRun.join(" \\\\[4pt] ")}\\end{aligned}` : texRun.join(" \\\\ ");
    html.push(`<div class="maths-static-block">${renderKatexBlock(body)}</div>`);
    texRun = [];
  };
  (lines || []).forEach((line) => {
    if (line.tex) {
      texRun.push(line.tex);
    } else if (line.text) {
      flush();
      // inline $...$ is typeset by renderMathInElement once the exam list is on the page
      html.push(`<p class="maths-static-note">${escapeHtml(line.text)}</p>`);
    }
  });
  flush();
  return html.join("");
}

function renderStaticMathsSolution(part) {
  const solution = part.workedSolution;
  const steps = solution.steps.map((step, index) => `
    <section class="maths-step maths-step--static">
      <div class="maths-step-rail" aria-hidden="true">
        <span>${String(index + 1).padStart(2, "0")}</span>
        <i></i>
      </div>
      <div class="maths-step-content">
        <div class="maths-step-heading"><h5>${escapeHtml(step.title || `Step ${index + 1}`)}</h5></div>
        <div class="maths-step-work maths-step-work--katex">${renderStaticMathsLines(step.lines)}</div>
      </div>
    </section>`).join("");
  // SVGs come from our own pipeline (checked, no scripts); still refuse anything script-like.
  const svg = typeof solution.svg === "string" && /^\s*<svg[\s>]/.test(solution.svg) && !/<script|\son\w+=/i.test(solution.svg)
    ? `<figure class="maths-static-figure">${solution.svg}</figure>`
    : "";
  const finalHtml = solution.finalAnswer
    ? `<div class="maths-final-answer maths-final-answer--katex">
        <span>Answer</span>
        <div>${renderKatexBlock(solution.finalAnswer, false)}</div>
      </div>`
    : "";
  return `
    <div class="maths-worked-solution maths-worked-solution--static">
      <div class="maths-step-list">
        ${steps}
        ${svg}
        ${finalHtml}
      </div>
    </div>`;
}

function renderMathsWorkedSolution(part, solutionKey) {
  if (isStaticMathsSolution(part)) return renderStaticMathsSolution(part);
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

  typesetMath(panel);
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

function openFullNotes(outcomeId = selectedOutcomeId) {
  const chapter = getSelectedChapter();
  if (!chapter) return;
  notesOutcomeId = chapterHasSubsections(chapter) ? outcomeId : "";
  els.openLiveReading.classList.remove("hidden");
  closeLiveReader();
  renderFullNotesPage();
  els.fullNotesScreen.classList.remove("hidden");
  document.body.style.overflow = "hidden";
  pushPhoneScreen("notes");
  markNotesViewed(chapter.id);
}

// In a chapter with subsections the notes are pages: the arrows either side,
// the arrow keys and a sideways swipe step between them.
function renderFullNotesPage(step = 0) {
  const chapter = getSelectedChapter();
  const outcomes = chapterHasSubsections(chapter) ? chapter.learningOutcomes : [];
  const index = outcomes.findIndex((lo) => lo.id === notesOutcomeId);
  const outcome = outcomes[index] || null;
  const prev = outcomes[index - 1];
  const next = outcomes[index + 1];
  const heading = outcome ? compactText(outcome.title || "") : chapter.title;
  els.fullNotesTitle.innerHTML = `
    <span class="full-notes-eyebrow">Full notes${outcome ? ` · ${escapeHtml(chapter.title)} · ${index + 1} of ${outcomes.length}` : ""}</span>
    <span class="full-notes-heading">${escapeHtml(heading)}</span>`;
  els.fullNotesBody.innerHTML = buildFullNotesHtml(chapter, outcome) + (next ? `
    <button class="notes-next-section" type="button" data-notes-step="1">
      <span>Next subsection</span>
      <strong>${escapeHtml(compactText(next.title || ""))}</strong>
    </button>` : "");
  els.fullNotesBody.scrollTop = 0;

  els.fullNotesScreen.classList.toggle("is-paged", Boolean(outcome));
  [[els.fullNotesPrev, prev, "Previous"], [els.fullNotesNext, next, "Next"]].forEach(([btn, lo, label]) => {
    btn.disabled = !lo;
    btn.title = lo ? `${label}: ${compactText(lo.title || "")}` : "";
  });

  els.fullNotesBody.classList.remove("notes-enter-next", "notes-enter-prev");
  if (step) {
    void els.fullNotesBody.offsetWidth; // restart the entrance animation
    els.fullNotesBody.classList.add(step > 0 ? "notes-enter-next" : "notes-enter-prev");
  }
}

function stepFullNotes(step) {
  if (!els.fullNotesScreen.classList.contains("is-paged")) return;
  const outcomes = getSelectedChapter()?.learningOutcomes || [];
  const target = outcomes[outcomes.findIndex((lo) => lo.id === notesOutcomeId) + step];
  if (!target) return;
  closeLiveReader();
  notesOutcomeId = target.id;
  renderFullNotesPage(step);
}

function bindFullNotesPager() {
  els.fullNotesPrev.addEventListener("click", () => stepFullNotes(-1));
  els.fullNotesNext.addEventListener("click", () => stepFullNotes(1));
  els.fullNotesBody.addEventListener("click", (event) => {
    if (event.target.closest("[data-notes-step]")) stepFullNotes(1);
  });
  document.addEventListener("keydown", (event) => {
    if (els.fullNotesScreen.classList.contains("hidden") || !els.liveReader.classList.contains("hidden")) return;
    if (event.altKey || event.metaKey || event.ctrlKey || event.target.closest?.("input, textarea, select")) return;
    if (event.key === "ArrowLeft") stepFullNotes(-1);
    else if (event.key === "ArrowRight") stepFullNotes(1);
  });
  // A clearly sideways swipe pages; anything steeper is left to scrolling
  let touch = null;
  els.fullNotesBody.addEventListener("touchstart", (event) => {
    touch = event.touches.length === 1 ? { x: event.touches[0].clientX, y: event.touches[0].clientY } : null;
  }, { passive: true });
  els.fullNotesBody.addEventListener("touchend", (event) => {
    if (!touch) return;
    const dx = event.changedTouches[0].clientX - touch.x;
    const dy = event.changedTouches[0].clientY - touch.y;
    touch = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) stepFullNotes(dx < 0 ? 1 : -1);
  }, { passive: true });
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
  document.body.style.overflow = "";
  if (_fullNotesReturnToBreakdown) {
    openExamBreakdown(_fullNotesReturnToBreakdown);
    _fullNotesReturnToBreakdown = null;
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
  return getEnabledSubjects().map((subject) => subjectStats(subject, user));
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

function formatModelAnswer(rawText, subject) {
  if (!rawText) return '';
  // History answers are written one point or one paragraph per line; sentence-splitting would break paragraphs.
  if (subject === 'history') return formatAuthoredModel(rawText);

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
  const section = data?.sections?.find(function (s) { return inBreakdownSection(q, s); });
  return section ? { section, data } : null;
}

// A guide section can draw on bank sections with other ids: bank: [{ sectionId, numbers? }]
function inBreakdownSection(q, section) {
  if (!section.bank) return q.sectionId === section.id;
  return section.bank.some((b) => b.sectionId === q.sectionId && (!b.numbers || b.numbers.includes(q.questionNumber)));
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
  return `<span class="exam-section-badge" style="background:${bg};color:color-mix(in srgb, ${section.color} 62%, #1A1916);border-color:${section.color}55">${escapeHtml(section.name)}${timeStr}</span>`;
}


function openExamBreakdown(subjectId) {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data) return;
  // Coming back from a section's questions keeps that section open; a fresh open starts on the first one
  const startIdx = breakdownSelection?.subjectId === subjectId ? breakdownSelection.idx : 0;
  breakdownSelection = null;
  requestExamPack(subjectId);
  document.getElementById('examBreakdownContent').innerHTML = renderBreakdownModal(data);
  document.getElementById('examBreakdownModal').classList.remove('hidden');
  if (data.sections?.length) selectBreakdownSection(subjectId, Math.min(startIdx, data.sections.length - 1));
}

// "Section A – Short Questions" → { kicker: "Section A", title: "Short Questions" }
function splitSectionName(name) {
  const [kicker, ...rest] = String(name).split(/\s+[–-]\s+/);
  return rest.length ? { kicker, title: rest.join(' – ') } : { kicker: '', title: kicker };
}

function sectionMinutes(section, data) {
  if (section.minutes) return section.minutes;
  if (!section.marks || section.marksRange || !data.totalMarks || !data.totalMinutes) return null;
  return Math.round((section.marks / data.totalMarks) * data.totalMinutes);
}

// A section whose share changes from year to year (History's essays) carries a marksRange
function sectionMarksText(section) {
  return section.marksRange ? section.marksRange.join('–') : String(section.marks);
}

function sectionShareText(section, data) {
  if (!section.marks || !data.totalMarks) return '';
  const pct = (marks) => Math.round((marks / data.totalMarks) * 100);
  return section.marksRange
    ? `${section.marksRange.map(pct).join('–')}% of paper`
    : `${pct(section.marks)}% of paper`;
}

function renderBreakdownModal(data) {
  const subjectTitle = escapeHtml(SUBJECTS.find((s) => s.id === data.subject)?.title || data.subject);
  const head = (meta) => `
    <header class="bd-head">
      <div class="bd-head-text">
        ${guideEyebrow('paper')}
        <h2 class="bd-title">${subjectTitle}</h2>
      </div>
      ${meta}
    </header>`;

  if (data.notice) {
    return `<div class="bd-screen">
      ${head('')}
      <div class="bd-notice">
        <span class="bd-label">Notice</span>
        <p>${escapeHtml(data.notice)}</p>
      </div>
    </div>`;
  }

  // A long timingNote is a paragraph, not a stat: show the total time big and the note beneath
  const shortNote = data.timingNote && data.timingNote.length <= 30;
  const timeStr = shortNote ? data.timingNote : (data.totalMinutes ? `${Math.floor(data.totalMinutes / 60)}h ${data.totalMinutes % 60}m` : data.timingNote || '');
  // Where the note names a coursework component, that phrase opens its AAC guide
  const noteHtml = aacGuidesFor(data.subject).reduce((html, { guide, section }) => html.replace(escapeHtml(guide.title),
    `<a class="bd-note-link" href="/app/${data.subject}/#${section}">${escapeHtml(guide.title)}</a>`), escapeHtml(data.timingNote || ''));
  const longNote = data.timingNote && !shortNote && data.totalMinutes ? `<p class="bd-timing-note">${noteHtml}</p>` : '';
  const meta = `
    <dl class="bd-stats">
      ${data.totalMarks ? `<div><dt>Marks</dt><dd>${data.totalMarks}</dd></div>` : ''}
      ${timeStr ? `<div><dt>Time</dt><dd>${escapeHtml(timeStr)}</dd></div>` : ''}
      <div><dt>${data.sections.length === 1 ? 'Section' : 'Sections'}</dt><dd>${data.sections.length}</dd></div>
    </dl>`;

  return `<div class="bd-screen">
    ${head(meta)}
    ${longNote}
    ${renderExamDay(data.examDay)}
    ${renderBreakdownBar(data)}
    <div class="bd-panels">
      ${data.sections.map((s, i) => renderBreakdownPanel(data, s, i)).join('')}
    </div>
  </div>`;
}

// Proportional strip of the paper's marks, one segment per section
function renderBreakdownBar(data) {
  if (!data.sections.every((s) => s.marks)) return '';
  return `<div class="bd-bar" aria-hidden="true">
    ${data.sections.map((s, i) => `
      <button type="button" class="bd-bar-seg" style="--sec:${s.color};flex-grow:${s.marks}"
        data-idx="${i}" tabindex="-1" onclick="selectBreakdownSection('${data.subject}', ${i}); scrollGuideTo(${i})">
        <span class="bd-bar-label">${escapeHtml(splitSectionName(s.name).kicker || s.name)} · ${sectionMarksText(s)}</span>
        <span class="bd-bar-strip"></span>
      </button>`).join('')}
  </div>`;
}

function renderBreakdownPanel(data, section, idx) {
  const { kicker, title } = splitSectionName(section.name);
  const share = sectionShareText(section, data);
  // A section that is one question long would show the same time twice, so only its per-question time is kept
  const sectionMins = sectionMinutes(section, data);
  const mins = sectionMins && !(section.minutesPerQuestion && sectionMins < section.minutesPerQuestion * 1.5) ? sectionMins : null;
  const tips = section.tips;
  const body = tips
    ? `
      <div class="bd-tips">
        <div class="bd-tip">
          <span class="bd-label">Timing</span>
          <p>${tips.timing}</p>
        </div>
        <div class="bd-tip">
          <span class="bd-label">Answer structure</span>
          <p>${tips.structure}</p>
        </div>
        ${renderCommandWords(section, data)}
        ${renderQuestionTypes(section.questionTypes)}
        <div class="bd-tip bd-tip--wide">
          <span class="bd-label">Reminders</span>
          <ul class="bd-reminders">
            ${tips.reminders.map((r) => `<li>${escapeHtml(r)}</li>`).join('')}
          </ul>
        </div>
      </div>`
    : `<p class="bd-empty">Tips for this section are on the way.</p>`;

  return `
    <section class="bd-panel" style="--sec:${section.color};--i:${idx}" data-idx="${idx}"
      onclick="if (!this.classList.contains('is-open')) selectBreakdownSection('${data.subject}', ${idx})">
      <button type="button" class="bd-panel-head" aria-expanded="false">
        <span class="bd-kicker">${escapeHtml(kicker || `Part ${idx + 1}`)}</span>
        <span class="bd-panel-title">${escapeHtml(title)}</span>
        ${section.marks ? `
          <span class="bd-marks${section.marksRange ? ' bd-marks--range' : ''}"><strong>${sectionMarksText(section)}</strong> marks</span>
          <span class="bd-facts">${[share, mins && `~${mins} min`, section.minutesPerQuestion && `${section.minutesPerQuestion} min per question`].filter(Boolean).join(' · ')}</span>` : ''}
      </button>
      <span class="bd-panel-cue" aria-hidden="true">${section.questionTypes ? `${section.questionTypes.length} question types · ` : tips ? `${tips.reminders.length} reminders · ` : ''}Click to open</span>
      <div class="bd-panel-body">
        ${body}
        <div class="bd-questions" data-questions-slot></div>
      </div>
    </section>`;
}

// The exam morning as a timeline. Wide: one bar drawn to scale (each block's width is exactly its
// share of the minutes) with the blocks' text in even columns beneath. Narrow: the blocks run down
// the page with their own bars, heights scaled by minutes (see .bd-day in styles.css).
function renderExamDay(day) {
  if (!day) return '';
  const tl = day.timeline || [];
  const bar = (b) => `<span class="bd-tl-bar">${(b.split || [{ minutes: b.minutes }]).map((x) => `<span style="flex-grow:${x.minutes}">${x.label ? `${escapeHtml(x.label)} ${x.minutes}′` : ''}</span>`).join('')}</span>`;
  return `<section class="aac-brief bd-day" aria-label="Time breakdown">
    <div class="aac-brief-main">
      <span class="bd-label">Time breakdown</span>
      <p class="aac-brief-task">${escapeHtml(day.task)}</p>
    </div>
    <div class="bd-tl-scale" aria-hidden="true" style="grid-template-columns:${tl.map((b) => `${b.minutes}fr`).join(' ')}">
      ${tl.map((b) => `<span style="--c:${b.color}">${bar(b)}</span>`).join('')}
    </div>
    <ol class="bd-timeline" style="grid-template-columns:repeat(${tl.length}, minmax(0, 1fr))">
      ${tl.map((b, i) => `
      <li class="bd-tl-block" style="--c:${b.color};--m:${b.minutes}">
        <span class="bd-tl-time">${escapeHtml(b.start)}${i === tl.length - 1 && day.end ? `<span>${escapeHtml(day.end)}</span>` : ''}</span>
        ${bar(b)}
        <strong class="bd-tl-label">${escapeHtml(b.label)}</strong>
        <span class="bd-tl-mins">${b.minutes} min</span>
        <p class="bd-tl-detail">${escapeHtml(b.detail)}</p>
      </li>`).join('')}
    </ol>
  </section>
  ${day.facts?.length ? `<section class="aac-brief bd-day bd-rules" aria-label="Key rules">
    <span class="bd-label">Key rules</span>
    <dl class="aac-brief-facts">${day.facts.map(([k, v]) => `<div><dt>${escapeHtml(k)}</dt><dd>${escapeHtml(v)}</dd></div>`).join('')}</dl>
  </section>` : ''}`;
}

// One collapsible row per kind of question in a section: what it looks like, how it's marked, how to play it
function renderQuestionTypes(types) {
  if (!types?.length) return '';
  const rows = [['Where it comes up', 'where'], ["What you'll see", 'see'], ['How it’s marked', 'marked'], ['How to answer', 'play']];
  return `<div class="bd-tip bd-tip--wide bd-types">
    <span class="bd-label">Question types · ${types.length}</span>
    ${types.map((t, i) => `
      <details class="bd-type"${i === 0 ? ' open' : ''}>
        <summary>
          <span class="bd-type-name">${escapeHtml(t.name)}</span>
          <span class="aac-depth-count">${[t.marks && (typeof t.marks === 'number' ? `${t.marks} marks` : t.marks), t.minutes && `~${t.minutes} min`].filter(Boolean).join(' · ')}</span>
        </summary>
        <dl class="aac-brief-facts">${rows.filter(([, k]) => t[k]).map(([label, k]) => `<div><dt>${label}</dt><dd>${escapeHtml(t[k])}</dd></div>`).join('')}</dl>
        ${t.traps?.length ? `<span class="bd-label bd-type-traps">Where marks are lost</span>
        <ul class="bd-reminders">${t.traps.map((x) => `<li>${escapeHtml(x)}</li>`).join('')}</ul>` : ''}
      </details>`).join('')}
  </div>`;
}

function selectBreakdownSection(subjectId, idx) {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data?.sections?.[idx]) return;
  breakdownSelection = { subjectId, idx };

  const modal = document.getElementById('examBreakdownModal');
  modal.querySelectorAll('.bd-panel').forEach((el) => {
    const open = Number(el.dataset.idx) === idx;
    el.classList.toggle('is-open', open);
    el.querySelector('.bd-panel-head').setAttribute('aria-expanded', String(open));
  });
  modal.querySelectorAll('.bd-bar-seg').forEach((el) => {
    el.classList.toggle('is-open', Number(el.dataset.idx) === idx);
  });

  // Question counts arrive with the exam pack, so every panel's button is refreshed together
  const packReady = examPackReady(subjectId);
  modal.querySelectorAll('[data-questions-slot]').forEach((slot) => {
    const i = Number(slot.closest('.bd-panel').dataset.idx);
    const questions = sectionQuestions(data.sections[i]);
    slot.innerHTML = questions.length
      ? `${renderChapterFrequency(questions, subjectId, i)}
         <button class="bd-questions-btn" type="button" onclick="openSectionQuestions('${subjectId}',${i})">
           Practise past-paper questions <span>${questions.length}</span>
         </button>`
      : `<p class="bd-empty">${packReady ? 'No past-paper questions indexed for this section yet.' : 'Loading past-paper questions…'}</p>`;
  });
}

// The instruction words this section's questions open with, counted from the past papers
// (pipeline/command_words.py), at the student's level, Higher until they've picked one
function renderCommandWords(section, data) {
  const byLevel = section.commandWords;
  if (!byLevel) return '';
  const chosen = getCurrentUser()?.onboarding?.levels?.[data.subject];
  const level = byLevel[chosen] ? chosen : byLevel.higher ? 'higher' : Object.keys(byLevel)[0];
  const words = byLevel[level] || [];
  if (!words.length) return '';
  return `<div class="bd-tip bd-tip--wide">
    <span class="bd-label">How the questions ask · ${level === 'higher' ? 'Higher' : 'Ordinary'} Level, ${escapeHtml(data.commandWordYears || '')} papers</span>
    <ul class="bd-words">${words.map(([w, n]) => `<li><strong>${escapeHtml(w)}</strong><span>${n}×</span></li>`).join('')}</ul>
  </div>`;
}

function sectionQuestions(section) {
  return (window.EXAM_QUESTIONS_DB || []).filter(q => inBreakdownSection(q, section) && !isOffSpecExamGroup(q) && !hiddenByMathsPilot(q) && !hiddenByUserLevel(q));
}

// Which chapters a section's questions have come from, as "in X of Y papers" (a paper is one year at one
// level). Each row opens that chapter's past questions. Empty for banks without chapter tags.
function renderChapterFrequency(questions, subjectId, sectionIdx) {
  const paperOf = (q) => `${q.year}-${examGroupLevel(q)}`;
  const papers = new Set(questions.map(paperOf));
  const byChapter = new Map();
  questions.forEach((q) => {
    if (!q.chapterId) return;
    if (!byChapter.has(q.chapterId)) byChapter.set(q.chapterId, new Set());
    byChapter.get(q.chapterId).add(paperOf(q));
  });
  if (papers.size < 2 || !byChapter.size) return '';
  const chapters = SUBJECTS.find((s) => s.id === subjectId)?.chapters || [];
  // "3. Rocks, Weathering and Mass Movement — …" reads as "Rocks, Weathering and Mass Movement"
  const nameOf = (id) => (chapters.find((c) => c.id === id)?.title || id).replace(/^\d+\.\s*/, '').split(' — ')[0];
  const rows = [...byChapter].sort((a, b) => b[1].size - a[1].size).map(([id, seen]) => `
    <li><button type="button" onclick="openSectionQuestions('${subjectId}',${sectionIdx},'${escapeHtml(id)}')">
      <span class="bd-ch-name">${escapeHtml(nameOf(id))}</span>
      <span class="bd-ch-bar" aria-hidden="true"><span style="width:${(seen.size / papers.size) * 100}%"></span></span>
      <span class="bd-ch-count">${seen.size}/${papers.size}</span>
    </button></li>`).join('');
  return `<div class="bd-chapters">
    <span class="bd-label">Chapters that come up · in how many of the last ${papers.size} papers</span>
    <ul>${rows}</ul>
  </div>`;
}

function openSectionQuestions(subjectId, sectionIdx, chapterId = '') {
  const data = window.EXAM_BREAKDOWN?.[subjectId];
  if (!data) return;
  const section = data.sections[sectionIdx];

  const questions = sectionQuestions(section).filter((q) => !chapterId || q.chapterId === chapterId);

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
          ${part.question ? `<p class="exam-question-text">${escapeHtml(part.question)}</p>` : ''}
          ${diagramHtml}
          ${renderExamPartStatus(group, part)}
          ${renderExamAnswer(group, part, partId)}
        </div>`;
    }).join('');

    const totalMarks = group.totalMarks || (group.parts || []).reduce((sum, part) => sum + (part.marks || 0), 0);
    const bodyId = `breakdown-exam-body-${qi}`;

    return `
      <div class="exam-group">
        <button class="exam-group-header" type="button" data-exam-toggle aria-expanded="false" aria-controls="${bodyId}" title="${escapeHtml(group.source || group.id)}">
          <span class="exam-source-tag">${escapeHtml(compactExamSource(group))}</span>
          <span class="exam-group-meta">${totalMarks ? `${totalMarks} marks` : ""}${group.parts?.length > 1 ? ` · ${group.parts.length} parts` : ""}</span>
          <span class="exam-group-chevron" aria-hidden="true">⌄</span>
        </button>
        <div class="exam-group-body hidden" id="${bodyId}">${renderExamPaperImages(group)}${parts}</div>
      </div>`;
  }).join('');

  // Hide the breakdown modal so the full-screen questions view is unobstructed
  document.getElementById('examBreakdownModal').classList.add('hidden');
  _fullNotesReturnToBreakdown = subjectId;

  // Populate and open the full-notes screen (true full-screen overlay)
  const chapterTitle = chapterId && SUBJECTS.find((s) => s.id === subjectId)?.chapters.find((c) => c.id === chapterId)?.title.replace(/^\d+\.\s*/, '').split(' — ')[0];
  document.getElementById('fullNotesTitle').textContent = `${section.name}${chapterTitle ? ` · ${chapterTitle}` : ''}: Practice questions`;
  els.fullNotesScreen.classList.remove('is-paged');
  closeLiveReader();
  els.openLiveReading.classList.add('hidden');
  document.getElementById('fullNotesBody').innerHTML = `<div class="exam-container exam-container--fullscreen">${questionsHtml}</div>`;
  bindExamAccordions(document.getElementById('fullNotesBody'));
  els.fullNotesScreen.classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  typesetMath(els.fullNotesScreen);
}

// ── AAC guides ──────────────────────────────────────────────
// Same modal, panels and strip as the Paper guide; data in aac-guides.js. Ticks are per browser.
const AAC_STAGE_COLORS = ['#3B82F6', '#14B8A6', '#F59E0B', '#F97316', '#EF4444', '#0EA5E9', '#64748B'];
const AAC_TICKS_KEY = 'aacTicks';

function readAacTicks() {
  try { return JSON.parse(localStorage.getItem(AAC_TICKS_KEY) || '{}') || {}; } catch { return {}; }
}

function aacTickCount(guide, ticks, key) {
  const done = new Set(ticks[key] || []);
  const all = guide.stages.flatMap((s) => s.checklist);
  return { done: all.filter((t) => done.has(t)).length, total: all.length };
}

function toggleAacTick(input) {
  const { key, text } = input.dataset;
  const ticks = readAacTicks();
  const set = new Set(ticks[key] || []);
  if (input.checked) set.add(text); else set.delete(text);
  ticks[key] = [...set];
  try { localStorage.setItem(AAC_TICKS_KEY, JSON.stringify(ticks)); } catch {}
  const { done, total } = aacTickCount(window.AAC_GUIDES[key], ticks, key);
  const out = document.getElementById('aacProgress');
  if (out) out.textContent = `${done}/${total}`;
}

// Eyebrow of both guide screens; each guide is its own section, so this is a label, not a switch
function guideEyebrow(active, aacTitle = '') {
  return `<span class="bd-eyebrow">${active === 'aac' ? `AAC guide · ${escapeHtml(aacTitle)}` : 'Paper guide'}</span>`;
}

function openAacGuide(subjectId, section = 'aac') {
  const found = aacGuidesFor(subjectId).find((a) => a.section === section);
  if (!found) return;
  document.getElementById('examBreakdownContent').innerHTML = renderAacGuide(found.guide, found.key);
  document.getElementById('examBreakdownModal').classList.remove('hidden');
  selectAacStage(0);
}

// Tapping a slice of the marks bar opens that section below it: bring it into view
function scrollGuideTo(idx) {
  document.querySelectorAll('#examBreakdownModal .bd-panel')[idx]?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function selectAacStage(idx) {
  const modal = document.getElementById('examBreakdownModal');
  modal.querySelectorAll('.bd-panel').forEach((el) => {
    const open = Number(el.dataset.idx) === idx;
    el.classList.toggle('is-open', open);
    el.querySelector('.bd-panel-head').setAttribute('aria-expanded', String(open));
  });
  modal.querySelectorAll('.bd-bar-seg').forEach((el) => el.classList.toggle('is-open', Number(el.dataset.idx) === idx));
}

// The year's task as the SEC sets it: topic or assignments, what to submit, and the due date
function renderAacBrief(brief) {
  if (!brief) return '';
  return `<section class="aac-brief" aria-label="The 2027 brief">
    <div class="aac-brief-main">
      <span class="bd-label">The 2027 brief</span>
      <p class="aac-brief-task">${escapeHtml(brief.task)}</p>
      ${brief.list ? `<ol class="aac-brief-list">${brief.list.map((t) => `<li>${escapeHtml(t)}</li>`).join('')}</ol>` : ''}
      <a class="aac-brief-source" href="${escapeHtml(brief.source.url)}" target="_blank" rel="noopener">${escapeHtml(brief.source.label)} ↗</a>
    </div>
    <dl class="aac-brief-facts">${brief.facts.map(([k, v]) => `<div><dt>${escapeHtml(k)}</dt><dd>${escapeHtml(v)}</dd></div>`).join('')}</dl>
  </section>`;
}

function renderAacGuide(guide, key) {
  const ticks = readAacTicks();
  const done = new Set(ticks[key] || []);
  const { done: doneCount, total } = aacTickCount(guide, ticks, key);
  const byMarks = guide.stages.every((s) => s.marks);
  const color = (i) => AAC_STAGE_COLORS[i % AAC_STAGE_COLORS.length];

  const bar = `<div class="bd-bar" aria-hidden="true">${guide.stages.map((s, i) => `
      <button type="button" class="bd-bar-seg" style="--sec:${color(i)};flex-grow:${byMarks ? s.marks : 1}"
        data-idx="${i}" tabindex="-1" onclick="selectAacStage(${i}); scrollGuideTo(${i})">
        <span class="bd-bar-label">${escapeHtml(splitSectionName(s.name).kicker || s.name)}${s.marks ? ` · ${s.marks}` : ''}</span>
        <span class="bd-bar-strip"></span>
      </button>`).join('')}</div>`;

  const panels = guide.stages.map((s, i) => {
    const { kicker, title } = splitSectionName(s.name);
    const depth = s.guide.reduce((n, g) => n + g.points.length, 0);
    const last = i === guide.stages.length - 1;
    return `
    <section class="bd-panel" style="--sec:${color(i)};--i:${i}" data-idx="${i}"
      onclick="if (!this.classList.contains('is-open')) selectAacStage(${i})">
      <button type="button" class="bd-panel-head" aria-expanded="false">
        <span class="bd-kicker">${escapeHtml(kicker || `Stage ${i + 1}`)}</span>
        <span class="bd-panel-title">${escapeHtml(title)}</span>
        ${s.marks ? `<span class="bd-marks"><strong>${s.marks}</strong> marks</span>` : ''}
        <span class="bd-facts">${s.checklist.length} step${s.checklist.length === 1 ? '' : 's'}${s.marksNote ? ` · ${escapeHtml(s.marksNote)}` : ''}</span>
      </button>
      <span class="bd-panel-cue" aria-hidden="true">${s.checklist.length} steps · Click to open</span>
      <div class="bd-panel-body">
        <div class="bd-tip aac-checklist">
          <span class="bd-label">Full-marks checklist</span>
          <ul class="aac-checks">${s.checklist.map((t) => `
            <li><label><input type="checkbox" data-key="${key}" data-text="${escapeHtml(t)}"
              ${done.has(t) ? 'checked' : ''} onchange="toggleAacTick(this)"><span>${escapeHtml(t)}</span></label></li>`).join('')}
          </ul>
        </div>
        <details class="bd-tip aac-depth">
          <summary><span class="bd-label">Full guide</span><span class="aac-depth-count">${depth} points</span></summary>
          ${s.guide.map((g) => `
            <h4 class="aac-h">${escapeHtml(g.h)}</h4>
            <ul class="bd-reminders aac-points">${g.points.map((p) => `<li>${escapeHtml(p)}</li>`).join('')}</ul>`).join('')}
        </details>
        ${last ? `
        <div class="bd-tip aac-sources">
          <span class="bd-label">Pooled from ${guide.sources.length} sources</span>
          <ul>${guide.sources.map((src) => `<li><a href="${escapeHtml(src.url)}" target="_blank" rel="noopener">${escapeHtml(src.label)}</a></li>`).join('')}</ul>
        </div>` : ''}
      </div>
    </section>`;
  }).join('');

  return `<div class="bd-screen aac-screen">
    <header class="bd-head">
      <div class="bd-head-text">
        ${guideEyebrow('aac', guide.title)}
        <h2 class="bd-title">${escapeHtml(guide.subjectTitle)}</h2>
      </div>
      <dl class="bd-stats">
        <div><dt>Of your grade</dt><dd>${escapeHtml(guide.weight)}</dd></div>
        <div><dt>Level</dt><dd>${escapeHtml(guide.level)}</dd></div>
        <div><dt>Checklist</dt><dd id="aacProgress">${doneCount}/${total}</dd></div>
      </dl>
    </header>
    <p class="bd-timing-note">${escapeHtml(guide.summary)}</p>
    ${renderAacBrief(guide.brief)}
    <a class="aac-ai-guide" href="./aac-ai-guides/${key}.pdf" download="${escapeHtml(guide.title)} AI review guide.pdf">
      <span class="bd-label">AI review guide · PDF</span>
      <span>Attach it with your draft to ChatGPT, Claude or Gemini. It leaves your writing as it is and shows how each paragraph could earn more marks, and why.</span>
      <span class="aac-ai-logos" aria-hidden="true"><img src="images/openai.svg" alt="" /><img src="images/claude.svg" alt="" /></span>
    </a>
    ${bar}
    <div class="bd-panels">${panels}</div>
  </div>`;
}

// ── Startup ───────────────────────────────────
// Last in the file so every declaration above exists before the first render:
// a subject page can open straight onto any section (#tests, #guide…).
bindEvents();
if (PAGE_SUBJECT) {
  window.addEventListener("hashchange", enterSection);
  enterSection();
} else {
  renderAll();
}
if (isLocalOnboardingPreview) {
  showOnboarding(getCurrentUser());
} else if (isLocalTestPreview) {
  if (!PAGE_SUBJECT) switchTab("test");
} else if (!isLocalMathsPreview) {
  initializeAccounts();
  startUsageTracking();
}
