import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Bridge } from "../src/bridge.js";
import { fakeAE } from "./helpers.js";

const tmp = () => fs.mkdtemp(path.join(os.tmpdir(), "ae-bridge-test-"));

test("bridge round-trips commands in order and surfaces AE errors", async () => {
  const dir = await tmp();
  const seen = [];
  const stop = fakeAE(dir, (cmd) => {
    seen.push(cmd.command);
    if (cmd.command === "boom") throw new Error("No composition named 'x'");
    return { echo: cmd.args };
  });
  const b = new Bridge({ dir, pollMs: 20 });
  assert.deepEqual(await b.send("a", { n: 1, t: "مرحبا" }), { echo: { n: 1, t: "مرحبا" } });
  await assert.rejects(b.send("boom"), /No composition named 'x'/);
  assert.deepEqual(seen, ["a", "boom"]);
  await stop();
});

test("bridge times out and withdraws the command when AE is not running", async () => {
  const dir = await tmp();
  const b = new Bridge({ dir, pollMs: 20 });
  await assert.rejects(b.send("ping", {}, { timeoutMs: 200 }), /not responding/);
  assert.deepEqual(await fs.readdir(path.join(dir, "commands")), []);
});

test("MCP server exposes tools and forwards calls to AE", async () => {
  const dir = await tmp();
  const stop = fakeAE(dir, (cmd) => ({ command: cmd.command, args: cmd.args }));
  const client = new Client({ name: "test", version: "0" });
  await client.connect(new StdioClientTransport({
    command: process.execPath,
    args: [path.join(import.meta.dirname, "..", "src", "index.js")],
    env: { ...process.env, AE_BRIDGE_DIR: dir },
  }));
  const { tools } = await client.listTools();
  const names = tools.map((t) => t.name);
  for (const n of ["ae_status", "ae_run_script", "ae_add_layer", "ae_set_keyframes", "ae_add_effect", "ae_render", "ae_preview_frame"]) {
    assert.ok(names.includes(n), `missing ${n}`);
  }

  const status = JSON.parse((await client.callTool({ name: "ae_status", arguments: {} })).content[0].text);
  assert.equal(status.connected, true);

  const r = await client.callTool({
    name: "ae_add_layer",
    arguments: { type: "text", text: "أهلا", fontSize: 90, position: [960, 540] },
  });
  assert.deepEqual(JSON.parse(r.content[0].text), {
    command: "addLayer",
    args: { type: "text", text: "أهلا", fontSize: 90, position: [960, 540] },
  });

  const k = await client.callTool({
    name: "ae_set_keyframes",
    arguments: { layer: 1, path: "Transform/Opacity", keyframes: [{ time: 0, value: 0 }, { time: 1, value: 100 }], ease: "easyEase", timeoutSec: 5 },
  });
  assert.equal(JSON.parse(k.content[0].text).command, "setKeyframes");
  assert.equal(JSON.parse(k.content[0].text).args.timeoutSec, undefined);

  await client.close();
  await stop();
});
