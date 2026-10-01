"""E01 «المخ الانفعالي» — v3: same visual system as v2, rewritten hook + narration.

- Speaker notes come from e01_script.py (SCRIPT dict); SCRIPT.md is generated from it.
- Images: public-domain files from Wikimedia Commons, processed (process_images.py), uploaded as assets;
  their /_blob urls live in assets.json. A missing image renders as an empty frame (alt kept).
- Webcam no-go zone: bottom-left (x < 440, y > 640). Breadcrumb sits top-left.
"""
import json, re, html, pathlib, datetime
import art
from e01_script import SCRIPT

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "deck" / "project"
A = json.loads((HERE / "assets.json").read_text()) if (HERE / "assets.json").exists() else {}

INK, INK2, PAPER = "#0E1522", "#141F33", "#EEE8DC"
PALE, MUTE, DIM = "#E6ECF2", "#9FB0C3", "#3A4A60"
AMB, TEAL, RED = "#F2A541", "#4FBDB0", "#E5533D"
PINK = "#2A1A0A"
DISP = "font-family:'Lalezar', Tahoma, sans-serif"
TXT = "font-family:'IBM Plex Sans Arabic', Tahoma, sans-serif"


slides, order = {}, []


def T(t, x, y, w, size, color=PALE, weight=400, disp=False, align="right", extra="", build=None, i=None):
    """Pinned text block."""
    b = f' data-build-in="{build}"' if build else ""
    idt = f' id="{i}"' if i else ""
    fam = DISP if disp else TXT
    lh = 1.15 if disp else 1.45
    return (f'<p{idt}{b} style="{fam};position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;'
            f'font-weight:{weight};color:{color};text-align:{align};line-height:{lh};{extra}">\u202b{t}\u202c</p>')


def IMG(key, x, y, w, h, fit="cover", extra="", alt=""):
    src = A.get(key)
    s = f' src="{src}"' if src else ""
    return f'<img{s} alt="{html.escape(alt or key)}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:{fit};{extra}">'


def SVG(markup, x, y, build=None):
    w = re.search(r'width="(\d+)"', markup).group(1)
    h = re.search(r'height="(\d+)"', markup).group(1)
    b = f' data-build-in="{build}"' if build else ""
    return f'<div{b} style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px">{markup}</div>'


def BOX(x, y, w, h, bg, extra=""):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}"></div>'


def crumb(page, dark=True):
    c = MUTE if dark else "#5A6170"
    out = T("الحلقة 1 · المخ الانفعالي", 64, 56, 360, 24, c, align="left")
    if page:
        out += T(page, 64, 96, 360, 30, AMB if dark else "#A35F00", 700, align="left")
    return out


def slide(sid, body, bg=INK, page=None, dark=True, transition="fade", crumbs=True):
    notes = SCRIPT[sid].strip()
    assert len(notes) <= 4000, sid
    slides[sid] = (f'<section id="{sid}" data-transition="{transition}" style="background:{bg};color:{PALE};{TXT};display:block">'
                   f'{body}{crumb(page, dark) if crumbs else ""}<aside>{html.escape(notes)}</aside></section>')
    order.append(sid)


def chip(book, x, y, w, text, ref, dark=True):
    cols = {"MoM": "#3FA796", "CC": "#6E95D8", "NVC": "#E07A62", "KZ": "#A88BD6"}
    names = {"MoM": "Mind Over Mood", "CC": "Crucial Conversations", "NVC": "Nonviolent Communication", "KZ": "Kabat-Zinn"}
    c = cols[book]
    bg = "#16223A" if dark else "#FFFFFF"
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;display:flex;flex-direction:column;gap:8px;background:{bg};'
            f'border:3px solid {c};border-radius:20px;padding:28px 32px">'
            f'<p style="{TXT};font-size:24px;font-weight:700;color:{c};text-align:right">\u202bكتاب تاني · {names[book]} · {ref}\u202c</p>'
            f'<p style="{TXT};font-size:32px;color:{PALE if dark else INK};text-align:right;line-height:1.4">\u202b{text}\u202c</p></div>')


# 1 cover — brain drawing glowing amber, huge title
slide("cover", f'''
{IMG("brain_lateral", 0, 0, 1920, 1080, "cover", "opacity:0.55", "رسم تشريحي قديم للمخ (Gray's Anatomy)")}
{BOX(0, 0, 1920, 1080, "linear-gradient(90deg, rgba(14,21,34,0.2) 0%, rgba(14,21,34,0.92) 55%)")}
{T("من كتاب «الذكاء العاطفي» · دانييل جولمان", 760, 250, 1040, 34, AMB, 700)}
{T("ليه بترد<br>قبل ما تفكر؟", 760, 320, 1040, 168, PALE, disp=True)}
{T("الحلقة 1 · المخ الانفعالي", 760, 740, 1040, 48, MUTE, 600)}
{T("المقدمة · الفصل 1 · الفصل 2", 760, 810, 1040, 32, AMB)}''', page=None)

# 2 meeting — top-down illustration
slide("meeting", f'''
{SVG(art.meeting(), 470, 300)}
{T("مثال توضيحي · الأسماء من تأليفنا", 1420, 150, 380, 24, MUTE)}
{T("اجتماع التنسيق · 10:05 ص", 1100, 190, 700, 36, MUTE, 600)}
{T("«مين عامل الشيت ده؟ ده شغل عيال.»", 1420, 330, 380, 64, PALE, disp=True, build="rise 1")}
{T("أ. هشام", 470, 880, 300, 32, RED, 700, align="left")}
{T("كريم (الشيت بتاعه)", 820, 880, 400, 32, AMB, 700, align="center")}''', page="مثال")

