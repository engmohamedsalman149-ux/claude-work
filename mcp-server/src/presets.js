// Named library of editing moves ("presets") extracted from analysed videos.
import fs from "node:fs/promises";
import path from "node:path";
import { z } from "zod";
import { defaultBridgeDir } from "./bridge.js";

export function defaultLibraryDir() {
  return process.env.AE_LIBRARY_DIR || path.join(path.dirname(defaultBridgeDir()), "claude-edit-library");
}

const num = z.number();
const color = z.union([z.string(), z.array(z.number())]);

// Every step is timed relative to the anchor time (the cut point): start < 0 means before it.
export const stepSchema = z
  .object({
    kind: z.enum([
      "cut", "jump_cut", "crossfade", "dip", "flash", "zoom", "punch", "whip", "spin",
      "blur", "shake", "push", "speed_ramp", "grade", "effect", "custom",
    ]),
    start: num.optional().describe("Seconds relative to the anchor (negative = before)"),
    duration: num.optional().describe("Seconds"),
    peakAt: num.optional().describe("Seconds relative to the anchor where the move peaks (default 0)"),
    color: color.optional(),
    peak: num.optional().describe("flash: peak opacity 0-100"),
    blendingMode: z.string().optional(),
    holdStart: num.optional(),
    holdEnd: num.optional(),
    scale: z.union([num, z.array(num)]).optional().describe("zoom: [from, peak, to] percent; punch: percent"),
    motionBlur: z.boolean().optional(),
    shutterAngle: num.optional(),
    mirrorEdges: z.boolean().optional(),
    direction: z.enum(["left", "right", "up", "down"]).optional(),
    distance: num.optional().describe("whip/push: fraction of the frame (1 = full width)"),
    degrees: num.optional(),
    amount: num.optional().describe("blur: blurriness"),
    amplitude: num.optional(),
    frequency: num.optional(),
    rotation: num.optional(),
    remove: num.optional().describe("jump_cut: seconds removed after the cut"),
    speed: num.optional().describe("speed_ramp: playback speed inside the ramp"),
    ease: z.enum(["easyEase", "linear", "easeIn", "easeOut", "strong"]).optional(),
    brightness: num.optional(),
    contrast: num.optional(),
    saturation: num.optional(),
    tint: z.object({ color, amount: num }).optional(),
    reference: z
      .object({ luma: num, contrast: num, saturation: num, u: num.optional(), v: num.optional() })
      .optional()
      .describe("grade: look measured from the source video; matched onto the target at apply time"),
    effect: z.string().optional().describe("effect: match name or display name"),
    properties: z.record(z.any()).optional(),
    keyframes: z.record(z.array(z.tuple([num, z.any()]))).optional().describe("effect: param -> [[relTime, value], ...]"),
    adjustment: z.boolean().optional(),
    script: z.string().optional().describe("custom: ExtendScript run with comp, layer, outLayer, inLayer, t, step, fx helpers"),
  })
  .passthrough();

export const presetSchema = z.object({
  name: z.string().min(1),
  category: z.enum(["transition", "cut", "effect", "grade", "rhythm", "custom"]),
  description: z.string().optional(),
  steps: z.array(stepSchema).default([]),
  rhythm: z
    .object({
      shotDurations: z.array(num).optional(),
      useBeats: z.boolean().optional(),
      everyNthBeat: z.number().int().optional(),
      transition: z.string().optional().describe("Name of a transition preset to put on every cut"),
      jumpRemove: num.optional(),
    })
    .optional(),
  source: z.object({ video: z.string().optional(), time: num.optional(), eventId: z.string().optional() }).optional(),
  tags: z.array(z.string()).optional(),
});

