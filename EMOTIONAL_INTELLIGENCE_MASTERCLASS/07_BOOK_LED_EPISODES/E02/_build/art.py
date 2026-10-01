"""Line-art SVG illustrations for E02 (no <text>: labels are real slide text placed over them).
Same style as E01: round-cap strokes on the dark slide; amber = alarm/emotion, teal = thinking, pale = neutral.
"""
import math
import random

AMB, TEAL, PALE, RED, DIM = "#F2A541", "#4FBDB0", "#DCE3EC", "#E5533D", "#3A4A60"


def svg(w, h, body, label):
    return (f'<svg aria-label="{label}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def laptop_send():
    """Karim at 2 AM: email open, cursor hovering over Send; clock at 2."""
    b = f'<rect x="80" y="30" width="520" height="320" rx="18" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    b += f'<path d="M 30 360 L 650 360 L 620 400 L 60 400 Z" stroke="{PALE}" stroke-width="8" fill="#16223A"/>'
    b += "".join(f'<line x1="120" y1="{90 + i * 36}" x2="{520 - i * 50}" y2="{90 + i * 36}" stroke="{DIM}" stroke-width="6"/>' for i in range(4))
    b += f'<rect x="420" y="262" width="140" height="56" rx="12" fill="{RED}"/>'
    b += f'<path d="M 500 300 L 500 340 L 510 330 L 520 352 L 528 348 L 518 326 L 532 326 Z" fill="{PALE}" stroke="#0C1320" stroke-width="3"/>'
    b += f'<circle cx="700" cy="80" r="60" stroke="{AMB}" stroke-width="8"/><line x1="700" y1="80" x2="700" y2="40" stroke="{AMB}" stroke-width="8"/><line x1="700" y1="80" x2="735" y2="100" stroke="{AMB}" stroke-width="8"/>'
    return svg(780, 420, b, "لابتوب فيه إيميل، والماوس على زرار الإرسال، والساعة 2")


def laptop_draft():
    """Same laptop, the email saved to Drafts (payoff)."""
    b = f'<rect x="80" y="30" width="520" height="320" rx="18" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    b += f'<path d="M 30 360 L 650 360 L 620 400 L 60 400 Z" stroke="{PALE}" stroke-width="8" fill="#16223A"/>'
    b += f'<rect x="110" y="60" width="140" height="260" rx="10" fill="#16223A"/>'
    b += f'<rect x="124" y="120" width="112" height="40" rx="8" fill="#123330" stroke="{TEAL}" stroke-width="4"/>'
    b += "".join(f'<rect x="124" y="{180 + i * 40}" width="112" height="24" rx="6" fill="{DIM}"/>' for i in range(3))
    b += "".join(f'<line x1="280" y1="{90 + i * 36}" x2="{560 - i * 40}" y2="{90 + i * 36}" stroke="{DIM}" stroke-width="6"/>' for i in range(5))
    b += f'<circle cx="700" cy="80" r="60" stroke="{TEAL}" stroke-width="8"/><line x1="700" y1="80" x2="700" y2="40" stroke="{TEAL}" stroke-width="8"/><line x1="700" y1="80" x2="735" y2="100" stroke="{TEAL}" stroke-width="8"/>'
    return svg(780, 420, b, "نفس اللابتوب، والإيميل متشال في المسودات")


def countdown():
    b = ""
    for i, (x, op) in enumerate(((120, 1), (360, 0.7), (600, 0.45))):
        b += f'<circle cx="{x}" cy="120" r="100" stroke="{AMB}" stroke-width="10" opacity="{op}"/>'
    return svg(720, 240, b, "عدّاد تنازلي 3، 2، 1")


def katana():
    """Samurai sword half-drawn from its scabbard (p.72)."""
    b = f'<path d="M 60 260 L 420 120" stroke="#5A4630" stroke-width="34"/>'  # scabbard
    b += f'<path d="M 60 260 L 420 120" stroke="#B8893F" stroke-width="6" stroke-dasharray="2 40"/>'
    b += f'<path d="M 420 120 C 520 82 620 50 700 36" stroke="{PALE}" stroke-width="16"/>'  # blade
    b += f'<path d="M 430 112 C 520 78 620 48 700 36" stroke="#FFFFFF" stroke-width="3" opacity="0.7"/>'
    b += f'<ellipse cx="420" cy="120" rx="18" ry="46" transform="rotate(-21 420 120)" fill="{AMB}"/>'  # guard
    return svg(760, 300, b, "سيف ساموراي متسحب نصه من الجراب")


def observer():
    """The 'observing self' (p.73-74): a figure in the storm and a calm eye watching from above."""
    b = f'<circle cx="300" cy="300" r="52" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'
    b += f'<path d="M 220 470 C 220 380 380 380 380 470" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'
    for r in (110, 160, 210):
        b += f'<path d="M {300 - r} 330 A {r} {r * 0.55} 0 0 1 {300 + r} 330" stroke="{RED}" stroke-width="5" opacity="{1.15 - r / 240:.2f}" stroke-dasharray="18 14"/>'
    b += f'<path d="M 520 70 C 560 30 640 30 680 70 C 640 110 560 110 520 70 Z" stroke="{TEAL}" stroke-width="7" fill="#123330"/>'
    b += f'<circle cx="600" cy="70" r="20" fill="{TEAL}"/>'
    b += f'<path d="M 560 110 L 360 250 M 640 110 L 420 270" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 12" opacity="0.8"/>'
    return svg(720, 500, b, "شخص في وسط موجة غضب، وعين هادية بتراقبه من فوق")


def gauge(value, color):
    """0-100 dial."""
    cx, cy, r = 160, 160, 130
    b = f'<path d="M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r} {cy}" stroke="{DIM}" stroke-width="22"/>'
    a = math.pi * (1 - value / 100)
    x, y = cx + r * math.cos(a), cy - r * math.sin(a)
    b += f'<path d="M {cx - r} {cy} A {r} {r} 0 0 1 {x:.1f} {y:.1f}" stroke="{color}" stroke-width="22"/>'
    nx, ny = cx + (r - 40) * math.cos(a), cy - (r - 40) * math.sin(a)
    b += f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{PALE}" stroke-width="8"/><circle cx="{cx}" cy="{cy}" r="12" fill="{PALE}"/>'
    return svg(320, 180, b, f"عداد عند {value} من 100")


def swimmers():
    """Mayer's three styles (p.75): above the water / drowning / floating and not moving."""
    b = ""
    for i, (dy, col) in enumerate(((0, TEAL), (60, RED), (0, MUTE_C))):
        x = 120 + i * 360
        b += f'<path d="M {x - 110} 230 q 27 -18 55 0 t 55 0 t 55 0 t 55 0" stroke="#6E95D8" stroke-width="7"/>'
        b += f'<path d="M {x - 110} 262 q 27 -18 55 0 t 55 0 t 55 0 t 55 0" stroke="#6E95D8" stroke-width="5" opacity="0.6"/>'
        if i == 0:
            b += f'<circle cx="{x}" cy="150" r="34" stroke="{col}" stroke-width="7" fill="#123330"/><path d="M {x - 70} 190 L {x + 70} 190" stroke="{col}" stroke-width="10"/>'
        elif i == 1:
            b += f'<circle cx="{x}" cy="250" r="34" stroke="{col}" stroke-width="7" fill="#2A1414"/><path d="M {x - 40} 190 L {x - 60} 120 M {x + 40} 190 L {x + 60} 120" stroke="{col}" stroke-width="9"/>'
        else:
            b += f'<circle cx="{x}" cy="206" r="34" stroke="{col}" stroke-width="7" fill="#16223A"/><path d="M {x - 80} 222 L {x + 80} 222" stroke="{col}" stroke-width="9"/>'
    return svg(980, 300, b, "تلات أشخاص في الميه: واحد فوقها، واحد غرقان، وواحد طافي ومستسلم")


MUTE_C = "#9FB0C3"


def calendar():
    """Elliot can't choose an appointment (p.82)."""
    b = f'<rect x="30" y="40" width="460" height="380" rx="18" stroke="{PALE}" stroke-width="8" fill="#16223A"/>'
    b += f'<rect x="30" y="40" width="460" height="70" rx="18" fill="{DIM}"/>'
    b += f'<line x1="130" y1="20" x2="130" y2="70" stroke="{PALE}" stroke-width="10"/><line x1="390" y1="20" x2="390" y2="70" stroke="{PALE}" stroke-width="10"/>'
    for r in range(4):
        for c in range(5):
            x, y = 60 + c * 86, 135 + r * 70
            hl = (r, c) in ((0, 1), (1, 3), (2, 0), (3, 2))
            b += f'<rect x="{x}" y="{y}" width="66" height="50" rx="8" stroke="{AMB if hl else DIM}" stroke-width="{5 if hl else 3}" fill="{"#3A2A10" if hl else "none"}"/>'
    return svg(520, 440, b, "نتيجة فيها كذا ميعاد متعلّم ومافيش واحد متختار")


def slider(pos=0.5):
    """Suppress <-> drown, balance in the middle (p.86-87)."""
    b = f'<line x1="40" y1="80" x2="900" y2="80" stroke="{DIM}" stroke-width="16"/>'
    b += f'<line x1="40" y1="80" x2="250" y2="80" stroke="#6E95D8" stroke-width="16"/>'
    b += f'<line x1="690" y1="80" x2="900" y2="80" stroke="{RED}" stroke-width="16"/>'
    b += f'<rect x="380" y="40" width="180" height="80" rx="40" fill="#123330" stroke="{TEAL}" stroke-width="7"/>'
    return svg(940, 160, b, "مؤشر بين الكبت والانجراف، والتوازن في النص")


def duration():
    """Same onset, two tails: you don't choose when the wave hits, you influence how long it stays (p.88)."""
    b = f'<line x1="40" y1="300" x2="900" y2="300" stroke="{DIM}" stroke-width="5"/><line x1="40" y1="300" x2="40" y2="20" stroke="{DIM}" stroke-width="5"/>'
    b += f'<path d="M 40 290 L 120 290 C 150 290 160 60 200 60 C 260 60 300 140 360 250 C 400 285 460 290 520 290" stroke="{TEAL}" stroke-width="9"/>'
    b += f'<path d="M 40 290 L 120 290 C 150 290 160 60 200 60 C 260 60 320 70 420 90 C 560 120 700 150 880 170" stroke="{AMB}" stroke-width="9" stroke-dasharray="20 14"/>'
    b += f'<line x1="200" y1="20" x2="200" y2="300" stroke="{PALE}" stroke-width="3" stroke-dasharray="10 10"/>'
    return svg(940, 320, b, "موجة انفعال بتبدأ زي بعض، وبتخلص بدري أو بتفضل")


def cascade():
    """Anger builds on anger: each wave rides the tail of the previous one (p.93-94)."""
    b = f'<line x1="40" y1="340" x2="900" y2="340" stroke="{DIM}" stroke-width="5"/><line x1="40" y1="340" x2="40" y2="20" stroke="{DIM}" stroke-width="5"/>'
    base = 330
    pts = []
    for k in range(5):
        x0 = 80 + k * 160
        peak = 260 - k * 50
        b += f'<path d="M {x0} {base - k * 52} C {x0 + 30} {base - k * 52} {x0 + 40} {peak - k * 10} {x0 + 70} {peak - k * 10} C {x0 + 120} {peak - k * 10} {x0 + 140} {base - (k + 1) * 52 + 10} {x0 + 160} {base - (k + 1) * 52}" stroke="{AMB if k < 3 else RED}" stroke-width="9"/>'
        pts.append(x0 + 70)
    b += f'<line x1="40" y1="70" x2="900" y2="70" stroke="{RED}" stroke-width="3" stroke-dasharray="12 10"/>'
    return svg(940, 360, b, "موجات غضب كل واحدة راكبة على اللي قبلها لحد ما تعدّي الخط الأحمر")


def bicycle():
    b = f'<circle cx="150" cy="230" r="90" stroke="{PALE}" stroke-width="8"/><circle cx="470" cy="230" r="90" stroke="{PALE}" stroke-width="8"/>'
    b += f'<path d="M 150 230 L 260 110 L 400 110 L 470 230 M 260 110 L 310 230 L 400 110 M 310 230 L 150 230" stroke="{TEAL}" stroke-width="8"/>'
    b += f'<path d="M 240 90 L 290 90 M 400 110 L 390 70 L 430 66" stroke="{PALE}" stroke-width="8"/>'
    return svg(600, 340, b, "عجلة: تجربة زيلمان على راكبي الدراجات")


def vent():
    """Venting as pouring fuel: shouting mouth -> bigger flame (p.97-98)."""
    b = f'<path d="M 360 330 C 270 320 260 220 320 160 C 320 210 350 220 360 200 C 340 140 370 70 420 40 C 410 100 470 130 470 210 C 470 290 420 330 360 330 Z" stroke="{RED}" stroke-width="9" fill="#2A1414"/>'
    b += f'<path d="M 40 180 L 140 140 L 140 220 Z" stroke="{AMB}" stroke-width="8" fill="#3A2A10"/>'
    for i, r in enumerate((40, 80, 120)):
        b += f'<path d="M {150 + r * 0.5} {180 - r * 0.6} A {r} {r} 0 0 1 {150 + r * 0.5} {180 + r * 0.6}" stroke="{AMB}" stroke-width="6" opacity="{1 - i * 0.25}"/>'
    return svg(520, 360, b, "صوت عالي رايح على نار فبتكبر")


def exam():
    """Goleman's blue exam booklet (p.116-117)."""
    b = f'<rect x="60" y="30" width="380" height="460" rx="12" stroke="{PALE}" stroke-width="8" fill="#1E3A6E"/>'
    b += f'<rect x="120" y="90" width="260" height="70" rx="8" stroke="{PALE}" stroke-width="5" fill="#16223A"/>'
    b += "".join(f'<line x1="120" y1="{220 + i * 46}" x2="380" y2="{220 + i * 46}" stroke="#6E95D8" stroke-width="5" opacity="0.6"/>' for i in range(5))
    b += f'<circle cx="250" cy="300" r="70" stroke="{RED}" stroke-width="8" opacity="0.9"/><path d="M 210 260 L 290 340 M 290 260 L 210 340" stroke="{RED}" stroke-width="8"/>'
    return svg(500, 520, b, "كراسة امتحان زرقا فاضية")


def inverted_u():
    b = f'<rect x="300" y="20" width="300" height="360" fill="{TEAL}" opacity="0.10"/>'
    b += f'<line x1="40" y1="380" x2="900" y2="380" stroke="{DIM}" stroke-width="5"/><line x1="40" y1="380" x2="40" y2="20" stroke="{DIM}" stroke-width="5"/>'
    b += f'<path d="M 60 340 C 220 340 300 60 450 60 C 600 60 680 340 880 350" stroke="{AMB}" stroke-width="10"/>'
    b += f'<circle cx="450" cy="60" r="16" fill="{PALE}"/>'
    return svg(940, 400, b, "منحنى على شكل U مقلوب: القلق المعتدل عند القمة")


def marshmallow():
    """Mischel's test (p.120-121): one now (right) or two if you wait (left)."""
    def m(x, y):
        o = f'<path d="M {x} {y + 30} L {x} {y + 110} A 70 20 0 0 0 {x + 140} {y + 110} L {x + 140} {y + 30}" stroke="{PALE}" stroke-width="6" fill="#E6ECF2"/>'
        return o + f'<ellipse cx="{x + 70}" cy="{y + 30}" rx="70" ry="20" stroke="{PALE}" stroke-width="6" fill="#FFFFFF"/>'
    b = m(40, 120) + m(220, 120) + m(540, 120)
    b += f'<line x1="450" y1="60" x2="450" y2="300" stroke="{DIM}" stroke-width="6" stroke-dasharray="14 12"/>'
    return svg(720, 320, b, "قطعتين حلوى لو استنيت، أو قطعة واحدة دلوقتي")


def phone_no():
    """Sales calls: a stack of 'no' (p.132)."""
    b = f'<rect x="40" y="20" width="240" height="440" rx="36" stroke="{PALE}" stroke-width="8" fill="#0C1320"/>'
    for i in range(6):
        y = 70 + i * 60
        b += f'<rect x="70" y="{y}" width="180" height="44" rx="12" fill="{RED if i < 5 else TEAL}" opacity="{0.45 + i * 0.1:.2f}"/>'
    return svg(320, 480, b, "موبايل عليه مكالمات مرفوضة كتير وواحدة نجحت")


def stream():
    """Flow (p.133-134): a smooth current."""
    b = ""
    for i in range(5):
        y = 80 + i * 50
        b += f'<path d="M 20 {y} C 180 {y - 60} 320 {y + 60} 480 {y} S 780 {y - 60} 900 {y}" stroke="{TEAL}" stroke-width="{10 - i}" opacity="{1 - i * 0.15:.2f}"/>'
    return svg(920, 340, b, "تيار ميه ماشي بانسيابية")


def bubbles():
    """Two ways to explain the same failure (p.131)."""
    b = f'<path d="M 40 40 H 420 A 20 20 0 0 1 440 60 V 200 A 20 20 0 0 1 420 220 H 140 L 90 270 L 100 220 H 60 A 20 20 0 0 1 40 200 V 60 A 20 20 0 0 1 60 40 Z" stroke="{RED}" stroke-width="7" fill="#2A1414"/>'
    b += f'<path d="M 520 40 H 900 A 20 20 0 0 1 920 60 V 200 A 20 20 0 0 1 900 220 H 860 L 870 270 L 820 220 H 540 A 20 20 0 0 1 520 200 V 60 A 20 20 0 0 1 540 40 Z" stroke="{TEAL}" stroke-width="7" fill="#123330"/>'
    return svg(960, 290, b, "فقاعتين كلام: تفسيرين لنفس الفشل")
