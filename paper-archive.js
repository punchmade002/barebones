// Exam papers: every whole past paper for a subject, opened one page at a time in a viewer
// with a page strip along the bottom and a pen, highlighter, text boxes and an eraser for
// writing on it.
// exam-papers.js (scripts/build_exam_papers.py) holds a short summary per subject; a subject's
// paper list (exam-papers/<subject>/papers.js) loads when its archive is opened, and a paper's
// PDF only when that paper is opened. PDF.js is fetched the first time a paper is opened, and a
// student's markup is kept in this browser per paper.

const PDFJS_SRC = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js";
const PDFJS_WORKER = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
const PAPER_INK_KEY = "bb-paper-ink:";
const LEVEL_NAMES = {
  higher: "Higher level",
  ordinary: "Ordinary level",
  foundation: "Foundation level",
  common: "Both levels",
};

// Line widths and the eraser's reach are fractions of the page width, so markup keeps its
// place and weight at every zoom
const PAPER_TOOLS = {
  pen: { width: 0.0028, alpha: 1, colors: ["#1A1916", "#DC2626", "#2563EB"] },
  highlighter: { width: 0.02, alpha: 0.42, colors: ["#FACC15", "#4ADE80", "#F472B6"] },
  eraser: { reach: 0.012 },
  // A text box's font size; 0.022 of the width sits just above the paper's own print
  text: { size: 0.022, colors: ["#1A1916", "#DC2626", "#2563EB"] },
};

const papersState = { subjectId: "", level: "all" };
const viewer = {
  paper: null,
  doc: null,
  loadId: 0,
  page: 1,
  zoom: 1,
  tool: "view",
  colors: {
    pen: PAPER_TOOLS.pen.colors[0],
    highlighter: PAPER_TOOLS.highlighter.colors[0],
    text: PAPER_TOOLS.text.colors[0],
  },
  ink: {},
  undo: {},
  stroke: null,
  erasing: false,
  pointerId: null,
  renderTask: null,
  thumbQueue: [],
  thumbBusy: false,
  thumbObserver: null,
};

const pv = {};
let pdfjsLoading = null;

function hasExamPapers(subjectId) {
  return window.EXAM_PAPERS?.[subjectId]?.papers > 0;
}

// A subject's paper list, once its script has loaded
function paperList(subjectId) {
  return window.EXAM_PAPER_LISTS?.[subjectId] || null;
}

const paperListLoads = new Map();

function loadPaperList(subjectId) {
  if (paperList(subjectId)) return Promise.resolve();
  if (paperListLoads.has(subjectId)) return paperListLoads.get(subjectId);
  const promise = new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = window.EXAM_PAPERS[subjectId].list;
    script.onload = () => (paperList(subjectId) ? resolve() : reject(new Error("Empty paper list")));
    script.onerror = () => {
      paperListLoads.delete(subjectId);
      script.remove();
      reject(new Error(`Could not load the paper list for ${subjectId}`));
    };
    document.head.appendChild(script);
  });
  paperListLoads.set(subjectId, promise);
  return promise;
}

function oldCourseTag() {
  return `<span class="paper-tag-old">Old Course</span>`;
}

// ── Archive ──────────────────────────────────────────────

function openExamPapers(subjectId) {
  if (!hasExamPapers(subjectId)) return;
  if (papersState.subjectId !== subjectId) papersState.level = "all";
  papersState.subjectId = subjectId;
  renderPapersArchive();
  if (!paperList(subjectId)) {
    loadPaperList(subjectId).then(() => {
      if (papersState.subjectId === subjectId) renderPapersArchive();
    }, (error) => {
      console.error(error);
      if (papersState.subjectId === subjectId) renderPapersArchive(true);
    });
  }
  document.getElementById("papersScreen").classList.remove("hidden");
  document.getElementById("papersScreen").scrollTop = 0;
  document.body.style.overflow = "hidden";
  pushPhoneScreen("papers");
}

function closeExamPapers() {
  closePaperViewer();
  document.getElementById("papersScreen").classList.add("hidden");
  document.body.style.overflow = "";
}

