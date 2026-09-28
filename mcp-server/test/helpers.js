import fs from "node:fs/promises";
import path from "node:path";

// Stands in for ClaudeBridge.jsx: answers command files the way the panel does.
export function fakeAE(dir, handler) {
  let stop = false;
  const loop = (async () => {
    await fs.mkdir(path.join(dir, "commands"), { recursive: true });
    await fs.mkdir(path.join(dir, "results"), { recursive: true });
    while (!stop) {
      await fs.writeFile(path.join(dir, "heartbeat.json"), JSON.stringify({ time: Date.now(), bridge: "test" }));
      const files = (await fs.readdir(path.join(dir, "commands"))).filter((f) => f.endsWith(".json")).sort();
      for (const f of files) {
        const p = path.join(dir, "commands", f);
        const cmd = JSON.parse(await fs.readFile(p, "utf8"));
        await fs.rm(p);
        let out;
        try { out = { id: cmd.id, ok: true, result: await handler(cmd) }; }
        catch (e) { out = { id: cmd.id, ok: false, error: e.message }; }
        await fs.writeFile(path.join(dir, "results", f), JSON.stringify(out));
      }
      await new Promise((r) => setTimeout(r, 30));
    }
  })();
  return async () => { stop = true; await loop; };
}