# 3 karim reply — stopwatch
slide("karim-reply", f'''
{SVG(art.timer(), 1440, 170)}
{T("ثانيتين", 1440, 560, 360, 56, AMB, disp=True, align="center")}
{T("«حضرتك لو كنت قريت<br>الإيميل كنت عرفت إن…»", 470, 200, 940, 88, PALE, disp=True, build="fade 1")}
{T("صمت.", 470, 520, 940, 120, "#5C6B80", disp=True, build="fade 2")}
{T("وبعد الاجتماع، لنفسه: «أنا ماكنتش عايز أقول كده.»", 470, 760, 1330, 44, AMB, 600, build="rise 3")}''', page="مثال")

# 4 who — accent statement slide (ties the jolt to Karim and to the viewer)
slide("who", f'''
{IMG("brain_lateral", 900, 80, 1000, 920, "contain", "opacity:0.18", "مخ")}
{T("نفس الحاجة اللي خضّتك من دقيقة…", 470, 230, 1330, 56, "#3A2405", 700)}
{T("هي اللي ردّت<br>مكان كريم", 470, 320, 1330, 190, INK, disp=True)}
{T("وهي اللي ردّت مكانك… آخر مرة قلت «ماكنتش قاصد».", 470, 800, 1330, 40, "#3A2405", 600, build="rise 1")}''', bg=AMB, page="السؤال", dark=False)

# 5 map — the book as a tree
eps = [("E1", "المخ الانفعالي"), ("E2", "أنا ومشاعري"), ("E3", "أنا والناس"), ("E4", "البيت والشغل"), ("E5", "الفرص المتاحة"), ("E6", "محو الأمية العاطفية")]
xs = [1580, 1360, 1140, 920, 700, 480]
mp = BOX(1020, 270, 360, 120, "#1E2B44", "border:3px solid " + AMB + ";border-radius:24px")
mp += T("«الذكاء العاطفي»", 1020, 292, 360, 48, PALE, disp=True, align="center")
mp += BOX(560, 470, 1280, 4, DIM)
mp += BOX(1198, 390, 4, 80, DIM)
for (i, t), x in zip(eps, xs):
    on = i == "E1"
    mp += BOX(x + 98, 470, 4, 60, DIM)
    mp += (f'<div style="position:absolute;left:{x}px;top:530px;width:200px;height:200px;border-radius:24px;'
           f'background:{AMB if on else "#16223A"};border:3px solid {AMB if on else DIM}"></div>')
    mp += T(i, x, 560, 200, 30, INK if on else MUTE, 700, align="center")
    mp += T(t, x + 10, 610, 180, 34, INK if on else PALE, disp=True, align="center")
slide("map", f'''
{T("الخريطة: كل حلقة = جزء من الكتاب", 470, 150, 1330, 56, PALE, disp=True)}
{mp}
{T("ومع كل جزء… الكتب التانية اللي بتكمّله", 470, 800, 1330, 38, MUTE)}''', page="الخريطة")

# 6 aristotle — bust beside the quote, museum paper
slide("aristotle", f'''
{IMG("aristotle", 470, 0, 640, 1080, "cover", "", "تمثال نصفي لأرسطو (متحف ألتمبس، روما)")}
{BOX(470, 0, 640, 1080, "linear-gradient(90deg, rgba(238,232,220,0) 70%, rgba(238,232,220,1) 100%)")}
{T("أرسطو · «الأخلاق إلى نيقوماخوس»", 1150, 150, 650, 28, "#A35F00", 700)}
{T("«أن يغضب أي إنسان، فهذا أمر سهل…»", 1150, 200, 650, 60, INK, disp=True)}
{T("لكن أن تغضب من الشخص المناسب، وبالقدر المناسب، وفي الوقت المناسب، وللهدف المناسب، وبالأسلوب المناسب… فليس هذا بالأمر السهل.", 1150, 430, 650, 38, "#2B3140", 500)}
{T("جولمان يفتتح بها كتابه · ص7", 1150, 860, 650, 28, "#5A6170")}''', bg=PAPER, page="ص7", dark=False)

# 7 specs — engineering spec sheet
rows = ""
specs = [("الشخص", "مديره", "?"), ("القدر", "كبير", "✗"), ("الوقت", "قدام 8", "✗"), ("الهدف", "يدافع عن نفسه", "?"), ("الأسلوب", "هجوم", "✗")]
for i, (a, b, c) in enumerate(specs):
    y = 300 + i * 104
    rows += BOX(470, y, 1330, 96, "#16223A" if i % 2 == 0 else INK2, "border-bottom:2px solid " + DIM)
    rows += T(a + " المناسب", 1330, y + 22, 450, 40, PALE, 700)
    rows += T(b, 700, y + 26, 600, 36, MUTE)
    rows += T(c, 490, y + 16, 160, 48, RED if c == "✗" else AMB, 700, align="center")
slide("specs", f'''
{T("SPEC SHEET · الغضب المناسب", 470, 140, 1330, 30, AMB, 700)}
{T("5 مواصفات… ورد كريم", 470, 180, 1330, 72, PALE, disp=True)}
{T("المواصفة", 1330, 260, 450, 26, MUTE, 600)}{T("رد كريم", 700, 260, 600, 26, MUTE, 600)}{T("مطابق؟", 490, 260, 160, 26, MUTE, 600, align="center")}
{rows}
{T("✎ علّم بالقلم وانت بتتكلم", 470, 840, 1330, 30, AMB)}''', page="ص7")

