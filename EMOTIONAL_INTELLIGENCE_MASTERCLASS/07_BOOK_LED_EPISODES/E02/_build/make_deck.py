"""E02 «أنا ومشاعري» — same visual system as E01 v3.

- Speaker notes come from e02_script.py (SCRIPT dict); SCRIPT.md is generated from it.
- Images: public-domain files from Wikimedia Commons, processed (process_images.py), uploaded as assets;
  their /_blob urls live in assets.json. A missing image renders as an empty frame (alt kept).
- Webcam no-go zone: bottom-left (x < 440, y > 640). Breadcrumb sits top-left.
"""
import json, re, html, pathlib, datetime
import art
from e02_script import SCRIPT

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
    out = T("الحلقة 2 · أنا ومشاعري", 64, 56, 360, 24, c, align="left")
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




def node(x, y, w, h, t, col, fill, size=40):
    return BOX(x, y, w, h, fill, f"border:4px solid {col};border-radius:24px") + T(t, x, y + (h - size * 1.3) / 2, w, size, PALE, disp=True, align="center")


# ===================== HOOK =====================
cd = "".join(T(str(n), 600 + i * 240, 470, 240, 120, AMB, disp=True, align="center", build=f"pop {i + 1}") for i, n in enumerate((3, 2, 1)))
slide("name-it", f'''
{T("سؤال واحد:", 470, 200, 1330, 44, MUTE, 600, align="center")}
{T("إنت حاسس بإيه دلوقتي؟", 470, 270, 1330, 110, PALE, disp=True, align="center")}
{SVG(art.countdown(), 600, 430)}
{cd}
{T("في كلمة واحدة.", 470, 760, 1330, 44, AMB, 700, align="center")}
{T("«كويس»؟ «عادي»؟ «مش عارف»؟", 470, 840, 1330, 40, MUTE, align="center", build="fade 4")}''', bg="#05080D", crumbs=False)

slide("engineers", f'''
{T("كتاب تاني · Nonviolent Communication · L971", 470, 150, 1330, 30, "#E07A62", 700)}
{T("صعوبة إنك تعرف مشاعرك وتعبّر عنها شائعة…", 470, 210, 1330, 56, PALE, 600)}
{T("«خصوصًا عند المحامين، والمهندسين…»", 470, 330, 1330, 120, AMB, disp=True, build="rise 1")}
{T("…لأن قواعد شغلهم بتشجعهم إنهم مايظهروش مشاعر.", 470, 680, 1330, 40, MUTE, build="rise 2")}
{T("اتدربنا نقرا كل الحساسات… إلا اللي جوانا.", 470, 800, 1330, 52, PALE, disp=True, build="rise 3")}''', page="NVC")

slide("send", f'''
{SVG(art.laptop_send(), 470, 330)}
{T("مثال توضيحي · من آخر الحلقة 1", 1300, 150, 500, 26, MUTE)}
{T("2:00 بالليل", 1300, 200, 500, 64, AMB, disp=True)}
{T("«أنا بستقيل.»", 1300, 300, 500, 72, RED, disp=True)}
{T("لو سألته حاسس بإيه: «ولا حاجة… أنا بس أخدت قرار.»", 1300, 480, 500, 36, PALE, build="rise 1")}
{T("قرار؟<br>ولا إحساس لابس بدلة قرار؟", 1300, 700, 500, 48, AMB, disp=True, build="rise 2")}''', page="مثال")

slide("question", f'''
{IMG("brain_lateral", 900, 80, 1000, 920, "contain", "opacity:0.18", "مخ")}
{T("الإيميل هيتبعت ولا لأ… بيتوقف على حاجة واحدة:", 470, 200, 1330, 50, "#3A2405", 700)}
{T("كريم يعرف هو<br>حاسس بإيه؟", 470, 290, 1330, 180, INK, disp=True)}
{T("① تعرفه وهو بيحصل   ② لا تكتمه ولا تفرّغه   ③ تخليه وقود", 470, 820, 1330, 40, "#3A2405", 700, build="rise 1")}''', bg=AMB, page="السؤال", dark=False)

