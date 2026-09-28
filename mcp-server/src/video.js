// Video analysis with ffmpeg: detects cuts, dissolves, dips to black/white, flashes,
// motion transitions, shot rhythm, audio beats and the colour look of each shot.
import { spawn } from "node:child_process";
import fs from "node:fs/promises";
import path from "node:path";

let bins;

// FFMPEG_PATH / FFPROBE_PATH win, then the bundled npm binaries, then PATH.
export async function binaries() {
  if (bins) return bins;
  let ffmpeg = process.env.FFMPEG_PATH;
  let ffprobe = process.env.FFPROBE_PATH;
  if (!ffmpeg) {
    try {
      const p = (await import("ffmpeg-static")).default;
      // The package can be installed without its binary when npm skipped its install script.
      if (p && (await fs.access(p).then(() => true, () => false))) ffmpeg = p;
    } catch {}
  }
  if (!ffprobe) {
    try {
      ffprobe = (await import("@ffprobe-installer/ffprobe")).default.path;
    } catch {}
  }
  bins = { ffmpeg: ffmpeg || "ffmpeg", ffprobe: ffprobe || "ffprobe" };
  return bins;
}

function run(cmd, args, { binary = false } = {}) {
  return new Promise((resolve, reject) => {
    const p = spawn(cmd, args, { windowsHide: true });
    const out = [];
    let err = "";
    p.stdout.on("data", (d) => out.push(d));
    p.stderr.on("data", (d) => {
      err += d;
      if (err.length > 20000) err = err.slice(-10000);
    });
    p.on("error", (e) =>
      reject(e.code === "ENOENT" ? new Error(`${cmd} not found. Run setup again (it downloads ffmpeg), install ffmpeg, or set FFMPEG_PATH/FFPROBE_PATH.`) : e)
    );
    p.on("close", (code) => {
      const buf = Buffer.concat(out);
      if (code !== 0) return reject(new Error(`${path.basename(cmd)} failed (${code}): ${err.trim().split("\n").slice(-3).join(" ")}`));
      resolve(binary ? buf : buf.toString("utf8"));
    });
  });
}

export async function probe(file) {
  await fs.access(file).catch(() => {
    throw new Error(`Video not found: ${file}`);
  });
  const { ffprobe } = await binaries();
  const json = JSON.parse(
    await run(ffprobe, ["-v", "error", "-print_format", "json", "-show_format", "-show_streams", file])
  );
  const v = json.streams.find((s) => s.codec_type === "video");
  if (!v) throw new Error(`No video stream in ${file}`);
  const [n, d] = (v.avg_frame_rate || v.r_frame_rate || "30/1").split("/").map(Number);
  return {
    file: path.resolve(file),
    duration: Number(json.format.duration || v.duration || 0),
    width: v.width,
    height: v.height,
    fps: d ? n / d : n,
    codec: v.codec_name,
    hasAudio: json.streams.some((s) => s.codec_type === "audio"),
  };
}

// One decode pass at low resolution; returns per-frame luma/chroma stats and scene score.
export async function frameMetrics(file, { sampleFps } = {}) {
  const { ffmpeg } = await binaries();
  const vf = [sampleFps ? `fps=${sampleFps}` : null, "scale=160:-2", "signalstats", "select='gte(scene,0)'", "metadata=mode=print:file=-"]
    .filter(Boolean)
    .join(",");
  const out = await run(ffmpeg, ["-hide_banner", "-nostats", "-i", file, "-map", "0:v:0", "-vf", vf, "-an", "-f", "null", "-"]);
  const frames = [];
  let cur = null;
  for (const line of out.split("\n")) {
    if (line.startsWith("frame:")) {
      const m = /pts_time:([\d.eE+-]+)/.exec(line);
      cur = { t: m ? Number(m[1]) : frames.length };
      frames.push(cur);
    } else if (cur) {
      const eq = line.indexOf("=");
      if (eq < 0) continue;
      const key = line.slice(0, eq).trim();
      const val = Number(line.slice(eq + 1));
      if (key === "lavfi.scene_score") cur.scene = val;
      else if (key.startsWith("lavfi.signalstats.")) {
        const k = key.slice(18);
        if (k === "YAVG") cur.y = val;
        else if (k === "YLOW") cur.ylow = val;
        else if (k === "YHIGH") cur.yhigh = val;
        else if (k === "SATAVG") cur.sat = val;
        else if (k === "UAVG") cur.u = val;
        else if (k === "VAVG") cur.v = val;
        else if (k === "YDIF") cur.dif = val;
      }
    }
  }
  return frames;
}

