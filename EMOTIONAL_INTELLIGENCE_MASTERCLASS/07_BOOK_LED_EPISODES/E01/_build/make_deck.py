"""E01 «المخ الانفعالي» — slide deck for screen-recording (presenter webcam circle bottom-left, pen annotations).

Writes ../deck/project/deck.json + ../deck/project/slides/<id>.html (Slides artifact type format).
Speaker notes (<aside>) = the spoken script (Egyptian Arabic) + ✎ pen cues + sources.
Sources: Goleman Arabic ed. (عالم المعرفة 262) pages verified against 00_SOURCE_AUDIT/notes/GOL_notes.md and the upload file;
cross-book refs from 06_BOOK_MAP/_build/goleman_map_data.py.
"""
import json, pathlib, datetime, html

OUT = pathlib.Path(__file__).resolve().parent.parent / "deck" / "project"
(OUT / "slides").mkdir(parents=True, exist_ok=True)

# palette: blueprint navy + paper, amber = alarm (amygdala), teal = thinking brain (cortex)
PAPER, INK, BODY, LINE = "#F3F4EF", "#172131", "#475262", "#D5D8CF"
NAVY, NT, NB = "#0F1B2D", "#EEF2F6", "#B8C4D2"
AMB, AMBT = "#E39B2F", "#A35F00"
TEAL, TEALT, TEALL = "#2D8C85", "#1F6E68", "#62C6BB"
BOOK = {"MoM": ("#2F8A7E", "Mind Over Mood"), "CC": ("#3A64A8", "Crucial Conversations"),
        "NVC": ("#C4553D", "Nonviolent Communication"), "KZ": ("#7A5AA6", "Kabat-Zinn")}
DISP = "font-family:'Reem Kufi', Tahoma, sans-serif"
TXT = "font-family:'IBM Plex Sans Arabic', Tahoma, sans-serif"
PAD = "padding:112px 128px 112px 480px"   # left 480px = webcam strip (circle bottom-left)

slides, order = {}, []


def esc(s):
    return html.escape(s, quote=True)


def p(t, size=32, color=None, weight=400, extra="", font=TXT, tag="p"):
    c = f"color:{color};" if color else ""
    return f'<{tag} style="{font};font-size:{size}px;font-weight:{weight};{c}text-align:right;line-height:1.45;{extra}">{t}</{tag}>'


def h(t, size=80, color=None, extra=""):
    return p(t, size, color, 700, "line-height:1.2;" + extra, DISP, "h2")


def chrome(dark, crumb, page=None):
    c = NB if dark else BODY
    out = f'<p style="{TXT};position:absolute;left:64px;top:64px;width:340px;font-size:24px;color:{c};text-align:left">{crumb}</p>'
    if page:
        out += f'<p style="{TXT};position:absolute;left:64px;top:112px;width:340px;font-size:28px;font-weight:600;color:{AMB if dark else AMBT};text-align:left">{page}</p>'
    out += f'<div style="position:absolute;left:432px;top:112px;width:2px;height:856px;background:{"#24344D" if dark else LINE}"></div>'
    return out


def chip(book, text, ref, dark=False):
    col, name = BOOK[book]
    bg = "#16263D" if dark else "#FFFFFF"
    tc = NT if dark else INK
    return (f'<div style="display:flex;flex-direction:column;gap:8px;background:{bg};border:2px solid {col};border-radius:16px;padding:24px 32px">'
            f'{p(f"من كتاب تاني · <b>{name}</b> · {ref}", 24, col, 600)}{p(text, 32, tc)}</div>')


def slide(sid, body, notes, dark=False, crumb="الحلقة 1 · المخ الانفعالي", page=None, layout=None, transition="fade"):
    bg = NAVY if dark else PAPER
    fg = NT if dark else INK
    lay = layout or "display:flex;flex-direction:column;justify-content:center;gap:40px"
    notes = " ".join(notes.split())
    assert len(notes) <= 4000, (sid, len(notes))
    slides[sid] = (f'<section id="{sid}" data-transition="{transition}" style="background:{bg};color:{fg};{TXT};{PAD};{lay}">'
                   f'{chrome(dark, crumb, page)}{body}<aside>{esc(notes)}</aside></section>')
    order.append(sid)


# ---------------------------------------------------------------- 1 cover
slide("cover", f'''
{p("من كتاب «الذكاء العاطفي» · دانييل جولمان", 32, AMB, 600)}
{h("ليه بترد قبل ما تفكر؟", 120, NT)}
{p("الحلقة 1 · المخ الانفعالي", 44, NB, 500)}
<div style="display:flex;flex-direction:row-reverse;gap:16px;flex-wrap:wrap">
{p("المقدمة · ص7", 28, NB, 500, "background:#16263D;border-radius:40px;padding:8px 24px")}
{p("الفصل 1 · ص17", 28, NB, 500, "background:#16263D;border-radius:40px;padding:8px 24px")}
{p("الفصل 2 · ص31", 28, NB, 500, "background:#16263D;border-radius:40px;padding:8px 24px")}
</div>''', """
[قبل التسجيل: الدايرة بتاعة الكاميرا تحت على الشمال؛ الشريط الشمال كله محجوز ليك.]
أهلًا بيك. السلسلة دي ماشية على كتاب واحد: «الذكاء العاطفي» لدانييل جولمان، الترجمة العربية بتاعة عالم المعرفة. وهنفتح معاه كتب تانية كل ما تيجي فكرة متصلة بيها.
النهارده الحلقة الأولى، وسؤالها بسيط جدًا: ليه ساعات بترد قبل ما تفكر؟
✎ القلم: ارسم دايرة حوالين «قبل ما تفكر».
""", dark=True, crumb="رحلة الذكاء العاطفي")

# ---------------------------------------------------------------- 2 meeting
slide("meeting", f'''
{p("مثال توضيحي · الأسماء من تأليفنا", 24, NB, 500)}
{p("اجتماع التنسيق الأسبوعي · 10:05 ص · 8 حاضرين", 32, NB)}
<div style="display:flex;flex-direction:column;gap:16px;background:#16263D;border-radius:24px;padding:48px">
{p("أ. هشام — مدير المكتب الفني", 28, AMB, 600)}
{h("«مين عامل الشيت ده؟ ده شغل عيال.»", 72, NT)}
</div>
{p("كريم — مهندس مدني، هو اللي عامل الشيت", 32, NB)}''', """
خليني أحكيلك موقف. ده مثال من تأليفنا، بس أي حد اشتغل في مكتب فني أو موقع هيعرفه كويس.
كريم، مهندس مدني، في اجتماع التنسيق الأسبوعي. تمانية قاعدين. أ. هشام، مدير المكتب الفني، ماسك الشيت، ويقول قدام الكل: «مين عامل الشيت ده؟ ده شغل عيال.»
(وقفة)
الشيت ده بتاع كريم.
✎ القلم: خط تحت «شغل عيال».
""", dark=True)

