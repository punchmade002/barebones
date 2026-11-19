/* Dashboard (app.html): the student's subjects, their progress and how much they
   study. Study time is the active time usage-tracker.js records in usage_time,
   read back with BarebonesAuth.myUsage(). Loads before app.js and uses its globals
   (els, getCurrentUser, …) only when renderDashboard() is called. */
const STUDY_RANGES = [[7, "7 days"], [30, "30 days"], [90, "3 months"]];
const STUDY_HISTORY_DAYS = 90;
let studyRange = 7; // every visit opens on the last week
let studyRows = null; // [{ day, subject, seconds }] for the last 90 days
let studyRowsFor = ""; // the auth user the rows belong to
let studyRowsError = "";

// Line icons (24×24, drawn with currentColor) for subject and section tiles
const ICONS = {
  biology: '<path d="M8 3c0 4.5 8 4.5 8 9s-8 4.5-8 9"/><path d="M16 3c0 4.5-8 4.5-8 9s8 4.5 8 9"/><path d="M9.5 6.5h5M9.5 17.5h5"/>',
  chemistry: '<path d="M9 3h6M10 3v6l-5.2 9.1A2 2 0 0 0 6.5 21h11a2 2 0 0 0 1.7-2.9L14 9V3"/><path d="M7.4 15h9.2"/>',
  geography: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3.2 3.4 3.2 14.6 0 18M12 3c-3.2 3.4-3.2 14.6 0 18"/>',
  history: '<path d="M3 21h18M5 10h14M12 3l8 5H4z"/><path d="M7 10v8M10.3 10v8M13.7 10v8M17 10v8"/>',
  business: '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
  "home-economics": '<path d="M4 10h16v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M2 10h20M9 3.5c1 1 1 2 0 3M13 3.5c1 1 1 2 0 3"/>',
  pe: '<path d="M6.5 6.5v11M3.5 9v6M17.5 6.5v11M20.5 9v6M6.5 12h11"/>',
  maths: '<path d="M5 7h6M8 4v6M14 7h5M6 15l4 4M10 15l-4 4M14 16h5M14 19h5"/>',
  english: '<path d="M4 20l1.5-5L16 4.5a2.1 2.1 0 0 1 3 3L8.5 18z"/><path d="M14 6.5l3 3M4 20h16"/>',
  irish: '<path d="M12 12a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7zM12 12a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7z"/><path d="M12 12a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0zM12 12a3.5 3.5 0 1 0-7 0 3.5 3.5 0 0 0 7 0z"/>',
  french: '<path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4z"/><path d="M8 9h5M8 11.5h3"/>',
  spanish: '<path d="M3 5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H8l-3 2.5V12a2 2 0 0 1-2-2z"/><path d="M18 9h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2v2.5L16 18h-4a2 2 0 0 1-2-2v-1"/>',
  "construction-studies": '<path d="M3 21h18M5 21V11l7-6 7 6v10"/><path d="M9.5 21v-6h5v6"/>',
  art: '<path d="M12 3a9 9 0 1 0 0 18c1.4 0 2-1 1.5-2.2-.6-1.4.3-2.8 1.8-2.8H18a3 3 0 0 0 3-3c0-5.5-4-10-9-10z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10.5" cy="7.5" r="1"/><circle cx="15" cy="7.5" r="1"/>',
  physics: '<circle cx="12" cy="12" r="1.6"/><ellipse cx="12" cy="12" rx="9" ry="3.6"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(120 12 12)"/>',
  guide: '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 11h7M9 15h7M9 19h4"/>',
  aac: '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2.5h6V4M8.5 11l2 2 4-4M9 17h6"/>',
  flashcards: '<rect x="3" y="8" width="14" height="12" rx="2"/><path d="M7 4h12a2 2 0 0 1 2 2v10"/>',
  notes: '<path d="M3 5h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H3z"/><path d="M21 5h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>',
  tests: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M10 2h4"/>',
  exam: '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 14l2 2 4-4"/>',
  papers: '<path d="M8 3h8l4 4v12a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M16 3v4h4M4 7v13a1 1 0 0 0 1 1h10M10.5 11h6M10.5 14.5h6"/>',
};

function iconHtml(name) {
  return `<span class="tile-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${ICONS[name] || ""}</svg></span>`;
}