slide("cover", f'''
{IMG("brain_medial", 0, 0, 1920, 1080, "cover", "opacity:0.5", "رسم تشريحي قديم للمخ (Gray's Anatomy)")}
{BOX(0, 0, 1920, 1080, "linear-gradient(90deg, rgba(14,21,34,0.2) 0%, rgba(14,21,34,0.92) 55%)")}
{T("من كتاب «الذكاء العاطفي» · دانييل جولمان", 760, 250, 1040, 34, AMB, 700)}
{T("إنت حاسس<br>بإيه… بجد؟", 760, 320, 1040, 168, PALE, disp=True)}
{T("الحلقة 2 · أنا ومشاعري", 760, 740, 1040, 48, MUTE, 600)}
{T("الفصل 3 · الفصل 4 · الفصل 5 · الفصل 6", 760, 810, 1040, 32, AMB)}''')

eps = [("E1", "المخ الانفعالي"), ("E2", "أنا ومشاعري"), ("E3", "أنا والناس"), ("E4", "البيت والشغل"), ("E5", "الفرص المتاحة"), ("E6", "محو الأمية العاطفية")]
xs = [1580, 1360, 1140, 920, 700, 480]
mp = BOX(1020, 270, 360, 120, "#1E2B44", "border:3px solid " + AMB + ";border-radius:24px")
mp += T("«الذكاء العاطفي»", 1020, 292, 360, 48, PALE, disp=True, align="center")
mp += BOX(560, 470, 1280, 4, DIM) + BOX(1198, 390, 4, 80, DIM)
for (i, t), x in zip(eps, xs):
    on, done = i == "E2", i == "E1"
    mp += BOX(x + 98, 470, 4, 60, DIM)
    mp += (f'<div style="position:absolute;left:{x}px;top:530px;width:200px;height:200px;border-radius:24px;'
           f'background:{AMB if on else "#16223A"};border:3px solid {AMB if on else (TEAL if done else DIM)}"></div>')
    mp += T(i + (" ✓" if done else ""), x, 560, 200, 30, INK if on else (TEAL if done else MUTE), 700, align="center")
    mp += T(t, x + 10, 610, 180, 34, INK if on else PALE, disp=True, align="center")
slide("map", f'''
{T("إحنا هنا", 470, 150, 1330, 56, PALE, disp=True)}
{mp}
{T("ف3 عندما يخون الذكاء · ف4 اعرف نفسك · ف5 عبيد العاطفة · ف6 القدرة المسيطرة", 470, 800, 1330, 34, MUTE)}''', page="الخريطة")

five = [("1", "تعرف عواطفك", True), ("2", "تديرها", True), ("3", "تحفّز نفسك", True), ("4", "تتعرف على عواطف غيرك", False), ("5", "تدير علاقاتك", False)]
fv = ""
for i, (n, t, on) in enumerate(five):
    x = 1540 - i * 266
    fv += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:{x}px;top:330px;width:246px;height:330px;background:{"#3A2A10" if on else "#16223A"};border-radius:22px;border-top:12px solid {AMB if on else DIM}"></div>'
    fv += T(n, x, 360, 246, 96, AMB if on else MUTE, disp=True, align="center", build=f"rise {i + 1}")
    fv += T(t, x + 16, 500, 214, 40, PALE, disp=True, align="center", build=f"rise {i + 1}")
slide("five", f'''
{T("الفصل 3 · تعريف سالوفي · ص67–68", 470, 140, 1330, 30, AMB, 700)}
{T("الذكاء العاطفي = 5 قدرات", 470, 180, 1330, 84, PALE, disp=True)}
{fv}
{T("كل واحدة مبنية على اللي قبلها", 470, 700, 1330, 36, MUTE)}
{T("النهارده: 1 و2 و3 · الحلقة الجاية: 4 و5", 470, 770, 1330, 40, AMB, 700, build="fade 6")}
{T("«مجموعة من العادات… ومن الممكن أن تتحسن مع بذل الجهد المناسب» · ص68", 470, 850, 1330, 30, PALE, build="fade 6")}''', page="ص67–68")

# ===================== CH4 =====================
slide("ch4", f'''
{IMG("socrates", 470, 0, 720, 1080, "cover", "", "تمثال رأس سقراط (متحف اللوفر)")}
{BOX(470, 0, 720, 1080, "linear-gradient(90deg, rgba(14,21,34,0) 60%, rgba(14,21,34,1) 100%)")}
{T("الفصل 4 · ص72", 1230, 380, 570, 40, AMB, 700)}
{T("«اعرف نفسك»", 1230, 440, 570, 150, PALE, disp=True)}
{T("وصية سقراط… وحجر الزاوية في الذكاء العاطفي", 1230, 820, 570, 34, MUTE)}''', page="ص72", transition="push")