# ---------------------------------------------------------------- 3 karim reply
slide("karim-reply", f'''
<div style="display:flex;flex-direction:column;gap:12px;background:{AMB};border-radius:24px;padding:40px 48px">
{p("كريم — في أقل من ثانيتين", 28, NAVY, 600)}
{h("«حضرتك لو كنت قريت الإيميل كنت عرفت إن…»", 64, NAVY)}
</div>
{h("صمت.", 96, NT, "letter-spacing:4px")}
{p("وبعد الاجتماع، لنفسه: «أنا ماكنتش عايز أقول كده.»", 40, NB)}''', """
وكريم؟ في أقل من ثانيتين، وقبل ما يلحق يفكر، رد: «حضرتك لو كنت قريت الإيميل كنت عرفت إن…»
(سكوت تقيل — اسكت انت كمان ثانيتين)
الاجتماع كله سكت.
وبعد ما خلص، كريم قاعد لوحده بيقول لنفسه: «أنا ماكنتش عايز أقول كده.»
✎ القلم: دايرة حوالين «ماكنتش عايز».
""", dark=True)

# ---------------------------------------------------------------- 4 who replied
slide("who", f'''
{h("طب لو كريم ماكانش عايز يقول كده…", 64, NB)}
{h("مين اللي رد مكانه؟", 140, AMB)}
{p("افتكر انت: آخر مرة رديت، وبعدها قلت «أنا ماكنتش قاصد».", 40, NT)}''', """
طب لو كريم نفسه بيقول إنه ماكانش عايز يقول كده…
مين اللي رد مكانه؟
(وقفة 3 ثواني)
وقبل ما نجاوب: افتكر انت آخر مرة رديت بسرعة، وبعدها قلت «أنا ماكنتش قاصد». في الشغل، أو في البيت، أو حتى على واتساب.
خليه في بالك، هنرجعله في آخر الحلقة.
الإجابة موجودة في الكتاب، في أول جزءين منه.
✎ القلم: علامة استفهام كبيرة جنب السؤال.
""", dark=True)

# ---------------------------------------------------------------- 5 map
eps = [("E1", "المخ الانفعالي", True), ("E2", "أنا ومشاعري", False), ("E3", "أنا والناس", False),
       ("E4", "البيت والشغل", False), ("E5", "الفرص المتاحة", False), ("E6", "محو الأمية العاطفية", False)]
boxes = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;background:{AMB if on else "#FFFFFF"};border:2px solid {AMB if on else LINE};border-radius:16px;padding:20px 16px">'
    f'{p(i, 24, NAVY if on else BODY, 600)}{p(t, 28, NAVY if on else INK, 600, "line-height:1.3")}</div>' for i, t, on in eps)
slide("map", f'''
{p("خريطة الكتاب", 32, AMBT, 600)}
<div style="display:flex;flex-direction:column;align-items:center;gap:0px">
<div style="background:{INK};border-radius:16px;padding:20px 48px">{p("«الذكاء العاطفي» — جولمان", 40, NT, 700, "text-align:center", DISP)}</div>
<div style="width:4px;height:48px;background:{LINE}"></div>
</div>
<div style="display:flex;flex-direction:row-reverse;gap:16px">{boxes}</div>
{p("كل حلقة = جزء من الكتاب · ومعاه الكتب التانية اللي بتكمّله", 32, BODY)}''', """
قبل ما نجاوب، دي الخريطة.
الكتاب مقسوم أجزاء، وكل حلقة هتشرح جزء. وكل ما نوصل لفكرة ليها علاقة بكتاب تاني، هنفتحه: Mind Over Mood، وNonviolent Communication، وCrucial Conversations، وكتاب Kabat-Zinn عن اليقظة.
النهارده إحنا هنا: المقدمة والجزء الأول، «المخ الانفعالي». يعني بنبدأ من تحت خالص: إيه اللي بيحصل في مخك في الثانيتين دول.
✎ القلم: دايرة حوالين E1، وسهم منها لـE2.
""", page="الخريطة", layout="display:flex;flex-direction:column;justify-content:center;gap:32px")

# ---------------------------------------------------------------- 6 aristotle
slide("aristotle", f'''
{p("المقدمة · التحدي الأرسطي", 32, AMBT, 600)}
{h("«أن يغضب أي إنسان، فهذا أمر سهل…", 72, INK)}
{h("لكن أن تغضب من الشخص المناسب، وبالقدر المناسب، وفي الوقت المناسب، وللهدف المناسب، وبالأسلوب المناسب… فليس هذا بالأمر السهل.»", 52, INK)}
{p("أرسطو، «الأخلاق إلى نيقوماخوس» — كما يفتتح بها جولمان كتابه", 28, BODY)}''', """
الكتاب بيبدأ بجملة لأرسطو. اسمعها كويس:
«أن يغضب أي إنسان، فهذا أمر سهل… لكن أن تغضب من الشخص المناسب، وبالقدر المناسب، وفي الوقت المناسب، وللهدف المناسب، وبالأسلوب المناسب… فليس هذا بالأمر السهل.»
لاحظ حاجة: أرسطو ماقالش «ماتغضبش». قال: اغضب صح.
وده بالظبط موضوع الكتاب كله. مش إنك تبطل تحس، إنك تحس وتتصرف صح.
✎ القلم: خط تحت كلمة «المناسب» كل مرة تتكرر (5 مرات).
المصدر: جولمان ص7.
""", page="ص7")

# ---------------------------------------------------------------- 7 specs
specs = ["الشخص المناسب", "القدر المناسب", "الوقت المناسب", "الهدف المناسب", "الأسلوب المناسب"]
rows = "".join(
    f'<div style="display:flex;flex-direction:row-reverse;align-items:center;gap:24px;background:#FFFFFF;border:2px solid {LINE};border-radius:12px;padding:16px 32px">'
    f'<p style="{TXT};font-size:32px;font-weight:600;color:{AMBT};font-variant-numeric:tabular-nums">{i + 1:02d}</p>{p(s, 40, INK, 600)}</div>'
    for i, s in enumerate(specs))
