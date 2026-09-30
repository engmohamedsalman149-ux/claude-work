"""Build the Goleman mind map: markdown (01_GOLEMAN_MIND_MAP.md) + interactive page (02_GOLEMAN_MIND_MAP.html)."""
import json, pathlib
from goleman_map_data import BOOK, PARTS, BOOKS, REL, EPISODES

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent

chapters = [c for p in PARTS for c in p["chapters"]]
n_ideas = sum(len(c["ideas"]) for c in chapters)
n_links = sum(len(c["links"]) for c in chapters)
used = [c for c in chapters if c["ep"]]
by_book = {k: sum(1 for c in chapters for l in c["links"] if l[0] == k) for k in BOOKS}
by_rel = {k: sum(1 for c in chapters for l in c["links"] if l[3] == k) for k in REL}

md = [f"# 01_GOLEMAN_MIND_MAP — خريطة كتاب «{BOOK['title']}»",
      f"**{BOOK['author']}** · {BOOK['edition']}", "",
      "**الفكرة:** الكتاب هو العمود الفقري للخريطة. كل فرع هو قسم أو فصل **بترتيب الكتاب نفسه**، وكل فصل معاه:",
      "- أهم أفكاره بالصفحة.",
      "- الكتب التانية اللي بتقول نفس الفكرة، أو بتدي أداة عملية ليها، أو بتختلف معاها.",
      "- الحلقة اللي استخدمت الفكرة في السلسلة.", "",
      "**المصادر:** الصفحات من `00_SOURCE_AUDIT/notes/GOL_notes.md`؛ الروابط من `02_KNOWLEDGE_GRAPH/03_BOOK_CROSSWALK.md` ومن مخططات الحلقات. لا صفحة مخترعة.",
      "**النسخة التفاعلية:** `02_GOLEMAN_MIND_MAP.html`.", "",
      "## الأرقام",
      "| البند | العدد |", "|---|---|",
      f"| أقسام | {len(PARTS)} (مقدمة + 5 أقسام + كلمة أخيرة) |",
      f"| فصول | {len(chapters)} |",
      f"| أفكار بالصفحة | {n_ideas} |",
      f"| روابط بالكتب التانية | {n_links} — " + " · ".join(f"{k} {v}" for k, v in by_book.items()) + " |",
      "| نوع الرابط | " + " · ".join(f"{REL[k]} {v}" for k, v in by_rel.items()) + " |",
      f"| فصول مستخدمة في السلسلة | {len(used)} من {len(chapters)} |", "",
      "**أنواع الروابط:**", "",
      "| النوع | المعنى |", "|---|---|",
      "| نفس الفكرة | كتاب تاني بيقول نفس الكلام من زاوية تانية |",
      "| الأداة العملية | Goleman بيشرح «ليه»، والكتاب التاني بيدي «إزاي» |",
      "| اختلاف | الكتب مش متفقة (D1–D7)؛ بنقول ده بأمانة |",
      "| حدود/تحفظ | كتاب تاني بيحط حدود للفكرة (غالبًا للحماية من سوء الاستخدام) |", "",
      "## الخريطة الهرمية (كل عمود = حلقة = جزء من الكتاب)", "", "```mermaid", "flowchart TD", "  R[\"«" + BOOK["title"] + "»<br/>جولمان\"]"]
CHX = {c["id"]: c for c in chapters}
for e in EPISODES:
    md.append(f'  R --> {e["id"]}["{e["id"]} · {e["title"]}"]')
    for cid in e["chapters"]:
        md.append(f'  {e["id"]} --> {cid}["{CHX[cid]["name"]} ({CHX[cid]["page"]})"]')
md += ["```", ""]
for p in PARTS:
    md += [f"## {p['name']} ({p['page']})", f"> {p['thesis']}", ""]
    for c in p["chapters"]:
        md += [f"### {c['name']} ({c['page']})", "", "**أفكار الكتاب:**", ""]
        md += [f"- {i} — {pg}" for i, pg in c["ideas"]]
        md.append("")
        if c["links"]:
            md += ["**الربط بالكتب التانية:**", "", "| الكتاب | الفكرة | المرجع | نوع الرابط |", "|---|---|---|---|"]
            md += [f"| {b} | {t} | {r} | {REL[k]} |" for b, t, r, k in c["links"]]
            md.append("")
        newep = next(e for e in EPISODES if c["id"] in e["chapters"])
        md.append(f"**حلقته في الخطة الجديدة:** {newep['id']} · {newep['title']}")
        md.append(f"**مواضع الاستخدام في الخطة القديمة:** {'، '.join(c['ep']) if c['ep'] else 'غير مستخدم'}")
        if c.get("note"):
            md.append(f"**ملاحظة:** {c['note']}")
        md.append("")