slide("samurai", f'''
{SVG(art.katana(), 470, 420)}
{T("حكاية من أول الفصل · ص72", 470, 140, 1330, 30, AMB, 700)}
{T("ساموراي، وراهب، وسؤال عن الجنة والنار", 470, 180, 1330, 64, PALE, disp=True)}
{T("السيف بيتسحب…", 1300, 330, 500, 34, MUTE)}
{T("«هذا تمامًا هو الجحيم»", 1300, 390, 500, 64, RED, disp=True, build="rise 1")}
{T("السيف بيرجع لجرابه…", 1300, 640, 500, 34, MUTE, build="rise 2")}
{T("«وهذه هي الجنة»", 1300, 700, 500, 64, TEAL, disp=True, build="rise 2")}
{T("الفرق: إنه شاف نفسه وهو غضبان.", 470, 900, 1330, 40, AMB, 700, build="rise 3")}''', page="ص72")

slide("observer", f'''
{SVG(art.observer(), 470, 330)}
{T("الوعي بالذات · «الذات المراقبة» · ص73–74", 1230, 140, 570, 30, AMB, 700)}
{T("جزء منك<br>بيتفرج", 1230, 190, 570, 96, PALE, disp=True)}
{T("غضبان جدًا…", 1230, 470, 570, 40, AMB, 600)}
{T("مقابل", 1230, 530, 570, 30, MUTE)}
{T("«أنا حاسس بالغضب»… وانت لسه غضبان", 1230, 580, 570, 48, TEAL, disp=True, build="rise 1")}
{T("يعني: أول خطوة للسيطرة على الانفعال · ص74", 1230, 760, 570, 34, PALE, 600, build="rise 2")}''', page="ص73–74")

gg = ""
for i, (lbl, v, c) in enumerate((("إهانة", 80, RED), ("إحراج", 70, AMB), ("خوف على شكله", 50, "#6E95D8"))):
    x = 1460 - i * 360
    gg += SVG(art.gauge(v, c), x, 640, build=f"pop {i + 4}")
    gg += T(f"{lbl} {v}", x, 830, 320, 34, PALE, 700, align="center", build=f"pop {i + 4}")
slide("name-rate", f'''
{T("سمّيه صح · من الكتب التانية", 470, 140, 1330, 30, AMB, 700)}
{T("مش «مضايق»… سمّيه وادّيله رقم", 470, 180, 1330, 72, PALE, disp=True)}
<div data-build-in="rise 1" style="position:absolute;left:1360px;top:300px;width:440px;height:290px;background:#16223A;border-radius:20px;border-top:8px solid #E07A62"></div>
{T("NVC · L997", 1380, 320, 400, 26, "#E07A62", 700, build="rise 1")}
{T("«حاسس إنك مش مهتم»<br>= فكرة، مش شعور", 1380, 370, 400, 36, PALE, build="rise 1")}
<div data-build-in="rise 2" style="position:absolute;left:900px;top:300px;width:440px;height:290px;background:#16223A;border-radius:20px;border-top:8px solid #6E95D8"></div>
{T("CC · p.103–104", 920, 320, 400, 26, "#6E95D8", 700, build="rise 2")}
{T("ناس كتير «أميين عاطفيًا»: يقولوا «زعلان» وهما حاسين إحراج ومفاجأة", 920, 370, 400, 32, PALE, build="rise 2")}
<div data-build-in="rise 3" style="position:absolute;left:470px;top:300px;width:410px;height:290px;background:#16223A;border-radius:20px;border-top:8px solid #3FA796"></div>
{T("MoM · p.25–30", 490, 320, 370, 26, "#3FA796", 700, build="rise 3")}
{T("سمّيه بكلمة… وادّيله رقم من 0 لـ100", 490, 370, 370, 36, PALE, build="rise 3")}
{gg}
{T("كريم الساعة 2 · مثال", 470, 900, 1330, 26, MUTE, build="pop 6")}''', page="أدوات")

