# -*- coding: utf-8 -*-
import os, sys, csv, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from series_data import EP, S, PCONCEPT_NAME
ROOT = os.path.abspath(os.path.join(HERE, '..', '..')) + '/'
OUT = ROOT + '03_INTEGRATED_FRAMEWORK/'
kb = {r['ID']: r for r in csv.DictReader(open(ROOT + '01_KNOWLEDGE_BASE/knowledge_base.csv', encoding='utf-8-sig'))}
errs = []
ids = [s[0] for s in S]
if len(ids) != len(set(ids)): errs.append('dup scene ids')
for s in S:
    if s[1] not in EP: errs.append('bad ep ' + s[0])
    for k in [x for x in s[7].split(';') if x]:
        if k not in kb: errs.append(f'{s[0]} bad KB {k}')
    for p in [x for x in s[6].split(';') if x]:
        if p not in PCONCEPT_NAME: errs.append(f'{s[0]} bad P {p}')
    if s[5] not in ('HOOK', 'PRESENTER', 'MONTAGE') and not s[8] and s[0] != 'E5-01':
        errs.append(f'{s[0]} has no source')
used_p = {p for s in S for p in s[6].split(';') if p}
missing = sorted(set(PCONCEPT_NAME) - used_p, key=lambda x: int(x[1:]))
if missing: errs.append('primary concepts not placed: ' + ','.join(missing))
print('ERRORS:', errs or 'none')
# durations
dur = collections.OrderedDict()
for e in EP: dur[e] = round(sum(s[4] for s in S if s[1] == e), 1)
total = round(sum(dur.values()), 1)
stats = dict(episodes=len(EP), total=total, avg=round(total / len(EP), 1),
             shortest=min(dur, key=dur.get), shortest_min=min(dur.values()),
             longest=max(dur, key=dur.get), longest_min=max(dur.values()), per_episode=dur,
             scenes=len(S), primary_placed=len(used_p))
json.dump(stats, open(HERE + '/series_stats.json', 'w'), ensure_ascii=False, indent=1)
def mmss(m):
    t = int(round(m * 60)); return f'{t // 60:02d}:{t % 60:02d}'
# 03 timelines
L = ['# 03_EPISODE_TIMELINES — الخطوط الزمنية للحلقات',
     '*مولَّد آليًا من `_build/series_data.py`. الأزمنة تقديرية للتخطيط (±15%) وتُضبط أثناء كتابة السكريبت؛ لا تُفرض على القصة.*', '']
for e, (title, q) in EP.items():
    L += [f'## {e} — {title} · ~{dur[e]} دقيقة', f'**السؤال المركزي:** {q}', '',
          '| من | إلى | المشهد | العنوان | المدة | نوع الإيقاع | المفاهيم الأساسية | الأقواس | حلقات مفتوحة/مغلقة |',
          '|---|---|---|---|---|---|---|---|---|']
    t = 0.0
    for s in [x for x in S if x[1] == e]:
        L.append(f'| {mmss(t)} | {mmss(t + s[4])} | {s[0]} ({s[2]}) | {s[3]} | {s[4]}د | {s[5]} | {s[6].replace(";", "، ") or "—"} | {s[12].replace(";", "، ") or "—"} | {s[13] or "—"} |')
        t += s[4]
    L.append('')