# 9 ch1 divider — Cajal neurons
slide("ch1", f'''
{IMG("cajal", 0, 0, 1920, 1080, "cover", "opacity:0.6", "رسم خلايا عصبية لسانتياغو رامون إي كاخال")}
{BOX(0, 0, 1920, 1080, "linear-gradient(0deg, rgba(14,21,34,0.95) 25%, rgba(14,21,34,0.35) 100%)")}
{T("الجزء الأول · المخ الانفعالي", 470, 470, 1330, 40, AMB, 700)}
{T("الفصل 1", 470, 530, 1330, 64, MUTE, disp=True)}
{T("العواطف… لماذا؟", 470, 610, 1330, 160, PALE, disp=True)}
{T("ص17", 470, 830, 1330, 36, MUTE)}''', page="ص17", transition="push")

# 10 motion
slide("motion", f'''
{T("أصل الكلمة", 470, 150, 1330, 32, AMB, 700)}
{T("E + motion", 1000, 230, 800, 150, PALE, disp=True, extra="letter-spacing:2px")}
{SVG(art.motion(), 470, 240)}
{T("= حركة", 1000, 420, 800, 110, AMB, disp=True)}
{T("كل انفعال = «نزوع إلى القيام بفعل»", 470, 640, 1330, 64, PALE, disp=True)}
{T("العاطفة مش مجرد إحساس… هي أمر تشغيل للجسم.", 470, 760, 1330, 40, MUTE)}''', page="ص20")

# 11 body — Vitruvian man with hands / legs callouts
slide("body", f'''
{IMG("vitruvian", 860, 110, 700, 870, "contain", "", "الرجل الفيتروفي لليوناردو دافنشي")}
{T("بصمة الانفعال في جسمك", 470, 150, 380, 64, PALE, disp=True)}
{T("الغضب", 1560, 230, 260, 56, AMB, disp=True, build="rise 1")}
{T("الدم يروح لليدين · القلب يسرع · أدرينالين", 1560, 300, 260, 30, PALE, build="rise 1")}
{T("الخوف", 1560, 620, 260, 56, "#6E95D8", disp=True, build="rise 2")}
{T("الدم لعضلات الرجلين · الوش يشحب · تجمّد لحظة", 1560, 690, 260, 30, PALE, build="rise 2")}
{chip("CC", 470, 330, 370, "جسمك بيبان عليه قبل ما انت تاخد بالك.", "p.48–49")}
{T("ص21", 470, 900, 370, 28, MUTE, align="left")}''', page="ص21")

# 12 two minds — brain with two halves + tear
slide("two-minds", f'''
{IMG("brain_lateral", 470, 230, 760, 640, "contain", "opacity:0.9", "رسم تشريحي للمخ")}
{BOX(470, 230, 380, 640, "rgba(79,189,176,0.18)", "mix-blend-mode:screen;border-radius:30px")}
{BOX(850, 230, 380, 640, "rgba(242,165,65,0.18)", "mix-blend-mode:screen;border-radius:30px")}
{T("في دماغنا عقلين", 470, 130, 1330, 80, PALE, disp=True)}
{T("الكلام", 1290, 300, 510, 30, TEAL, 700)}
{T("«لم يعد يهمني حقًا»", 1290, 345, 510, 60, PALE, disp=True)}
{T("العقل اللي بيفكر", 1290, 430, 510, 32, TEAL)}
{T("العينين", 1290, 560, 510, 30, AMB, 700, build="rise 1")}
{T("اغرورقت بالدموع", 1290, 605, 510, 60, PALE, disp=True, build="rise 1")}
{T("العقل اللي بيحس", 1290, 690, 510, 32, AMB, build="rise 1")}
{T("صديقة جولمان بعد طلاقها · ص23–24", 1290, 860, 510, 26, MUTE)}''', page="ص23–24")

# 13 five-part — pentagon diagram
ring = [("موقف", 1060, 220), ("أفكار", 1420, 420), ("مشاعر", 1290, 760), ("جسم", 830, 760), ("تصرف", 700, 420)]
pent = '<svg aria-label="خماسية متصلة" width="1100" height="760" viewBox="0 0 1100 760" fill="none" stroke-linecap="round">'
cent = [(x - 470 + 130, y - 160 + 50) for _, x, y in ring]
for i in range(5):
    for j in range(i + 1, 5):
        pent += f'<line x1="{cent[i][0]}" y1="{cent[i][1]}" x2="{cent[j][0]}" y2="{cent[j][1]}" stroke="#3FA796" stroke-width="{5 if (j - i) in (1, 4) else 2}" opacity="{0.9 if (j - i) in (1, 4) else 0.35}"/>'
pent += "</svg>"
nodes = "".join(BOX(x, y, 260, 100, "#16223A", "border:4px solid #3FA796;border-radius:50px") + T(t, x, y + 18, 260, 48, PALE, disp=True, align="center") for t, x, y in ring)
slide("five-part", f'''
{T("كتاب تاني · Mind Over Mood · p.7–8", 470, 110, 1330, 28, "#3FA796", 700)}
{T("كلهم ماسكين في بعض", 470, 150, 600, 64, PALE, disp=True, align="left")}
{SVG(pent, 470, 160)}
{nodes}
{T("أي تغيير في واحدة… بيحرّك الباقي", 900, 560, 620, 34, MUTE, align="center")}''', page="MoM")

