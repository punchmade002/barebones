const storageKey = "bare-bones-app-v4";
const AVATAR_COLORS = ["#ff4d4d", "#ff8a00", "#ffd400", "#63e000", "#00d084", "#00c2ff", "#2f6bff", "#8e44ff", "#ff4fd8", "#ff6b9a"];
let APPROVED_USERNAMES = ["gabriel", "whatever"];

async function loadApprovedUsernames() {
  try {
    const res = await fetch(`./approved_usernames.txt?ts=${Date.now()}`, { cache: "no-store" });
    if (!res.ok) return;
    const text = await res.text();
    const names = text
      .split(/\r?\n/)
      .map((l) => l.trim().toLowerCase())
      .filter((l) => l && !l.startsWith("#"));
    if (names.length) APPROVED_USERNAMES = names;
  } catch (err) {
    // Keep fallback list if file is unreachable.
  }
}
loadApprovedUsernames();

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
  return filtered.map((chapter) => ({
    id: chapter.id,
    title: `${chapter.number}. ${chapter.title}`,
    learningOutcomes: [
      {
        id: `${chapter.id}-core`,
        code: `${chapter.number}.0`,
        title: "Core Concepts",
        keyTerms: ensureMinimumConcepts(
          (chapter.learningOutcomes || []).flatMap((lo, loIndex) =>
            (lo.notes || []).map((note, idx) => ({
              term: note.h || `${lo.title} ${idx + 1}`,
              definition: note.b || "",
              section: lo.title || `Section ${loIndex + 1}`,
            }))
          ),
          chapter
        ),
      },
    ],
  }));
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
];

const SUBJECT_PROMPT_STYLES = {
  business: [
    (t) => `Explain ${t} in business terms.`,
    (t) => `State what ${t} means and why it matters to a firm.`,
    (t) => `Define ${t} and outline its impact on a business.`,
    (t) => `Outline the key idea behind ${t} and give a business application.`,
    (t) => `Describe ${t} with a business-focused explanation.`,
  ],
  pe: [
    (t) => `Explain ${t} in the context of physical education.`,
    (t) => `State what ${t} means and its relevance to athletic performance.`,
    (t) => `Describe ${t} and how it applies to sport or training.`,
    (t) => `Outline ${t} and explain how a coach or athlete would apply it.`,
    (t) => `Define ${t} in sport science terms.`,
  ],
  biology: [
    (t) => `Explain ${t} in biological terms.`,
    (t) => `State what ${t} means and its role in a biological process.`,
    (t) => `Define ${t} and describe its function in living organisms.`,
    (t) => `Outline ${t} and explain how it operates in the body or cell.`,
    (t) => `State the biological significance of ${t}.`,
  ],
};

const SUBJECT_FALLBACK_QUESTION = {
  business: (term) => `Explain "${term}" and give one simple business example.`,
  pe: (term) => `Explain "${term}" and give one example from sport or physical activity.`,
  biology: (term) => `Explain "${term}" and describe its role in a biological context.`,
};

const els = {
  authPanel: document.getElementById("authPanel"),
  accountName: document.getElementById("accountName"),
  avatarLabel: document.getElementById("avatarLabel"),
  avatarPicker: document.getElementById("avatarPicker"),
  themePicker: document.getElementById("themePicker"),
  openProgress: document.getElementById("openProgress"),
  closeProgress: document.getElementById("closeProgress"),
  progressScreen: document.getElementById("progressScreen"),
  progressBody: document.getElementById("progressBody"),
  profileAvatar: document.getElementById("profileAvatar"),
  profileLevel: document.getElementById("profileLevel"),
  subjectPicker: document.getElementById("subjectPicker"),
  profileMenu: document.getElementById("profileMenu"),
  accountSwitcher: document.getElementById("accountSwitcher"),
  openAuthButton: document.getElementById("openAuthButton"),
  signOutButton: document.getElementById("signOutButton"),
  saveAccount: document.getElementById("saveAccount"),
  accountStatus: document.getElementById("accountStatus"),
  subjectGraph: document.getElementById("subjectGraph"),
  subjectWorkbench: document.getElementById("subjectWorkbench"),
  flashcardList: document.getElementById("flashcardList"),
  flashcardStudy: document.getElementById("flashcardStudy"),
  openFullNotes: document.getElementById("openFullNotes"),
  fullNotesScreen: document.getElementById("fullNotesScreen"),
  fullNotesTitle: document.getElementById("fullNotesTitle"),
  fullNotesBody: document.getElementById("fullNotesBody"),
  closeFullNotes: document.getElementById("closeFullNotes"),
  hierarchyPanel: document.getElementById("hierarchyPanel"),
  startTest: document.getElementById("startTest"),
  testContainer: document.getElementById("testContainer"),
  tabs: Array.from(document.querySelectorAll(".tab")),
  flashcardsTab: document.getElementById("flashcardsTab"),
  testTab: document.getElementById("testTab"),
  examTab: document.getElementById("examTab"),
  examContainer: document.getElementById("examContainer"),
};

