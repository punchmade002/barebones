(function () {
  "use strict";

  // First-run questionnaire shown once after a new account is created.
  // Builds its own DOM; app.js supplies the subject list and persists the answers.

  const ICONS = {
    compass: '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>',
    sprout: '<path d="M7 20h10"/><path d="M12 20v-9"/><path d="M12 11C12 7 9.5 5 5 5c0 4 2.5 6 7 6Z"/><path d="M12 11c0-3.5 2.2-6 7-6 0 4-2.4 6-7 6Z"/>',
    summit: '<path d="m3 20 6.5-11 4 6.5L16 12l5 8Z"/><path d="M9.5 9V3l4 1.5-4 1.5"/>',
    business: '<rect x="2.5" y="7" width="19" height="13" rx="2.5"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M2.5 13h19"/>',
    pe: '<path d="M22 12h-4l-3 8L9 4l-3 8H2"/>',
    biology: '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    geography: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10Z"/>',
    maths: '<path d="M18 7V4H6l6 8-6 8h12v-3"/>',
    chemistry: '<path d="M9 2v6.5L4.2 17.4A3 3 0 0 0 6.8 22h10.4a3 3 0 0 0 2.6-4.6L15 8.5V2"/><path d="M7.5 2h9"/><path d="M6.5 15h11"/>',
    "home-economics": '<path d="M6 13.87A4 4 0 0 1 7.41 6a5.11 5.11 0 0 1 9.18 0A4 4 0 0 1 18 13.87V21H6Z"/><path d="M6 17h12"/>',
    history: '<path d="M3 22h18"/><path d="M6 18v-7"/><path d="M10 18v-7"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M12 2 20 7H4Z"/>',
    book: '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
    check: '<polyline points="20 6 9 17 4 12"/>',
    arrowLeft: '<path d="M19 12H5"/><path d="m12 19-7-7 7-7"/>',
    arrowRight: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    calendar: '<rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
    layers: '<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    stack: '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/><path d="M8 7h8"/><path d="M8 11h6"/>',
    cap: '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
  };

  const YEARS = [
    { id: "ty", label: "Transition Year", icon: "compass" },
    { id: "5th", label: "5th Year", icon: "sprout" },
    { id: "6th", label: "6th Year", icon: "summit" },
  ];

  const DAYS = [
    { id: "mon", short: "M", label: "Monday" },
    { id: "tue", short: "T", label: "Tuesday" },
    { id: "wed", short: "W", label: "Wednesday" },
    { id: "thu", short: "T", label: "Thursday" },
    { id: "fri", short: "F", label: "Friday" },
    { id: "sat", short: "S", label: "Saturday" },
    { id: "sun", short: "S", label: "Sunday" },
  ];

  const DAY_PRESETS = [
    { id: "weekdays", label: "Weekdays", days: ["mon", "tue", "wed", "thu", "fri"] },
    { id: "weekends", label: "Weekends", days: ["sat", "sun"] },
    { id: "everyday", label: "Every day", days: DAYS.map((d) => d.id) },
  ];

  const STEPS = [
    { id: "year", kicker: "Year", icon: "cap" },
    { id: "subjects", kicker: "Subjects", icon: "stack" },
    { id: "levels", kicker: "Levels", icon: "layers" },
    { id: "days", kicker: "Study days", icon: "calendar" },
    { id: "priority", kicker: "Priority", icon: "target" },
  ];

  function icon(name, extraClass = "") {
    const body = ICONS[name] || ICONS.book;
    return `<svg class="ob-icon ${extraClass}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
  }

  function escapeText(value) {
    return String(value ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    }[c]));
  }

  const reducedMotion = () =>
    window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;

  function open({ subjects, username = "", initial = {}, onComplete }) {
    const existing = document.getElementById("onboardingScreen");
    if (existing) existing.remove();

    const answers = {
      year: initial.year || "",
      subjects: Array.isArray(initial.subjects) ? [...initial.subjects] : [],
      levels: { ...(initial.levels || {}) },
      studyDays: Array.isArray(initial.studyDays) ? [...initial.studyDays] : [],
      prioritySubject: initial.prioritySubject || "",
    };
    let stepIndex = 0;
    let direction = 1;

    const root = document.createElement("section");
    root.id = "onboardingScreen";
    root.className = "ob-screen";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-labelledby", "obTitle");
    root.innerHTML = `
      <div class="ob-aura" aria-hidden="true">
        <span class="ob-blob ob-blob-a"></span>
        <span class="ob-blob ob-blob-b"></span>
        <span class="ob-blob ob-blob-c"></span>
      </div>
      <div class="ob-frame">
        <header class="ob-head">
          <img class="ob-logo" src="design_handoff_barebones_landing/assets/logo-wordmark.png" alt="barebones" />
          <ol class="ob-rail" aria-label="Setup progress">
            ${STEPS.map((s, i) => `
              <li class="ob-rail-step" data-rail="${i}">
                <span class="ob-rail-dot">${icon(s.icon)}</span>
                <span class="ob-rail-label">${s.kicker}</span>
              </li>`).join("")}
          </ol>
          <div class="ob-rail-track" aria-hidden="true"><span class="ob-rail-fill"></span></div>
        </header>
        <div class="ob-stage" aria-live="polite"></div>
        <footer class="ob-foot">
          <button type="button" class="ob-back" data-ob-back>${icon("arrowLeft")}<span>Back</span></button>
          <button type="button" class="ob-next" data-ob-next><span>Continue</span>${icon("arrowRight")}</button>
        </footer>
      </div>`;

    document.body.appendChild(root);
    document.body.classList.add("onboarding-open");

    const stage = root.querySelector(".ob-stage");
    const nextBtn = root.querySelector("[data-ob-next]");
    const backBtn = root.querySelector("[data-ob-back]");
    const railFill = root.querySelector(".ob-rail-fill");

    const subjectById = (id) => subjects.find((s) => s.id === id);
    const chosenSubjects = () => subjects.filter((s) => answers.subjects.includes(s.id));

    function isStepValid(id) {
      if (id === "year") return Boolean(answers.year);
      if (id === "subjects") return answers.subjects.length > 0;
      if (id === "levels") return true;
      if (id === "days") return answers.studyDays.length > 0;
      if (id === "priority") return Boolean(answers.prioritySubject);
      return true;
    }

    function titleFor(id) {
      const first = escapeText(username ? `, ${username}` : "");
      return {
        year: `Welcome${first}. What <em>year</em> are you in?`,
        subjects: `Which <em>subjects</em> are you taking?`,
        levels: `Which <em>level</em> for each?`,
        days: `Which <em>days</em> will you study?`,
        priority: `What's your <em>biggest priority</em> right now?`,
      }[id];
    }

    function subtitleFor(id) {
      return {
        year: "We'll pace your study around where you are.",
        subjects: "Pick every one you sit. You can change this later.",
        levels: "Everything starts at Higher. Tap to switch to Ordinary.",
        days: "Choose the days that work. Little and often wins.",
        priority: "We'll put this one front and centre when you sign in.",
      }[id];
    }

    function bodyFor(id) {
      if (id === "year") {
        return `<div class="ob-grid ob-grid-years" role="radiogroup" aria-label="School year">
          ${YEARS.map((y, i) => `
            <button type="button" class="ob-tile ob-tile-year ${answers.year === y.id ? "is-on" : ""}"
              role="radio" aria-checked="${answers.year === y.id}" data-year="${y.id}" style="--i:${i}">
              <span class="ob-tile-icon">${icon(y.icon)}</span>
              <span class="ob-tile-label">${y.label}</span>
              <span class="ob-tick">${icon("check")}</span>
            </button>`).join("")}
        </div>`;
      }

      if (id === "subjects") {
        return `<div class="ob-grid ob-grid-subjects" role="group" aria-label="Subjects">
          ${subjects.map((s, i) => {
            const on = answers.subjects.includes(s.id);
            return `<button type="button" class="ob-tile ob-tile-subject ${on ? "is-on" : ""}"
                aria-pressed="${on}" data-subject="${s.id}" style="--i:${i}">
              <span class="ob-tile-icon">${icon(s.id)}</span>
              <span class="ob-tile-label">${escapeText(s.title)}</span>
              <span class="ob-tick">${icon("check")}</span>
            </button>`;
          }).join("")}
        </div>
        <p class="ob-meta"><span class="ob-meta-num">${answers.subjects.length}</span> selected</p>`;
      }

      if (id === "levels") {
        return `<div class="ob-levels">
          ${chosenSubjects().map((s, i) => {
            const ordinary = answers.levels[s.id] === "ordinary";
            return `<div class="ob-level-row" style="--i:${i}">
              <span class="ob-level-icon">${icon(s.id)}</span>
              <span class="ob-level-name">${escapeText(s.title)}</span>
              <button type="button" class="ob-switch ${ordinary ? "is-ordinary" : ""}" data-level="${s.id}"
                role="switch" aria-checked="${ordinary}" aria-label="${escapeText(s.title)}: ${ordinary ? "Ordinary" : "Higher"} level">
                <span class="ob-switch-thumb"></span>
                <span class="ob-switch-opt ob-switch-h">Higher</span>
                <span class="ob-switch-opt ob-switch-o">Ordinary</span>
              </button>
            </div>`;
          }).join("")}
        </div>`;
      }

      if (id === "days") {
        const set = new Set(answers.studyDays);
        return `<div class="ob-days" role="group" aria-label="Study days">
          ${DAYS.map((d, i) => `
            <button type="button" class="ob-day ${set.has(d.id) ? "is-on" : ""}" data-day="${d.id}"
              aria-pressed="${set.has(d.id)}" aria-label="${d.label}" style="--i:${i}">
              <span class="ob-day-letter">${d.short}</span>
              <span class="ob-day-name">${d.label.slice(0, 3)}</span>
            </button>`).join("")}
        </div>
        <div class="ob-presets">
          ${DAY_PRESETS.map((p) => {
            const active = p.days.length === set.size && p.days.every((d) => set.has(d));
            return `<button type="button" class="ob-preset ${active ? "is-on" : ""}" data-preset="${p.id}">${p.label}</button>`;
          }).join("")}
        </div>
        <p class="ob-meta"><span class="ob-meta-num">${set.size}</span> day${set.size === 1 ? "" : "s"} a week</p>`;
      }

      if (id === "priority") {
        return `<div class="ob-grid ob-grid-subjects" role="radiogroup" aria-label="Priority subject">
          ${chosenSubjects().map((s, i) => {
            const on = answers.prioritySubject === s.id;
            const level = answers.levels[s.id] === "ordinary" ? "Ordinary" : "Higher";
            return `<button type="button" class="ob-tile ob-tile-subject ob-tile-priority ${on ? "is-on" : ""}"
                role="radio" aria-checked="${on}" data-priority="${s.id}" style="--i:${i}">
              <span class="ob-tile-icon">${icon(s.id)}</span>
              <span class="ob-tile-label">${escapeText(s.title)}</span>
              <span class="ob-tile-hint">${level}</span>
              <span class="ob-tick">${icon("target")}</span>
            </button>`;
          }).join("")}
        </div>`;
      }
      return "";
    }

    function renderFooter() {
      const step = STEPS[stepIndex];
      backBtn.classList.toggle("is-hidden", stepIndex === 0);
      backBtn.tabIndex = stepIndex === 0 ? -1 : 0;
      nextBtn.disabled = !isStepValid(step.id);
      nextBtn.querySelector("span").textContent =
        stepIndex === STEPS.length - 1 ? "Finish" : "Continue";
      railFill.style.setProperty("--p", String(stepIndex / (STEPS.length - 1)));
      root.querySelectorAll(".ob-rail-step").forEach((el, i) => {
        el.classList.toggle("is-done", i < stepIndex);
        el.classList.toggle("is-current", i === stepIndex);
      });
    }

    function renderStep({ animate = true } = {}) {
      const step = STEPS[stepIndex];
      const panel = document.createElement("div");
      panel.className = "ob-panel";
      panel.dataset.step = step.id;
      panel.innerHTML = `
        <h2 id="obTitle" class="ob-title">${titleFor(step.id)}</h2>
        <p class="ob-sub">${subtitleFor(step.id)}</p>
        <div class="ob-body">${bodyFor(step.id)}</div>`;

      const old = stage.querySelector(".ob-panel:not(.is-leaving)");
      if (old && animate && !reducedMotion()) {
        old.classList.add("is-leaving");
        old.style.setProperty("--dir", direction);
        old.addEventListener("animationend", () => old.remove(), { once: true });
        window.setTimeout(() => old.remove(), 600);
      } else if (old) {
        old.remove();
      }
      panel.style.setProperty("--dir", direction);
      stage.appendChild(panel);
      renderFooter();
      const focusable = panel.querySelector(".is-on, .ob-tile, .ob-switch, .ob-day");
      window.setTimeout(() => focusable?.focus({ preventScroll: true }), animate ? 260 : 0);
    }

    // Re-renders the current step in place (selection changed) without the slide.
    function refreshStep() {
      const panel = stage.querySelector(".ob-panel:not(.is-leaving)");
      if (!panel) return;
      const body = panel.querySelector(".ob-body");
      const active = document.activeElement;
      const key = active && ["year", "subject", "level", "day", "priority", "preset"]
        .map((k) => active.dataset?.[k] ? `[data-${k}="${active.dataset[k]}"]` : "")
        .find(Boolean);
      body.innerHTML = bodyFor(STEPS[stepIndex].id);
      body.classList.add("is-static");
      if (key) body.querySelector(key)?.focus({ preventScroll: true });
      renderFooter();
    }

    function go(delta) {
      const target = stepIndex + delta;
      if (delta > 0 && !isStepValid(STEPS[stepIndex].id)) return;
      if (target >= STEPS.length) return finish();
      if (target < 0) return;
      direction = delta > 0 ? 1 : -1;
      stepIndex = target;
      // Keep downstream answers consistent with the subject list.
      answers.subjects = answers.subjects.filter((id) => subjectById(id));
      if (!answers.subjects.includes(answers.prioritySubject)) answers.prioritySubject = "";
      if (STEPS[stepIndex].id === "priority" && !answers.prioritySubject && answers.subjects.length === 1) {
        answers.prioritySubject = answers.subjects[0];
      }
      renderStep();
    }

    function finish() {
      const levels = {};
      answers.subjects.forEach((id) => {
        levels[id] = answers.levels[id] === "ordinary" ? "ordinary" : "higher";
      });
      const result = {
        year: answers.year,
        subjects: [...answers.subjects],
        levels,
        studyDays: DAYS.map((d) => d.id).filter((d) => answers.studyDays.includes(d)),
        prioritySubject: answers.prioritySubject,
        completedAt: new Date().toISOString(),
      };
      showDone(result);
    }

    function showDone(result) {
      const priority = subjectById(result.prioritySubject);
      const dayNames = DAYS.filter((d) => result.studyDays.includes(d.id)).map((d) => d.label.slice(0, 3));
      const year = YEARS.find((y) => y.id === result.year);
      root.classList.add("is-done");
      stage.innerHTML = `
        <div class="ob-panel ob-done">
          <div class="ob-burst" aria-hidden="true">
            ${Array.from({ length: 12 }, (_, i) => `<span style="--a:${i * 30}deg"></span>`).join("")}
            <span class="ob-burst-core">${icon("check")}</span>
          </div>
          <h2 id="obTitle" class="ob-title">You're <em>all set.</em></h2>
          <p class="ob-sub">Here's your plan. You can change subjects any time from your account menu.</p>
          <div class="ob-summary">
            <span class="ob-chip" style="--i:0">${icon(year?.icon || "cap")}${escapeText(year?.label || "")}</span>
            <span class="ob-chip" style="--i:1">${icon("stack")}${result.subjects.length} subject${result.subjects.length === 1 ? "" : "s"}</span>
            <span class="ob-chip" style="--i:2">${icon("calendar")}${escapeText(dayNames.join(" · "))}</span>
            <span class="ob-chip ob-chip-hot" style="--i:3">${icon(priority?.id || "target")}${escapeText(priority?.title || "")} first</span>
          </div>
          <button type="button" class="ob-start" data-ob-start><span>Start studying</span>${icon("arrowRight")}</button>
        </div>`;
      const start = stage.querySelector("[data-ob-start]");
      window.setTimeout(() => start.focus({ preventScroll: true }), 300);
      start.addEventListener("click", () => close(result));
    }

    function close(result) {
      root.classList.add("is-exiting");
      const done = () => {
        root.remove();
        document.body.classList.remove("onboarding-open");
        document.removeEventListener("keydown", onKey);
      };
      if (reducedMotion()) done();
      else window.setTimeout(done, 520);
      onComplete?.(result);
    }

    function onKey(event) {
      if (root.classList.contains("is-done")) return;
      if (event.key === "Enter" && !event.target.closest?.("button")) {
        event.preventDefault();
        go(1);
      }
    }

    root.addEventListener("click", (event) => {
      const t = event.target.closest("button");
      if (!t || !root.contains(t)) return;

      if (t.matches("[data-ob-next]")) return go(1);
      if (t.matches("[data-ob-back]")) return go(-1);

      if (t.dataset.year) {
        answers.year = t.dataset.year;
        refreshStep();
        if (!reducedMotion()) window.setTimeout(() => stepIndex === 0 && go(1), 420);
        return;
      }
      if (t.dataset.subject) {
        const id = t.dataset.subject;
        answers.subjects = answers.subjects.includes(id)
          ? answers.subjects.filter((s) => s !== id)
          : subjects.map((s) => s.id).filter((s) => s === id || answers.subjects.includes(s));
        return refreshStep();
      }
      if (t.dataset.level) {
        const id = t.dataset.level;
        answers.levels[id] = answers.levels[id] === "ordinary" ? "higher" : "ordinary";
        // Animate the thumb in place rather than re-rendering the row.
        const ordinary = answers.levels[id] === "ordinary";
        t.classList.toggle("is-ordinary", ordinary);
        t.setAttribute("aria-checked", String(ordinary));
        const name = subjectById(id)?.title || id;
        t.setAttribute("aria-label", `${name}: ${ordinary ? "Ordinary" : "Higher"} level`);
        return;
      }
      if (t.dataset.day) {
        const id = t.dataset.day;
        answers.studyDays = answers.studyDays.includes(id)
          ? answers.studyDays.filter((d) => d !== id)
          : [...answers.studyDays, id];
        return refreshStep();
      }
      if (t.dataset.preset) {
        const preset = DAY_PRESETS.find((p) => p.id === t.dataset.preset);
        if (preset) answers.studyDays = [...preset.days];
        return refreshStep();
      }
      if (t.dataset.priority) {
        answers.prioritySubject = t.dataset.priority;
        return refreshStep();
      }
    });

    document.addEventListener("keydown", onKey);
    renderStep({ animate: false });
    return { close: () => close(null) };
  }

  window.BarebonesOnboarding = { open };
})();