# 14 ch2 divider — medial brain
slide("ch2", f'''
{IMG("brain_medial", 760, 0, 1160, 1080, "cover", "opacity:0.55", "مقطع طولي في المخ (Gray's Anatomy)")}
{BOX(0, 0, 1920, 1080, "linear-gradient(90deg, rgba(14,21,34,0.25) 0%, rgba(14,21,34,0.95) 60%)")}
{T("الجزء الأول · المخ الانفعالي", 470, 380, 1330, 40, AMB, 700)}
{T("الفصل 2", 470, 440, 1330, 64, MUTE, disp=True)}
{T("تشريح النوبات<br>الانفعالية", 470, 520, 1330, 150, PALE, disp=True)}
{T("ص31", 470, 880, 1330, 36, MUTE)}''', page="ص31", transition="push")

# 15 hijack — protection relay vs control room (our analogy)
slide("hijack", f'''
{T("النوبة الانفعالية · Emotional Hijacking", 470, 140, 1330, 30, AMB, 700)}
{T("المخ يعلن حالة الطوارئ…", 470, 180, 1330, 84, PALE, disp=True)}
{T("قبل ما العقل اللي بيفكر يلحق يشوف إيه اللي بيحصل.", 470, 290, 1330, 38, MUTE, 600)}
{SVG(art.relay(), 470, 390)}
{T("ريليه الحماية: بيفصل في جزء من الثانية", 470, 800, 360, 26, AMB, 700, align="center", build="rise 1")}
{T("غرفة التحكم: بتعرف بعدين", 880, 760, 340, 26, TEAL, 700, align="center", build="rise 1")}
{T("تشبيه من عندنا", 470, 900, 750, 24, MUTE, align="center")}
{T("العلامة:", 1300, 500, 500, 34, AMB, 700, build="rise 2")}
{T("«أنا مش عارف إيه اللي جرالي»", 1300, 550, 500, 56, PALE, disp=True, build="rise 2")}''', page="ص31")

# 16 small daily hijack — painting + phone
slide("small", f'''
{T("مش لازم تبقى كارثة… بتحصل كل يوم", 470, 140, 1330, 64, PALE, disp=True)}
{SVG(art.frame(), 1280, 280)}
{T("من الكتاب · ص34", 1280, 690, 520, 26, AMB, 700)}
{T("لوحة كانت نفسها فيها من شهور… رمتها في الزبالة في لحظة، وندمت بعدها بشهور.", 1280, 730, 520, 30, PALE)}
{SVG(art.phone(), 900, 260)}
{T("ريييم… التعديلات جاهزة", 960, 400, 220, 22, PALE, align="center")}
{T("تمام.", 1050, 572, 130, 26, PALE, 700, align="center")}
{T("خلاص يا ستي…", 960, 680, 220, 24, AMB, 600, align="center")}
{T("من شغلنا · مثال توضيحي", 470, 300, 400, 26, AMB, 700)}
{T("نور، مهندسة معمارية، بعتت التعديلات للـPM. الرد بعد 40 دقيقة: «تمام.»… وفي 40 ثانية كتبت رد فيه عتاب.", 470, 340, 400, 30, PALE)}''', page="ص34")

# 17 alarm — smoke detector + 3 questions
qs = ["هل أكره ده؟", "هل ده هيأذيني؟", "هل ده حاجة بخاف منها؟"]
qb = "".join(T(f"«{q}»", 1100, 330 + i * 110, 700, 48, PALE, disp=True, build=f"rise {i + 1}") for i, q in enumerate(qs))
slide("alarm", f'''
{SVG(art.detector(), 520, 280)}
{T("الأميجدالا (اللوزة)", 470, 140, 1330, 32, AMB, 700)}
{T("فريق الإنذار اللي في بيتك", 470, 180, 1330, 76, PALE, disp=True)}
{T("بيسأل 3 أسئلة بس:", 1100, 280, 700, 32, MUTE)}
{qb}
{T("ومش بيسأل: «هو قصده إيه بالظبط؟»", 470, 720, 1330, 44, RED, 700, build="rise 4")}
{T("زي حساس الدخان: شغلته يصفّر بسرعة… مش يحلل نوع الدخان.", 470, 800, 1330, 34, MUTE, build="rise 4")}''', page="ص34–35")

# 18 two roads — schematic over faded brain
def node(x, y, w, t, col, fill):
    return BOX(x, y, w, 120, fill, f"border:4px solid {col};border-radius:24px") + T(t, x, y + 22, w, 40, PALE, disp=True, align="center")


slide("two-roads", f'''
{IMG("brain_medial", 470, 160, 1330, 860, "contain", "opacity:0.12", "مخ")}
{T("اكتشاف جوزيف لودو · ص36–37 · (رسم تبسيطي)", 470, 110, 1330, 28, AMB, 700)}
{T("الإشارة بتمشي في طريقين", 470, 150, 1330, 72, PALE, disp=True)}
{node(1560, 500, 240, "العين والودن", MUTE, "#16223A")}
{node(1160, 500, 260, "المهاد", MUTE, "#16223A")}
<div id="cx" data-build-in="fade 2" style="position:absolute;left:520px;top:300px;width:400px;height:130px;background:#123330;border:4px solid {TEAL};border-radius:24px"></div>
{T("القشرة الجديدة · بتفكر", 520, 335, 400, 40, PALE, disp=True, align="center", build="fade 2")}
<div id="am" data-build-in="rise 1" style="position:absolute;left:520px;top:720px;width:400px;height:130px;background:#3A2A10;border:4px solid {AMB};border-radius:24px"></div>
{T("الأميجدالا · الإنذار", 520, 755, 400, 40, PALE, disp=True, align="center", build="rise 1")}
<x-connector x1="1560" y1="560" x2="1420" y2="560" head="end" style="color:{MUTE};border-width:5px"></x-connector>
<x-connector x1="1160" y1="600" x2="920" y2="785" head="end" style="color:{AMB};border-width:10px"></x-connector>
<x-connector x1="1160" y1="520" x2="920" y2="365" head="end" style="color:{TEAL};border-width:5px;border-style:dashed"></x-connector>
{T("① قصير: بيوصل الأول", 960, 760, 380, 34, AMB, 700, build="rise 1")}
{T("② طويل: بيفكر… ويتأخر", 960, 330, 380, 34, TEAL, 700, build="fade 2")}''', page="ص36–37")

