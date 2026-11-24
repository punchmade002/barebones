import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,H='essential','helpful'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
q='hist-ire2-s2.';c='hist-ire2-s1.'
D=[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),
('0.2',1,[L(q+'0.3',H,'the 1870 Act')]),
('0.3',2,[L(q+'0.1',H,'the Three Fs, rents')]),
('0.4',1,[L(q+'0.3',E,'the 1870 Act provisions')]),
('0.5',1,[L(q+'0.3',H,'the 1870 Act')]),
('0.6',2,[L(q+'0.4',E,'rent rises and eviction loophole')]),
('1.b',1,[]),('1.0',1,[]),
('1.1',1,[L(q+'1.0',H,'the farming crisis')]),
('1.2',2,[L(c+'4.1',E,'Davitt, Devoy and New Departure')]),
('1.3',1,[L(c+'3.2',H,'Parnell introduced as MP','low')]),
('1.4',2,[L(q+'1.2',E,'Irishtown meeting leading to the League')]),
('1.5',1,[L(q+'1.4',H,'the Land League'),L(q+'0.1',H,'tenant demands','low')]),
('1.6',1,[L(q+'1.4',E,'the Land League')]),
('2.b',1,[L(q+'1.4',H,'the Land League')]),
('2.0',1,[L(q+'1.4',H,'Parnell and the Land League')]),
('2.1',2,[L(q+'2.0',E,'Parnell urging shunning at Ennis')]),
('2.2',2,[L(q+'2.1',H,'Boycott as first victim')]),
('2.3',1,[]),
('2.4',1,[L(q+'1.4',H,'the Land League')]),
('2.5',2,[L(q+'1.4',H,'the Land League campaign','low')]),
('2.6',1,[L(q+'2.5',E,'the coercion bill')]),
('3.b',1,[L(q+'1.5',H,'the League\'s demands','low')]),
('3.0',2,[L(q+'0.1',E,'the Three Fs')]),
('3.1',2,[L(q+'3.0',E,'fair rents under the 1881 Act')]),
('3.2',1,[L(q+'3.0',E,'the 1881 Act')]),
('3.3',1,[L(q+'3.0',H,'the 1881 Act')]),
('3.4',1,[L(q+'3.0',E,'the 1881 Act')]),
('3.5',2,[L(q+'3.4',E,'Parnell\'s test-case policy')]),
('3.6',1,[L(q+'3.5',E,'the No Rent Manifesto')]),
('3.7',1,[L(c+'6.2',E,'the Kilmainham settlement')]),
('4.b',1,[]),('4.0',1,[]),
('4.1',2,[L(q+'4.0',E,'the Plan of Campaign')]),
('4.2',1,[L(q+'4.1',E,'estates where Plan was applied')]),
('4.3',2,[L(q+'4.0',E,'answer to the Plan of Campaign')]),
('4.4',1,[L(q+'4.3',H,'Balfour\'s coercion policy')]),
('4.5',1,[L(q+'4.0',E,'the Plan of Campaign')]),
('4.6',1,[L(q+'4.0',E,'the Plan of Campaign')]),
('5.b',1,[]),
('5.0',2,[L(q+'0.5',H,'purchase loans to tenants')]),
('5.1',1,[L(q+'5.0',H,'earlier purchase loans')]),
('5.2',2,[]),
('5.3',1,[L(q+'5.b',H,'constructive unionism')]),
('5.4',1,[L(q+'5.1',H,'purchase terms')]),
('6.b',1,[]),
('6.0',2,[L(q+'4.0',H,'William O\'Brien','low')]),
('6.1',2,[L(q+'6.0',H,'the Land Conference scheme')]),
('6.2',1,[L(q+'6.1',E,'the Wyndham Act')]),
('6.3',1,[L(q+'6.2',E,'the landlord bonus')]),
('6.4',1,[L(q+'2.b',H,'the Land War','low')]),
('6.5',1,[]),
('6.6',1,[L(q+'6.1',H,'voluntary purchase under Wyndham')]),
('6.7',1,[L(q+'6.1',H,'mass tenant purchase')]),
('7.b',1,[]),('7.0',1,[]),('7.1',1,[]),
('7.2',2,[L(c+'4.4',H,'the IRB','low')]),
('7.3',1,[L(q+'1.4',H,'the Land League')]),
('7.4',1,[L(q+'2.5',H,'coercion in 1881')]),
('7.5',1,[L(q+'1.5',E,'peasant proprietorship vs nationalisation')]),
('7.6',1,[L(q+'4.6',H,'the Parnell split','low')]),
('7.7',1,[]),
('7.8',2,[L(q+'7.3',H,'his Land League role')]),
('8.b',1,[]),
('8.0',2,[L(q+'3.0',E,'the 1881 Three Fs'),L(q+'6.7',H,'tenant purchase by 1914')]),
('8.1',2,[L(q+'6.7',H,'the purchase settlement')]),
('8.2',1,[L(q+'1.4',H,'the Land League')]),
('8.3',2,[L(q+'4.5',H,'papal condemnation')]),
('8.4',2,[L(q+'2.2',H,'boycotting intimidation')]),
('8.5',2,[L(q+'5.3',E,'constructive unionism')]),
('8.6',2,[L(q+'7.5',H,'Davitt\'s land nationalisation')]),
]
txt=open(P+'packs/hist-ire2-s2.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire2-s2\.[^\]]+)\]',txt,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={q+k:{"cost":x,"needs":n} for k,x,n in D}
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for n in v['needs']:assert n['id'] in ids and n['id']!=k,n
json.dump(out,open(P+'point-links/hist-ire2-s2.t1g1.json','w'),ensure_ascii=False)
j=json.load(open(P+'point-links/hist-ire2-s2.t1g1.json'))
ns=[n for v in j.values() for n in v['needs']]
print(len(j),len(ns),sum(v['cost']==2 for v in j.values()),sum(n['confidence']=='low' for n in ns))
