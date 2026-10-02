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


def head(eyebrow, title, ecol=AMB, size=76):
    return T(eyebrow, L, 140, W, 30, ecol, 700) + T(title, L, 186, W, size, PALE, disp=True)


def src(t):
    return T(t, L, 990, W, 24, MUTE)


def crumb(page, dark=True):
    out = T("الذكاء العاطفي للمهندسين", 64, 56, 420, 24, MUTE if dark else "#5A3A10", align="left")
    if page:
        out += T(page, 64, 94, 420, 30, AMB if dark else INK, 700, align="left")
    return out


def slide(sid, body, notes, bg=INK, page=None, transition="fade", crumbs=True, section=None):
    notes = re.sub(r"\n\s+", "\n", notes.strip())
    assert len(notes) <= 4000, sid
    assert sid not in slides, sid
    if section:
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