const fileName = (name) =>
  name
    .trim()
    .replace(/[<>:"/\\|?*\x00-\x1f]/g, "")
    .replace(/\s+/g, "-")
    .toLowerCase()
    .slice(0, 80) || "preset";

export class Library {
  constructor(dir = defaultLibraryDir()) {
    this.dir = dir;
    this.presetDir = path.join(dir, "presets");
    this.analysisDir = path.join(dir, "analyses");
  }

  async ensure() {
    await fs.mkdir(this.presetDir, { recursive: true });
    await fs.mkdir(this.analysisDir, { recursive: true });
  }

  async list() {
    await this.ensure();
    const out = [];
    for (const f of await fs.readdir(this.presetDir)) {
      if (!f.endsWith(".json")) continue;
      try {
        out.push(JSON.parse(await fs.readFile(path.join(this.presetDir, f), "utf8")));
      } catch {}
    }
    return out.sort((a, b) => a.name.localeCompare(b.name));
  }

  async get(name) {
    const all = await this.list();
    const key = name.trim().toLowerCase();
    const p = all.find((x) => x.name.toLowerCase() === key) || all.find((x) => fileName(x.name) === fileName(name));
    if (!p) {
      const near = all.filter((x) => x.name.toLowerCase().includes(key) || key.includes(x.name.toLowerCase()));
      const hint = (near.length ? near : all).map((x) => x.name).slice(0, 20).join(", ");
      throw new Error(`No preset named '${name}'. ${hint ? "Available: " + hint : "The library is empty."}`);
    }
    return p;
  }

  async save(preset, { overwrite = false } = {}) {
    await this.ensure();
    const p = presetSchema.parse(preset);
    const file = path.join(this.presetDir, `${fileName(p.name)}.json`);
    const exists = await fs.access(file).then(() => true, () => false);
    if (exists && !overwrite) throw new Error(`A preset named '${p.name}' already exists. Pass overwrite: true to replace it.`);
    const now = new Date().toISOString();
    const stored = { ...p, updated: now, created: exists ? JSON.parse(await fs.readFile(file, "utf8")).created ?? now : now };
    await fs.writeFile(file, JSON.stringify(stored, null, 2), "utf8");
    return { ...stored, file };
  }

  async remove(name) {
    const p = await this.get(name);
    await fs.rm(path.join(this.presetDir, `${fileName(p.name)}.json`), { force: true });
    return { deleted: p.name };
  }

  async saveAnalysis(analysis) {
    await this.ensure();
    const base = fileName(path.basename(analysis.video.file).replace(/\.[^.]+$/, ""));
    const file = path.join(this.analysisDir, `${base}.json`);
    await fs.writeFile(file, JSON.stringify(analysis, null, 2), "utf8");
    return file;
  }

  async loadAnalysis(videoFile) {
    const base = fileName(path.basename(videoFile).replace(/\.[^.]+$/, ""));
    try {
      const a = JSON.parse(await fs.readFile(path.join(this.analysisDir, `${base}.json`), "utf8"));
      return a.video.file === path.resolve(videoFile) ? a : null;
    } catch {
      return null;
    }
  }
}

// Match a measured reference look onto a target look with basic AE effects.
export function gradeFromLooks(ref, target) {
  const clamp = (x, lo, hi) => Math.max(lo, Math.min(hi, x));
  const r = (x) => Math.round(x * 10) / 10;
  const out = {
    brightness: r(clamp((ref.luma - target.luma) * 0.9, -150, 150)),
    contrast: r(clamp((ref.contrast / Math.max(1, target.contrast) - 1) * 100, -100, 100)),
    saturation: r(clamp((ref.saturation / Math.max(1, target.saturation) - 1) * 100, -100, 100)),
  };
  if (ref.u !== undefined && ref.v !== undefined) {
    const du = ref.u - 128, dv = ref.v - 128;
    const strength = Math.hypot(du, dv);
    if (strength > 3) {
      const y = 128;
      const c = (x) => Math.max(0, Math.min(255, Math.round(x)));
      const hex = [y + 1.402 * dv * 4, y - 0.344136 * du * 4 - 0.714136 * dv * 4, y + 1.772 * du * 4]
        .map((x) => c(x).toString(16).padStart(2, "0"))
        .join("");
      out.tint = { color: `#${hex}`, amount: r(clamp(strength * 2, 0, 40)) };
    }
  }
  return out;
}
