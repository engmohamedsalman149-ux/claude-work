#!/usr/bin/env node
// MCP server exposing Adobe After Effects to Claude through the ClaudeBridge.jsx panel.
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { Bridge } from "./bridge.js";

const bridge = new Bridge();
const server = new McpServer({ name: "after-effects", version: "1.0.0" });

const compRef = z
  .union([z.string(), z.number()])
  .optional()
  .describe("Composition name or item id. Omit to use the active composition.");
const layerRef = z
  .union([z.string(), z.number()])
  .optional()
  .describe("Layer name or 1-based index. Omit to use the first selected layer.");
const propPath = z
  .string()
  .describe(
    "Property path separated by '/', using display names or match names, e.g. 'Transform/Position', " +
      "'Effects/Gaussian Blur/Blurriness', 'Text/Source Text', 'Contents/Group 1/Contents/Fill 1/Color'. " +
      "Use ae_layer_properties to discover paths."
  );
const color = z
  .union([z.string(), z.array(z.number())])
  .describe("Colour as '#rrggbb' or [r,g,b] (0-1 or 0-255)");
const timeoutSec = z.number().optional().describe("How long to wait for After Effects (default 60s)");

const text = (data) => ({
  content: [{ type: "text", text: typeof data === "string" ? data : JSON.stringify(data, null, 2) }],
});

function tool(name, description, schema, command, { mapArgs = (a) => a, timeout } = {}) {
  server.registerTool(name, { description, inputSchema: schema }, async (args) => {
    try {
      const { timeoutSec: t, ...rest } = args;
      const ms = (t ?? timeout ?? 60) * 1000;
      return text(await bridge.send(command, mapArgs(rest), { timeoutMs: ms }));
    } catch (e) {
      return { ...text(`Error: ${e.message}`), isError: true };
    }
  });
}

// ---------------------------------------------------------------- status

server.registerTool(
  "ae_status",
  {
    description:
      "Check whether After Effects is connected (the Claude Bridge panel must be open and running). Call this first.",
    inputSchema: {},
  },
  async () => {
    const hb = await bridge.heartbeat();
    if (!hb || hb.ageMs > 10_000) {
      return text({
        connected: false,
        bridgeDir: bridge.dir,
        help:
          "Open After Effects, then Window > ClaudeBridge.jsx and press Start. Make sure " +
          "Settings > Scripting & Expressions > 'Allow Scripts to Write Files and Access Network' is on.",
      });
    }
    try {
      const info = await bridge.send("ping", {}, { timeoutMs: 10_000 });
      return text({ connected: true, bridgeDir: bridge.dir, ...info });
    } catch (e) {
      return text({ connected: false, bridgeDir: bridge.dir, error: e.message });
    }
  }
);

// ---------------------------------------------------------------- scripting

tool(
  "ae_run_script",
  "Run arbitrary ExtendScript (ES3 JavaScript) inside After Effects and return the value of the last expression. " +
    "This gives full access to the AE scripting API (app, app.project, CompItem, Layer, Property...). " +
    "The code runs inside an undo group. `args` holds the optional args object. " +
    "ExtendScript has no JSON, Array.forEach/map/indexOf or Object.keys; return plain objects/arrays and they are serialised for you.",
  {
    code: z.string().describe("ExtendScript source. The last expression is returned."),
    args: z.record(z.any()).optional().describe("Values made available to the script as `args`"),
    timeoutSec,
  },
  "runScript"
);

// ---------------------------------------------------------------- project

tool("ae_project_info", "Get info about the open project: name, path, item count, active item.", {}, "projectInfo");

tool(
  "ae_list_items",
  "List project panel items (compositions, footage, folders) with their ids.",
  { type: z.enum(["Composition", "Footage", "Folder"]).optional().describe("Only return this item type") },
  "listItems"
);

tool(
  "ae_project_file",
  "Save, save as, open, create or close a project.",
  {
    action: z.enum(["save", "open", "new", "close"]),
    path: z.string().optional().describe("Path to .aep for open or save-as"),
    save: z.boolean().optional().describe("For close: save changes first"),
    timeoutSec,
  },
  "projectFile"
);

