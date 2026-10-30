"""Builds the profile README graphics.

Run from the profile repo root:  python assets/build.py <fonts-dir>
<fonts-dir> holds the Google Fonts latin variable files jbm.woff2 (JetBrains Mono)
and bric.woff2 (Bricolage Grotesque). Each SVG embeds only the glyphs it uses.
"""
import base64
import io
import math
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

FONT_DIR = Path(sys.argv[1])
OUT = Path(__file__).parent

# name -> (file, axis location, css family)
FONTS = {
    "mono": ("jbm.woff2", {"wght": 400}, "HRMono"),
    "monob": ("jbm.woff2", {"wght": 700}, "HRMonoB"),
    "sans": ("bric.woff2", {"opsz": 24, "wght": 420}, "HRSans"),
    "display": ("bric.woff2", {"opsz": 96, "wght": 800}, "HRDisplay"),
}
FALLBACK = {
    "mono": "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace",
    "sans": "-apple-system,Segoe UI,Helvetica,Arial,sans-serif",
}
_cache = {}


def font(key):
    if key not in _cache:
        f, loc, _ = FONTS[key]
        t = TTFont(FONT_DIR / f)
        t = instancer.instantiateVariableFont(t, loc)
        _cache[key] = t
    return _cache[key]


def width(key, text, size, spacing=0.0):
    t = font(key)
    cmap, hmtx = t.getBestCmap(), t["hmtx"]
    upm = t["head"].unitsPerEm
    w = sum(hmtx[cmap.get(ord(c), cmap[ord("?")])][0] for c in text)
    return w * size / upm + spacing * len(text)


def wrap(key, text, size, maxw):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if width(key, trial, size) > maxw and cur:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur]


def font_face(key, chars):
    buf = io.BytesIO()
    t = TTFont(io.BytesIO(_bytes(key)))
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga", "calt"]
    sub = subset.Subsetter(opts)
    sub.populate(text="".join(sorted(set(chars))) + " ")
    sub.subset(t)
    t.flavor = "woff2"
    t.save(buf)
    fam = FONTS[key][2]
    data = base64.b64encode(buf.getvalue()).decode()
    return f"@font-face{{font-family:{fam};src:url(data:font/woff2;base64,{data}) format('woff2')}}"


def _bytes(key):
    b = io.BytesIO()
    t = font(key)
    t.flavor = None
    t.save(b)
    return b.getvalue()


class SVG:
    def __init__(self, w, h, label):
        self.w, self.h, self.label = w, h, label
        self.parts, self.used, self.css = [], {}, []

    def text(self, x, y, s, key, size, fill, anchor="start", spacing=0, cls="", extra=""):
        self.used.setdefault(key, set()).update(s)
        fam = FONTS[key][2]
        fb = FALLBACK["mono" if key.startswith("mono") else "sans"]
        ls = f' letter-spacing="{spacing}"' if spacing else ""
        c = f' class="{cls}"' if cls else ""
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam},{fb}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{ls}{c}{extra}>{escape(s)}</text>'
        )

    def add(self, s):
        self.parts.append(s)

    def save(self, name):
        faces = "".join(font_face(k, v) for k, v in self.used.items())
        reduce = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-label="{escape(self.label)}">'
            f"<title>{escape(self.label)}</title>"
            f"<style>{faces}{''.join(self.css)}{reduce}</style>"
            + "".join(self.parts)
            + "</svg>"
        )
        (OUT / name).write_text(svg)
        print(f"{name}: {len(svg) / 1024:.0f} KB")


# ---------------------------------------------------------------- palettes
LIGHT = dict(
    bg="#f4f7f5", panel="#ffffff", ink="#0f1a15", muted="#5b6b63", line="#d5dfd9",
    grid="#dce6e0", green="#1a7f37", amber="#b35900", blue="#326ce5", red="#cf222e",
)
DARK = dict(
    bg="#0b1110", panel="#111917", ink="#e8efeb", muted="#8b9a93", line="#24312c",
    grid="#1a2622", green="#3fb950", amber="#e3a03f", blue="#5b8def", red="#ff7b72",
)
TERM = dict(
    bg="#0a0f0d", bar="#141c19", ink="#d7e2dc", muted="#6f8079", green="#3fb950",
    amber="#e3a03f", cyan="#56d4dd", blue="#7ea6ff", red="#ff7b72", line="#1f2a26",
)