// ── Subject page sections ──
// scripts/subject-pages.cjs runs this file at build time to write each subject page's tiles
// and placeholders into its HTML, so they show before the app's scripts have loaded.
const SECTION_LABELS = { guide: "Paper guide", aac: "AAC guide", flashcards: "Flashcards", notes: "Notes", tests: "Tests", exam: "Exam", papers: "Exam papers" };
// Subjects that so far have only their whole past papers (exam-papers.js); each joins the app once
// scripts/build_exam_papers.py has built its archive. They have paper and AAC guides but no study tools yet.
const PAPERS_ONLY_SUBJECTS = {
  english: "English", irish: "Irish", french: "French", "construction-studies": "Construction Studies",
  spanish: "Spanish", art: "Art", physics: "Physics",
};
// Maths has no flashcards or notes yet; it keeps its chapter → exam questions view.
// One AAC section per coursework component in aac-guides.js (none for Maths).
function sectionsFor(subjectId) {
  const sections = subjectId in PAPERS_ONLY_SUBJECTS ? ["guide", "aac", "papers"]
    : subjectId === "maths" ? ["guide", "aac", "exam"]
    : ["guide", "aac", "flashcards", "notes", "tests", "exam"];
  return sections.flatMap((id) => (id === "aac" ? aacGuidesFor(subjectId).map((a) => a.section) : [id]));
}
// A subject with two coursework components (PE, Home Economics) has two guides: aac-guides.js
// keys them "<subject>" and "<subject>-<part>", and their sections are "aac" and "aac-<part>".
function aacGuidesFor(subjectId) {
  return Object.entries(window.AAC_GUIDES || {})
    .filter(([, guide]) => guide.subject === subjectId)
    .map(([key, guide]) => ({ key, guide, section: key === subjectId ? "aac" : `aac-${key.slice(subjectId.length + 1)}` }));
}
const isAacSection = (id) => /^aac(-|$)/.test(id);
function sectionLabel(subjectId, id) {
  if (!isAacSection(id)) return SECTION_LABELS[id] || "";
  const all = aacGuidesFor(subjectId);
  const own = all.find((a) => a.section === id);
  return all.length > 1 && own ? `AAC · ${own.guide.short || own.guide.title}` : SECTION_LABELS.aac;
}

function sectionTilesHtml(subjectId) {
  const tiles = sectionsFor(subjectId).map((id) => `
    <li><a class="section-tile" href="app/${subjectId}/#${id}">${iconHtml(isAacSection(id) ? "aac" : id)}<span>${escapeHtml(sectionLabel(subjectId, id))}</span></a></li>`).join("");
  return `<ul class="section-tiles">${tiles}</ul>`;
}

// Placeholder shapes shown while a screen's data downloads
function skeletonHtml(kind) {
  const bar = (w, h = "0.9rem", extra = "") => `<span class="skeleton" style="width:${w};height:${h};${extra}"></span>`;
  // Margins pad a bar out to the line box of the text it stands in for (line-height 1.55 / 1.65)
  const small = (w) => bar(w, "0.7rem", "margin-block:0.1925rem");
  if (kind === "card") {
    // Same parts and classes as the real card (head, centred face, controls) so nothing shifts when it loads
    return `
      <header class="study-card-head" aria-hidden="true">
        <div class="study-progress"><div class="progress-bar"><span style="width:0"></span></div>${small("1.6rem")}</div>
        ${small("2rem")}
      </header>
      <div class="study-face" aria-busy="true" aria-label="Loading flashcard">${bar("min(320px, 70%)", "1em", "font-size:clamp(1.35rem, 2.5vw, 2rem);margin-block:0.325em")}</div>
      <div class="study-card-footer" aria-hidden="true">
        <div class="study-controls">
          <button id="prevCard" class="button-secondary study-step" tabindex="-1" disabled>←</button>
          <button id="flipCard" class="button-primary" tabindex="-1" disabled>Reveal</button>
          <button id="nextCard" class="button-secondary study-step" tabindex="-1" disabled>→</button>
          <button id="markLearned" class="button-secondary study-learned" tabindex="-1" disabled>Mark learned</button>
        </div>
      </div>`;
  }
  const rows = [0, 1, 2, 3].map(() => `<div class="skeleton-row">${bar("34%", "1rem")}${bar("92%")}${bar("78%")}</div>`).join("");
  return `<div class="skeleton-block" aria-busy="true" aria-label="Loading">${rows}</div>`;
}

