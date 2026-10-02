"""Labelled Bloch sphere showing H: |0> -> |+>, |1> -> |->. Neutral SVG + PNG."""
import math, os, cairosvg
HERE = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(HERE, "..", "assets", "illustrations")
W, H = 560, 520; cx, cy, R = 280, 270, 190; ey = 0.32
def P(x, y, z):   # oblique projection: x toward viewer-left-down, y right, z up
    return cx + R * (y - 0.45 * x), cy - R * (z - 0.35 * x * ey * 2)
f = lambda v: f"{v:.1f}"
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif">',
     '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#111"/></marker></defs>',
     f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#111" stroke-width="2.5"/>',
     f'<path d="M {cx-R} {cy} A {R} {R*ey} 0 0 1 {cx+R} {cy}" fill="none" stroke="#888" stroke-width="1.8" stroke-dasharray="7 6"/>',
     f'<path d="M {cx-R} {cy} A {R} {R*ey} 0 0 0 {cx+R} {cy}" fill="none" stroke="#111" stroke-width="1.8"/>']
for (a, b, lab, dx, dy) in [((0, 0, -1.1), (0, 0, 1.25), "z", 8, 0), ((0, -1.1, 0), (0, 1.3, 0), "y", 6, 5), ((-1.1, 0, 0), (1.45, 0, 0), "x", -8, 24)]:
    x1, y1 = P(*a); x2, y2 = P(*b)
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#888" stroke-width="1.5" marker-end="url(#a)"/>')
    s.append(f'<text x="{f(x2+dx)}" y="{f(y2+dy)}" font-size="20" fill="#555" font-style="italic">{lab}</text>')
pts = {"|0⟩": ((0, 0, 1), -14, -16), "|1⟩": ((0, 0, -1), -14, 34), "|+⟩": ((1, 0, 0), -70, 2), "|−⟩": ((-1, 0, 0), 12, -12)}
for lab, (v, dx, dy) in pts.items():
    x, y = P(*v); s.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="7" fill="#111"/>')
    s.append(f'<text x="{f(x+dx)}" y="{f(y+dy)}" font-size="24" fill="#111">{lab}</text>')
# H arrows: |0> -> |+>, |1> -> |->
for (a, b) in [((0, 0, 1), (1, 0, 0)), ((0, 0, -1), (-1, 0, 0))]:
    pts2 = []
    for i in range(1, 20):
        t = i / 20 * math.pi / 2; v = [a[k] * math.cos(t) + b[k] * math.sin(t) for k in range(3)]
        pts2.append(P(*[c * 0.93 for c in v]))
    d = "M " + " L ".join(f"{f(x)} {f(y)}" for x, y in pts2)
    s.append(f'<path d="{d}" fill="none" stroke="#111" stroke-width="2.5" stroke-dasharray="3 5" marker-end="url(#a)"/>')
x, y = P(0.72, 0, 0.72); s.append(f'<text x="{f(x-44)}" y="{f(y+2)}" font-size="26" font-weight="bold" fill="#111">H</text>')
x, y = P(-0.72, 0, -0.72); s.append(f'<text x="{f(x+14)}" y="{f(y+8)}" font-size="26" font-weight="bold" fill="#111">H</text>')
s.append('</svg>'); svg = "\n".join(s)
open(os.path.join(O, "bloch_sphere_hadamard.svg"), "w").write(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(O, "bloch_sphere_hadamard.png"), scale=2.5, background_color="white")
print("bloch ok")
