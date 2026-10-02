"""Shared helpers for the book deck «الذكاء العاطفي للمهندسين».

Same visual system as the E01/E02 decks (dark navy, Lalezar + IBM Plex Sans Arabic, line-art SVG,
public-domain images), without the webcam no-go zone: content spans x 160–1760.
Every text run is wrapped in RLE/PDF so Arabic with Latin fragments keeps its order.
"""
import html, importlib.util, json, math, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
EP = HERE.parent.parent / "07_BOOK_LED_EPISODES"
A = json.loads((HERE / "assets.json").read_text())


def _load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


art1 = _load("art1", EP / "E01/_build/art.py")
art2 = _load("art2", EP / "E02/_build/art.py")

INK, INK2, PAPER = "#0E1522", "#141F33", "#EEE8DC"
PALE, MUTE, DIM = "#E6ECF2", "#9FB0C3", "#3A4A60"
AMB, TEAL, RED = "#F2A541", "#4FBDB0", "#E5533D"
CARD, CARD2, HEAD = "#16223A", "#121C2E", "#1E2B44"
BOOK = {"G": AMB, "MoM": "#3FA796", "CC": "#6E95D8", "NVC": "#E07A62", "KZ": "#A88BD6"}
DISP = "font-family:'Lalezar', Tahoma, sans-serif"
TXT = "font-family:'IBM Plex Sans Arabic', Tahoma, sans-serif"
L, R = 160, 1760
W = R - L

slides, order, sections = {}, [], {}


def nlines(t, size, w, disp=False):
    k = 0.47 if disp else 0.5
    return sum(max(1, math.ceil(len(re.sub(r"<[^>]+>", "", seg)) * size * k / max(w, 1))) for seg in t.split("<br>"))


def T(t, x, y, w, size, color=PALE, weight=400, disp=False, align="right", extra="", build=None):
    b = f' data-build-in="{build}"' if build else ""
    fam = DISP if disp else TXT
    lh = 1.15 if disp else 1.45
    return (f'<p{b} style="{fam};position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;font-size:{size}px;'
            f'font-weight:{weight};color:{color};text-align:{align};line-height:{lh};{extra}">‫{t}‬</p>')


def IMG(key, x, y, w, h, fit="cover", extra="", alt=""):
    return (f'<img src="{A[key]}" alt="{html.escape(alt or key)}" style="position:absolute;left:{x}px;top:{y}px;'
            f'width:{w}px;height:{h}px;object-fit:{fit};{extra}">')


def SVG(markup, x, y, label=None, build=None):
    if label:
        markup = re.sub(r'aria-label="[^"]*"', f'aria-label="{html.escape(label)}"', markup, count=1)
    w = re.search(r'width="(\d+)"', markup).group(1)
    h = re.search(r'height="(\d+)"', markup).group(1)
    b = f' data-build-in="{build}"' if build else ""
    return f'<div{b} style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px">{markup}</div>'


