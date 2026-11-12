const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

function loadAuthHarness({ hash = "", rpcErrors = {} } = {}) {
  const calls = [];
  let usernameAvailable = true;
  const session = {
    user: {
      id: "11111111-1111-1111-1111-111111111111",
      email: "student@example.com",
      user_metadata: { username: "student" },
    },
  };

  const client = {
    auth: {
      onAuthStateChange(callback) {
        calls.push(["onAuthStateChange", callback]);
        return { data: { subscription: { unsubscribe() {} } } };
      },
      async getSession() {
        return { data: { session }, error: null };
      },
      async signUp(payload) {
        calls.push(["signUp", payload]);
        return { data: { session }, error: null };
      },
      async signInWithPassword(payload) {
        calls.push(["signInWithPassword", payload]);
        return { data: { session }, error: null };
      },
      async signOut() {
        calls.push(["signOut"]);
        return { error: null };
      },
      async resetPasswordForEmail(email, options) {
        calls.push(["resetPasswordForEmail", email, options]);
        return { error: null };
      },
      async resend(payload) {
        calls.push(["resend", payload]);
        return { error: null };
      },
      async updateUser(payload) {
        calls.push(["updateUser", payload]);
        return { data: { user: session.user }, error: null };
      },
    },
    async rpc(name, payload) {
      calls.push(["rpc", name, payload]);
      if (rpcErrors[name]) return { data: null, error: { message: rpcErrors[name] } };
      return { data: usernameAvailable, error: null };
    },
    from(table) {
      return {
        upsert: async (payload, options) => {
          calls.push(["upsert", table, payload, options]);
          return { error: null };
        },
      };
    },
  };

  const storage = new Map();
  const window = {
    BAREBONES_AUTH_CONFIG: {
      supabaseUrl: "https://project-ref.supabase.co",
      supabasePublishableKey: "sb_publishable_test_key_that_is_long_enough",
    },
    supabase: {
      createClient(url, key, options) {
        calls.push(["createClient", url, key, options]);
        return client;
      },
    },
    location: {
      origin: "https://barebones.example",
      pathname: "/study/app.html",
      hash,
      search: "",
    },
    setTimeout(callback) {
      callback();
      return 1;
    },
  };
  const localStorage = {
    getItem(key) {
      return storage.get(key) || null;
    },
    setItem(key, value) {
      storage.set(key, String(value));
    },
    removeItem(key) {
      storage.delete(key);
    },
  };
  const context = vm.createContext({ window, localStorage, console, URLSearchParams });
  const source = fs.readFileSync(path.join(__dirname, "..", "auth.js"), "utf8");
  vm.runInContext(source, context);
  return {
    auth: window.BarebonesAuth,
    calls,
    session,
    storage,
    setUsernameAvailable(value) {
      usernameAvailable = value;
    },
  };
}

test("sign-up normalizes identity and uses the app callback URL", async () => {
  const { auth, calls } = loadAuthHarness();
  await auth.ready();
  await auth.signUp({
    username: "  Student_1 ",
    email: "  Student@Example.com ",
    password: "long-password",
  });

  const signUpCall = calls.find(([name]) => name === "signUp");
  assert.equal(signUpCall[1].email, "student@example.com");
  assert.equal(signUpCall[1].options.data.username, "student_1");
  assert.equal(
    signUpCall[1].options.emailRedirectTo,
    "https://barebones.example/study/app.html"
  );
});

test("password recovery uses a non-enumerating email flow", async () => {
  const { auth, calls } = loadAuthHarness();
  await auth.ready();
  await auth.sendPasswordReset(" Student@Example.com ");

  const resetCall = calls.find(([name]) => name === "resetPasswordForEmail");
  assert.equal(resetCall[1], "student@example.com");
  assert.equal(resetCall[2].redirectTo, "https://barebones.example/study/app.html");
});