function renderPapersArchive(failed = false) {
  const summary = window.EXAM_PAPERS[papersState.subjectId];
  const subject = SUBJECTS.find((s) => s.id === papersState.subjectId);
  document.getElementById("papersKicker").textContent = subject?.title || "";

  const list = paperList(papersState.subjectId);
  if (!list) {
    document.getElementById("papersBody").innerHTML = `<p class="papers-status">${failed
      ? "The papers could not be loaded. Check your connection and open them again."
      : "Loading papers…"}</p>`;
    return;
  }
  const archive = { ...summary, papers: list };

  const levels = [...new Set(archive.papers.map((p) => p.level))];
  const shown = archive.papers.filter((p) => papersState.level === "all" || p.level === papersState.level || p.level === "common");
  const years = [...new Set(shown.map((p) => p.year))];

  // "Both levels" papers belong to every level, so they get no button of their own
  const filters = ["all", ...levels.filter((level) => level !== "common")].map((level) => `
    <button class="papers-filter${papersState.level === level ? " is-active" : ""}" type="button"
      data-level="${level}" aria-pressed="${papersState.level === level}">
      ${level === "all" ? "All levels" : LEVEL_NAMES[level] || level}
    </button>`).join("");

  const note = archive.papers.some((p) => p.oldCourse)
    ? `<p class="papers-note">${oldCourseTag()}
        <span>Set before the ${escapeHtml(archive.course)} was first examined in ${archive.firstExamined}. Still good practice, but some questions cover topics that are no longer on the course.</span>
      </p>`
    : "";

  const rows = years.map((year, i) => {
    const inYear = shown.filter((p) => p.year === year);
    const old = inYear.some((p) => p.oldCourse);
    const groups = levels.filter((level) => inYear.some((p) => p.level === level)).map((level) => `
      <div class="papers-level">
        <h3>${LEVEL_NAMES[level] || level}</h3>
        <div class="papers-sheets">
          ${inYear.filter((p) => p.level === level).map((p) => paperSheet(archive, p)).join("")}
        </div>
      </div>`).join("");
    return `
      <section class="papers-year" style="--i:${i}">
        <div class="papers-year-head">
          <h2>${year}</h2>
          ${old ? oldCourseTag() : ""}
        </div>
        <div class="papers-levels">${groups}</div>
      </section>`;
  }).join("");

  const body = document.getElementById("papersBody");
  body.innerHTML = `
    <div class="papers-toolbar">
      <div class="papers-filters" role="group" aria-label="Level">${filters}</div>
      <span class="papers-count">${shown.filter((p) => p.kind === "papers").length} papers · ${years.length} years</span>
    </div>
    ${note}
    <div class="papers-years">${rows}</div>`;

  body.querySelectorAll("[data-level]").forEach((button) => {
    button.addEventListener("click", () => {
      papersState.level = button.dataset.level;
      renderPapersArchive();
    });
  });
  body.querySelectorAll("[data-paper]").forEach((button) => {
    button.addEventListener("click", () => {
      openPaperViewer(archive.papers[Number(button.dataset.paper)]);
    });
  });
}

function paperSheet(archive, paper) {
  const index = archive.papers.indexOf(paper);
  const scheme = paper.kind === "scheme";
  const marked = Object.keys(loadPaperInk(paper.file)).length > 0;
  return `
    <button class="paper-sheet${scheme ? " paper-sheet--scheme" : ""}" type="button" data-paper="${index}"
      aria-label="${paper.year} ${LEVEL_NAMES[paper.level] || paper.level}, ${escapeHtml(paper.label)}">
      <span class="paper-sheet-kind">${scheme ? "Answers" : "Paper"}</span>
      <strong class="paper-sheet-label">${escapeHtml(paper.label)}</strong>
      ${marked ? `<span class="paper-sheet-marked">Your notes</span>` : ""}
    </button>`;
}

// ── Viewer ───────────────────────────────────────────────

function loadPdfJs() {
  if (window.pdfjsLib) return Promise.resolve(window.pdfjsLib);
  if (!pdfjsLoading) {
    pdfjsLoading = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = PDFJS_SRC;
      script.onload = () => {
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS_WORKER;
        resolve(window.pdfjsLib);
      };
      script.onerror = () => {
        pdfjsLoading = null;
        reject(new Error("PDF.js did not load"));
      };
      document.head.appendChild(script);
    });
  }
  return pdfjsLoading;
}

async function openPaperViewer(paper) {
  const loadId = ++viewer.loadId;
  viewer.paper = paper;
  viewer.page = 1;
  viewer.zoom = 1;
  viewer.ink = loadPaperInk(paper.file);
  viewer.undo = {};
  viewer.doc?.destroy();
  viewer.doc = null;

  const levelName = LEVEL_NAMES[paper.level] || paper.level;
  pv.title.textContent = `${paper.year} · ${levelName} · ${paper.label}`;
  pv.tag.innerHTML = paper.oldCourse ? oldCourseTag() : "";
  pv.open.href = paper.file;
  pv.strip.innerHTML = "";
  pv.textLayer.innerHTML = "";
  pv.textLayer.dataset.key = "";
  pv.pageLabel.textContent = "";
  pv.sheet.classList.add("is-loading");
  setPaperStatus("Opening the paper…");
  pv.root.classList.remove("hidden");
  document.body.style.overflow = "hidden";
  pushPhoneScreen("paper");

  try {
    const pdfjs = await loadPdfJs();
    // Fetch only the parts of the file the pages on screen need (where the server allows
    // range requests) rather than streaming the whole PDF in the background
    const doc = await pdfjs.getDocument({ url: paper.file, disableAutoFetch: true, disableStream: true }).promise;
    if (loadId !== viewer.loadId) { doc.destroy(); return; }
    viewer.doc = doc;
    setPaperStatus("");
    await buildPageStrip();
    showPaperPage(1);
    // Pick up markup saved from another device without blocking the paper itself
    pullPaperInk(paper.file).then((remoteInk) => {
      if (!remoteInk || loadId !== viewer.loadId) return;
      viewer.ink = remoteInk;
      viewer.undo = {};
      pv.strip.querySelectorAll(".pv-thumb").forEach((thumb) => {
        thumb.classList.toggle("has-ink", Boolean(viewer.ink[thumb.dataset.page]?.length));
      });
      drawPaperInk();
    }).catch((error) => console.error("Could not load paper markup from your account", error));
  } catch (error) {
    if (loadId !== viewer.loadId) return;
    console.error(error);
    setPaperStatus("This paper could not be opened here.");
    pv.status.insertAdjacentHTML("beforeend", ` <a href="${escapeHtml(paper.file)}" target="_blank" rel="noopener">Open the PDF</a> instead.`);
  }
}

