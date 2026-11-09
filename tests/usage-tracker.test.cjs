const test = require("node:test");
const assert = require("node:assert/strict");
const { createUsageTracker, localDay, TICK_MS, FLUSH_MS, IDLE_MS } = require("../usage-tracker.js");

function memoryStorage() {
  const map = new Map();
  return {
    getItem: (k) => (map.has(k) ? map.get(k) : null),
    setItem: (k, v) => map.set(k, String(v)),
    removeItem: (k) => map.delete(k),
    map,
  };
}

function harness({ context, visible = true, sendImpl } = {}) {
  let clock = new Date(2026, 10, 9, 10, 0, 0).getTime();
  const sent = [];
  const state = {
    context: context || { userId: "u1", subject: "biology", screen: "learn" },
    visible,
  };
  const storage = memoryStorage();
  const tracker = createUsageTracker({
    getContext: () => state.context,
    send: sendImpl || (async (entries) => { sent.push(entries); }),
    storage,
    now: () => clock,
    isVisible: () => state.visible,
  });
  return {
    tracker,
    state,
    sent,
    storage,
    advance(ms) { clock += ms; },
    step(n = 1) {
      for (let i = 0; i < n; i++) {
        clock += TICK_MS;
        tracker.tick();
      }
    },
    pendingSeconds(userId = "u1") {
      return Object.values(tracker.readPending(userId)).reduce((a, b) => a + b, 0);
    },
  };
}

test("counts active time under the current subject and screen", () => {
  const h = harness();
  h.step(4);
  const day = localDay(new Date(2026, 10, 9).getTime());
  assert.deepEqual(h.tracker.readPending("u1"), { [`${day}|biology|learn`]: 20 });
  h.state.context = { userId: "u1", subject: "maths", screen: "exam" };
  h.step(2);
  assert.equal(h.tracker.readPending("u1")[`${day}|maths|exam`], 10);
});

test("does not count hidden tabs, idle students, signed-out state or sleep gaps", () => {
  const h = harness();
  h.state.visible = false;
  h.step(3);
  assert.equal(h.pendingSeconds(), 0);

  h.state.visible = true;
  h.tracker.markInput();
  h.step(Math.ceil(IDLE_MS / TICK_MS) + 3); // goes idle partway through
  const counted = h.pendingSeconds();
  assert.ok(counted >= IDLE_MS / 1000 - TICK_MS / 1000 && counted <= IDLE_MS / 1000 + TICK_MS / 1000, String(counted));

  h.tracker.markInput();
  h.advance(10 * 60 * 1000); // laptop slept
  h.tracker.markInput();
  h.tracker.tick();
  assert.equal(h.pendingSeconds(), counted);

  h.state.context = null;
  h.step(2);
  assert.equal(h.pendingSeconds(), counted);
});

test("flushes about once a minute and clears what was sent", async () => {
  const h = harness();
  h.step(FLUSH_MS / TICK_MS);
  await new Promise((r) => setImmediate(r));
  assert.equal(h.sent.length, 1);
  assert.equal(h.sent[0][0].seconds, 60);
  assert.equal(h.sent[0][0].subject, "biology");
  assert.equal(h.pendingSeconds(), 0);
});

test("keeps time pending when a send fails, and retries", async () => {
  let fail = true;
  const sent = [];
  const h = harness({
    sendImpl: async (entries) => {
      if (fail) throw new Error("offline");
      sent.push(entries);
    },
  });
  h.step(6);
  await h.tracker.flush();
  assert.equal(h.pendingSeconds(), 30);
  fail = false;
  await h.tracker.flush();
  assert.equal(sent.length, 1);
  assert.equal(sent[0][0].seconds, 30);
  assert.equal(h.pendingSeconds(), 0);
});

test("pending time is kept per account", () => {
  const h = harness();
  h.step(2);
  h.state.context = { userId: "u2", subject: "history", screen: "notes" };
  h.step(3);
  assert.equal(h.pendingSeconds("u1"), 10);
  assert.equal(h.pendingSeconds("u2"), 15);
});

test("ignores contexts with unsafe subject or screen ids", () => {
  const h = harness({ context: { userId: "u1", subject: "Bio logy", screen: "learn" } });
  h.step(3);
  assert.equal(h.pendingSeconds(), 0);
});
