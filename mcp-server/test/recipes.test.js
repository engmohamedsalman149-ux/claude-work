// Runs the ExtendScript recipe engine (ClaudeBridge.jsx) against a mock AE object model.
import { test } from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const { createAE } = createRequire(import.meta.url)("./mock-ae.cjs");
// Values created inside the vm realm have foreign prototypes, so compare plain copies.
const eq = (actual, expected, msg) => assert.deepEqual(JSON.parse(JSON.stringify(actual)), expected, msg);

function oneClip() {
  const ae = createAE();
  const res = ae.H.setupVideos({ paths: [import.meta.filename] });
  return { ...ae, comp: ae.app.project.activeItem, res };
}

const layers = (comp) => comp._layers.map((l) => ({ name: l.name, in: +l.inPoint.toFixed(3), out: +l.outPoint.toFixed(3), fx: l.comment === "claude-fx" }));

test("setupVideos joins clips and reports junctions", () => {
  const ae = createAE();
  const r = ae.H.setupVideos({ paths: [import.meta.filename, import.meta.dirname + "/mock-ae.cjs"] });
  assert.equal(r.clips.length, 2);
  eq(r.junctions, [10]);
  assert.equal(r.comp.duration, 20);
});

test("overlay moves (flash, zoom, whip, spin, blur, shake, dip, punch) create keyed FX layers without splitting", () => {
  const { H, comp } = oneClip();
  const steps = [
    { kind: "flash", start: -0.05, duration: 0.3, peak: 80 },
    { kind: "zoom", scale: [100, 180, 100] },
    { kind: "whip", direction: "right" },
    { kind: "spin", degrees: 180 },
    { kind: "blur", amount: 30 },
    { kind: "shake", amplitude: 10 },
    { kind: "dip", color: "#000000", holdStart: -0.05, holdEnd: 0.05 },
    { kind: "punch", scale: 120 },
  ];
  const r = H.applyRecipe({ comp: comp.id, layer: 1, times: [2, 6], steps, name: "Mix" });
  eq(r.warnings, []);
  assert.equal(r.created.length, 16);
  const footage = comp._layers.filter((l) => l.comment !== "claude-fx");
  assert.equal(footage.length, 1, "no split for overlay-only moves");

  const flash = comp._layers.find((l) => l.name === "Mix flash" && Math.abs(l.inPoint - 1.95) < 1e-6);
  const op = flash.property("ADBE Transform Group").property("ADBE Opacity");
  eq(op.keys.map((k) => [+k.t.toFixed(3), k.v]), [[1.95, 0], [2, 80], [2.25, 0]]);

  const zoom = comp._layers.find((l) => l.name === "Mix zoom" && l.inPoint < 3);
  const tf = zoom.property("ADBE Effect Parade").property("Transform");
  eq(tf.property("Scale Height").keys.map((k) => k.v), [100, 180, 100]);
  assert.equal(tf.property("Shutter Angle").value, 240);
  assert.equal(zoom.property("ADBE Effect Parade").property("Motion Tile").property("Mirror Edges").value, 1);

  const whip = comp._layers.find((l) => l.name === "Mix whip" && l.inPoint < 3);
  const pos = whip.property("ADBE Effect Parade").property("Transform").property("Position");
  eq(pos.keys.map((k) => k.v[0]), [960, 960 + 1920, 960 - 1920, 960]);

  const shake = comp._layers.find((l) => l.name === "Mix shake");
  assert.match(shake.property("ADBE Effect Parade").property("Transform").property("Position").expression, /wiggle\(12, 10\)/);
});

test("crossfade on a single clip splits it, freezes the outgoing frame and fades it out", () => {
  const { H, comp } = oneClip();
  const r = H.applyRecipe({ comp: comp.id, layer: 1, times: [4], steps: [{ kind: "crossfade", start: -0.25, duration: 0.5 }], name: "Dissolve" });
  eq(r.warnings, []);
  assert.equal(comp.numLayers, 2);
  const [top, bottom] = comp._layers;
  assert.equal(+top.inPoint.toFixed(3), 0, "outgoing half is moved on top");
  assert.equal(+top.outPoint.toFixed(3), 4.5);
  assert.equal(+bottom.inPoint.toFixed(3), 4);
  assert.ok(top.timeRemapEnabled);
  const remap = top.property("ADBE Time Remapping");
  assert.ok(Math.abs(remap.valueAtTime(4.4) - (4 - 1 / 30)) < 1e-6, "outgoing frame is held");
  eq(top.property("ADBE Transform Group").property("ADBE Opacity").keys.map((k) => [k.t, k.v]), [[4, 100], [4.5, 0]]);
});