slide("styles", f'''
{SVG(art.swimmers(), 820, 330)}
{T("جون ماير · ص75", 470, 140, 1330, 30, AMB, 700)}
{T("3 طرق نتعامل بيها مع مشاعرنا", 470, 180, 1330, 76, PALE, disp=True)}
{T("الواعي", 1540, 660, 260, 48, TEAL, disp=True, align="center", build="rise 1")}
{T("عارف وهو بيحس… وبيطلع بسرعة", 1520, 730, 300, 30, PALE, align="center", build="rise 1")}
{T("الغرقان", 1180, 660, 260, 48, RED, disp=True, align="center", build="rise 2")}
{T("المشاعر بلعته… ومش قادر يطلع", 1160, 730, 300, 30, PALE, align="center", build="rise 2")}
{T("المتقبّل", 820, 660, 260, 48, MUTE, disp=True, align="center", build="rise 3")}
{T("شايفها… وسايبها زي ما هي", 800, 730, 300, 30, PALE, align="center", build="rise 3")}
{T("وانت؟", 470, 420, 300, 72, AMB, disp=True, build="rise 4")}''', page="ص75")

slide("elliot", f'''
{SVG(art.calendar(), 470, 330)}
{T("قصة إليوت · أنطونيو داماسيو · ص80–82", 1060, 140, 740, 30, AMB, 700)}
{T("ذكاء سليم…<br>من غير مشاعر", 1060, 190, 740, 84, PALE, disp=True)}
{T("محامي ناجح. ورم صغير ورا الجبهة اتشال. اختبارات الذكاء والذاكرة: سليمة.", 1060, 420, 740, 34, PALE)}
{T("بس ماعرفش يختار ميعاد الزيارة الجاية.", 1060, 580, 740, 44, AMB, disp=True, build="rise 1")}
{T("المشاعر مش ضد التفكير… هي جزء من آلة القرار.", 1060, 760, 740, 40, TEAL, 700, build="rise 2")}''', page="ص80–82")

# ===================== CH5 =====================
slide("ch5", f'''
{IMG("cajal", 0, 0, 1920, 1080, "cover", "opacity:0.55", "رسم خلايا عصبية لسانتياغو رامون إي كاخال")}
{BOX(0, 0, 1920, 1080, "linear-gradient(0deg, rgba(14,21,34,0.95) 25%, rgba(14,21,34,0.35) 100%)")}
{T("القسم الثاني · طبيعة الذكاء العاطفي", 470, 470, 1330, 40, AMB, 700)}
{T("الفصل 5", 470, 530, 1330, 64, MUTE, disp=True)}
{T("عبيد العاطفة", 470, 610, 1330, 160, PALE, disp=True)}
{T("ص86", 470, 830, 1330, 36, MUTE)}''', page="ص86", transition="push")

slide("balance", f'''
{T("الهدف · ص86", 470, 140, 1330, 30, AMB, 700)}
{T("«تحقيق التوازن العاطفي وليس قمع العاطفة»", 470, 180, 1330, 76, PALE, disp=True)}
{T("…لأن لكل شعور قيمته ودلالته", 470, 390, 1330, 40, MUTE)}
{SVG(art.slider(), 490, 500)}
{T("كبت ← فتور وعزلة", 1460, 660, 340, 34, "#6E95D8", 700, align="center")}
{T("توازن", 870, 545, 180, 40, PALE, disp=True, align="center")}
{T("انجراف ← حالة مرضية", 470, 660, 400, 34, RED, 700, align="center")}
{chip("CC", 470, 760, 1330, "أحسن ناس في الحوار مش رهاين لمشاعرهم… ولا بيخبّوها ويكتموها.", "p.96–97")}''', page="ص86")

slide("duration", f'''
{SVG(art.duration(), 860, 360)}
{T("جملة من أهم جمل الحلقة · ص88", 470, 140, 1330, 30, AMB, 700)}
{T("مش في إيدك إمتى الموجة تضرب…", 470, 180, 1330, 72, PALE, disp=True)}
{T("بس في إيدك<br>تفضل فيها<br>قد إيه", 470, 360, 360, 72, TEAL, disp=True, build="rise 1")}
{T("هنا ضربت", 900, 330, 260, 26, MUTE)}
{T("دقيقة؟", 1240, 600, 240, 34, TEAL, 700, build="rise 1")}
{T("ولا ليلة كاملة؟", 1500, 450, 300, 34, AMB, 700, build="rise 1")}
{T("كريم مااختارش إن «شغل عيال» توجعه… بس هو اللي فضل يعيدها لحد الساعة 2.", 470, 860, 1330, 34, PALE, build="rise 2")}''', page="ص88")