def svg(w, h, body, label):
    return (f'<svg aria-label="{label}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def BOX(x, y, w, h, bg, extra="", build=None):
    b = f' data-build-in="{build}"' if build else ""
    return f'<div{b} style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;height:{h:.0f}px;background:{bg};{extra}"></div>'


def CONN(x1, y1, x2, y2, color=MUTE, width=4, head="end", dashed=False):
    st = ";border-style:dashed" if dashed else ""
    return (f'<x-connector x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" head="{head}" route="straight" '
            f'style="color:{color};border-width:{width}px{st}"></x-connector>')


def NODE(x, y, w, h, t, col, fill, size=36, build=None, tcol=PALE):
    return (BOX(x, y, w, h, fill, f"border:4px solid {col};border-radius:22px", build)
            + T(t, x + 10, y + (h - size * 1.15 * nlines(t, size, w - 20, True)) / 2, w - 20, size, tcol, disp=True, align="center", build=build))


# ---- navigation state: which chapter and which step of it we are in ----
NAV = {"ch": 0, "name": "", "step": ""}
CHAPTERS = {1: "ما المشاعر؟", 2: "الاختطاف العاطفي", 3: "الأفكار والمشاعر", 4: "الوعي الذاتي", 5: "إدارة الانفعال",
            6: "التحفيز الذاتي", 7: "التعاطف والإصغاء", 8: "الحوار الصعب", 9: "النقد والفريق", 10: "الغضب والصراع",
            11: "خطة التدريب", 12: "الملاحق"}
PARTS = [("الآلة", [1, 2, 3]), ("المهارات الذاتية", [4, 5, 6]), ("مع الآخرين", [7, 8, 9, 10]), ("التطبيق", [11, 12])]
SKIP = set()   # slide ids dropped from the deck in the restructure (their key lines moved elsewhere)
EX = {}        # chapter -> exercises, shown on the chapter's closing slide


def chapter(n):
    NAV.update(ch=n, name=CHAPTERS.get(n, ""), step="")


def step(label):
    NAV["step"] = label


def head(eyebrow, title, ecol=AMB, size=76):
    rest = re.sub(r"^الفصل \d+ · ", "", eyebrow)
    if NAV["step"]:
        eyebrow = NAV["step"] + ("  ·  " + rest if rest and not rest.startswith("تمارين") else "")
    return T(eyebrow, L, 140, W, 30, ecol, 700) + T(title, L, 186, W, size, PALE, disp=True)


def progress(dark=True):
    """Map of the book on every slide: 4 parts, 12 segments (11 chapters + appendices); current one in amber."""
    x0, x1, gap = 900, 1760, 6
    n = 12
    sw = (x1 - x0 - gap * (n - 1)) / n
    cur = NAV["ch"]
    out = ""
    for k in range(1, n + 1):
        x = x1 - k * sw - (k - 1) * gap
        col = AMB if k == cur else ((TEAL if dark else "#2E6F68") if k < cur else (DIM if dark else "#C98A2E"))
        op = "1" if k == cur else ("0.55" if k < cur else "0.8")
        out += BOX(x, 92, sw, 10, col, f"border-radius:5px;opacity:{op}")
    for name, chs in PARTS:
        a, b = min(chs), max(chs)
        xr = x1 - (a - 1) * (sw + gap)
        xl = x1 - b * sw - (b - 1) * gap
        on = cur in chs
        c = (AMB if on else MUTE) if dark else (INK if on else "#5A3A10")
        out += T(name, xl, 44, xr - xl, 24, c, 700 if on else 400, align="center")
    return out


def src(t):
    return T(t, L, 990, W, 24, MUTE)


def crumb(page, dark=True):
    out = T("الذكاء العاطفي للمهندسين", 64, 56, 420, 24, MUTE if dark else "#5A3A10", align="left")
    if page:
        out += T(page, 64, 94, 420, 30, AMB if dark else INK, 700, align="left")
    return out


def slide(sid, body, notes, bg=INK, page=None, transition="fade", crumbs=True, section=None):
    if sid in SKIP:
        return
    if NAV["ch"] and crumbs:
        page = f"الفصل {NAV['ch']} · {NAV['name']}" if NAV["ch"] < 12 else "الملاحق"
    if NAV["step"]:
        body = re.sub("\u202bالفصل \\d+ · ", "\u202b" + NAV["step"] + "  ·  ", body, count=1)
    if NAV["name"]:
        body = body.replace(f"  ·  {NAV['name']} · ", "  ·  ")
    if NAV["step"]:
        def fit(m):
            w, txt = int(m.group(1)), m.group(2)
            if len(txt) * 13.5 > w and "  ·  " in txt:
                st, rest = txt.split("  ·  ", 1)
                txt = st + "  ·  " + rest.split(" · ")[-1]
                if len(txt) * 13.5 > w:
                    txt = st
            return m.group(0).replace(m.group(2), txt)
        body = re.sub(r'width:(\d+)px;font-size:30px;[^>]*>\u202b(' + re.escape(NAV["step"]) + r'[^\u202c]*)\u202c', fit, body, count=1)
    if crumbs:
        body += progress(bg != AMB)
    notes = re.sub(r"\n\s+", "\n", notes.strip())
    assert len(notes) <= 4000, sid
    assert sid not in slides, sid
    if section and (NAV["ch"] == 0 or sid.startswith(("open", "part"))):
        sections[f"s{len(sections) + 1}"] = {"description": section, "start": sid}
    slides[sid] = (f'<section id="{sid}" data-transition="{transition}" style="background:{bg};color:{PALE};{TXT};display:block">'
                   f'{body}{crumb(page, bg != AMB) if crumbs else ""}<aside>{html.escape(notes)}</aside></section>')
    order.append(sid)


def cards(items, y, x0=L, w0=W, gap=28, tsize=40, bsize=28, build=True, minh=0, top=10):
    """Row of cards, first item on the right. items: (title, body, color)."""
    n = len(items)
    w = (w0 - gap * (n - 1)) / n
    inner = w - 64
    h = max(minh, max(nlines(t, tsize, inner, True) * tsize * 1.15 + (14 + nlines(b, bsize, inner) * bsize * 1.45 if b else 0)
                      for t, b, c in items) + 64)
    out = ""
    for i, (t, b, c) in enumerate(items):
        x = x0 + w0 - w - i * (w + gap)
        bl = f"rise {i + 1}" if build else None
        out += BOX(x, y, w, h, CARD, f"border-radius:20px;border-top:{top}px solid {c}", bl)
        out += T(t, x + 32, y + 30, inner, tsize, c, disp=True, build=bl)
        if b:
            out += T(b, x + 32, y + 30 + nlines(t, tsize, inner, True) * tsize * 1.15 + 14, inner, bsize, PALE, build=bl)
    return out, y + h


def grid(rows, y, widths, size=28, header=True, colors=None, build=False, pad=18, gap=6, bold_first=True):
    """Table as painted rows; first column on the right. widths are fractions of W."""
    ws = [W * f for f in widths]
    out, cy = "", y
    for ri, row in enumerate(rows):
        hd = header and ri == 0
        h = max(nlines(c, size, w - 2 * pad) for c, w in zip(row, ws)) * size * 1.45 + 2 * pad - 4
        bg = HEAD if hd else (CARD if ri % 2 else CARD2)
        bl = f"fade {ri}" if build and ri else None
        out += BOX(L, cy, W, h, bg, "border-radius:12px", bl)
        x = R
        for ci, (c, w) in enumerate(zip(row, ws)):
            x -= w
            col = AMB if hd else (colors[ci] if colors else (PALE if ci else (TEAL if bold_first else PALE)))
            wt = 700 if hd or (ci == 0 and bold_first) else 400
            out += T(c, x + pad, cy + pad - 2, w - 2 * pad, size, col, wt, build=bl)
        cy += h + gap
    return out, cy


def chip(book, text, x, y, w):
    c = BOOK[book]
    return T(text, x, y, w, 26, c, 700)


def exercises(sid, ch, items, notes, page):
    EX[ch] = items


def _old_exercises(sid, ch, items, notes, page):
    body = head(f"الفصل {ch} · تمارين", "التمارين: القراءة وحدها لا تبني المهارة")
    n = len(items)
    rows = [items[:2], items[2:]] if n == 4 else [items]
    y = 330
    for r in rows:
        c, y = cards([(t, b, TEAL) for t, b in r], y, tsize=40, bsize=30, minh=230)
        body += c
        y += 28
    slide(sid, body, notes, bg=INK2, page=page)


def write(out):
    (out / "slides").mkdir(parents=True, exist_ok=True)
    for f in (out / "slides").glob("*.html"):
        if f.stem not in slides:
            f.unlink()
    for sid, h in slides.items():
        (out / "slides" / f"{sid}.html").write_text(h, encoding="utf-8")
    dj = out / "deck.json"
    deck = json.loads(dj.read_text(encoding="utf-8")) if dj.exists() else {
        "v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-02T12:00:00Z"}, "lists": "css",
        "title": "الذكاء العاطفي للمهندسين",
        "faces": {"lalezar": {"family": "Lalezar", "href": "https://fonts.googleapis.com/css2?family=Lalezar&display=swap"},
                  "ibm-plex-sans-arabic": {"family": "IBM Plex Sans Arabic",
                                           "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap"}},
        "designSystems": []}
    deck["order"] = order
    deck["sections"] = sections
    dj.write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")


