// Tools for learning editing moves from reference videos and re-applying them by name.
import path from "node:path";
import { z } from "zod";
import { analyzeVideo, detectOnsets, audioEnvelope, frameStrip, stripTimes, videoLook, probe } from "./video.js";
import { Library, presetSchema, gradeFromLooks } from "./presets.js";

export const EDITING_INSTRUCTIONS = `
Editing-style workflow (video analysis -> named presets -> apply in After Effects):
1. video_analyze on a reference video. It returns detected edits (cut, dissolve, dip_to_black, flash,
   flash_transition, motion_transition, motion), shot rhythm, the colour look, and frame strips around each edit.
   Look at the frame strips to decide what each move really is (zoom in/out, whip pan, spin, glitch, slide...)
   and fix the suggestedRecipe when the signal-based guess is wrong. Use video_frames to inspect any moment closer.
2. Describe the moves to the user and save the ones they want with preset_save (or preset_from_event),
   using the name the user gives (any language). Keep timings from the analysis so the move feels the same.
3. When the user says e.g. "apply <name> to <video>", call preset_apply with that preset name and the video path
   (or an AE comp/layer). With no time given it goes on every edit point: clip junctions, or detected cuts.
Step kinds: cut, jump_cut, crossfade, dip, flash, zoom, punch, whip, spin, blur, shake, push, speed_ramp,
grade, effect (any AE effect with keyframes), custom (ExtendScript). Times are seconds relative to the edit point.
`;

const text = (data) => ({ content: [{ type: "text", text: typeof data === "string" ? data : JSON.stringify(data, null, 2) }] });
const errorResult = (e) => ({ ...text(`Error: ${e.message}`), isError: true });
const img = (buf) => ({ type: "image", data: buf.toString("base64"), mimeType: "image/jpeg" });

