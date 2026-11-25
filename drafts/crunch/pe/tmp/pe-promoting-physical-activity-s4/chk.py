import json,re,sys
for s in sys.argv[1:]:
    txt=open(f'points/{s}.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=[i for i in ids if i.startswith(s+'.')]
    d=json.load(open(f'point-links/{s}.json'))
    assert list(d)==tgt,(set(tgt)^set(d))
    L=[n for v in d.values() for n in v['needs']]
    assert all(n['id'] in ids for n in L)
    assert all(n['id']!=k for k,v in d.items() for n in v['needs'])
    print(s,len(d),len(L),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in L))