function closePaperViewer() {
  if (pv.root.classList.contains("hidden")) return;
  viewer.loadId++;
  viewer.renderTask?.cancel();
  viewer.thumbObserver?.disconnect();
  viewer.thumbQueue = [];
  viewer.doc?.destroy();
  viewer.doc = null;
  pv.root.classList.add("hidden");
  // Back on the archive, which still covers the page; refresh its "Your notes" marks
  if (!document.getElementById("papersScreen").classList.contains("hidden")) renderPapersArchive();
  else document.body.style.overflow = "";
}

function setPaperStatus(text) {
  pv.status.textContent = text;
  pv.status.classList.toggle("hidden", !text);
}

function showPaperPage(n) {
  if (!viewer.doc) return;
  const page = Math.min(Math.max(1, n), viewer.doc.numPages);
  const turned = page !== viewer.page;
  viewer.page = page;
  viewer.stroke = null;
  viewer.pointerId = null;
  pv.pageLabel.textContent = `Page ${page} of ${viewer.doc.numPages}`;
  pv.prev.disabled = page === 1;
  pv.next.disabled = page === viewer.doc.numPages;
  pv.strip.querySelectorAll(".pv-thumb").forEach((thumb) => {
    const active = Number(thumb.dataset.page) === page;
    thumb.classList.toggle("is-active", active);
    thumb.setAttribute("aria-current", active ? "page" : "false");
    if (active) thumb.scrollIntoView({ block: "nearest", inline: "center", behavior: turned ? "smooth" : "auto" });
  });
  if (turned) pv.stage.scrollTo(0, 0);
  renderPaperPage();
}

async function renderPaperPage() {
  const doc = viewer.doc;
  if (!doc) return;
  const pageNumber = viewer.page;
  const page = await doc.getPage(pageNumber);
  if (doc !== viewer.doc || pageNumber !== viewer.page) return;

  const base = page.getViewport({ scale: 1 });
  // Fit inside the stage's padding, which leaves room for the floating tools
  const style = getComputedStyle(pv.stage);
  const padX = parseFloat(style.paddingLeft) + parseFloat(style.paddingRight);
  const padY = parseFloat(style.paddingTop) + parseFloat(style.paddingBottom);
  const fit = Math.min(
    (pv.stage.clientWidth - padX) / base.width,
    (pv.stage.clientHeight - padY) / base.height,
  );
  const scale = Math.max(0.2, fit * viewer.zoom);
  const viewport = page.getViewport({ scale });
  const ratio = window.devicePixelRatio || 1;
  const width = Math.floor(viewport.width);
  const height = Math.floor(viewport.height);

  // Draw off-screen, then swap in, so the old page stays up until the new one is ready
  const canvas = document.createElement("canvas");
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  viewer.renderTask?.cancel();
  const task = page.render({
    canvasContext: canvas.getContext("2d"),
    viewport,
    transform: ratio !== 1 ? [ratio, 0, 0, ratio, 0, 0] : null,
  });
  viewer.renderTask = task;
  try {
    await task.promise;
  } catch (error) {
    if (error?.name !== "RenderingCancelledException") console.error(error);
    return;
  }
  if (doc !== viewer.doc || pageNumber !== viewer.page) return;

  pv.page.width = canvas.width;
  pv.page.height = canvas.height;
  pv.page.getContext("2d").drawImage(canvas, 0, 0);
  for (const el of [pv.page, pv.ink]) {
    el.style.width = `${width}px`;
    el.style.height = `${height}px`;
  }
  pv.ink.width = canvas.width;
  pv.ink.height = canvas.height;
  pv.sheet.style.setProperty("--pv-w", `${width}px`);
  pv.sheet.classList.remove("is-loading");
  // Text boxes scale with --pv-w, so a zoom keeps them (and any box being typed in) as they are
  if (pv.textLayer.dataset.key !== `${viewer.paper.file}#${pageNumber}`) renderPaperText();
  pv.stage.classList.toggle("can-pan",
    pv.stage.scrollWidth > pv.stage.clientWidth + 1 || pv.stage.scrollHeight > pv.stage.clientHeight + 1);
  pv.zoomFit.textContent = viewer.zoom === 1 ? "Fit" : `${Math.round(viewer.zoom * 100)}%`;
  drawPaperInk();
}

