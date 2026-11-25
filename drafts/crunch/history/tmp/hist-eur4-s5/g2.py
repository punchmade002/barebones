import json,re
def L(i,s,w,c='high'): return {"id":"hist-eur4-"+i,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":c}
D={'0.0':[L('s6.1.3','H','dollar dependence on USA','low')],
'0.1':[L('s6.0.0','H','Cold War division of Europe')],
'0.2':[L('s6.2.1','H','OEEC and Marshall aid details')],
'0.3':[L('s6.5.0','H','Benelux customs union'),L('s6.0.4','H','common market idea','low')],
'1.3':[L('s6.0.4','H','common market definition')],
'3.2':[L('s6.7.0','H','the Monnet Plan in France')],
'6.2':[L('s6.5.2','H','Treaty of Rome and EEC','low')],
'6.3':[L('s6.0.4','H','common market and four freedoms')],
'7.0':[L('s6.5.3','H','CAP and common farm prices')],
'7.2':[L('s6.5.3','H','1968 tariff abolition')],
'7.3':[L('s6.5.4','H','EFTA members and tariffs')],
'9.4':[L('s6.13.2','H','end of fixed exchange rates')],
}
txt=open('packs/hist-eur4-s5.t1g2.txt').read()
tg=re.findall(r'^\[(hist-eur4-s5\.\d+\.[b\d]+)\]',txt.split('CANDIDATES')[0],re.M)
allid=set(re.findall(r'^\[(hist-[\w.-]+)\]',txt,re.M))
out={t:{"needs":D.get(t.split('s5.')[1],[])} for t in tg}
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allid
assert all(k=='' or ('s5.'+k) in [t.split('hist-eur4-')[1] for t in out] for k in D)
json.dump(out,open('point-links/hist-eur4-s5.t1g2.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