slide("cascade", f'''
{SVG(art.cascade(), 860, 330)}
{T("دولف زيلمان · ص91–94", 470, 140, 1330, 30, AMB, 700)}
{T("«وهكذا يُبنى الغضب على غضب»", 470, 180, 1330, 76, PALE, disp=True)}
{T("كل فكرة مستفزة = دفعة هرمونات… والتانية بتركب على الأولى.", 470, 330, 370, 30, PALE)}
{T("① «شغل عيال»", 470, 480, 370, 32, AMB, 700, build="rise 1")}
{T("② «قدام الكل»", 470, 540, 370, 32, AMB, 700, build="rise 2")}
{T("③ «دايمًا كده»", 470, 600, 370, 32, AMB, 700, build="rise 3")}
{T("④ «مش بيحترمني»", 470, 660, 370, 32, RED, 700, build="rise 4")}
{T("الخط الأحمر: التسامح يختفي", 1340, 290, 460, 28, RED, 600, align="left", build="rise 5")}
{T("الصوت اللي جواك بيملا دماغك «بالذرائع المقنعة» · ص91", 470, 860, 1330, 32, MUTE)}''', page="ص91–94")

slide("cyclist", f'''
{SVG(art.bicycle(), 470, 330)}
{T("تجربة زيلمان · ص94–95", 1130, 140, 670, 30, AMB, 700)}
{T("معلومة واحدة<br>طفّت الغضب", 1130, 190, 670, 84, PALE, disp=True)}
{T("واحد قليل الأدب استفزهم… وجت فرصة ينتقموا منه.", 1130, 410, 670, 32, PALE)}
{T("«ده تحت ضغط رهيب… عنده امتحان تخرج قريب»", 1130, 500, 670, 40, TEAL, disp=True, build="rise 1")}
{T("النتيجة: اتنازلوا عن الانتقام.", 1130, 620, 670, 36, PALE, 700, build="rise 1")}
{T("بس في الغضب المتوسط بس. في القمة: «عجز معرفي».", 1130, 720, 670, 32, RED, 600, build="rise 2")}
{T("مثال: لو كريم عرف إن أ. هشام نفسه اتبهدل قدام الإدارة قبل الاجتماع بساعة؟", 470, 880, 1330, 30, AMB, build="rise 3")}''', page="ص94–95")

slide("vent", f'''
{SVG(art.vent(), 470, 300)}
{T("خرافة التنفيس · ص97–98", 1060, 140, 740, 30, AMB, 700)}
{T("«طلّع اللي جواك»؟", 1060, 190, 740, 84, PALE, disp=True)}
{T("سواق تاكسي في نيويورك: «كل اللي تقدر تعمله إنك تزعق… تنفّس عن نفسك»", 1060, 330, 740, 32, PALE)}
{T("تايس: التنفيس أسوأ وسيلة للتهدئة… الغضب بيزيد.", 1060, 470, 740, 36, RED, 700, build="rise 1")}
{T("«لا تقهره… ولكن إياك أيضًا أن تطيعه»", 470, 720, 1330, 72, TEAL, disp=True, build="rise 2")}
{T("تشوجيام ترونجبا، معلم من التبت، كما ينقل جولمان · ص98", 470, 860, 1330, 28, MUTE, build="rise 2")}''', page="ص97–98")

tools = [("امسكه بدري", "التهدئة في أوله أنجح حاجة · ص98"), ("ابعد شوية", "لوحدك، أو اتمشى · ص96"),
         ("اشغل دماغك", "مش بالأكل ولا الشوبينج · ص97"), ("اكتبه على ورق", "وأعد تقييمه · ردفورد ويليامز ص97"), ("وبعدين واجه", "بشكل بنّاء عشان تنهوا الخلاف · ص98")]
