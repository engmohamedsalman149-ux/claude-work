"""Line-art SVG illustrations for E01 (no <text>: labels are real slide text placed over them).
Style: round-cap strokes on the dark slide; amber = alarm, teal = thinking, pale = neutral.
"""
AMB, TEAL, PALE, RED, DIM = "#F2A541", "#4FBDB0", "#DCE3EC", "#E5533D", "#3A4A60"


def svg(w, h, body, label):
    return (f'<svg aria-label="{label}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def meeting():
    """Top-down meeting table: 8 seats, Karim's seat amber, Hesham at the head with sound waves."""
    b = f'<ellipse cx="450" cy="300" rx="300" ry="150" stroke="{PALE}" stroke-width="6" fill="#16223A"/>'
    seats = [(250, 120), (450, 105), (650, 120), (250, 480), (450, 495), (650, 480), (870, 300)]
    for i, (x, y) in enumerate(seats):
        col = AMB if i == 4 else PALE
        fill = "#3A2A10" if i == 4 else "#101826"
        b += f'<circle cx="{x}" cy="{y}" r="42" stroke="{col}" stroke-width="6" fill="{fill}"/>'
    # Hesham at the head (left end), holding a sheet
    b += f'<circle cx="60" cy="300" r="46" stroke="{RED}" stroke-width="7" fill="#2A1414"/>'
    b += f'<rect x="120" y="262" width="70" height="90" rx="6" stroke="{PALE}" stroke-width="5" fill="#101826"/>'
    b += "".join(f'<line x1="132" y1="{282 + i * 16}" x2="178" y2="{282 + i * 16}" stroke="{DIM}" stroke-width="4"/>' for i in range(4))
    for r in (70, 100, 130):  # voice waves toward the table
        b += f'<path d="M {60 + r * 0.7} {300 - r * 0.7} A {r} {r} 0 0 1 {60 + r * 0.7} {300 + r * 0.7}" stroke="{RED}" stroke-width="4" opacity="0.7"/>'
    return svg(920, 600, b, "اجتماع من فوق: 8 كراسي، كرسي كريم مميز، وهشام على راس الترابيزة بيتكلم")


def timer(frac=0.12):
    import math
    r, cx, cy = 150, 180, 180
    a = -math.pi / 2 + 2 * math.pi * frac
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{DIM}" stroke-width="18"/>'
    b += f'<path d="M {cx} {cy - r} A {r} {r} 0 0 1 {x:.1f} {y:.1f}" stroke="{AMB}" stroke-width="18"/>'
    b += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{AMB}" stroke-width="8"/><circle cx="{cx}" cy="{cy}" r="10" fill="{AMB}"/>'
    b += f'<rect x="{cx - 26}" y="4" width="52" height="22" rx="6" fill="{PALE}"/>'
    return svg(360, 360, b, "ساعة إيقاف: ثانيتين بس")


def motion():
    b = ""
    for i, y in enumerate((60, 110, 160)):
        b += f'<line x1="{40 + i * 30}" y1="{y}" x2="{300 + i * 20}" y2="{y}" stroke="{TEAL if i != 1 else AMB}" stroke-width="10" opacity="{0.5 + i * 0.2}"/>'
    b += f'<path d="M 360 30 L 470 110 L 360 190" stroke="{AMB}" stroke-width="14"/>'
    return svg(500, 220, b, "خطوط حركة وسهم: العاطفة أمر تشغيل")


def siren():
    b = f'<path d="M 120 300 L 120 190 A 90 90 0 0 1 300 190 L 300 300 Z" stroke="{RED}" stroke-width="10" fill="#2A1414"/>'
    b += f'<rect x="80" y="300" width="260" height="46" rx="10" stroke="{PALE}" stroke-width="8" fill="#101826"/>'
    b += f'<path d="M 160 200 A 50 50 0 0 1 210 150" stroke="{PALE}" stroke-width="8" opacity="0.6"/>'
    for ang in (-60, -30, 0, 30, 60):
        import math
        a = math.radians(ang - 90)
        b += f'<line x1="{210 + 130 * math.cos(a):.0f}" y1="{200 + 130 * math.sin(a):.0f}" x2="{210 + 185 * math.cos(a):.0f}" y2="{200 + 185 * math.sin(a):.0f}" stroke="{RED}" stroke-width="10"/>'
    return svg(420, 360, b, "لمبة طوارئ بتنور")


def phone():
    b = f'<rect x="20" y="10" width="300" height="560" rx="44" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    b += f'<rect x="130" y="28" width="80" height="12" rx="6" fill="{DIM}"/>'
    b += f'<rect x="60" y="120" width="220" height="150" rx="22" fill="#1E3A34"/>'
    b += f'<rect x="150" y="300" width="130" height="62" rx="22" fill="#2A3242"/>'
    b += f'<rect x="60" y="390" width="220" height="110" rx="22" fill="#3A2A10" stroke="{AMB}" stroke-width="4"/>'
    return svg(340, 580, b, "موبايل فيه رسالة طويلة، ورد قصير، ورد متعصب")


def detector():
    b = f'<circle cx="200" cy="120" r="100" stroke="{PALE}" stroke-width="10" fill="#16223A"/>'
    b += f'<circle cx="200" cy="120" r="56" stroke="{DIM}" stroke-width="6"/>'
    b += f'<circle cx="200" cy="120" r="14" fill="{RED}"/>'
    for r in (140, 185, 230):
        b += f'<path d="M {200 - r * 0.62:.0f} {120 + r * 0.78:.0f} A {r} {r} 0 0 0 {200 + r * 0.62:.0f} {120 + r * 0.78:.0f}" stroke="{AMB}" stroke-width="8" opacity="{1.2 - r / 250:.2f}"/>'
    return svg(400, 360, b, "حساس دخان بيصفّر")


def bedroom():
    b = f'<line x1="20" y1="40" x2="660" y2="40" stroke="{PALE}" stroke-width="8"/>'
    b += f'<rect x="60" y="300" width="320" height="70" rx="12" stroke="{PALE}" stroke-width="7" fill="#16223A"/>'
    b += f'<rect x="60" y="250" width="70" height="60" rx="14" stroke="{PALE}" stroke-width="6"/>'
    b += f'<line x1="70" y1="370" x2="70" y2="400" stroke="{PALE}" stroke-width="7"/><line x1="370" y1="370" x2="370" y2="400" stroke="{PALE}" stroke-width="7"/>'
    # falling boxes
    for x, y, rot in ((520, 120, -12), (580, 220, 18), (500, 300, -6)):
        b += f'<rect x="{x}" y="{y}" width="90" height="70" rx="6" stroke="{AMB}" stroke-width="7" fill="#3A2A10" transform="rotate({rot} {x + 45} {y + 35})"/>'
    b += f'<path d="M 470 70 L 450 110 M 640 90 L 660 130" stroke="{AMB}" stroke-width="6"/>'
    # moon
    b += f'<path d="M 230 90 A 50 50 0 1 0 290 160 A 40 40 0 1 1 230 90 Z" fill="{PALE}" opacity="0.85"/>'
    return svg(700, 420, b, "أوضة نوم بالليل وكراتين بتقع")


def notebook():
    b = f'<rect x="40" y="20" width="300" height="380" rx="10" stroke="{PALE}" stroke-width="7" fill="#16223A"/>'
    b += "".join(f'<line x1="70" y1="{80 + i * 40}" x2="310" y2="{80 + i * 40}" stroke="{DIM}" stroke-width="4"/>' for i in range(8))
    b += f'<path d="M 110 120 L 190 200 M 190 120 L 110 200" stroke="{RED}" stroke-width="10"/>'
    b += f'<path d="M 200 250 L 270 320 M 270 250 L 200 320" stroke="{RED}" stroke-width="10"/>'
    b += f'<line x1="40" y1="20" x2="40" y2="400" stroke="{AMB}" stroke-width="10"/>'
    return svg(380, 420, b, "كراسة قديمة عليها علامات حمرا")


def balance():
    b = f'<line x1="300" y1="380" x2="300" y2="120" stroke="{PALE}" stroke-width="10"/>'
    b += f'<path d="M 240 400 L 360 400" stroke="{PALE}" stroke-width="10"/>'
    b += f'<line x1="70" y1="190" x2="530" y2="70" stroke="{PALE}" stroke-width="10"/>'
    b += f'<circle cx="300" cy="128" r="14" fill="{PALE}"/>'
    b += f'<path d="M 30 190 L 110 190 L 70 260 Z" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'   # heavy alarm side (down)
    b += f'<path d="M 490 70 L 570 70 L 530 140 Z" stroke="{TEAL}" stroke-width="8" fill="#123330"/>'  # light brakes side (up)
    return svg(600, 420, b, "ميزان: كفة الإنذار نازلة وكفة الفرامل طالعة")


def fire():
    b = f'<path d="M 150 340 C 60 330 50 240 110 180 C 110 230 140 240 150 220 C 130 160 160 90 210 60 C 200 120 260 150 260 230 C 260 300 210 340 150 340 Z" stroke="{AMB}" stroke-width="9" fill="#3A2A10"/>'
    b += f'<path d="M 360 300 L 360 80 M 320 120 L 360 80 L 400 120" stroke="{RED}" stroke-width="10"/>'
    b += f'<path d="M 470 80 L 470 300 M 430 260 L 470 300 L 510 260" stroke="{TEAL}" stroke-width="10"/>'
    return svg(540, 360, b, "نار، وسهم بيكبرها وسهم بيطفيها")


def laptop():
    b = f'<rect x="80" y="30" width="460" height="290" rx="18" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    b += f'<path d="M 30 330 L 590 330 L 560 370 L 60 370 Z" stroke="{PALE}" stroke-width="8" fill="#16223A"/>'
    b += "".join(f'<line x1="120" y1="{90 + i * 34}" x2="{460 - i * 40}" y2="{90 + i * 34}" stroke="{DIM}" stroke-width="6"/>' for i in range(4))
    b += f'<rect x="380" y="240" width="130" height="54" rx="12" fill="{RED}"/>'
    b += f'<circle cx="610" cy="90" r="70" stroke="{AMB}" stroke-width="8" fill="#101826"/>'
    b += f'<line x1="610" y1="90" x2="610" y2="40" stroke="{AMB}" stroke-width="8"/><line x1="610" y1="90" x2="636" y2="75" stroke="{AMB}" stroke-width="8"/>'
    return svg(700, 400, b, "لابتوب فيه إيميل وزرار إرسال، وساعة عند 2")


def books():
    b = ""
    for x, col, tilt in ((60, "#2F8A7E", -6), (300, "#C4553D", 6)):
        b += f'<g transform="rotate({tilt} {x + 100} 200)"><rect x="{x}" y="40" width="200" height="300" rx="10" stroke="{col}" stroke-width="8" fill="#16223A"/>'
        b += f'<line x1="{x + 30}" y1="40" x2="{x + 30}" y2="340" stroke="{col}" stroke-width="6"/>'
        b += "".join(f'<line x1="{x + 60}" y1="{100 + i * 30}" x2="{x + 170}" y2="{100 + i * 30}" stroke="{DIM}" stroke-width="5"/>' for i in range(3)) + "</g>"
    b += f'<path d="M 270 20 L 290 60 L 262 60 L 284 110" stroke="{AMB}" stroke-width="8"/>'
    return svg(560, 380, b, "كتابين مختلفين وبينهم شرارة خلاف")


def frame():
    """Ornate frame with a simple landscape — stands in for the Spanish painting in Goleman's story."""
    b = f'<rect x="10" y="10" width="500" height="370" rx="6" stroke="#B8893F" stroke-width="22" fill="#2A2416"/>'
    b += f'<rect x="38" y="38" width="444" height="314" stroke="#7A5A2A" stroke-width="4" fill="#1E2B44"/>'
    b += f'<circle cx="380" cy="120" r="40" fill="{AMB}" opacity="0.85"/>'
    b += f'<path d="M 40 300 L 160 180 L 250 260 L 330 200 L 480 320 L 480 350 L 40 350 Z" fill="#2F5A55" stroke="{TEAL}" stroke-width="4"/>'
    b += f'<path d="M 470 30 L 380 380" stroke="{RED}" stroke-width="10" opacity="0.9"/>'
    return svg(520, 390, b, "لوحة في برواز، وعليها خط أحمر: اترمت")


def snow_car():
    """Goleman in the Colorado snow (p.20): car stopped, snow, crash ahead hidden."""
    b = f'<path d="M 0 330 L 700 330" stroke="{DIM}" stroke-width="6"/>'
    b += f'<path d="M 40 300 L 200 300 L 230 250 L 330 250 L 370 300 L 420 300 L 420 330 L 40 330 Z" stroke="{PALE}" stroke-width="7" fill="#16223A"/>'
    b += f'<circle cx="120" cy="335" r="26" stroke="{PALE}" stroke-width="7" fill="#101826"/><circle cx="350" cy="335" r="26" stroke="{PALE}" stroke-width="7" fill="#101826"/>'
    b += f'<path d="M 430 290 L 470 290" stroke="{AMB}" stroke-width="8"/>'  # headlights
    import random
    random.seed(4)
    for _ in range(46):
        x, y = random.randint(10, 690), random.randint(10, 240)
        b += f'<circle cx="{x}" cy="{y}" r="{random.choice((3, 4, 5))}" fill="{PALE}" opacity="0.8"/>'
    b += f'<path d="M 560 330 L 600 270 L 640 330" stroke="{RED}" stroke-width="7"/><circle cx="600" cy="300" r="5" fill="{RED}"/>'  # warning triangle ahead
    return svg(700, 370, b, "عربية واقفة في التلج، وقدامها علامة حادثة")


def building():
    """Brain as a 3-floor building (p.25–28): stem (ground), limbic (1st), neocortex (top)."""
    b = f'<path d="M 40 560 L 560 560" stroke="{PALE}" stroke-width="8"/>'
    b += f'<rect x="80" y="400" width="440" height="160" stroke="{DIM}" stroke-width="7" fill="#16223A"/>'
    b += f'<rect x="80" y="240" width="440" height="160" stroke="{AMB}" stroke-width="7" fill="#3A2A10"/>'
    b += f'<rect x="80" y="80" width="440" height="160" stroke="{TEAL}" stroke-width="7" fill="#123330"/>'
    b += f'<path d="M 60 80 L 300 10 L 540 80" stroke="{TEAL}" stroke-width="7" fill="none"/>'
    for y in (110, 270, 430):
        b += "".join(f'<rect x="{x}" y="{y}" width="60" height="50" rx="4" stroke="{PALE}" stroke-width="4" opacity="0.5"/>' for x in (120, 270, 420))
    return svg(600, 580, b, "مبنى من 3 أدوار: جذع المخ تحت، الجهاز الحوفي في النص، القشرة الجديدة فوق")


def relay():
    """Engineering analogy: protection relay trips fast; the control room reads later."""
    b = f'<rect x="30" y="120" width="220" height="260" rx="16" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'
    b += f'<path d="M 150 170 L 110 260 L 150 260 L 120 340" stroke="{AMB}" stroke-width="10" fill="none"/>'
    b += f'<rect x="420" y="80" width="300" height="200" rx="14" stroke="{TEAL}" stroke-width="8" fill="#123330"/>'
    b += "".join(f'<line x1="450" y1="{120 + i * 34}" x2="{690 - i * 50}" y2="{120 + i * 34}" stroke="{TEAL}" stroke-width="6" opacity="0.7"/>' for i in range(4))
    b += f'<path d="M 520 280 L 500 340 L 640 340 L 620 280" stroke="{TEAL}" stroke-width="7"/>'
    b += f'<path d="M 260 250 L 400 190" stroke="{DIM}" stroke-width="5" stroke-dasharray="14 12"/>'
    return svg(750, 400, b, "ريليه حماية بيفصل بسرعة، وغرفة تحكم بتقرا بعده")


def alarm_flood():
    """Control-room screen flooded with alarms (working memory freeze, p.48–49)."""
    b = f'<rect x="20" y="20" width="560" height="360" rx="18" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    import random
    random.seed(7)
    for r in range(7):
        for c in range(5):
            col = random.choice((RED, RED, AMB, DIM))
            b += f'<rect x="{50 + c * 104}" y="{50 + r * 46}" width="88" height="30" rx="6" fill="{col}" opacity="{0.55 + random.random() * 0.45:.2f}"/>'
    b += f'<path d="M 230 400 L 210 450 L 390 450 L 370 400" stroke="{PALE}" stroke-width="7"/>'
    return svg(600, 470, b, "شاشة غرفة تحكم مليانة إنذارات")


def legacy():
    """Stone-age hardware running today's software (p.19): campfire + laptop."""
    b = f'<path d="M 120 300 C 60 290 60 220 100 180 C 100 220 120 225 128 210 C 115 160 140 110 175 90 C 168 140 210 165 210 225 C 210 280 170 300 120 300 Z" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'
    b += f'<path d="M 60 320 L 230 290 M 60 290 L 230 320" stroke="{PALE}" stroke-width="10"/>'
    b += f'<path d="M 280 200 L 360 200" stroke="{DIM}" stroke-width="8"/><path d="M 340 180 L 365 200 L 340 220" stroke="{DIM}" stroke-width="8"/>'
    b += f'<rect x="420" y="90" width="300" height="190" rx="14" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    b += f'<path d="M 390 290 L 750 290 L 730 320 L 410 320 Z" stroke="{PALE}" stroke-width="8" fill="#16223A"/>'
    b += "".join(f'<rect x="{445 + i * 62}" y="120" width="48" height="36" rx="6" fill="{RED}" opacity="0.8"/>' for i in range(4))
    return svg(780, 340, b, "نار عصر الصيد ← لابتوب الشغل: نفس الجهاز، مشاكل جديدة")


def jolt():
    b = "".join(f'<line x1="300" y1="300" x2="{300 + 260 * __import__("math").cos(a):.0f}" y2="{300 + 260 * __import__("math").sin(a):.0f}" stroke="{PALE}" stroke-width="{10 if i % 2 else 5}" opacity="0.9"/>'
                for i, a in enumerate([k * 0.3927 for k in range(16)]))
    b += f'<circle cx="300" cy="300" r="90" fill="{PALE}"/>'
    return svg(600, 600, b, "وميض مفاجئ")