// ~20 Hz RMS envelope of the first audio stream, in dB.
export async function audioEnvelope(file) {
  const { ffmpeg } = await binaries();
  const out = await run(ffmpeg, [
    "-hide_banner", "-nostats", "-i", file, "-map", "0:a:0", "-vn",
    "-af", "aresample=22050,asetnsamples=n=1102:p=0,astats=metadata=1:reset=1,ametadata=mode=print:key=lavfi.astats.Overall.RMS_level:file=-",
    "-f", "null", "-",
  ]);
  const env = [];
  let t = null;
  for (const line of out.split("\n")) {
    if (line.startsWith("frame:")) {
      const m = /pts_time:([\d.eE+-]+)/.exec(line);
      t = m ? Number(m[1]) : null;
    } else if (line.includes("RMS_level=") && t !== null) {
      const v = Number(line.split("=")[1]);
      env.push({ t, db: Number.isFinite(v) ? v : -120 });
    }
  }
  return env;
}

// Onsets = sharp rises in loudness; a rough stand-in for beats / hits.
export function detectOnsets(env) {
  const onsets = [];
  for (let i = 3; i < env.length; i++) {
    const prev = (env[i - 1].db + env[i - 2].db + env[i - 3].db) / 3;
    const rise = env[i].db - prev;
    if (rise > 6 && env[i].db > -45 && (!onsets.length || env[i].t - onsets[onsets.length - 1].t > 0.15)) {
      onsets.push({ t: round(env[i].t), strength: round(rise, 1) });
    }
  }
  return onsets;
}

const round = (x, d = 3) => Math.round(x * 10 ** d) / 10 ** d;
const median = (a) => {
  if (!a.length) return 0;
  const s = [...a].sort((x, y) => x - y);
  const m = s.length >> 1;
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
};
const mean = (a) => (a.length ? a.reduce((x, y) => x + y, 0) / a.length : 0);

// Limited-range video has black at 16, full-range at 0.
const isBlack = (f) => f.y < 24 && f.yhigh < 48;