tool(
  "ae_import_file",
  "Import a file (video, image, audio, .ai, .psd, image sequence...) into the project, optionally adding it to a comp.",
  {
    path: z.string().describe("Absolute path on the machine running After Effects"),
    sequence: z.boolean().optional().describe("Import as image sequence"),
    importAs: z.enum(["FOOTAGE", "COMP", "COMP_CROPPED_LAYERS", "PROJECT"]).optional(),
    addToComp: z
      .union([z.boolean(), z.string(), z.number()])
      .optional()
      .describe("true = add to active comp, or a comp name/id"),
    timeoutSec,
  },
  "importFile"
);

// ---------------------------------------------------------------- compositions

tool(
  "ae_get_comp",
  "Get a composition's settings and every layer with type, timing, parent, transform values and effects.",
  { comp: compRef },
  "getComp"
);

tool(
  "ae_create_comp",
  "Create a new composition and open it in the viewer.",
  {
    name: z.string().optional(),
    width: z.number().int().optional().describe("Default 1920"),
    height: z.number().int().optional().describe("Default 1080"),
    duration: z.number().optional().describe("Seconds, default 10"),
    frameRate: z.number().optional().describe("Default 30"),
    pixelAspect: z.number().optional(),
    bgColor: color.optional(),
    open: z.boolean().optional(),
  },
  "createComp"
);

tool(
  "ae_set_comp",
  "Change composition settings (name, size, duration, frame rate, background, current time, work area, motion blur).",
  {
    comp: compRef,
    settings: z
      .object({
        name: z.string(),
        width: z.number().int(),
        height: z.number().int(),
        duration: z.number(),
        frameRate: z.number(),
        pixelAspect: z.number(),
        bgColor: color,
        time: z.number().describe("Move the playhead (seconds)"),
        workAreaStart: z.number(),
        workAreaDuration: z.number(),
        motionBlur: z.boolean(),
        open: z.boolean().describe("Open in viewer"),
      })
      .partial(),
  },
  "setComp"
);

tool(
  "ae_precompose",
  "Pre-compose layers into a new composition.",
  {
    comp: compRef,
    layers: z.array(z.union([z.string(), z.number()])).describe("Layer names or indices"),
    name: z.string().optional(),
    moveAllAttributes: z.boolean().optional(),
  },
  "precompose"
);

// ---------------------------------------------------------------- layers

const layerSettings = {
  name: z.string(),
  enabled: z.boolean(),
  solo: z.boolean(),
  locked: z.boolean(),
  shy: z.boolean(),
  label: z.number().int().min(0).max(16),
  startTime: z.number(),
  inPoint: z.number(),
  outPoint: z.number(),
  stretch: z.number(),
  parent: z.union([z.string(), z.number(), z.null()]).describe("Parent layer name/index, or null to unparent"),
  threeD: z.boolean(),
  motionBlur: z.boolean(),
  adjustmentLayer: z.boolean(),
  collapseTransformation: z.boolean(),
  blendingMode: z.string().describe("e.g. NORMAL, ADD, SCREEN, MULTIPLY, OVERLAY"),
  trackMatteLayer: z.union([z.string(), z.number()]),
  trackMatteType: z.enum(["ALPHA", "ALPHA_INVERTED", "LUMA", "LUMA_INVERTED"]),
  position: z.array(z.number()),
  anchorPoint: z.array(z.number()),
  scale: z.array(z.number()).describe("Percent, e.g. [100,100]"),
  rotation: z.number(),
  opacity: z.number().describe("0-100"),
  orientation: z.array(z.number()),
  xRotation: z.number(),
  yRotation: z.number(),
};

const shapeSpec = {
  shape: z.enum(["rectangle", "ellipse", "circle", "star", "polygon", "path"]).optional(),
  size: z.union([z.number(), z.array(z.number())]).optional().describe("[w,h] for rectangle/ellipse"),
  roundness: z.number().optional(),
  points: z.number().optional().describe("Star/polygon points"),
  outerRadius: z.number().optional(),
  innerRadius: z.number().optional(),
  vertices: z.array(z.array(z.number())).optional().describe("For 'path'"),
  inTangents: z.array(z.array(z.number())).optional(),
  outTangents: z.array(z.array(z.number())).optional(),
  closed: z.boolean().optional(),
  fill: color.nullable().optional().describe("Fill colour, null for no fill"),
  stroke: color.optional(),
  strokeWidth: z.number().optional(),
  offset: z.array(z.number()).optional().describe("Position of the shape group inside the layer"),
};

