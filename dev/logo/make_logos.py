"""Generate three black-and-white hex logo candidates for nakagami."""
import numpy as np
from scipy.stats import nakagami

W, H = 518, 600  # hex sticker aspect (pointy top)
cx, cy, R = W / 2, H / 2, 290

def hexpts(r):
    a = np.deg2rad(np.arange(6) * 60 - 90)
    return " ".join(f"{cx + r*np.cos(t):.1f},{cy + r*np.sin(t):.1f}" for t in a)

def path(xs, ys):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))

def svg(body, bg, fg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs><clipPath id="hx"><polygon points="{hexpts(R-14)}"/></clipPath></defs>
<polygon points="{hexpts(R-7)}" fill="{bg}" stroke="{fg}" stroke-width="14" stroke-linejoin="round"/>
<g clip-path="url(#hx)">{body}</g>
</svg>'''

def curve(m, x0, x1, y0, sx, sy, xmax=2.6):
    x = np.linspace(0.001, xmax, 300)
    d = nakagami.pdf(x, m)
    return x0 + (x / xmax) * (x1 - x0), y0 - d * sy

# --- A: family of densities, white hex, latin wordmark
body = ""
for m, w in [(0.5, 5), (1, 5), (2, 5), (5, 5)]:
    xs, ys = curve(m, 70, 450, 380, None, 115)
    body += f'<path d="{path(xs, ys)}" fill="none" stroke="black" stroke-width="{w}" stroke-linecap="round"/>'
body += '<line x1="62" y1="382" x2="456" y2="382" stroke="black" stroke-width="6"/>'
body += f'<text x="{cx}" y="455" font-family="DejaVu Sans" font-weight="bold" font-size="62" text-anchor="middle">nakagami</text>'
open("logo_A_densities.svg", "w").write(svg(body, "white", "black"))

# --- B: black hex, radio mast + Nakagami-faded carrier, kana wordmark
rng = np.random.default_rng(7)
t = np.linspace(0, 1, 1400)
# smooth fading envelope: sum of a few random sinusoids -> |complex gain|
g = sum(rng.normal() * np.exp(2j*np.pi*(f*t + rng.uniform())) for f in rng.uniform(0.8, 2.5, 4))
env = np.abs(g); env = env / env.max()
sig = env * np.sin(2*np.pi*16*t)
xs = 40 + t * 438; ys = 360 - 62 * sig
body = f'<path d="{path(xs, ys)}" fill="none" stroke="white" stroke-width="4"/>'
body += f'<path d="{path(xs, 360-64*env)}" fill="none" stroke="white" stroke-width="5" stroke-dasharray="2 9" stroke-linecap="round"/>'
body += f'<path d="{path(xs, 360+64*env)}" fill="none" stroke="white" stroke-width="5" stroke-dasharray="2 9" stroke-linecap="round"/>'
# mast
mx, my = cx, 110
body += f'<path d="M{mx-38},{my+150} L{mx},{my} L{mx+38},{my+150} M{mx-25},{my+100} L{mx+25},{my+100} M{mx-13},{my+50} L{mx+13},{my+50}" fill="none" stroke="white" stroke-width="7" stroke-linejoin="round"/>'
body += f'<circle cx="{mx}" cy="{my}" r="9" fill="white"/>'
for r in (30, 52, 74):
    for s in (-1, 1):
        a0, a1 = np.deg2rad(-35), np.deg2rad(35)
        x0, y0 = mx + s*r*np.cos(a0), my + r*np.sin(a0)
        x1, y1 = mx + s*r*np.cos(a1), my + r*np.sin(a1)
        body += f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 {1 if s>0 else 0} {x1:.1f},{y1:.1f}" fill="none" stroke="white" stroke-width="6" stroke-linecap="round"/>'
body += f'<text x="{cx}" y="500" font-family="Noto Sans Mono CJK JP" font-weight="bold" font-size="78" fill="white" text-anchor="middle">なかがみ</text>'
open("logo_B_fading.svg", "w").write(svg(body, "black", "black"))

# --- C: filled density with lightning bolt, nod to the old radio logo
xs, ys = curve(1.5, 40, 478, 422, None, 200, xmax=2.8)
area = path(xs, ys) + f" L{xs[-1]:.1f},420 L{xs[0]:.1f},420 Z"
body = f'<path d="{area}" fill="black"/>'
bolt = "M318,95 L258,215 L298,215 L240,345 L352,190 L310,190 L360,95 Z"
body += f'<path d="{bolt}" fill="white" stroke="black" stroke-width="9" stroke-linejoin="miter"/>'
body += f'<rect x="0" y="420" width="{W}" height="200" fill="black"/>'
body += f'<text x="{cx}" y="505" font-family="Noto Sans Mono CJK JP" font-weight="bold" font-size="74" fill="white" text-anchor="middle">なかがみ</text>'
open("logo_C_bolt.svg", "w").write(svg(body, "white", "black"))