export function detectEvents(frames, fps) {
  const n = frames.length;
  const fd = 1 / (fps || 30);
  const events = [];
  if (n < 3) return { events, shots: [] };

  // Rolling baseline of frame-to-frame change (±1.5s) so camera motion isn't mistaken for edits.
  const w = Math.max(5, Math.round(1.5 * (fps || 30)));
  const base = frames.map((_, i) => median(frames.slice(Math.max(0, i - w), Math.min(n, i + w + 1)).map((f) => f.dif ?? 0)));

  const active = frames.map((f, i) => {
    const d = f.dif ?? 0;
    return (f.scene ?? 0) > 0.3 || d > Math.max(3 * base[i], base[i] + 3);
  });

  // Group active frames into segments, bridging gaps of up to 2 frames.
  const segs = [];
  for (let i = 0; i < n; i++) {
    if (!active[i]) continue;
    const last = segs[segs.length - 1];
    if (last && i - last.end <= 3) last.end = i;
    else segs.push({ start: i, end: i });
  }

  // Also include black runs that may sit between two fade segments.
  for (const s of segs) {
    let e = s.end;
    while (e + 1 < n && isBlack(frames[e + 1])) e++;
    s.end = e;
  }
  const merged = [];
  for (const s of segs) {
    const last = merged[merged.length - 1];
    if (last && s.start <= last.end + 3) last.end = Math.max(last.end, s.end);
    else merged.push({ ...s });
  }

  const ctx = (i0, i1) => frames.slice(Math.max(0, i0), Math.max(0, Math.min(n, i1)));
  for (const s of merged) {
    const seg = frames.slice(s.start, s.end + 1);
    const before = ctx(s.start - Math.round(0.5 / fd), s.start);
    const after = ctx(s.end + 1, s.end + 1 + Math.round(0.5 / fd));
    const yBefore = before.length ? median(before.map((f) => f.y)) : seg[0].y;
    const yAfter = after.length ? median(after.map((f) => f.y)) : seg[seg.length - 1].y;
    const satAround = Math.max(before.length ? median(before.map((f) => f.sat ?? 0)) : 0, after.length ? median(after.map((f) => f.sat ?? 0)) : 0);
    const maxScene = Math.max(...seg.map((f) => f.scene ?? 0));
    const peak = seg.reduce((a, f) => (f.y > a.y ? f : a), seg[0]);
    const blacks = seg.filter(isBlack);
    const tStart = seg[0].t - fd; // change starts between previous frame and this one
    const tEnd = seg[seg.length - 1].t;
    const dur = round(tEnd - tStart);
    const difs = seg.map((f) => f.dif ?? 0);
    const cv = difs.length > 1 ? Math.sqrt(mean(difs.map((d) => (d - mean(difs)) ** 2))) / (mean(difs) || 1) : 0;
    const monotonic = (() => {
      const ys = seg.map((f) => f.y);
      let up = 0, down = 0;
      for (let i = 1; i < ys.length; i++) (ys[i] >= ys[i - 1] ? up++ : down++);
      return Math.max(up, down) / Math.max(1, ys.length - 1);
    })();

    const ev = { start: round(tStart), end: round(tEnd), duration: dur };

    if (seg.length <= 2 && maxScene > 0.3) {
      const cutFrame = seg.reduce((a, f) => ((f.scene ?? 0) > (a.scene ?? 0) ? f : a), seg[0]);
      Object.assign(ev, { type: "cut", time: round(cutFrame.t), duration: 0, confidence: round(Math.min(1, maxScene + 0.2), 2) });
      ev.suggestedRecipe = { category: "cut", steps: [{ kind: "cut" }] };
    } else if (blacks.length) {
      const firstBlack = blacks[0].t;
      const lastBlack = blacks[blacks.length - 1].t;
      const fadeOut = round(Math.max(0, firstBlack - tStart));
      const fadeIn = round(Math.max(0, tEnd - lastBlack));
      const hold = round(lastBlack - firstBlack + fd);
      const mid = round((firstBlack + lastBlack) / 2);
      Object.assign(ev, {
        type: "dip_to_black",
        time: mid,
        fadeOut, hold, fadeIn,
        confidence: 0.9,
      });
      ev.suggestedRecipe = {
        category: "transition",
        steps: [{ kind: "dip", color: "#000000", start: round(tStart - mid), duration: dur, holdStart: round(firstBlack - mid), holdEnd: round(lastBlack + fd - mid) }],
      };
    } else if (peak.y - Math.max(yBefore, yAfter) > 35 && peak.y > 170 && (peak.sat ?? 0) < Math.max(25, 0.5 * satAround)) {
      const attack = round(Math.max(fd, peak.t - tStart));
      const release = round(Math.max(fd, tEnd - peak.t));
      const white = 235;
      const opacity = Math.min(100, Math.round(((peak.y - Math.max(yBefore, yAfter)) / Math.max(1, white - Math.max(yBefore, yAfter))) * 100));
      const hasCut = maxScene > 0.3;
      Object.assign(ev, {
        type: hasCut || Math.abs(yBefore - yAfter) > 10 ? "flash_transition" : "flash",
        time: round(peak.t),
        attack, release, peakLuma: round(peak.y, 1), estimatedOpacity: opacity,
        confidence: 0.8,
      });
      const u = mean(seg.map((f) => f.u ?? 128)), v = mean(seg.map((f) => f.v ?? 128));
      const tinted = Math.abs(u - 128) > 8 || Math.abs(v - 128) > 8;
      ev.suggestedRecipe = {
        category: "transition",
        steps: [{ kind: "flash", color: tinted ? yuvToHex(peak.y, u, v) : "#ffffff", start: -attack, duration: round(attack + release), peakAt: 0, peak: opacity }],
      };
    } else if (maxScene <= 0.3 && cv < 0.6 && monotonic > 0.7 && seg.length >= 4) {
      Object.assign(ev, { type: "dissolve", time: round((tStart + tEnd) / 2), confidence: 0.7 });
      ev.suggestedRecipe = { category: "transition", steps: [{ kind: "crossfade", start: round(-dur / 2), duration: dur }] };
    } else if (maxScene > 0.3 || Math.abs(yBefore - yAfter) > 12) {
      // Change of shot hidden inside motion: zoom/whip/spin/glitch transitions look like this.
      const cutFrame = seg.reduce((a, f) => ((f.scene ?? 0) > (a.scene ?? 0) ? f : a), seg[0]);
      const t = round(cutFrame.t);
      Object.assign(ev, {
        type: "motion_transition",
        time: t,
        motionBefore: round(t - tStart),
        motionAfter: round(tEnd - t),
        peakMotion: round(Math.max(...difs), 1),
        confidence: 0.5,
        note: "Shot changes during fast motion: likely a zoom, whip pan, spin or glitch transition. Check the frames to decide which.",
      });
      ev.suggestedRecipe = {
        category: "transition",
        steps: [{ kind: "zoom", start: round(tStart - t), duration: dur, peakAt: 0, scale: [100, 200, 100], motionBlur: true }],
      };
    } else {
      Object.assign(ev, {
        type: "motion",
        time: round((tStart + tEnd) / 2),
        peakMotion: round(Math.max(...difs), 1),
        confidence: 0.3,
        note: "Burst of motion without a change of shot: camera move, shake, speed ramp or an effect. Check the frames.",
      });
      ev.suggestedRecipe = { category: "effect", steps: [{ kind: "shake", start: round(tStart - ev.time), duration: dur, amplitude: 25, frequency: 12 }] };
    }
    events.push(ev);
  }

  // A hard cut right next to a burst of motion is one move (zoom/whip into the cut), not two.
  for (let i = 0; i < events.length; i++) {
    const cut = events[i];
    if (cut.type !== "cut") continue;
    const near = [events[i - 1], events[i + 1]].find(
      (e) => e && (e.type === "motion" || e.type === "motion_transition") && Math.min(Math.abs(e.end - cut.time), Math.abs(e.start - cut.time)) <= 0.25
    );
    if (!near) continue;
    const start = Math.min(near.start, cut.start), end = Math.max(near.end, cut.end);
    Object.assign(near, {
      type: "motion_transition", time: cut.time, start, end, duration: round(end - start),
      motionBefore: round(cut.time - start), motionAfter: round(end - cut.time), confidence: 0.6,
      note: "Shot changes during fast motion: likely a zoom, whip pan, spin or glitch transition. Check the frames to decide which.",
    });
    near.suggestedRecipe = {
      category: "transition",
      steps: [{ kind: "zoom", start: round(start - cut.time), duration: round(end - start), peakAt: 0, scale: [100, 200, 100], motionBlur: true }],
    };
    events.splice(i, 1);
    i--;
  }

  // Shots = spans between edit events.
  const bounds = [];
  for (const e of events) {
    if (e.type === "motion") continue;
    bounds.push(e.type === "cut" ? [e.time, e.time] : [e.start, e.end]);
  }
  const shots = [];
  let from = frames[0].t;
  const endT = frames[n - 1].t + fd;
  for (const [s, e] of [...bounds, [endT, endT]]) {
    if (s - from > fd * 1.5) {
      const fr = frames.filter((f) => f.t >= from && f.t < s);
      shots.push({ start: round(from), end: round(s), duration: round(s - from), look: lookOf(fr), motion: round(mean(fr.map((f) => f.dif ?? 0)), 2) });
    }
    from = e;
  }
  events.forEach((e, i) => (e.id = `e${i + 1}`));
  shots.forEach((s, i) => (s.id = `s${i + 1}`));
  return { events, shots };
}

