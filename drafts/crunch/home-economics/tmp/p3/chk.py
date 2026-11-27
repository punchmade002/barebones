import json,re
for f in ['hom-sociological-concepts-s2','hom-clothing-selection-s1','hom-marriage-s3']:
    t=open(f'packs/{f}.t1g1.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    tg=[];sec=None
    for l in t.splitlines():
        if l.startswith('TARGET'):sec='T'
        elif l.startswith('CANDIDATES'):sec='C'
        m=re.match(r'\[([^\]]+)\]',l)
        if m and sec=='T':tg.append(m[1])
    d=json.load(open(f'point-links/{f}.t1g1.json'))
    assert list(d)==tg,(f,set(tg)^set(d))
    links=[x for v in d.values() for x in v['needs']]
    assert all(x['id'] in ids and x['id'] not in () for x in links),f
    assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
    print(f,len(d),len(links),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in links))
