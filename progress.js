// ─── Separate progress store ─────────────────────────────────────────────────
// Stored under a different localStorage key from the main app state so that
// progress data is cleanly separated from session / auth data.
// Key: username → { conceptPoints, testsCompleted, subjectProgress, chapterProgress }

const PROGRESS_STORAGE_KEY = "bare-bones-progress-v1";

function loadAllProgress() {
  try {
    return JSON.parse(localStorage.getItem(PROGRESS_STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveAllProgress(data) {
  localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(data));
}

// Return the stored progress snapshot for a username, or null if none.
function getUserProgressData(username) {
  if (!username) return null;
  const all = loadAllProgress();
  return all[username] || null;
}

// Write a computed progress snapshot for a username.
function saveUserProgressData(username, snapshot) {
  if (!username || !snapshot) return;
  const all = loadAllProgress();
  all[username] = { ...snapshot, lastUpdated: new Date().toISOString() };
  saveAllProgress(all);
}

// Remove stored progress for a username (e.g. on account deletion).
function deleteUserProgressData(username) {
  if (!username) return;
  const all = loadAllProgress();
  delete all[username];
  saveAllProgress(all);
}

// Return every username that has stored progress data.
function getAllProgressUsernames() {
  return Object.keys(loadAllProgress());
}