function setPaperZoom(zoom) {
  viewer.zoom = Math.min(4, Math.max(0.5, Math.round(zoom * 100) / 100));
  renderPaperPage();
}

// ── Page strip ───────────────────────────────────────────

async function buildPageStrip() {
  const doc = viewer.doc;
  const first = await doc.getPage(1);
  if (doc !== viewer.doc) return;
  const base = first.getViewport({ scale: 1 });
  pv.strip.style.setProperty("--thumb-ratio", `${base.width} / ${base.height}`);
  pv.strip.innerHTML = Array.from({ length: doc.numPages }, (_, i) => `
    <button class="pv-thumb${viewer.ink[i + 1]?.length ? " has-ink" : ""}" type="button" data-page="${i + 1}" aria-label="Page ${i + 1}">
      <canvas></canvas>
      <span>${i + 1}</span>
    </button>`).join("");

  viewer.thumbObserver?.disconnect();
  viewer.thumbQueue = [];
  viewer.thumbObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      viewer.thumbObserver.unobserve(entry.target);
      viewer.thumbQueue.push(entry.target);
    });
    drainThumbQueue();
  }, { root: pv.strip, rootMargin: "0px 240px" });

  pv.strip.querySelectorAll(".pv-thumb").forEach((thumb) => {
    thumb.addEventListener("click", () => showPaperPage(Number(thumb.dataset.page)));
    viewer.thumbObserver.observe(thumb);
  });
}

// Thumbnails render one at a time so they never hold up the page being read
async function drainThumbQueue() {
  if (viewer.thumbBusy) return;
  viewer.thumbBusy = true;
  const doc = viewer.doc;
  while (viewer.thumbQueue.length && doc === viewer.doc) {
    const thumb = viewer.thumbQueue.shift();
    try {
      const page = await doc.getPage(Number(thumb.dataset.page));
      const canvas = thumb.querySelector("canvas");
      const ratio = window.devicePixelRatio || 1;
      const base = page.getViewport({ scale: 1 });
      const viewport = page.getViewport({ scale: (thumb.clientWidth * ratio) / base.width });
      canvas.width = Math.floor(viewport.width);
      canvas.height = Math.floor(viewport.height);
      await page.render({ canvasContext: canvas.getContext("2d"), viewport }).promise;
      thumb.classList.add("is-drawn");
    } catch (error) {
      if (doc !== viewer.doc) break;
      console.error(error);
    }
  }
  viewer.thumbBusy = false;
}

// ── Markup ───────────────────────────────────────────────

function paperInkKey(file) {
  const user = typeof state !== "undefined" ? state.session?.currentUser : "";
  return `${PAPER_INK_KEY}${user || "guest"}:${file}`;
}

function loadPaperInk(file) {
  try {
    return JSON.parse(localStorage.getItem(paperInkKey(file))) || {};
  } catch (error) {
    return {};
  }
}

// ── Account sync ─────────────────────────────────────────
// The browser copy stays the working copy (it works offline and for guests). Signed-in
// users also get one row per paper in their account. Per paper, the last save wins;
// a local edit that hasn't reached the account yet is marked dirty and wins on open.
const INK_SYNC_KEY = "bb-paper-ink-sync:";
const inkSyncTimers = {};

function inkAuth() {
  const auth = window.BarebonesAuth;
  const user = typeof state !== "undefined" ? state.session?.currentUser : "";
  return auth?.configured && user && auth.getSession() ? auth : null;
}

function inkSyncKey(file) {
  return paperInkKey(file).replace(PAPER_INK_KEY, INK_SYNC_KEY);
}

function readInkSync(file) {
  try { return JSON.parse(localStorage.getItem(inkSyncKey(file))) || {}; } catch (error) { return {}; }
}

function queueInkSync(file) {
  const auth = inkAuth();
  if (!auth) return;
  const localKey = paperInkKey(file);
  const syncKey = inkSyncKey(file);
  try { localStorage.setItem(syncKey, JSON.stringify({ ...readInkSync(file), dirty: true })); } catch (error) { /* quota */ }
  clearTimeout(inkSyncTimers[localKey]);
  inkSyncTimers[localKey] = setTimeout(async () => {
    try {
      const raw = localStorage.getItem(localKey);
      const at = await auth.savePaperInk(file, raw ? JSON.parse(raw) : {});
      if (at) localStorage.setItem(syncKey, JSON.stringify({ at, dirty: false }));
    } catch (error) {
      console.error("Could not sync paper markup", error);
    }
  }, 800);
}

