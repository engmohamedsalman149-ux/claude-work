"""PHASE 5 QA: scene coverage + timing consistency between series_data.py and E##_OUTLINE.md."""
import re, sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT.parent / "03_INTEGRATED_FRAMEWORK" / "_build"))
from series_data import S, EP  # noqa

def secs(t):
    m, s = t.split(":"); return int(m) * 60 + int(s)

head = re.compile(r"^### (E\d+-\d+) · (.+?) \((\d+:\d\d)[–-](\d+:\d\d)\)")
found, rows, problems = {}, [], []
beats = {}
for f in sorted(ROOT.glob("E*_OUTLINE.md")):
    ep = "E" + str(int(f.name[1:3]))
    txt = f.read_text(encoding="utf-8")
    for tag in ["DO", "HOOK", "TURN", "REVEAL"]:
        beats.setdefault(ep, {})[tag] = len(re.findall(r"\*\*?%s\b|\] %s\b|\b%s:" % (tag, tag, tag), txt))
    for line in txt.splitlines():
        m = head.match(line)
        if m:
            sid = m.group(1)
            if sid in found: problems.append(f"duplicate heading {sid}")
            found[sid] = (f.name, secs(m.group(3)), secs(m.group(4)))

planned = {s[0]: s for s in S}
missing = [k for k in planned if k not in found]
extra = [k for k in found if k not in planned]
per_ep = {}
for sid, s in planned.items():
    if sid not in found: continue
    fn, a, b = found[sid]
    dur = (b - a) / 60
    plan = s[4]
    diff = round(dur - plan, 2)
    rows.append((sid, s[1], plan, round(dur, 2), diff))
    per_ep.setdefault(s[1], []).append((a, b, plan, dur))
    if abs(diff) > 0.05: problems.append(f"{sid}: outline {dur:.2f} vs plan {plan}")
cont = []
for ep, L in per_ep.items():
    L.sort()
    if L[0][0] != 0: cont.append(f"{ep} starts at {L[0][0]}s")
    for x, y in zip(L, L[1:]):
        if x[1] != y[0]: cont.append(f"{ep}: gap/overlap {x[1]}s→{y[0]}s")
ep_tot = {ep: round(max(b for a, b, *_ in L) / 60, 2) for ep, L in per_ep.items()}
out = {"planned": len(planned), "found": len(found), "missing": missing, "extra": extra,
       "timing_problems": problems, "continuity": cont, "episode_totals": ep_tot,
       "series_total": round(sum(ep_tot.values()), 2), "beats": beats}
print(json.dumps(out, ensure_ascii=False, indent=1))
(HERE / "outline_qa.json").write_text(json.dumps({**out, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