function setStudyRange(days) {
  studyRange = days;
  renderAll();
}

// The last `count` local days as "YYYY-MM-DD", oldest first
function lastDays(count) {
  const days = [];
  for (let i = count - 1; i >= 0; i -= 1) {
    const d = new Date();
    d.setDate(d.getDate() - i);
    days.push(window.BarebonesUsage.localDay(d.getTime()));
  }
  return days;
}

// Called from activateAuthenticatedSession the moment the account is known, in parallel
// with the rest of sign-in, so it never waits on a re-render to start.
async function loadStudyRows(userId) {
  studyRowsFor = userId;
  studyRows = null;
  studyRowsError = "";
  try {
    // Send this browser's unsent time first so today is current
    await usageTracker?.flush();
    const rows = await accountAuth.myUsage(lastDays(STUDY_HISTORY_DAYS)[0]);
    if (studyRowsFor === userId) studyRows = rows;
  } catch (error) {
    console.error(error);
    if (studyRowsFor === userId) studyRowsError = error?.message || "error";
  }
  if (studyRowsFor === userId && getCurrentUser()) renderAll();
}

function formatStudyTime(seconds) {
  const minutes = Math.round(seconds / 60);
  if (minutes < 60) return `${minutes}m`;
  const rest = minutes % 60;
  return rest ? `${Math.floor(minutes / 60)}h ${rest}m` : `${Math.floor(minutes / 60)}h`;
}

function renderDashboard() {
  const user = getCurrentUser();
  if (!user || !els.dashboard) return;
  const { percent } = computeUserProgress(user);
  const tests = user.testsCompleted || 0;
  const subjects = buildProgressSubjectStats(user);
  const days = lastDays(studyRange);
  const inRange = new Set(days);
  const secondsBySubject = {};
  (studyRows || []).forEach((row) => {
    if (inRange.has(row.day)) secondsBySubject[row.subject] = (secondsBySubject[row.subject] || 0) + row.seconds;
  });
  const rangeLabel = STUDY_RANGES.find(([n]) => n === studyRange)[1];

  const subjectRows = subjects.map((ss) => {
    const id = ss.subject.id;
    const time = studyRows ? secondsBySubject[id] || 0 : null;
    const hasCards = ss.total > 0 && sectionsFor(id).includes("flashcards");
    return `
      <li>
        <a class="dash-subject" href="app/${id}/">
          ${iconHtml(id)}
          <span class="dash-subject-title">${escapeHtml(ss.subject.title)}</span>
          <span class="dash-subject-meta">${[
            hasCards ? `${ss.pct}% learned` : "",
            time === null ? "" : time >= 60 ? `${formatStudyTime(time)} in ${rangeLabel}` : `Not studied in ${rangeLabel}`,
          ].filter(Boolean).join(" · ")}</span>
          ${hasCards ? `<span class="dash-subject-bar" aria-hidden="true"><span style="width:${ss.pct}%"></span></span>` : ""}
        </a>
      </li>`;
  }).join("");

  els.dashboard.innerHTML = `
    <header class="dash-head">
      <h1>Hi, ${escapeHtml(user.displayName || user.username)}</h1>
      <p>${percent}% of your course learned · ${plural(tests, "test")} passed</p>
    </header>
    <section class="dash-subjects" aria-labelledby="dashSubjectsTitle">
      <div class="dash-block-head">
        <h2 id="dashSubjectsTitle">Your subjects</h2>
        <button class="dash-text-button" type="button" onclick="openProgress()">Chapter progress ›</button>
      </div>
      <ul class="dash-subject-grid">${subjectRows}</ul>
    </section>
    ${studyTimeBlockHtml()}`;
}

// The Study time card: every subject on the dashboard, one subject on its own page
function studyTimeBlockHtml(subjectId = "") {
  return `
    <section class="dash-block dash-habits" aria-labelledby="dashHabitsTitle">
      <div class="dash-block-head">
        <h2 id="dashHabitsTitle">Study time</h2>
        <div class="dash-range" role="group" aria-label="Time range">
          ${STUDY_RANGES.map(([n, label]) => `
            <button type="button" aria-pressed="${n === studyRange}" onclick="setStudyRange(${n})">${label}</button>`).join("")}
        </div>
      </div>
      ${studyHabitsHtml(lastDays(studyRange), subjectId)}
    </section>`;
}