// Called when a paper opens. Returns the account's markup if it should replace what is
// on screen, otherwise null (and uploads local markup the account doesn't have yet).
async function pullPaperInk(file) {
  const auth = inkAuth();
  if (!auth) return null;
  const remote = await auth.loadPaperInk(file);
  const local = loadPaperInk(file);
  const sync = readInkSync(file);
  const localHasInk = Object.keys(local).length > 0;
  const remoteHasInk = remote && Object.keys(remote.data).length > 0;
  if (!remote || sync.dirty || (!remoteHasInk && localHasInk && !sync.at)) {
    if (localHasInk || remote) queueInkSync(file);
    return null;
  }
  if (sync.at === remote.updatedAt) return null;
  // Markup made here before this paper was ever synced: keep its pages alongside the account's
  const incoming = !sync.at && localHasInk && remoteHasInk ? { ...local, ...remote.data } : remote.data;
  try {
    if (remoteHasInk) localStorage.setItem(paperInkKey(file), JSON.stringify(incoming));
    else localStorage.removeItem(paperInkKey(file));
    localStorage.setItem(inkSyncKey(file), JSON.stringify({ at: remote.updatedAt, dirty: false }));
  } catch (error) {
    console.error(error);
  }
  if (incoming !== remote.data) queueInkSync(file);
  return incoming;
}

function savePaperInk() {
  viewer.ink = Object.fromEntries(Object.entries(viewer.ink).filter(([, items]) => items.length));
  // A text box still empty (just placed, not typed in yet) isn't kept
  const stored = Object.fromEntries(Object.entries(viewer.ink)
    .map(([page, items]) => [page, items.filter((item) => item.tool !== "text" || item.text.trim())])
    .filter(([, items]) => items.length));
  try {
    if (Object.keys(stored).length) localStorage.setItem(paperInkKey(viewer.paper.file), JSON.stringify(stored));
    else localStorage.removeItem(paperInkKey(viewer.paper.file));
  } catch (error) {
    console.error(error);
  }
  queueInkSync(viewer.paper.file);
  pv.strip.querySelector(`.pv-thumb[data-page="${viewer.page}"]`)
    ?.classList.toggle("has-ink", Boolean(stored[viewer.page]?.length));
}

function pageStrokes() {
  if (!viewer.ink[viewer.page]) viewer.ink[viewer.page] = [];
  return viewer.ink[viewer.page];
}

function rememberForUndo() {
  pushUndo(JSON.stringify(pageStrokes()));
}

function undoPaperInk() {
  const stack = viewer.undo[viewer.page];
  if (!stack?.length) return;
  viewer.ink[viewer.page] = JSON.parse(stack.pop());
  savePaperInk();
  drawPaperInk();
  renderPaperText();
}

function clearPaperPage() {
  if (!viewer.ink[viewer.page]?.length) return;
  rememberForUndo();
  viewer.ink[viewer.page] = [];
  savePaperInk();
  drawPaperInk();
  renderPaperText();
}

function drawPaperInk() {
  const ctx = pv.ink.getContext("2d");
  const w = pv.ink.width;
  const h = pv.ink.height;
  ctx.clearRect(0, 0, w, h);
  const strokes = (viewer.ink[viewer.page] || []).filter((item) => item.tool !== "text");
  if (viewer.stroke) strokes.push(viewer.stroke);
  // Highlighter goes under the pen so written answers stay crisp on top
  strokes.sort((a, b) => (a.tool === "highlighter" ? 0 : 1) - (b.tool === "highlighter" ? 0 : 1));
  strokes.forEach((stroke) => {
    const tool = PAPER_TOOLS[stroke.tool];
    const pts = stroke.points.map(([x, y]) => [x * w, y * h]);
    ctx.globalAlpha = tool.alpha;
    ctx.strokeStyle = ctx.fillStyle = stroke.color;
    ctx.lineWidth = stroke.width * w;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    if (pts.length === 1) {
      ctx.beginPath();
      ctx.arc(pts[0][0], pts[0][1], ctx.lineWidth / 2, 0, Math.PI * 2);
      ctx.fill();
      return;
    }
    // Curve through the midpoints so fast strokes don't look faceted
    ctx.beginPath();
    ctx.moveTo(pts[0][0], pts[0][1]);
    for (let i = 1; i < pts.length - 1; i++) {
      const mx = (pts[i][0] + pts[i + 1][0]) / 2;
      const my = (pts[i][1] + pts[i + 1][1]) / 2;
      ctx.quadraticCurveTo(pts[i][0], pts[i][1], mx, my);
    }
    const last = pts[pts.length - 1];
    ctx.lineTo(last[0], last[1]);
    ctx.stroke();
  });
  ctx.globalAlpha = 1;
}

function inkPoint(event) {
  const rect = pv.ink.getBoundingClientRect();
  return [(event.clientX - rect.left) / rect.width, (event.clientY - rect.top) / rect.height];
}

function eraseAt([x, y]) {
  const strokes = pageStrokes();
  const aspect = pv.ink.height / pv.ink.width;
  const reach = PAPER_TOOLS.eraser.reach;
  // Distances are measured in page widths so the eraser is round on the page
  const near = (stroke) => stroke.tool !== "text" && stroke.points.some(([px, py], i) => {
    const [qx, qy] = stroke.points[i + 1] || [px, py];
    const ax = px, ay = py * aspect, bx = qx, by = qy * aspect, cx = x, cy = y * aspect;
    const len = (bx - ax) ** 2 + (by - ay) ** 2;
    const t = len ? Math.max(0, Math.min(1, ((cx - ax) * (bx - ax) + (cy - ay) * (by - ay)) / len)) : 0;
    const dx = ax + t * (bx - ax) - cx;
    const dy = ay + t * (by - ay) - cy;
    return Math.hypot(dx, dy) <= reach + stroke.width / 2;
  });
  const kept = strokes.filter((stroke) => !near(stroke));
  if (kept.length === strokes.length) return;
  if (!viewer.erasing) {
    rememberForUndo();
    viewer.erasing = true;
  }
  viewer.ink[viewer.page] = kept;
  drawPaperInk();
}