slide("specs", f'''
{h("5 مواصفات للغضب", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:48px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">{rows}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:24px">
{p("كريم في الاجتماع:", 36, BODY, 600)}
{p("الشخص: مديره · القدر: كبير · الوقت: قدام 8 · الهدف: يدافع عن نفسه · الأسلوب: هجوم", 36, INK)}
{p("نجح في كام واحدة؟", 44, AMBT, 700, "", DISP)}
</div></div>''', """
إحنا مهندسين، فخليني أقولها بطريقتنا: أرسطو كاتب specs للغضب. خمس مواصفات: الشخص، والقدر، والوقت، والهدف، والأسلوب.
تعالى نعمل review على رد كريم.
الشخص: مديره. ممكن يبقى مقبول.
القدر؟ الوقت؟ قدام تمانية؟ الأسلوب؟
(وقفة) كريم فشل في أغلب الـspecs. ومش لأنه مهندس وحش، لأنه ماكانش هو اللي بيرد أصلًا.
✎ القلم: علّم ✓ أو ✗ جنب كل واحدة وانت بتتكلم.
""", page="ص7")

# ---------------------------------------------------------------- 8 disagreement teaser
slide("books-disagree", f'''
{h("الغضب نفسه: حاجة وحشة؟", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
<div style="flex:1">{chip("MoM", "الغضب ممكن يكون صحي ومفيد… وغيابه قدام الإساءة نفسه مشكلة.", "p.256–258")}</div>
<div style="flex:1">{chip("NVC", "إحنا مش بنغضب بسبب اللي الناس بتقوله أو بتعمله… بسبب اللي جوانا.", "L2732")}</div>
</div>
{p("الكتب مش متفقة 100%. وده هنرجعله بالتفصيل في حلقة جاية.", 36, BODY)}''', """
وهنا أول مرة نفتح كتاب تاني.
Mind Over Mood بيقول إن الغضب ساعات يبقى صحي ومفيد، وإن غيابه قدام الإساءة نفسه مشكلة.
وNonviolent Communication بيقول حاجة أقوى: إن الغضب مش سببه اللي الناس عملوه، سببه اللي جوانا.
الكتب مش متفقة 100%، وأنا مش هخبي ده عنك. هنرجع للخلاف ده بالتفصيل لما يبقى معانا الأدوات.
النهارده سؤالنا أبسط: الرد اللي بيطلع قبل ما نفكر… بيطلع منين؟
✎ القلم: علامة ⚡ بين الكارتين.
المصادر: MoM p.256–258؛ NVC L2732 (الاختلاف D3).
""", page="ص7")

# ---------------------------------------------------------------- 9 ch1 divider
slide("ch1", f'''
{p("الجزء الأول · المخ الانفعالي", 36, AMB, 600)}
{h("الفصل 1", 64, NB)}
{h("العواطف… لماذا؟", 140, NT)}
{p("ص17", 36, NB)}''', """
الجزء الأول من الكتاب اسمه «المخ الانفعالي». وأول فصل فيه بيسأل سؤال غريب: العواطف… لماذا؟ ليه أصلًا عندنا مشاعر؟
""", dark=True, page="ص17", transition="push")

# ---------------------------------------------------------------- 10 emotion = motion
slide("motion", f'''
{p("أصل الكلمة", 32, AMBT, 600)}
<div style="display:flex;flex-direction:row-reverse;align-items:center;gap:40px">
{p("E + <b>motion</b>", 120, INK, 600, "", DISP)}
{p("=", 96, BODY)}
{p("حركة", 120, AMBT, 700, "", DISP)}
</div>
{h("كل انفعال = «نزوع إلى القيام بفعل»", 64, INK)}
{p("العاطفة مش مجرد إحساس… هي أمر تشغيل للجسم.", 40, BODY)}''', """
جولمان بيبدأ من أصل الكلمة. Emotion جاية من فعل لاتيني معناه «يتحرك»، وقدامه حرف e، يعني «يتحرك بعيد».
يعني كل انفعال، بتعبيره، «نزوع إلى القيام بفعل».
بلغتنا: العاطفة مش مجرد إحساس، هي أمر تشغيل. الجسم بيستلمه ويبدأ ينفذ… حتى قبل ما انت توافق.
ارجع لكريم: الغضب ماكانش إحساس بس، كان أمر: «رد دلوقتي».
✎ القلم: سهم من «motion» لـ«حركة».
المصدر: جولمان ص20.
""", page="ص20")

# ---------------------------------------------------------------- 11 body signatures
def card(title, items, col):
    lis = "".join(p("• " + i, 36, INK) for i in items)
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;border-top:12px solid {col};border-radius:16px;padding:40px">'
            f'{p(title, 52, col, 700, "", DISP)}{lis}</div>')


slide("body", f'''
{h("كل انفعال ليه بصمة في جسمك", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
{card("الغضب", ["الدم يروح لليدين", "القلب يسرع", "دفعة أدرينالين"], AMBT)}
{card("الخوف", ["الدم يروح لعضلات الرجلين", "الوش يشحب", "الجسم يتجمد لحظة"], "#3A64A8")}
</div>
{chip("CC", "جسمك بيبان عليه قبل ما انت تاخد بالك من الشعور.", "p.48–49")}''', """
الانفعال مش بس في دماغك، ليه بصمة في جسمك.
في الغضب، الكتاب بيقول إن الدم بيروح لليدين، كأن الجسم بيجهزك تمسك حاجة أو تضرب. والقلب بيسرع، وفيه دفعة أدرينالين.
وفي الخوف العكس: الدم بيروح لعضلات الرجلين عشان تجري، والوش يشحب، والجسم ممكن يتجمد لحظة.
وCrucial Conversations بيضيف ملاحظة عملية جدًا: جسمك بيبان عليه قبل ما انت تاخد بالك إنك متضايق. خلي دي في بالك، هنستخدمها في التمرين.
✎ القلم: ارسم إيد جنب «الغضب» ورجل جنب «الخوف».
المصادر: جولمان ص21؛ CC p.48–49.
""", page="ص21")

# ---------------------------------------------------------------- 12 two minds
slide("two-minds", f'''
{h("في دماغنا عقلين", 80, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px;align-items:stretch">
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;border:2px solid {TEAL};border-radius:16px;padding:40px">
{p("الكلام", 32, TEALT, 600)}
{p("«لم يعد يهمني حقًا»", 52, INK, 700, "", DISP)}
{p("العقل اللي بيفكر", 36, TEALT, 600)}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;border:2px solid {AMB};border-radius:16px;padding:40px">
{p("العينين", 32, AMBT, 600)}
{p("اغرورقت بالدموع", 52, INK, 700, "", DISP)}
{p("العقل اللي بيحس", 36, AMBT, 600)}
</div></div>
{p("صديقة جولمان بعد طلاقها — ص23–24", 28, BODY)}''', """
جولمان بيحكي عن صديقة له بعد طلاقها. قالتله: «لم يعد يهمني حقًا». وهي بتقولها، عينيها دمعت.
الكلام قال حاجة، والعينين قالت حاجة تانية.
ومن هنا جولمان بيقول: في دماغنا عقلين. عقل بيفكر، وعقل بيحس. والاتنين مش دايمًا متفقين.
في اجتماع كريم، العقل اللي بيفكر كان عايز يوضح الإيميل بهدوء. العقل اللي بيحس سبقه.
✎ القلم: سهم رايح جاي بين الكارتين، واكتب عليه «مش دايمًا متفقين».
المصدر: جولمان ص23–24.
""", page="ص23–24")