export function lookOf(frames) {
  if (!frames.length) return null;
  return {
    luma: round(mean(frames.map((f) => f.y)), 1),
    contrast: round(mean(frames.map((f) => (f.yhigh ?? 235) - (f.ylow ?? 16))), 1),
    saturation: round(mean(frames.map((f) => f.sat ?? 0)), 1),
    u: round(mean(frames.map((f) => f.u ?? 128)), 1),
    v: round(mean(frames.map((f) => f.v ?? 128)), 1),
  };
}

function yuvToHex(y, u, v) {
  const c = (x) => Math.max(0, Math.min(255, Math.round(x)));
  const r = c(y + 1.402 * (v - 128));
  const g = c(y - 0.344136 * (u - 128) - 0.714136 * (v - 128));
  const b = c(y + 1.772 * (u - 128));
  return "#" + [r, g, b].map((x) => x.toString(16).padStart(2, "0")).join("");
}

export function rhythm(events, shots, onsets = []) {
  const cuts = events.filter((e) => e.type !== "motion").map((e) => e.time);
  const durs = shots.map((s) => s.duration);
  const total = shots.length ? shots[shots.length - 1].end - shots[0].start : 0;
  const out = {
    edits: cuts.length,
    editsPerMinute: total ? round((cuts.length / total) * 60, 1) : 0,
    averageShot: round(mean(durs), 2),
    medianShot: round(median(durs), 2),
    shortestShot: durs.length ? round(Math.min(...durs), 2) : 0,
    longestShot: durs.length ? round(Math.max(...durs), 2) : 0,
    shotDurations: durs.map((d) => round(d, 2)),
  };
  if (onsets.length && cuts.length) {
    const onBeat = cuts.filter((c) => onsets.some((o) => Math.abs(o.t - c) < 0.1)).length;
    out.cutsOnBeat = round(onBeat / cuts.length, 2);
  }
  return out;
}