md += ["## أسماء الكتب", "", "| الرمز | الكتاب |", "|---|---|"] + [f"| {k} | {v} |" for k, v in BOOKS.items()]
(OUT / "01_GOLEMAN_MIND_MAP.md").write_text("\n".join(md) + "\n", encoding="utf-8")

data = dict(book=BOOK, parts=PARTS, books=BOOKS, rel=REL, episodes=EPISODES,
            stats=dict(chapters=len(chapters), ideas=n_ideas, links=n_links, used=len(used)))
tpl = (HERE / "map_template.html").read_text(encoding="utf-8")
(OUT / "02_GOLEMAN_MIND_MAP.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
plan = ["# 04_BOOK_LED_SERIES_PLAN — السلسلة بترتيب الكتاب",
        "**توجيه المستخدم (2026-09-30):** خريطة ذهنية هرمية للكتاب، وكل جزء منها يتشرح في حلقة، ونتطرق وإحنا بنشرح الجزء للأجزاء المتصلة بيه من بقية الكتب.", "",
        "**القرار البنيوي:**",
        "- الحلقة = جزء من الكتاب، بترتيب الكتاب نفسه.",
        "- القسم الثاني (قلب الكتاب: 6 فصول ونموذج سالوفي) اتقسم حلقتين على خط الكتاب نفسه: «أنا ومشاعري» (ف3–6) و«أنا والناس» (ف7–8).",
        "- المقدمة تفتح الحلقة 1، والكلمة الأخيرة تختم الحلقة 6.", "",
        f"**المجموع:** {len(EPISODES)} حلقات · ~{sum(e['minutes'] for e in EPISODES)} دقيقة · {len(chapters)} فصل (كل فصل في حلقة واحدة بالظبط).", "",
        "| الحلقة | الجزء من الكتاب | الفصول | ~دقيقة | السؤال | روابط بالكتب التانية |", "|---|---|---|---|---|---|"]
CHX = {c["id"]: c for c in chapters}
PX = {p["id"]: p for p in PARTS}
for e in EPISODES:
    cnt = {}
    for cid in e["chapters"]:
        for l in CHX[cid]["links"]:
            cnt[l[0]] = cnt.get(l[0], 0) + 1
    plan.append(f"| {e['id']} {e['title']} | {' + '.join(PX[x]['name'] for x in e['parts'])} | {'، '.join(CHX[c]['name'] for c in e['chapters'])} | {e['minutes']} | «{e['question']}» | {' · '.join(f'{k} {v}' for k, v in cnt.items()) or '—'} |")
plan.append("")
for e in EPISODES:
    plan += [f"## {e['id']} · {e['title']} (~{e['minutes']} د)", f"**السؤال:** «{e['question']}»", f"**المسار:** {e['spine']}", "", "**الفصول ونقاط التطرق للكتب التانية:**", ""]
    for cid in e["chapters"]:
        c = CHX[cid]
        plan.append(f"- **{c['name']}** ({c['page']})")
        for b, txt, r, k in c["links"]:
            plan.append(f"  - {b} — {txt} ({r}) · {REL[k]}")
        if not c["links"]:
            plan.append("  - لا رابط مباشر؛ يُشرح من الكتاب وحده")
    plan += ["", "**قصص وأدوات جاهزة من الشغل اللي فات (تُعاد تسكينها):** " + "، ".join(e["reuse"]), ""]
plan += ["## أثر التغيير على الشغل اللي فات",
         "- **ما يُعاد استخدامه:** كل القصص الخيالية (نور، كريم، سلمى ويوسف، صابر وداليا، عادل)، والأدوات (الكاميرا، الترمومتر، القالب، الاستراحة، جملة الحد)، وخط عتمان، وحراس الدقة، وخريطة المصادر.",
         "- **ما يتغير:** ترتيب الحلقات وعددها (10 ← 6)، وحدود كل حلقة. الكتاب يصبح معلنًا: كل حلقة تبدأ بمكانها على الخريطة.",
         "- **حزمة الحلقة 1 الحالية** (`05_FULL_SCRIPT/E01`): مادتها (نور والكاميرا) تتوزع على E1 الجديدة (النوبة والـ40 ثانية) وE2 الجديدة (الكاميرا و«فكّر كامل» تحت ف5–6 وف9). تحتاج إعادة كتابة بعد اعتماد الخطة.",
         "- **قواعد ثابتة:** «Dark EQ» مصطلح من المشروع لا من الكتاب؛ الكتاب يقول إن المهارات «يمكن استخدامها للإضرار» (ص167). لا IQ≈20% كحقيقة، ولا تجربة الحلوى كسبب، ولا إحصاءات أمريكية. لا تشخيص لعتمان.", ""]
(OUT / "04_BOOK_LED_SERIES_PLAN.md").write_text("\n".join(plan), encoding="utf-8")
print("chapters", len(chapters), "ideas", n_ideas, "links", n_links, by_book, by_rel, "used", len(used))