# ---------------------------------------------------------------- 13 five-part model (MoM)
ring = [("موقف", 986, 330), ("أفكار", 1440, 470), ("مشاعر", 1280, 740), ("جسم", 690, 740), ("تصرف", 530, 470)]
nodes = "".join(
    f'<div style="position:absolute;left:{x}px;top:{y}px;width:300px;background:#FFFFFF;border:3px solid {BOOK["MoM"][0]};border-radius:60px;padding:16px 0px">'
    f'{p(t, 40, INK, 700, "text-align:center", DISP)}</div>' for t, x, y in ring)
slide("five-part", f'''
<p style="{TXT};position:absolute;left:480px;top:112px;width:1312px;font-size:28px;font-weight:600;color:{BOOK["MoM"][0]};text-align:right">من كتاب تاني · Mind Over Mood · p.7–8</p>
<h2 style="{DISP};position:absolute;left:480px;top:160px;width:1312px;font-size:64px;font-weight:700;color:{INK};text-align:right;line-height:1.2">كلهم ماسكين في بعض</h2>
{nodes}
<p style="{TXT};position:absolute;left:830px;top:590px;width:600px;font-size:32px;color:{BODY};text-align:center">أي تغيير في واحدة… بيحرّك الباقي</p>''', """
Mind Over Mood عنده رسمة بسيطة بتكمّل كلام جولمان: خمس حاجات ماسكين في بعض.
الموقف، وأفكارك، ومشاعرك، وجسمك، وتصرفك. أي تغيير في واحدة بيحرّك الباقي.
عند كريم: الموقف «شغل عيال» ← جسمه سخن ← الشعور غضب ← التصرف رد هجومي. وكله في ثانيتين.
والخبر الحلو إن الربط ده شغال في الاتجاهين. هنستغله في الحلقات الجاية.
✎ القلم: وصّل الخمسة ببعض بأسهم، وابدأ من «موقف».
المصدر: MoM p.7–8.
""", page="ص23 ← MoM", layout="display:block")

# ---------------------------------------------------------------- 14 ch2 divider
slide("ch2", f'''
{p("الجزء الأول · المخ الانفعالي", 36, AMB, 600)}
{h("الفصل 2", 64, NB)}
{h("تشريح النوبات الانفعالية", 120, NT)}
{p("ص31", 36, NB)}''', """
الفصل التاني هو قلب الحلقة: «تشريح النوبات الانفعالية». هنا هنلاقي إجابة سؤال: مين اللي رد مكان كريم؟
""", dark=True, page="ص31", transition="push")

# ---------------------------------------------------------------- 15 hijack definition
slide("hijack", f'''
{p("النوبة الانفعالية (Emotional Hijacking)", 36, AMBT, 600)}
{h("المخ يعلن حالة الطوارئ…", 88, INK)}
{h("قبل ما العقل اللي بيفكر يلحق يشوف إيه اللي بيحصل.", 64, BODY)}
{p("والعلامة: بعدها بتقول «أنا مش عارف إيه اللي جرالي».", 40, INK)}''', """
جولمان بيسمي اللي حصل لكريم «النوبة الانفعالية»، وبالإنجليزي Emotional Hijacking، يعني «خطف».
ومعناها ببساطة: جزء في المخ بيعلن حالة الطوارئ قبل ما العقل اللي بيفكر يلحق يتأمل إيه اللي بيحصل.
وليها علامة سهل تعرفها: بعد ما تخلص، بتقول «أنا مش عارف إيه اللي جرالي» أو «أنا ماكنتش عايز أقول كده». دي بالظبط جملة كريم.
✎ القلم: اكتب «كريم» جنب الجملة الأخيرة.
المصدر: جولمان ص31.
""", page="ص31")

# ---------------------------------------------------------------- 16 small daily hijack
slide("small", f'''
{h("مش لازم تبقى كارثة… بتحصل كل يوم", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;border:2px solid {LINE};border-radius:16px;padding:40px">
{p("من الكتاب · ص34", 28, AMBT, 600)}
{p("بنت صديقها جابلها لوحة كانت نفسها فيها من شهور. قالها مش هيقدر يقعد بعد الغدا عشان عنده تمرين. رمت اللوحة في الزبالة… وندمت بعدها بشهور.", 34, INK)}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;border:2px solid {LINE};border-radius:16px;padding:40px">
{p("من شغلنا · مثال توضيحي", 28, AMBT, 600)}
{p("نور، مهندسة معمارية، بعتت تعديلات التصميم للـPM بعد يومين شغل. الرد بعد 40 دقيقة: «تمام.» وفي 40 ثانية كانت كاتبة رد فيه عتاب.", 34, INK)}
</div></div>''', """
ومتفتكرش إن النوبة دي لازم تبقى حاجة كبيرة. جولمان بيحكي عن بنت سافرت ساعتين عشان تقضي اليوم مع صديقها، وجابلها لوحة كانت نفسها فيها من شهور. وبعد الغدا قالها إنه مش هيقدر يقعد معاها لأن عنده تمرين. في لحظة، رمت اللوحة في الزبالة. وبعد شهور كانت لسه ندمانة.
وعندنا في الشغل: نور، مهندسة معمارية، بعتت تعديلات التصميم للـPM بعد يومين شغل. الرد جه بعد 40 دقيقة: «تمام.» كلمة واحدة. وفي 40 ثانية، نور كانت كاتبة رد فيه عتاب.
نوبات صغيرة، بس بتتكرر كل يوم.
✎ القلم: دايرة حوالين «في لحظة» و«40 ثانية».
المصدر: جولمان ص34. نور مثال توضيحي من تأليفنا.
""", page="ص34")

# ---------------------------------------------------------------- 17 alarm team
qs = "".join(p("«" + q + "»", 40, INK, 600, f"background:#FFFFFF;border-right:8px solid {AMB};border-radius:8px;padding:16px 32px") for q in
             ["هل أكره ده؟", "هل ده هيأذيني؟", "هل ده حاجة بخاف منها؟"])
