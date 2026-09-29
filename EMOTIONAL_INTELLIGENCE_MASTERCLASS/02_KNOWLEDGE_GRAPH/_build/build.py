# -*- coding: utf-8 -*-
import os, csv, re, json, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import N, E, R, F
from roles import PRIMARY, SUPPORTING, NODE2P
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')) + '/'
OUT = ROOT + '02_KNOWLEDGE_GRAPH/'
kb = {r['ID']: r for r in csv.DictReader(open(ROOT + '01_KNOWLEDGE_BASE/knowledge_base.csv', encoding='utf-8-sig'))}
ct_rows = {int(r['#']) for r in csv.DictReader(open(ROOT + '00_SOURCE_AUDIT/concept_table.csv', encoding='utf-8-sig'))}
ALLOWED = {'CAUSES','LEADS_TO','ENABLES','REQUIRES','REINFORCES','EXPLAINS','CONTRASTS_WITH','COMPLEMENTS',
           'APPLIES_TO','PROTECTS_AGAINST','REINTERPRETS','PRACTICES','TRANSITIONS_TO','SYNTHESIZES'}
TAG = {'DIRECT_SOURCE_RELATIONSHIP':'[DIRECT_SOURCE_RELATIONSHIP]','CROSS_BOOK_PARALLEL':'[CROSS_BOOK_PARALLEL]',
       'CROSS_BOOK_DIFFERENCE':'[CROSS_BOOK_DIFFERENCE]','INTEGRATED_SYNTHESIS':'[INTEGRATED_SYNTHESIS]',
       'EXTERNAL_KNOWLEDGE':'[EXTERNAL_KNOWLEDGE]','UNSUPPORTED':'[UNSUPPORTED]'}
errs = []
nodes = {n[0]: n for n in N}
if len(nodes) != len(N): errs.append('duplicate node ids')
def chk_kb(s, where):
    for k in [x for x in s.split(';') if x]:
        if k not in kb: errs.append(f'{where}: bad KB {k}')
def chk_ct(s, where):
    for c in [x for x in s.split(';') if x]:
        if int(c) not in ct_rows: errs.append(f'{where}: bad CT {c}')
for n in N:
    chk_kb(n[10], n[0]); chk_ct(n[11], n[0])
    if n[9] not in ('DIRECT_SOURCE','CROSS_BOOK','INTEGRATED_SYNTHESIS','USER_FRAMEWORK','FICTIONAL_CASE_STUDY'): errs.append(n[0]+' tag')
seen = set()
for i, e in enumerate(E):
    f, rel, t, cls = e[0], e[1], e[2], e[3]
    if f not in nodes or t not in nodes: errs.append(f'edge {i} bad node {f}->{t}')
    if rel not in ALLOWED: errs.append(f'edge {i} bad rel {rel}')
    if cls not in TAG: errs.append(f'edge {i} bad class')
    chk_kb(e[7], f'edge {i}'); chk_ct(e[8], f'edge {i}')
    key = (f, rel, t, e[4])
    if key in seen: errs.append(f'dup edge {key}')
    seen.add(key)
for r in R:
    chk_kb(r[7], 'rej'); chk_ct(r[8], 'rej')
# ---- case edges (film -> concept); status inherited from F
Fd = {f[0]: f for f in F}
CASE = [
 ("F03","APPLIES_TO","N63","التهديد بتلفيق تهمة لفرض قرار = تخويف محسوب لا نوبة غضب (Gol ص160–161)"),
 ("F03","APPLIES_TO","N75","طلاق تحت التهديد = امتثال لا موافقة (CC p.23؛ NVC L640–642)"),
 ("F03","APPLIES_TO","N64","صاحب السلطة الاقتصادية/الإدارية يفرض قراره (Gol ص213–214؛ CC p.198–200)"),
 ("F04","APPLIES_TO","N68","توظيف مرجعية دينية لإضفاء شرعية (KZ p.172؛ NVC L666–742)"),
 ("F02","APPLIES_TO","N92","الحاجة الوحيدة المسموح نسبتها للشخصية: الرغبة المعلنة في وريث"),
 ("F05","APPLIES_TO","N82","استعادة قدر من السيطرة (Gol ص283–284) — حل درامي لا نموذج واقعي"),
 ("F06","APPLIES_TO","N79","إتلاف الأوراق المزورة في النهاية: من يملك «الورق» يملك الرواية الرسمية — قراءة المشروع"),
 ("F07","APPLIES_TO","N70","الفقر والأمية كأرضية للاعتمادية (KZ p.54–55؛ MoM p.172–173)"),
 ("F08","APPLIES_TO","N74","ضمير يعترض ثم يُسكَت (Gol ص157–159)"),
 ("F09","APPLIES_TO","N64","الاستيلاء على الإجراء الرسمي («الدفاتر») لتجاوز الاعتراض"),
 ("F10","APPLIES_TO","N68","اقتباس النص المقدس لإنهاء النقاش"),
 ("F11","APPLIES_TO","N71","صمت الجماعة يمنح الشرعية (Gol ص225–227)"),
 ("F11","APPLIES_TO","N76","العجز ← الاستسلام بدل الغضب (MoM p.256؛ Gol ص283)"),
]
for c in CASE:
    if c[0] not in Fd or c[2] not in nodes: errs.append('case edge '+str(c))
