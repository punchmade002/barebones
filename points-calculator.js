// barebones — Leaving Cert (CAO) points calculator.
// Scoring is a pure function (BBPoints.score) so tests can load this file in a vm
// without a DOM; the UI below only binds when it finds #pc on the page.
//
// Common Points Scale (CAO, 2017 onwards):
//   Higher    H1 100  H2 88  H3 77  H4 66  H5 56  H6 46  H7 37  H8 0
//   Ordinary  O1 56   O2 46  O3 37  O4 28  O5 20  O6 12  O7 0   O8 0
//   Foundation Maths F1 20  F2 12 (only some colleges count it)
//   LCVP Link Modules  Distinction 66  Merit 46  Pass 28
//   +25 bonus for Higher Level Mathematics at H6 or above, only if Maths makes the best six.
(function () {
  "use strict";

  const SCALE = {
    H: [100, 88, 77, 66, 56, 46, 37, 0],
    O: [56, 46, 37, 28, 20, 12, 0, 0],
    F: [20, 12, 0, 0, 0, 0, 0, 0],
  };
  const LCVP_POINTS = { D: 66, M: 46, P: 28 };
  const MATHS = "Mathematics";
  const LCVP = "LCVP Link Modules";
  const MATHS_BONUS = 25;
  const COUNTED = 6;

  // One row -> { base, bonus, total } or null when the row has no grade yet.
  function rowPoints(row) {
    if (!row || !row.grade) return null;
    if (row.subject === LCVP) {
      const base = LCVP_POINTS[row.grade];
      return base == null ? null : { base, bonus: 0, total: base };
    }
    const level = row.level || "H";
    if (level === "F" && row.subject !== MATHS) return null;
    const scale = SCALE[level];
    const g = Number(row.grade);
    if (!scale || !(g >= 1 && g <= 8)) return null;
    const base = scale[g - 1];
    const bonus = row.subject === MATHS && level === "H" && g <= 6 ? MATHS_BONUS : 0;
    return { base, bonus, total: base + bonus };
  }

  // rows: [{ subject, level: "H"|"O"|"F", grade: "1".."8" | "D"|"M"|"P" }]
  // Returns the total, which rows count, and why the others don't.
  function score(rows) {
    const scored = rows.map((row, index) => ({ index, row, pts: rowPoints(row) }));
    const graded = scored.filter((s) => s.pts);

    // A subject only counts once: keep its best result.
    const bestBySubject = new Map();
    const duplicates = new Set();
    for (const s of graded) {
      const key = s.row.subject;
      if (!key) continue;
      const held = bestBySubject.get(key);
      if (!held) { bestBySubject.set(key, s); continue; }
      if (s.pts.total > held.pts.total) { duplicates.add(held.index); bestBySubject.set(key, s); }
      else duplicates.add(s.index);
    }

    // Sort by points including the bonus, so the bonus only helps if Maths makes the top six.
    const eligible = graded
      .filter((s) => !duplicates.has(s.index))
      .sort((a, b) => b.pts.total - a.pts.total || a.index - b.index);
    const counted = eligible.slice(0, COUNTED);
    const countedIdx = new Set(counted.map((s) => s.index));
    const total = counted.reduce((n, s) => n + s.pts.total, 0);
    const bonus = counted.reduce((n, s) => n + s.pts.bonus, 0);

    const status = scored.map((s) => {
      if (!s.pts) return { index: s.index, state: "empty", points: null };
      if (duplicates.has(s.index)) return { index: s.index, state: "duplicate", points: s.pts };
      return { index: s.index, state: countedIdx.has(s.index) ? "counted" : "dropped", points: s.pts };
    });

    return {
      total, bonus,
      counted: counted.map((s) => ({ index: s.index, subject: s.row.subject, points: s.pts })),
      status,
      graded: graded.length,
    };
  }

  // Where a grade sits nationally, from grade-stats.js (SEC national statistics).
  // top = % of that subject and level's candidates who got this grade or better.
  const LEVEL_NAMES = { H: "Higher", O: "Ordinary", F: "Foundation" };
  function rank(row, stats) {
    if (!row || !row.grade || row.subject === LCVP) return null;
    const level = row.level || "H";
    const s = stats && stats.subjects && stats.subjects[row.subject] && stats.subjects[row.subject][level];
    const g = Number(row.grade);
    if (!s || !(g >= 1 && g <= 8)) return null;
    let top = 0;
    for (let i = 0; i < g; i++) top += s.p[i];
    top = Math.min(100, Math.round(top * 10) / 10);
    const below = Math.max(0, Math.round((100 - top) * 10) / 10);
    return { top, below, got: s.p[g - 1], n: s.n, level, grade: g, levelName: LEVEL_NAMES[level] };
  }
  const pct = (x) => (x > 0 && x < 1 ? "<1" : String(Math.round(x)));
  // Short label: "Top 29%" for strong grades, "Ahead of 12%" for weaker ones.
  function rankLabel(r) {
    if (!r) return "";
    if (r.top <= 50 || r.grade === 1) return `Top ${pct(r.top)}%`;
    if (r.below >= 0.5) return `Ahead of ${pct(r.below)}%`;
    return `${pct(r.got)}% got this grade`;
  }

  const api = { score, rowPoints, rank, rankLabel, SCALE, LCVP_POINTS, MATHS, LCVP, MATHS_BONUS, MAX: 625 };
  const g = typeof window !== "undefined" ? window : globalThis;
  g.BBPoints = api;

  if (typeof document === "undefined") return;

  // ---------------------------------------------------------------- UI

  const SUBJECTS = [
    "English", "Irish", MATHS, "French", "German", "Spanish", "Italian", "Japanese",
    "Russian", "Mandarin Chinese", "Polish", "Lithuanian", "Portuguese", "Arabic", "Ukrainian",
    "Romanian", "Croatian", "Dutch", "Swedish", "Hungarian", "Czech", "Slovakian", "Latvian",
    "Bulgarian", "Modern Greek", "Latin",
    "Ancient Greek", "Classical Studies", "Biology", "Chemistry", "Physics",
    "Physics and Chemistry", "Agricultural Science", "Applied Mathematics", "Computer Science",
    "Accounting", "Business", "Economics", "Geography", "History", "Politics and Society",
    "Religious Education", "Home Economics", "Physical Education", "Art", "Music",
    "Construction Studies", "Engineering", "Design and Communication Graphics", "Technology",
    LCVP,
  ];
  const PCT = ["90–100%", "80–89%", "70–79%", "60–69%", "50–59%", "40–49%", "30–39%", "0–29%"];
  const LCVP_GRADES = [["D", "Distinction (80–100%)"], ["M", "Merit (65–79%)"], ["P", "Pass (50–64%)"]];
  const STORE = "bb-points-v1";
  const MIN_ROWS = 6;
  const MAX_ROWS = 10;
  const DEFAULT_ROWS = () => ["English", "Irish", MATHS, "", "", "", ""].map((subject) => ({ subject, level: "H", grade: "" }));

  const root = document.getElementById("pc");
  if (!root) return;
  const list = root.querySelector(".pc-rows");
  const addBtn = root.querySelector(".pc-add");
  const resetBtn = root.querySelector(".pc-reset");
  const totalPix = root.querySelector(".pc-total .pix");
  const live = root.querySelector(".pc-live");
  const bar = root.querySelector(".pc-bar");
  const breakdown = root.querySelector(".pc-breakdown");
  const mobileTotal = root.querySelector(".pc-mbar-total");
  const standout = root.querySelector(".pc-standout");
  const STATS = window.BB_GRADE_STATS || null;

  let rows = load() || DEFAULT_ROWS();
  let uid = 0;

  function load() {
    try {
      const saved = JSON.parse(localStorage.getItem(STORE) || "null");
      if (Array.isArray(saved) && saved.length >= MIN_ROWS && saved.length <= MAX_ROWS) {
        return saved.map((r) => ({ subject: String(r.subject || ""), level: ["H", "O", "F"].includes(r.level) ? r.level : "H", grade: String(r.grade || "") }));
      }
    } catch (e) { /* storage unavailable: start fresh */ }
    return null;
  }
  function save() {
    try { localStorage.setItem(STORE, JSON.stringify(rows)); } catch (e) { /* ignore */ }
  }

  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const SHORT = {
    [MATHS]: "Maths", [LCVP]: "LCVP", "Design and Communication Graphics": "DCG",
    "Applied Mathematics": "Applied Maths", "Physical Education": "PE", "Home Economics": "Home Ec",
    "Agricultural Science": "Ag Science", "Politics and Society": "Politics & Society",
    "Construction Studies": "Construction", "Religious Education": "RE", "Physics and Chemistry": "Physics & Chem",
  };
  const short = (name) => SHORT[name] || name;

  function gradeOptions(row) {
    const blank = `<option value="">Grade</option>`;
    if (row.subject === LCVP) {
      return blank + LCVP_GRADES.map(([v, label]) => `<option value="${v}"${row.grade === v ? " selected" : ""}>${label}</option>`).join("");
    }
    const lv = row.level || "H";
    let out = blank;
    for (let g = 1; g <= 8; g++) {
      out += `<option value="${g}"${row.grade === String(g) ? " selected" : ""}>${lv}${g} (${PCT[g - 1]})</option>`;
    }
    return out;
  }

  function subjectOptions(row, i) {
    const taken = new Set(rows.filter((r, j) => j !== i && r.subject).map((r) => r.subject));
    let out = `<option value="">Choose subject</option>`;
    for (const s of SUBJECTS) {
      const mark = taken.has(s) && s !== row.subject ? " (already added)" : "";
      out += `<option value="${esc(s)}"${row.subject === s ? " selected" : ""}>${esc(s + mark)}</option>`;
    }
    return out;
  }

  function levelControl(row, i) {
    if (row.subject === LCVP) return `<div class="pc-level pc-level-na" aria-hidden="true">No level</div>`;
    const levels = [["H", "Higher"], ["O", "Ordinary"]];
    if (row.subject === MATHS) levels.push(["F", "Foundation"]);
    const name = `pc-lv-${uid}-${i}`;
    return `<fieldset class="pc-level"><legend class="sr">Level for subject ${i + 1}</legend>${levels.map(([v, label]) =>
      `<label title="${label}"><input type="radio" name="${name}" value="${v}"${(row.level || "H") === v ? " checked" : ""} data-i="${i}" data-f="level" /><span>${v}</span><span class="sr"> ${label}</span></label>`
    ).join("")}</fieldset>`;
  }

  function render() {
    uid++;
    list.innerHTML = rows.map((row, i) => `
      <li class="pc-row" data-i="${i}">
        <span class="pc-n" aria-hidden="true">${String(i + 1).padStart(2, "0")}</span>
        <label class="pc-field pc-subject"><span class="sr">Subject ${i + 1}</span>
          <select data-i="${i}" data-f="subject">${subjectOptions(row, i)}</select></label>
        ${levelControl(row, i)}
        <label class="pc-field pc-grade"><span class="sr">Grade for subject ${i + 1}</span>
          <select data-i="${i}" data-f="grade">${gradeOptions(row)}</select><span class="pc-rank"></span></label>
        <output class="pc-pts" aria-live="off"></output>
        <button type="button" class="pc-remove" data-i="${i}" aria-label="Remove subject ${i + 1}"${rows.length <= MIN_ROWS ? " disabled" : ""}>×</button>
      </li>`).join("");
    addBtn.disabled = rows.length >= MAX_ROWS;
    update();
  }

  function update() {
    const result = score(rows);
    const items = list.querySelectorAll(".pc-row");
    let best = null;
    result.status.forEach((st) => {
      const li = items[st.index];
      if (!li) return;
      li.dataset.state = st.state;
      const r = rank(rows[st.index], STATS);
      const cap = li.querySelector(".pc-rank");
      if (cap) {
        cap.textContent = r ? `${rankLabel(r)} of ${r.levelName} ${short(rows[st.index].subject)}` : "";
        cap.title = r ? `${r.got}% of ${r.n.toLocaleString("en-IE")} ${r.levelName} Level ${rows[st.index].subject} students got a ${r.level}${r.grade} in ${STATS.year}` : "";
      }
      if (r && st.state !== "duplicate" && (!best || r.top < best.r.top)) best = { r, subject: rows[st.index].subject };
      const out = li.querySelector(".pc-pts");
      if (!st.points) { out.innerHTML = `<span class="pc-pts-num">–</span>`; return; }
      const note = st.state === "dropped" ? "not counted" : st.state === "duplicate" ? "duplicate" : st.points.bonus ? `+${st.points.bonus} bonus` : "counted";
      out.innerHTML = `<span class="pc-pts-num">${st.points.total}</span><span class="pc-pts-note">${note}</span>`;
    });

    // Standout: the grade that ranks highest nationally, not the one with most points.
    if (best) {
      const r = best.r;
      standout.hidden = false;
      standout.innerHTML = `<p class="pc-board-label pc-board-label-sub">Your standout grade</p>
        <p class="pc-standout-line"><b>${esc(short(best.subject))} ${r.level}${r.grade}</b>: ${r.top <= 50 || r.grade === 1 ? `top ${pct(r.top)}%` : `ahead of ${pct(r.below)}%`} of ${r.n.toLocaleString("en-IE")} ${r.levelName} Level students in ${STATS.year}.</p>`;
    } else {
      standout.hidden = true;
      standout.innerHTML = "";
    }

    // Scoreboard
    const t = String(result.total).padStart(3, "0");
    totalPix.setAttribute("data-text", t);
    if (window.PixelText) window.PixelText.render(totalPix);
    totalPix.setAttribute("aria-hidden", "true");
    mobileTotal.textContent = result.total;
    live.textContent = `${result.total} CAO points from ${result.counted.length} of 6 counted subjects${result.bonus ? ", including the 25 point Higher Maths bonus" : ""}.`;

    bar.innerHTML = result.counted.map((c) =>
      `<span class="pc-seg${c.points.bonus ? " pc-seg-bonus" : ""}" style="flex-basis:${(c.points.total / 625) * 100}%" title="${esc(short(c.subject || "Subject"))}: ${c.points.total}"></span>`
    ).join("");

    const slots = [];
    for (let k = 0; k < 6; k++) {
      const c = result.counted[k];
      slots.push(c
        ? `<li><span>${esc(short(c.subject || `Subject ${c.index + 1}`))}</span><b>${c.points.base}${c.points.bonus ? `<i>+${c.points.bonus}</i>` : ""}</b></li>`
        : `<li class="pc-slot-empty"><span>Empty slot</span><b>–</b></li>`);
    }
    const dropped = result.status.filter((s) => s.state === "dropped");
    breakdown.innerHTML = `<ol>${slots.join("")}</ol>${dropped.length
      ? `<p class="pc-dropped">Not counted: ${dropped.map((s) => esc(short(rows[s.index].subject || `Subject ${s.index + 1}`)) + ` (${s.points.total})`).join(", ")}</p>`
      : ""}`;
  }

  list.addEventListener("change", (e) => {
    const el = e.target;
    const i = Number(el.dataset.i);
    const f = el.dataset.f;
    if (!rows[i] || !f) return;
    const row = rows[i];
    if (f === "subject") {
      const wasLcvp = row.subject === LCVP;
      row.subject = el.value;
      if (row.subject === LCVP || wasLcvp) row.grade = "";
      if (row.level === "F" && row.subject !== MATHS) { row.level = "O"; }
      save(); render();
      const next = list.querySelector(`.pc-row[data-i="${i}"] .pc-grade select`);
      if (next && row.subject && !row.grade) next.focus();
      return;
    }
    if (f === "level") {
      row.level = el.value;
      save(); render();
      const same = list.querySelector(`.pc-row[data-i="${i}"] input[value="${el.value}"]`);
      if (same) same.focus();
      return;
    }
    if (f === "grade") { row.grade = el.value; save(); update(); }
  });

  list.addEventListener("click", (e) => {
    const btn = e.target.closest(".pc-remove");
    if (!btn || rows.length <= MIN_ROWS) return;
    rows.splice(Number(btn.dataset.i), 1);
    save(); render();
  });

  addBtn.addEventListener("click", () => {
    if (rows.length >= MAX_ROWS) return;
    rows.push({ subject: "", level: "H", grade: "" });
    save(); render();
    const sel = list.querySelector(`.pc-row[data-i="${rows.length - 1}"] .pc-subject select`);
    if (sel) sel.focus();
  });

  resetBtn.addEventListener("click", () => {
    rows = DEFAULT_ROWS();
    try { localStorage.removeItem(STORE); } catch (e) { /* ignore */ }
    render();
  });

  root.classList.add("pc-ready");
  render();
})();
