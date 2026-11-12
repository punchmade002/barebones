(function () {
  "use strict";

  const config = window.BAREBONES_AUTH_CONFIG || {};
  const url = String(config.supabaseUrl || "").trim();
  const key = String(config.supabasePublishableKey || config.supabaseAnonKey || "").trim();
  const configured =
    Boolean(window.supabase?.createClient) &&
    /^https:\/\/[a-z0-9-]+\.supabase\.co$/i.test(url) &&
    key.length > 20 &&
    !url.includes("YOUR_PROJECT") &&
    !key.includes("YOUR_PUBLISHABLE_KEY");

  let client = null;
  let session = null;
  const listeners = new Set();

  function notify(event, nextSession) {
    session = nextSession || null;
    if (session) {
      localStorage.setItem("bb_has_auth_session", "1");
    } else {
      localStorage.removeItem("bb_has_auth_session");
    }
    window.setTimeout(() => {
      listeners.forEach((listener) => listener(event, session));
    }, 0);
  }

  const readyPromise = (async () => {
    if (!configured) return null;

    client = window.supabase.createClient(url, key, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
      },
    });

    client.auth.onAuthStateChange((event, nextSession) => {
      notify(event, nextSession);
    });

    const { data, error } = await client.auth.getSession();
    if (error) throw error;
    session = data.session || null;
    if (session) localStorage.setItem("bb_has_auth_session", "1");
    return session;
  })();

  function requireClient() {
    if (!client) {
      throw new Error("Account services are not configured yet.");
    }
    return client;
  }

  function normalizeUsername(value) {
    return String(value || "").trim().toLowerCase();
  }

  function redirectUrl() {
    const path = window.location.pathname.replace(/\/[^/]*$/, "/app.html");
    return `${window.location.origin}${path}`;
  }

  async function isUsernameAvailable(username) {
    const authClient = requireClient();
    const normalized = normalizeUsername(username);
    const { data, error } = await authClient.rpc("username_available", {
      candidate: normalized,
    });
    if (error) throw error;
    return Boolean(data);
  }

  // Bump when terms.html or privacy.html change in a way users must agree to again.
  const TERMS_VERSION = "2026-11-06";

  async function signUp({ username, email, password, origin = "self_service", marketingOptIn = false }) {
    const authClient = requireClient();
    const normalized = normalizeUsername(username);

    if (!(await isUsernameAvailable(normalized))) {
      const error = new Error("That username is already taken.");
      error.code = "username_taken";
      throw error;
    }

    const { data, error } = await authClient.auth.signUp({
      email: String(email || "").trim().toLowerCase(),
      password,
      options: {
        emailRedirectTo: redirectUrl(),
        data: {
          username: normalized,
          account_origin: origin,
          // Proof of what the person agreed to, stored on their Supabase auth user.
          terms_version: TERMS_VERSION,
          terms_accepted_at: new Date().toISOString(),
          marketing_opt_in: Boolean(marketingOptIn),
        },
      },
    });
    if (error) throw error;
    return data;
  }

  async function signIn(email, password) {
    const authClient = requireClient();
    const { data, error } = await authClient.auth.signInWithPassword({
      email: String(email || "").trim().toLowerCase(),
      password,
    });
    if (error) throw error;
    return data;
  }

  async function signOut() {
    const authClient = requireClient();
    const { error } = await authClient.auth.signOut();
    if (error) throw error;
    localStorage.removeItem("bb_has_auth_session");
  }

  async function sendPasswordReset(email) {
    const authClient = requireClient();
    const { error } = await authClient.auth.resetPasswordForEmail(
      String(email || "").trim().toLowerCase(),
      { redirectTo: redirectUrl() }
    );
    if (error) throw error;
  }

  async function updatePassword(password) {
    const authClient = requireClient();
    const { data, error } = await authClient.auth.updateUser({ password });
    if (error) throw error;
    return data;
  }

  async function getAccountSnapshot() {
    const authClient = requireClient();
    const currentSession = session || (await authClient.auth.getSession()).data.session;
    if (!currentSession?.user) return null;

    const userId = currentSession.user.id;
    const [profileResult, studyResult, entitlementResult] = await Promise.all([
      authClient
        .from("profiles")
        .select("id, username, account_origin, created_at")
        .eq("id", userId)
        .maybeSingle(),
      authClient
        .from("study_states")
        .select("data, updated_at")
        .eq("user_id", userId)
        .maybeSingle(),
      authClient
        .from("entitlements")
        .select("product_key, status, current_period_end")
        .eq("user_id", userId),
    ]);

    if (profileResult.error) throw profileResult.error;
    if (studyResult.error) throw studyResult.error;
    if (entitlementResult.error) throw entitlementResult.error;

    return {
      user: currentSession.user,
      profile: profileResult.data || {
        id: userId,
        username: normalizeUsername(currentSession.user.user_metadata?.username),
        account_origin: currentSession.user.user_metadata?.account_origin || "self_service",
      },
      studyData: studyResult.data?.data || null,
      studyUpdatedAt: studyResult.data?.updated_at || null,
      entitlements: entitlementResult.data || [],
    };
  }

  async function saveStudyData(data) {
    const authClient = requireClient();
    const currentSession = session || (await authClient.auth.getSession()).data.session;
    if (!currentSession?.user) return false;

    const { error } = await authClient.from("study_states").upsert(
      {
        user_id: currentSession.user.id,
        data,
        updated_at: new Date().toISOString(),
      },
      { onConflict: "user_id" }
    );
    if (error) throw error;
    return true;
  }

  // Exam paper markup: one row per paper file (see supabase/paper-ink.sql)
  async function loadPaperInk(file) {
    const authClient = requireClient();
    const { data, error } = await authClient
      .from("paper_ink")
      .select("data, updated_at")
      .eq("file", file)
      .maybeSingle();
    if (error) throw error;
    return data ? { data: data.data || {}, updatedAt: data.updated_at } : null;
  }

  async function savePaperInk(file, data) {
    const authClient = requireClient();
    const currentSession = session || (await authClient.auth.getSession()).data.session;
    if (!currentSession?.user) return null;
    const updatedAt = new Date().toISOString();
    const { error } = await authClient.from("paper_ink").upsert(
      { user_id: currentSession.user.id, file, data, updated_at: updatedAt },
      { onConflict: "user_id,file" }
    );
    if (error) throw error;
    return updatedAt;
  }

  async function currentUserId() {
    const authClient = requireClient();
    const currentSession = session || (await authClient.auth.getSession()).data.session;
    return currentSession?.user?.id || "";
  }

  async function submitFeedback(message) {
    const authClient = requireClient();
    const { data, error } = await authClient.rpc("submit_feedback", {
      feedback_message: String(message || ""),
    });
    if (error) throw error;
    return data;
  }

  // Replies the admin wrote that this student has not yet been shown.
  async function getUnseenFeedbackReplies() {
    const authClient = requireClient();
    const userId = await currentUserId();
    if (!userId) return [];
    const { data, error } = await authClient
      .from("feedback")
      .select("id, message, reply, created_at, addressed_at")
      .eq("user_id", userId)
      .eq("status", "addressed")
      .not("reply", "is", null)
      .is("reply_seen_at", null)
      .order("addressed_at", { ascending: true });
    if (error) throw error;
    return data || [];
  }

  async function markFeedbackRepliesSeen(ids) {
    if (!ids?.length) return;
    const authClient = requireClient();
    const { error } = await authClient.rpc("mark_feedback_replies_seen", {
      feedback_ids: ids,
    });
    if (error) throw error;
  }

  async function isAdmin() {
    const authClient = requireClient();
    const { data, error } = await authClient.rpc("is_admin");
    // Before feedback.sql is applied the function does not exist: not an admin.
    if (error) return false;
    return Boolean(data);
  }

  async function listFeedback() {
    const authClient = requireClient();
    const { data, error } = await authClient
      .from("feedback")
      .select("id, username, message, status, reply, created_at, addressed_at, reply_seen_at")
      .order("created_at", { ascending: false })
      .limit(200);
    if (error) throw error;
    return data || [];
  }

  async function addressFeedback(id, reply) {
    const authClient = requireClient();
    const { error } = await authClient.rpc("address_feedback", {
      feedback_id: id,
      reply_text: String(reply || ""),
    });
    if (error) throw error;
  }

  async function reopenFeedback(id) {
    const authClient = requireClient();
    const { error } = await authClient.rpc("reopen_feedback", { feedback_id: id });
    if (error) throw error;
  }

  async function recordUsage(entries) {
    if (!entries?.length) return;
    const authClient = requireClient();
    const { error } = await authClient.rpc("record_usage", { entries });
    if (error) throw error;
  }

  // sinceDay: "YYYY-MM-DD" or null for all time. Admin only.
  async function adminUsageStats(sinceDay) {
    const authClient = requireClient();
    const { data, error } = await authClient.rpc("admin_usage_stats", {
      since_day: sinceDay || null,
    });
    if (error) throw error;
    return data || [];
  }

  window.BarebonesAuth = {
    recordUsage,
    adminUsageStats,
    submitFeedback,
    getUnseenFeedbackReplies,
    markFeedbackRepliesSeen,
    isAdmin,
    listFeedback,
    addressFeedback,
    reopenFeedback,
    configured,
    ready: () => readyPromise,
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    getSession: () => session,
    normalizeUsername,
    isUsernameAvailable,
    signUp,
    signIn,
    signOut,
    sendPasswordReset,
    updatePassword,
    getAccountSnapshot,
    saveStudyData,
    loadPaperInk,
    savePaperInk,
  };
})();