tool(
  "ae_add_layer",
  "Add a layer: solid, text, shape, null, camera, light, adjustment, or an existing project item (footage/precomp). " +
    "Any layer setting (position, scale, opacity, parent, threeD, blendingMode...) can be passed too.",
  {
    comp: compRef,
    type: z.enum(["solid", "text", "shape", "null", "camera", "light", "adjustment", "item"]),
    name: z.string().optional(),
    color: color.optional().describe("Solid colour"),
    width: z.number().optional(),
    height: z.number().optional(),
    text: z.string().optional().describe("Text layer content (Arabic and other scripts supported)"),
    font: z.string().optional().describe("PostScript font name, e.g. 'Arial-BoldMT'"),
    fontSize: z.number().optional(),
    fillColor: color.optional(),
    strokeColor: color.optional(),
    strokeWidth: z.number().optional(),
    tracking: z.number().optional(),
    leading: z.number().optional(),
    justification: z.enum(["left", "center", "right", "full"]).optional(),
    fauxBold: z.boolean().optional(),
    allCaps: z.boolean().optional(),
    lightType: z.enum(["PARALLEL", "SPOT", "POINT", "AMBIENT"]).optional(),
    itemId: z.number().optional().describe("Project item id for type 'item'"),
    shape: z.object(shapeSpec).optional().describe("Initial shape for type 'shape'"),
    ...Object.fromEntries(Object.entries(layerSettings).map(([k, v]) => [k, v.optional()]).filter(([k]) => k !== "name")),
  },
  "addLayer"
);

tool(
  "ae_add_shape",
  "Add a vector shape (rectangle, ellipse, star, polygon or custom path) with fill/stroke. " +
    "Creates a new shape layer, or adds a group to an existing shape layer when `layer` is given.",
  {
    comp: compRef,
    layer: layerRef.describe("Existing shape layer to add to; omit to create a new layer"),
    name: z.string().optional(),
    position: z.array(z.number()).optional().describe("Layer position for a new layer"),
    ...shapeSpec,
  },
  "addShape"
);

tool(
  "ae_modify_layer",
  "Change layer settings: name, timing, parent, 3D, blending mode, track matte, switches and transform values.",
  { comp: compRef, layer: layerRef, settings: z.object(layerSettings).partial() },
  "modifyLayer"
);

tool(
  "ae_layer_action",
  "Delete, duplicate, reorder, select, split or center a layer.",
  {
    comp: compRef,
    layer: layerRef,
    action: z.enum(["delete", "duplicate", "moveToTop", "moveToBottom", "moveBefore", "moveAfter", "select", "deselect", "split", "center"]),
    target: z.union([z.string(), z.number()]).optional().describe("Other layer for moveBefore/moveAfter"),
    time: z.number().optional().describe("Split time in seconds"),
  },
  "layerAction"
);

// ---------------------------------------------------------------- properties & animation

tool(
  "ae_layer_properties",
  "List a layer's property tree (names, match names, values, keyframe counts, expressions) to discover property paths.",
  {
    comp: compRef,
    layer: layerRef,
    path: z.string().optional().describe("Start from this group, e.g. 'Effects' or 'Transform'"),
    depth: z.number().int().optional().describe("How deep to recurse (default 3)"),
  },
  "layerProperties"
);

tool(
  "ae_get_property",
  "Read one property's value, keyframes and expression.",
  { comp: compRef, layer: layerRef, path: propPath, time: z.number().optional() },
  "getProperty"
);

tool(
  "ae_set_property",
  "Set any property value (transform, effect parameter, text, shape colour...). " +
    "If `time` is given (or the property already has keyframes) a keyframe is set at that time. " +
    "For 'Text/Source Text' pass a string or {text, font, fontSize, fillColor, strokeColor, strokeWidth, tracking, justification}.",
  { comp: compRef, layer: layerRef, path: propPath, value: z.any(), time: z.number().optional() },
  "setProperty"
);

