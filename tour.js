(function () {
  "use strict";

  // First-run tour of a subject page. The questionnaire's last step (onboarding.js) stores the
  // chosen subject in sessionStorage.bb_tour and opens /app/<subject>/; here each section tile is
  // spotlit in turn, then opened on a real chapter for the student to try (flip a card, scroll a note).
  // Uses app.js / dashboard.js globals: PAGE_SUBJECT, PAGE_SUBJECT_DATA, getCurrentUser, sectionsFor,
  // sectionLabel, isAacSection, iconHtml, CRUNCH_FILES, closeTestScreen, isLocalTourPreview.

  const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const reducedMotion = () => window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
  const shown = (el) => el && el.getClientRects().length > 0;
  const click = (el) => el && el.click();
  // The first selector that matches, in the order given (a comma selector would go by document order)
  const first = (...selectors) => () => selectors.map((sel) => document.querySelector(sel)).find(shown);

  async function waitFor(find, timeout = 8000) {
    const end = Date.now() + timeout;
    while (Date.now() < end) {
      const el = typeof find === "string" ? document.querySelector(find) : find();
      if (shown(el)) return el;
      await wait(100);
    }
    return null;
  }

  // A chapter about a third of the way in: past the course's introductory chapters, early enough to be familiar.
  const pick = (list) => list[Math.floor(list.length / 3)];
  const openSection = async (id) => {
    if (location.hash.slice(1) !== id) location.hash = id;
    await wait(250);
  };

  // What each section is (`tile`) and what using it looks like (`inside`). `open` gets the section to a
  // real example and returns the element to spotlight, which the student can then click and scroll.
  // `reserve` is the scroller that gets room at its bottom when the card has to sit over the spotlight;
  // `dock` places the card itself; `bare` shows the section without the dim.
  // `react` maps clicks inside it to a reply on the card; `leave` tidies up before the next step.
  const SECTIONS = {
    guide: {
      tile: "How the paper is laid out: every section, its marks, and how long to spend on it.",
      inside: "Your exam day, question by question: when to start each one so you finish on time. Tap a block on the bar to see that question.",
      open: () => waitFor(first("#examBreakdownContent .bd-day", "#examBreakdownContent .bd-head")),
      react: { ".bd-bar-seg": "That's the plan for that question, with how long it should take." },
    },
    aac: {
      tile: "Your coursework, broken into stages, with what to hand in for each.",
      inside: "Each stage of your coursework with what the examiners look for. Scroll to read through it.",
      open: () => waitFor(first("#examBreakdownContent .aac-brief", "#examBreakdownContent .bd-head")),
    },
    flashcards: {
      tile: "Bite-size cards for every topic on the course, chapter by chapter.",
      inside: "Answer it in your head, then tap Reveal to flip the card yourself.",
      async open() {
        await waitFor("#subjectOverview details");
        const chapters = [...document.querySelectorAll("#subjectOverview details")]
          .filter((d) => !/(^|\s)0\/0(\s|$)/.test(d.querySelector("summary")?.innerText || ""));
        click(pick(chapters)?.querySelector(".chapter-subs button"));
        return waitFor("#flashcardStudy");
      },
      react: {
        "#flipCard": "Did you get it? Tap Mark learned if you did, or → for the next card.",
        "#markLearned": "Learned. It counts toward your progress bar now. Try another with →.",
        "#nextCard": "New card. Flip it with Reveal when you're ready.",
        "#prevCard": "Back one. Flip it with Reveal when you're ready.",
      },
    },
    notes: {
      tile: "Clear notes for every subsection, written to the syllabus.",
      inside: "Scroll to read. The arrows at the sides move between subsections.",
      async open() {
        await waitFor("#sectionPanel .chapter-fold");
        click(pick([...document.querySelectorAll("#sectionPanel .chapter-fold")])?.querySelector(".chapter-subs button"));
        // The whole notes screen: it's fixed to the viewport, so scrolling the note never moves the spotlight
        return waitFor("#fullNotesScreen:not(.hidden)");
      },
      react: { ".notes-pager": "Next subsection. Lock each one in with its flashcards." },
      reserve: "#fullNotesBody",
      leave: () => shown(document.querySelector("#closeFullNotes")) && click(document.querySelector("#closeFullNotes")),
    },
    tests: {
      tile: "Timed tests that mix flashcards with real exam questions.",
      inside: "A real 10 minute test on one chapter. Pick an answer and try a few. This one won't be saved.",
      async open() {
        click(await waitFor("#testContainer .test-start"));
        return waitFor("#testScreen:not(.hidden)");
      },
      // Just above the test's own Back / Next bar, right-aligned, so it never covers a control
      dock(cw, ch) {
        const foot = document.querySelector("#testScreen .test-foot")?.getBoundingClientRect();
        return foot && { cx: innerWidth - cw - 24, cy: Math.min(foot.top, innerHeight) - ch - 12 };
      },
      react: {
        ".test-option": "Answer picked. Next moves on, and the numbered dots jump to any question.",
        '[data-test-action="finish"]': "When you finish, every answer is marked and you see your score.",
      },
      // Discards the test without saving, whatever state the student left it in
      leave: () => { if (shown(document.querySelector("#testScreen"))) closeTestScreen(); },
    },
    exam: {
      tile: "Every past exam question, sorted by chapter.",
      inside: "Have a go at the question, then tap Show Model Answer to check it against the marking scheme.",
      async open() {
        await waitFor("#subjectOverview button.overview-chapter-row");
        const rows = [...document.querySelectorAll("#subjectOverview button.overview-chapter-row")]
          .filter((row) => !row.getAttribute("onclick")?.includes("'own'") && !/(^|\s)0 questions/.test(row.innerText));
        click(pick(rows));
        const header = await waitFor("#examContainer .exam-group-header");
        if (header && header.getAttribute("aria-expanded") === "false") click(header);
        await waitFor("#examContainer .exam-group");
        // The panel the questions scroll in: a fixed frame, so scrolling never slides the spotlight over the text
        return waitFor("#subjectWorkbench");
      },
      reserve: "#subjectWorkbench",
      react: { ".exam-toggle-btn": "That's the official marking scheme answer. Every question in the bank has one." },
    },
    crunch: {
      tile: "Crunch ranks every point in your notes by how much it's worth in the exam, then cuts the least valuable ones first and tells you the paper mark you can still get.",
      inside: "Switch on Crunch at the top, then slide to choose how much less you want to study. The lowest-value points go first, and you see the paper mark what's left is worth.",
      // The whole Crunch card (heading, slider and result), so none of it sits under the dim
      open: () => waitFor(first("#sectionPanel .crunch-settings", "#sectionPanel .crunch-setup")),
      reserve: "#sectionPanel",
      bare: true, // the Crunch page explains itself; no dim needed
      react: {
        "#crunchOn": "Crunch is on. Now slide to choose how much less to study.",
        "#crunchCut": "Bigger cut, lower expected mark. Cut points are only hidden: one tap shows them in your notes and flashcards.",
      },
    },
    skills: {
      tile: "Step-by-step lessons on the core maths skills, each built from a real exam question.",
    },
  };

  function buildSteps() {
    const ids = sectionsFor(PAGE_SUBJECT);
    if (CRUNCH_FILES[PAGE_SUBJECT]) ids.push("crunch");
    if (PAGE_SUBJECT === "maths") ids.unshift("skills");
    return ids.map((id) => ({
      id,
      def: SECTIONS[isAacSection(id) ? "aac" : id],
      label: id === "skills" ? "Skills" : id === "crunch" ? "Crunch Mode" : sectionLabel(PAGE_SUBJECT, id),
      icon: isAacSection(id) ? "aac" : id,
      // Crunch only becomes a tile once it's set up; before that it's the offer bar on the subject page
      tile: id === "skills" ? first('.section-tile[href="maths-skill.html"]')
        : first(`.section-tile[href$="#${id}"]`, ...(id === "crunch" ? [".crunch-bar"] : [])),
    })).filter((s) => s.def);
  }

  function run() {
    const subject = PAGE_SUBJECT_DATA.title;
    const steps = buildSteps();
    let target = null; // the spotlit element; null dims the whole page
    let open = false; // clicks and scrolling reach the spotlit element
    let react = null; // { selector: reply } for clicks inside it
    let busy = false;
    let cleanup = null;
    let reserved = null; // the scroller padded so its content and buttons clear the card
    let dock = null; // a step's own place for the card

    const root = document.createElement("div");
    root.className = "tour";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-labelledby", "tourTitle");
    root.innerHTML = `
      <div class="tour-catch"></div>
      <div class="tour-hole" aria-hidden="true"></div>
      <div class="tour-card">
        <div class="tour-card-top">
          <ol class="tour-rail" aria-hidden="true">${steps.map((s) => `<li>${iconHtml(s.icon)}</li>`).join("")}</ol>
          <span class="tour-count sr-only" aria-live="polite"></span>
          <button type="button" class="tour-skip" data-tour-skip>Skip tour</button>
        </div>
        <h2 id="tourTitle" class="tour-title"></h2>
        <p class="tour-body" aria-live="polite"></p>
        <div class="tour-foot">
          <button type="button" class="tour-alt" data-tour-alt></button>
          <button type="button" class="ob-next tour-next" data-tour-next><span></span>
            <svg class="ob-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </button>
        </div>
      </div>`;
    document.body.appendChild(root);
    document.body.classList.add("tour-open");
    const catcher = root.querySelector(".tour-catch");
    const hole = root.querySelector(".tour-hole");
    const card = root.querySelector(".tour-card");
    const body = root.querySelector(".tour-body");
    const nextBtn = root.querySelector("[data-tour-next]");
    const altBtn = root.querySelector("[data-tour-alt]");
    let primary = null, secondary = null; // what the two buttons do on this screen

    // One loop eases the spotlight and card toward where they should be. Easing by elapsed time keeps
    // the speed the same at any frame rate, and it follows the target smoothly while the page scrolls.
    const now = { x: innerWidth / 2, y: innerHeight / 2, w: 0, h: 0, cx: (innerWidth - 380) / 2, cy: innerHeight };
    let last = performance.now();
    let glideUntil = 0; // ease while moving to a new target, then lock on so scrolling can't make it lag
    let frame = 0;
    function goal() {
      const pad = 8;
      const r = target && shown(target) ? target.getBoundingClientRect() : null;
      let box = null;
      if (r) {
        const top = Math.max(r.top - pad, 8), bottom = Math.min(r.bottom + pad, innerHeight - 8);
        // Scrolled almost out of view: hold the spotlight where it was rather than collapse it
        box = bottom - top > 40 ? { x: r.left - pad, y: top, w: r.width + pad * 2, h: bottom - top } : { x: now.x, y: now.y, w: now.w, h: now.h };
      }
      const spot = box || { x: innerWidth / 2, y: innerHeight / 2, w: 0, h: 0 };
      // Card below the spotlight, else above, else over it in a corner (phones, tall targets)
      const ch = card.offsetHeight, cw = card.offsetWidth, gap = 14;
      let cy, cx;
      const docked = box && dock?.(cw, ch);
      if (docked) ({ cx, cy } = docked);
      else if (!box) { cy = (innerHeight - ch) / 2; cx = (innerWidth - cw) / 2; }
      else if (innerWidth < 640) { cy = innerHeight - ch - 12; cx = (innerWidth - cw) / 2; }
      else if (spot.y + spot.h + gap + ch < innerHeight - 8) { cy = spot.y + spot.h + gap; cx = spot.x; }
      else if (spot.y - gap - ch > 8) { cy = spot.y - gap - ch; cx = spot.x; }
      else { cy = innerHeight - ch - 16; cx = innerWidth - cw - 24; }
      cx = Math.min(Math.max(cx, 16), innerWidth - cw - 16);
      cy = Math.min(Math.max(cy, 8), innerHeight - ch - 8);
      // Sitting over the spotlight: reserve its height at the bottom of the spotlit scroller
      const over = box && cy < spot.y + spot.h && cy + ch > spot.y;
      return { ...spot, cx, cy, reserve: over ? innerHeight - cy + 12 : 0 };
    }
    function tick(time) {
      const dt = Math.min(time - last, 64);
      last = time;
      const to = goal();
      document.documentElement.style.setProperty("--tour-reserve", `${Math.round(to.reserve)}px`);
      const ease = reducedMotion() ? 1 : 1 - Math.exp(-dt / 95);
      // The card always eases (its height changes with its words); the spotlight locks on once it arrives
      const holeK = time > glideUntil ? 1 : ease;
      for (const key of Object.keys(now)) {
        const k = key === "cx" || key === "cy" ? ease : holeK;
        now[key] += (to[key] - now[key]) * k;
        if (Math.abs(to[key] - now[key]) < 0.3) now[key] = to[key];
      }
      hole.style.transform = `translate3d(${now.x}px, ${now.y}px, 0)`;
      hole.style.width = `${now.w}px`;
      hole.style.height = `${now.h}px`;
      card.style.transform = `translate3d(${Math.round(now.cx)}px, ${Math.round(now.cy)}px, 0)`;
      // Cut the same hole out of the click blocker so the spotlit element can be used
      catcher.style.clipPath = open && now.w > 0
        ? `polygon(evenodd, 0 0, 100% 0, 100% 100%, 0 100%, 0 0, ${now.x}px ${now.y}px, ${now.x + now.w}px ${now.y}px, ${now.x + now.w}px ${now.y + now.h}px, ${now.x}px ${now.y + now.h}px, ${now.x}px ${now.y}px)`
        : "";
      frame = requestAnimationFrame(tick);
    }
    frame = requestAnimationFrame(tick);

    // Clicks inside the spotlight get a reply on the card
    function onUse(event) {
      if (!react || !target?.contains(event.target)) return;
      const hit = Object.keys(react).find((sel) => event.target.closest(sel));
      if (hit) setTimeout(() => say(react[hit]), 120);
    }
    function say(text) {
      if (body.textContent === text) return;
      body.classList.add("is-changing");
      setTimeout(() => { body.textContent = text; body.classList.remove("is-changing"); }, 140);
    }

    function spotlight(el) {
      target = el || null;
      glideUntil = performance.now() + 650;
      if (el) el.scrollIntoView({ block: el.offsetHeight > innerHeight * 0.55 ? "start" : "center", behavior: reducedMotion() ? "auto" : "smooth" });
    }

    function setReserve(selector) {
      reserved?.classList.remove("tour-reserve");
      reserved = selector ? document.querySelector(selector) : null;
      reserved?.classList.add("tour-reserve");
    }

    async function show({ el, count, title, text, next, alt = null, stepIndex, interactive = false, replies = null, reserve = null, place = null, big = false, bare = false }) {
      // Fade the old words out, swap them while invisible, then rise the new ones in
      card.classList.add("is-swapping");
      await wait(reducedMotion() ? 0 : 150);
      spotlight(el);
      open = interactive;
      react = replies;
      setReserve(reserve);
      dock = place;
      root.classList.toggle("is-open", interactive);
      root.classList.toggle("no-spot", bare); // the section shows as it is, without the dim
      card.classList.toggle("is-big", big);
      root.querySelector(".tour-count").textContent = count;
      root.querySelector(".tour-title").innerHTML = title;
      body.textContent = text;
      nextBtn.querySelector("span").textContent = next.label;
      nextBtn.disabled = false;
      primary = next.go;
      secondary = alt?.go || null;
      altBtn.textContent = alt?.label || "";
      altBtn.hidden = !alt;
      root.querySelectorAll(".tour-rail li").forEach((li, i) => {
        li.classList.toggle("is-done", stepIndex !== undefined && i < stepIndex);
        li.classList.toggle("is-current", i === stepIndex);
      });
      card.classList.remove("is-swapping");
      nextBtn.focus({ preventScroll: true });
    }

    // The moves: welcome → each feature's tile, where Show me opens it and Next goes to the next tile → done
    const intro = () => show({
      count: "Quick tour", title: `Welcome to <em>${subject}</em>.`, big: true,
      text: "Every subject has the same few sections. Here's a quick look at what each one does.",
      next: { label: "Let's go", go: () => tile(0) },
    });

    const after = (i) => (i + 1 < steps.length ? tile(i + 1) : outro());

    async function tile(i) {
      const s = steps[i];
      await openSection("");
      const count = `${i + 1} of ${steps.length}: ${s.label}`;
      const last = i === steps.length - 1;
      await show({
        el: await waitFor(s.tile, 4000), count, title: s.label, text: s.def.tile, stepIndex: i,
        ...(s.def.open
          ? { next: { label: "Show me", go: () => inside(i) }, alt: { label: last ? "Finish" : "Next", go: () => after(i) } }
          : { next: { label: last ? "Finish" : "Next", go: () => after(i) } }),
      });
    }

    async function inside(i) {
      const s = steps[i];
      nextBtn.disabled = true;
      nextBtn.querySelector("span").textContent = "Opening…";
      altBtn.hidden = true;
      if (s.def.bare) root.classList.add("no-spot"); // gone before the section opens, not faded out after
      await openSection(s.id);
      const el = await s.def.open();
      cleanup = s.def.leave || null;
      await show({
        el, count: `${i + 1} of ${steps.length}: ${s.label}`, title: `${s.label} <em>in use</em>`, text: s.def.inside, stepIndex: i,
        next: { label: i === steps.length - 1 ? "Finish" : "Next", go: () => after(i) },
        interactive: true, replies: s.def.react, reserve: s.def.reserve, place: s.def.dock, bare: s.def.bare,
      });
    }

    async function outro() {
      await openSection("");
      root.classList.add("is-last");
      await show({
        count: "Done", title: "You're <em>ready.</em>", stepIndex: steps.length, big: true,
        text: "Pick any section to start. Your progress saves as you go, and every subject works the same way.",
        next: { label: "Start studying", go: end },
      });
    }

    // Runs one move at a time: tidies the last screen, then shows the next
    async function go(move) {
      if (busy || !move) return;
      busy = true;
      open = false;
      react = null;
      dock = null;
      setReserve(null);
      root.classList.remove("is-reading");
      try {
        if (cleanup) await cleanup();
        cleanup = null;
        await move();
      } catch (error) {
        console.error("Tour step failed", error);
      } finally {
        busy = false;
      }
    }

    // Scrolling the spotlit section: the spotlight fades so the page reads clearly, and the card grows
    function onScrollIntent(event) {
      if (!open || !target?.contains(event.target) || root.classList.contains("is-reading")) return;
      root.classList.add("is-reading");
      card.classList.add("is-big");
    }

    async function end() {
      if (cleanup) await cleanup();
      cleanup = null;
      setReserve(null);
      document.documentElement.style.removeProperty("--tour-reserve");
      sessionStorage.removeItem("bb_tour");
      document.removeEventListener("keydown", onKey, true);
      document.removeEventListener("click", onUse, true);
      document.removeEventListener("wheel", onScrollIntent, true);
      document.removeEventListener("touchmove", onScrollIntent, true);
      document.body.classList.remove("tour-open");
      root.classList.add("is-exiting");
      setTimeout(() => { cancelAnimationFrame(frame); root.remove(); }, reducedMotion() ? 0 : 360);
    }

    function onKey(event) {
      if (event.key === "Escape") { event.preventDefault(); end(); }
      // Keep keyboard focus in the card or the spotlit element
      if (event.key === "Tab" && !card.contains(document.activeElement) && !(open && target?.contains(document.activeElement))) {
        event.preventDefault();
        nextBtn.focus();
      }
    }

    nextBtn.addEventListener("click", () => go(primary));
    altBtn.addEventListener("click", () => go(secondary));
    root.querySelector("[data-tour-skip]").addEventListener("click", end);
    document.addEventListener("keydown", onKey, true);
    document.addEventListener("click", onUse, true);
    document.addEventListener("wheel", onScrollIntent, { capture: true, passive: true });
    document.addEventListener("touchmove", onScrollIntent, { capture: true, passive: true });
    go(intro);
  }

  // Demo only: back to the sign-up screen with a fresh tab state
  function addRestart() {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "tour-restart";
    btn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>Restart demo`;
    btn.addEventListener("click", () => {
      sessionStorage.removeItem("bb_tour");
      sessionStorage.removeItem("bb_tour_user");
      location.href = "/app.html?preview=tour";
    });
    document.body.appendChild(btn);
  }

  async function start() {
    if (typeof isLocalTourPreview !== "undefined" && isLocalTourPreview) addRestart();
    if (!PAGE_SUBJECT || sessionStorage.getItem("bb_tour") !== PAGE_SUBJECT) return;
    // Real accounts restore their session asynchronously; the tour needs the signed-in page.
    if (!(await waitFor(() => getCurrentUser() && document.querySelector(".section-tile"), 15000))) return;
    run();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
