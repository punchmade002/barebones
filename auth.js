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

  async function signUp({ username, email, password, origin = "self_service" }) {
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

  window.BarebonesAuth = {
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
  };
})();