function bindPaperInk() {
  pv.ink.addEventListener("pointerdown", (event) => {
    if (viewer.tool === "view" || event.button > 0) return;
    if (viewer.tool === "text") {
      event.preventDefault();
      placeTextBox(inkPoint(event));
      return;
    }
    if (viewer.pointerId !== null) return;
    event.preventDefault();
    viewer.pointerId = event.pointerId;
    try { pv.ink.setPointerCapture(event.pointerId); } catch (error) { /* drawing still works without it */ }
    if (viewer.tool === "eraser") {
      viewer.erasing = false;
      eraseAt(inkPoint(event));
      return;
    }
    const tool = PAPER_TOOLS[viewer.tool];
    // A stylus presses harder for a heavier line; mice and fingers draw at the set width
    const pressure = event.pointerType === "pen" && event.pressure ? 0.6 + event.pressure * 0.8 : 1;
    viewer.stroke = {
      tool: viewer.tool,
      color: viewer.colors[viewer.tool],
      width: viewer.tool === "pen" ? tool.width * pressure : tool.width,
      points: [inkPoint(event)],
    };
    drawPaperInk();
  });
  pv.ink.addEventListener("pointermove", (event) => {
    if (event.pointerId !== viewer.pointerId) return;
    // Coalesced events give a smooth line from a fast stylus; some browsers return none
    const coalesced = event.getCoalescedEvents?.();
    const events = coalesced?.length ? coalesced : [event];
    if (viewer.tool === "eraser") {
      events.forEach((e) => eraseAt(inkPoint(e)));
      return;
    }
    if (!viewer.stroke) return;
    events.forEach((e) => viewer.stroke.points.push(inkPoint(e)));
    drawPaperInk();
  });
  const finish = (event) => {
    if (event.pointerId !== viewer.pointerId) return;
    viewer.pointerId = null;
    if (pv.ink.hasPointerCapture(event.pointerId)) pv.ink.releasePointerCapture(event.pointerId);
    if (viewer.tool === "eraser") {
      eraseAt(inkPoint(event));
      if (viewer.erasing) savePaperInk();
      viewer.erasing = false;
      return;
    }
    if (!viewer.stroke) return;
    const end = inkPoint(event);
    const last = viewer.stroke.points[viewer.stroke.points.length - 1];
    if (end[0] !== last[0] || end[1] !== last[1]) viewer.stroke.points.push(end);
    rememberForUndo();
    // Keep 4 decimal places: finer than a pixel at any zoom, and a quarter of the storage
    viewer.stroke.points = viewer.stroke.points.map(([x, y]) => [Math.round(x * 1e4) / 1e4, Math.round(y * 1e4) / 1e4]);
    pageStrokes().push(viewer.stroke);
    viewer.stroke = null;
    savePaperInk();
    drawPaperInk();
  };
  pv.ink.addEventListener("pointerup", finish);
  pv.ink.addEventListener("pointercancel", finish);
}

// ── Text boxes ───────────────────────────────────────────

function renderPaperText() {
  if (pv.textLayer.contains(document.activeElement)) document.activeElement.blur();
  pv.textLayer.dataset.key = viewer.paper ? `${viewer.paper.file}#${viewer.page}` : "";
  pv.textLayer.innerHTML = "";
  (viewer.ink[viewer.page] || []).forEach((item) => {
    if (item.tool === "text") pv.textLayer.appendChild(makeTextBox(item));
  });
}

// The text tool places one box where the page is next clicked, then hands back to Move
function placeTextBox([x, y]) {
  const before = JSON.stringify(pageStrokes());
  const item = {
    tool: "text",
    x: Math.round(x * 1e4) / 1e4,
    y: Math.round(y * 1e4) / 1e4,
    color: viewer.colors.text,
    size: PAPER_TOOLS.text.size,
    text: "",
  };
  pageStrokes().push(item);
  const box = makeTextBox(item, before);
  pv.textLayer.appendChild(box);
  setPaperTool("view");
  box.focus();
}