let state = loadState();
let selectedAvatarColor = AVATAR_COLORS[0];
let expandedSubjectId = SUBJECTS[0].id;
let selectedSubjectId = SUBJECTS[0].id;
let selectedChapterId = SUBJECTS[0].chapters[0].id;
let selectedOutcomeId = SUBJECTS[0].chapters[0].learningOutcomes[0].id;
let studyIndex = 0;
let showAnswer = false;

bindEvents();
renderAll();

function bindEvents() {
  renderAvatarPicker();
  els.openAuthButton.addEventListener("click", () => {
    els.authPanel.classList.toggle("hidden");
    els.profileMenu.classList.add("hidden");
  });
  els.saveAccount.addEventListener("click", async () => {
    const name = els.accountName.value.trim();
    if (!name) {
      els.accountStatus.textContent = "Enter a username.";
      return;
    }
    await loadApprovedUsernames();
    if (!APPROVED_USERNAMES.includes(name.toLowerCase())) {
      els.accountStatus.textContent = "Username not approved. Contact the site owner for access.";
      return;
    }

    if (!state.usersByName[name]) {
      state.usersByName[name] = {
        username: name,
        avatarColor: selectedAvatarColor,
        testsCompleted: 0,
        viewedNotesByChapter: {},
        progressByOutcome: {},
        learnedByOutcome: {},
        subjects: SUBJECTS.map((s) => s.id),
      };
    }
    state.session.currentUser = name;
    persist();
    renderAll();
    els.accountStatus.textContent = `Welcome, ${name}.`;
  });
  els.startTest.addEventListener("click", startTest);
  els.openFullNotes.addEventListener("click", openFullNotes);
  els.closeFullNotes.addEventListener("click", closeFullNotes);
  els.openProgress.addEventListener("click", openProgress);
  els.closeProgress.addEventListener("click", closeProgress);
  els.tabs.forEach((tab) => tab.addEventListener("click", () => switchTab(tab.dataset.tab)));
  els.profileAvatar.addEventListener("click", () => {
    if (!getCurrentUser()) return;
    els.profileMenu.classList.toggle("hidden");
    renderAccountSwitcher();
  });
  els.signOutButton.addEventListener("click", () => {
    state.session.currentUser = "";
    els.profileMenu.classList.add("hidden");
    persist();
    renderAll();
    els.accountStatus.textContent = "Signed out.";
  });
  els.accountSwitcher.addEventListener("change", () => {
    const username = els.accountSwitcher.value;
    if (!username) return;
    state.session.currentUser = username;
    persist();
    renderAll();
    els.profileMenu.classList.add("hidden");
  });
  document.addEventListener("click", (event) => {
    const target = event.target;
    if (
      target !== els.profileAvatar &&
      !els.profileMenu.contains(target) &&
      !els.profileMenu.classList.contains("hidden")
    ) {
      els.profileMenu.classList.add("hidden");
    }
  });
}

function switchTab(tab) {
  els.tabs.forEach((btn) => btn.classList.toggle("active", btn.dataset.tab === tab));
  els.flashcardsTab.classList.toggle("active", tab === "flashcards");
  els.testTab.classList.toggle("active", tab === "test");
  els.examTab.classList.toggle("active", tab === "exam");
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
    expandedSubjectId = first.id;
  }
}

function renderAll() {
  reconcileSelection();
  renderAccount();
  renderProfileAvatar();
  renderAccountSwitcher();
  renderAvatarPicker();
  renderSubjectPicker();
  renderGraph();
  renderOutcomes();
  renderTestOverview();
  if (els.examTab?.classList.contains("active")) renderExamSection();
}