# ---------------------------------------------------------------- data
# (project, merged, in review); order sets the spoke positions around the wheel
WHEEL = [
    ("PipeCD", 5, 6), ("KEDA", 2, 0), ("kgateway", 1, 1), ("Prowler", 1, 1),
    ("Kubeflow", 1, 1), ("Kyverno", 6, 2), ("Volcano", 1, 5),
]
MERGED = sum(m for _, m, _ in WHEEL)
IN_REVIEW = 21

FIXES = [
    ("kyverno", "cli-namespaced-vpol-noop", "#17608", "2026-09-17", "CLI passed policies it never evaluated"),
    ("keda", "external-scaler-grpc-leak", "#8193", "2026-09-22", "pooled gRPC connections never closed"),
    ("pipecd", "ecs-rollback-stale-synced", "#7412", "2026-10-03", "rollback said Synced on the old revision"),
    ("volcano", "ufm-config-crashloop", "#6057", "2026-10-08", "one config typo crash-looped 3 controllers"),
    ("pipecd", "terraform-cancel-lock", "#7440", "2026-10-11", "cancel left the remote state lock held"),
    ("kyverno", "mpol-patch-webhook-panic", "#17620", "2026-10-21", "one policy panicked the mutating webhook"),
    ("kubeflow", "optjob-invalid-names", "#4155", "2026-10-28", "invalid jobs accepted that could never run"),
    ("prowler", "split-cidr-open-sg", "#13191", "2026-10-29", "0.0.0.0/1 + 128.0.0.0/1 never flagged open"),
    ("kgateway", "tls-san-type-mismatch", "#14760", "2026-10-30", "SPIFFE and IP backends got 503 on every call"),
]

POP = (
    "@keyframes pop{from{opacity:0;transform:scale(.2)}to{opacity:1;transform:scale(1)}}"
    ".pop{transform-box:fill-box;transform-origin:center;animation:pop .45s cubic-bezier(.3,1.6,.5,1) both}"
    "@keyframes rise{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}"
    ".rise{animation:rise .5s ease-out both}"
    "@keyframes blink{50%{opacity:0}}.blink{animation:blink 1.1s steps(1) infinite}"
    "@keyframes breathe{50%{opacity:.35}}.breathe{animation:breathe 3.2s ease-in-out infinite}"
)


