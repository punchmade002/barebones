import json,re
b='/Users/gabrielwhelan/barebones/drafts/crunch/pe/'
for s in ['s5','s6','s7']:
    sid='pe-performance-demands-'+s
    txt=open(b+'points/'+sid+'.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=[]
    sec=None
    for l in txt.split('\n'):
        if l.startswith('TARGET'):sec='T'
        elif l.startswith('CANDIDATES'):sec='C'
        m=re.match(r'\[([^\]]+)\]',l)
        if m and sec=='T':tgt.append(m.group(1))
    d=json.load(open(b+'point-links/'+sid+'.json'))
    ok=list(d)==tgt and len(set(tgt))==len(tgt)
    bad=[n['id'] for v in d.values() for n in v['needs'] if n['id'] not in ids]
    selfl=[k for k,v in d.items() if any(n['id']==k for n in v['needs'])]
    print(s,len(tgt),ok,bad,selfl,sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
