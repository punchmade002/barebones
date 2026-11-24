"""Draw a worked example's figure for the maths Learn page as a clean SVG, with every position computed, not guessed.

    import sys; sys.path.insert(0, '/Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn')
    from figlib import Fig
    f = Fig(x=(-3, 5), y=(-25, 25))               # a co-ordinate plane (or Fig() for a plain 320x240 canvas in pixels)
    f.axes(ticks=1)
    f.plot(lambda x: x**3 - 3*x**2 - 9*x + 5)
    f.point((-1, 10), 'max (−1, 10)', colour=2)
    svg = f.svg()

Colours: None is the pencil grey; 1–4 are the page's highlight colours (the same slot colours as the working);
'muted' is light grey. Lengths in px are screen pixels; everything else is in the figure's own units.
"""
import math
from xml.sax.saxutils import escape

PENCIL, MUTED = 'var(--pencil, #3d3a36)', '#a8a29a'


def colour(c):
    return PENCIL if c is None else MUTED if c == 'muted' else f'var(--hl{c})'


def tint(c):
    return '#ece9e3' if c in (None, 'muted') else f'var(--hl{c}-bg)'


class Fig:
    def __init__(self, x=None, y=None, w=320, h=240, equal=False, pad=26):
        """x=(xmin, xmax), y=(ymin, ymax) makes a co-ordinate plane drawn in w x h pixels; equal=True keeps
        circles round (one unit is the same length on both axes, and h is adjusted to fit). Without x and y
        the figure is a plain canvas whose units are pixels, y downwards."""
        self.coords = x is not None
        self.x0, self.x1 = x or (0, w)
        self.y0, self.y1 = y or (0, h)
        if self.coords and equal:
            h = w * (self.y1 - self.y0) / (self.x1 - self.x0)
        self.w, self.h, self.pad, self.items = w, h, pad, []

    # ── positions ──
    def P(self, p):
        x, y = p
        if not self.coords:
            return x, y
        return (x - self.x0) / (self.x1 - self.x0) * self.w, (self.y1 - y) / (self.y1 - self.y0) * self.h

    def scale(self):
        """pixels per unit along x (for radii on an equal-scale plane)"""
        return self.w / (self.x1 - self.x0) if self.coords else 1

    def _stroke(self, c, width, dash):
        return f'style="stroke:{colour(c)};fill:none" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"' + (f' stroke-dasharray="{dash}"' if dash else '')

    def _path(self, pts, close=False):
        return 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ('Z' if close else '')

    # ── drawing ──
    def axes(self, ticks=None, xlabel='x', ylabel='y', numbers=True):
        """x and y axes through the origin (or along the edge when 0 is off the figure); ticks every `ticks` units."""
        ox = min(max(0, self.x0), self.x1)
        oy = min(max(0, self.y0), self.y1)
        self.line((self.x0, oy), (self.x1, oy), width=1.5, arrow=True)
        self.line((ox, self.y0), (ox, self.y1), width=1.5, arrow=True)
        ax, ay = self.P((self.x1, oy)); self.text((self.x1, oy), xlabel, dx=10, dy=4, italic=True, anchor='start')
        self.text((ox, self.y1), ylabel, dx=7, dy=-4, italic=True, anchor='start')
        if ticks:
            k = math.ceil(self.x0 / ticks)
            while k * ticks <= self.x1:
                v = k * ticks
                if abs(v) > 1e-9:
                    px, py = self.P((v, oy))
                    self.items.append(f'<path d="M{px:.1f},{py - 3:.1f}L{px:.1f},{py + 3:.1f}" {self._stroke(None, 1.2, None)}/>')
                    if numbers: self.text((v, oy), num(v), dy=16, size=11, colour='muted')
                k += 1
            k = math.ceil(self.y0 / ticks)
            while k * ticks <= self.y1:
                v = k * ticks
                if abs(v) > 1e-9:
                    px, py = self.P((ox, v))
                    self.items.append(f'<path d="M{px - 3:.1f},{py:.1f}L{px + 3:.1f},{py:.1f}" {self._stroke(None, 1.2, None)}/>')
                    if numbers: self.text((ox, v), num(v), dx=-7, dy=4, size=11, colour='muted', anchor='end')
                k += 1
        return self

    def plot(self, f, a=None, b=None, colour=None, width=2.4, dash=None, steps=400):
        """y = f(x) from a to b; the pen lifts where f is undefined or jumps off the figure."""
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        span, runs, run = self.y1 - self.y0, [], []
        for i in range(steps + 1):
            x = a + (b - a) * i / steps
            try:
                y = f(x)
                ok = y == y and abs(y) != math.inf and self.y0 - span < y < self.y1 + span
            except (ZeroDivisionError, ValueError, OverflowError):
                ok = False
            if ok and run and abs(y - run[-1][1]) > span:
                ok = False
            if ok:
                run.append((x, y))
            elif run:
                runs.append(run); run = []
        if run: runs.append(run)
        clip = f'clip{len(self.items)}'
        x0, y0 = self.P((self.x0, self.y1)); x1, y1 = self.P((self.x1, self.y0))
        self.items.append(f'<clipPath id="{clip}"><rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/></clipPath>')
        for r in runs:
            if len(r) > 1:
                self.items.append(f'<path d="{self._path([self.P(p) for p in r])}" {self._stroke(colour, width, dash)} clip-path="url(#{clip})"/>')
        return self

    def shade(self, f, a, b, g=None, colour=1, steps=200):
        """fill the region between y = f(x) and y = g(x) (default the x-axis) for a ≤ x ≤ b"""
        g = g or (lambda x: 0)
        top = [(a + (b - a) * i / steps, f(a + (b - a) * i / steps)) for i in range(steps + 1)]
        bot = [(x, g(x)) for x, _ in reversed(top)]
        self.items.insert(0, f'<path d="{self._path([self.P(p) for p in top + bot], True)}" style="fill:{tint(colour)};stroke:none" opacity="0.85"/>')
        return self

    def line(self, p, q, colour=None, width=2, dash=None, arrow=False):
        (x1, y1), (x2, y2) = self.P(p), self.P(q)
        self.items.append(f'<path d="M{x1:.1f},{y1:.1f}L{x2:.1f},{y2:.1f}" {self._stroke(colour, width, dash)}/>')
        if arrow:
            ang = math.atan2(y2 - y1, x2 - x1)
            pts = [(x2 - 8 * math.cos(ang + s), y2 - 8 * math.sin(ang + s)) for s in (0.4, -0.4)]
            self.items.append(f'<path d="M{pts[0][0]:.1f},{pts[0][1]:.1f}L{x2:.1f},{y2:.1f}L{pts[1][0]:.1f},{pts[1][1]:.1f}" {self._stroke(colour, width, None)}/>')
        return self

    def polygon(self, pts, colour=None, width=2, dash=None, fill=None, close=True):
        style = f'style="stroke:{colour_(colour)};fill:{tint(fill) if fill is not None else "none"}"'
        extra = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<path d="{self._path([self.P(p) for p in pts], close)}" {style} stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{extra}/>')
        return self

    def rect(self, p, q, colour=None, width=1.6, fill=None):
        """axis-aligned rectangle with opposite corners p and q (bars of a histogram, a box plot's box)"""
        (x1, y1), (x2, y2) = p, q
        return self.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], colour, width, fill=fill)

    def circle(self, c, r, colour=None, width=2, dash=None, fill=None):
        """radius in the figure's units (use equal=True on a co-ordinate plane)"""
        cx, cy = self.P(c)
        style = f'style="stroke:{colour_(colour)};fill:{tint(fill) if fill is not None else "none"}"'
        self.items.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * self.scale():.1f}" {style} stroke-width="{width}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')
        return self

    def arc(self, c, r, a0, a1, colour=None, width=2, dash=None):
        """arc of radius r (figure units) from angle a0 to a1, degrees anticlockwise from the positive x direction"""
        cx, cy = self.P(c)
        R = r * self.scale()
        n = max(8, int(abs(a1 - a0) / 3))
        pts = [(cx + R * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy - R * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        self.items.append(f'<path d="{self._path(pts)}" {self._stroke(colour, width, dash)}/>')
        return self

    def angle(self, v, p, q, label=None, colour=None, px=18):
        """mark the angle at vertex v between the rays to p and q (the smaller one) with an arc, and label it"""
        V, A, B = self.P(v), self.P(p), self.P(q)
        a0 = math.atan2(-(A[1] - V[1]), A[0] - V[0]); a1 = math.atan2(-(B[1] - V[1]), B[0] - V[0])
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        n = 16
        pts = [(V[0] + px * math.cos(a0 + d * i / n), V[1] - px * math.sin(a0 + d * i / n)) for i in range(n + 1)]
        self.items.append(f'<path d="{self._path(pts)}" {self._stroke(colour, 1.8, None)}/>')
        if label:
            m = a0 + d / 2
            self._text_px(V[0] + (px + 13) * math.cos(m), V[1] - (px + 13) * math.sin(m) + 4, label, colour=colour, size=12)
        return self

    def right_angle(self, v, p, q, px=10, colour=None):
        """the small square that marks a right angle at v"""
        V, A, B = self.P(v), self.P(p), self.P(q)
        ua = unit(A[0] - V[0], A[1] - V[1]); ub = unit(B[0] - V[0], B[1] - V[1])
        P1 = (V[0] + ua[0] * px, V[1] + ua[1] * px); P3 = (V[0] + ub[0] * px, V[1] + ub[1] * px)
        P2 = (P1[0] + ub[0] * px, P1[1] + ub[1] * px)
        self.items.append(f'<path d="{self._path([P1, P2, P3])}" {self._stroke(colour, 1.6, None)}/>')
        return self

    def ticks(self, p, q, n=1, colour=None):
        """n small marks across the middle of segment pq: segments with the same marks are equal"""
        A, B = self.P(p), self.P(q)
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        u = unit(B[0] - A[0], B[1] - A[1]); nrm = (-u[1], u[0])
        for k in range(n):
            o = (k - (n - 1) / 2) * 5
            cx, cy = mx + u[0] * o, my + u[1] * o
            self.items.append(f'<path d="M{cx - nrm[0] * 6:.1f},{cy - nrm[1] * 6:.1f}L{cx + nrm[0] * 6:.1f},{cy + nrm[1] * 6:.1f}" {self._stroke(colour, 1.6, None)}/>')
        return self

    def point(self, p, label=None, colour=None, pos='ne', r=4):
        """a dot, with an optional label placed to one side: pos is n, ne, e, se, s, sw, w or nw"""
        x, y = self.P(p)
        self.items.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{colour_(colour)}"/>')
        if label:
            dx, dy = {'n': (0, -10), 'ne': (7, -8), 'e': (9, 4), 'se': (7, 16), 's': (0, 18), 'sw': (-7, 16), 'w': (-9, 4), 'nw': (-7, -8)}[pos]
            anchor = 'middle' if pos in ('n', 's') else 'start' if 'e' in pos else 'end'
            self._text_px(x + dx, y + dy, label, colour=colour, bold=True, anchor=anchor)
        return self

    def text(self, p, s, dx=0, dy=0, anchor='middle', colour=None, size=13, bold=False, italic=False):
        x, y = self.P(p)
        return self._text_px(x + dx, y + dy, s, anchor, colour, size, bold, italic)

    def _text_px(self, x, y, s, anchor='middle', colour=None, size=13, bold=False, italic=False):
        style = f'fill:{colour_(colour)};font-family:Outfit,system-ui,sans-serif;font-size:{size}px' + (';font-weight:700' if bold else '') + (';font-style:italic' if italic else '')
        self.items.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" style="{style}">{escape(str(s))}</text>')
        return self

    def svg(self, label='Figure for the worked example'):
        p = self.pad
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-p} {-p} {self.w + 2 * p:.0f} {self.h + 2 * p:.0f}" role="img" aria-label="{escape(label)}">'
                + ''.join(self.items) + '</svg>')


def colour_(c):
    return colour(c)


def unit(x, y):
    d = math.hypot(x, y) or 1
    return x / d, y / d


def num(v):
    return (f'{v:g}' if v == int(v) else f'{v:.2g}').replace('-', '−')


if __name__ == '__main__':          # self-check: every shape renders to well-formed SVG with the positions expected
    import xml.etree.ElementTree as ET
    f = Fig(x=(-2, 4), y=(-3, 3), w=300, equal=True)
    assert f.P((-2, 3)) == (0, 0) and f.P((4, -3)) == (300, 300)
    f.axes(ticks=1).plot(lambda x: 1 / (x - 1), colour=1).shade(lambda x: x * x / 4, 0, 2, colour=2)
    f.circle((0, 0), 2, dash='4 4').arc((0, 0), 1, 0, 90).angle((0, 0), (2, 0), (0, 2), 'θ').right_angle((0, 0), (1, 0), (0, 1))
    f.ticks((0, 0), (2, 0), 2).point((1, 1), 'A', pos='sw').rect((2, 0), (3, 2), fill=3).polygon([(0, 0), (1, 2), (2, 0)])
    ET.fromstring(f.svg())
    assert num(-2.0) == '−2' and num(0.5) == '0.5'
    print('figlib ok')
