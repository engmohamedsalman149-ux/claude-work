"""Build E01 animatic preview (single HTML) from the package files.

Reads: E01/04 (slide times), E01/09 (camera/presenter per segment), _build/e01_runtime.json (spoken lines).
Writes: E01/12_E01_PREVIEW.html
"""
import json, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
EP = HERE.parent / "E01"


def sec(mmss):
    m, s = mmss.split(":")
    return int(m) * 60 + int(s)


slides_md = (EP / "04_E01_SLIDE_BY_SLIDE.md").read_text(encoding="utf-8")
times = {s: (sec(a), sec(b)) for s, a, b in re.findall(r"^### (S\d+) · (\d\d:\d\d)–(\d\d:\d\d)", slides_md, flags=re.M)}

tl_md = (EP / "09_E01_PRODUCTION_TIMELINE.md").read_text(encoding="utf-8")
segs = [dict(a=sec(a), b=sec(b), scene=sc, cam=cam.replace("**", "").strip(), pres=pr.replace("**", "").strip())
        for _, a, b, sc, cam, pr in re.findall(r"^\| (\d+) \| (\d\d:\d\d)–(\d\d:\d\d) \| (E1-\d+) \| ([^|]+) \| ([^|]+) \|", tl_md, flags=re.M)]

rt = json.loads((HERE / "e01_runtime.json").read_text(encoding="utf-8"))
lines, scenes = [], []
for s in rt["scenes"]:
    scenes.append(dict(id=s["id"], a=sec(s["start"]), b=sec(s["end"])))
    for start, text, dur in s["rows"]:
        a = sec(start)
        m = re.match(r"^(⏳|🎬)(\d+)$", text)
        kind = "hold" if m and m.group(1) == "⏳" else "visual" if m else "say"
        lines.append(dict(a=a, b=a + dur, kind=kind, text=text.replace("‖", "").replace("**", "").strip()))

TITLES = {
    "E1-01": "Cold Open — «تمام.»", "E1-02": "الوعد + العنوان", "E1-03": "«تمام» × 3", "E1-04": "المترو",
    "E1-05": "كاميرا المراقبة", "E1-06": "الفكرة السخنة والمحكمة", "E1-07": "تلات نظارات", "E1-08": "عتمان",
    "E1-09": "الخطاف",
}
for s in scenes:
    s["title"] = TITLES[s["id"]]