slide("alarm", f'''
{p("الأميجدالا (اللوزة)", 36, AMBT, 600)}
{h("فريق الإنذار اللي في بيتك", 80, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:48px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:16px">{p("بيسأل 3 أسئلة بس:", 36, BODY)}{qs}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">{p("ولو الإجابة «أيوه»:", 36, BODY)}{p("يبعت نداء طوارئ لكل المخ والجسم… «اضرب أو اهرب».", 44, INK, 700, "", DISP)}{p("مش بيسأل: «هو فعلًا قصده إيه؟»", 36, AMBT, 600)}</div>
</div>''', """
مين بيعلن الطوارئ؟ جولمان بيقول إنه جزء صغير في المخ اسمه الأميجدالا، أو «اللوزة».
وبيشبّهه بفريق الإنذار في البيت: أول ما جهاز الأمان يدي إشارة، الفريق يتصل بالمطافي والبوليس والجيران.
والفريق ده بيسأل أسئلة بدائية جدًا، تلاتة بس: هل أكره ده؟ هل ده هيأذيني؟ هل ده حاجة بخاف منها؟ ولو الإجابة «أيوه»، يبعت نداء طوارئ للمخ والجسم كله.
لاحظ السؤال اللي مش بيسأله: «هو قصده إيه بالظبط؟» ده سؤال محتاج وقت، والإنذار مابيستناش.
للمهندسين: فكّر فيه زي حساس دخان. شغلته إنه يصفّر بسرعة، مش إنه يحلل نوع الدخان.
✎ القلم: ارسم جرس إنذار صغير جنب العنوان.
المصدر: جولمان ص34–35.
""", page="ص34–35")

# ---------------------------------------------------------------- 18 two roads (LeDoux)
def box(x, y, w, t, col, fill="#FFFFFF", tc=INK, bid=None, build=None):
    b = f' data-build-in="{build}"' if build else ""
    i = f' id="{bid}"' if bid else ""
    return (f'<div{i}{b} style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:{fill};border:3px solid {col};border-radius:20px;padding:24px 16px">'
            f'{p(t, 36, tc, 700, "text-align:center;line-height:1.25", DISP)}</div>')


slide("two-roads", f'''
<p style="{TXT};position:absolute;left:480px;top:112px;width:1312px;font-size:28px;font-weight:600;color:{AMBT};text-align:right">اكتشاف جوزيف لودو · ص36–37</p>
<h2 style="{DISP};position:absolute;left:480px;top:160px;width:1312px;font-size:64px;font-weight:700;color:{INK};text-align:right;line-height:1.2">الإشارة بتمشي في طريقين</h2>
{box(1520, 480, 240, "العين<br>والودن", LINE)}
{box(1120, 480, 260, "المهاد", LINE)}
{box(520, 300, 360, "القشرة الجديدة<br>(العقل اللي بيفكر)", TEAL, bid="cortex", build="fade 2")}
{box(520, 700, 360, "الأميجدالا<br>(الإنذار)", AMB, "#FFF4E3", bid="amyg", build="rise 1")}
<x-connector x1="1520" y1="560" x2="1380" y2="560" head="end" style="color:{BODY};border-width:4px"></x-connector>
<x-connector x1="1120" y1="600" x2="880" y2="770" head="end" style="color:{AMB};border-width:8px"></x-connector>
<x-connector x1="1120" y1="520" x2="880" y2="380" head="end" style="color:{TEAL};border-width:4px;border-style:dashed"></x-connector>
<p data-build-in="rise 1" style="{TXT};position:absolute;left:900px;top:760px;width:420px;font-size:32px;font-weight:700;color:{AMBT};text-align:right">طريق قصير: بيوصل الأول</p>
<p data-build-in="fade 2" style="{TXT};position:absolute;left:900px;top:330px;width:420px;font-size:32px;font-weight:700;color:{TEALT};text-align:right">طريق طويل: بيفكر… ويتأخر</p>''', """
هنا أهم اكتشاف في الحلقة، وهو لعالم أعصاب اسمه جوزيف لودو.
الإشارة اللي جاية من عينك أو ودنك بتروح الأول لمحطة اسمها «المهاد». ومن هناك بتطلع في طريقين.
[اضغط: يظهر الطريق القصير] طريق قصير ومباشر للأميجدالا، الإنذار.
[اضغط: يظهر الطريق الطويل] وطريق أطول للقشرة الجديدة، العقل اللي بيفكر ويحلل.
والنتيجة؟ الإنذار بيوصله الخبر الأول، وممكن يبدأ الاستجابة قبل ما العقل اللي بيفكر يخلص قراءته.
عند كريم: «شغل عيال» وصلت الإنذار قبل ما توصل المهندس اللي جواه.
للأمانة: ده تبسيط الكتاب (1995). العلم بعده شايف الصورة أعقد من طريقين. بس الفكرة الأساسية لسه صالحة: فيه رد سريع بيحصل قبل التفكير الكامل. [EXTERNAL_KNOWLEDGE]
✎ القلم: ارسم سباق. علّم الطريق القصير «1» والطويل «2»، واكتب جنب الأميجدالا «كريم رد من هنا».
المصدر: جولمان ص36–37.
""", page="ص36–37", layout="display:block")

# ---------------------------------------------------------------- 19 fast but error-prone
slide("fast-wrong", f'''
{p("جوزيف لودو، كما ينقله جولمان · ص44", 32, AMBT, 600)}
{h("«وسيلة سريعة جدًا للانفعال… لكنها عملية سريعة كثيرة الأخطاء.»", 72, INK)}
<div style="display:flex;flex-direction:column;gap:12px;background:#FFFFFF;border:2px solid {LINE};border-radius:16px;padding:40px">
{p("جولمان نفسه · ص42–43", 28, AMBT, 600)}
{p("الساعة 3 الفجر: صوت خبطة ضخمة. نط من السرير وجري برا الأوضة، فاكر السقف وقع. طلعت كراتين مراتة كانت راصاها في ركن الأوضة ووقعت.", 36, INK)}
</div>''', """
طب الطريق القصير ده كويس ولا وحش؟
لودو بيقول عنه جملة مهمة جدًا: «وسيلة سريعة جدًا للانفعال… لكنها عملية سريعة كثيرة الأخطاء».
سريع، بس بيغلط كتير.
وجولمان بيحكي عن نفسه: الساعة تلاتة الفجر سمع خبطة ضخمة في ركن أوضة النوم. نط من السرير وجري برا الأوضة في ثانية، فاكر السقف وقع. ولما رجع بحذر، لقى كراتين كانت مراته راصاها فوق بعض ووقعت.
لو السقف كان وقع فعلًا، النطة دي كانت هتنقذه. بس المرة دي كان إنذار غلط.
المشكلة إننا في الشغل مش بنتعامل مع أسقف بتقع… بنتعامل مع جمل زي «شغل عيال».
✎ القلم: خط تحت «سريعة جدًا» بلون، وتحت «كثيرة الأخطاء» بلون تاني.
المصادر: جولمان ص42–44.
""", page="ص42–44")