function getEnabledSubjectIds(user) {
  if (!user) return SUBJECTS.map((s) => s.id);
  if (!Array.isArray(user.subjects)) return SUBJECTS.map((s) => s.id);
  return user.subjects.length ? user.subjects : SUBJECTS.map((s) => s.id);
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
  const enabled = new Set(getEnabledSubjectIds(user));
  els.subjectPicker.innerHTML = SUBJECTS.map(
    (s) => `
      <label>
        <input type="checkbox" data-subject="${escapeHtml(s.id)}" ${enabled.has(s.id) ? "checked" : ""} />
        <span>${escapeHtml(s.title)}</span>
      </label>`
  ).join("");
  els.subjectPicker.querySelectorAll("input[type=checkbox]").forEach((cb) => {
    cb.addEventListener("change", () => {
      const u = getCurrentUser();
      if (!u) return;
      const ids = Array.from(
        els.subjectPicker.querySelectorAll("input[type=checkbox]:checked")
      ).map((el) => el.dataset.subject);
      u.subjects = ids.length ? ids : SUBJECTS.map((s) => s.id);
      if (!u.subjects.includes(selectedSubjectId)) {
        const first = SUBJECTS.find((s) => u.subjects.includes(s.id));
        if (first) {
          selectedSubjectId = first.id;
          selectedChapterId = first.chapters[0]?.id || "";
          selectedOutcomeId = first.chapters[0]?.learningOutcomes[0]?.id || "";
          expandedSubjectId = first.id;
        }
      }
      persist();
      renderAll();
    });
  });
}

function renderAccount() {
  const current = getCurrentUser();
  const isLoggedIn = Boolean(current);
  els.accountName.value = "";
  els.authPanel.classList.toggle("hidden", isLoggedIn);
  if (isLoggedIn) {
    els.accountStatus.textContent = `${current.username} logged in. Tests completed: ${current.testsCompleted || 0}`;
  } else if (!els.accountStatus.textContent || els.accountStatus.textContent.includes("logged in")) {
    els.accountStatus.textContent = "Create account or log in.";
  }
}

function renderAccountSwitcher() {
  const usernames = Object.keys(state.usersByName).sort();
  els.accountSwitcher.innerHTML = usernames.map((name) => `<option value="${escapeHtml(name)}">${escapeHtml(name)}</option>`).join("");
  if (!usernames.length) {
    els.accountSwitcher.innerHTML = "<option value=''>No accounts yet</option>";
    return;
  }
  els.accountSwitcher.value = state.session.currentUser || usernames[0];
}

function renderAvatarPicker() {
  [els.avatarPicker, els.themePicker].forEach((host) => {
    if (!host) return;
    host.innerHTML = "";
    AVATAR_COLORS.forEach((color) => {
      const swatch = document.createElement("button");
      swatch.type = "button";
      const activeColor = getCurrentUser()?.avatarColor || selectedAvatarColor;
      swatch.className = `avatar-option${activeColor === color ? " selected" : ""}`;
      swatch.style.background = color;
      swatch.ariaLabel = `Select ${color} theme colour`;
      swatch.addEventListener("click", () => {
        const current = getCurrentUser();
        if (current) {
          current.avatarColor = color;
        } else {
          selectedAvatarColor = color;
        }
        persist();
        renderAvatarPicker();
        renderProfileAvatar();
      });
      host.appendChild(swatch);
    });
  });
}

function renderProfileAvatar() {
  if (!els.profileAvatar) return;
  const current = getCurrentUser();
  const color = current?.avatarColor || selectedAvatarColor || AVATAR_COLORS[0];
  els.profileAvatar.style.background = color;
  els.profileAvatar.title = current ? `${current.username}'s profile` : "Profile picture";
  els.profileAvatar.disabled = !current;
  if (!current) els.profileMenu.classList.add("hidden");
  applyAccentColor(current ? color : "#f97316");
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
  let earned = 0;
  let total = 0;
  const enabledIds = getEnabledSubjectIds(user);
  SUBJECTS.filter((s) => enabledIds.includes(s.id)).forEach((subject) => {
    (subject.chapters || []).forEach((ch) => {
      (ch.learningOutcomes || []).forEach((lo) => {
        const concepts = (lo.keyTerms || []).length;
        total += concepts;
        if ((progress[lo.id] || 0) >= 1) earned += concepts;
      });
    });
  });
  const percent = total ? Math.round((earned / total) * 100) : 0;
  return { earned, total, percent };
}

