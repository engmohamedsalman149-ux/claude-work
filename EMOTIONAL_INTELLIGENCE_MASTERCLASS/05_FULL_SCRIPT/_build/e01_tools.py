"""E01 tools: runtime estimate, TIME-field fill, teleprompter export, spoken-text QA.

Usage: python3 e01_tools.py
Reads/updates  ../E01/01_E01_FINAL_SCRIPT.md  (only the **TIME:** lines and the runtime row)
Writes         ../E01/11_E01_TELEPROMPTER.txt  and  e01_runtime.json
"""
import json, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
EP = HERE.parent / "E01"
SCRIPT = EP / "01_E01_FINAL_SCRIPT.md"

WPM = 130            # Egyptian conversational explanatory pace (assumption; recalibrate after table read)
SHORT_PAUSE = 0.5    # ‖  (extra beyond natural phrasing already inside the WPM rate)
LONG_PAUSE = 2.0     # ‖‖

# Spoken-text QA: phrases that must never be spoken (00_SCRIPT_BIBLE §7, 06_ACCURACY_GUARDRAILS)
BANNED = [
    "الذكاء العاطفي هو", "كل المشكلة في دماغك", "محدش يقدر يزعلك", "أنت لازم", "انت لازم",
    "الحل إنك تتجاهل", "تقدر تتحكم فيه", "كل شخص غاضب", "فهو متلاعب", "نرجسي", "سيكوباتي",
    "سوسيوباتي", "Dark EQ", "الذكاء العاطفي المظلم", "12 ملّي", "98,000", "فكّر إيجابي وخلاص",
    "مشاعرك كلها من أفكارك", "لازم تسامح",
]


def fmt(sec):
    sec = int(round(sec))
    return f"{sec // 60:02d}:{sec % 60:02d}"


def line_cost(l):
    """Seconds for one blockquote line: speech + pauses, or a hold/visual-only token."""
    m = re.match(r"^(⏳|🎬)(\d+)$", l)
    if m:
        return float(m.group(2)), 0, 0, 0
    long_p = l.count("‖‖")
    short_p = l.count("‖") - 2 * long_p
    clean = re.sub(r"[‖*«»…:؟?!،,.\"]", " ", l)
    words = [w for w in clean.split() if re.search(r"[\w\u0600-\u06FF]", w)]
    return len(words) / (WPM / 60) + short_p * SHORT_PAUSE + long_p * LONG_PAUSE, len(words), short_p, long_p


def parse(text):
    scenes = []
    for b in re.split(r"^### ", text, flags=re.M)[1:]:
        sid = b.split(" ", 1)[0]
        field = re.search(r"\*\*SILENT:\*\*\s*(\d+)ث", b)
        m = re.search(r"\*\*SPOKEN SCRIPT:\*\*\n((?:>.*\n?)+)", b)
        lines = [l[1:].strip() for l in m.group(1).splitlines()] if m else []
        rows, words, sp, lp = [], 0, 0, 0
        for l in lines:
            c, w, s, lg = line_cost(l)
            rows.append([l, round(c, 1)])
            words, sp, lp = words + w, sp + s, lp + lg
        holds = sum(int(x) for l in lines for x in re.findall(r"^⏳(\d+)$", l))
        silent = sum(int(x) for l in lines for x in re.findall(r"^🎬(\d+)$", l))
        if field and int(field.group(1)) != silent:
            raise SystemExit(f"{sid}: SILENT field {field.group(1)} != 🎬 total {silent}")
        spoken = [l for l in lines if not re.match(r"^(⏳|🎬)", l)]
        scenes.append(dict(id=sid, words=words, short_pauses=sp, long_pauses=lp, holds_s=holds,
                           silent_s=silent, dur_s=round(sum(r[1] for r in rows), 1),
                           spoken=spoken, lines=lines, rows=rows))
    return scenes


