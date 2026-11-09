/* Usage tracker.
   Counts active time (tab visible, some input in the last IDLE_MS) and files
   it under the subject + screen the student is on. Totals wait in
   localStorage, keyed by account, and are sent about once a minute through
   the record_usage() RPC (supabase/usage.sql). If a send fails or the tab
   closes first, the time is sent next visit. */
(function () {
  const TICK_MS = 5000;
  const FLUSH_MS = 60000;
  const IDLE_MS = 90000;
  // A long gap between ticks means the machine slept or the tab was frozen.
  const MAX_TICK_MS = TICK_MS * 3;
  const STORAGE_PREFIX = "bb-usage-pending-v1:";
  const SLUG = /^[a-z0-9-]{1,40}$/;

  function localDay(time) {
    const d = new Date(time);
    const pad = (n) => String(n).padStart(2, "0");
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  }

  function createUsageTracker(options) {
    const {
      getContext, // () => { userId, subject, screen } | null (null = don't count)
      send, // async (entries) => void
      storage = safeStorage(),
      now = () => Date.now(),
      isVisible = () => typeof document === "undefined" || document.visibilityState === "visible",
    } = options;

    let lastTick = now();
    let lastInput = now();
    let lastFlush = now();
    let flushing = null;

    function storageKey(userId) {
      return STORAGE_PREFIX + userId;
    }

    function readPending(userId) {
      try {
        const parsed = JSON.parse(storage.getItem(storageKey(userId)) || "{}");
        return parsed && typeof parsed === "object" && !Array.isArray(parsed) ? parsed : {};
      } catch (error) {
        return {};
      }
    }

    function writePending(userId, pending) {
      try {
        if (Object.keys(pending).length) storage.setItem(storageKey(userId), JSON.stringify(pending));
        else storage.removeItem(storageKey(userId));
      } catch (error) {
        // Storage full or blocked: the time is simply not kept.
      }
    }

    function markInput() {
      lastInput = now();
    }

    function tick() {
      const t = now();
      const elapsed = t - lastTick;
      lastTick = t;
      if (elapsed <= 0 || elapsed > MAX_TICK_MS) return;
      if (!isVisible() || t - lastInput > IDLE_MS) return;
      const context = getContext();
      if (!context?.userId || !SLUG.test(context.subject || "") || !SLUG.test(context.screen || "")) return;

      const pending = readPending(context.userId);
      const key = `${localDay(t)}|${context.subject}|${context.screen}`;
      pending[key] = (Number(pending[key]) || 0) + elapsed / 1000;
      writePending(context.userId, pending);

      if (t - lastFlush >= FLUSH_MS) flush();
    }

    async function flush() {
      if (flushing) return flushing;
      lastFlush = now();
      const userId = getContext()?.userId;
      if (!userId) return;
      const pending = readPending(userId);
      const entries = [];
      Object.entries(pending).forEach(([key, value]) => {
        const seconds = Math.floor(Number(value) || 0);
        if (seconds < 1) return;
        const [day, subject, screen] = key.split("|");
        entries.push({ day, subject, screen, seconds });
      });
      if (!entries.length) return;

      flushing = (async () => {
        try {
          await send(entries.slice(0, 200));
          // Subtract what was sent; time added while the request was in
          // flight stays pending.
          const latest = readPending(userId);
          entries.slice(0, 200).forEach(({ day, subject, screen, seconds }) => {
            const key = `${day}|${subject}|${screen}`;
            const left = (Number(latest[key]) || 0) - seconds;
            if (left >= 0.5) latest[key] = left;
            else delete latest[key];
          });
          writePending(userId, latest);
        } catch (error) {
          // Leave it pending; the next flush retries.
        } finally {
          flushing = null;
        }
      })();
      return flushing;
    }

    return { tick, flush, markInput, readPending };
  }

  function safeStorage() {
    try {
      return window.localStorage;
    } catch (error) {
      const memory = new Map();
      return {
        getItem: (k) => (memory.has(k) ? memory.get(k) : null),
        setItem: (k, v) => memory.set(k, String(v)),
        removeItem: (k) => memory.delete(k),
      };
    }
  }

  function startUsageTracker(options) {
    const tracker = createUsageTracker(options);
    ["pointerdown", "keydown", "wheel", "touchstart", "scroll"].forEach((type) => {
      window.addEventListener(type, tracker.markInput, { passive: true, capture: true });
    });
    document.addEventListener("visibilitychange", () => {
      if (document.visibilityState === "visible") tracker.markInput();
      else tracker.flush();
    });
    window.addEventListener("pagehide", () => tracker.flush());
    setInterval(tracker.tick, TICK_MS);
    return tracker;
  }

  const api = { createUsageTracker, startUsageTracker, localDay, TICK_MS, FLUSH_MS, IDLE_MS };
  if (typeof window !== "undefined") window.BarebonesUsage = api;
  if (typeof module !== "undefined") module.exports = api;
})();