# 19 fast but wrong — bedroom 3am
slide("fast-wrong", f'''
{SVG(art.bedroom(), 470, 380)}
{T("لودو، كما ينقله جولمان · ص44", 470, 140, 1330, 28, AMB, 700)}
{T("«سريعة جدًا… لكنها كثيرة الأخطاء»", 470, 180, 1330, 84, PALE, disp=True)}
{T("3:00 الفجر", 1240, 400, 560, 64, AMB, disp=True)}
{T("خبطة ضخمة… جولمان نط من السرير فاكر السقف وقع.", 1240, 490, 560, 36, PALE)}
{T("طلعت كراتين مراته وقعت.", 1240, 640, 560, 44, AMB, 700, build="rise 1")}
{T("ص42–43", 1240, 860, 560, 26, MUTE)}''', page="ص42–44")

# 20 old alarm — notebook to meeting
slide("old-alarm", f'''
{SVG(art.notebook(), 1400, 330)}
{T("زمان", 1400, 760, 380, 44, RED, disp=True, align="center")}
<x-connector x1="1380" y1="540" x2="1000" y2="540" head="end" style="color:{AMB};border-width:8px;border-style:dashed"></x-connector>
{T("«شغل عيال»", 470, 470, 500, 76, AMB, disp=True, align="center")}
{T("دلوقتي", 470, 580, 500, 44, AMB, disp=True, align="center")}
{T("إنذارات قديمة", 470, 140, 1330, 84, PALE, disp=True)}
{T("الإنذار بيقارن الحاضر بالماضي… ويتصرف بطريقة «انطبعت في ذاكرتنا منذ زمن طويل» · ص41", 470, 250, 1330, 34, MUTE)}
{T("كريم (مثال): مدرس في إعدادي ضحك على كراسته قدام الفصل.", 1000, 640, 380, 28, PALE)}
{chip("MoM", 470, 700, 500, "الماضي بيشكّل إزاي بنقرا الحاضر.", "p.63")}''', page="ص41")

# 21 jessica — telephone photo + 3 beats
beats = [("منتصف الليل", "جيسكا (6 سنين) بايتة برا لأول مرة. التليفون يرن.", AMB),
         ("الإنذار", "الفرشة وقعت… جريت وصرخت: «جيسكا!»", RED),
         ("الفرامل", "«أظن أنني طلبت رقمًا خطأ» ← تهدى وتسأل: «ما الرقم الذي تطلبينه؟»", TEAL)]
bt = ""
for i, (a, b, c) in enumerate(beats):
    y = 300 + i * 190
    bt += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:1040px;top:{y}px;width:760px;height:170px;background:#16223A;border-radius:20px;border-right:12px solid {c}"></div>'
    bt += T(a, 1060, y + 18, 710, 40, c, disp=True, build=f"rise {i + 1}")
    bt += T(b, 1060, y + 76, 710, 30, PALE, build=f"rise {i + 1}")
slide("jessica", f'''
{IMG("telephone", 470, 300, 520, 520, "cover", "border-radius:24px;filter:grayscale(1) contrast(1.1)", "تليفون قديم بقرص")}
{T("قصة من الكتاب · ص45", 470, 140, 1330, 28, AMB, 700)}
{T("أم جيسكا: الإنذار… والفرامل", 470, 180, 1330, 72, PALE, disp=True)}
{bt}''', page="ص45")

# 22 two forces — balance
slide("two-forces", f'''
{SVG(art.balance(), 820, 330)}
{T("النوبة محتاجة قوتين مع بعض", 470, 150, 1330, 76, PALE, disp=True)}
{T("بتشغّل الإنذار", 1440, 640, 360, 44, AMB, disp=True)}
{T("«شغل عيال» · ذكرى قديمة · ضغط", 1440, 700, 360, 28, PALE)}
{T("بتضعف الفرامل", 470, 300, 380, 44, TEAL, disp=True)}
{T("الذاكرة العاملة تتجمد: «مش قادر أفكر صح»", 470, 360, 380, 28, PALE)}
{T("لو الاتنين حصلوا مع بعض… الإنذار بيكسب. · ص47–49", 470, 860, 1330, 32, MUTE)}''', page="ص47–49")

# 23 two layers — fire
slide("two-layers", f'''
{SVG(art.fire(), 470, 330)}
{T("طب الأفكار مالهاش دور؟", 470, 150, 1330, 76, PALE, disp=True)}
{T("① إنذار سريع", 1100, 320, 700, 64, AMB, disp=True)}
{T("② حكاية بتغذيه… أو تطفيه", 1100, 420, 700, 64, TEAL, disp=True, build="rise 1")}
{chip("CC", 1100, 560, 700, "بين اللي حصل واللي حسيته «حكاية»… وبتتحكي «بسرعة كبيرة جدًا».", "p.98–101")}
{T("الطبقة التانية = الحلقة الجاية", 470, 860, 1330, 34, MUTE)}''', page="CC")