# ---------------------------------------------------------------- 20 old alarms
slide("old-alarm", f'''
{h("إنذارات قديمة", 88, INK)}
{p("الإنذار بيقارن اللي بيحصل دلوقتي باللي حصل زمان… ويتصرف بطريقة «انطبعت في ذاكرتنا منذ زمن طويل».", 40, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#FFFFFF;border:2px solid {AMB};border-radius:16px;padding:32px">
{p("كريم · مثال توضيحي", 28, AMBT, 600)}
{p("في إعدادي، مدرس ضحك على كراسته قدام الفصل. «شغل عيال» قدام 8 = نفس الإحساس.", 34, INK)}
</div>
<div style="flex:1">{chip("MoM", "الماضي بيشكّل إزاي بنقرا الحاضر.", "p.63")}</div>
</div>''', """
طب ليه الجملة دي بالذات فجّرت كريم؟
جولمان بيقول إن الإنذار بيشتغل كمخزن ذكريات. بيقارن اللي بيحصل دلوقتي باللي حصل زمان. ولو لقى شبه، حتى لو جزئي، يتصرف بطريقة بتعبير الكتاب «انطبعت في ذاكرتنا منذ زمن طويل».
عند كريم، وده جزء من المثال التوضيحي: وهو في إعدادي، مدرس ضحك على كراسته قدام الفصل كله. «شغل عيال» قدام تمانية مهندسين… نفس الإحساس القديم بالظبط.
وMind Over Mood بيقول نفس الكلام من زاويته: الماضي بيشكّل إزاي بنقرا الحاضر.
سؤال ليك: فيه جملة معينة في الشغل بتفجّرك أكتر من غيرها؟
✎ القلم: وصّل «زمان» بـ«دلوقتي» بسهم.
المصادر: جولمان ص41؛ MoM p.63.
""", page="ص41")

# ---------------------------------------------------------------- 21 jessica
beats = [("منتصف الليل", "بنتها «جيسكا» (6 سنين) بايتة برا البيت لأول مرة. التليفون يرن."),
         ("الإنذار", "الفرشة وقعت من إيدها، جريت، وصرخت في السماعة: «جيسكا!»"),
         ("العقل اللي بيفكر يلحق", "صوت ست: «أظن أنني طلبت رقمًا خطأ». الأم تهدى وتسأل بهدوء: «ما الرقم الذي تطلبينه؟»")]
bl = "".join(
    f'<div data-build-in="rise {i + 1}" style="position:absolute;left:{1312 - i * 420}px;top:360px;width:390px;display:flex;flex-direction:column;gap:12px;background:#FFFFFF;border-top:10px solid {AMB if i < 2 else TEAL};border-radius:16px;padding:32px">'
    f'{p(a, 32, AMBT if i < 2 else TEALT, 700, "", DISP)}{p(b, 30, INK)}</div>' for i, (a, b) in enumerate(beats))
slide("jessica", f'''
<p style="{TXT};position:absolute;left:480px;top:112px;width:1312px;font-size:28px;font-weight:600;color:{AMBT};text-align:right">قصة من الكتاب · ص45</p>
<h2 style="{DISP};position:absolute;left:480px;top:160px;width:1312px;font-size:64px;font-weight:700;color:{INK};text-align:right;line-height:1.2">أم جيسكا: الإنذار… والفرامل</h2>
{bl}
<p style="{TXT};position:absolute;left:480px;top:860px;width:1312px;font-size:34px;font-weight:600;color:{TEALT};text-align:right">الفصوص الأمامية (ورا الجبهة) هي اللي بتصحح الإنذار… لما تلحق.</p>''', """
طب هل إحنا محكوم علينا؟ لا. وجولمان بيورينا ده في قصة جميلة.
[اضغط] أم عندها بنت اسمها جيسكا، ست سنين، بايتة برا البيت لأول مرة عند صاحبتها. نص الليل التليفون يرن.
[اضغط] الأم كانت بتغسل سنانها. الفرشة وقعت من إيدها، جريت على التليفون وقلبها بيدق، وصرخت في السماعة: «جيسكا!»
[اضغط] ترد ست على الناحية التانية: «أظن أنني طلبت رقمًا خطأ». وفي اللحظة دي بالظبط الأم تمالكت أعصابها، وسألتها بهدوء: «ما الرقم الذي تطلبينه؟»
اللي حصل إن الإنذار اشتغل، وبعده جزء تاني في المخ لحق وصحّح: الفصوص الأمامية اللي ورا الجبهة. زي الفرامل.
الإنذار عند كريم اشتغل برضه. الفرق إن الفرامل مالحقتش.
✎ القلم: ارسم فرامل (دايرة وجواها خط) جنب الكارت التالت.
المصدر: جولمان ص45.
""", page="ص45", layout="display:block")

# ---------------------------------------------------------------- 22 two forces + working memory
slide("two-forces", f'''
{h("النوبة محتاجة قوتين مع بعض", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
{card("قوة بتشغّل الإنذار", ["«شغل عيال» قدام 8", "ذكرى قديمة", "ضغط وتعب"], AMBT)}
{card("قوة بتضعف الفرامل", ["العقل اللي بيفكر يتجمد", "«مش قادر أفكر صح»", "الذاكرة العاملة تقع"], TEALT)}
</div>
{p("عشان كده في الـreview وانت متضايق… بتنسى أوضح حاجة كنت عايز تقولها.", 36, BODY)}''', """
جولمان بيقول إن النوبة الانفعالية محتاجة قوتين مع بعض: قوة بتشغّل الإنذار، وقوة بتضعف الفرامل اللي في العقل اللي بيفكر.
والأخطر إن الانفعال الشديد بيعمل حاجة بيسميها الكتاب «تجمد عصبي» في الجزء الأمامي من المخ، في حاجة اسمها «الذاكرة العاملة». وده اللي بيخليك تقول: «أنا مش قادر أفكر صح».
عشان كده، وانت متضايق في design review، بتنسى أوضح نقطة كنت محضّرها. مش عشان انت مش فاهم، عشان الذاكرة العاملة وقعت.
كريم كان عارف كويس اللي في الإيميل. بس في اللحظة دي، المعلومة ماكانتش متاحة.
✎ القلم: ارسم ميزان، وخلي كفة الإنذار نازلة.
المصادر: جولمان ص47–49.
""", page="ص47–49")