def cross_checks(scenes):
    """Consistency between the E01 package files and the Phase 5 outline."""
    root = HERE.parent.parent
    outline = (root / "04_MASTER_OUTLINE" / "E01_OUTLINE.md").read_text(encoding="utf-8")
    want = re.findall(r"^### (E1-\d+) ", outline, flags=re.M)
    have = [s["id"] for s in scenes]
    slides = (EP / "04_E01_SLIDE_BY_SLIDE.md").read_text(encoding="utf-8")
    sids = [int(x) for x in re.findall(r"^### S(\d+) ", slides, flags=re.M)]
    ost = (EP / "06_E01_ON_SCREEN_TEXT.md").read_text(encoding="utf-8")
    tids = re.findall(r"^\| (T\d+) \|", ost, flags=re.M)
    spoken = " ".join(" ".join(s["spoken"]) for s in scenes)
    tl = (EP / "09_E01_PRODUCTION_TIMELINE.md").read_text(encoding="utf-8")
    tl_rows = re.findall(r"^\| (\d+) \| (\d\d:\d\d)–(\d\d:\d\d) \|", tl, flags=re.M)
    gaps = [r[0] for a, r in zip(tl_rows, tl_rows[1:]) if a[2] != r[1]]
    checks = {
        "scene_ids_match_phase5": have == want,
        "slides_contiguous_S01_to_Sn": sids == list(range(1, len(sids) + 1)),
        "slide_count": len(sids),
        "onscreen_text_count": len(tids),
        "film_obs_F07_F18_in_spoken": re.findall(r"F(0[7-9]|1[0-8])", spoken),
        "timeline_segments": len(tl_rows),
        "timeline_gaps_or_overlaps": gaps,
        "timeline_end": tl_rows[-1][2] if tl_rows else None,
    }
    return checks


def main():
    text = SCRIPT.read_text(encoding="utf-8")
    scenes = parse(text)
    t = 0.0
    for s in scenes:
        s["start"], s["end"] = t, t + s["dur_s"]
        c = t
        for r in s["rows"]:
            r.insert(0, fmt(c))
            c += r[2]
        t = s["end"]
        text = re.sub(rf"(### {re.escape(s['id'])} [^\n]*\n\*\*TIME:\*\*) [^\n]*",
                      lambda m: f"{m.group(1)} {fmt(s['start'])}–{fmt(s['end'])} (~{s['dur_s'] / 60:.1f}د)", text)
    text = re.sub(r"(\| المدة المقدّرة \| )[^|]*\|", lambda m: f"{m.group(1)}**{fmt(t)}** (Phase 5: ~17:00) |", text)
    SCRIPT.write_text(text, encoding="utf-8")

    # Teleprompter: spoken text only, pause marks kept, holds shown as a bracketed silence cue
    tp = ["الحلقة 1 — «تمام.» — نسخة التلقين (الكلام فقط)", ""]
    for s in scenes:
        tp.append(f"——— {s['id']} ({fmt(s['start'])}) ———")
        for l in s["lines"]:
            if l.startswith("⏳"):
                tp.append(f"[صمت للمشاهد {l[1:]} ثانية — عينك في الكاميرا]")
            elif l.startswith("🎬"):
                tp.append(f"[مقطع بصري بلا كلام {l[1:]} ثانية — لا تسجيل]")
            else:
                tp.append(l.replace("**", ""))
        tp.append("")
    (EP / "11_E01_TELEPROMPTER.txt").write_text("\n".join(tp), encoding="utf-8")

    hits = [(s["id"], b) for s in scenes for b in BANNED if b in " ".join(s["spoken"])]
    checks = cross_checks(scenes)
    out = dict(wpm=WPM, total=fmt(t), total_s=round(t, 1), words=sum(s["words"] for s in scenes),
               banned_hits=hits, checks=checks,
               scenes=[{k: v for k, v in s.items() if k not in ("spoken", "lines")} | {"start": fmt(s["start"]), "end": fmt(s["end"])} for s in scenes])
    (HERE / "e01_runtime.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in out["scenes"]:
        print(f"{s['id']:6} {s['start']}–{s['end']}  {s['dur_s']:6.1f}s  words={s['words']:4}  pauses={s['short_pauses']}/{s['long_pauses']}  holds={s['holds_s']}  silent={s['silent_s']}")
    print("TOTAL", out["total"], "words", out["words"], "banned", hits)
    print("CHECKS", json.dumps(checks, ensure_ascii=False))


if __name__ == "__main__":
    main()