function makeTextBox(item, newBefore = null) {
  const box = document.createElement("div");
  box.className = "pv-textbox";
  try {
    box.contentEditable = "plaintext-only";
  } catch (error) {
    box.contentEditable = "true";
  }
  box.spellcheck = false;
  box.setAttribute("role", "textbox");
  box.setAttribute("aria-label", "Text box");
  box.style.left = `${item.x * 100}%`;
  box.style.top = `${item.y * 100}%`;
  box.style.maxWidth = `${(1 - item.x) * 100}%`;
  box.style.color = item.color;
  box.style.fontSize = `calc(var(--pv-w) * ${item.size})`;
  box.textContent = item.text;

  // Undo steps back over a whole edit, from focus to blur, rather than each keystroke
  let before = newBefore;
  let startText = item.text;
  box.addEventListener("focus", () => {
    if (newBefore === null) before = JSON.stringify(pageStrokes());
    startText = item.text;
  });
  box.addEventListener("input", () => {
    item.text = box.innerText.replace(/\n$/, "");
    savePaperInk();
  });
  box.addEventListener("blur", () => {
    const strokes = viewer.ink[viewer.page] || [];
    if (!strokes.includes(item)) return;
    if (!item.text.trim()) {
      strokes.splice(strokes.indexOf(item), 1);
      box.remove();
      if (newBefore === null) pushUndo(before);
    } else if (newBefore !== null || item.text !== startText) {
      pushUndo(before);
    }
    newBefore = null;
    savePaperInk();
  });
  // Typing stays in the box: the viewer's and the app's key shortcuts don't see it
  box.addEventListener("keydown", (event) => event.stopPropagation());
  box.addEventListener("pointerdown", (event) => {
    if (viewer.tool === "eraser") {
      event.preventDefault();
      const strokes = pageStrokes();
      pushUndo(JSON.stringify(strokes));
      strokes.splice(strokes.indexOf(item), 1);
      box.remove();
      savePaperInk();
      return;
    }
    if (viewer.tool === "view" && event.button === 0 && document.activeElement !== box) dragTextBox(event, box, item);
  });
  return box;
}

// With Move, pressing a text box and moving drags it; a press that doesn't move is a click,
// which puts the cursor in the box where it was clicked
function dragTextBox(event, box, item) {
  event.preventDefault();
  const sheet = pv.sheet.getBoundingClientRect();
  const start = { x: event.clientX, y: event.clientY, itemX: item.x, itemY: item.y };
  const snapshot = JSON.stringify(pageStrokes());
  let dragging = false;
  try { box.setPointerCapture(event.pointerId); } catch (error) { /* the drag still follows */ }

  const move = (e) => {
    if (e.pointerId !== event.pointerId) return;
    const dx = e.clientX - start.x;
    const dy = e.clientY - start.y;
    if (!dragging && Math.hypot(dx, dy) < 4) return;
    dragging = true;
    box.classList.add("is-dragging");
    item.x = Math.min(0.98, Math.max(0, start.itemX + dx / sheet.width));
    item.y = Math.min(0.99, Math.max(0.01, start.itemY + dy / sheet.height));
    box.style.left = `${item.x * 100}%`;
    box.style.top = `${item.y * 100}%`;
    box.style.maxWidth = `${(1 - item.x) * 100}%`;
  };
  const end = (e) => {
    if (e.pointerId !== event.pointerId) return;
    box.removeEventListener("pointermove", move);
    box.removeEventListener("pointerup", end);
    box.removeEventListener("pointercancel", end);
    box.classList.remove("is-dragging");
    if (dragging) {
      item.x = Math.round(item.x * 1e4) / 1e4;
      item.y = Math.round(item.y * 1e4) / 1e4;
      pushUndo(snapshot);
      savePaperInk();
      return;
    }
    if (e.type === "pointercancel") return;
    box.focus();
    const range = document.caretRangeFromPoint?.(e.clientX, e.clientY);
    if (range && box.contains(range.startContainer)) {
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
    }
  };
  box.addEventListener("pointermove", move);
  box.addEventListener("pointerup", end);
  box.addEventListener("pointercancel", end);
}

// With Move, dragging a zoomed page with a mouse or stylus pans it (fingers already scroll)
function bindPaperPan() {
  let pan = null;
  pv.stage.addEventListener("pointerdown", (event) => {
    if (viewer.tool !== "view" || event.button > 0 || event.pointerType === "touch") return;
    if (event.target.closest(".pv-textbox")) return;
    event.preventDefault();
    pan = { id: event.pointerId, x: event.clientX, y: event.clientY, left: pv.stage.scrollLeft, top: pv.stage.scrollTop };
    try { pv.stage.setPointerCapture(event.pointerId); } catch (error) { /* panning still follows */ }
    pv.stage.classList.add("is-panning");
  });
  pv.stage.addEventListener("pointermove", (event) => {
    if (event.pointerId !== pan?.id) return;
    pv.stage.scrollLeft = pan.left - (event.clientX - pan.x);
    pv.stage.scrollTop = pan.top - (event.clientY - pan.y);
  });
  const end = (event) => {
    if (event.pointerId !== pan?.id) return;
    pan = null;
    pv.stage.classList.remove("is-panning");
  };
  pv.stage.addEventListener("pointerup", end);
  pv.stage.addEventListener("pointercancel", end);
}

function pushUndo(snapshot) {
  const stack = viewer.undo[viewer.page] || (viewer.undo[viewer.page] = []);
  stack.push(snapshot);
  if (stack.length > 60) stack.shift();
}