# ---------------------------------------------------------------- 23 two layers (CC)
slide("two-layers", f'''
{h("طب الأفكار مالهاش دور؟", 72, INK)}
<div style="display:flex;flex-direction:row-reverse;gap:32px">
<div style="flex:1">{chip("CC", "بين اللي حصل واللي حسيته فيه «حكاية» بنحكيها لنفسنا… وبتتحكي «بسرعة كبيرة جدًا».", "p.98–101")}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:{NAVY};border-radius:16px;padding:40px">
{p("يبقى فيه طبقتين:", 32, NB, 600)}
{p("1 · إنذار سريع", 44, AMB, 700, "", DISP)}
{p("2 · حكاية بتغذيه… أو تطفيه", 44, TEALL, 700, "", DISP)}
</div></div>
{p("الطبقة التانية دي موضوع الحلقة الجاية.", 36, BODY)}''', """
هنا ممكن حد يسأل: طب يعني الموضوع كله كيمياء في المخ؟ أفكاري مالهاش دور؟
Crucial Conversations بيقول حاجة مهمة: بين اللي بيحصل واللي بنحسه فيه «حكاية» بنحكيها لنفسنا، وإن الحكاية دي بتتحكي «بسرعة كبيرة جدًا».
فالصورة الأكمل فيها طبقتين: إنذار سريع، زي ما جولمان شرح، وحكاية بتغذيه أو تطفيه.
«ده بيهيني قدام الكل» حكاية بتغذي الإنذار. «ده شكله متضغوط من الإدارة» حكاية بتطفيه.
والطبقة التانية دي، الحكاية، هي اللي نقدر نشتغل عليها. ودي موضوع الحلقة الجاية.
✎ القلم: ارسم نار صغيرة جنب «1»، وجنب «2» سهمين: واحد لفوق وواحد لتحت.
المصدر: CC p.98–101 (الاختلاف D6 بين الكتب: محسوم كطبقتين).
""", page="CC ← ص44")

# ---------------------------------------------------------------- 24 karim replay
steps = [("0.0 ث", "«شغل عيال»", LINE, INK), ("0.1 ث", "الإنذار: «ده هجوم… زي زمان»", AMB, INK),
         ("0.5 ث", "الجسم: سخونة · قلب · فك مشدود", AMB, INK), ("1.5 ث", "الرد: «لو كنت قريت الإيميل…»", AMB, INK),
         ("بعد الاجتماع", "العقل اللي بيفكر يوصل: «أنا ماكنتش عايز أقول كده»", TEAL, INK)]
st = "".join(
    f'<div data-build-in="rise {i + 1}" style="position:absolute;left:480px;top:{250 + i * 136}px;width:1312px;display:flex;flex-direction:row-reverse;align-items:center;gap:32px;background:#FFFFFF;border-right:12px solid {c};border-radius:12px;padding:20px 32px">'
    f'<p style="{TXT};font-size:28px;font-weight:600;color:{BODY};width:220px;text-align:right">{t}</p>{p(s, 36, tc, 600)}</div>'
    for i, (t, s, c, tc) in enumerate(steps))
slide("replay", f'''
<h2 style="{DISP};position:absolute;left:480px;top:112px;width:1312px;font-size:64px;font-weight:700;color:{INK};text-align:right;line-height:1.2">نرجّع الشريط: الثانيتين بتوع كريم</h2>
{st}''', """
يلا نرجع لكريم ونعيد الثانيتين بالبطيء.
[اضغط] «شغل عيال».
[اضغط] الإنذار: «ده هجوم»، وكمان «ده زي زمان».
[اضغط] الجسم: سخونة، والقلب بيسرع، والفك مشدود.
[اضغط] الرد يطلع: «لو كنت قريت الإيميل…»
[اضغط] والعقل اللي بيفكر يوصل متأخر، بعد الاجتماع: «أنا ماكنتش عايز أقول كده».
(ملحوظة: الأزمنة دي توضيحية، مش قياس.)
يبقى نرجع لسؤالنا: مين اللي رد مكان كريم؟ الإنذار. الطريق القصير. رد قبل ما الفرامل تلحق.
وده مش عيب في كريم. ده تصميم المخ عند كلنا. بس لما تفهم التصميم، تقدر تشتغل عليه.
✎ القلم: ارسم خط زمن تحت الخطوات، وعلّم النقطة اللي كان ممكن الفرامل تلحق فيها.
""", page="الإجابة", layout="display:block")

# ---------------------------------------------------------------- 25 body map exercise
spots = [("الفك", 1000, 335), ("الصدر", 1000, 435), ("المعدة", 1000, 545), ("القبضة", 1000, 615)]
body_svg = (f'<svg aria-label="رسم جسم بسيط" width="420" height="720" viewBox="0 0 420 720" style="position:absolute;left:560px;top:230px">'
            f'<circle cx="210" cy="90" r="62" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="130" y="170" width="160" height="250" rx="60" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="60" y="185" width="56" height="230" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="304" y="185" width="56" height="230" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="140" y="425" width="62" height="270" rx="30" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="218" y="425" width="62" height="270" rx="30" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            f'<circle cx="210" cy="132" r="14" fill="{AMB}"/><circle cx="210" cy="230" r="14" fill="{AMB}"/>'
            f'<circle cx="210" cy="340" r="14" fill="{AMB}"/><circle cx="88" cy="410" r="14" fill="{AMB}"/><circle cx="332" cy="410" r="14" fill="{AMB}"/></svg>')