# Visual spec per slide (render hints only; content mirrors 04/06).
V = {
 "S01": dict(k="black"),
 "S02": dict(k="chat", msgs=[["me", "ريييم!! لقيت المكان 😍", "7:12"], ["me", "📷 📷 📷  🔗 الرابط", "7:12"], ["me", "بصي: نطلع الخميس بعد الشغل ونرجع السبت بالليل، والحجز لسه متاح لو أكدنا النهارده. قوليلي رأيك!!", "7:12"]]),
 "S03": dict(k="chat", top="بعد 40 دقيقة", msgs=[["me", "بصي: نطلع الخميس بعد الشغل… قوليلي رأيك!!", "7:12"], ["them", "تمام.", "7:52"]]),
 "S04": dict(k="inner", thoughts=["تمام بس؟", "هي زهقانة مني؟", "أكيد مش عايزة تيجي", "آخر مرة برضه ردت كده…"], counter=[22, 0]),
 "S05": dict(k="chat", typing=True, counter=[22, 0], msgs=[["them", "تمام.", "7:52"], ["me", "خلاص يا ستي لو مش عايزة تيجي قولي من الأول بدل تمام دي 🙂", "7:53"]]),
 "S06": dict(k="chat", freeze=68, msgs=[["them", "تمام.", "7:52"], ["me", "خلاص يا ستي لو مش عايزة تيجي قولي من الأول بدل تمام دي 🙂", "7:53"], ["them", "إيه ده؟؟ أنا كنت بقول تمام عادي 😅 مالك؟", "7:53"]]),
 "S07": dict(k="question", q="المشكلة حصلت فين؟", qa=90, chips=[["في الرسالة؟", 93, ""], ["في ريم؟", 94, ""], ["جوّه نور؟", 96, "gold"]]),
 "S08": dict(k="split3", panels=[["«تمام.»", "", ""], ["نور", "", "sil"], ["🧠", "", "red"]], big="كلمة واحدة ← رواية"),
 "S09": dict(k="prompt", text="افتكر آخر رسالة قلبت يومك.", icon="💬"),
 "S10": dict(k="icons", ovl=True, items=["👁", "🎥", "•  •", "🙂🙂", "💬", "⎸"]),
 "S11": dict(k="shadow", ovl=True),
 "S12": dict(k="title", series="رحلة الذكاء العاطفي", ep="الحلقة 1 · تمام."),
 "S13": dict(k="split3", panels=[["زهقت منّي", "حزن 70", "70"], ["بتستهبل عليّا؟", "غضب 75", "75"], ["أكيد مشغولة", "هدوء 15", "15"]]),
 "S14": dict(k="big", text="الرسالة واحدة ← 3 مشاعر", gold=True),
 "S15": dict(k="big", ovl=True, text="زهقت «منّي» · بتستهبل «عليّا»", gold=True, small=True),
 "S16": dict(k="list", head="حفلة: عينه ورا كتفك", items=["قليل الذوق ← ضيق", "أنا مملّ ← زعل", "مكسوف ← تعاطف"], src="Mind Over Mood · p.16"),
 "S17": dict(k="exercise", chat="عايز أشوفك بكرة.", prompt="3 تفسيرات؟", boxes=["هيرفدني", "مسؤولية جديدة", "سؤال في الشغل"], fill=274),
 "S18": dict(k="metro", stations=["شفت", "حكيت لنفسي", "حسّيت", "عملت"], blur=1),
 "S19": dict(k="metro", stations=["«تمام.» 7:52", "هي زهقانة منّي", "زعل + غضب", "رد فيه عتاب"], rewind=True),
 "S20": dict(k="five", items=["موقف", "أفكار", "مشاعر", "جسم", "تصرف"]),
 "S21": dict(k="card", ovl=True, text="طب لو حد ظلمني فعلًا… هل غضبي مجرد قصة في دماغي؟"),
 "S22": dict(k="metro", ovl=True, stations=["شفت", "الحكاية", "حسّيت", "عملت"], glow=1, src="Crucial Conversations · p.98–101 · Mind Over Mood · p.7–8"),
 "S23": dict(k="camcom"),
 "S24": dict(k="game", cards=[["ردّت بعد 40 دقيقة بكلمة واحدة", "cam", 478], ["هي مش مهتمة", "com", 487], ["المدير رفع صوته", "cam", 492], ["المدير بيكرهني", "com", 496], ["جوزي بصّ في الموبايل وأنا بتكلم", "cam", 500], ["جوزي مش فارق معاه", "com", 505]]),
 "S25": dict(k="blur", sharp="بصّ في الموبايل", soft="مش فارق معاه"),
 "S26": dict(k="big", text="تقدر تشوفها أو تسمعها؟", sub="👁  👂   ·   اتنين هيشوفوها زي بعض؟"),
 "S27": dict(k="twocol", prompt="إيه اللي كان في دماغك قبلها بثانية؟", cols=["🎥 سجّلت إيه؟", "🎙 قال إيه؟"]),
 "S28": dict(k="big", ovl=True, small=True, text="🎥 بتسجّل · 🎙 بيحكم"),
 "S29": dict(k="wires", wires=["تمام بس؟", "زهقانة منّي", "مش عايزة تيجي", "آخر مرة برضه…"], hot="أنا تقيلة عليها", hotAt=620, temp=80),
 "S30": dict(k="court", pro=[["ردّت بكلمة", 656], ["اتأخرت آخر مرة", 659]], con=[["هي اقترحت السفر", 664], ["بتبعتلي كل يوم", 669], ["مختصرة في الشغل", 672]]),
 "S31": dict(k="big", text="لو صاحبتك قالتها… هتقولّها إيه؟", temp=[80, 50]),
 "S32": dict(k="court", empty=True, label="دليلين مع · دليلين ضد"),
 "S33": dict(k="big", ovl=True, small=True, text="فرضية ≠ حكم", src="Mind Over Mood · p.61–75"),
 "S34": dict(k="glasses", phases=[[747, "dark", "هي زهقت منّي"], [754, "rose", "أكيد بتحبني ومفيش أي مشكلة"], [785, "clear", "الرسالة · 7:52 · نور متضايقة"]], src="Mind Over Mood · p.23 · p.98–99 · p.106"),
 "S35": dict(k="swap"),
 "S36": dict(k="template", noor=["صحيح إن ريم ردّت بكلمة…", "وكمان بترد كده لما بتبقى مشغولة. أسألها بدل ما أفترض."], clearAt=831),
 "S37": dict(k="rewind", newAt=872, temp=[80, 35]),
 "S38": dict(k="ink", title="الزوجة الثانية · 1967"),
 "S39": dict(k="columns", strikeAt=950),
 "S40": dict(k="harm", factAt=976, src="Crucial Conversations · p.107 · Mind Over Mood · p.24"),
 "S41": dict(k="couch"),
 "S42": dict(k="meeting"),
 "S43": dict(k="title", series="الحلقة الجاية", ep="الحلقة 2 · الإنذار"),
}
slides = [dict(id=k, a=times[k][0], b=times[k][1], **V[k]) for k in sorted(times, key=lambda x: int(x[1:]))]
assert len(slides) == 43
extra_src = [dict(a=sec("09:13"), text="Mind Over Mood · p.72–73 · Crucial Conversations · p.105 · NVC · Ch.3")]

data = dict(total=sec(rt["total"]), scenes=scenes, slides=slides, segs=segs, lines=lines, extraSrc=extra_src)
tpl = (HERE / "e01_preview_template.html").read_text(encoding="utf-8")
out = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
(EP / "12_E01_PREVIEW.html").write_text(out, encoding="utf-8")
print("slides", len(slides), "lines", len(lines), "segs", len(segs), "total", data["total"])