function setPaperTool(tool) {
  viewer.tool = tool;
  pv.root.dataset.tool = tool;
  pv.root.querySelectorAll("[data-tool]").forEach((button) => {
    const active = button.dataset.tool === tool;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  renderPaperColors();
}

function renderPaperColors() {
  const tool = PAPER_TOOLS[viewer.tool];
  pv.colors.classList.toggle("hidden", !tool?.colors);
  if (!tool?.colors) return;
  pv.colors.innerHTML = tool.colors.map((color) => `
    <button class="pv-swatch${viewer.colors[viewer.tool] === color ? " is-active" : ""}" type="button"
      data-color="${color}" style="--swatch:${color}" aria-label="Colour ${color}"
      aria-pressed="${viewer.colors[viewer.tool] === color}"></button>`).join("");
  pv.colors.querySelectorAll("[data-color]").forEach((button) => {
    button.addEventListener("click", () => {
      viewer.colors[viewer.tool] = button.dataset.color;
      renderPaperColors();
    });
  });
}

// ── Wiring ───────────────────────────────────────────────

function initPaperArchive() {
  const byId = (id) => document.getElementById(id);
  Object.assign(pv, {
    root: byId("paperViewer"),
    title: byId("pvTitle"),
    tag: byId("pvTag"),
    open: byId("pvOpen"),
    stage: byId("pvStage"),
    sheet: byId("pvSheet"),
    page: byId("pvPage"),
    ink: byId("pvInk"),
    textLayer: byId("pvText"),
    prev: byId("pvPrev"),
    next: byId("pvNext"),
    status: byId("pvStatus"),
    strip: byId("pvStrip"),
    pageLabel: byId("pvPageLabel"),
    colors: byId("pvColors"),
    zoomFit: byId("pvZoomFit"),
  });
  if (!pv.root) return;

  byId("closePapers").addEventListener("click", () => leavePhoneScreen("papers", closeExamPapers));
  byId("pvBack").addEventListener("click", () => leavePhoneScreen("paper", closePaperViewer));
  pv.prev.addEventListener("click", () => showPaperPage(viewer.page - 1));
  pv.next.addEventListener("click", () => showPaperPage(viewer.page + 1));
  byId("pvZoomIn").addEventListener("click", () => setPaperZoom(viewer.zoom + 0.25));
  byId("pvZoomOut").addEventListener("click", () => setPaperZoom(viewer.zoom - 0.25));
  pv.zoomFit.addEventListener("click", () => setPaperZoom(1));
  byId("pvUndo").addEventListener("click", undoPaperInk);
  byId("pvClear").addEventListener("click", clearPaperPage);
  pv.root.querySelectorAll("[data-tool]").forEach((button) => {
    button.addEventListener("click", () => setPaperTool(button.dataset.tool));
  });
  bindPaperInk();
  bindPaperPan();
  setPaperTool("view");

  let resizeTimer = 0;
  window.addEventListener("resize", () => {
    if (pv.root.classList.contains("hidden")) return;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(renderPaperPage, 120);
  });

  // Capture phase, so the app's own Escape and arrow-key handlers don't also act underneath
  document.addEventListener("keydown", (event) => {
    const viewerOpen = !pv.root.classList.contains("hidden");
    const archiveOpen = !byId("papersScreen").classList.contains("hidden");
    if (!viewerOpen && !archiveOpen) return;
    if (event.target.isContentEditable) {
      // Escape finishes the text box instead of closing the paper
      if (event.key === "Escape") {
        event.stopImmediatePropagation();
        event.target.blur();
      }
      return;
    }
    if (event.key === "Escape") {
      event.stopImmediatePropagation();
      if (viewerOpen) leavePhoneScreen("paper", closePaperViewer);
      else leavePhoneScreen("papers", closeExamPapers);
      return;
    }
    if (!viewerOpen || event.altKey) return;
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "z") {
      event.preventDefault();
      undoPaperInk();
      return;
    }
    if (event.metaKey || event.ctrlKey) return;
    const keys = {
      ArrowRight: () => showPaperPage(viewer.page + 1),
      ArrowDown: () => showPaperPage(viewer.page + 1),
      PageDown: () => showPaperPage(viewer.page + 1),
      ArrowLeft: () => showPaperPage(viewer.page - 1),
      ArrowUp: () => showPaperPage(viewer.page - 1),
      PageUp: () => showPaperPage(viewer.page - 1),
      Home: () => showPaperPage(1),
      End: () => showPaperPage(viewer.doc?.numPages || 1),
      v: () => setPaperTool("view"),
      p: () => setPaperTool("pen"),
      h: () => setPaperTool("highlighter"),
      e: () => setPaperTool("eraser"),
      t: () => setPaperTool("text"),
    };
    const action = keys[event.key] || keys[event.key.toLowerCase()];
    // Up and down scroll the page instead when it is zoomed past the screen
    const scrolls = pv.stage.scrollHeight > pv.stage.clientHeight + 1;
    if (!action || (scrolls && (event.key === "ArrowUp" || event.key === "ArrowDown"))) return;
    event.preventDefault();
    event.stopImmediatePropagation();
    action();
  }, true);
}

initPaperArchive();