# 24 replay — film strip timeline
steps = [("0.0 ث", "«شغل عيال»", MUTE), ("0.1 ث", "الإنذار: «هجوم… زي زمان»", AMB), ("0.5 ث", "الجسم: سخونة · قلب · فك", AMB),
         ("1.5 ث", "الرد: «لو كنت قريت الإيميل…»", RED), ("بعدين", "الفرامل توصل: «ماكنتش عايز أقول كده»", TEAL)]
fs = BOX(470, 330, 1330, 420, "#0A0F18", "border-radius:12px")
for k in range(24):
    fs += BOX(490 + k * 55, 345, 30, 22, DIM, "border-radius:4px") + BOX(490 + k * 55, 713, 30, 22, DIM, "border-radius:4px")
for i, (t, s, c) in enumerate(steps):
    x = 1540 - i * 262
    fs += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:{x}px;top:390px;width:246px;height:300px;background:#16223A;border-top:10px solid {c};border-radius:10px"></div>'
    fs += T(t, x + 10, 410, 226, 30, c, 700, build=f"rise {i + 1}")
    fs += T(s, x + 10, 470, 226, 30, PALE, disp=True, build=f"rise {i + 1}")
slide("replay", f'''
{T("نرجّع الشريط بالبطيء", 470, 150, 1330, 80, PALE, disp=True)}
{T("الأزمنة توضيحية", 470, 260, 1330, 26, MUTE)}
{fs}
{T("مين اللي رد مكان كريم؟ الإنذار… نفس اللي خضّك في أول الحلقة.", 470, 810, 1330, 52, AMB, disp=True, build="rise 6")}''', page="الإجابة")

# 25 body map — Vitruvian with lamps
LAMPS = "".join(
    f'<div data-build-in="pop {i + 1}" style="position:absolute;left:{x - 18}px;top:{y - 18}px;width:36px;height:36px;border-radius:50%;background:{AMB};border:4px solid #FFF3DD;box-shadow:0 0 28px {AMB}"></div>'
    for i, (x, y) in enumerate([(820, 395), (820, 473), (820, 548), (561, 440), (1065, 440)]))
slide("body-map", f'''
{IMG("vitruvian", 470, 170, 700, 860, "contain", "", "الرجل الفيتروفي")}
{T("تمرين: إنذارك بيبان فين الأول؟", 470, 100, 1330, 64, PALE, disp=True)}
{LAMPS}
{T("1 · افتكر آخر مرة رديت قبل ما تفكر", 1220, 280, 580, 34, PALE, 600)}
{T("2 · أول حاجة حسيتها في جسمك؟", 1220, 360, 580, 34, PALE, 600)}
{T("الفك · الصدر · المعدة · القبضة", 1220, 440, 580, 34, AMB, 700)}
{T("3 · علّمها بالقلم على الرسمة", 1220, 520, 580, 34, PALE, 600)}
{T("دي «اللمبة» بتاعتك", 1220, 620, 580, 56, AMB, disp=True)}
{chip("CC", 1220, 730, 580, "العلامات المبكرة = أول فرصة تلحق نفسك.", "p.48–49")}''', page="تمرين")

# 26 recap
rc = [("1", "المشاعر مش عدوك", "ص20", AMB), ("2", "فيه طريق قصير… بيغلط كتير", "ص36–44", RED), ("3", "فيه فرامل… بتضعف", "ص45–49", TEAL)]
rcb = ""
for i, (n, a, b, c) in enumerate(rc):
    x = 1370 - i * 450
    rcb += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:{x}px;top:330px;width:430px;height:420px;background:#16223A;border-radius:24px;border-top:12px solid {c}"></div>'
    rcb += T(n, x, 360, 430, 120, c, disp=True, align="center", build=f"rise {i + 1}")
    rcb += T(a, x + 30, 520, 370, 48, PALE, disp=True, align="center", build=f"rise {i + 1}")
    rcb += T(b, x, 680, 430, 28, MUTE, align="center", build=f"rise {i + 1}")
slide("recap", f'''
{T("3 حاجات من الحلقة دي", 470, 150, 1330, 84, PALE, disp=True)}
{rcb}
{T("+ عرفت أول لمبة للإنذار في جسمك", 470, 820, 1330, 40, AMB, 700)}''', bg=INK2, page="الخلاصة")

# 27 next — laptop at 2am
slide("next", f'''
{SVG(art.laptop(), 470, 330)}
{T("الحلقة الجاية · أنا ومشاعري", 1200, 140, 600, 32, AMB, 700)}
{T("كريم هدي…", 1200, 200, 600, 72, PALE, disp=True)}
{T("بس الساعة 2 بالليل فتح الإيميل وكتب:", 1200, 320, 600, 36, MUTE)}
{T("«أنا بستقيل.»", 1200, 400, 600, 96, RED, disp=True)}
{T("هيدوس Send؟", 1200, 640, 600, 72, AMB, disp=True, build="rise 1")}
{T("Send", 850, 571, 130, 30, PALE, 700, align="center")}''', page="الحلقة 2")

# 28 end
slide("end", f'''
{IMG("cajal", 0, 0, 1920, 1080, "cover", "opacity:0.25", "خلايا عصبية (كاخال)")}
{T("اكتبلي في التعليقات:", 470, 260, 1330, 56, MUTE, 600)}
{T("إنذارك بيبان<br>فين الأول؟", 470, 340, 1330, 150, AMB, disp=True)}
{T("الفك · الصدر · المعدة · القبضة… ولا حاجة تانية؟", 470, 720, 1330, 40, PALE)}
{T("صور: Wikimedia Commons (ملكية عامة) · المصدر: جولمان، «الذكاء العاطفي»، عالم المعرفة 262", 470, 920, 1330, 24, MUTE)}''', page="النهاية")

