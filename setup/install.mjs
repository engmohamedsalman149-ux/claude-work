#!/usr/bin/env node
// One-step installer: copies the bridge panel into After Effects, turns on script file access,
// and registers the MCP server with Claude Desktop and Claude Code.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import readline from "node:readline/promises";
import { execFileSync, spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const serverEntry = path.join(repo, "mcp-server", "src", "index.js");
const panelSrc = path.join(repo, "after-effects", "ClaudeBridge.jsx");
const isWin = process.platform === "win32";
const isMac = process.platform === "darwin";

const ok = (m) => console.log(`  [OK] ${m}`);
const warn = (m) => console.log(`  [!]  ${m}`);
const step = (m) => console.log(`\n== ${m}`);

// ---------------------------------------------------------------- After Effects installs

export function findAfterEffects() {
  const found = [];
  const roots = isWin
    ? [process.env.ProgramFiles || "C:\\Program Files", process.env["ProgramW6432"]].filter(Boolean).map((p) => path.join(p, "Adobe"))
    : isMac ? ["/Applications"] : [];
  for (const root of new Set(roots)) {
    let names = [];
    try { names = fs.readdirSync(root); } catch { continue; }
    for (const n of names) {
      if (!/^Adobe After Effects/i.test(n)) continue;
      const base = path.join(root, n);
      const panels = isWin ? path.join(base, "Support Files", "Scripts", "ScriptUI Panels") : path.join(base, "Scripts", "ScriptUI Panels");
      if (fs.existsSync(path.dirname(panels))) found.push({ name: n, panels });
    }
  }
  return found;
}

function copyElevated(src, destDir) {
  const dest = path.join(destDir, path.basename(src));
  if (isWin) {
    const cmd = `New-Item -ItemType Directory -Force -Path '${destDir}' | Out-Null; Copy-Item -Force -LiteralPath '${src}' -Destination '${dest}'`;
    spawnSync("powershell.exe", ["-NoProfile", "-Command", `Start-Process powershell -Verb RunAs -Wait -ArgumentList '-NoProfile','-Command',"${cmd.replace(/"/g, '\\"')}"`], { stdio: "inherit" });
  } else if (isMac) {
    const sh = `mkdir -p '${destDir}' && cp -f '${src}' '${dest}'`;
    spawnSync("osascript", ["-e", `do shell script "${sh.replace(/"/g, '\\"')}" with administrator privileges`], { stdio: "inherit" });
  }
  return fs.existsSync(dest) && fs.readFileSync(dest, "utf8") === fs.readFileSync(src, "utf8");
}

function installPanel() {
  step("Installing the Claude Bridge panel into After Effects");
  const installs = findAfterEffects();
  if (!installs.length) {
    warn("After Effects was not found in the default location.");
    warn(`Copy this file into your AE 'Scripts/ScriptUI Panels' folder manually:\n       ${panelSrc}`);
    return false;
  }
  let any = false;
  for (const ae of installs) {
    try {
      fs.mkdirSync(ae.panels, { recursive: true });
      fs.copyFileSync(panelSrc, path.join(ae.panels, "ClaudeBridge.jsx"));
      ok(`${ae.name}`);
      any = true;
    } catch (e) {
      if (e.code !== "EPERM" && e.code !== "EACCES") throw e;
      console.log(`  Needs administrator permission for ${ae.name}, a permission prompt will appear...`);
      if (copyElevated(panelSrc, ae.panels)) { ok(`${ae.name}`); any = true; }
      else warn(`Could not copy into ${ae.panels}. Copy ClaudeBridge.jsx there manually.`);
    }
  }
  return any;
}

// ---------------------------------------------------------------- AE preference

const PREF_KEY = "Pref_SCRIPTING_FILE_NETWORK_SECURITY";

// Returns the patched prefs text (AE stores prefs as a text file with ["Section"] headers).
export function patchPrefsText(text) {
  const re = new RegExp(`("${PREF_KEY}"\\s*=\\s*)(\\S+)`);
  if (re.test(text)) return text.replace(re, "$101");
  const header = /\["Main Pref Section(?: v2)?"\]\r?\n/.exec(text);
  const eol = text.includes("\r\n") ? "\r\n" : "\n";
  const line = `\t"${PREF_KEY}" = 01${eol}`;
  if (header) return text.slice(0, header.index + header[0].length) + line + text.slice(header.index + header[0].length);
  return text + `${eol}["Main Pref Section v2"]${eol}${line}`;
}

export function findPrefsFiles() {
  const base = isWin
    ? path.join(process.env.APPDATA || path.join(os.homedir(), "AppData", "Roaming"), "Adobe", "After Effects")
    : path.join(os.homedir(), "Library", "Preferences", "Adobe", "After Effects");
  const out = [];
  let versions = [];
  try { versions = fs.readdirSync(base); } catch { return out; }
  for (const v of versions) {
    const dir = path.join(base, v);
    let files = [];
    try { files = fs.readdirSync(dir); } catch { continue; }
    for (const f of files) if (/^Adobe After Effects .* Prefs\.txt$/i.test(f)) out.push(path.join(dir, f));
  }
  return out;
}

function aeRunning() {
  try {
    if (isWin) return /AfterFX\.exe/i.test(execFileSync("tasklist", ["/FI", "IMAGENAME eq AfterFX.exe"], { encoding: "utf8" }));
    if (isMac) return spawnSync("pgrep", ["-f", "Adobe After Effects"]).status === 0;
  } catch {}
  return false;
}

async function enableScripting(rl) {
  step("Allowing scripts to write files (Settings > Scripting & Expressions)");
  const files = findPrefsFiles();
  if (!files.length) {
    warn("No After Effects preferences found yet (open AE once first), or enable it by hand:");
    warn("Edit > Preferences > Scripting & Expressions > Allow Scripts to Write Files and Access Network");
    return;
  }
  while (aeRunning()) {
    await rl.question("  After Effects is open. Close it (it overwrites preferences on exit), then press Enter... ");
  }
  for (const f of files) {
    const text = fs.readFileSync(f, "latin1");
    const next = patchPrefsText(text);
    if (next === text) { ok(`already on: ${f}`); continue; }
    fs.copyFileSync(f, f + ".before-claude.bak");
    fs.writeFileSync(f, next, "latin1");
    ok(f);
  }
}

// ---------------------------------------------------------------- Claude

export function mergeDesktopConfig(text, entry) {
  let cfg = {};
  if (text && text.trim()) cfg = JSON.parse(text);
  cfg.mcpServers = { ...(cfg.mcpServers || {}), "after-effects": { command: "node", args: [entry] } };
  return JSON.stringify(cfg, null, 2) + "\n";
}

function configureClaudeDesktop() {
  step("Registering with Claude Desktop");
  const dir = isWin
    ? path.join(process.env.APPDATA || path.join(os.homedir(), "AppData", "Roaming"), "Claude")
    : isMac ? path.join(os.homedir(), "Library", "Application Support", "Claude") : path.join(os.homedir(), ".config", "Claude");
  const file = path.join(dir, "claude_desktop_config.json");
  let text = "";
  if (fs.existsSync(file)) {
    text = fs.readFileSync(file, "utf8");
    fs.copyFileSync(file, file + ".before-claude.bak");
  } else if (!fs.existsSync(dir)) {
    warn("Claude Desktop is not installed (skipped). Get it from claude.ai/download if you want to use it.");
    return;
  }
  try {
    fs.writeFileSync(file, mergeDesktopConfig(text, serverEntry.replace(/\\/g, "/")), "utf8");
    ok(file);
    ok("Quit Claude Desktop completely (tray icon > Quit) and open it again.");
  } catch (e) {
    warn(`Could not update ${file}: ${e.message}`);
  }
}

function configureClaudeCode() {
  step("Registering with Claude Code");
  // Windows needs the shell to find claude.cmd; pass one quoted string so args aren't concatenated unescaped.
  const claude = (args, opts) =>
    isWin
      ? spawnSync(["claude", ...args].map((a) => (/[\s"]/.test(a) ? `"${a.replace(/"/g, '\\"')}"` : a)).join(" "), { shell: true, ...opts })
      : spawnSync("claude", args, opts);
  const has = claude(["--version"], { encoding: "utf8" });
  if (has.status !== 0) { warn("Claude Code CLI not found (skipped)."); return; }
  claude(["mcp", "remove", "--scope", "user", "after-effects"], { stdio: "ignore" });
  const r = claude(["mcp", "add", "--scope", "user", "after-effects", "--", "node", serverEntry.replace(/\\/g, "/")], { encoding: "utf8" });
  if (r.status === 0) ok("claude mcp add after-effects (user scope)");
  else warn(`claude mcp add failed: ${(r.stderr || r.stdout || "").trim()}`);
}

// ---------------------------------------------------------------- ffmpeg

// Newer npm versions skip install scripts unless approved, so ffmpeg-static may not have
// downloaded its binary. Run its installer directly when the binary is missing.
function ensureFfmpeg() {
  step("Checking ffmpeg (used for video analysis)");
  const pkg = path.join(repo, "mcp-server", "node_modules", "ffmpeg-static");
  const bin = path.join(pkg, isWin ? "ffmpeg.exe" : "ffmpeg");
  if (!fs.existsSync(bin) && fs.existsSync(path.join(pkg, "install.js"))) {
    console.log("  Downloading ffmpeg...");
    spawnSync(process.execPath, ["install.js"], { cwd: pkg, stdio: "inherit" });
  }
  if (fs.existsSync(bin)) ok(bin);
  else warn("ffmpeg could not be downloaded. Install ffmpeg and set FFMPEG_PATH, or video analysis will not work.");
}

// ---------------------------------------------------------------- main

async function main() {
  console.log("Claude <-> After Effects setup");
  console.log(`Project: ${repo}`);
  if (!fs.existsSync(path.join(repo, "mcp-server", "node_modules", "@modelcontextprotocol"))) {
    step("Installing server dependencies (npm install)");
    const r = isWin
      ? spawnSync("npm install --no-fund --no-audit", { cwd: path.join(repo, "mcp-server"), stdio: "inherit", shell: true })
      : spawnSync("npm", ["install", "--no-fund", "--no-audit"], { cwd: path.join(repo, "mcp-server"), stdio: "inherit" });
    if (r.status !== 0) throw new Error("npm install failed");
  }
  ensureFfmpeg();
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  try {
    installPanel();
    await enableScripting(rl);
    configureClaudeDesktop();
    configureClaudeCode();
  } finally {
    rl.close();
  }
  console.log(`
Done. Next:
  1. Open After Effects > Window > ClaudeBridge.jsx (it shows "Listening on ...").
  2. Open Claude and ask: "Is After Effects connected?"`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((e) => {
    console.error(`\nSetup failed: ${e.message}`);
    process.exitCode = 1;
  });
}
