"""Does each line of working show the maths that was checked? learn.py checks a line's `sym` with SymPy, but students
read its `tex`; this compares the two for every worked-example line of every skill.

  python3 texcheck.py      # prints lines whose tex and sym disagree; lines it cannot parse are only counted

shortcut: numeric comparison at random points, so a tex the LaTeX parser misreads shows up as a false alarm;
read each reported line before changing anything.
"""
import json
import random
import re
import sys
from pathlib import Path

import sympy as sp
from sympy.parsing.latex import parse_latex

HERE = Path(__file__).resolve().parent


def unwrap_hl(t):
    """\\hl{n}{body} → body, with nested braces"""
    while (k := t.find('\\hl{')) != -1:
        j = t.index('}', k) + 1                 # end of {n}
        assert t[j] == '{'
        depth, m = 0, j
        while True:
            depth += {'{': 1, '}': -1}.get(t[m], 0)
            if depth == 0:
                break
            m += 1
        t = t[:k] + t[j + 1:m] + t[m + 1:]
    return t


def clean(tex):
    t = unwrap_hl(tex)
    t = re.sub(r'\\(quad|qquad)\b.*$', '', t)               # trailing notes such as \quad (1)
    t = re.sub(r'\\text\{[^}]*\}', '', t)
    for a, b in [('&', ''), ('\\left', ''), ('\\right', ''), ('\\,', ''), ('\\!', ''), ('\\ldots', ''), ('\\dots', ''),
                 ('\\tfrac', '\\frac'), ('\\dfrac', '\\frac'), ('°', '^\\circ'), ('\\approx', '=')]:
        t = t.replace(a, b)
    return t


def sides(tex):
    """the parsed sides of a line, in two readings: degrees as a plain number, and inside trig as radians"""
    t = clean(tex)
    out = []
    for deg in (lambda m: '', lambda m: '\\cdot\\frac{\\pi}{180}'):
        u = re.sub(r'\^\{?\\circ\}?', deg, t)
        out.append([parse_latex(x) for x in re.split(r'(?<![<>!])=(?!=)', u) if x.strip()])
    return out


def same(a, b, rel=1e-6):
    """numerically equal at random points (None when it cannot tell)"""
    a = a.subs(sp.Symbol('e'), sp.E).subs(sp.Symbol('pi'), sp.pi)
    if {str(x) for x in a.free_symbols} != {str(x) for x in b.free_symbols}:
        return None                             # a substitution line: the tex still has letters the sym has filled in
    syms = sorted(b.free_symbols, key=str)
    asyms = {str(x): x for x in a.free_symbols}
    for _ in range(3):
        pt = {s: sp.Rational(random.randint(11, 97), random.randint(3, 13)) for s in syms}
        try:
            d = complex(sp.N(a.subs({asyms[str(s)]: v for s, v in pt.items()}) - b.subs(pt)))
            scale = max(1, abs(complex(sp.N(b.subs(pt)))))
        except Exception:
            return None
        if abs(d) > rel * scale:
            return False
    return True


def agrees(tex, sym):
    """True if some reading of the line matches sym: its last side, or left − right for an equation"""
    b = sp.sympify(sym, locals={'e': sp.E})
    rel = 6e-3 if re.search(r'\\approx|\\ldots|\\dots|\d\.\d', tex) else 1e-6   # rounded values
    verdicts = []
    for parts in sides(tex):
        cands = [parts[-1]] + ([parts[0] - parts[-1], parts[-1] - parts[0]] if len(parts) > 1 else [])
        verdicts += [same(c, b, rel) for c in cands]
    if True in verdicts:
        return True
    return False if False in verdicts else None


def main():
    sys.path.insert(0, str(HERE))
    from proof import sources
    random.seed(1)
    checked = unparsed = 0
    bad = []
    for sid, (f, i) in sources().items():
        o = json.loads(f.read_text())[i]
        for k, st in enumerate(o['example']['workedSolution']['steps'], 1):
            for ln in st.get('lines', []):
                if not (ln.get('tex') and ln.get('sym')):
                    continue
                try:
                    ok = agrees(ln['tex'], ln['sym'])
                except Exception:
                    ok = None
                if ok is None:
                    unparsed += 1
                    continue
                checked += 1
                if not ok:
                    bad.append((sid, k, ln['tex'], ln['sym']))
    print(f'{checked} lines compared, {unparsed} not parsed, {len(bad)} disagree')
    for b in bad:
        print(' ', b[0], 'step', b[1], '|', b[2], '| sym:', b[3])


if __name__ == '__main__':
    assert unwrap_hl(r'\hl{1}{x^{2}} + 1') == 'x^{2} + 1'
    assert agrees(r'(a) &= \hl{2}{2x} - 6 \quad (1)', '2*x-6') and agrees(r'x^2 &= 9', 'x**2-9')
    assert agrees(r'(-2x + 4x)', '-2*x-4*x') is False
    main()