tb = ""
for i, (a, b) in enumerate(tools):
    y = 300 + i * 118
    tb += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:470px;top:{y}px;width:1330px;height:100px;background:#16223A;border-radius:18px;border-right:12px solid {TEAL}"></div>'
    tb += T(str(i + 1), 1700, y + 14, 80, 56, TEAL, disp=True, align="center", build=f"rise {i + 1}")
    tb += T(a, 1180, y + 20, 500, 44, PALE, disp=True, build=f"rise {i + 1}")
    tb += T(b, 500, y + 30, 660, 30, MUTE, build=f"rise {i + 1}")
slide("cool", f'''
{T("لا تكتمه ولا تطيعه… أمال إيه؟", 470, 140, 1330, 30, AMB, 700)}
{T("صندوق أدوات الكتاب", 470, 180, 1330, 76, PALE, disp=True)}
{tb}''', page="ص96–98")

# ===================== CH6 =====================
slide("ch6", f'''
{IMG("brain_medial", 760, 0, 1160, 1080, "cover", "opacity:0.55", "مقطع في المخ (Gray's Anatomy)")}
{BOX(0, 0, 1920, 1080, "linear-gradient(90deg, rgba(14,21,34,0.25) 0%, rgba(14,21,34,0.95) 60%)")}
{T("القسم الثاني · طبيعة الذكاء العاطفي", 470, 380, 1330, 40, AMB, 700)}
{T("الفصل 6", 470, 440, 1330, 64, MUTE, disp=True)}
{T("القدرة<br>المسيطرة", 470, 520, 1330, 150, PALE, disp=True)}
{T("المشاعر: عائق للتفكير… أو وقوده · ص116", 470, 880, 1330, 36, MUTE)}''', page="ص116", transition="push")

slide("exam", f'''
{SVG(art.exam(), 520, 300)}
{T("اعتراف جولمان · ص116–118", 1130, 140, 670, 30, AMB, 700)}
{T("امتحان الحساب…<br>والتجمّد", 1130, 190, 670, 84, PALE, disp=True)}
{T("قلبه بيدق في ودنه. معدته متوترة. فتح الكراسة الزرقا… وماعرفش يكتب حاجة.", 1130, 420, 670, 34, PALE)}
{T("الانزعاج الانفعالي «يشل» قدرة المخ على التفكير", 1130, 620, 670, 40, RED, disp=True, build="rise 1")}
{T("السبب: الذاكرة العاملة · ص118", 1130, 760, 670, 32, MUTE, build="rise 1")}''', page="ص116–118")

slide("inverted-u", f'''
{SVG(art.inverted_u(), 860, 330)}
{T("منحنى U مقلوب · ص125–126", 470, 140, 1330, 30, AMB, 700)}
{T("القلق مش دايمًا عدوك", 470, 180, 1330, 76, PALE, disp=True)}
{T("قليل أوي: لامبالاة", 860, 750, 300, 30, MUTE, 700, align="center")}
{T("معتدل: أحسن أداء", 1160, 290, 300, 32, TEAL, 700, align="center", build="rise 1")}
{T("كتير أوي: بيدمّر الأداء", 1500, 750, 300, 30, RED, 700, align="center")}
{T("الأداء", 860, 330, 200, 26, MUTE, align="left")}
{T("القلق ⟶", 860, 800, 940, 26, MUTE, align="center")}
{T("تشبيه من عندنا: الـdeadline اللي بيصحيك وتركّز… مقابل اللي مش مخليك تبدأ.", 470, 380, 360, 32, PALE, build="rise 2")}''', page="ص125–126")

slide("marshmallow", f'''
{SVG(art.marshmallow(), 470, 330)}
{T("لو استنيت", 470, 680, 450, 36, TEAL, 700, align="center")}
{T("دلوقتي", 960, 680, 230, 36, AMB, 700, align="center")}
{T("والتر ميشيل · الستينات · ص120–123", 1230, 140, 570, 30, AMB, 700)}
{T("قطعة دلوقتي…<br>ولا اتنين بعدين؟", 1230, 190, 570, 76, PALE, disp=True)}
{T("اللي استنوا: غطّوا عينيهم، كلموا نفسهم، غنّوا، حاولوا يناموا.", 1230, 400, 570, 34, PALE, build="rise 1")}
{T("ماكانتش إرادة وبس… كانت حيل.", 1230, 560, 570, 44, TEAL, disp=True, build="rise 1")}
{T("تنبيه: إعادة التجربة بعد الكتاب على عينات أكبر لقت العلاقة بالمستقبل أضعف بكتير، وظروف الطفل ليها دور كبير.", 470, 820, 1330, 30, AMB, 600, build="rise 2")}''', page="ص120–123")

