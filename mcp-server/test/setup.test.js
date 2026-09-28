import { test } from "node:test";
import assert from "node:assert/strict";
import { patchPrefsText, mergeDesktopConfig } from "../../setup/install.mjs";

test("prefs: flips an existing value, inserts a missing key, keeps CRLF", () => {
  const on = patchPrefsText('["Main Pref Section v2"]\r\n\t"Pref_SCRIPTING_FILE_NETWORK_SECURITY" = 00\r\n\t"Other" = 1\r\n');
  assert.equal(on, '["Main Pref Section v2"]\r\n\t"Pref_SCRIPTING_FILE_NETWORK_SECURITY" = 01\r\n\t"Other" = 1\r\n');
  const added = patchPrefsText('["Misc"]\n\t"A" = 1\n["Main Pref Section v2"]\n\t"B" = 2\n');
  assert.equal(added, '["Misc"]\n\t"A" = 1\n["Main Pref Section v2"]\n\t"Pref_SCRIPTING_FILE_NETWORK_SECURITY" = 01\n\t"B" = 2\n');
  assert.equal(patchPrefsText(added), added, "idempotent");
});

test("Claude Desktop config: keeps other servers and settings", () => {
  const before = JSON.stringify({ theme: "dark", mcpServers: { other: { command: "x" } } });
  const after = JSON.parse(mergeDesktopConfig(before, "C:/p/index.js"));
  assert.equal(after.theme, "dark");
  assert.deepEqual(after.mcpServers.other, { command: "x" });
  assert.deepEqual(after.mcpServers["after-effects"], { command: "node", args: ["C:/p/index.js"] });
  assert.deepEqual(JSON.parse(mergeDesktopConfig("", "/a.js")).mcpServers["after-effects"].args, ["/a.js"]);
});