# ---------------------------------------------------------------- hero
def hero(p, name):
    W, H = 1000, 420
    s = SVG(W, H, f"Harsh Raj. Finds bugs in Kubernetes controllers, schedulers and policy engines and fixes them upstream. "
                  f"{MERGED} merged pull requests across {len(WHEEL)} projects, {IN_REVIEW} more in review.")
    s.css.append(POP)
    s.add(f'<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
          f'<circle cx="2" cy="2" r="1.1" fill="{p["grid"]}"/></pattern>'
          f'<clipPath id="r"><rect width="{W}" height="{H}" rx="20"/></clipPath></defs>')
    s.add(f'<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="{p["bg"]}"/>'
          f'<rect width="{W}" height="{H}" fill="url(#dots)"/></g>')
    s.add(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="{p["line"]}"/>')

    x = 56
    s.text(x, 74, "$", "monob", 14, p["green"])
    s.text(x + 16, 74, "kubectl describe engineer harsh-raj", "mono", 14, p["muted"])
    cx = x + 16 + width("mono", "kubectl describe engineer harsh-raj ", 14)
    s.add(f'<rect class="blink" x="{cx:.1f}" y="62" width="8" height="15" fill="{p["green"]}"/>')

    s.text(x - 4, 170, "Harsh Raj", "display", 96, p["ink"], spacing=-2.5)
    tag = ("I find the bugs that hide in Kubernetes controllers, schedulers and policy engines, "
           "then fix them upstream.")
    for i, line in enumerate(wrap("sans", tag, 22, 400)):
        s.text(x, 214 + i * 31, line, "sans", 22, p["muted"])

    stats = [(str(MERGED), "MERGED UPSTREAM", p["green"]), (str(len(WHEEL)), "PROJECTS", p["ink"]),
             (str(IN_REVIEW), "IN REVIEW", p["amber"])]
    sx = x
    for num, label, col in stats:
        s.text(sx, 345, num, "display", 50, col, spacing=-1)
        s.text(sx + 2, 372, label, "mono", 11, p["muted"], spacing=1.6)
        sx += max(width("display", num, 50), width("mono", label, 11, 1.6)) + 40

    # the wheel: seven spokes, one per project with a merge, like the Kubernetes helm
    cx, cy, R = 737, 220, 124
    n = len(WHEEL)
    pts = []
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    s.add(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{p["panel"]}" '
          f'fill-opacity=".7" stroke="{p["line"]}" stroke-width="1.5" stroke-linejoin="round"/>')
    delay = 0.3
    for i, (proj, m, r) in enumerate(WHEEL):
        a = math.radians(-90 + i * 360 / n)
        ca, sa = math.cos(a), math.sin(a)
        s.add(f'<line x1="{cx + 30*ca:.1f}" y1="{cy + 30*sa:.1f}" x2="{pts[i][0]:.1f}" y2="{pts[i][1]:.1f}" '
              f'stroke="{p["line"]}" stroke-width="1.5"/>')
        for k in range(m + r):
            d = 38 + k * 7.6
            px, py = cx + d * ca, cy + d * sa
            style = f' style="animation-delay:{delay:.2f}s"'
            if k < m:
                s.add(f'<circle class="pop"{style} cx="{px:.1f}" cy="{py:.1f}" r="3.3" fill="{p["green"]}"/>')
            else:
                s.add(f'<circle class="pop"{style} cx="{px:.1f}" cy="{py:.1f}" r="2.9" fill="{p["bg"]}" '
                      f'stroke="{p["amber"]}" stroke-width="1.5"/>')
            delay += 0.06
        lr = R + 14
        lx, ly = cx + lr * ca, cy + lr * sa + 4
        anchor = "middle" if abs(ca) < 0.3 else ("start" if ca > 0 else "end")
        if sa < -0.9:
            ly -= 4
        if sa > 0.5:
            ly += 8
        s.text(lx, ly, proj, "monob", 12, p["ink"], anchor=anchor)
        s.text(lx, ly + 15, f"{m} merged" + (f" · {r} open" if r else ""), "mono", 10.5, p["muted"], anchor=anchor)
    s.add(f'<circle class="breathe" cx="{cx}" cy="{cy}" r="27" fill="{p["blue"]}" fill-opacity=".18"/>')
    s.add(f'<circle cx="{cx}" cy="{cy}" r="19" fill="{p["blue"]}"/>')
    s.add(f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="#ffffff" stroke-width="2.4"/>')

    lx, LY = W - 32, 44
    s.text(lx, LY, "in review", "mono", 11, p["muted"], anchor="end")
    s.add(f'<circle cx="{lx - width("mono", "in review", 11) - 10:.1f}" cy="{LY - 4}" r="3" fill="none" '
          f'stroke="{p["amber"]}" stroke-width="1.5"/>')
    mx = lx - width("mono", "in review", 11) - 26
    s.text(mx, LY, "merged", "mono", 11, p["muted"], anchor="end")
    s.add(f'<circle cx="{mx - width("mono", "merged", 11) - 10:.1f}" cy="{LY - 4}" r="3.6" fill="{p["green"]}"/>')
    s.save(name)


# ---------------------------------------------------------------- terminal
def terminal():
    t = TERM
    size, lh = 14, 30
    cw = width("mono", "M", size)
    cols = [("NAMESPACE", 11), ("NAME", 27), ("PR", 8), ("STATUS", 8), ("MERGED", 12), ("IMPACT", 0)]
    W = 1000
    top = 44
    H = top + 40 + lh * (len(FIXES) + 1) + 100
    s = SVG(W, H, "Terminal: kubectl get fixes. " + "; ".join(
        f"{ns} {pr} merged {d}: {imp}" for ns, _, pr, d, imp in FIXES))
    s.css.append(POP)
    s.add(f'<defs><clipPath id="w"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>')
    s.add(f'<g clip-path="url(#w)"><rect width="{W}" height="{H}" fill="{t["bg"]}"/>'
          f'<rect width="{W}" height="{top}" fill="{t["bar"]}"/></g>')
    s.add(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{t["line"]}"/>')
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        s.add(f'<circle cx="{24 + i*20}" cy="{top/2}" r="6" fill="{c}"/>')
    s.text(W / 2, top / 2 + 4, "harsh@control-plane: ~", "mono", 12, t["muted"], anchor="middle")

    x0 = 32
    y = top + 40
    cmd = "kubectl get fixes -A --field-selector status=merged --sort-by=.status.mergedAt"
    s.text(x0, y, "$", "monob", size, t["green"])
    cmdx = x0 + 2 * cw
    cmdw = width("mono", cmd, size)
    s.text(cmdx, y, cmd, "mono", size, t["ink"])
    n = len(cmd)
    s.css.append(f"@keyframes type{{from{{transform:none}}to{{transform:translateX({cmdw + 12:.1f}px)}}}}"
                 f".type{{animation:type 1.6s steps({n}) .2s both}}")
    s.add(f'<rect class="type" x="{cmdx - 1:.1f}" y="{y - 18}" width="{W - cmdx:.1f}" height="26" '
          f'fill="{t["bg"]}" style="transform:translateX({W:.1f}px)"/>')

    def row(y, values, colors, keys, delay):
        s.add(f'<g class="rise" style="animation-delay:{delay:.2f}s">')
        x = x0
        for (label, wch), v, c, k in zip(cols, values, colors, keys):
            s.text(x, y, v, k, size, c)
            x += wch * cw
        s.add("</g>")

    y += lh + 8
    base = 1.8
    row(y, [c for c, _ in cols], [t["muted"]] * 6, ["mono"] * 6, base)
    for i, (ns, nm, pr, d, imp) in enumerate(FIXES):
        y += lh
        row(y, [ns, nm, pr, "Merged", d, imp],
            [t["blue"], t["ink"], t["amber"], t["green"], t["muted"], t["ink"]],
            ["mono", "mono", "mono", "monob", "mono", "mono"], base + 0.15 + i * 0.12)
    end = base + 0.3 + len(FIXES) * 0.12
    y += lh + 10
    s.add(f'<g class="rise" style="animation-delay:{end:.2f}s">')
    s.text(x0, y, f"# {len(FIXES)} of {MERGED} merged shown, {IN_REVIEW} more in review", "mono", size, t["muted"])
    s.add("</g>")
    y += lh
    s.add(f'<g class="rise" style="animation-delay:{end + .2:.2f}s">')
    s.text(x0, y, "$", "monob", size, t["green"])
    s.add(f'<rect class="blink" x="{x0 + 2*cw:.1f}" y="{y - 13}" width="{cw:.1f}" height="17" fill="{t["green"]}"/>')
    s.add("</g>")
    s.save("terminal.svg")


# ---------------------------------------------------------------- project cards
PROJECTS = [
    ("sigstore-guard", "Go · admission webhook",
     "Rejects pods whose images carry no Sigstore signature from an accepted signer."),
    ("aws-misconfig-scanner", "Python · cloud security",
     "Read-only AWS scanner with 32 checks mapped to CIS and Security Hub."),
    ("phishnet", "Python · machine learning",
     "Cross-modal attention model for explainable, real-time phishing detection."),
]


def card(p, proj, meta, desc, name):
    W, H = 400, 232
    s = SVG(W, H, f"{proj}: {desc}")
    s.add(f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="16" fill="{p["panel"]}" '
          f'stroke="{p["line"]}" stroke-width="1.5"/>')
    s.add(f'<rect x="28" y="30" width="22" height="4" rx="2" fill="{p["green"]}"/>')
    s.text(28, 66, meta.upper(), "mono", 13, p["muted"], spacing=1.2)
    size = 36
    while width("display", proj, size, -0.8) > W - 90:
        size -= 1
    s.text(26, 112, proj, "display", size, p["ink"], spacing=-0.8)
    for i, line in enumerate(wrap("sans", desc, 18, W - 56)):
        s.text(28, 152 + i * 26, line, "sans", 18, p["muted"])
    s.add(f'<path d="M{W-48} 44 l12 -12 M{W-46} 32 h10 v10" fill="none" stroke="{p["ink"]}" '
          f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    s.save(name)


# ---------------------------------------------------------------- contact pills
CONTACT = [("web", "harshrajdebug.in"), ("mail", "harshrajdebug@gmail.com"), ("in", "linkedin/harsh2789")]


def pill(p, key, label, name):
    size = 14
    tw = width("mono", label, size)
    W, H = int(tw + 76), 46
    s = SVG(W, H, label)
    s.add(f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="{H/2-1}" fill="{p["panel"]}" '
          f'stroke="{p["line"]}" stroke-width="1.5"/>')
    s.add(f'<circle cx="24" cy="{H/2}" r="5" fill="{p["green"]}"/>')
    s.text(40, H / 2 + 5, label, "mono", size, p["ink"])
    ax = 40 + tw + 12
    s.add(f'<path d="M{ax:.1f} {H/2+5} l9 -9 M{ax+2:.1f} {H/2-4} h7 v7" fill="none" stroke="{p["muted"]}" '
          f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    s.save(name)


if __name__ == "__main__":
    for mode, pal in (("light", LIGHT), ("dark", DARK)):
        hero(pal, f"hero-{mode}.svg")
        for proj, meta, desc in PROJECTS:
            card(pal, proj, meta, desc, f"card-{proj}-{mode}.svg")
        for key, label in CONTACT:
            pill(pal, key, label, f"contact-{key}-{mode}.svg")
    terminal()