L += ['## ملخص المدد', '| الحلقة | العنوان | المدة (د) |', '|---|---|---|']
for e, (title, q) in EP.items(): L.append(f'| {e} | {title} | {dur[e]} |')
L.append(f'| **المجموع** | {len(EP)} حلقات | **{total}** |')
open(OUT + '03_EPISODE_TIMELINES.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
# 04 scene catalog
L = ['# 04_SCENE_CATALOG — كتالوج المشاهد',
     '*مولَّد آليًا. كل مشهد يحمل: الحلقة، مرجعه في معمار المرحلة 3 (`02_KNOWLEDGE_GRAPH/08`)، المدة، نوع الإيقاع، المفاهيم، المصادر، الشخصيات، البصري، التمرين، الأقواس، الحلقات المفتوحة، وملاحظات الحالة.*', '',
     '**مفتاح نوع الإيقاع:** STORY مشهد تمثيلي · DEMO عرض/تجربة · GAME لعبة تفاعلية · ANIMATION رسوم · METAPHOR استعارة بصرية · PRESENTER_STORY المقدم يحكي قصة من مصدر · DIALOGUE حوار نموذجي · BEFORE_AFTER نسختان · CASE حالة الفيلم · REVEAL كشف · RULE قاعدة قصيرة · EXERCISE تمرين · HOOK خطاف · MONTAGE مونتاج · CLOSE ختام · END_CARD بطاقة نهاية', '']
for e, (title, q) in EP.items():
    L.append(f'## {e} — {title}')
    for s in [x for x in S if x[1] == e]:
        src = '؛ '.join(f"{a.split('|')[0]} {a.split('|')[1]} [{a.split('|')[2]}]" for a in s[8]) or '— (مشهد ربط/إيقاع بلا ادعاء معرفي)'
        pc = '، '.join(f'{p} {PCONCEPT_NAME[p]}' for p in s[6].split(';') if p) or '—'
        sk = '، '.join(f"{k} {kb[k]['CONCEPT'].split('|')[0].strip()}" for k in s[7].split(';') if k) or '—'
        L += [f'### {s[0]} · {s[3]}',
              f'- **مرجع المرحلة 3:** {s[2]} · **المدة:** ~{s[4]}د · **النوع:** {s[5]}',
              f'- **المفاهيم الأساسية:** {pc}', f'- **الداعمة:** {sk}', f'- **المصادر:** {src}',
              f'- **الشخصيات:** {s[9]}', f'- **البصري:** {s[10]}', f'- **التمرين:** {s[11]}',
              f'- **الأقواس:** {s[12] or "—"} · **الحلقات:** {s[13] or "—"}']
        if s[14]: L.append(f'- **ملاحظة:** {s[14]}')
        L.append('')
open(OUT + '04_SCENE_CATALOG.md', 'w', encoding='utf-8').write('\n'.join(L))
# 05 concept -> episode
with open(OUT + '05_CONCEPT_TO_EPISODE_MAP.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['CONCEPT_ID', 'CONCEPT', 'ROLE', 'FIRST_EPISODE', 'ALL_EPISODES', 'SCENES', 'APPEARANCES', 'KB_IDS_OR_NOTE'])
    for p in sorted(PCONCEPT_NAME, key=lambda x: int(x[1:])):
        sc = [s for s in S if p in s[6].split(';')]
        eps = list(dict.fromkeys(s[1] for s in sc))
        w.writerow([p, PCONCEPT_NAME[p], 'PRIMARY', eps[0], ';'.join(eps), ';'.join(s[0] for s in sc), len(sc), 'see 02_KNOWLEDGE_GRAPH/08 §13'])
    sup = collections.defaultdict(list)
    for s in S:
        for k in [x for x in s[7].split(';') if x]: sup[k].append(s)
    for k in sorted(sup):
        sc = sup[k]; eps = list(dict.fromkeys(s[1] for s in sc))
        w.writerow([k, kb[k]['CONCEPT'].split('|')[0].strip(), 'SUPPORTING', eps[0], ';'.join(eps), ';'.join(s[0] for s in sc), len(sc), k])
# 06 source -> episode
rows = []
for s in S:
    for a in s[8]:
        book, ref, tag = a.split('|')
        rows.append([s[1], s[0], s[3], book, ref, tag, s[6].replace(';', '، '), s[7].replace(';', '، ')])
with open(OUT + '06_SOURCE_TO_EPISODE_MAP.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f); w.writerow(['EPISODE', 'SCENE', 'SCENE_TITLE', 'SOURCE', 'REFERENCE', 'USE_TAG', 'PRIMARY_CONCEPTS', 'SUPPORTING_KB']); w.writerows(rows)
bybook = collections.defaultdict(set)
for r in rows: bybook[r[3]].add(r[0])
stats['source_rows'] = len(rows); stats['books_by_episode'] = {b: sorted(v, key=lambda x: int(x[1:])) for b, v in bybook.items()}
json.dump(stats, open(HERE + '/series_stats.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
