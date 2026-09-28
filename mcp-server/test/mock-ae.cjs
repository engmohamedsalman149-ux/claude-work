// Minimal in-memory model of the After Effects scripting DOM, enough to run ClaudeBridge.jsx
// handlers in Node. It models layers, timing, keyframes, effects and time remapping loosely.
const vm = require("node:vm");
const fs = require("node:fs");
const path = require("node:path");
const os = require("node:os");

const PT = { PROPERTY: 6212, INDEXED_GROUP: 6214, NAMED_GROUP: 6213 };
const PVT = { NO_VALUE: 6412, ThreeD_SPATIAL: 6413, ThreeD: 6414, TwoD_SPATIAL: 6415, TwoD: 6416, OneD: 6417, COLOR: 6418, CUSTOM_VALUE: 6419, MARKER: 6420, LAYER_INDEX: 6421, MASK_INDEX: 6422, SHAPE: 6423, TEXT_DOCUMENT: 6424 };
const KIT = { LINEAR: 6612, BEZIER: 6613, HOLD: 6614 };

const EFFECTS = {
  "ADBE Tile": ["Motion Tile", [["ADBE Tile-0004", "Output Width", 100], ["ADBE Tile-0005", "Output Height", 100], ["ADBE Tile-0006", "Mirror Edges", 0]]],
  "ADBE Geometry2": ["Transform", [["ADBE Geometry2-0002", "Position", [960, 540]], ["ADBE Geometry2-0011", "Uniform Scale", 1], ["ADBE Geometry2-0003", "Scale Height", 100], ["ADBE Geometry2-0007", "Rotation", 0], ["ADBE Geometry2-0008", "Opacity", 100], ["ADBE Geometry2-0009", "Use Composition's Shutter Angle", 1], ["ADBE Geometry2-0010", "Shutter Angle", 0]]],
  "ADBE Gaussian Blur 2": ["Gaussian Blur", [["ADBE Gaussian Blur 2-0001", "Blurriness", 0], ["ADBE Gaussian Blur 2-0003", "Repeat Edge Pixels", 0]]],
  "ADBE Brightness & Contrast 2": ["Brightness & Contrast", [["ADBE Brightness & Contrast 2-0001", "Brightness", 0], ["ADBE Brightness & Contrast 2-0002", "Contrast", 0], ["ADBE Brightness & Contrast 2-0003", "Use Legacy", 0]]],
  "ADBE Vibrance": ["Vibrance", [["ADBE Vibrance-0001", "Vibrance", 0], ["ADBE Vibrance-0002", "Saturation", 0]]],
  "ADBE Tint": ["Tint", [["ADBE Tint-0001", "Map Black To", [0, 0, 0, 1]], ["ADBE Tint-0002", "Map White To", [1, 1, 1, 1]], ["ADBE Tint-0003", "Amount to Tint", 100]]],
  "ADBE Glo2": ["Glow", [["ADBE Glo2-0002", "Glow Radius", 10], ["ADBE Glo2-0003", "Glow Intensity", 1]]],
};