tool(
  "ae_set_keyframes",
  "Animate a property with keyframes, including easing and interpolation.",
  {
    comp: compRef,
    layer: layerRef,
    path: propPath,
    keyframes: z
      .array(
        z.object({
          time: z.number().describe("Seconds"),
          value: z.any(),
          ease: z.enum(["easyEase", "easeIn", "easeOut"]).optional(),
          easeIn: z.object({ speed: z.number(), influence: z.number() }).optional(),
          easeOut: z.object({ speed: z.number(), influence: z.number() }).optional(),
          interpolation: z.enum(["linear", "bezier", "hold"]).optional(),
        })
      )
      .min(1),
    ease: z.enum(["easyEase", "easeIn", "easeOut"]).optional().describe("Default ease for every keyframe"),
    interpolation: z.enum(["linear", "bezier", "hold"]).optional(),
    clear: z.boolean().optional().describe("Remove existing keyframes first"),
  },
  "setKeyframes"
);

tool(
  "ae_set_expression",
  "Set (or clear with an empty string) an expression on a property. Returns any expression error.",
  { comp: compRef, layer: layerRef, path: propPath, expression: z.string(), enabled: z.boolean().optional() },
  "setExpression"
);

// ---------------------------------------------------------------- effects

tool(
  "ae_add_effect",
  "Apply an effect to a layer by match name ('ADBE Gaussian Blur 2') or display name ('Gaussian Blur'), optionally setting its parameters.",
  {
    comp: compRef,
    layer: layerRef,
    effect: z.string(),
    name: z.string().optional().describe("Rename the effect instance"),
    properties: z.record(z.any()).optional().describe("Parameter name -> value, e.g. {\"Blurriness\": 20}"),
  },
  "addEffect"
);

tool(
  "ae_list_effects",
  "List installed effects (display name, match name, category), optionally filtered by a search string.",
  { filter: z.string().optional() },
  "listEffects"
);

// ---------------------------------------------------------------- misc

tool(
  "ae_menu_command",
  "Run an After Effects menu command by name (in the AE UI language, e.g. 'Undo', 'Redo', 'Save') or by numeric id.",
  { name: z.string().optional(), id: z.number().int().optional() },
  "menuCommand"
);

tool(
  "ae_render",
  "Add a composition to the render queue and render it (or send it to Adobe Media Encoder).",
  {
    comp: compRef,
    outputPath: z.string().optional().describe("Output file path, e.g. C:/renders/out.mp4"),
    renderSettingsTemplate: z.string().optional().describe("e.g. 'Best Settings'"),
    outputModuleTemplate: z.string().optional().describe("e.g. 'H.264 - Match Render Settings - 15 Mbps'"),
    render: z.boolean().optional().describe("false = only queue it"),
    useAME: z.boolean().optional().describe("Queue in Adobe Media Encoder instead"),
    timeoutSec: z.number().optional().describe("Default 1800s"),
  },
  "render",
  { timeout: 1800 }
);

server.registerTool(
  "ae_preview_frame",
  {
    description:
      "Render one frame of a composition to PNG and return it as an image so you can see the result of your changes.",
    inputSchema: { comp: compRef, time: z.number().optional().describe("Seconds; default current time") },
  },
  async ({ comp, time }) => {
    const file = path.join(os.tmpdir(), `ae-claude-frame-${Date.now()}.png`);
    try {
      const info = await bridge.send("saveFrame", { comp, time, path: file }, { timeoutMs: 60_000 });
      // saveFrameToPng may finish writing asynchronously.
      let data;
      for (let i = 0; i < 100 && !data; i++) {
        try {
          const buf = await fs.readFile(info.path || file);
          if (buf.length > 0) data = buf;
        } catch {}
        if (!data) await new Promise((r) => setTimeout(r, 200));
      }
      if (!data) throw new Error("Frame was not written by After Effects");
      await fs.rm(info.path || file, { force: true });
      return {
        content: [
          { type: "image", data: data.toString("base64"), mimeType: "image/png" },
          { type: "text", text: JSON.stringify(info) },
        ],
      };
    } catch (e) {
      return { ...text(`Error: ${e.message}`), isError: true };
    }
  }
);

await server.connect(new StdioServerTransport());