export function registerEditingTools(server, bridge, lib = new Library()) {
  const analysisCache = new Map();

  async function getAnalysis(file, { fresh = false } = {}) {
    const abs = path.resolve(file);
    if (!fresh) {
      if (analysisCache.has(abs)) return analysisCache.get(abs);
      const saved = await lib.loadAnalysis(abs);
      if (saved) {
        analysisCache.set(abs, saved);
        return saved;
      }
    }
    const a = await analyzeVideo(abs);
    analysisCache.set(abs, a);
    a.savedTo = await lib.saveAnalysis(a);
    return a;
  }

  server.registerTool(
    "video_analyze",
    {
      description:
        "Analyse a video's editing: detects cuts, dissolves, dips to black, flashes, zoom/whip-style motion transitions, " +
        "shot rhythm, cuts on the beat and the colour look. Returns the events with suggested recipes plus frame strips " +
        "(before / during / after) for each edit so you can see what the move is. Needs ffmpeg (bundled via npm).",
      inputSchema: {
        video: z.string().describe("Absolute path of the video file"),
        maxStrips: z.number().int().min(0).max(30).optional().describe("How many events get a frame strip (default 10)"),
        includeCuts: z.boolean().optional().describe("Also send strips for plain hard cuts (default only if there are few other events)"),
        fresh: z.boolean().optional().describe("Re-analyse even if a saved analysis exists"),
      },
    },
    async ({ video, maxStrips = 10, includeCuts, fresh }) => {
      try {
        const a = await getAnalysis(video, { fresh });
        const special = a.events.filter((e) => e.type !== "cut");
        const cuts = a.events.filter((e) => e.type === "cut");
        const withStrips = [...special, ...(includeCuts || special.length < maxStrips ? cuts : [])].slice(0, maxStrips);
        const summary = {
          video: a.video,
          savedTo: a.savedTo,
          rhythm: a.rhythm,
          look: a.look,
          counts: a.events.reduce((m, e) => ((m[e.type] = (m[e.type] || 0) + 1), m), {}),
          events: a.events.slice(0, 300),
          shots: a.shots.length > 150 ? `${a.shots.length} shots (see savedTo for all)` : a.shots,
          audioOnsets: a.audioOnsets.length > 200 ? `${a.audioOnsets.length} onsets` : a.audioOnsets,
        };
        const content = [{ type: "text", text: JSON.stringify(summary, null, 2) }];
        for (const e of withStrips) {
          const times = stripTimes(e, a.video.duration);
          try {
            const buf = await frameStrip(a.video.file, times);
            content.push({ type: "text", text: `${e.id} ${e.type} @ ${e.time}s - frames at ${times.join(", ")}s` });
            content.push(img(buf));
          } catch (err) {
            content.push({ type: "text", text: `${e.id}: could not extract frames (${err.message})` });
          }
        }
        return { content };
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "video_frames",
    {
      description: "Extract frames from a video as one horizontal strip so you can inspect a moment (e.g. around an edit).",
      inputSchema: {
        video: z.string(),
        times: z.array(z.number()).min(1).max(12).optional().describe("Exact times in seconds"),
        around: z.number().optional().describe("Centre time; used with span/count when times is omitted"),
        span: z.number().optional().describe("Total seconds covered around 'around' (default 0.6)"),
        count: z.number().int().min(2).max(12).optional().describe("Frames for around/span (default 6)"),
        width: z.number().int().min(64).max(640).optional().describe("Width of each frame (default 256)"),
      },
    },
    async ({ video, times, around, span = 0.6, count = 6, width }) => {
      try {
        const info = await probe(video);
        let ts = times;
        if (!ts) {
          if (around === undefined) throw new Error("Pass times or around");
          ts = Array.from({ length: count }, (_, i) => around - span / 2 + (span * i) / (count - 1));
        }
        ts = ts.map((t) => Math.round(Math.min(Math.max(0, t), Math.max(0, info.duration - 0.05)) * 1000) / 1000);
        const buf = await frameStrip(info.file, ts, { width });
        return { content: [{ type: "text", text: `frames at ${ts.join(", ")}s` }, img(buf)] };
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_save",
    {
      description:
        "Save an editing move under a name (any language) so it can be applied later with preset_apply. " +
        "Steps are timed in seconds relative to the edit point (start < 0 = before the cut).",
      inputSchema: { ...presetSchema.shape, overwrite: z.boolean().optional() },
    },
    async ({ overwrite, ...preset }) => {
      try {
        return text(await lib.save(preset, { overwrite }));
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_from_event",
    {
      description:
        "Save a detected event from a video_analyze result as a named preset, using its suggested recipe " +
        "(optionally replacing the steps after you checked the frames). Use eventId 'look' to save the video's colour grade " +
        "and 'rhythm' to save its cutting rhythm.",
      inputSchema: {
        video: z.string(),
        eventId: z.string().describe("e.g. 'e3', or 'look' / 'rhythm'"),
        name: z.string(),
        description: z.string().optional(),
        steps: z.array(z.any()).optional().describe("Replace the suggested steps"),
        useBeats: z.boolean().optional().describe("rhythm: cut on the target's audio beats instead of copying shot lengths"),
        transition: z.string().optional().describe("rhythm: preset to place on every cut"),
        overwrite: z.boolean().optional(),
      },
    },
    async ({ video, eventId, name, description, steps, useBeats, transition, overwrite }) => {
      try {
        const a = await getAnalysis(video);
        let preset;
        const source = { video: a.video.file, eventId };
        if (eventId === "look") {
          preset = { name, category: "grade", description, source, steps: steps || [{ kind: "grade", reference: a.look }] };
        } else if (eventId === "rhythm") {
          preset = {
            name, category: "rhythm", description, source, steps: steps || [],
            rhythm: { shotDurations: a.rhythm.shotDurations, useBeats, transition },
          };
        } else {
          const ev = a.events.find((e) => e.id === eventId);
          if (!ev) throw new Error(`No event ${eventId}. Events: ${a.events.map((e) => `${e.id}:${e.type}`).join(", ")}`);
          preset = {
            name,
            category: ev.suggestedRecipe.category,
            description: description || `${ev.type} learned from ${path.basename(a.video.file)} at ${ev.time}s`,
            source: { ...source, time: ev.time },
            steps: steps || ev.suggestedRecipe.steps,
          };
        }
        return text(await lib.save(preset, { overwrite }));
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_list",
    { description: "List saved editing presets (name, category, description, steps).", inputSchema: { category: z.string().optional() } },
    async ({ category }) => {
      try {
        const all = await lib.list();
        return text({
          library: lib.dir,
          presets: all
            .filter((p) => !category || p.category === category)
            .map((p) => ({ name: p.name, category: p.category, description: p.description, steps: p.steps.map((s) => s.kind), rhythm: p.rhythm ? true : undefined })),
        });
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_get",
    { description: "Show one preset in full.", inputSchema: { name: z.string() } },
    async ({ name }) => {
      try {
        return text(await lib.get(name));
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_delete",
    { description: "Delete a saved preset.", inputSchema: { name: z.string() } },
    async ({ name }) => {
      try {
        return text(await lib.remove(name));
      } catch (e) {
        return errorResult(e);
      }
    }
  );

  server.registerTool(
    "preset_apply",
    {
      description:
        "Apply a saved preset (transition, cut style, effect, grade or rhythm) in After Effects. Give a video path " +
        "(or several clips to join) and it builds a comp, or target an existing comp/layer. 'at' picks the edit points: " +
        "seconds, 'cuts' (detected in the footage), 'junctions' (between clips) or 'playhead'. Everything is one undo step.",
      inputSchema: {
        preset: z.string().describe("Preset name"),
        video: z.union([z.string(), z.array(z.string())]).optional().describe("Video path, or several clips to join end to end"),
        comp: z.union([z.string(), z.number()]).optional().describe("Existing comp instead of video"),
        layer: z.union([z.string(), z.number()]).optional().describe("Footage layer in that comp"),
        at: z
          .union([z.number(), z.array(z.number()), z.enum(["cuts", "junctions", "playhead"])])
          .optional()
          .describe("Comp time(s) in seconds, or 'cuts' / 'junctions' / 'playhead'. Default: junctions, else detected cuts."),
        durationScale: z.number().positive().optional().describe("Stretch (>1) or tighten (<1) the move's timing"),
        timeoutSec: z.number().optional(),
      },
    },
    async ({ preset: presetName, video, comp, layer, at, durationScale, timeoutSec = 300 }) => {
      try {
        const preset = await lib.get(presetName);
        const opts = { timeoutMs: timeoutSec * 1000 };
        let junctions = [];
        let sourceFile = null;
        let mapping = { startTime: 0, inPoint: 0, outPoint: Infinity };

        if (video) {
          const paths = [].concat(video).map((p) => path.resolve(p));
          const res = await bridge.send("setupVideos", { paths }, opts);
          comp = res.comp.id;
          junctions = res.junctions;
          if (paths.length === 1) {
            sourceFile = paths[0];
            layer = res.clips[0].index;
            mapping = { startTime: 0, inPoint: 0, outPoint: res.clips[0].end };
          }
        }

        const needSource = at === "cuts" || preset.category === "rhythm" || preset.steps.some((s) => s.kind === "grade" && s.reference)
          || (at === undefined && !junctions.length && preset.category !== "grade");
        if (needSource && !sourceFile) {
          const src = await bridge.send("layerSource", { comp, layer }, opts);
          if (!src.file) throw new Error(`Layer '${src.layer}' has no source file to analyse`);
          sourceFile = src.file;
          layer = src.index;
          comp = comp ?? src.comp;
          mapping = src;
        }
        const toComp = (t) => mapping.startTime + t;
        const inLayer = (t) => t > (mapping.inPoint ?? 0) + 0.01 && t < (mapping.outPoint ?? Infinity) - 0.01;

        let times;
        if (typeof at === "number") times = [at];
        else if (Array.isArray(at)) times = at;
        else if (at === "playhead") times = [(await bridge.send("getComp", { comp }, opts)).time];
        else if (at === "junctions") times = junctions;
        else if (preset.category === "grade") times = [0];
        else if (at === "cuts" || !junctions.length) {
          const a = await getAnalysis(sourceFile);
          times = a.events.filter((e) => e.type !== "motion").map((e) => toComp(e.time)).filter(inLayer);
        } else times = junctions;

        let steps = preset.steps.map((s) => ({ ...s }));

        // Colour grade: match the reference look onto this footage.
        for (const s of steps) {
          if (s.kind === "grade" && s.reference) {
            const target = await videoLook(sourceFile);
            Object.assign(s, gradeFromLooks(s.reference, target));
            delete s.reference;
          }
        }

        const calls = [];
        if (preset.category === "rhythm" && preset.rhythm) {
          const r = preset.rhythm;
          let cutTimes = [];
          if (r.useBeats) {
            const onsets = detectOnsets(await audioEnvelope(sourceFile));
            const n = r.everyNthBeat || 1;
            cutTimes = onsets.filter((_, i) => i % n === n - 1).map((o) => toComp(o.t));
          } else if (r.shotDurations?.length) {
            let t = mapping.inPoint ?? 0;
            for (let i = 0; ; i++) {
              t += r.shotDurations[i % r.shotDurations.length];
              if (!inLayer(t)) break;
              cutTimes.push(Math.round(t * 1000) / 1000);
            }
          }
          if (Array.isArray(at) || typeof at === "number") cutTimes = times;
          if (!cutTimes.length) throw new Error("The rhythm produced no cut points for this footage");
          const cutStep = r.jumpRemove ? { kind: "jump_cut", remove: r.jumpRemove } : { kind: "cut" };
          calls.push({ name: preset.name, times: cutTimes, steps: [cutStep, ...steps] });
          if (r.transition) {
            const tr = await lib.get(r.transition);
            calls.push({ name: tr.name, times: cutTimes, steps: tr.steps });
          }
        } else {
          if (!times.length) throw new Error("No edit points found. Pass 'at' with times in seconds.");
          calls.push({ name: preset.name, times, steps });
        }

        const results = [];
        for (const c of calls) {
          results.push(await bridge.send("applyRecipe", { comp, layer, durationScale, ...c }, opts));
        }
        return text(results.length === 1 ? results[0] : results);
      } catch (e) {
        return errorResult(e);
      }
    }
  );
}
