const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// mergeCrunchSettings (app.js) combines two copies of a student's Crunch settings, e.g. this device's
// and the account's: per subject, the most recently changed one wins.
const appSource = fs.readFileSync(path.join(__dirname, "..", "app.js"), "utf8");
const start = appSource.indexOf("function mergeCrunchSettings");
const end = appSource.indexOf("\n}\n", start) + 2;
const context = {};
vm.runInNewContext(`${appSource.slice(start, end)}\nthis.merge = mergeCrunchSettings;`, context);
const merge = context.merge;

test("the newer copy of a subject's settings wins", () => {
  const device = { biology: { on: true, grade: "H4", at: 200 } };
  const account = { biology: { on: false, grade: "H2", at: 100 } };
  assert.equal(merge(device, account).biology.grade, "H4");
  assert.equal(merge(account, device).biology.grade, "H4");
});

test("subjects set on only one side are kept", () => {
  const merged = merge({ biology: { on: true, at: 5 } }, { pe: { on: true, at: 1 } });
  assert.deepEqual(Object.keys(merged).sort(), ["biology", "pe"]);
});

test("settings saved before timestamps existed lose to any timestamped copy", () => {
  const merged = merge({ geography: { grade: "H1" } }, { geography: { grade: "H5", at: 1 } });
  assert.equal(merged.geography.grade, "H5");
});

test("a tie keeps the first copy given, and missing maps are ignored", () => {
  const merged = merge({ maths: { grade: "H3", at: 7 } }, undefined, { maths: { grade: "H6", at: 7 } });
  assert.equal(merged.maths.grade, "H3");
});
