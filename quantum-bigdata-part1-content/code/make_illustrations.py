"""Original line drawings for Part 1 -- neutral black/grey on white, so any slide design can restyle them.
Writes assets/illustrations/*.svg (and 3x PNG copies if cairosvg is installed: pip install cairosvg)."""
import math, os
try:
    import cairosvg  # optional: only needed for the PNG copies
except ImportError:
    cairosvg = None
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "illustrations")
INK, MID, LIGHT = "#111111", "#777777", "#cccccc"
FONT = 'font-family="DejaVu Sans, Helvetica, Arial, sans-serif"'
def T(x, y, s, size=18, anchor="middle", color=INK, weight="normal", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" text-anchor="{anchor}" fill="{color}" font-weight="{weight}"{st}>{s}</text>'
def L(x1, y1, x2, y2, w=3, color=INK, dash=None, cap="round", op=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="{cap}"{d} opacity="{op}"/>'
def ARROW(x1, y1, x2, y2, w=3, color=INK, head=11, dash=None):
    a = math.atan2(y2 - y1, x2 - x1); hx, hy = x2 - head * math.cos(a), y2 - head * math.sin(a)
    p1 = (hx + head * .55 * math.sin(a), hy - head * .55 * math.cos(a)); p2 = (hx - head * .55 * math.sin(a), hy + head * .55 * math.cos(a))
    return L(x1, y1, hx, hy, w, color, dash) + f'<path d="M {x2:.1f} {y2:.1f} L {p1[0]:.1f} {p1[1]:.1f} L {p2[0]:.1f} {p2[1]:.1f} Z" fill="{color}"/>'
def C(x, y, r, fill="none", w=3, color=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{color}" stroke-width="{w}"{d}/>'
def R(x, y, w, h, rx=0, fill="#ffffff", sw=3, color=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{color}" stroke-width="{sw}"{d}/>'
def sphere(cx, cy, r, w=3):
    ry = r * .3
    return (C(cx, cy, r, w=w) + f'<path d="M {cx-r:.1f} {cy:.1f} A {r:.1f} {ry:.1f} 0 0 1 {cx+r:.1f} {cy:.1f}" fill="none" stroke="{INK}" stroke-width="{w*.7:.1f}" stroke-dasharray="7 7" opacity="0.6"/>'
            + f'<path d="M {cx-r:.1f} {cy:.1f} A {r:.1f} {ry:.1f} 0 0 0 {cx+r:.1f} {cy:.1f}" fill="none" stroke="{INK}" stroke-width="{w*.9:.1f}"/>'
            + L(cx, cy - r, cx, cy + r, w * .7, dash="7 7", op=.6) + C(cx, cy, w * 1.6, fill=INK, w=0))
def meter(x, y, s=46):
    return (R(x, y, s, s, rx=5, sw=3) + f'<path d="M {x+s*.2:.1f} {y+s*.72:.1f} A {s*.3:.1f} {s*.3:.1f} 0 0 1 {x+s*.8:.1f} {y+s*.72:.1f}" fill="none" stroke="{INK}" stroke-width="3"/>'
            + L(x + s * .5, y + s * .72, x + s * .74, y + s * .3, 3))
def svg(name, w, h, body):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>'
    open(os.path.join(OUT, name + ".svg"), "w").write(s)
    if cairosvg: cairosvg.svg2png(bytestring=s.encode(), write_to=os.path.join(OUT, name + ".png"), scale=3)


def sine(x0, y0, w, amp, cycles=2, n=120, phase=0.0):
    pts = []
    for i in range(n + 1):
        t = i / n; pts.append(f"{x0 + w*t:.1f} {y0 - amp*math.sin(2*math.pi*cycles*t + phase):.1f}")
    return "M " + " L ".join(pts)
def P(d, w=3, color=INK, dash=None, fill="none"):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{dd}/>'
def check(x, y, s=18): return P(f"M {x-s*.5:.1f} {y:.1f} L {x-s*.1:.1f} {y+s*.4:.1f} L {x+s*.6:.1f} {y-s*.5:.1f}", 4)
def cross(x, y, s=16): return L(x-s*.5, y-s*.5, x+s*.5, y+s*.5, 4) + L(x+s*.5, y-s*.5, x-s*.5, y+s*.5, 4)

# ---------- 1 bit vs qubit (unchanged idea, plainer captions) ----------
b = ""
b += R(70, 95, 160, 64, rx=32, sw=3) + C(198, 127, 24, fill=INK, w=0) + T(52, 135, "0", 26) + T(250, 135, "1", 26)
b += T(150, 290, "Bit: a switch", 22, weight="bold") + T(150, 318, "only 0 or 1", 18, color=MID)
cx, cy, r = 500, 135, 88
b += sphere(cx, cy, r) + ARROW(cx, cy, cx + 58, cy - 62, 5) + T(cx, cy - r - 12, "0", 22, weight="bold") + T(cx, cy + r + 28, "1", 22, weight="bold")
b += T(cx, 290, "Qubit: an arrow on a sphere", 22, weight="bold") + T(cx, 318, "up = 0, down = 1, anything in between = a mix", 18, color=MID)
svg("bit_vs_qubit", 720, 340, b)

# ---------- 2 chessboard doubling (NEW, slide 2) ----------
b = ""; sq = 74; x0 = 30; y0 = 40
counts = [1, 2, 4, 8, 16, 32, 64]
for i, n in enumerate(counts):
    x = x0 + i * (sq + 8)
    b += R(x, y0, sq, sq, rx=4, fill=(LIGHT if i % 2 else "#ffffff"), sw=2)
    k = math.ceil(math.sqrt(n)); rows = math.ceil(n / k); gap = (sq - 12) / max(k, 1); rr = min(8, gap * .36)
    for j in range(n):
        cx_ = x + 6 + gap * (j % k + .5); cy_ = y0 + sq / 2 - (rows - 1) * gap / 2 + gap * (j // k)
        b += C(cx_, cy_, rr, fill=INK, w=0)
    b += T(x + sq / 2, y0 + sq + 28, str(n), 18, weight="bold")
xe = x0 + 7 * (sq + 8)
b += T(xe + 12, y0 + sq / 2 + 8, "…", 30, "start")
bw = 160; bx = xe + 50; bm = bx + bw / 2
b += R(bx, y0 - 6, bw, sq + 12, rx=4, sw=2, dash="6 5") + T(bm, y0 + 18, "square 64", 15, color=MID) + T(bm, y0 + 44, "9 billion billion", 16, weight="bold") + T(bm, y0 + 66, "grains", 16, weight="bold")
b += T(440, 205, "Rice on a chessboard: each square doubles the one before.", 19)
b += T(440, 235, "A quantum system does the same: every extra particle doubles the numbers needed.", 17, color=MID)
svg("chessboard_doubling", 880, 255, b)

# ---------- 3 superposition: hidden coin vs qubit (NEW, slide 4) ----------
b = ""
b += T(170, 36, "Hidden coin", 22, weight="bold") + T(530, 36, "Qubit in superposition", 22, weight="bold")
b += f'<ellipse cx="170" cy="190" rx="62" ry="15" fill="{LIGHT}" stroke="{INK}" stroke-width="2.5"/>'
b += P("M 110 190 L 128 88 L 212 88 L 230 190 Z", 3, fill="#ffffff") + f'<ellipse cx="170" cy="88" rx="42" ry="9" fill="#ffffff" stroke="{INK}" stroke-width="3"/>'
b += T(170, 150, "?", 34, weight="bold")
b += T(170, 295, "Already heads or tails —", 17) + T(170, 317, "we just can't see it.", 17)
b += cross(58, 34, 20) + T(170, 348, "Not how a qubit works", 16, color=MID)
cx, cy, r = 530, 160, 78
b += sphere(cx, cy, r) + ARROW(cx, cy, cx + r - 6, cy + 10, 5) + T(cx, cy - r - 10, "0", 20, weight="bold") + T(cx, cy + r + 26, "1", 20, weight="bold")
b += T(530, 295, "Genuinely undecided until read,", 17) + T(530, 317, "and the arrow also has a direction.", 17)
b += check(356, 30, 22) + T(530, 348, "How a qubit really behaves", 16, color=MID)
svg("hidden_coin_vs_qubit", 720, 365, b)

# ---------- 4 plus / minus weights (REVISED, slide 4) ----------
b = ""
for i, (title, s1) in enumerate((("plus  |+⟩", 1), ("minus  |−⟩", -1))):
    ox = 50 + i * 320; base = 150
    b += T(ox + 110, 34, title, 24, weight="bold") + L(ox, base, ox + 220, base, 2.5)
    b += R(ox + 40, base - 70, 50, 70, fill=INK, sw=0) + T(ox + 65, base - 80, "+", 24, weight="bold") + T(ox + 65, base + 26, "0", 19)
    if s1 > 0: b += R(ox + 130, base - 70, 50, 70, fill=INK, sw=0) + T(ox + 155, base - 80, "+", 24, weight="bold") + T(ox + 155, base + 26, "1", 19)
    else: b += R(ox + 130, base, 50, 70, fill=MID, sw=0) + T(ox + 155, base + 96, "−", 26, weight="bold") + T(ox + 155, base - 12, "1", 19)
b += T(320, 282, "Same size → same 50/50 when read. Only the sign differs.", 17, color=MID)
svg("plus_minus_amplitudes", 640, 300, b)

# ---------- 5 Bloch sphere (REVISED, slide 5) ----------
cx, cy, r = 250, 230, 150; rx, ry = r, r * .3
def eq(tdeg): t = math.radians(tdeg); return cx + rx * math.cos(t), cy + ry * math.sin(t)
b = sphere(cx, cy, r)
xp, yp = eq(135); xm, ym = eq(-45)
b += C(xp, yp, 7, fill=INK, w=0) + C(xm, ym, 7, fill=INK, w=0)
b += C(cx, cy - r, 7, fill=INK, w=0) + C(cx, cy + r, 7, fill=INK, w=0)
b += T(cx, cy - r - 16, "0", 26, weight="bold") + T(cx, cy + r + 34, "1", 26, weight="bold")
b += T(xp + 14, yp + 30, "plus", 20) + T(xm - 5, ym - 14, "minus", 20)
b += ARROW(cx, cy, cx - 90, cy - 95, 5)
b += T(475, 120, "Height (latitude)", 20, "start", weight="bold") + T(475, 146, "→ the chance of reading 0 or 1", 18, "start", MID)
b += T(475, 300, "Direction around (longitude)", 20, "start", weight="bold") + T(475, 326, "→ the phase", 18, "start", MID)
b += L(cx + 30, cy - 132, 470, 128, 1.5, MID, "4 5") + L(cx + 150, cy + 10, 470, 292, 1.5, MID, "4 5")
b += T(475, 200, "Equator = 50/50 mixes", 18, "start")
svg("bloch_sphere_labeled", 840, 430, b)

# ---------- 6 phase compass (NEW, slide 5) ----------
b = ""
cx, cy, r = 160, 150, 100
b += C(cx, cy, r, w=3) + C(cx, cy, 5, fill=INK, w=0) + T(cx, cy + r + 34, "The equator seen from above", 16, color=MID)
b += ARROW(cx, cy, cx + r - 4, cy, 5) + T(cx + r + 14, cy + 7, "E", 18, "start", weight="bold")
b += ARROW(cx, cy, cx - r + 4, cy, 5, MID) + T(cx - r - 14, cy + 7, "W", 18, "end", weight="bold")
b += T(cx + 50, cy - 14, "plus", 17) + T(cx - 50, cy - 14, "minus", 17, color=MID)
b += R(330, 40, 440, 95, rx=10, sw=2.5) + T(350, 72, "Ask “0 or 1?”", 19, "start", weight="bold")
b += T(350, 104, "plus → 50/50   ·   minus → 50/50", 18, "start") + T(350, 126, "They look identical.", 16, "start", MID)
b += R(330, 160, 440, 95, rx=10, sw=2.5) + T(350, 192, "Ask “east or west?”", 19, "start", weight="bold")
b += T(350, 224, "plus → always E   ·   minus → always W", 18, "start") + T(350, 246, "The phase is real information.", 16, "start", MID)
svg("phase_compass", 800, 290, b)

# ---------- 7 measurement collapse (label tweak, slide 6) ----------
b = ""
cx, cy, r = 110, 130, 80
b += sphere(cx, cy, r) + ARROW(cx, cy, cx + r - 6, cy + 8, 5) + T(cx, 250, "before: on the equator", 18)
b += ARROW(215, 130, 285, 130, 3) + meter(300, 107) + ARROW(362, 130, 432, 130, 3) + T(346, 195, "read it", 18, color=MID)
for j, (dy, lab) in enumerate(((-1, "0  (50%)"), (1, "1  (50%)"))):
    sx, sy, sr = 520, 70 + j * 125, 48
    b += sphere(sx, sy, sr, w=2.4) + ARROW(sx, sy, sx, sy + dy * (sr - 5), 4.5) + T(sx + 66, sy + 7, lab, 19, "start")
b += L(452, 118, 470, 80, 2, MID, "4 4") + L(452, 142, 470, 180, 2, MID, "4 4")
b += T(380, 280, "After reading, the arrow snaps to a pole. Everything else is lost.", 17, color=MID)
svg("measurement_collapse", 720, 295, b)

# ---------- 8 big store, small door (NEW, slide 6) ----------
b = ""
b += R(30, 30, 300, 190, rx=12, sw=3)
import random; random.seed(3)
for _ in range(260): b += C(45 + random.random() * 270, 45 + random.random() * 160, 2.6, fill=INK if random.random() < .5 else MID, w=0)
b += T(180, 250, "Inside: 2ⁿ weights at once", 18, weight="bold")
b += P("M 330 60 L 470 118 L 470 132 L 330 190", 3) + L(470, 125, 520, 125, 6)
b += T(470, 170, "the one", 15, color=MID) + T(470, 188, "exit", 15, color=MID)
for i, bit in enumerate("0110"): b += R(530 + i * 38, 106, 32, 38, rx=4, sw=2.5) + T(546 + i * 38, 132, bit, 20, weight="bold")
b += T(606, 180, "Out: n bits", 18, weight="bold")
b += T(360, 282, "Reading gives back only one bit per qubit — a huge store with a tiny door.", 17, color=MID)
svg("big_store_small_door", 720, 300, b)

# ---------- 9 water waves (NEW, slide 7) ----------
b = ""
W = 170; amp = 22
for row, (lab, ph, res) in enumerate((("In step", 0.0, "stronger"), ("Out of step", math.pi, "cancelled"))):
    y = 70 + row * 130
    b += T(20, y + 6, lab, 19, "start", weight="bold")
    b += P(sine(150, y, W, amp), 3) + T(345, y + 8, "+", 28, weight="bold")
    b += P(sine(370, y, W, amp, phase=ph), 3, MID) + T(565, y + 8, "=", 28, weight="bold")
    if row == 0: b += P(sine(590, y, W, amp * 2), 3.5)
    else: b += L(590, y, 590 + W, y, 3.5)
    b += T(590 + W / 2, y + 62, res, 16, color=MID)
b += T(400, 320, "Quantum weights add like waves: in step they grow, out of step they cancel.", 17, color=MID)
svg("water_waves", 800, 340, b)

# ---------- 10 interference paths (label tweak, slide 7) ----------
b = ""
for i, (lab, a2, res) in enumerate((("plus, then H", "+½", "= 1  → always 0"), ("minus, then H", "−½", "= 0  → never 0"))):
    y0 = 85 + i * 175
    b += T(95, y0 + 7, lab, 19, weight="bold")
    b += f'<path d="M 190 {y0} C 260 {y0-55}, 340 {y0-55}, 410 {y0-6}" fill="none" stroke="{INK}" stroke-width="3.5"/>'
    b += f'<path d="M 190 {y0} C 260 {y0+55}, 340 {y0+55}, 410 {y0+6}" fill="none" stroke="{INK if i == 0 else MID}" stroke-width="3.5" stroke-dasharray="{"none" if i == 0 else "9 6"}"/>'
    b += C(190, y0, 7, fill=INK, w=0) + C(430, y0, 22, fill="#ffffff", w=3) + T(430, y0 + 8, "0", 22, weight="bold")
    b += T(300, y0 - 52, "+½", 19) + T(300, y0 + 68, a2, 19, color=INK if i == 0 else MID)
    b += T(470, y0 + 8, res, 20, "start")
b += T(340, 372, "Two paths lead to the same result: same signs add up, opposite signs cancel.", 17, color=MID)
svg("interference_paths", 700, 392, b)

# ---------- 11 combinations grid (NEW, slide 8) ----------
b = ""
rows = (("1 qubit", ["0", "1"]), ("2 qubits", ["00", "01", "10", "11"]), ("3 qubits", [format(i, "03b") for i in range(8)]))
for i, (lab, cells) in enumerate(rows):
    y = 30 + i * 70
    b += T(20, y + 30, lab, 19, "start", weight="bold")
    for j, c in enumerate(cells): b += R(140 + j * 66, y + 4, 58, 40, rx=6, sw=2.5) + T(169 + j * 66, y + 31, c, 18)
    b += T(140 + len(cells) * 66 + 10, y + 31, f"= {len(cells)}", 19, "start", weight="bold")
b += T(20, 262, "n qubits", 19, "start", weight="bold") + T(140, 262, "→ 2ⁿ combinations, each with its own weight", 19, "start")
b += T(20, 300, "Every extra qubit doubles the list.", 16, "start", MID)
svg("combinations_grid", 760, 315, b)

# ---------- 12 Bell pair circuit (REVISED, slide 9) ----------
b = ""
for y in (50, 120): b += L(70, y, 440, y, 2.4, op=.85)
b += T(40, 57, "0", 20, weight="bold") + T(40, 127, "0", 20, weight="bold")
b += R(110, 30, 40, 40, sw=2.4) + T(130, 58, "H", 22, weight="bold")
b += L(230, 50, 230, 132, 2.4) + C(230, 50, 6, fill=INK, w=0) + C(230, 120, 13, fill="#ffffff", w=2.4) + L(217, 120, 243, 120, 2.4) + L(230, 107, 230, 133, 2.4)
b += T(230, 165, "CNOT", 16, color=MID)
b += meter(330, 28, 44) + meter(330, 98, 44)
b += T(560, 80, "always 00 or 11", 21, weight="bold") + T(560, 108, "never 01 or 10", 18, color=MID)
svg("bell_pair_circuit", 680, 180, b)

# ---------- 13 entangled pair far apart (NEW, slide 9) ----------
b = ""
for x, who in ((110, "Alice"), (650, "Bob")):
    b += sphere(x, 95, 55, w=2.6) + T(x, 185, who, 19, weight="bold")
b += P(sine(175, 95, 410, 10, cycles=6), 2.5, MID, "7 6") + T(380, 70, "1,000 km apart", 16, color=MID)
runs = (("0", "0"), ("1", "1"), ("1", "1"), ("0", "0"), ("1", "1"))
for i, (a, bb) in enumerate(runs):
    x = 210 + i * 75
    b += T(x, 150, f"{a} · {bb}", 19, weight="bold")
b += T(380, 180, "each run: always the same", 15, color=MID)
b += T(380, 232, "Each side alone sees random 0s and 1s. The link shows only when they compare.", 17, color=MID)
svg("entangled_pair_distance", 760, 250, b)

# ---------- 14 gloves in boxes (NEW, slide 10) ----------
def mitten(x, y, right=True):
    s = 1 if right else -1
    d = (f"M {x} {y+70} L {x} {y+18} Q {x} {y} {x+s*18} {y} L {x+s*30} {y} Q {x+s*48} {y} {x+s*48} {y+18} L {x+s*48} {y+70} Z")
    th = f"M {x+s*48} {y+40} Q {x+s*66} {y+30} {x+s*62} {y+48} L {x+s*48} {y+56}"
    return P(d, 3, fill="#ffffff") + P(th, 3) + L(x - s*2, y + 70, x + s*50, y + 70, 5)
b = ""
for bx, right, lab in ((60, False, "left"), (500, True, "right")):
    b += R(bx, 40, 170, 130, rx=6, sw=3) + (mitten(bx + 110, 60, False) if not right else mitten(bx + 60, 60, True)) + T(bx + 85, 196, lab + " glove", 18)
b += ARROW(250, 105, 480, 105, 2.5, MID, dash="8 6") + T(365, 92, "shipped apart", 16, color=MID)
b += T(365, 240, "Open one box and you instantly know the other.", 18) + T(365, 266, "Nothing strange: the answers were fixed from the start.", 17, color=MID)
svg("gloves_in_boxes", 730, 285, b)

# ---------- 15 no-cloning, photocopier (REVISED, slide 11) ----------
def paper(x, y): return P(f"M {x} {y} L {x+30} {y} L {x+40} {y+10} L {x+40} {y+50} L {x} {y+50} Z", 2.5, fill="#ffffff") + L(x + 8, y + 22, x + 32, y + 22, 2) + L(x + 8, y + 32, x + 32, y + 32, 2)
def mini_q(x, y): return sphere(x, y, 22, w=2) + ARROW(x, y, x + 15, y - 14, 3, head=7)
b = ""
for row, (thing, ok) in enumerate((("paper", True), ("qubit", False))):
    y = 40 + row * 120
    b += (paper(40, y) if thing == "paper" else mini_q(60, y + 25))
    b += ARROW(100, y + 25, 170, y + 25, 3) + R(175, y - 5, 150, 60, rx=10) + T(250, y + 32, "copier", 19, weight="bold") + ARROW(330, y + 25, 400, y + 25, 3)
    if thing == "paper": b += paper(415, y) + paper(470, y) + check(560, y + 25, 24) + T(600, y + 32, "bits: fine", 18, "start")
    else: b += mini_q(440, y + 25) + mini_q(500, y + 25) + L(418, y - 5, 525, y + 55, 5) + L(525, y - 5, 418, y + 55, 5) + T(560, y + 32, "qubits: impossible", 18, "start")
b += T(400, 300, "A copier that works for 0 and 1 turns a mix into a linked pair, not two copies.", 16, color=MID)
svg("no_cloning", 800, 315, b)

# ---------- 16 eavesdropper / QKD (NEW, slide 11) ----------
b = ""
b += R(20, 70, 110, 60, rx=8) + T(75, 107, "Alice", 19, weight="bold") + R(630, 70, 110, 60, rx=8) + T(685, 107, "Bob", 19, weight="bold")
b += L(130, 100, 630, 100, 2.5, MID)
for i in range(4): b += C(160 + i * 40, 100, 8, fill=INK, w=0)
b += R(330, 150, 100, 55, rx=8) + T(380, 184, "Eve", 19, weight="bold") + L(380, 150, 380, 108, 2.5) + meter(357, 212, 46)
for i in range(4):
    x = 470 + i * 40; b += C(x, 100, 8, fill="#ffffff", w=2.5)
    if i % 2 == 0: b += T(x, 80, "!", 18, weight="bold")
b += T(230, 60, "quantum signals", 15, color=MID) + T(550, 60, "disturbed", 15, color=MID)
b += T(380, 300, "Eve cannot copy the signals, so she must read them — and reading leaves errors.", 16, color=MID)
b += T(380, 324, "Alice and Bob compare a sample, see the errors, and know someone listened.", 16, color=MID)
svg("eavesdropper_qkd", 760, 340, b)

# ---------- 17 three resources + two rules (REVISED, slide 12) ----------
b = ""
items = (("Superposition", "opens up 2ⁿ possibilities"), ("Entanglement", "links qubits together"), ("Interference", "pushes toward the answer"))
for i, (h, s_) in enumerate(items):
    x = 20 + i * 262
    b += R(x, 30, 226, 110, rx=14) + T(x + 113, 78, h, 21, weight="bold") + T(x + 113, 108, s_, 15, color=MID)
    if i < 2: b += ARROW(x + 230, 85, x + 258, 85, 3)
b += R(20, 170, 750, 70, rx=14, dash="8 6", sw=2.5) + T(40, 200, "Two rules:", 18, "start", weight="bold")
b += T(160, 200, "reading gives one bit per qubit", 17, "start") + T(160, 226, "qubits cannot be copied", 17, "start")
svg("three_resources", 790, 255, b)

# ---------- 18 CHSH game (slide 10) ----------
b = ""
b += R(270, 20, 160, 56, rx=8) + T(350, 55, "Referee", 20, weight="bold")
b += R(60, 150, 150, 70, rx=8) + T(135, 192, "Alice", 20, weight="bold") + R(490, 150, 150, 70, rx=8) + T(565, 192, "Bob", 20, weight="bold")
b += ARROW(290, 78, 170, 146, 2.8) + T(206, 104, "question A or B", 15, "end") + ARROW(410, 78, 530, 146, 2.8) + T(494, 104, "question A or B", 15, "start")
b += ARROW(110, 224, 110, 268, 2.8) + T(110, 292, "answer 0 or 1", 17) + ARROW(590, 224, 590, 268, 2.8) + T(590, 292, "answer 0 or 1", 17)
b += L(350, 110, 350, 280, 3, MID, "8 7") + T(350, 305, "no talking", 16, color=MID)
b += T(350, 345, "Win if the answers match —", 17, weight="bold") + T(350, 370, "unless both got question B, then they must differ.", 17, weight="bold")
svg("chsh_game", 700, 390, b)
print("illustrations ok")
