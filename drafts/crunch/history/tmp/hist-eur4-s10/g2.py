import json,re
P='hist-eur4-s10.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful'
pack=open('packs/hist-eur4-s10.t1g2.txt').read()
tgt=re.findall(r'^\[(hist-eur4-s10\.\S+?)\]',pack.split('CANDIDATES')[0],re.M)
L={ # every other target explicitly has no link (decided on reading candidates)
 '10.2':[n('hist-eur4-s11.4.7',H,"Dutch Church after the Council",'low')],
 '11.b':[n('hist-eur4-s11.4.b',H,"Church divisions after the Council")],
 '11.4':[n('hist-eur4-s11.3.b',H,"Council reforms"),n('hist-eur4-s11.4.3',H,"contraception controversy")],
 '11.5':[n('hist-eur4-s11.4.3',H,"Humanae Vitae's ban on contraception")],
 '13.1':[n('hist-eur4-s11.5.b',H,"Wojtyła elected pope in 1978")],
 '14.b':[n('hist-eur4-s11.3.3',H,"the ecumenical movement")],
 '14.2':[n('hist-eur4-s11.3.4',H,"Paul VI and Athenagoras meeting",'low')],
 '14.3':[n('hist-eur4-s11.3.4',H,"lifting of the 1054 excommunications")],
 '15.4':[n('hist-eur4-s11.6.b',H,"secularisation and the Council's effect",'low')],
 '15.5':[n('hist-eur4-s11.5.2',H,"Church and Solidarity in Poland",'low')],
}
D={t:{"needs":L.get(t[len(P):],[])} for t in tgt}
ids=set(re.findall(r'^\[(\S+?)\]',pack,re.M))
for k,v in D.items():
    for x in v['needs']: assert x['id'] in ids
assert all(k[len(P):] in {t[len(P):] for t in tgt} for k in D) and set(L)<={t[len(P):] for t in tgt}
json.dump(D,open('point-links/hist-eur4-s10.t1g2.json','w'),indent=1)
print(len(D),sum(len(v['needs']) for v in D.values()),sum(x['confidence']=='low' for v in D.values() for x in v['needs']))
