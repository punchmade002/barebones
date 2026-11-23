"""Flag point-link packages that look rushed or default-filled (one-off audit, not production)."""
import json, glob, os, statistics as st
rows = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'point-links', 'bio*.json'))):
    if f.endswith('.bak'): continue
    r = json.load(open(f)); sid = os.path.basename(f)[:-5]
    vals = list(r.values()); n = len(vals)
    c2 = sum(v['cost'] == 2 for v in vals) / n
    dens = sum(len(v['needs']) for v in vals) / n
    run = best = 0
    for v in vals:  # longest run of untouched-looking items
        run = run + 1 if v['cost'] == 1 and not v['needs'] else 0
        best = max(best, run)
    rows.append((sid, n, c2, dens, best))
mc, sc = st.mean(r[2] for r in rows), st.pstdev(r[2] for r in rows)
md, sd = st.mean(r[3] for r in rows), st.pstdev(r[3] for r in rows)
print(f'{len(rows)} packages; cost-2 rate {mc:.0%}±{sc:.0%}, links/item {md:.2f}±{sd:.2f}')
for sid, n, c2, dens, best in rows:
    why = []
    if c2 < mc - 2 * sc: why.append(f'cost-2 {c2:.0%}')
    if dens < md - 2 * sd: why.append(f'links/item {dens:.2f}')
    if best >= 15 and best / n > 0.3: why.append(f'{best}/{n} untouched-looking in a row')
    if why: print(f'  FLAG {sid} ({n} items): ' + ', '.join(why))