export async function analyzeVideo(file, { withAudio = true } = {}) {
  const info = await probe(file);
  const frames = await frameMetrics(info.file);
  const { events, shots } = detectEvents(frames, info.fps);
  let onsets = [];
  if (withAudio && info.hasAudio) {
    try {
      onsets = detectOnsets(await audioEnvelope(info.file));
    } catch {}
  }
  if (onsets.length) {
    for (const e of events) e.onBeat = onsets.some((o) => Math.abs(o.t - e.time) < 0.1);
  }
  return {
    video: info,
    events,
    shots,
    rhythm: rhythm(events, shots, onsets),
    look: lookOf(frames),
    audioOnsets: onsets.map((o) => o.t),
  };
}

// Fast whole-video look (2 fps sample), used to match a grade onto another clip.
export async function videoLook(file) {
  const frames = await frameMetrics(path.resolve(file), { sampleFps: 2 });
  return lookOf(frames.filter((f) => !isBlack(f)));
}

// Horizontal strip of frames at the given times, as JPEG.
export async function frameStrip(file, times, { width = 256 } = {}) {
  const { ffmpeg } = await binaries();
  const args = ["-hide_banner", "-loglevel", "error"];
  for (const t of times) args.push("-ss", String(Math.max(0, t)), "-i", file);
  const parts = times.map((_, i) => `[${i}:v:0]scale=${width}:-2,setsar=1,format=yuvj420p[f${i}]`);
  const stack = times.length > 1 ? `${times.map((_, i) => `[f${i}]`).join("")}hstack=inputs=${times.length}[out]` : `[f0]null[out]`;
  args.push("-filter_complex", [...parts, stack].join(";"), "-map", "[out]", "-frames:v", "1", "-f", "image2pipe", "-c:v", "mjpeg", "-q:v", "4", "-");
  return run(ffmpeg, args, { binary: true });
}

// Frames around an event: before, during, after.
export function stripTimes(ev, duration) {
  const s = ev.start ?? ev.time, e = ev.end ?? ev.time;
  const pad = Math.max(0.15, (e - s) * 0.25);
  const ts = [s - pad * 2, s - pad * 0.3, (s + e) / 2, e + pad * 0.3, e + pad * 2];
  return ts.map((t) => round(Math.min(Math.max(0, t), Math.max(0, duration - 0.05))));
}