print('ERRORS:', errs if errs else 'none')
def role(n):
    if n[0] in NODE2P: return 'PRIMARY'
    ks = {x for x in n[10].split(';') if x}
    if ks & (PRIMARY | set(SUPPORTING)) or n[5] == 'FRAMEWORK' or n[4] in ('CASE','FRAME'): return 'SUPPORTING'
    return 'LIBRARY'
# ---- write CSV
cols = ['REL_ID','FROM_ID','FROM_CONCEPT','RELATION','TO_ID','TO_CONCEPT','RELATIONSHIP_CLASS','SOURCE','CHAPTER','PAGE',
        'SOURCE_TAG','KB_IDS','CT_ROWS','EVIDENCE_OR_NOTE','GRAPH_LAYER','FILM_STATUS']
def layer(f, t):
    lv = max(nodes[f][1], nodes[t][1])
    dom = {nodes[f][5], nodes[t][5]}
    if 'DEFENSIVE' in dom: return 'DEFENSIVE'
    if lv == 7: return 'INTEGRATION'
    return 'KNOWLEDGE'
rows = []
for i, e in enumerate(E, 1):
    f, rel, t, cls, src, ch, pg, k, c, note = e
    if not note and cls == 'INTEGRATED_SYNTHESIS': note = 'تجميع من إطار المشروع/الـBrief — لا يُنسب لأي مؤلف'
    rows.append([f'R{i:03d}', f, nodes[f][2], rel, t, nodes[t][2], cls, src, ch, pg, TAG[cls], k, c, note, layer(f, t), ''])
base = len(rows)
for j, c in enumerate(CASE, 1):
    fo = Fd[c[0]]; n = nodes[c[2]]
    rows.append([f'C{j:03d}', c[0], fo[1], c[1], c[2], n[2], 'INTEGRATED_SYNTHESIS', 'FILM + '+n[6], '—', fo[4]+' ؛ '+n[8],
                 '[INTEGRATED_SYNTHESIS] [FICTIONAL_CASE_STUDY]', n[10], (n[11]+';189').strip(';'), c[3], 'CASE',
                 '[NEEDS_FILM_VERIFICATION]' if fo[2]=='NEEDS_FILM_VERIFICATION' else '[WEB_CORROBORATED — film check pending]'])
for j, r in enumerate(R, 1):
    fl = nodes[r[0]][2] if r[0] in nodes else r[0]
    tl = nodes[r[2]][2] if r[2] in nodes else r[2]
    rows.append([f'X{j:03d}', r[0], fl, r[1], r[2], tl, 'UNSUPPORTED', r[4], r[5], r[6], TAG['UNSUPPORTED'], r[7], r[8], r[9], 'REJECTED', ''])
with open(OUT + '02_CONCEPT_RELATIONSHIPS.csv', 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh); w.writerow(cols); w.writerows(rows)
# nodes CSV
with open(OUT + '02b_GRAPH_NODES.csv', 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['NODE_ID','LEVEL','CONCEPT_AR','CONCEPT_EN','NODE_TYPE','DOMAIN','SOURCE','CHAPTER','PAGE','SOURCE_TAG','KB_IDS','CT_ROWS','STORY_ROLE','PRIMARY_CONCEPT','STORY_SCENE'])
    for n in N:
        r = role(n); w.writerow(list(n[:12]) + [r, NODE2P.get(n[0],''), n[12] if r != 'LIBRARY' else ''])
# ---- stats
cls_count = collections.Counter(e[3] for e in E)
deg = collections.Counter()
for e in E: deg[e[0]] += 1; deg[e[2]] += 1
orphans = [n[0] for n in N if deg[n[0]] == 0]
used_kb = set(); used_ct = set()
for n in N:
    used_kb |= {x for x in n[10].split(';') if x}; used_ct |= {int(x) for x in n[11].split(';') if x}
stats = dict(nodes=len(N), edges=len(E), case_edges=len(CASE), rejected=len(R), by_class=dict(cls_count),
             film_items=len(F), film_needs=sum(1 for f in F if f[2]=='NEEDS_FILM_VERIFICATION'),
             film_corroborated=sum(1 for f in F if f[2]=='WEB_CORROBORATED'),
             orphans=orphans, kb_covered=len(used_kb), ct_covered=len(used_ct & ct_rows),
             by_level=dict(collections.Counter(n[1] for n in N)), by_type=dict(collections.Counter(n[4] for n in N)),
             by_domain=dict(collections.Counter(n[5] for n in N)), by_tag=dict(collections.Counter(n[9] for n in N)),
             hubs=[(k, nodes[k][2], v) for k, v in deg.most_common(15)],
             no_scene=[n[0] for n in N if not n[12]], roles=dict(collections.Counter(role(n) for n in N)), library_nodes=[n[0] for n in N if role(n)=='LIBRARY'])
json.dump(stats, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stats.json'),'w'), ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