# ---------- v3 new slides ----------

# jolt — cold open: focus dot, then a single white flash
slide("jolt", f'''
<div style="position:absolute;left:942px;top:522px;width:36px;height:36px;border-radius:50%;background:{AMB};box-shadow:0 0 40px {AMB}"></div>
{T("ركّز على النقطة دي", 470, 640, 1000, 34, DIM, 600, align="center")}
<div data-build-in="pop 1" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;background:#FFFFFF"></div>
{T("اتخضّيت؟", 470, 300, 1330, 220, INK, disp=True, align="center", build="pop 1")}
{T("مين اللي قرر؟", 470, 620, 1330, 96, RED, disp=True, align="center", build="rise 2")}''', bg="#05080D", crumbs=False, transition="fade")

# smart — the book's big question + the 20% bar
bar = (BOX(470, 560, 1330, 150, "#1A2436", "border-radius:20px")
       + f'<div data-build-in="fade 1" style="position:absolute;left:1534px;top:560px;width:266px;height:150px;background:{TEAL};border-radius:20px"></div>'
       + T("IQ ≈ 20%", 1534, 600, 266, 52, INK, disp=True, align="center", build="fade 1")
       + T("80% … إيه؟", 470, 600, 1040, 56, MUTE, disp=True, align="center", build="fade 2"))
slide("smart", f'''
{T("سؤال الكتاب · ص52–54", 470, 140, 1330, 30, AMB, 700)}
{T("ليه ناس أذكيا جدًا…<br>بيعملوا حاجات غبية جدًا؟", 470, 190, 1330, 112, PALE, disp=True)}
{bar}
{T("معامل الذكاء، «على أحسن تقدير»، بيساهم بحوالي 20% بس من العوامل اللي بتحدد النجاح في الحياة · ص54", 470, 740, 1330, 32, PALE)}
{T("رأي جولمان في الكتاب… واتناقش كتير بعده", 470, 860, 1330, 26, MUTE)}''', page="ص52–54")

# answer — the other intelligence, as a spec list
abil = ["تحفّز نفسك وتكمّل رغم الإحباط", "تتحكم في النزوة وتأجّل المكافأة", "تظبط مزاجك… وماتسيبش الضيق يشلّ تفكيرك",
        "تحس باللي قدامك", "تفضل عندك أمل"]
ab = ""
for i, a in enumerate(abil):
    y = 300 + i * 96
    hl = i == 2
    ab += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:820px;top:{y}px;width:980px;height:80px;background:{"#3A2A10" if hl else "#16223A"};border-radius:16px;border-right:10px solid {AMB if hl else TEAL}"></div>'
    ab += T(a, 850, y + 14, 910, 38, PALE, 600 if hl else 500, build=f"rise {i + 1}")
slide("answer", f'''
{T("إجابة جولمان", 470, 140, 1330, 30, AMB, 700)}
{T("فيه ذكاء تاني", 470, 180, 1330, 96, PALE, disp=True)}
{ab}
<div data-build-in="pop 6" style="position:absolute;left:470px;top:420px;width:300px;height:220px;border-radius:28px;background:#123330;border:4px solid {TEAL}"></div>
{T("والأهم:", 470, 445, 300, 32, TEAL, 700, align="center", build="pop 6")}
{T("بيتعلّم", 470, 495, 300, 84, PALE, disp=True, align="center", build="pop 6")}
{T("القدرات ص54 · «الطبع مش مصير» المقدمة ص10–13", 820, 800, 980, 26, MUTE)}''', page="ص54")

# snow — Goleman's Colorado story
slide("snow", f'''
{SVG(art.snow_car(), 470, 330)}
{T("قصة جولمان نفسه · ص20", 1230, 140, 570, 30, AMB, 700)}
{T("كولورادو.<br>التلج قفل الرؤية.", 1230, 190, 570, 76, PALE, disp=True)}
{T("خاف… فركن على جنب واستنى.", 1230, 390, 570, 36, PALE)}
{T("وبعد كام مية متر: حادثة قفلت الطريق.", 1230, 480, 570, 36, RED, 700, build="rise 1")}
{T("«ربما كان الخوف الحذر الذي تملكني في ذلك اليوم قد أنقذ حياتي»", 470, 760, 1330, 46, AMB, disp=True, build="rise 2")}''', page="ص20")

# legacy — stone-age hardware, modern software
slide("legacy", f'''
{SVG(art.legacy(), 470, 360)}
{T("هاردوير قديم", 470, 720, 280, 34, AMB, 700, align="center")}
{T("سوفتوير جديد", 860, 720, 400, 34, RED, 700, align="center")}
{T("المشكلة فين؟ · ص19", 1300, 140, 500, 30, AMB, 700)}
{T("ملفات اتكتبت<br>لعالم تاني", 1300, 190, 500, 84, PALE, disp=True)}
{T("«حقائق الحضارة الجديدة قد تسارعت بهذه الدرجة التي لم يستطع إيقاع التطور البطيء أن يواكبها»", 1300, 420, 500, 32, PALE)}
{T("وقوانين زي حمورابي كانت محاولات لترويض الحياة العاطفية.", 1300, 680, 500, 28, MUTE, build="rise 1")}''', page="ص19")

