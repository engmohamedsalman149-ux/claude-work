"""Build the Goleman mind map: markdown (01_GOLEMAN_MIND_MAP.md) + interactive page (02_GOLEMAN_MIND_MAP.html)."""
import json, pathlib
from goleman_map_data import BOOK, PARTS, BOOKS, REL

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
      "## الخريطة المختصرة", "", "```mermaid", "mindmap", f"  root((«{BOOK['title']}»<br/>جولمان))"]
for p in PARTS:
    md.append(f"    {p['name']}")
    for c in p["chapters"]:
        if c["name"] != p["name"].split(": ")[-1]:
            md.append(f"      {c['name']}")
        for idea, _ in c["ideas"][:2]:
            md.append(f"        {idea[:38]}{'…' if len(idea) > 38 else ''}")
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
        md.append(f"**في السلسلة:** {'، '.join(c['ep']) if c['ep'] else 'غير مستخدم'}")
        if c.get("note"):
            md.append(f"**ملاحظة:** {c['note']}")
        md.append("")
md += ["## أسماء الكتب", "", "| الرمز | الكتاب |", "|---|---|"] + [f"| {k} | {v} |" for k, v in BOOKS.items()]
(OUT / "01_GOLEMAN_MIND_MAP.md").write_text("\n".join(md) + "\n", encoding="utf-8")

data = dict(book=BOOK, parts=PARTS, books=BOOKS, rel=REL,
            stats=dict(chapters=len(chapters), ideas=n_ideas, links=n_links, used=len(used)))
tpl = (HERE / "map_template.html").read_text(encoding="utf-8")
(OUT / "02_GOLEMAN_MIND_MAP.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print("chapters", len(chapters), "ideas", n_ideas, "links", n_links, by_book, by_rel, "used", len(used))
