import json,re,sys
P='hist-eur1-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
'0.0':(2,[]),'0.1':(2,[]),'0.2':(2,[L('hist-eur1-s7.1.4',H,'1846–47 agricultural crisis')]),'0.3':(1,[]),
'1.b':(1,[L('hist-eur1-s1.0.b',H,'the system of 1815')]),'1.0':(1,[]),'1.1':(2,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[L(P+'0.0',H,'the Paris revolution')]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L(P+'2.3',E,'troops and the dead of 18 March')]),
'2.5':(1,[L('hist-eur1-s1.4.0',H,'black, red and gold colours')]),
'2.6':(1,[]),'2.7':(1,[L(P+'1.4',H,'peasants and feudal dues')]),
'3.0':(1,[]),'3.1':(1,[L(P+'3.0',E,'the Vorparlament')]),
'3.2':(1,[L(P+'3.1',H,'radicals who wanted a republic')]),
'3.3':(1,[L(P+'3.1',H,'elections arranged by Vorparlament')]),
'3.4':(2,[L(P+'3.3',E,'the Frankfurt Assembly')]),
'3.5':(1,[L(P+'3.4',H,'deputies elected to the Assembly')]),
'3.6':(1,[L(P+'3.3',H,'the Assembly he presided over')]),
'3.7':(2,[L(P+'3.3',H,'the Frankfurt Assembly')]),
'4.0':(2,[]),'4.1':(1,[L(P+'4.0',E,'the Basic Rights')]),
'4.2':(1,[]),'4.3':(1,[L(P+'4.2',H,'contrast with Grossdeutsch'),L(P+'3.6',H,'Gagern the president')]),
'4.4':(1,[L(P+'4.2',E,'the Grossdeutsch plan')]),
'4.5':(1,[]),
'5.0':(2,[L('hist-eur1-s1.1.0',H,'the German Confederation')]),
'5.1':(1,[L(P+'5.0',E,'status of Schleswig and Holstein')]),
'5.2':(1,[L(P+'5.1',E,'the German rising in Schleswig')]),
'5.3':(1,[L(P+'5.2',E,'the Prussian invasion')]),
'5.4':(1,[L(P+'5.3',E,'the Malmö armistice')]),
'5.5':(1,[L(P+'5.4',E,'acceptance of the armistice')]),
'5.6':(2,[L(P+'5.3',H,'the Malmö armistice')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'0.1',H,'the Prague rising')]),
'6.1':(1,[L(P+'6.0',H,'Windischgrätz')]),
'6.2':(1,[L(P+'6.1',H,'the Vienna rising')]),
'6.3':(1,[]),
'6.4':(1,[L(P+'2.6',H,'liberal ministry being replaced')]),
'6.5':(1,[L(P+'2.6',H,'the Prussian National Assembly')]),
'6.6':(2,[]),
'7.0':(1,[L(P+'3.3',H,'the Frankfurt Assembly')]),
'7.1':(1,[L(P+'7.0',H,'the Frankfurt constitution')]),
'7.2':(1,[L(P+'7.1',E,'the offer of the crown')]),
'7.3':(1,[L(P+'7.2',H,'refusal of the crown')]),
'7.4':(1,[L(P+'7.0',E,'the Frankfurt constitution')]),
'7.5':(1,[L(P+'7.0',E,'the Frankfurt constitution')]),
'8.0':(1,[L(P+'7.5',H,'constitution not in force')]),
'8.1':(1,[L(P+'8.0',E,'the radical risings')]),
'8.2':(1,[L(P+'3.3',H,'the Frankfurt Assembly')]),
'8.3':(1,[L(P+'3.2',H,'Hecker and the Baden rising')]),
'8.4':(2,[L(P+'4.3',H,'Prussian-led Kleindeutsch idea','low')]),
'8.5':(1,[L(P+'8.4',E,'the Erfurt Union')]),
'8.6':(1,[L('hist-eur1-s1.1.1',H,'the Diet at Frankfurt')]),
'9.0':(1,[L(P+'3.7',H,'Provisional Central Power lacked army')]),
'9.1':(1,[L(P+'6.b',H,'old governments retaking capitals')]),
'9.2':(1,[]),
'9.3':(1,[L(P+'2.7',H,'peasant risings and dues'),]),
'9.4':(1,[L(P+'4.2',H,'Grossdeutsch–Kleindeutsch question')]),
'9.5':(1,[L(P+'4.5',H,'Assembly claiming Posen'),L(P+'6.1',H,'Jelačić')]),
'9.6':(1,[L(P+'7.2',E,'refusal of the crown')]),
'10.0':(1,[L(P+'4.0',H,'the Basic Rights'),L(P+'8.6',H,'Confederation restored')]),
'10.1':(1,[L(P+'6.5',H,'Prussian constitution of 1848')]),
'10.2':(2,[]),'10.3':(1,[L(P+'3.3',H,'the Frankfurt Assembly')]),
'10.4':(2,[]),'10.5':(2,[]),
}
suf=lambda k:k
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur1-s2.t1g1.txt').read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-eur1-s2\.[^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(P+k for k in D)==set(tids) and len(tids)==len(D),(set(tids)^set(P+k for k in D))
out={}
for t in tids:
    c,n=D[t[len(P):]]; out[t]={"cost":c,"needs":n}
    for x in n: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s2.t1g1.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