labels = "".join(f'<p style="{TXT};position:absolute;left:{x}px;top:{y}px;width:220px;font-size:36px;font-weight:700;color:{AMBT};text-align:left">← {t}</p>' for t, x, y in spots)
slide("body-map", f'''
<h2 style="{DISP};position:absolute;left:480px;top:112px;width:1312px;font-size:64px;font-weight:700;color:{INK};text-align:right;line-height:1.2">تمرين: إنذارك بيبان فين الأول؟</h2>
{body_svg}{labels}
<div style="position:absolute;left:1360px;top:280px;width:432px;display:flex;flex-direction:column;gap:20px">
{p("1 · افتكر آخر مرة رديت قبل ما تفكر.", 32, INK, 600)}
{p("2 · إيه أول حاجة حسيتها في جسمك؟", 32, INK, 600)}
{p("3 · علّمها على الرسمة.", 32, INK, 600)}
{p("دي «اللمبة» بتاعتك: أول إشارة إن الإنذار اشتغل.", 32, AMBT, 700)}
</div>
<div style="position:absolute;left:1360px;top:760px;width:432px">{chip("CC", "العلامات المبكرة في الجسم هي أول فرصة تلحق نفسك.", "p.48–49")}</div>''', """
تمرين، ومحتاجك تعمله بجد، 30 ثانية بس.
افتكر الموقف اللي قلتلك عليه في الأول: آخر مرة رديت قبل ما تفكر.
إيه أول حاجة حسيتها في جسمك؟ فكك اتشد؟ صدرك اتقفل؟ معدتك اتقلبت؟ إيدك اتقفلت؟
(صمت 10 ثواني — بص للكاميرا ومتتكلمش)
دي اسمها «اللمبة» بتاعتك. أول إشارة إن الإنذار اشتغل.
وCrucial Conversations بيقول إن العلامات دي هي أول فرصة تلحق نفسك قبل ما الموقف يفلت. وMind Over Mood وKabat-Zinn بيتكلموا عن نفس الفكرة: جسمك بيقولك قبل عقلك.
الحلقة الجاية هنتعلم نعمل إيه لما اللمبة دي تنور.
✎ القلم: علّم على الرسمة مكان «لمبتك» انت شخصيًا، وقول للمشاهد يعمل زيك.
المصادر: CC p.48–49؛ MoM p.26؛ KZ p.101–103.
""", page="تمرين", layout="display:block")

# ---------------------------------------------------------------- 26 recap
rc = [("1", "العاطفة أمر تشغيل", "كل انفعال «نزوع لفعل» · ص20"), ("2", "فيه طريق قصير", "الإنذار بيوصل قبل التفكير… وبيغلط كتير · ص36–44"),
      ("3", "فيه فرامل", "الفصوص الأمامية بتصحح لما تلحق · ص45–47")]
rcc = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#16263D;border-radius:16px;padding:40px">'
    f'{p(n, 64, AMB, 700, "", DISP)}{p(a, 44, NT, 700, "", DISP)}{p(b, 30, NB)}</div>' for n, a, b in rc)
slide("recap", f'''
{h("3 حاجات من الحلقة دي", 80, NT)}
<div style="display:flex;flex-direction:row-reverse;gap:24px">{rcc}</div>
{p("وأول لمبة للإنذار في جسمك… انت عرفتها النهارده.", 36, NB)}''', """
نلخص في تلات حاجات.
واحد: العاطفة مش مجرد إحساس، دي أمر تشغيل للجسم.
اتنين: فيه طريق قصير في المخ، الإنذار بيوصله الخبر قبل التفكير. سريع، بس بيغلط كتير.
تلاتة: فيه فرامل، الجزء الأمامي من المخ. بيصحح لما يلحق، زي أم جيسكا.
والحاجة الرابعة، اللي عملتها انت بنفسك: عرفت أول لمبة للإنذار في جسمك.
✎ القلم: علامة ✓ على كل كارت.
""", dark=True, page="الخلاصة")

# ---------------------------------------------------------------- 27 next
boxes2 = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;background:{AMB if i == "E2" else ("#DDE7E4" if i == "E1" else "#FFFFFF")};border:2px solid {AMB if i == "E2" else LINE};border-radius:16px;padding:20px 16px">'
    f'{p(i + (" ✓" if i == "E1" else ""), 24, NAVY if i == "E2" else BODY, 600)}{p(t, 28, NAVY if i == "E2" else INK, 600, "line-height:1.3")}</div>' for i, t, _ in eps)
slide("next", f'''
<div style="display:flex;flex-direction:row-reverse;gap:16px">{boxes2}</div>
{p("الحلقة الجاية · أنا ومشاعري", 36, AMBT, 600)}
{h("كريم هدي… بس الساعة 2 بالليل فتح الإيميل وكتب: «أنا بستقيل».", 64, INK)}
{p("هيدوس Send؟", 48, INK, 700, "", DISP)}''', """
الحلقة الجاية ننتقل على الخريطة للجزء التاني: «أنا ومشاعري». هنتكلم إزاي تعرف اللي جواك وانت جواه، وإزاي تتحكم فيه من غير ما تكتمه.
ونرجع لكريم. الاجتماع خلص، وكريم هدي… أو كان فاكر إنه هدي.
الساعة 2 بالليل فتح الإيميل، وكتب: «أنا بستقيل».
هيدوس Send؟
نشوف الحلقة الجاية.
✎ القلم: دايرة حوالين «Send».
""", page="الحلقة 2")

# ---------------------------------------------------------------- 28 end
slide("end", f'''
{h("اكتبلي في التعليقات:", 64, NB)}
{h("إنذارك بيبان فين الأول؟", 110, AMB)}
{p("الفك · الصدر · المعدة · القبضة… ولا حاجة تانية؟", 40, NT)}
{p("المصادر الأساسية: جولمان، «الذكاء العاطفي»، عالم المعرفة 262 — المقدمة، ف1، ف2", 28, NB)}''', """
وقبل ما تمشي، اكتبلي في التعليقات: إنذارك بيبان فين الأول؟ الفك؟ الصدر؟ المعدة؟ القبضة؟ ولا حاجة تانية خالص؟
أنا بقرا التعليقات، وممكن أستخدم إجاباتكم في الحلقة الجاية.
أشوفك في الحلقة التانية.
""", dark=True, page="النهاية")

# ---------------------------------------------------------------- index
for sid, htmltext in slides.items():
    (OUT / "slides" / f"{sid}.html").write_text(htmltext, encoding="utf-8")
deck = {"v": 4, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
        "lists": "css", "title": "الحلقة 1 · المخ الانفعالي", "order": order,
        "sections": {"s1": {"description": "المشكلة: رد كريم في الاجتماع وسؤال «مين اللي رد مكانه؟»", "start": "cover"},
                     "s2": {"description": "المقدمة: أرسطو والغضب الصح، وخريطة السلسلة", "start": "map"},
                     "s3": {"description": "الفصل 1: العاطفة نزوع لفعل، بصمة الجسم، والعقلين", "start": "ch1"},
                     "s4": {"description": "الفصل 2: النوبة الانفعالية، الإنذار، الطريقين، والفرامل", "start": "ch2"},
                     "s5": {"description": "الإجابة والتمرين والخطاف", "start": "replay"}},
        "faces": {"reem-kufi": {"family": "Reem Kufi", "href": "https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@400..700&display=swap"},
                  "ibm-plex-sans-arabic": {"family": "IBM Plex Sans Arabic", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap"}},
        "designSystems": []}
(OUT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")
words = sum(len(s.split("<aside>")[1].split()) for s in slides.values())
print(len(order), "slides;", words, "note words ≈", round(words / 125, 1), "min at 125 wpm")
