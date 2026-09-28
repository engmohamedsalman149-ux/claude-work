// End to end: synthetic video -> analysis -> named preset -> preset_apply through the MCP server.
import { test, before } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { analyzeVideo, binaries } from "../src/video.js";
import { fakeAE } from "./helpers.js";

let video;
let skip = false;

// 6 shots joined by: hard cut @3, dissolve 5.5-6, dip to black 8.2-9, white flash 10.6-10.9, zoom 13.2-13.6.
before(async () => {
  const { ffmpeg } = await binaries();
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "ae-video-"));
  video = path.join(dir, "reference.mp4");
  const src = (f) => ["-f", "lavfi", "-i", f];
  const r = spawnSync(ffmpeg, [
    "-hide_banner", "-loglevel", "error", "-y",
    ...src("testsrc2=s=320x180:r=30:d=3"),
    ...src("smptebars=s=320x180:r=30:d=3"),
    ...src("mandelbrot=s=320x180:r=30,trim=duration=3"),
    ...src("life=s=320x180:r=30:mold=10:ratio=0.1:death_color=#202060:life_color=#f0c040,trim=duration=3"),
    ...src("testsrc=s=320x180:r=30:d=3"),
    ...src("cellauto=s=320x180:r=30:rule=110,trim=duration=3"),
    ...src("sine=f=220:beep_factor=6:d=16.2"),
    "-filter_complex",
    "[0][1]concat=n=2:v=1:a=0,settb=AVTB,fps=30[ab];[ab][2]xfade=transition=dissolve:duration=0.5:offset=5.5,fps=30[abc];" +
      "[abc][3]xfade=transition=fadeblack:duration=0.8:offset=8.2,fps=30[abcd];[abcd][4]xfade=transition=fadewhite:duration=0.3:offset=10.6,fps=30[abcde];" +
      "[abcde][5]xfade=transition=zoomin:duration=0.4:offset=13.2,fps=30,format=yuv420p[v]",
    "-map", "[v]", "-map", "6:a", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20", "-c:a", "aac", video,
  ]);
  if (r.error || r.status !== 0) skip = `ffmpeg unavailable: ${r.error?.message || r.stderr}`;
});

test("detects each kind of edit at the right time", async (t) => {
  if (skip) return t.skip(skip);
  const a = await analyzeVideo(video);
  const got = a.events.map((e) => [e.type, e.time]);
  const expect = [["cut", 3], ["dissolve", 5.75], ["dip_to_black", 8.4], ["flash_transition", 10.65], ["motion_transition", 13.4]];
  assert.equal(got.length, expect.length, JSON.stringify(got));
  expect.forEach(([type, time], i) => {
    assert.equal(got[i][0], type);
    assert.ok(Math.abs(got[i][1] - time) < 0.1, `${type} at ${got[i][1]}`);
  });
  assert.equal(a.shots.length, 6);
  assert.ok(Math.abs(a.events[1].duration - 0.5) < 0.07, "dissolve length");
  assert.equal(a.events[3].suggestedRecipe.steps[0].kind, "flash");
});

test("MCP: analyse, save presets by name, apply them to another video", async (t) => {
  if (skip) return t.skip(skip);
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "ae-edit-"));
  const bridgeDir = path.join(dir, "bridge");
  const calls = [];
  const stop = fakeAE(bridgeDir, (cmd) => {
    calls.push(cmd);
    if (cmd.command === "setupVideos") {
      return { comp: { id: 42, name: "edit" }, clips: cmd.args.paths.map((p, i) => ({ index: i + 1, start: i * 16.2, end: (i + 1) * 16.2, file: p })), junctions: cmd.args.paths.slice(1).map((_, i) => (i + 1) * 16.2) };
    }
    if (cmd.command === "applyRecipe") return { applied: cmd.args.times.length, warnings: [] };
    throw new Error("unexpected " + cmd.command);
  });
  const client = new Client({ name: "test", version: "0" });
  await client.connect(new StdioClientTransport({
    command: process.execPath,
    args: [path.join(import.meta.dirname, "..", "src", "index.js")],
    env: { ...process.env, AE_BRIDGE_DIR: bridgeDir, AE_LIBRARY_DIR: path.join(dir, "lib") },
  }));
  const call = async (name, args) => {
    const r = await client.callTool({ name, arguments: args });
    if (r.isError) throw new Error(r.content[0].text);
    return r;
  };

  const analysed = await call("video_analyze", { video, maxStrips: 4 });
  const images = analysed.content.filter((c) => c.type === "image");
  assert.equal(images.length, 4);
  assert.equal(Buffer.from(images[0].data, "base64").subarray(0, 2).toString("hex"), "ffd8", "JPEG strip");
  const summary = JSON.parse(analysed.content[0].text);
  const flash = summary.events.find((e) => e.type === "flash_transition");

  await call("preset_from_event", { video, eventId: flash.id, name: "فلاش أبيض" });
  await call("preset_from_event", { video, eventId: "look", name: "Reference look" });
  await call("preset_from_event", { video, eventId: "rhythm", name: "Fast rhythm", transition: "فلاش أبيض" });
  await call("preset_save", { name: "Whip left", category: "transition", steps: [{ kind: "whip", direction: "left", start: -0.15, duration: 0.3 }] });
  await assert.rejects(call("preset_save", { name: "whip LEFT", category: "transition", steps: [] }), /already exists/);

  const list = JSON.parse((await call("preset_list", {})).content[0].text);
  assert.deepEqual(list.presets.map((p) => p.name).sort(), ["Fast rhythm", "Reference look", "Whip left", "فلاش أبيض"].sort());

  // Transition on every detected cut of the same video.
  calls.length = 0;
  await call("preset_apply", { preset: "فلاش أبيض", video });
  const apply = calls.find((c) => c.command === "applyRecipe").args;
  assert.equal(apply.comp, 42);
  assert.equal(apply.times.length, 5);
  assert.equal(apply.steps[0].kind, "flash");

  // Joining two clips: the transition goes on the junction.
  calls.length = 0;
  await call("preset_apply", { preset: "whip left", video: [video, video] });
  assert.deepEqual(calls.find((c) => c.command === "applyRecipe").args.times, [16.2]);

  // Explicit times.
  calls.length = 0;
  await call("preset_apply", { preset: "Whip left", video, at: [1, 2.5] });
  assert.deepEqual(calls.find((c) => c.command === "applyRecipe").args.times, [1, 2.5]);

  // Grade: the reference look is converted to concrete effect values for the target.
  calls.length = 0;
  await call("preset_apply", { preset: "Reference look", video });
  const grade = calls.find((c) => c.command === "applyRecipe").args.steps[0];
  assert.equal(grade.kind, "grade");
  assert.equal(grade.reference, undefined);
  assert.equal(typeof grade.brightness, "number");

  // Rhythm: cuts at the reference shot lengths, then the named transition on each cut.
  calls.length = 0;
  await call("preset_apply", { preset: "Fast rhythm", video });
  const applies = calls.filter((c) => c.command === "applyRecipe").map((c) => c.args);
  assert.equal(applies.length, 2);
  assert.equal(applies[0].steps[0].kind, "cut");
  assert.ok(Math.abs(applies[0].times[0] - 3) < 0.05, `first cut ${applies[0].times[0]}`);
  assert.deepEqual(applies[1].times, applies[0].times);
  assert.equal(applies[1].name, "فلاش أبيض");

  await assert.rejects(call("preset_apply", { preset: "nothing", video }), /No preset named 'nothing'/);

  await client.close();
  await stop();
});
