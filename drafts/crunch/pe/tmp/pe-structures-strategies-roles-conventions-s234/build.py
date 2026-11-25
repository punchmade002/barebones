import json, re
B = '/Users/gabrielwhelan/barebones/drafts/crunch/pe/'
P = 'pe-structures-strategies-roles-conventions-'
H, E = 'helpful', 'essential'
hi, lo = 'high', 'low'

def L(x, s, why, c):  # local ref or full id
    return (x, s, why, c)

# ---------- s2 ----------
S1 = P + 's1.'
PD4 = 'pe-performance-demands-s4.'
s2 = [
 ('0.0', 1, []),
 ('0.1', 1, [(PD4+'0.0', H, 'fitness components an activity demands', hi)]),
 ('0.2', 1, []),
 ('0.3', 1, []),
 ('1.0', 1, [('0.1', H, 'physical demands of a role', hi)]),
 ('1.1', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('1.2', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('1.3', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('1.4', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('2.0', 1, [('0.1', H, 'physical demands of a role', hi)]),
 ('2.1', 1, [('0.1', H, 'physical demands of a role', hi)]),
 ('2.2', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('2.3', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('2.4', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('2.5', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('3.0', 1, [('0.1', H, 'physical demands of a role', hi)]),
 ('3.1', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('3.2', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('3.3', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('3.4', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('4.0', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('4.1', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('4.2', 1, [('0.2', H, 'personal demands of a role', hi)]),
 ('4.3', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('4.4', 1, [('0.3', H, 'technical demands of a role', hi)]),
 ('5.0', 1, []),
 ('5.1', 1, [('5.0', H, 'affiliation to a club', hi)]),
 ('5.2', 1, [('5.3', H, 'task cohesion', lo)]),
 ('5.3', 1, []),
 ('5.4', 1, []),
 ('6.0', 1, []),
 ('6.1', 1, []),
 ('6.2', 1, []),
 ('7.0', 1, [('0.0', H, 'role as specific responsibilities', hi)]),
 ('7.1', 1, []),
 ('7.2', 1, []),
 ('8.0', 1, []),
 ('8.1', 1, [('8.0', H, 'watching previous matches', hi)]),
 ('8.2', 1, [(S1+'10.1', H, 'notational analysis tallying', hi)]),
 ('8.3', 1, [('8.0', H, 'what scouting suggested', hi)]),
 ('9.b', 1, [(S1+'0.1', H, 'strategies exploiting opponent weaknesses', hi)]),
 ('9.0', 1, [(S1+'6.1', H, 'targeting the weaker side', hi)]),
 ('9.1', 1, [(S1+'4.4', H, 'playing into space behind defenders', hi)]),
 ('9.2', 1, []),
 ('9.3', 1, [(S1+'4.4', H, 'playing into space behind defenders', hi)]),
 ('9.4', 1, [(S1+'1.2.b'.replace('1.2.b','2.b'), H, 'rehearsed set play', hi)]),
 ('9.5', 1, [(S1+'5.0', H, 'pressing to force errors', hi)]),
]
# fix 9.4 id: s1.1.2.b is wrong; the real id is s1.2.b
s2[[k for k,_,_ in s2].index('9.4')] = ('9.4', 1, [(S1+'2.b', H, 'rehearsed set play', hi)])

# ---------- s3 ----------
PD6 = 'pe-performance-demands-s6.'
s3 = [
 ('0.0', 1, []), ('0.1', 1, []), ('0.2', 1, []), ('0.3', 1, []), ('0.4', 1, []),
 ('1.0', 1, []), ('1.1', 1, []), ('1.2', 1, []), ('1.3', 1, []), ('1.4', 1, []),
 ('1.5', 1, []), ('1.6', 1, []), ('1.7', 1, []),
 ('2.0', 1, []),
 ('2.1', 1, [(PD6+'1.6', H, 'dynamic stretching', hi)]),
 ('2.2', 1, []), ('2.3', 1, []), ('2.4', 1, []),
 ('3.0', 1, []), ('3.1', 1, []), ('3.2', 1, []), ('3.3', 1, []),
 ('4.0', 1, []),
 ('4.1', 1, [(PD6+'1.5', H, 'static stretching', hi)]),
 ('4.2', 1, []), ('4.3', 1, []), ('4.4', 1, []), ('4.5', 1, []), ('4.6', 1, []),
 ('5.0', 1, []), ('5.1', 1, []), ('5.2', 1, []), ('5.3', 1, []), ('5.4', 1, []),
 ('5.5', 1, []), ('5.6', 1, []), ('5.7', 1, []),
 ('5.8', 1, [('5.7', H, 'correct size and fit selection', lo)]),
 ('6.0', 1, []), ('6.1', 1, []), ('6.2', 1, []), ('6.3', 1, []), ('6.4', 1, []),
 ('6.5', 1, [('6.0', H, 'securing goals and posts', hi)]),
 ('7.0', 1, [('7.2', H, 'sprain and strain defined', lo)]),
 ('7.1', 1, []),
 ('7.2', 1, []), ('7.3', 1, []),
 ('8.0', 1, [('7.2', H, 'sprain defined', hi)]),
 ('8.1', 1, [('7.3', H, 'strain defined', hi)]),
 ('8.2', 1, [('7.0', H, 'acute injury', lo)]),
 ('8.3', 1, [('7.0', H, 'acute injury', lo)]),
 ('9.0', 2, []),
 ('9.1', 1, [('9.0', H, 'PRICE step', hi)]),
 ('9.2', 1, [('9.0', H, 'PRICE step', hi)]),
 ('9.3', 1, [('9.0', H, 'PRICE step', hi)]),
 ('9.4', 1, [('9.0', H, 'PRICE step', hi)]),
 ('9.5', 1, [('9.0', H, 'PRICE step', hi)]),
 ('9.6', 1, [('9.3', H, 'ice treatment of soft-tissue injury', lo)]),
 ('9.7', 1, []),
 ('10.0', 2, []),
 ('10.1', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.2', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.3', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.4', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.5', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.6', 1, [('10.0', H, 'SALTAPS step', hi), ('10.5', H, 'contrasts with active movement', hi)]),
 ('10.7', 1, [('10.0', H, 'SALTAPS step', hi)]),
 ('10.8', 1, [('10.0', H, 'SALTAPS steps assessed', hi)]),
 ('11.0', 1, []),
 ('11.1', 1, [('11.0', H, 'concussion signs', hi)]),
 ('11.2', 1, [('11.0', H, 'concussion', hi)]),
 ('11.3', 1, [('11.2', H, 'return to play after removal', hi)]),
 ('11.4', 1, []),
 ('11.5', 1, [('11.4', H, 'bleeding cuts', hi)]),
 ('12.0', 1, []),
 ('12.1', 1, [('12.0', H, 'overtraining', hi)]),
 ('12.2', 1, [('12.0', H, 'overtraining', hi)]),
 ('12.3', 1, [('12.0', H, 'overtraining', hi)]),
 ('13.0', 1, [('12.0', H, 'preventing overtraining', hi)]),
 ('13.1', 1, [('12.0', H, 'recovery to prevent overtraining', hi)]),
 ('13.2', 1, [(PD6+'6.0', H, 'periodisation', lo)]),
 ('13.3', 1, []),
 ('13.4', 1, []),
 ('13.5', 1, []),
 ('13.6', 1, []),
 ('13.7', 1, [('13.0', E, 'gradual weekly load progression', hi)]),
 ('13.8', 1, [('13.1', H, 'rest days and easy weeks', hi)]),
 ('13.9', 1, [('13.7', H, 'spotting load jumps', hi)]),
]

# ---------- s4 ----------
ETH2 = 'pe-ethics-fair-play-s2.'
s4 = [
 ('0.0', 1, []),
 ('0.1', 1, [('0.0', H, 'rules of an activity', hi)]),
 ('0.2', 1, [('0.0', H, 'rules and their enforcement', hi)]),
 ('0.3', 1, [('0.2', H, 'sanction such as a free kick', lo)]),
 ('0.4', 1, []),
 ('0.5', 1, []),
 ('1.0', 1, []),
 ('1.1', 1, [('1.0', H, 'rituals before an activity', hi)]),
 ('1.2', 1, [('1.0', H, 'rituals before an activity', hi)]),
 ('1.3', 1, [('1.0', H, 'rituals before an activity', hi)]),
 ('1.4', 1, [('1.0', H, 'rituals as symbolic actions', hi)]),
 ('2.0', 1, [('0.0', H, 'rules versus unwritten conventions', hi)]),
 ('2.1', 1, [('2.0', H, 'convention as unwritten code', hi)]),
 ('2.2', 1, [('2.0', H, 'convention as unwritten code', hi)]),
 ('2.3', 1, [('2.0', H, 'convention as unwritten code', hi)]),
 ('2.4', 1, [('2.0', H, 'convention as unwritten code', hi)]),
 ('2.5', 1, [('2.0', E, 'conventions versus rules', hi)]),
 ('3.0', 1, [('0.0', H, 'rules of an activity', hi)]),
 ('3.1', 1, [('1.0', H, 'rituals', hi)]),
 ('3.2', 1, [('2.0', H, 'conventions', hi)]),
 ('4.0', 1, []),
 ('4.1', 1, [('0.0', H, 'rules clarified to teams', lo)]),
 ('4.2', 1, []),
 ('4.3', 1, []),
 ('4.4', 1, [('1.0', H, 'rituals built into an event', hi)]),
 ('4.5', 1, [('2.0', H, 'conventions built into an event', hi)]),
 ('4.6', 1, [('0.0', H, 'rules applied consistently', lo)]),
 ('4.7', 1, [('2.0', H, 'respectful behaviour conventions', lo)]),
 ('5.0', 1, []),
 ('5.1', 1, []),
 ('5.2', 1, [(ETH2+'8.2', H, 'dissent as open disagreement', hi)]),
 ('5.3', 1, []),
 ('5.4', 1, []),
 ('6.0', 1, []), ('6.1', 1, []), ('6.2', 1, []), ('6.3', 1, []),
 ('7.0', 1, []), ('7.1', 1, []), ('7.2', 1, []), ('7.3', 1, []), ('7.4', 1, []),
]

def build(sid, spec):
    prefix = P + sid + '.'
    path = B + 'points/' + P + sid + '.txt'
    ids = re.findall(r'^\[(' + re.escape(P + sid) + r'\.[^\]]+)\]', open(path).read().split('CANDIDATES')[0], re.M)
    allids = set(re.findall(r'^\[([^\]]+)\]', open(path).read(), re.M))
    out = {}
    for suf, cost, needs in spec:
        k = prefix + suf
        assert k in ids and k not in out, k
        ns = []
        for t, st, why, c in needs:
            t = t if t.startswith('pe-') else prefix + t
            assert t in allids and t != k, (k, t)
            ns.append({'id': t, 'strength': st, 'why': why, 'confidence': c})
        out[k] = {'cost': cost, 'needs': ns}
    assert list(out) == ids, [i for i in ids if i not in out]
    json.dump(out, open(B + 'point-links/' + P + sid + '.json', 'w'), indent=0)
    json.load(open(B + 'point-links/' + P + sid + '.json'))
    links = sum(len(v['needs']) for v in out.values())
    c2 = sum(v['cost'] == 2 for v in out.values())
    low = sum(n['confidence'] == 'low' for v in out.values() for n in v['needs'])
    print(sid, len(out), links, c2, low)

build('s2', s2); build('s3', s3); build('s4', s4)
