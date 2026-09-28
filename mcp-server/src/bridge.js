// File-based transport to the ClaudeBridge.jsx panel running inside After Effects.
// Commands go to <root>/commands/<id>.json, results come back in <root>/results/<id>.json.
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";

// Must match Folder.userData + "/ae-claude-bridge" on the ExtendScript side.
export function defaultBridgeDir() {
  if (process.env.AE_BRIDGE_DIR) return process.env.AE_BRIDGE_DIR;
  const home = os.homedir();
  if (process.platform === "win32") {
    return path.join(process.env.APPDATA || path.join(home, "AppData", "Roaming"), "ae-claude-bridge");
  }
  if (process.platform === "darwin") {
    return path.join(home, "Library", "Application Support", "ae-claude-bridge");
  }
  return path.join(home, ".config", "ae-claude-bridge");
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export class Bridge {
  constructor({ dir = defaultBridgeDir(), pollMs = 100 } = {}) {
    this.dir = dir;
    this.cmdDir = path.join(dir, "commands");
    this.resDir = path.join(dir, "results");
    this.pollMs = pollMs;
    this.seq = 0;
  }

  async ensureDirs() {
    await fs.mkdir(this.cmdDir, { recursive: true });
    await fs.mkdir(this.resDir, { recursive: true });
  }

  async heartbeat() {
    try {
      const raw = await fs.readFile(path.join(this.dir, "heartbeat.json"), "utf8");
      const hb = JSON.parse(raw);
      return { ...hb, ageMs: Date.now() - hb.time };
    } catch {
      return null;
    }
  }

  // Sortable id so AE processes commands in the order they were sent.
  nextId() {
    this.seq = (this.seq + 1) % 1e6;
    return `${Date.now()}-${String(this.seq).padStart(6, "0")}-${crypto.randomBytes(3).toString("hex")}`;
  }

  async send(command, args = {}, { timeoutMs = 60_000 } = {}) {
    await this.ensureDirs();
    const id = this.nextId();
    const cmdFile = path.join(this.cmdDir, `${id}.json`);
    const resFile = path.join(this.resDir, `${id}.json`);
    // Write then rename so AE never reads a half-written file.
    await fs.writeFile(`${cmdFile}.tmp`, JSON.stringify({ id, command, args }), "utf8");
    await fs.rename(`${cmdFile}.tmp`, cmdFile);

    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
      try {
        const raw = await fs.readFile(resFile, "utf8");
        await fs.rm(resFile, { force: true });
        const res = JSON.parse(raw);
        if (!res.ok) {
          const err = new Error(res.error + (res.line ? ` (line ${res.line})` : ""));
          err.aeError = true;
          throw err;
        }
        return res.result;
      } catch (e) {
        if (e.code !== "ENOENT") throw e;
      }
      await sleep(this.pollMs);
    }

    // Pull the command back if AE never picked it up, so it doesn't run later by surprise.
    let pickedUp = true;
    try {
      await fs.rm(cmdFile);
      pickedUp = false;
    } catch {}
    const hb = await this.heartbeat();
    const hint = !hb || hb.ageMs > 10_000
      ? "After Effects is not responding. Open Window > ClaudeBridge.jsx in After Effects and press Start."
      : pickedUp
        ? "After Effects accepted the command but it is still running (increase timeoutSec for long jobs such as renders)."
        : "After Effects is busy (a modal dialog may be open).";
    throw new Error(`Timed out after ${timeoutMs / 1000}s waiting for '${command}'. ${hint}`);
  }
}