test("crossfade at a clip junction reuses the existing edit instead of splitting", () => {
  const ae = createAE();
  const r0 = ae.H.setupVideos({ paths: [import.meta.filename, import.meta.filename + "x".slice(1)] });
  const comp = ae.app.project.activeItem;
  const r = ae.H.applyRecipe({ comp: comp.id, times: r0.junctions, steps: [{ kind: "crossfade", duration: 0.4 }], name: "X" });
  eq(r.warnings, []);
  assert.equal(comp.numLayers, 2);
});

test("cuts and jump cuts are applied latest-first so every split lands where asked", () => {
  const { H, comp } = oneClip();
  H.applyRecipe({ comp: comp.id, layer: 1, times: [3, 6], steps: [{ kind: "jump_cut", remove: 0.5 }], name: "Jump" });
  const ls = layers(comp).sort((a, b) => a.in - b.in);
  eq(ls.map((l) => [l.in, l.out]), [[0, 3], [3, 5.5], [5.5, 9]]);
  const mid = comp._layers.find((l) => Math.abs(l.inPoint - 3) < 1e-6);
  assert.equal(mid.startTime, -0.5, "content after the cut jumps ahead by 0.5s");
  assert.ok(Math.abs(comp._layers.find((l) => l.inPoint > 5).startTime + 1) < 1e-6, "later segments ripple left, no gaps");
});

test("push slides both shots and a speed ramp remaps time", () => {
  const { H, comp } = oneClip();
  let r = H.applyRecipe({ comp: comp.id, layer: 1, times: [5], steps: [{ kind: "push", direction: "left", duration: 0.4 }], name: "Push" });
  eq(r.warnings, []);
  const inn = comp._layers.find((l) => Math.abs(l.inPoint - 5) < 1e-6);
  eq(inn.property("ADBE Transform Group").property("ADBE Position").keys.map((k) => k.v[0]), [960 + 1920, 960]);

  const b = oneClip();
  r = b.H.applyRecipe({ comp: b.comp.id, layer: 1, times: [2], steps: [{ kind: "speed_ramp", start: 0, duration: 1, speed: 3 }], name: "Ramp" });
  eq(r.warnings, []);
  const L = b.comp.layer(1);
  const tr = L.property("ADBE Time Remapping");
  assert.equal(tr.valueAtTime(2), 2);
  assert.equal(tr.valueAtTime(3), 5);
  assert.ok(Math.abs(L.outPoint - 8) < 1e-6, "clip ends 2s earlier after playing 1s at 3x");
});

test("grade, generic effect and custom script steps", () => {
  const { H, comp } = oneClip();
  const r = H.applyRecipe({
    comp: comp.id, layer: 1, times: [1, 5], name: "Look",
    steps: [
      { kind: "grade", brightness: 10, contrast: 20, saturation: -30, tint: { color: "#ff8800", amount: 15 } },
      { kind: "effect", effect: "Glow", properties: { "Glow Radius": 50 }, keyframes: { "Glow Intensity": [[-0.2, 0], [0, 3], [0.2, 0]] } },
      { kind: "custom", script: "comp.name = 'renamed at ' + t; null" },
    ],
  });
  eq(r.warnings, []);
  const grades = comp._layers.filter((l) => l.name === "Look grade");
  assert.equal(grades.length, 1, "a whole-comp grade is added once");
  assert.equal(grades[0].outPoint, comp.duration);
  const fx = grades[0].property("ADBE Effect Parade");
  assert.equal(fx.property("Brightness & Contrast").property("Contrast").value, 20);
  assert.equal(fx.property("Vibrance").property("Saturation").value, -30);
  const glow = comp._layers.find((l) => l.name === "Look Glow" && l.inPoint < 2).property("ADBE Effect Parade").property("Glow");
  assert.equal(glow.property("Glow Radius").value, 50);
  eq(glow.property("Glow Intensity").keys.map((k) => [+k.t.toFixed(3), k.v]), [[0.8, 0], [1, 3], [1.2, 0]]);
  assert.equal(comp.name, "renamed at 1");
});

test("durationScale stretches timings and a bad step only produces a warning", () => {
  const { H, comp } = oneClip();
  const r = H.applyRecipe({ comp: comp.id, layer: 1, times: [3], durationScale: 2, name: "S", steps: [{ kind: "flash", start: -0.1, duration: 0.2 }, { kind: "effect", effect: "Nope" }] });
  assert.equal(r.warnings.length, 1);
  const flash = comp._layers.find((l) => l.name === "S flash");
  eq([+flash.inPoint.toFixed(3), +flash.outPoint.toFixed(3)], [2.8, 3.2]);
});
