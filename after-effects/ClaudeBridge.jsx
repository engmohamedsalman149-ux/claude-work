/*
 * Claude Bridge for Adobe After Effects
 * -------------------------------------
 * A dockable ScriptUI panel that lets an external MCP server (and so Claude)
 * drive After Effects. The server drops JSON command files into a shared
 * folder; this panel polls the folder, runs each command inside an undo
 * group and writes a JSON result file back.
 *
 * Install: copy this file into
 *   Windows: C:\Program Files\Adobe\Adobe After Effects <ver>\Support Files\Scripts\ScriptUI Panels\
 *   macOS:   /Applications/Adobe After Effects <ver>/Scripts/ScriptUI Panels/
 * then enable Settings > Scripting & Expressions > "Allow Scripts to Write Files
 * and Access Network", restart AE and open Window > ClaudeBridge.jsx.
 *
 * ExtendScript is ES3: no JSON, Array.indexOf, forEach, Object.keys, trim...
 */

(function (thisObj) {
    var VERSION = "1.0.0";
    var POLL_MS = 200;
    var HEARTBEAT_MS = 2000;

    // ------------------------------------------------------------------
    // JSON (ES3 safe)
    // ------------------------------------------------------------------
    function quoteString(s) {
        var out = '"';
        for (var i = 0; i < s.length; i++) {
            var c = s.charAt(i);
            var code = s.charCodeAt(i);
            if (c === '"') out += '\\"';
            else if (c === "\\") out += "\\\\";
            else if (c === "\n") out += "\\n";
            else if (c === "\r") out += "\\r";
            else if (c === "\t") out += "\\t";
            else if (code < 32) {
                var hex = code.toString(16);
                while (hex.length < 4) hex = "0" + hex;
                out += "\\u" + hex;
            } else out += c;
        }
        return out + '"';
    }

    function stringify(v, depth) {
        depth = depth || 0;
        if (depth > 40) return '"[max depth]"';
        if (v === null || v === undefined) return "null";
        var t = typeof v;
        if (t === "number") return isFinite(v) ? String(v) : "null";
        if (t === "boolean") return v ? "true" : "false";
        if (t === "string") return quoteString(v);
        if (t === "function") return "null";
        var tag = Object.prototype.toString.call(v);
        if (tag === "[object Array]") {
            var parts = [];
            for (var i = 0; i < v.length; i++) parts.push(stringify(v[i], depth + 1));
            return "[" + parts.join(",") + "]";
        }
        if (tag === "[object Date]") return quoteString(v.toString());
        if (tag === "[object Object]") {
            var props = [];
            for (var k in v) {
                if (v.hasOwnProperty(k)) props.push(quoteString(k) + ":" + stringify(v[k], depth + 1));
            }
            return "{" + props.join(",") + "}";
        }
        // Host objects (Layer, Property, File...) are not serialisable.
        return quoteString(String(v));
    }

    function parse(text) {
        // Command files come from the local MCP server, which can already run
        // arbitrary script through runScript, so eval adds no new capability.
        return eval("(" + text + ")");
    }

    // ------------------------------------------------------------------
    // Files
    // ------------------------------------------------------------------
    function bridgeRoot() {
        return new Folder(Folder.userData.fsName + "/ae-claude-bridge");
    }

    function ensureFolder(f) {
        if (!f.exists) f.create();
        return f;
    }

    function readText(file) {
        file.encoding = "UTF-8";
        if (!file.open("r")) throw new Error("Cannot open " + file.fsName);
        var s = file.read();
        file.close();
        return s;
    }

    function writeTextAtomic(folder, name, text) {
        var tmp = new File(folder.fsName + "/" + name + ".tmp");
        tmp.encoding = "UTF-8";
        tmp.lineFeed = "Unix";
        if (!tmp.open("w")) throw new Error("Cannot write " + tmp.fsName + " (enable 'Allow Scripts to Write Files and Access Network')");
        tmp.write(text);
        tmp.close();
        var target = new File(folder.fsName + "/" + name);
        if (target.exists) target.remove();
        tmp.rename(name);
    }

    // ------------------------------------------------------------------
    // Helpers: lookups and conversions
    // ------------------------------------------------------------------
    function fail(msg) { throw new Error(msg); }

    function isArray(v) { return Object.prototype.toString.call(v) === "[object Array]"; }

    function hexToRgb(hex) {
        var h = hex.replace("#", "");
        if (h.length === 3) h = h.charAt(0) + h.charAt(0) + h.charAt(1) + h.charAt(1) + h.charAt(2) + h.charAt(2);
        if (h.length !== 6) fail("Bad hex colour: " + hex);
        return [parseInt(h.substr(0, 2), 16) / 255, parseInt(h.substr(2, 2), 16) / 255, parseInt(h.substr(4, 2), 16) / 255];
    }

    // Accepts "#rrggbb", [r,g,b] in 0..1, or [r,g,b] in 0..255.
    function toRgb(c) {
        if (c === undefined || c === null) return null;
        if (typeof c === "string") return hexToRgb(c);
        if (!isArray(c) || c.length < 3) fail("Colour must be a hex string or [r,g,b]");
        var big = c[0] > 1 || c[1] > 1 || c[2] > 1;
        return big ? [c[0] / 255, c[1] / 255, c[2] / 255] : [c[0], c[1], c[2]];
    }

    function toRgba(c) {
        var rgb = toRgb(c);
        return rgb ? [rgb[0], rgb[1], rgb[2], 1] : null;
    }

    function findItemById(id) {
        for (var i = 1; i <= app.project.numItems; i++) {
            if (app.project.item(i).id === id) return app.project.item(i);
        }
        return null;
    }

    function getComp(ref) {
        if (ref === undefined || ref === null || ref === "" || ref === "active") {
            var a = app.project.activeItem;
            if (a instanceof CompItem) return a;
            fail("No comp given and no active composition. Pass comp as a name or id.");
        }
        if (typeof ref === "number") {
            var byId = findItemById(ref);
            if (byId instanceof CompItem) return byId;
            fail("No composition with id " + ref);
        }
        for (var i = 1; i <= app.project.numItems; i++) {
            var it = app.project.item(i);
            if (it instanceof CompItem && it.name === ref) return it;
        }
        fail("No composition named '" + ref + "'");
    }

    function getLayer(comp, ref) {
        if (ref === undefined || ref === null) {
            if (comp.selectedLayers.length) return comp.selectedLayers[0];
            fail("No layer given and nothing selected in '" + comp.name + "'");
        }
        if (typeof ref === "number") {
            if (ref < 1 || ref > comp.numLayers) fail("Layer index " + ref + " out of range (1.." + comp.numLayers + ")");
            return comp.layer(ref);
        }
        var l = comp.layer(ref);
        if (!l) fail("No layer named '" + ref + "' in '" + comp.name + "'");
        return l;
    }

    // Friendly names -> match names, so paths work in any AE UI language.
    var ALIASES = {
        "transform": "ADBE Transform Group",
        "effects": "ADBE Effect Parade",
        "masks": "ADBE Mask Parade",
        "contents": "ADBE Root Vectors Group",
        "text": "ADBE Text Properties",
        "source text": "ADBE Text Document",
        "sourcetext": "ADBE Text Document",
        "anchor point": "ADBE Anchor Point",
        "anchorpoint": "ADBE Anchor Point",
        "position": "ADBE Position",
        "x position": "ADBE Position_0",
        "y position": "ADBE Position_1",
        "z position": "ADBE Position_2",
        "scale": "ADBE Scale",
        "rotation": "ADBE Rotate Z",
        "z rotation": "ADBE Rotate Z",
        "x rotation": "ADBE Rotate X",
        "y rotation": "ADBE Rotate Y",
        "orientation": "ADBE Orientation",
        "opacity": "ADBE Opacity",
        "audio levels": "ADBE Audio Levels",
        "time remap": "ADBE Time Remapping",
        "material options": "ADBE Material Options Group",
        "camera options": "ADBE Camera Options Group",
        "light options": "ADBE Light Options Group"
    };

    function childProp(group, seg) {
        var p = null;
        if (/^\d+$/.test(seg)) {
            p = group.property(parseInt(seg, 10));
        } else {
            var alias = ALIASES[seg.toLowerCase()];
            if (alias) { try { p = group.property(alias); } catch (e1) { p = null; } }
            if (!p) { try { p = group.property(seg); } catch (e2) { p = null; } }
        }
        return p;
    }

    // Path like "Transform/Position" or "Effects/Gaussian Blur/Blurriness".
    function resolveProp(layer, path) {
        if (!path) fail("Property path is required");
        var segs = isArray(path) ? path : String(path).split("/");
        var cur = layer;
        for (var i = 0; i < segs.length; i++) {
            if (segs[i] === "") continue;
            var next = childProp(cur, segs[i]);
            if (!next) fail("Property '" + segs[i] + "' not found under '" + cur.name + "'. Use ae_layer_properties to list paths.");
            cur = next;
        }
        return cur;
    }

    function textDocToObj(td) {
        var o = { text: td.text };
        try { o.fontSize = td.fontSize; } catch (e) {}
        try { o.font = td.font; } catch (e) {}
        try { o.fillColor = td.fillColor; } catch (e) {}
        try { o.applyFill = td.applyFill; } catch (e) {}
        try { o.applyStroke = td.applyStroke; } catch (e) {}
        try { if (td.applyStroke) { o.strokeColor = td.strokeColor; o.strokeWidth = td.strokeWidth; } } catch (e) {}
        try { o.tracking = td.tracking; } catch (e) {}
        try { o.leading = td.leading; } catch (e) {}
        try { o.justification = String(td.justification); } catch (e) {}
        return o;
    }

    var JUSTIFY = {
        left: "LEFT_JUSTIFY", center: "CENTER_JUSTIFY", right: "RIGHT_JUSTIFY",
        full: "FULL_JUSTIFY_LASTLINE_LEFT"
    };

    function applyTextDoc(td, o) {
        if (typeof o === "string") { td.text = o; return td; }
        if (o.text !== undefined) td.text = o.text;
        if (o.font !== undefined) td.font = o.font;
        if (o.fontSize !== undefined) td.fontSize = o.fontSize;
        if (o.fillColor !== undefined) { td.applyFill = true; td.fillColor = toRgb(o.fillColor); }
        if (o.strokeColor !== undefined) { td.applyStroke = true; td.strokeColor = toRgb(o.strokeColor); }
        if (o.strokeWidth !== undefined) td.strokeWidth = o.strokeWidth;
        if (o.strokeOverFill !== undefined) td.strokeOverFill = o.strokeOverFill;
        if (o.tracking !== undefined) td.tracking = o.tracking;
        if (o.leading !== undefined) { td.autoLeading = false; td.leading = o.leading; }
        if (o.fauxBold !== undefined) td.fauxBold = o.fauxBold;
        if (o.fauxItalic !== undefined) td.fauxItalic = o.fauxItalic;
        if (o.allCaps !== undefined) td.allCaps = o.allCaps;
        if (o.justification !== undefined) {
            var j = JUSTIFY[String(o.justification).toLowerCase()] || o.justification;
            td.justification = ParagraphJustification[j];
        }
        return td;
    }

    function serializeValue(prop, v) {
        if (v === undefined || v === null) return null;
        if (prop.propertyValueType === PropertyValueType.TEXT_DOCUMENT) return textDocToObj(v);
        if (prop.propertyValueType === PropertyValueType.SHAPE) {
            return { vertices: v.vertices, inTangents: v.inTangents, outTangents: v.outTangents, closed: v.closed };
        }
        if (prop.propertyValueType === PropertyValueType.MARKER) return { comment: v.comment, duration: v.duration };
        if (prop.propertyValueType === PropertyValueType.CUSTOM_VALUE || prop.propertyValueType === PropertyValueType.NO_VALUE) return null;
        return v;
    }

    function convertValue(prop, v) {
        var t = prop.propertyValueType;
        if (t === PropertyValueType.TEXT_DOCUMENT) {
            return applyTextDoc(prop.value, v);
        }
        if (t === PropertyValueType.COLOR) return toRgba(v);
        if (t === PropertyValueType.SHAPE) {
            var s = new Shape();
            s.vertices = v.vertices;
            if (v.inTangents) s.inTangents = v.inTangents;
            if (v.outTangents) s.outTangents = v.outTangents;
            s.closed = v.closed !== false;
            return s;
        }
        if (t === PropertyValueType.MARKER) {
            var m = new MarkerValue(typeof v === "string" ? v : (v.comment || ""));
            if (v.duration) m.duration = v.duration;
            return m;
        }
        return v;
    }

    function propInfo(prop, withValue) {
        var o = { name: prop.name, matchName: prop.matchName };
        if (prop.propertyType === PropertyType.PROPERTY) {
            o.kind = "property";
            if (withValue) { try { o.value = serializeValue(prop, prop.value); } catch (e) {} }
            if (prop.numKeys) o.numKeys = prop.numKeys;
            if (prop.canSetExpression && prop.expression) {
                o.expression = prop.expression;
                if (prop.expressionError) o.expressionError = prop.expressionError;
            }
        } else {
            o.kind = prop.propertyType === PropertyType.INDEXED_GROUP ? "indexedGroup" : "group";
            o.numProperties = prop.numProperties;
        }
        return o;
    }

    function propTree(group, depth, maxDepth) {
        var list = [];
        for (var i = 1; i <= group.numProperties; i++) {
            var p = group.property(i);
            if (!p) continue;
            var info = propInfo(p, true);
            info.index = i;
            if (p.propertyType !== PropertyType.PROPERTY && depth < maxDepth && p.numProperties > 0) {
                info.children = propTree(p, depth + 1, maxDepth);
            }
            // Skip hidden internal properties to keep output readable.
            if (p.propertyType === PropertyType.PROPERTY && p.propertyValueType === PropertyValueType.NO_VALUE) continue;
            list.push(info);
        }
        return list;
    }

    function layerType(l) {
        if (l instanceof TextLayer) return "text";
        if (l instanceof ShapeLayer) return "shape";
        if (l instanceof CameraLayer) return "camera";
        if (l instanceof LightLayer) return "light";
        if (l.nullLayer) return "null";
        if (l.adjustmentLayer) return "adjustment";
        if (l.source instanceof CompItem) return "precomp";
        try { if (l.source && l.source.mainSource instanceof SolidSource) return "solid"; } catch (e) {}
        return "footage";
    }

    function layerSummary(l) {
        var o = {
            index: l.index, name: l.name, type: layerType(l),
            enabled: l.enabled, solo: l.solo, locked: l.locked, shy: l.shy,
            inPoint: l.inPoint, outPoint: l.outPoint, startTime: l.startTime,
            parent: l.parent ? l.parent.index : null, label: l.label, selected: l.selected
        };
        if (l instanceof AVLayer) {
            o.threeD = l.threeDLayer;
            o.blendingMode = String(l.blendingMode);
            if (l.source) o.sourceId = l.source.id;
        }
        var tr = l.property("ADBE Transform Group");
        if (tr) {
            o.transform = {};
            for (var i = 1; i <= tr.numProperties; i++) {
                var p = tr.property(i);
                try { if (p.propertyValueType !== PropertyValueType.NO_VALUE) o.transform[p.name] = p.value; } catch (e) {}
            }
        }
        var fx = l.property("ADBE Effect Parade");
        if (fx && fx.numProperties) {
            o.effects = [];
            for (var e = 1; e <= fx.numProperties; e++) o.effects.push({ name: fx.property(e).name, matchName: fx.property(e).matchName, enabled: fx.property(e).enabled });
        }
        if (l instanceof TextLayer) {
            try { o.text = l.property("ADBE Text Properties").property("ADBE Text Document").value.text; } catch (e2) {}
        }
        return o;
    }

    function itemSummary(it) {
        var o = { id: it.id, name: it.name, type: it.typeName, parentFolder: it.parentFolder ? it.parentFolder.name : null };
        if (it instanceof CompItem) {
            o.type = "Composition";
            o.width = it.width; o.height = it.height; o.duration = it.duration;
            o.frameRate = it.frameRate; o.numLayers = it.numLayers; o.pixelAspect = it.pixelAspect;
        } else if (it instanceof FootageItem) {
            o.type = "Footage";
            try { o.file = it.file ? it.file.fsName : null; } catch (e) {}
            if (it.hasVideo) { o.width = it.width; o.height = it.height; o.duration = it.duration; }
        } else if (it instanceof FolderItem) {
            o.type = "Folder";
            o.numItems = it.numItems;
        }
        return o;
    }

    function compSummary(c) {
        return {
            id: c.id, name: c.name, width: c.width, height: c.height, pixelAspect: c.pixelAspect,
            duration: c.duration, frameRate: c.frameRate, time: c.time, bgColor: c.bgColor,
            workAreaStart: c.workAreaStart, workAreaDuration: c.workAreaDuration,
            motionBlur: c.motionBlur, numLayers: c.numLayers
        };
    }

    function setKeyEase(prop, k, key) {
        var inE = key.easeIn, outE = key.easeOut;
        if (key.ease === "easyEase" || key.ease === "easy") { inE = { speed: 0, influence: 33.333 }; outE = inE; }
        if (key.ease === "easeIn") { inE = { speed: 0, influence: 33.333 }; }
        if (key.ease === "easeOut") { outE = { speed: 0, influence: 33.333 }; }
        if (!inE && !outE) return;
        var dims = 1;
        if (!prop.isSpatial && isArray(prop.value)) dims = prop.value.length;
        var build = function (e, n) {
            var arr = [];
            for (var i = 0; i < n; i++) arr.push(new KeyframeEase(e.speed || 0, e.influence || 33.333));
            return arr;
        };
        var curIn = prop.keyInTemporalEase(k), curOut = prop.keyOutTemporalEase(k);
        try {
            prop.setTemporalEaseAtKey(k, inE ? build(inE, dims) : curIn, outE ? build(outE, dims) : curOut);
        } catch (err) {
            prop.setTemporalEaseAtKey(k, inE ? build(inE, 1) : curIn, outE ? build(outE, 1) : curOut);
        }
    }

    var INTERP = { linear: "LINEAR", bezier: "BEZIER", hold: "HOLD" };

    function applyLayerSettings(l, s, comp) {
        if (!s) return;
        if (s.name !== undefined) l.name = s.name;
        if (s.enabled !== undefined) l.enabled = s.enabled;
        if (s.solo !== undefined) l.solo = s.solo;
        if (s.shy !== undefined) l.shy = s.shy;
        if (s.label !== undefined) l.label = s.label;
        if (s.startTime !== undefined) l.startTime = s.startTime;
        if (s.inPoint !== undefined) l.inPoint = s.inPoint;
        if (s.outPoint !== undefined) l.outPoint = s.outPoint;
        if (s.stretch !== undefined) l.stretch = s.stretch;
        if (s.parent !== undefined) l.parent = s.parent === null ? null : getLayer(comp, s.parent);
        if (l instanceof AVLayer) {
            if (s.threeD !== undefined) l.threeDLayer = s.threeD;
            if (s.motionBlur !== undefined) l.motionBlur = s.motionBlur;
            if (s.adjustmentLayer !== undefined) l.adjustmentLayer = s.adjustmentLayer;
            if (s.collapseTransformation !== undefined) l.collapseTransformation = s.collapseTransformation;
            if (s.blendingMode !== undefined) l.blendingMode = BlendingMode[String(s.blendingMode).toUpperCase()];
            if (s.trackMatteLayer !== undefined && l.setTrackMatte) {
                l.setTrackMatte(getLayer(comp, s.trackMatteLayer), TrackMatteType[String(s.trackMatteType || "ALPHA").toUpperCase()]);
            }
        }
        if (s.locked !== undefined) l.locked = s.locked;
        var tr = l.property("ADBE Transform Group");
        var map = { position: "ADBE Position", anchorPoint: "ADBE Anchor Point", scale: "ADBE Scale", rotation: "ADBE Rotate Z", opacity: "ADBE Opacity", orientation: "ADBE Orientation", xRotation: "ADBE Rotate X", yRotation: "ADBE Rotate Y" };
        for (var k in map) {
            if (map.hasOwnProperty(k) && s[k] !== undefined) {
                var p = tr.property(map[k]);
                if (!p) continue;
                var v = s[k];
                // Allow 2D values on 3D-capable properties and vice versa.
                if (isArray(v) && isArray(p.value) && v.length < p.value.length) v = v.concat(p.value.slice(v.length));
                if (p.numKeys > 0) p.setValueAtTime(comp.time, v); else p.setValue(v);
            }
        }
    }

    function addShapeContent(layer, spec) {
        var contents = layer.property("ADBE Root Vectors Group");
        var grp = contents.addProperty("ADBE Vector Group");
        var gIndex = grp.propertyIndex;
        if (spec.name) grp.name = spec.name;
        var vectors = function () { return layer.property("ADBE Root Vectors Group").property(gIndex).property("ADBE Vectors Group"); };
        var type = (spec.shape || "rectangle").toLowerCase();
        var size = spec.size || [200, 200];
        if (!isArray(size)) size = [size, size];
        if (type === "rectangle" || type === "rect") {
            var r = vectors().addProperty("ADBE Vector Shape - Rect");
            r.property("ADBE Vector Rect Size").setValue(size);
            if (spec.roundness) r.property("ADBE Vector Rect Roundness").setValue(spec.roundness);
        } else if (type === "ellipse" || type === "circle") {
            var el = vectors().addProperty("ADBE Vector Shape - Ellipse");
            el.property("ADBE Vector Ellipse Size").setValue(size);
        } else if (type === "star" || type === "polygon") {
            var st = vectors().addProperty("ADBE Vector Shape - Star");
            st.property("ADBE Vector Star Type").setValue(type === "star" ? 1 : 2);
            st.property("ADBE Vector Star Points").setValue(spec.points || 5);
            st.property("ADBE Vector Star Outer Radius").setValue(spec.outerRadius || size[0] / 2);
            if (type === "star") st.property("ADBE Vector Star Inner Radius").setValue(spec.innerRadius || size[0] / 4);
            if (spec.roundness) st.property("ADBE Vector Star Outer Roundess").setValue(spec.roundness);
        } else if (type === "path") {
            var pa = vectors().addProperty("ADBE Vector Shape - Group");
            var sh = new Shape();
            sh.vertices = spec.vertices || [[0, 0], [100, 0], [100, 100]];
            if (spec.inTangents) sh.inTangents = spec.inTangents;
            if (spec.outTangents) sh.outTangents = spec.outTangents;
            sh.closed = spec.closed !== false;
            pa.property("ADBE Vector Shape").setValue(sh);
        } else {
            fail("Unknown shape '" + type + "'. Use rectangle, ellipse, star, polygon or path.");
        }
        if (spec.fill !== null) {
            var f = vectors().addProperty("ADBE Vector Graphic - Fill");
            f.property("ADBE Vector Fill Color").setValue(toRgba(spec.fill || [1, 1, 1]));
        }
        if (spec.stroke) {
            var s = vectors().addProperty("ADBE Vector Graphic - Stroke");
            s.property("ADBE Vector Stroke Color").setValue(toRgba(spec.stroke));
            s.property("ADBE Vector Stroke Width").setValue(spec.strokeWidth || 4);
        }
        if (spec.offset) {
            var gtr = layer.property("ADBE Root Vectors Group").property(gIndex).property("ADBE Vector Transform Group");
            gtr.property("ADBE Vector Position").setValue(spec.offset);
        }
        return gIndex;
    }

    // ------------------------------------------------------------------
    // Command handlers
    // ------------------------------------------------------------------
    var H = {};

    H.ping = function () {
        return { bridge: VERSION, aeVersion: app.version, buildName: app.buildName, project: app.project.file ? app.project.file.fsName : null };
    };

    H.projectInfo = function () {
        var p = app.project;
        var active = p.activeItem;
        return {
            name: p.file ? p.file.name : "Untitled Project",
            path: p.file ? p.file.fsName : null,
            dirty: p.dirty,
            numItems: p.numItems,
            bitsPerChannel: p.bitsPerChannel,
            activeItem: active ? itemSummary(active) : null,
            renderQueueItems: p.renderQueue.numItems,
            aeVersion: app.version
        };
    };

    H.listItems = function (a) {
        var out = [];
        for (var i = 1; i <= app.project.numItems; i++) {
            var s = itemSummary(app.project.item(i));
            if (!a.type || s.type.toLowerCase() === String(a.type).toLowerCase()) out.push(s);
        }
        return out;
    };

    H.getComp = function (a) {
        var c = getComp(a.comp);
        var o = compSummary(c);
        o.layers = [];
        for (var i = 1; i <= c.numLayers; i++) o.layers.push(layerSummary(c.layer(i)));
        return o;
    };

    H.createComp = function (a) {
        var c = app.project.items.addComp(
            a.name || "Comp " + (app.project.numItems + 1),
            a.width || 1920, a.height || 1080, a.pixelAspect || 1,
            a.duration || 10, a.frameRate || 30
        );
        if (a.bgColor) c.bgColor = toRgb(a.bgColor);
        if (a.open !== false) c.openInViewer();
        return compSummary(c);
    };

    H.setComp = function (a) {
        var c = getComp(a.comp);
        var s = a.settings || {};
        if (s.name !== undefined) c.name = s.name;
        if (s.width !== undefined) c.width = s.width;
        if (s.height !== undefined) c.height = s.height;
        if (s.duration !== undefined) c.duration = s.duration;
        if (s.frameRate !== undefined) c.frameRate = s.frameRate;
        if (s.pixelAspect !== undefined) c.pixelAspect = s.pixelAspect;
        if (s.bgColor !== undefined) c.bgColor = toRgb(s.bgColor);
        if (s.time !== undefined) c.time = s.time;
        if (s.workAreaStart !== undefined) c.workAreaStart = s.workAreaStart;
        if (s.workAreaDuration !== undefined) c.workAreaDuration = s.workAreaDuration;
        if (s.motionBlur !== undefined) c.motionBlur = s.motionBlur;
        if (s.open) c.openInViewer();
        return compSummary(c);
    };

    H.addLayer = function (a) {
        var c = getComp(a.comp);
        var type = (a.type || "solid").toLowerCase();
        var name = a.name;
        var l;
        if (type === "solid" || type === "adjustment") {
            var col = toRgb(a.color) || (type === "adjustment" ? [1, 1, 1] : [0.5, 0.5, 0.5]);
            l = c.layers.addSolid(col, name || (type === "adjustment" ? "Adjustment Layer" : "Solid"), a.width || c.width, a.height || c.height, c.pixelAspect, c.duration);
            if (type === "adjustment") l.adjustmentLayer = true;
        } else if (type === "text") {
            l = c.layers.addText(typeof a.text === "string" ? a.text : "Text");
            var src = l.property("ADBE Text Properties").property("ADBE Text Document");
            var td = src.value;
            applyTextDoc(td, {
                font: a.font, fontSize: a.fontSize, fillColor: a.fillColor, strokeColor: a.strokeColor,
                strokeWidth: a.strokeWidth, tracking: a.tracking, leading: a.leading,
                justification: a.justification || "center", fauxBold: a.fauxBold, allCaps: a.allCaps
            });
            src.setValue(td);
            if (name) l.name = name;
        } else if (type === "shape") {
            l = c.layers.addShape();
            if (name) l.name = name;
            if (a.shape) addShapeContent(l, a.shape);
        } else if (type === "null") {
            l = c.layers.addNull(c.duration);
            if (name) l.name = name;
        } else if (type === "camera") {
            l = c.layers.addCamera(name || "Camera", [c.width / 2, c.height / 2]);
        } else if (type === "light") {
            l = c.layers.addLight(name || "Light", [c.width / 2, c.height / 2]);
            if (a.lightType) l.lightType = LightType[String(a.lightType).toUpperCase()];
        } else if (type === "item" || type === "footage" || type === "precomp") {
            var it = typeof a.itemId === "number" ? findItemById(a.itemId) : null;
            if (!it) fail("addLayer type '" + type + "' needs a valid itemId (see ae_list_items)");
            l = c.layers.add(it);
            if (name) l.name = name;
        } else {
            fail("Unknown layer type '" + type + "'");
        }
        applyLayerSettings(l, a, c);
        return layerSummary(l);
    };

    H.addShape = function (a) {
        var c = getComp(a.comp);
        var l = a.layer !== undefined ? getLayer(c, a.layer) : c.layers.addShape();
        if (!(l instanceof ShapeLayer)) fail("Layer '" + l.name + "' is not a shape layer");
        if (a.name && a.layer === undefined) l.name = a.name;
        var groupIndex = addShapeContent(l, a);
        if (a.position && a.layer === undefined) l.property("ADBE Transform Group").property("ADBE Position").setValue(a.position);
        var o = layerSummary(l);
        o.groupIndex = groupIndex;
        return o;
    };

    H.modifyLayer = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        applyLayerSettings(l, a.settings || {}, c);
        return layerSummary(l);
    };

    H.layerAction = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var act = a.action;
        if (act === "delete") { var n = l.name; l.remove(); return { deleted: n }; }
        if (act === "duplicate") return layerSummary(l.duplicate());
        if (act === "moveToTop") l.moveToBeginning();
        else if (act === "moveToBottom") l.moveToEnd();
        else if (act === "moveBefore") l.moveBefore(getLayer(c, a.target));
        else if (act === "moveAfter") l.moveAfter(getLayer(c, a.target));
        else if (act === "select") l.selected = true;
        else if (act === "deselect") l.selected = false;
        else if (act === "split") return layerSummary(l.splitLayer(a.time !== undefined ? a.time : c.time));
        else if (act === "center") {
            var tr = l.property("ADBE Transform Group");
            tr.property("ADBE Position").setValue([c.width / 2, c.height / 2].concat(l.threeDLayer ? [0] : []));
        } else fail("Unknown action '" + act + "'");
        return layerSummary(l);
    };

    H.layerProperties = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var root = a.path ? resolveProp(l, a.path) : l;
        if (root.propertyType === PropertyType.PROPERTY) return H.getProperty(a);
        return { layer: l.name, path: a.path || "", properties: propTree(root, 1, a.depth || 3) };
    };

    H.getProperty = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var p = resolveProp(l, a.path);
        if (p.propertyType !== PropertyType.PROPERTY) fail("'" + a.path + "' is a group; use ae_layer_properties");
        var o = propInfo(p, true);
        if (a.time !== undefined) o.valueAtTime = serializeValue(p, p.valueAtTime(a.time, false));
        if (p.numKeys) {
            o.keyframes = [];
            for (var k = 1; k <= p.numKeys; k++) {
                o.keyframes.push({ time: p.keyTime(k), value: serializeValue(p, p.keyValue(k)) });
            }
        }
        return o;
    };

    H.setProperty = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var p = resolveProp(l, a.path);
        if (p.propertyType !== PropertyType.PROPERTY) fail("'" + a.path + "' is a group, not a property");
        var v = convertValue(p, a.value);
        if (a.time !== undefined) p.setValueAtTime(a.time, v);
        else if (p.numKeys > 0) p.setValueAtTime(c.time, v);
        else p.setValue(v);
        return propInfo(p, true);
    };

    H.setKeyframes = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var p = resolveProp(l, a.path);
        if (a.clear) { for (var r = p.numKeys; r >= 1; r--) p.removeKey(r); }
        var keys = a.keyframes || [];
        for (var i = 0; i < keys.length; i++) {
            var key = keys[i];
            if (key.ease === undefined && a.ease) key.ease = a.ease;
            p.setValueAtTime(key.time, convertValue(p, key.value));
            var k = p.nearestKeyIndex(key.time);
            var interp = key.interpolation || a.interpolation;
            if (interp && INTERP[interp]) {
                var it = KeyframeInterpolationType[INTERP[interp]];
                p.setInterpolationTypeAtKey(k, it, it);
            }
            setKeyEase(p, k, key);
        }
        var o = propInfo(p, false);
        o.numKeys = p.numKeys;
        return o;
    };

    H.setExpression = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var p = resolveProp(l, a.path);
        if (!p.canSetExpression) fail("Expressions are not allowed on '" + p.name + "'");
        p.expression = a.expression || "";
        if (a.enabled !== undefined) p.expressionEnabled = a.enabled;
        var o = propInfo(p, true);
        o.expressionError = p.expressionError || null;
        return o;
    };

    H.addEffect = function (a) {
        var c = getComp(a.comp);
        var l = getLayer(c, a.layer);
        var parade = l.property("ADBE Effect Parade");
        var eff = null;
        if (parade.canAddProperty(a.effect)) eff = parade.addProperty(a.effect);
        else {
            // Accept display names too ("Gaussian Blur").
            for (var i = 0; i < app.effects.length; i++) {
                if (app.effects[i].displayName.toLowerCase() === String(a.effect).toLowerCase()) {
                    eff = parade.addProperty(app.effects[i].matchName);
                    break;
                }
            }
        }
        if (!eff) fail("Effect '" + a.effect + "' not found. Use ae_list_effects.");
        var effIndex = eff.propertyIndex;
        if (a.name) eff.name = a.name;
        var props = a.properties || {};
        for (var k in props) {
            if (!props.hasOwnProperty(k)) continue;
            // Re-resolve every time: setting values can invalidate references.
            var e2 = l.property("ADBE Effect Parade").property(effIndex);
            var p = childProp(e2, k);
            if (!p) fail("Effect property '" + k + "' not found on " + e2.name);
            p.setValue(convertValue(p, props[k]));
        }
        var ef = l.property("ADBE Effect Parade").property(effIndex);
        return { layer: l.name, effect: ef.name, matchName: ef.matchName, index: effIndex, properties: propTree(ef, 1, 1) };
    };

    H.listEffects = function (a) {
        var f = a.filter ? String(a.filter).toLowerCase() : null;
        var out = [];
        for (var i = 0; i < app.effects.length; i++) {
            var e = app.effects[i];
            var hay = (e.displayName + " " + e.matchName + " " + e.category).toLowerCase();
            if (!f || hay.indexOf(f) !== -1) out.push({ displayName: e.displayName, matchName: e.matchName, category: e.category });
        }
        return out;
    };

    H.importFile = function (a) {
        var f = new File(a.path);
        if (!f.exists) fail("File not found: " + a.path);
        var io = new ImportOptions(f);
        if (a.sequence) io.sequence = true;
        if (a.importAs) io.importAs = ImportAsType[String(a.importAs).toUpperCase()];
        var item = app.project.importFile(io);
        var o = { item: itemSummary(item) };
        if (a.addToComp !== undefined && a.addToComp !== false) {
            var c = getComp(a.addToComp === true ? null : a.addToComp);
            o.layer = layerSummary(c.layers.add(item));
        }
        return o;
    };

    H.precompose = function (a) {
        var c = getComp(a.comp);
        var idx = [];
        var layers = a.layers || [];
        for (var i = 0; i < layers.length; i++) idx.push(getLayer(c, layers[i]).index);
        if (!idx.length) fail("layers is required");
        var nc = c.layers.precompose(idx, a.name || "Pre-comp", a.moveAllAttributes !== false);
        return compSummary(nc);
    };

    H.render = function (a) {
        var c = getComp(a.comp);
        var rq = app.project.renderQueue;
        var item = rq.items.add(c);
        if (a.renderSettingsTemplate) item.applyTemplate(a.renderSettingsTemplate);
        var om = item.outputModule(1);
        if (a.outputModuleTemplate) om.applyTemplate(a.outputModuleTemplate);
        if (a.outputPath) om.file = new File(a.outputPath);
        var o = { comp: c.name, output: om.file ? om.file.fsName : null, queued: true, templates: om.templates };
        if (a.useAME) { rq.queueInAME(true); o.sentToAME = true; }
        else if (a.render !== false) { rq.render(); o.rendered = true; }
        return o;
    };

    H.projectFile = function (a) {
        var act = a.action;
        if (act === "save") {
            if (a.path) app.project.save(new File(a.path));
            else if (app.project.file) app.project.save();
            else fail("Project has never been saved; pass path");
        } else if (act === "open") {
            app.open(new File(a.path));
        } else if (act === "new") {
            app.newProject();
        } else if (act === "close") {
            app.project.close(a.save ? CloseOptions.SAVE_CHANGES : CloseOptions.DO_NOT_SAVE_CHANGES);
        } else fail("Unknown project action '" + act + "'");
        return H.projectInfo({});
    };

    H.menuCommand = function (a) {
        var id = typeof a.id === "number" ? a.id : app.findMenuCommandId(a.name);
        if (!id) fail("Menu command '" + a.name + "' not found (names are in the AE UI language)");
        app.executeCommand(id);
        return { executed: id };
    };

    H.saveFrame = function (a) {
        var c = getComp(a.comp);
        var t = a.time !== undefined ? a.time : c.time;
        var f = new File(a.path);
        if (!c.saveFrameToPng) fail("saveFrameToPng is not available in this AE version");
        c.saveFrameToPng(t, f);
        return { path: f.fsName, time: t, width: c.width, height: c.height };
    };

    H.runScript = function (a) {
        var args = a.args || {}; // visible to the evaluated code
        var result = eval(a.code);
        return result === undefined ? null : result;
    };

    // Commands that change nothing skip the undo group.
    var READ_ONLY = { ping: 1, projectInfo: 1, listItems: 1, getComp: 1, layerProperties: 1, getProperty: 1, listEffects: 1, saveFrame: 1 };
    // Commands that manage the project or undo stack themselves.
    var NO_UNDO = { projectFile: 1, menuCommand: 1, render: 1 };

    function execute(cmd) {
        var fn = H[cmd.command];
        if (!fn) fail("Unknown command '" + cmd.command + "'");
        var undo = !READ_ONLY[cmd.command] && !NO_UNDO[cmd.command];
        if (undo) app.beginUndoGroup("Claude: " + (cmd.label || cmd.command));
        try {
            return fn(cmd.args || {});
        } finally {
            if (undo) app.endUndoGroup();
        }
    }

    // ------------------------------------------------------------------
    // Polling loop
    // ------------------------------------------------------------------
    var B = $.global.ClaudeBridge || {};
    $.global.ClaudeBridge = B;
    B.version = VERSION;
    B.handlers = H;
    B.busy = false;
    B.lastHeartbeat = 0;
    B.log = B.log || [];

    function dirs() {
        var root = ensureFolder(bridgeRoot());
        return { root: root, cmd: ensureFolder(new Folder(root.fsName + "/commands")), res: ensureFolder(new Folder(root.fsName + "/results")) };
    }

    function addLog(line) {
        var d = new Date();
        var ts = ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2);
        B.log.unshift(ts + "  " + line);
        if (B.log.length > 60) B.log.length = 60;
        if (B.ui && B.ui.logList) {
            try {
                B.ui.logList.removeAll();
                for (var i = 0; i < B.log.length; i++) B.ui.logList.add("item", B.log[i]);
            } catch (e) {}
        }
    }

    function heartbeat(d) {
        var now = new Date().getTime();
        if (now - B.lastHeartbeat < HEARTBEAT_MS) return;
        B.lastHeartbeat = now;
        try {
            writeTextAtomic(d.root, "heartbeat.json", stringify({ time: now, bridge: VERSION, aeVersion: app.version, pollMs: POLL_MS }));
        } catch (e) {}
    }

    B.poll = function () {
        if (B.busy) return;
        B.busy = true;
        try {
            var d = dirs();
            heartbeat(d);
            var files = d.cmd.getFiles("*.json");
            if (!files || !files.length) return;
            files.sort(function (x, y) { return x.name < y.name ? -1 : x.name > y.name ? 1 : 0; });
            for (var i = 0; i < files.length && i < 10; i++) {
                var f = files[i];
                var id = f.name.replace(/\.json$/, "");
                var out;
                var started = new Date().getTime();
                var cmd = null;
                try {
                    cmd = parse(readText(f));
                    f.remove();
                    out = { id: id, ok: true, result: execute(cmd) };
                } catch (err) {
                    try { f.remove(); } catch (e3) {}
                    out = { id: id, ok: false, error: String(err.message || err), line: err.line || null };
                }
                out.ms = new Date().getTime() - started;
                var text;
                try { text = stringify(out); } catch (se) { text = stringify({ id: id, ok: false, error: "Could not serialise result: " + se }); }
                writeTextAtomic(d.res, id + ".json", text);
                addLog((out.ok ? "OK   " : "ERR  ") + (cmd ? cmd.command : "?") + (out.ok ? "" : " - " + out.error));
            }
        } catch (e) {
            addLog("Bridge error: " + e);
        } finally {
            B.busy = false;
        }
    };

    B.start = function () {
        if (B.taskId) return;
        B.taskId = app.scheduleTask("$.global.ClaudeBridge.poll()", POLL_MS, true);
        B.lastHeartbeat = 0;
        addLog("Listening on " + bridgeRoot().fsName);
        if (B.ui) B.ui.status.text = "Status: running";
    };

    B.stop = function () {
        if (B.taskId) { app.cancelTask(B.taskId); B.taskId = null; }
        try { var hb = new File(bridgeRoot().fsName + "/heartbeat.json"); if (hb.exists) hb.remove(); } catch (e) {}
        addLog("Stopped");
        if (B.ui) B.ui.status.text = "Status: stopped";
    };

    // ------------------------------------------------------------------
    // UI
    // ------------------------------------------------------------------
    function buildUI(host) {
        var w = host instanceof Panel ? host : new Window("palette", "Claude Bridge", undefined, { resizeable: true });
        w.orientation = "column";
        w.alignChildren = ["fill", "top"];
        w.spacing = 6;
        w.margins = 8;

        var title = w.add("statictext", undefined, "Claude Bridge v" + VERSION);
        var status = w.add("statictext", undefined, "Status: stopped");
        status.characters = 30;
        var pathTxt = w.add("edittext", undefined, bridgeRoot().fsName, { readonly: true });

        var row = w.add("group");
        row.alignChildren = ["fill", "center"];
        var startBtn = row.add("button", undefined, "Start");
        var stopBtn = row.add("button", undefined, "Stop");
        var openBtn = row.add("button", undefined, "Open Folder");

        var logList = w.add("listbox", undefined, [], { multiselect: false });
        logList.preferredSize = [320, 180];
        logList.alignment = ["fill", "fill"];

        startBtn.onClick = function () { B.start(); };
        stopBtn.onClick = function () { B.stop(); };
        openBtn.onClick = function () { dirs().root.execute(); };

        B.ui = { window: w, status: status, logList: logList, title: title, path: pathTxt };

        w.onResizing = w.onResize = function () { this.layout.resize(); };
        if (w instanceof Window) { w.center(); w.show(); } else w.layout.layout(true);

        try {
            if (!app.preferences.getPrefAsLong("Main Pref Section", "Pref_SCRIPTING_FILE_NETWORK_SECURITY")) {
                addLog("Enable: Settings > Scripting & Expressions > Allow Scripts to Write Files and Access Network");
            }
        } catch (e) {}
        B.start();
    }

    buildUI(thisObj);
})(this);