function applyAccentColor(hex) {
  const root = document.documentElement;
  const hsl = hexToHsl(hex);
  if (!hsl) return;
  const { h, s } = hsl;
  const sat = Math.max(60, Math.min(s, 90));
  const isYellow = h >= 40 && h <= 70;
  const accentL = isYellow ? 44 : 50;
  const accent2L = isYellow ? 56 : 62;
  const inkL = isYellow ? 22 : 18;
  const strongL = isYellow ? 24 : 28;
  const set = (name, l, sOverride) =>
    root.style.setProperty(name, `hsl(${h} ${sOverride ?? sat}% ${l}%)`);
  set("--accent", accentL);
  set("--accent-2", accent2L);
  set("--accent-strong", strongL);
  set("--accent-ink", inkL, Math.max(70, sat));
  set("--accent-edge", 70);
  set("--accent-soft", 84);
  set("--accent-softer", 94);
  set("--accent-bg", 97);
  set("--highlight-orange", 70, Math.max(70, sat));
  set("--highlight-orange-soft", 88, Math.max(60, sat));
}

function hexToHsl(hex) {
  const m = String(hex || "").trim().match(/^#?([a-f0-9]{6}|[a-f0-9]{3})$/i);
  if (!m) return null;
  let h = m[1];
  if (h.length === 3) h = h.split("").map((c) => c + c).join("");
  const r = parseInt(h.slice(0, 2), 16) / 255;
  const g = parseInt(h.slice(2, 4), 16) / 255;
  const b = parseInt(h.slice(4, 6), 16) / 255;
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  const l = (max + min) / 2;
  let s = 0;
  let hue = 0;
  if (max !== min) {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    switch (max) {
      case r: hue = (g - b) / d + (g < b ? 6 : 0); break;
      case g: hue = (b - r) / d + 2; break;
      default: hue = (r - g) / d + 4;
    }
    hue *= 60;
  }
  return { h: Math.round(hue), s: Math.round(s * 100), l: Math.round(l * 100) };
}

function renderGraph() {
  els.subjectGraph.innerHTML = "";
  getEnabledSubjects().forEach((subject) => {
    const block = document.createElement("div");
    block.className = "graph-subject";
    block.innerHTML = `
      <button class="graph-subject-main button-primary">${escapeHtml(subject.title)}</button>
      <div class="graph-chapters ${expandedSubjectId === subject.id ? "" : "hidden"}"></div>
    `;
    block.querySelector(".graph-subject-main").addEventListener("click", () => {
      expandedSubjectId = expandedSubjectId === subject.id ? "" : subject.id;
      renderGraph();
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
        studyIndex = 0;
        showAnswer = false;
        renderAll();
      });
      chaptersWrap.appendChild(chapterButton);
    });
    els.subjectGraph.appendChild(block);
  });
  els.subjectWorkbench.classList.toggle("hidden", !getCurrentUser());
}

