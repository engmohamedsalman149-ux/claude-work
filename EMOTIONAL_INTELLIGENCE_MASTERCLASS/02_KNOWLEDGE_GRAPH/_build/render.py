# -*- coding: utf-8 -*-
import os, csv, json, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import N
from roles import SUPPORTING, EXCLUDED_REASON, DEFAULT_REASON, PRIMARY
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')) + '/'
OUT=ROOT+'02_KNOWLEDGE_GRAPH/'
st=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stats.json')))
rows=list(csv.DictReader(open(OUT+'02b_GRAPH_NODES.csv',encoding='utf-8-sig')))
rel=list(csv.DictReader(open(OUT+'02_CONCEPT_RELATIONSHIPS.csv',encoding='utf-8-sig')))
kb={r['ID']:r for r in csv.DictReader(open(ROOT+'01_KNOWLEDGE_BASE/knowledge_base.csv',encoding='utf-8-sig'))}
cls=collections.Counter(r['RELATIONSHIP_CLASS'] for r in rel if r['GRAPH_LAYER'] not in ('CASE','REJECTED'))
case=sum(1 for r in rel if r['GRAPH_LAYER']=='CASE'); rej=sum(1 for r in rel if r['GRAPH_LAYER']=='REJECTED')
LV={1:'الأساس',2:'التنظيم الداخلي',3:'فهم الآخر',4:'التواصل',5:'الضغط العالي',6:'الوعي الدفاعي',7:'التكامل'}
def node_table():
    h='| ID | م | المفهوم | النوع | المجال | الوسم | المصدر (الصفحة) | KB | CT | الدور القصصي | المشهد |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
    for r in rows:
        role=r['STORY_ROLE']+(f" ({r['PRIMARY_CONCEPT']})" if r['PRIMARY_CONCEPT'] else '')
        h+=f"| {r['NODE_ID']} | {r['LEVEL']} | {r['CONCEPT_AR']} | {r['NODE_TYPE']} | {r['DOMAIN']} | {r['SOURCE_TAG']} | {r['SOURCE']} — {r['PAGE']} | {r['KB_IDS'].replace(';','، ')} | {r['CT_ROWS'].replace(';','، ') or '—'} | {role} | {r['STORY_SCENE'] or '—'} |\n"
    return h
def level_summary():
    by=collections.defaultdict(list)
    for r in rows: by[int(r['LEVEL'])].append(r)
    h='| المستوى | الاسم | العقد | عدد | الأنواع |\n|---|---|---|---|---|\n'
    for l in range(1,8):
        rs=by[l]; t=collections.Counter(r['NODE_TYPE'] for r in rs)
        h+=f"| {l} | {LV[l]} | "+'، '.join(f"{r['NODE_ID']} {r['CONCEPT_AR']}" for r in rs)+f" | {len(rs)} | "+'، '.join(f'{k}:{v}' for k,v in t.items())+' |\n'
    h+='\n**ملاحظة ربط بمستويات الطلب:** «الضغط» و«التأثير القائم على الخوف» و«انتهاك الحدود» في المستوى 6 ليست عقدًا مستقلة بل **مجموعات**: الضغط = N62–N75؛ التأثير بالخوف = N63، N64، N72؛ انتهاك الحدود = N75 + N80. «الوقفة التكتيكية» = نفس العقدة N18 مطبقة في المسار الدفاعي (R: N18 APPLIES_TO N105) — لم تُنشأ عقدة مكررة.\n'
    return h
def hubs():
    h='| العقدة | المفهوم | عدد الروابط المصنفة |\n|---|---|---|\n'
    for k,n,v in st['hubs'][:10]: h+=f'| {k} | {n} | {v} |\n'
    return h
def supporting():
    h='| KB | المفهوم | المشهد | كيف يظهر (≤ 60 ث) |\n|---|---|---|---|\n'
    for k,(sc,how) in sorted(SUPPORTING.items()):
        h+=f"| {k} | {kb[k]['CONCEPT'].split('|')[0].strip()} | {sc} | {how} |\n"
    return h
def excluded():
    ex=[k for k in kb if k not in PRIMARY and k not in SUPPORTING]
    h=f'**العدد: {len(ex)} مدخلًا** (من 142). الأساسي: {len(PRIMARY)} مدخلًا تشكّل 28 مفهومًا أساسيًا؛ الداعم: {len(SUPPORTING)}.\n\n| KB | المفهوم | سبب الاستبعاد من السرد الرئيسي |\n|---|---|---|\n'
    for k in ex: h+=f"| {k} | {kb[k]['CONCEPT'].split('|')[0].strip()} | {EXCLUDED_REASON.get(k,DEFAULT_REASON)} |\n"
    return h
rep={'{{NODE_TABLE}}':node_table(),'{{LEVEL_SUMMARY}}':level_summary(),'{{HUBS}}':hubs(),
     '{{C_D}}':str(cls['DIRECT_SOURCE_RELATIONSHIP']),'{{C_P}}':str(cls['CROSS_BOOK_PARALLEL']),'{{C_X}}':str(cls['CROSS_BOOK_DIFFERENCE']),
     '{{C_S}}':str(cls['INTEGRATED_SYNTHESIS']),'{{C_U}}':str(rej),'{{C_CASE}}':str(case),
     '{{SUPPORTING_TABLE}}':supporting(),'{{EXCLUDED_TABLE}}':excluded()}
for k,v in st['by_type'].items(): rep['{{T_%s}}'%k]=str(v)
for k,v in st['by_domain'].items(): rep['{{D_%s}}'%k]=str(v)
for k,v in st['by_tag'].items(): rep['{{G_%s}}'%k]=str(v)
def fill(src,dst):
    s=open(src,encoding='utf-8').read()
    for k,v in rep.items(): s=s.replace(k,v)
    left=[x for x in s.split('{{')[1:]]
    if left: print('UNFILLED',dst,[x[:20] for x in left])
    open(dst,'w',encoding='utf-8').write(s)
fill(os.path.join(os.path.dirname(os.path.abspath(__file__)), 't01.md'),OUT+'01_MASTER_KNOWLEDGE_GRAPH.md')
fill(OUT+'08_STORY_ARCHITECTURE.md',OUT+'08_STORY_ARCHITECTURE.md')
print(dict(cls),case,rej)