CASE = ("الثلاثاء 10:00 · اجتماع التنسيق", "«من أعد هذا الجدول؟ هذا عمل صبياني»",
        "قالها المدير أمام 8 زملاء. الخطأ في بند واحد من أربعين.")


def case_card(x=L, y=300, w=520):
    c = BOOK["CC"]
    out = BOX(x, y, w, 420, "#121E36", f"border-radius:22px;border:3px solid {c}")
    out += T("الحالة", x + 30, y + 26, w - 60, 26, c, 700)
    out += T(CASE[0], x + 30, y + 70, w - 60, 30, MUTE, 600)
    out += T(CASE[1], x + 30, y + 130, w - 60, 46, PALE, disp=True)
    out += T(CASE[2], x + 30, y + 300, w - 60, 28, MUTE)
    return out


def case(sid, title, points, notes, extra="", label="الخطوة 4 من 4: الحالة"):
    """«نرجع للحالة»: the same meeting, seen through this chapter."""
    step(label)
    body = head("", title) + case_card()
    y = 310
    for i, (t, b, c) in enumerate(points):
        h = 40 * 1.15 * nlines(t, 40, 1020, True) + 14 + nlines(b, 28, 1020) * 28 * 1.45 + 40
        body += BOX(740, y, 1020, h, CARD, f"border-radius:18px;border-right:10px solid {c}", f"rise {i + 1}")
        body += T(t, 770, y + 18, 960, 40, c, disp=True, build=f"rise {i + 1}")
        body += T(b, 770, y + 18 + 40 * 1.15 * nlines(t, 40, 960, True) + 10, 960, 28, PALE, build=f"rise {i + 1}")
        y += h + 18
    slide(sid, body + extra, notes, bg=INK2)