test("sign-up identifies an existing username as a returning-account state", async () => {
  const { auth, setUsernameAvailable } = loadAuthHarness();
  await auth.ready();
  setUsernameAvailable(false);

  await assert.rejects(
    auth.signUp({
      username: "gabriel",
      email: "gabriel@example.com",
      password: "long-password",
    }),
    (error) => error.code === "username_taken"
  );
});

test("study state is written against the authenticated immutable user id", async () => {
  const { auth, calls, session } = loadAuthHarness();
  await auth.ready();
  await auth.saveStudyData({ testsCompleted: 3 });

  const upsertCall = calls.find(([name]) => name === "upsert");
  assert.equal(upsertCall[1], "study_states");
  assert.equal(upsertCall[2].user_id, session.user.id);
  assert.deepEqual(upsertCall[2].data, { testsCompleted: 3 });
});

test("account creation stores normalized emails in the protected mailing list", () => {
  const schema = fs.readFileSync(
    path.join(__dirname, "..", "supabase", "schema.sql"),
    "utf8"
  );

  assert.match(schema, /create table if not exists public\.mailing_list/i);
  assert.match(schema, /alter table public\.mailing_list enable row level security/i);
  assert.match(schema, /revoke all on public\.mailing_list from anon, authenticated/i);
  assert.match(
    schema,
    /insert into public\.mailing_list[\s\S]*lower\(trim\(new\.email\)\)/i
  );
  assert.match(
    schema,
    /from auth\.users[\s\S]*on conflict \(user_id\) do update/i
  );
});

test("sign-up lets the same email reclaim its unconfirmed username", async () => {
  const { auth, calls } = loadAuthHarness();
  await auth.ready();
  await auth.signUp({ username: "Student", email: " Student@Example.com ", password: "long-password" });

  const rpcCall = calls.find(([name, fn]) => name === "rpc" && fn === "username_claimable");
  assert.equal(rpcCall[2].candidate, "student");
  assert.equal(rpcCall[2].candidate_email, "student@example.com");
});

test("sign-up falls back to the plain username check before the SQL fix is applied", async () => {
  const { auth, calls } = loadAuthHarness({
    rpcErrors: { username_claimable: "Could not find the function public.username_claimable" },
  });
  await auth.ready();
  await auth.signUp({ username: "student", email: "student@example.com", password: "long-password" });

  assert.ok(calls.some(([name, fn]) => name === "rpc" && fn === "username_available"));
  assert.ok(calls.some(([name]) => name === "signUp"));
});

test("confirmation emails can be resent to the app callback URL", async () => {
  const { auth, calls } = loadAuthHarness();
  await auth.ready();
  await auth.resendConfirmation(" Student@Example.com ");

  const resendCall = calls.find(([name]) => name === "resend");
  assert.equal(resendCall[1].type, "signup");
  assert.equal(resendCall[1].email, "student@example.com");
  assert.equal(resendCall[1].options.emailRedirectTo, "https://barebones.example/study/app.html");
});

test("a failed email link is reported instead of swallowed", () => {
  const { auth } = loadAuthHarness({
    hash: "#error=access_denied&error_code=otp_expired&error_description=Email+link+is+invalid+or+has+expired",
  });
  assert.equal(auth.urlAuthError.code, "otp_expired");
  assert.equal(auth.urlAuthError.message, "Email link is invalid or has expired");

  assert.equal(loadAuthHarness({ hash: "#signup" }).auth.urlAuthError, null);
});

test("abandoned unconfirmed sign-ups release their username", () => {
  const sql = fs.readFileSync(path.join(__dirname, "..", "supabase", "signup-fixes.sql"), "utf8");
  assert.match(sql, /function public\.username_claimable\(candidate text, candidate_email text\)/i);
  assert.match(sql, /grant execute on function public\.username_claimable\(text, text\) to anon, authenticated/i);
  assert.match(sql, /delete from auth\.users[\s\S]*email_confirmed_at is null[\s\S]*interval '24 hours'/i);
});