function renderOutcomes() {
  const chapter = getSelectedChapter();
  const outcome = getSelectedOutcome();
  if (!chapter || !outcome) return;

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
  const step = getProgressByOutcome()[outcome.id] || 0;
  const pct = Math.round((step / 3) * 100);
  const learnedSet = new Set(getLearnedByOutcome()[outcome.id] || []);
  const learnedCount = learnedSet.size;

  els.flashcardStudy.innerHTML = `
    <p class="muted small">${escapeHtml(chapter.title)}</p>
    <p class="muted small">${allPoints.length} concept points</p>
    <div class="progress-bar"><span style="width:${pct}%"></span></div>
    <p class="muted small">Learned cards: ${learnedCount}/${cards.length}</p>
    <p class="muted small">Goal progress: ${step}/3</p>
    <div class="study-face">${showAnswer ? escapeHtml(card.definition) : `<strong>${escapeHtml(card.term)}</strong>`}</div>
    <div class="study-controls">
      <button id="prevCard" class="button-secondary">Prev</button>
      <button id="flipCard" class="button-primary">${showAnswer ? "Show Term" : "Show Point"}</button>
      <button id="nextCard" class="button-secondary">Next</button>
      <button id="markLearned" class="button-secondary">${learnedSet.has(card.id) ? "Learned" : "Mark Learned"}</button>
    </div>
    ${renderKeywordRow(card.keywords)}
    <p class="muted small">Include these key words in your test answer to earn bonus marks.</p>
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
  document.getElementById("markLearned").addEventListener("click", () => {
    const learnedByOutcome = getLearnedByOutcome();
    if (!learnedByOutcome[outcome.id]) learnedByOutcome[outcome.id] = [];
    const set = new Set(learnedByOutcome[outcome.id]);
    set.add(card.id);
    learnedByOutcome[outcome.id] = Array.from(set);
    persist();
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

function startTest() {
  if (!getCurrentUser()) {
    els.testContainer.innerHTML = "<p class='muted'>Log in to track tests and progress.</p>";
    return;
  }
  const chapter = getSelectedChapter();
  const outcome = getSelectedOutcome();
  if (!outcome) return;
  const pool = questionsForChapter(chapter);
  const sample = shuffleArray(pool).slice(0, 3);

  els.testContainer.innerHTML = "";
  sample.forEach((card, idx) => {
    const div = document.createElement("div");
    div.className = "test-card";
    div.innerHTML = `
      <p><strong>Q${idx + 1}:</strong> ${escapeHtml(card.term)}</p>
      <textarea data-id="${card.id}" placeholder="Write your answer..."></textarea>
    `;
    els.testContainer.appendChild(div);
  });

  const btn = document.createElement("button");
  btn.className = "button-primary";
  btn.textContent = "Submit Test";
  btn.addEventListener("click", () => submitTest(sample, outcome.id));
  els.testContainer.appendChild(btn);
}

function submitTest(sample, outcomeId) {
  if (!getCurrentUser()) return;
  const answers = Array.from(els.testContainer.querySelectorAll("textarea"));
  const review = sample.map((card) => {
    const text = answers.find((a) => a.dataset.id === card.id)?.value?.trim() || "";
    const detail = evaluateAnswerDetailed(text, card.answer);
    const hits = findKeywordHits(text, card.keywords);
    const totalKw = (card.keywords || []).length;
    detail.keywordHits = hits;
    detail.keywordTotal = totalKw;
    const bonus = hits.length * 5;
    detail.bonus = bonus;
    detail.finalScore = Math.min(100, detail.score + bonus);
    return detail;
  });
  const avg = Math.round(review.reduce((a, b) => a + b.finalScore, 0) / review.length);

  if (avg >= 70) {
    const progressByOutcome = getProgressByOutcome();
    progressByOutcome[outcomeId] = Math.min(3, (progressByOutcome[outcomeId] || 0) + 1);
    const current = getCurrentUser();
    if (current) current.testsCompleted = (current.testsCompleted || 0) + 1;
  }
  persist();
  renderOutcomes();
  renderTestOverview(avg);
  renderDetailedReview(sample, review);
  renderProfileLevel();
}

function renderTestOverview(latestScore) {
  const outcome = getSelectedOutcome();
  if (!outcome) return;
  const step = getProgressByOutcome()[outcome.id] || 0;
  const current = getCurrentUser();
  const extra = typeof latestScore === "number" ? `<p>Latest score: <strong>${latestScore}%</strong></p>` : "";
  els.testContainer.innerHTML = `
    <p class="muted small">${escapeHtml(outcome.code)} ${escapeHtml(outcome.title)}</p>
    <p>User: <strong>${escapeHtml(current?.username || "Guest")}</strong></p>
    <p>Tests completed: <strong>${current?.testsCompleted || 0}</strong></p>
    <p>Goal: <strong>${step}/3</strong></p>
    ${extra}
    <p class="muted">Pass mark: 70%. Each key word hit adds +5% to your score.</p>
  `;
}

function cardsForOutcome(outcome, subjectId) {
  return (outcome.keyTerms || []).map((kt, idx) => ({
    id: `${outcome.id}-k-${idx + 1}`,
    term: buildPrompt(kt.term, idx, kt, subjectId),
    definition: compactText(kt.definition),
    keywords: extractKeywords(kt),
  }));
}

function getExamQuestionsForChapter(chapter) {
  const source = getOriginalChapter(chapter.id);
  return source?.examQuestions || [];
}

function getExamDisclaimer(subject) {
  if (subject === "business") {
    return `<div class="exam-disclaimer exam-disclaimer--warning">
      <span class="exam-disclaimer-icon">⚠</span>
      <span>The Business course has changed significantly. Past exam papers may not reflect current course requirements and are <strong>not a reliable</strong> study tool on their own — use them with caution.</span>
    </div>`;
  }
  if (subject === "biology") {
    return `<div class="exam-disclaimer exam-disclaimer--info">
      <span class="exam-disclaimer-icon">ℹ</span>
      <span>The Biology course has minor differences from previous years. Past exam papers are still a <strong>reliable</strong> way to study — the core content is largely the same.</span>
    </div>`;
  }
  return "";
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

  const disclaimer = getExamDisclaimer(chapter.subject);

  els.examContainer.innerHTML = disclaimer + examGroups.map((group) => {
    const parts = (group.parts || []).map((part, pIdx) => {
      const partId = `${group.id}-p${pIdx}`;
      const diagramBtn = part.diagram
        ? `<button class="button-secondary exam-diagram-btn" onclick="openDiagramModal('${escapeHtml(part.diagram)}')">Show Diagram</button>`
        : "";
      return `
        <div class="exam-part">
          <div class="exam-part-header">
            <span class="exam-part-label">${escapeHtml(part.label)}</span>
            <span class="exam-marks muted small">${part.marks} mark${part.marks === 1 ? "" : "s"}</span>
            ${diagramBtn}
          </div>
          <p class="exam-question-text">${escapeHtml(part.question)}</p>
          <textarea class="exam-textarea" placeholder="Write your answer here…" rows="5"></textarea>
          <div class="exam-answer-wrap hidden" id="ans-${escapeHtml(partId)}">
            <p class="exam-answer-label">Model Answer</p>
            <p class="exam-answer-text">${escapeHtml(part.model)}</p>
          </div>
          <button class="button-secondary exam-toggle-btn" onclick="toggleExamAnswer('${escapeHtml(partId)}', this)">Show Model Answer</button>
        </div>`;
    }).join("");

    const contextBox = group.caseStudy && group.context
      ? `<div class="exam-case-study-context">
          <div class="exam-case-study-context-label">Case Study — Read carefully before answering</div>
          <div class="exam-case-study-context-body">${escapeHtml(group.context).replace(/\n/g, "<br>")}</div>
        </div>`
      : "";

    return `
      <div class="exam-group${group.caseStudy ? " exam-group--case-study" : ""}">
        <div class="exam-group-header">
          <span class="exam-source-tag">${escapeHtml(group.source)}</span>
        </div>
        ${contextBox}
        ${parts}
      </div>`;
  }).join("");
}

function toggleExamAnswer(partId, btn) {
  const wrap = document.getElementById(`ans-${partId}`);
  if (!wrap) return;
  const hidden = wrap.classList.toggle("hidden");
  btn.textContent = hidden ? "Show Model Answer" : "Hide Model Answer";
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

function findKeywordHits(answer, keywords) {
  const text = sanitize(compactText(answer));
  return (keywords || []).filter((kw) => {
    const k = sanitize(kw);
    return k && text.includes(k);
  });
}

function buildPrompt(term, index, kt, subjectId) {
  const cleanTerm = compactText(term);
  const styleSet = SUBJECT_PROMPT_STYLES[subjectId] || SUBJECT_PROMPT_STYLES.business;
  let prompt = styleSet[index % styleSet.length](cleanTerm);
  if (shouldAskForExamples(kt)) prompt += " State examples.";
  return prompt;
}

function compactText(text) {
  return String(text || "")
    .replace(/\*\*/g, "")
    .replace(/—/g, "-")
    .replace(/\s+/g, " ")
    .replace(/\s*:\s*/g, ": ")
    .trim();
}

function questionsForOutcome(outcome, subjectId) {
  const fallback = SUBJECT_FALLBACK_QUESTION[subjectId] || SUBJECT_FALLBACK_QUESTION.business;
  return (outcome.keyTerms || []).map((kt, idx) => ({
    id: `${outcome.id}-q-${idx + 1}`,
    term: fallback(kt.term),
    answer: `${kt.term} ${kt.definition}`,
    keywords: extractKeywords(kt),
  }));
}

function questionsForChapter(chapter) {
  const subjectId = chapter.subject || "business";
  const source = getOriginalChapter(chapter.id);
  if (source && Array.isArray(source.learningOutcomes)) {
    const all = [];
    source.learningOutcomes.forEach((lo) => {
      (lo.questions || []).forEach((q, idx) => {
        if (q.type !== "short" || !q.prompt) return;
        const promptText = compactText(q.prompt);
        const modelText = compactText(q.model || "");
        all.push({
          id: `${lo.id}-q-${idx + 1}`,
          term: promptText,
          answer: modelText || promptText,
          keywords: extractKeywords({ term: promptText, definition: modelText }),
        });
      });
    });
    if (all.length) return all;
  }
  return (chapter.learningOutcomes || []).flatMap((lo) =>
    questionsForOutcome(lo, subjectId)
  );
}

function shuffleArray(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
  }
  return a;
}

function evaluateAnswerDetailed(answer, expected) {
  if (!answer) return { score: 0, parts: splitExpectedParts(expected).map((text) => ({ text, hit: false })) };
  const answerTokens = tokenize(answer);
  const parts = splitExpectedParts(expected).map((part) => {
    const partTokens = tokenize(part);
    const overlap = partTokens.filter((t) => matchesToken(answerTokens, t)).length;
    const ratio = partTokens.length ? overlap / partTokens.length : 0;
    return { text: part, hit: ratio >= 0.35 || (overlap >= 2 && partTokens.length >= 3) };
  });
  const matched = parts.filter((p) => p.hit).length;
  let score;
  if (parts.length) {
    score = Math.round((matched / parts.length) * 100);
  } else {
    const eTokens = [...new Set(tokenize(expected))];
    const hits = eTokens.filter((t) => matchesToken(answerTokens, t)).length;
    score = Math.min(100, Math.round((hits / Math.max(1, eTokens.length)) * 100));
  }
  return { score, parts };
}

function renderDetailedReview(sample, review) {
  const blocks = sample
    .map((card, idx) => {
      const r = review[idx];
      const chips = r.parts
        .map((p) => `<div class="${p.hit ? "mark-right" : "mark-wrong"}">${escapeHtml(compactText(p.text))}</div>`)
        .join("");
      const kwRow = renderKeywordRow(card.keywords, r.keywordHits || []);
      let bonusLine = "";
      if (r.keywordTotal) {
        bonusLine = `<p class="bonus-line"><strong>Key words:</strong> ${r.keywordHits.length}/${r.keywordTotal} matched · +${r.bonus}% (5% each)</p>`;
      }
      return `
        <div class="feedback-block">
          <p><strong>Q${idx + 1}</strong> Base: <strong>${r.score}%</strong> · Final: <strong>${r.finalScore}%</strong></p>
          <p class="muted small">Orange = concept covered. Grey = concept missing or unclear.</p>
          ${chips}
          ${bonusLine}
          ${kwRow}
        </div>
      `;
    })
    .join("");
  els.testContainer.insertAdjacentHTML("beforeend", blocks);
}

function splitExpectedParts(text) {
  return compactText(text)
    .split(/(?:\.\s+|\;\s+|\?\s+|\!\s+|\s\-\s)/)
    .map((p) => p.trim())
    .filter((p) => p.length > 6);
}

function tokenize(text) {
  return sanitize(compactText(text))
    .split(" ")
    .filter(Boolean)
    .map(stemToken);
}

function stemToken(token) {
  if (token.length <= 4) return token;
  for (const suffix of ["tion", "ing", "ed", "ly", "s"]) {
    if (token.endsWith(suffix)) {
      const stem = token.slice(0, token.length - suffix.length);
      if (stem.length >= 4) return stem;
    }
  }
  return token;
}

function matchesToken(answerTokens, token) {
  const groups = synonymGroup(token);
  return answerTokens.some((a) => groups.some((g) => a === g || a.startsWith(g) || g.startsWith(a)));
}

function synonymGroup(token) {
  const map = {
    // Business
    customer: ["customer", "consumer", "buyer", "client"],
    employee: ["employee", "staff", "worker", "team"],
    profit: ["profit", "earn", "income", "revenue", "return"],
    marketing: ["marketing", "promotion", "advertising", "brand"],
    risk: ["risk", "threat", "uncertainty", "hazard"],
    legal: ["legal", "law", "regulation", "compliance"],
    money: ["money", "cash", "finance", "funding", "capital"],
    // PE
    exercise: ["exercise", "workout", "training", "activity", "practice"],
    aerobic: ["aerobic", "cardiovascular", "cardio"],
    flexibility: ["flexibility", "mobility"],
    endurance: ["endurance", "stamina"],
    fitness: ["fitness", "health", "wellbeing", "wellness"],
    injury: ["injury", "damage", "strain"],
    // Biology
    enzyme: ["enzyme", "catalyst"],
    respiration: ["respiration", "breathing"],
    nucleus: ["nucleus", "nuclei"],
    autotroph: ["autotroph", "producer"],
    heterotroph: ["heterotroph", "consumer", "buyer", "client", "customer"],
    protein: ["protein", "polypeptide"],
    chromosome: ["chromosome", "chromatid"],
    photosynthesis: ["photosynthesis", "photosynthesize"],
  };
  for (const v of Object.values(map)) {
    if (v.includes(token)) return v.map(stemToken);
  }
  return [token];
}

function sanitize(text) {
  return text.toLowerCase().replace(/[^a-z0-9\s]/g, "");
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
  els.fullNotesTitle.textContent = `Full Notes — ${chapter.title}`;
  els.fullNotesBody.innerHTML = buildFullNotesHtml(chapter);
  els.fullNotesScreen.classList.remove("hidden");
  els.fullNotesScreen.scrollTop = 0;
  document.body.style.overflow = "hidden";
  markNotesViewed(chapter.id);
}

function buildFullNotesHtml(chapter) {
  const source = getOriginalChapter(chapter.id);
  if (source && Array.isArray(source.learningOutcomes) && source.learningOutcomes.length) {
    return source.learningOutcomes
      .map((lo) => {
        const noteHtml = (lo.notes || [])
          .map(
            (n) => `
              <div class="note-block">
                <h5>${escapeHtml(compactText(n.h || ""))}</h5>
                <p>${escapeHtml(compactText(n.b || ""))}</p>
              </div>`
          )
          .join("");
        return `
          <section class="lo-block">
            <h4>${escapeHtml(lo.code || "")} ${escapeHtml(lo.title || "")}</h4>
            ${noteHtml || "<p class='muted'>No notes for this outcome.</p>"}
          </section>`;
      })
      .join("");
  }
  const allPoints = chapter.learningOutcomes.flatMap((lo) => lo.keyTerms || []);
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
  return (data.chapters || []).find((c) => c.id === chapterId) || null;
}

function closeFullNotes() {
  els.fullNotesScreen.classList.add("hidden");
  document.body.style.overflow = "";
}

function buildProgressSubjectStats(user) {
  const progress = user?.progressByOutcome || {};
  return getEnabledSubjects().map((subject) => {
    let subEarned = 0, subTotal = 0;
    const chStats = (subject.chapters || []).map((ch) => {
      let chEarned = 0, chTotal = 0;
      (ch.learningOutcomes || []).forEach((lo) => {
        const concepts = (lo.keyTerms || []).length;
        chTotal += concepts;
        if ((progress[lo.id] || 0) >= 1) chEarned += concepts;
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

  const subjectCards = subjectStats.map((ss) => {
    const started = ss.chStats.filter((c) => c.earned > 0).length;
    const complete = ss.chStats.filter((c) => c.ratio === 1).length;
    return `
      <div class="progress-subject-card">
        <div class="progress-subject-pct" style="color:var(--accent)">${ss.pct}%</div>
        <div class="progress-subject-title">${escapeHtml(ss.subject.title)}</div>
        <div class="progress-subject-sub">${started} of ${ss.chStats.length} started &middot; ${complete} complete</div>
        <div class="progress-subject-bar-wrap">
          <div class="progress-subject-bar-fill" style="width:${ss.pct}%"></div>
        </div>
        <button class="button-secondary progress-subject-btn" onclick="renderProgressSubjectDetail('${escapeHtml(ss.subject.id)}')">View Chapters ›</button>
      </div>`;
  }).join("");

  els.progressBody.innerHTML = `
    <div class="progress-summary">
      <div class="progress-percent">${percent}%</div>
      <div class="progress-summary-meta">
        <strong>${testsCompleted} tests passed</strong>
        <span class="muted small">${earned} of ${total} concept points earned</span>
      </div>
    </div>
    <div class="progress-subject-grid">${subjectCards}</div>
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

  els.progressBody.innerHTML = `
    <div class="progress-detail-header">
      <button class="button-secondary" onclick="renderProgressOverview()">← Overview</button>
      <h4>${escapeHtml(ss.subject.title)} — Chapter Progress</h4>
      <span class="muted small">${ss.pct}% overall &middot; ${ss.earned}/${ss.total} concepts</span>
    </div>
    <div class="progress-chart progress-chart-detail">${bars}</div>
  `;
}

function openProgress() {
  renderProgressOverview();
  els.progressScreen.classList.remove("hidden");
  document.body.style.overflow = "hidden";
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

function persist() {
  localStorage.setItem(storageKey, JSON.stringify(state));
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

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}