slide("metlife", f'''
{SVG(art.phone_no(), 470, 300)}
{T("مارتن سليجمان وشركة «ميتلايف» · ص132", 900, 140, 900, 30, AMB, 700)}
{T("شغلانة مليانة «لأ»", 900, 190, 900, 84, PALE, disp=True)}
{T("¾ المندوبين بيسيبوا الشغل في أول 3 سنين", 900, 320, 900, 34, MUTE)}
{T("37%", 1500, 420, 300, 110, TEAL, disp=True, align="center", build="rise 1")}
{T("زيادة مبيعات المتفائلين في أول سنتين", 1500, 560, 300, 28, PALE, align="center", build="rise 1")}
{T("الضعف", 1160, 420, 300, 110, RED, disp=True, align="center", build="rise 2")}
{T("عدد المتشائمين اللي سابوا الشغل", 1160, 560, 300, 28, PALE, align="center", build="rise 2")}
{T("57%", 900, 420, 240, 110, AMB, disp=True, align="center", build="rise 3")}
{T("زيادة في السنة التانية (21% في الأولى) لمتفائلين سقطوا في اختبار التوظيف", 900, 560, 240, 26, PALE, align="center", build="rise 3")}
{T("اللي بيفرق: هتعمل إيه في المكالمة اللي بعدها.", 900, 760, 900, 40, PALE, disp=True, build="rise 4")}''', page="ص132")

slide("explain", f'''
{SVG(art.bubbles(), 860, 320)}
{T("التفاؤل عند سليجمان · ص131", 470, 140, 1330, 30, AMB, 700)}
{T("التفاؤل = طريقة تفسيرك للفشل", 470, 180, 1330, 76, PALE, disp=True)}
{T("«أنا فاشل في ده»", 880, 380, 420, 44, PALE, disp=True, align="center")}
{T("صفة دايمة… مش هتتغير", 880, 460, 420, 28, RED, 700, align="center")}
{T("«التصميم محتاج زاوية تانية»", 1380, 380, 400, 34, PALE, disp=True, align="center")}
{T("حاجة أقدر أغيّرها", 1380, 460, 400, 28, TEAL, 700, align="center")}
{T("تفاؤل واقعي، مش ساذج · ص130", 470, 380, 360, 32, AMB, 700, build="rise 1")}
{T("والتفاؤل والأمل بيتعلموا · ص133", 470, 500, 360, 32, TEAL, 700, build="rise 1")}
{chip("MoM", 860, 680, 940, "نفس الموقف… بأفكار مختلفة… بيطلّع مشاعر مختلفة.", "p.16")}''', page="ص130–133")

slide("flow", f'''
{SVG(art.stream(), 470, 560)}
{T("ميهالي تشيكسنتميهالي · ص133–134", 470, 140, 1330, 30, AMB, 700)}
{T("التدفق", 470, 180, 1330, 110, PALE, disp=True)}
{T("تنسى الوقت… والشغل كأنه طالع لوحده.", 470, 330, 1330, 40, PALE)}
{T("متسلقين جبال، أبطال شطرنج، جراحين… ومهندسين.", 470, 400, 1330, 34, MUTE)}
{T("«فهذا هو الذكاء العاطفي في أحسن حالاته»", 470, 920, 1330, 44, TEAL, disp=True, build="rise 1")}''', page="ص133–134")

# ===================== PAYOFF =====================
steps = [("سمّى", "إهانة · إحراج · خوف… مش «قرار»", AMB), ("لا كتم ولا تنفيس", "Save مش Send: مسودة", TEAL),
         ("سابها لبكرة", "قفل اللابتوب ونام", TEAL), ("الصبح", "عرف إن هشام اتبهدل قبل الاجتماع", "#6E95D8"), ("واجه بهدوء", "«ممكن عشر دقايق؟»", TEAL)]