function createAE() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "mock-ae-"));

  class Prop {
    constructor(parent, name, matchName, value, opts = {}) {
      Object.assign(this, { parentProperty: parent, name, matchName, value, isSpatial: !!opts.spatial, propertyType: PT.PROPERTY, keys: [], expression: "", canSetExpression: true, expressionEnabled: true, expressionError: "" });
      this.propertyValueType = opts.pvt || (Array.isArray(value) ? (value.length === 4 ? PVT.COLOR : PVT.TwoD) : PVT.OneD);
    }
    get propertyIndex() { return this.parentProperty.props.indexOf(this) + 1; }
    get numKeys() { return this.keys.length; }
    setValue(v) { if (this.keys.length) throw new Error("setValue on keyed property"); this.value = v; }
    setValueAtTime(t, v) {
      const k = this.keys.find((x) => Math.abs(x.t - t) < 1e-9);
      if (k) k.v = v; else { this.keys.push({ t, v, inI: KIT.BEZIER, outI: KIT.BEZIER }); this.keys.sort((a, b) => a.t - b.t); }
    }
    keyTime(i) { return this.keys[i - 1].t; }
    keyValue(i) { return this.keys[i - 1].v; }
    removeKey(i) { if (!this.keys[i - 1]) throw new Error("bad key " + i); this.keys.splice(i - 1, 1); }
    nearestKeyIndex(t) { let best = 1, d = Infinity; this.keys.forEach((k, i) => { if (Math.abs(k.t - t) < d) { d = Math.abs(k.t - t); best = i + 1; } }); return best; }
    valueAtTime(t) {
      const ks = this.keys;
      if (!ks.length) return this.value;
      if (t <= ks[0].t) return ks[0].v;
      if (t >= ks[ks.length - 1].t) return ks[ks.length - 1].v;
      for (let i = 0; i < ks.length - 1; i++) {
        const a = ks[i], b = ks[i + 1];
        if (t >= a.t && t <= b.t) {
          if (a.outI === KIT.HOLD) return a.v;
          const f = (t - a.t) / (b.t - a.t);
          return Array.isArray(a.v) ? a.v.map((x, j) => x + (b.v[j] - x) * f) : a.v + (b.v - a.v) * f;
        }
      }
    }
    setInterpolationTypeAtKey(i, a, b) { this.keys[i - 1].inI = a; this.keys[i - 1].outI = b ?? a; }
    keyInInterpolationType(i) { return this.keys[i - 1].inI; }
    keyInTemporalEase(i) { return this.keys[i - 1].easeIn || [new KeyframeEase(0, 16.7)]; }
    keyOutTemporalEase(i) { return this.keys[i - 1].easeOut || [new KeyframeEase(0, 16.7)]; }
    setTemporalEaseAtKey(i, a, b) {
      const dims = this.isSpatial || !Array.isArray(this.value) ? 1 : this.value.length;
      if (a.length !== dims || b.length !== dims) throw new Error(`ease needs ${dims} dims`);
      Object.assign(this.keys[i - 1], { easeIn: a, easeOut: b });
    }
  }

  class Group {
    constructor(parent, name, matchName, type = PT.NAMED_GROUP) { Object.assign(this, { parentProperty: parent, name, matchName, propertyType: type, props: [], enabled: true }); }
    get propertyIndex() { return this.parentProperty.props ? this.parentProperty.props.indexOf(this) + 1 : 1; }
    get numProperties() { return this.props.length; }
    property(k) { return typeof k === "number" ? this.props[k - 1] || null : this.props.find((p) => p.matchName === k || p.name === k) || null; }
    canAddProperty(mn) { return this.matchName === "ADBE Effect Parade" && !!EFFECTS[mn]; }
    addProperty(mn) {
      if (!this.canAddProperty(mn)) throw new Error("cannot add " + mn);
      const [display, params] = EFFECTS[mn];
      const count = this.props.filter((p) => p.matchName === mn).length;
      const g = new Group(this, count ? `${display} ${count + 1}` : display, mn);
      for (const [pm, pn, def] of params) g.props.push(new Prop(g, pn, pm, JSON.parse(JSON.stringify(def)), { spatial: pn === "Position" }));
      this.props.push(g);
      return g;
    }
  }

  class Item { constructor(name) { this.id = ++Item.nextId; this.name = name; this.parentFolder = null; } get typeName() { return this.constructor.name; } }
  Item.nextId = 0;
  class FootageItem extends Item {
    constructor(file, opts = {}) {
      super(path.basename(file.fsName));
      Object.assign(this, { file, width: 1920, height: 1080, pixelAspect: 1, frameRate: 30, duration: 10, hasVideo: true, mainSource: {} }, opts);
    }
  }
  class SolidSource {}
  class CompItem extends Item {
    constructor(name, w, h, pa, dur, fps) {
      super(name);
      Object.assign(this, { width: w, height: h, pixelAspect: pa, duration: dur, frameRate: fps, time: 0, bgColor: [0, 0, 0], workAreaStart: 0, workAreaDuration: dur, motionBlur: false, selectedLayers: [], _layers: [] });
      const comp = this;
      this.layers = {
        addSolid(color, name, w2, h2, pa2, dur2) {
          const src = new FootageItem({ fsName: "solid" }, { width: w2, height: h2, duration: dur2, mainSource: new SolidSource() });
          src.name = name; src.file = null;
          return comp._add(new AVLayer(comp, name, src, 0));
        },
        add(item) { return comp._add(new AVLayer(comp, item.name, item, comp.time)); },
        addShape() { return comp._add(new ShapeLayer(comp, "Shape Layer", null, 0)); },
      };
    }
    get frameDuration() { return 1 / this.frameRate; }
    get numLayers() { return this._layers.length; }
    layer(k) { return typeof k === "number" ? this._layers[k - 1] : this._layers.find((l) => l.name === k) || null; }
    _add(l, at = 0) { this._layers.splice(at, 0, l); return l; }
    openInViewer() {}
  }
  class FolderItem extends Item {}

  class AVLayer {
    constructor(comp, name, source, startTime) {
      this.containingComp = comp;
      Object.assign(this, { name, source, enabled: true, solo: false, locked: false, shy: false, label: 1, selected: false, comment: "", adjustmentLayer: false, nullLayer: false, threeDLayer: false, motionBlur: false, blendingMode: 1, parent: null, stretch: 100 });
      this._start = startTime;
      this.inPoint = startTime;
      this.outPoint = Math.min(comp.duration, startTime + (source ? source.duration : comp.duration));
      this.hasVideo = true;
      this.canSetTimeRemapEnabled = !!source && !(source.mainSource instanceof SolidSource);
      this._tre = false;
      this.root = new Group(null, name, "ADBE AV Layer");
      const tr = new Group(this.root, "Transform", "ADBE Transform Group");
      tr.props.push(new Prop(tr, "Anchor Point", "ADBE Anchor Point", [comp.width / 2, comp.height / 2], { spatial: true }));
      tr.props.push(new Prop(tr, "Position", "ADBE Position", [comp.width / 2, comp.height / 2], { spatial: true }));
      tr.props.push(new Prop(tr, "Scale", "ADBE Scale", [100, 100]));
      tr.props.push(new Prop(tr, "Rotation", "ADBE Rotate Z", 0));
      tr.props.push(new Prop(tr, "Opacity", "ADBE Opacity", 100));
      const fx = new Group(this.root, "Effects", "ADBE Effect Parade", PT.INDEXED_GROUP);
      this.root.props.push(tr, fx, new Prop(this.root, "Time Remap", "ADBE Time Remapping", 0));
    }
    get index() { return this.containingComp._layers.indexOf(this) + 1; }
    get startTime() { return this._start; }
    set startTime(v) { const d = v - this._start; this._start = v; this._in += d; this._out += d; }
    get timeRemapEnabled() { return this._tre; }
    set timeRemapEnabled(v) {
      if (v && !this._tre) {
        const tr = this.property("ADBE Time Remapping");
        tr.keys = [];
        tr.setValueAtTime(this._start, 0);
        tr.setValueAtTime(this._start + this.source.duration, this.source.duration);
      }
      this._tre = v;
    }
    set inPoint(v) { if (this.outPoint !== undefined && v >= this.outPoint) throw new Error("inPoint after outPoint"); if (!this._tre && this.source && v < this._start - 1e-9) throw new Error("inPoint before source start"); this._in = v; }
    get inPoint() { return this._in; }
    set outPoint(v) { if (this._in !== undefined && v <= this._in) throw new Error("outPoint before inPoint"); if (!this._tre && this.source && !(this.source.mainSource instanceof SolidSource) && v > this._start + this.source.duration + 1e-9) throw new Error("outPoint beyond source without time remap"); this._out = v; }
    get outPoint() { return this._out; }
    property(k) { return this.root.property(k); }
    get numProperties() { return this.root.numProperties; }
    splitLayer(t) {
      if (!(t > this.inPoint && t < this.outPoint)) throw new Error("split outside layer");
      const c = this.containingComp;
      const nl = new this.constructor(c, this.name, this.source, this._start);
      for (const k of ["comment", "adjustmentLayer", "label", "motionBlur", "_tre"]) nl[k] = this[k];
      const copy = (g, h) => g.props.forEach((p, i) => { if (p instanceof Prop) { h.props[i].value = JSON.parse(JSON.stringify(p.value)); h.props[i].keys = p.keys.map((k) => ({ ...k })); } });
      copy(this.property("ADBE Transform Group"), nl.property("ADBE Transform Group"));
      nl.property("ADBE Time Remapping").keys = this.property("ADBE Time Remapping").keys.map((k) => ({ ...k }));
      nl._in = t; nl._out = this._out;
      this._out = t;
      c._add(nl, this.index - 1);
      return nl;
    }
    moveBefore(l) { const c = this.containingComp; c._layers.splice(c._layers.indexOf(this), 1); c._layers.splice(c._layers.indexOf(l), 0, this); }
    moveToBeginning() { const c = this.containingComp; c._layers.splice(c._layers.indexOf(this), 1); c._layers.unshift(this); }
    remove() { const c = this.containingComp; c._layers.splice(c._layers.indexOf(this), 1); }
  }
  class TextLayer extends AVLayer {}
  class ShapeLayer extends AVLayer {}
  class CameraLayer {}
  class LightLayer {}

  class FsObj { constructor(p) { this.fsName = path.resolve(String(p)); this.name = path.basename(this.fsName); } get exists() { return fs.existsSync(this.fsName); } remove() { fs.rmSync(this.fsName, { force: true }); return true; } }
  class Folder extends FsObj { create() { fs.mkdirSync(this.fsName, { recursive: true }); return true; } getFiles() { return fs.readdirSync(this.fsName).filter((f) => f.endsWith(".json")).map((f) => new File(path.join(this.fsName, f))); } execute() {} }
  Folder.userData = { fsName: root };
  class File extends FsObj { open(m) { this.m = m; this.buf = ""; return true; } read() { return fs.readFileSync(this.fsName, "utf8"); } write(s) { this.buf += s; } close() { if (this.m === "w") fs.writeFileSync(this.fsName, this.buf); } rename(n) { fs.renameSync(this.fsName, path.join(path.dirname(this.fsName), n)); return true; } }
  class ImportOptions { constructor(f) { this.file = f; } }
  class KeyframeEase { constructor(s, i) { this.speed = s; this.influence = i; } }

  const items = [];
  const project = {
    file: null, dirty: false, bitsPerChannel: 8, renderQueue: { numItems: 0 },
    get numItems() { return items.length; },
    item: (i) => items[i - 1],
    activeItem: null,
    items: { addComp(name, w, h, pa, d, fps) { const c = new CompItem(name, w, h, pa, d, fps); items.push(c); project.activeItem = c; return c; } },
    importFile(io) { const it = new FootageItem(io.file, { duration: io.file.fsName.includes("short") ? 4 : 10 }); items.push(it); return it; },
  };
  const app = {
    version: "25.0", buildName: "mock", project,
    effects: Object.entries(EFFECTS).map(([matchName, [displayName]]) => ({ displayName, matchName, category: "mock" })),
    beginUndoGroup() {}, endUndoGroup() {}, scheduleTask: () => 1, cancelTask() {},
    preferences: { getPrefAsLong: () => 1 },
  };

  const ctx = {
    app, Folder, File, CompItem, AVLayer, TextLayer, ShapeLayer, CameraLayer, LightLayer, FootageItem, FolderItem, SolidSource,
    ImportOptions, KeyframeEase, PropertyType: PT, PropertyValueType: PVT, KeyframeInterpolationType: KIT,
    BlendingMode: { NORMAL: 1, ADD: 2, SCREEN: 3 }, Window: class {}, Panel: function Panel() {},
  };
  ctx.$ = { global: ctx };
  const w = { add: () => w, layout: { layout() {}, resize() {} }, removeAll() {}, preferredSize: [], text: "" };
  ctx.__panel = Object.assign(Object.create(ctx.Panel.prototype), w);
  vm.createContext(ctx);
  const src = fs.readFileSync(path.join(__dirname, "..", "..", "after-effects", "ClaudeBridge.jsx"), "utf8");
  vm.runInContext(src.replace(/\}\)\(this\);\s*$/, "})(__panel);"), ctx);
  return { app, H: ctx.ClaudeBridge.handlers, bridge: ctx.ClaudeBridge, root, File, KIT };
}

module.exports = { createAE };