def opener(sid, question, came_from, agenda, can_do, notes, section, img="brain_lateral"):
    n = NAV["ch"]
    step("")
    ag = ""
    k = len(agenda)
    w = (W - 30 * (k - 1)) / k
    for i, a in enumerate(agenda):
        x = R - w - i * (w + 30)
        ag += BOX(x, 640, w, 150, CARD, f"border-radius:20px;border-top:8px solid {TEAL}", f"rise {i + 2}")
        ag += T(f"{i + 1}", x + 24, 656, 60, 44, TEAL, disp=True, build=f"rise {i + 2}")
        ag += T(a, x + 24, 712, w - 48, 30, PALE, 700, build=f"rise {i + 2}")
        if i:
            ag += CONN(x + w + 28, 715, x + w + 4, 715, MUTE, 4)
    body = f'''
{T(came_from, L, 140, W, 30, MUTE, 600)}
{T(f"الفصل {n}", L, 206, 560, 100, AMB, disp=True, align="left")}
{T(NAV["name"], 760, 214, 1000, 90, PALE, disp=True)}
{T("السؤال الذي يجيب عنه الفصل:", L, 370, W, 30, AMB, 700)}
{T(question, L, 420, W, 56, PALE, disp=True, build="rise 1")}
{T("خطوات الفصل:", L, 590, W, 28, MUTE)}
{ag}
{T("في نهايته تستطيع: " + can_do, L, 840, W, 34, TEAL, 700, build="rise 6")}'''
    slide(sid, body, notes, section=section)


def closer(sid, takeaways, bridge, nxt, notes):
    n = NAV["ch"]
    step("")
    body = head(f"خلاصة الفصل {n}", "ما الذي أخذناه، وإلى أين بعده")
    tk = ""
    for i, t in enumerate(takeaways):
        y = 320 + i * 132
        tk += BOX(1000, y, 760, 116, CARD, f"border-radius:16px;border-right:10px solid {AMB}", f"rise {i + 1}")
        tk += T(f"{i + 1}", 1680, y + 22, 60, 56, AMB, disp=True, align="center", build=f"rise {i + 1}")
        tk += T(t, 1024, y + 20, 646, 28, PALE, 600, build=f"rise {i + 1}")
    ex = EX.get(n, [])
    exs = T("تمارين الفصل" if ex else "لا تمارين في هذا الفصل", L, 316, 800, 30, TEAL, 700)
    y = 366
    if ex:
        for t, b in ex:
            exs += T(t, L, y, 800, 28, PALE, disp=True) + T(b, L, y + 36, 800, 24, MUTE)
            y += 36 + nlines(b, 24, 860) * 34 + 10
    else:
        exs += T("هذا الفصل أساس نظري: يشرح الآلة التي تتعامل معها المهارات في الفصول التالية.", L, y, 800, 28, MUTE)
    if y > 820: print("closer tight", n, y)
    br = (BOX(L, 810, W, 140, "#2A1E0C", f"border-radius:20px;border:3px solid {AMB}", "rise 4")
          + T("السؤال الذي يبقى مفتوحًا:", L + 40, 826, W - 80, 26, AMB, 700, build="rise 4")
          + T(bridge, L + 520, 866, W - 560, 38, PALE, disp=True, build="rise 4")
          + T(nxt, L + 40, 874, 440, 30, AMB, 700, align="left", build="rise 4"))
    slide(sid, body + tk + exs + br, notes, bg=INK2)