function studyHabitsHtml(days, subjectId) {
  if (!accountAuth?.configured) return `<p class="dash-empty">Study time is recorded once you sign in with an account.</p>`;
  if (studyRowsError) {
    const missing = /usage_time|schema cache|does not exist/i.test(studyRowsError);
    return `<p class="dash-empty">${missing ? "Study time isn’t switched on yet." : "Your study time couldn’t be loaded. Check your connection and reload."}</p>`;
  }
  if (!studyRows) return skeletonHtml("rows");

  const byDay = {};
  studyRows.forEach((row) => {
    if (!subjectId || row.subject === subjectId) byDay[row.day] = (byDay[row.day] || 0) + row.seconds;
  });
  const seconds = days.map((day) => byDay[day] || 0);
  const total = seconds.reduce((a, b) => a + b, 0);
  const studied = seconds.filter((s) => s >= 60).length;

  // Streak: days in a row with at least a minute, counting back from today (or yesterday, if today hasn't started)
  const history = lastDays(STUDY_HISTORY_DAYS).map((day) => byDay[day] || 0);
  let i = history.length - 1;
  if (history[i] < 60) i -= 1;
  let streak = 0;
  while (i >= 0 && history[i] >= 60) { streak += 1; i -= 1; }

  const stats = [
    ["Total", formatStudyTime(total)],
    ["Daily average", formatStudyTime(total / days.length)],
    ["Days studied", `${studied} of ${days.length}`],
    ["Streak", plural(streak, "day")],
  ];
  return `
    <dl class="study-stats">${stats.map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join("")}</dl>
    ${studyChartHtml(days, seconds)}`;
}

// A round top for the y axis: 15m, 30m, 1h, 2h, 3h…
function studyAxisMax(maxSeconds) {
  const steps = [15, 30, 60, 120, 180, 240, 360, 480, 720];
  const minutes = maxSeconds / 60;
  return (steps.find((s) => s >= minutes) || Math.ceil(minutes / 60) * 60) * 60;
}

function studyChartHtml(days, seconds) {
  const top = studyAxisMax(Math.max(...seconds, 60));
  const dayDate = (day) => new Date(`${day}T12:00:00`);
  const short = (day, opts) => dayDate(day).toLocaleDateString("en-IE", opts);
  // Which columns get a date under them: every day for a week, Mondays for a month, month starts for 3 months
  const showLabel = (day, i) => {
    if (days.length <= 7) return true;
    const d = dayDate(day);
    return days.length <= 31 ? d.getDay() === 1 : d.getDate() === 1 || i === 0;
  };
  const label = (day) => days.length <= 7
    ? short(day, { weekday: "short" })
    : days.length <= 31 ? short(day, { day: "numeric", month: "short" }) : short(day, { month: "short" });

  const cols = days.map((day, i) => {
    const pct = (seconds[i] / top) * 100;
    const tip = `${short(day, { weekday: "short", day: "numeric", month: "short" })} · ${seconds[i] >= 60 ? formatStudyTime(seconds[i]) : "no study"}`;
    return `
      <div class="study-col">
        <span class="study-bar" style="height:${pct}%"></span>
        <span class="study-tip">${tip}</span>
        ${showLabel(day, i) ? `<span class="study-x">${label(day)}</span>` : ""}
      </div>`;
  }).join("");

  const rows = days.map((day, i) => `<tr><th scope="row">${short(day, { weekday: "long", day: "numeric", month: "long" })}</th><td>${formatStudyTime(seconds[i])}</td></tr>`).join("");
  return `
    <div class="study-chart" style="--cols:${days.length}" aria-hidden="true">
      <div class="study-y">
        <span>${formatStudyTime(top)}</span><span>${formatStudyTime(top / 2)}</span><span>0</span>
      </div>
      <div class="study-plot ${days.length > 31 ? "is-dense" : ""}">${cols}</div>
    </div>
    <table class="sr-only"><caption>Study time per day</caption><tbody>${rows}</tbody></table>`;
}