st = ""
for i, (a, b, c) in enumerate(steps):
    y = 300 + i * 120
    st += f'<div data-build-in="rise {i + 1}" style="position:absolute;left:1260px;top:{y}px;width:540px;height:104px;background:#16223A;border-radius:18px;border-right:12px solid {c}"></div>'
    st += T(a, 1280, y + 12, 490, 40, c, disp=True, build=f"rise {i + 1}")
    st += T(b, 1280, y + 60, 490, 28, PALE, build=f"rise {i + 1}")
slide("karim-draft", f'''
{SVG(art.laptop_draft(), 470, 380)}
{T("كريم، الساعة 2 · مثال", 470, 140, 1330, 30, AMB, 700)}
{T("نطبّق اللي اتعلمناه", 470, 180, 1330, 76, PALE, disp=True)}
{T("الإيميل في المسودات", 470, 820, 680, 30, TEAL, 700, align="center")}
{st}''', page="الإجابة")

slide("exercise", f'''
{T("تمرين · 30 ثانية", 470, 140, 1330, 30, AMB, 700)}
{T("إنت حاسس بإيه دلوقتي؟ تاني.", 470, 180, 1330, 76, PALE, disp=True)}
{T("1 · تلات كلمات… ومن غير «كويس»", 1100, 340, 700, 38, PALE, 600)}
{T("2 · ادّي كل كلمة رقم من 0 لـ100", 1100, 430, 700, 38, PALE, 600)}
{T("3 · «حاسس إن…»؟ غالبًا دي فكرة", 1100, 520, 700, 38, PALE, 600)}
{SVG(art.gauge(60, AMB), 640, 360)}
{T("✎ اكتب كلماتك على الشاشة", 470, 780, 1330, 34, AMB)}''', page="تمرين")

rc = [("1", "اعرفه وهو بيحصل", "ص74", AMB), ("2", "لا تقهره… ولا تطعه", "ص88، 98", TEAL), ("3", "خليه وقود", "ص126، 131، 134", "#6E95D8")]
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
{T("+ عرفت تسمّي إحساسك بتلات كلمات وأرقام", 470, 820, 1330, 40, AMB, 700)}''', bg=INK2, page="الخلاصة")

slide("next", f'''
{IMG("vitruvian", 470, 220, 560, 700, "contain", "opacity:0.35", "الرجل الفيتروفي")}
{T("الحلقة الجاية · أنا والناس", 1100, 140, 700, 32, AMB, 700)}
{T("كريم عرف هو حاسس بإيه…", 1100, 200, 700, 64, PALE, disp=True)}
{T("بس أ. هشام، الصبح ده،<br>كان حاسس بإيه؟", 1100, 360, 700, 72, AMB, disp=True, build="rise 1")}
{T("إزاي تقرا اللي جوه غيرك… من غير ما يقولك؟", 1100, 640, 700, 44, PALE, 600, build="rise 2")}''', page="الحلقة 3")

slide("end", f'''
{IMG("cajal", 0, 0, 1920, 1080, "cover", "opacity:0.25", "خلايا عصبية (كاخال)")}
{T("اكتبلي في التعليقات:", 470, 260, 1330, 56, MUTE, 600)}
{T("تلات كلمات<br>وصفت إحساسك", 470, 340, 1330, 130, AMB, disp=True)}
{T("وأرقامهم كام؟ ولو كتبت «حاسس إن…»… هقولك شعور ولا فكرة.", 470, 720, 1330, 40, PALE)}
{T("صور: Wikimedia Commons (كاخال، Gray's Anatomy، دافنشي: ملكية عامة · سقراط: Eric Gaba، CC BY-SA 2.5) · المصدر: جولمان، «الذكاء العاطفي»، عالم المعرفة 262", 470, 900, 1330, 24, MUTE)}''', page="النهاية")

assert sorted(order) == sorted(SCRIPT), set(order) ^ set(SCRIPT)
for f in (OUT / "slides").glob("*.html"):
    if f.stem not in slides:
        f.unlink()
for sid, h in slides.items():
    (OUT / "slides" / f"{sid}.html").write_text(h, encoding="utf-8")
deck = json.loads((OUT / "deck.json").read_text(encoding="utf-8"))
deck["order"] = order
(OUT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(order), "slides · missing images:", sorted({"cajal", "brain_lateral", "brain_medial", "vitruvian", "socrates"} - set(A)))