# inverse — the inverse rule as an illustrative chart (not data)
ch = '<svg aria-label="رسم توضيحي: كل ما الانفعال يزيد، العقل المنطقي يضعف" width="900" height="560" viewBox="0 0 900 560" fill="none" stroke-linecap="round">'
ch += f'<rect x="470" y="20" width="420" height="470" fill="{RED}" opacity="0.12"/>'
ch += f'<line x1="60" y1="490" x2="890" y2="490" stroke="{DIM}" stroke-width="5"/><line x1="60" y1="490" x2="60" y2="20" stroke="{DIM}" stroke-width="5"/>'
ch += f'<path d="M 60 430 C 300 410 420 330 470 260 C 560 130 720 60 880 40" stroke="{AMB}" stroke-width="10"/>'
ch += f'<path d="M 60 90 C 300 110 420 190 470 260 C 560 390 720 450 880 470" stroke="{TEAL}" stroke-width="10"/>'
ch += f'<line x1="470" y1="20" x2="470" y2="490" stroke="{PALE}" stroke-width="4" stroke-dasharray="14 12"/>'
ch += f'<circle cx="470" cy="260" r="16" fill="{PALE}"/></svg>'
slide("inverse", f'''
{T("القاعدة · ص23–24", 470, 140, 1330, 30, AMB, 700)}
{T("كل ما الانفعال يعلى… التفكير يوطى", 470, 180, 1330, 84, PALE, disp=True)}
{SVG(ch, 900, 330)}
{T("العقل الانفعالي", 1560, 330, 260, 30, AMB, 700, align="left")}
{T("العقل المنطقي", 1560, 700, 260, 30, TEAL, 700, align="left")}
{T("ذروة التوازن", 1220, 290, 300, 28, PALE, 700, align="center")}
{T("شدة الانفعال ⟶", 960, 830, 840, 28, MUTE, align="center")}
{T("رسم توضيحي للفكرة · مش بيانات", 960, 870, 840, 22, DIM, align="center")}
{T("«كلما كانت المشاعر أكثر حدة… أصبح العقل المنطقي أقل فاعلية»", 470, 340, 400, 36, PALE, disp=True)}
{T("«فالمشاعر ضرورية للتفكير، والتفكير مهم للمشاعر»", 470, 580, 400, 30, TEAL, build="rise 1")}''', page="ص23–24")

# building — the brain as three floors
slide("building", f'''
{SVG(art.building(), 470, 300)}
{T("المخ اتبنى أدوار · ص25–28", 1180, 140, 620, 30, AMB, 700)}
{T("اللي بيفكر… اتبنى<br>فوق اللي بيحس", 1180, 190, 620, 76, PALE, disp=True)}
{T("القشرة الجديدة: تفكير وتخطيط… و«مشاعر عن مشاعرنا»", 1180, 420, 620, 32, TEAL, 600, build="rise 3")}
{T("الجهاز الحوفي: المشاعر · الأميجدالا هنا", 1180, 560, 620, 32, AMB, 600, build="rise 2")}
{T("جذع المخ: الأوتوماتيك · التنفس وضربات القلب", 1180, 700, 620, 32, MUTE, 600, build="rise 1")}
{T("وفي الطوارئ؟ المراكز العليا «تنزل عند إرادة الجهاز الحوفي» · ص28", 470, 920, 1330, 32, AMB, 700, build="rise 4")}''', page="ص25–28")

# flood — working memory freeze as an alarm flood
slide("flood", f'''
{SVG(art.alarm_flood(), 1200, 300)}
{T("الذاكرة العاملة · ص48–49", 470, 140, 700, 30, AMB, 700)}
{T("مش قادر<br>أفكر صح", 470, 190, 700, 110, PALE, disp=True)}
{T("الانفعال القوي بيشلّ المساحة اللي بتفكر فيها دلوقتي.", 470, 470, 680, 36, PALE)}
{T("تشبيه من عندنا: alarm flood. الشاشة تتملي أحمر… فماتعرفش تقرا ولا إنذار.", 470, 620, 680, 32, MUTE, build="rise 1")}
{T("عشان كده في الـreview وانت متضايق… بتنسى أوضح نقطة.", 470, 800, 1330, 34, AMB, 700, build="rise 2")}''', page="ص48–49")

ORDER = ["jolt", "meeting", "karim-reply", "who", "cover", "smart", "answer", "map", "aristotle", "specs",
         "ch1", "snow", "motion", "body", "legacy", "two-minds", "inverse", "building", "five-part",
         "ch2", "hijack", "small", "alarm", "two-roads", "fast-wrong", "old-alarm", "jessica", "two-forces", "flood",
         "two-layers", "replay", "body-map", "recap", "next", "end"]
assert sorted(ORDER) == sorted(slides) == sorted(SCRIPT), (set(slides) ^ set(ORDER), set(SCRIPT) ^ set(ORDER))
order[:] = ORDER

for sid, h in slides.items():
    (OUT / "slides" / f"{sid}.html").write_text(h, encoding="utf-8")
deck = json.loads((OUT / "deck.json").read_text(encoding="utf-8"))
deck["order"] = order
deck["faces"] = {"lalezar": {"family": "Lalezar", "href": "https://fonts.googleapis.com/css2?family=Lalezar&display=swap"},
                 "ibm-plex-sans-arabic": {"family": "IBM Plex Sans Arabic", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap"}}
(OUT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")
missing = sorted({k for k in ["brain_lateral", "brain_medial", "aristotle", "cajal", "vitruvian", "telephone"] if k not in A})
print(len(order), "slides · missing images:", missing)
