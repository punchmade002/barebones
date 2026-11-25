import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
p='hist-eur6-s6.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L(p+'0.4','essential','uses the GI Bill home loans')]),
'0.6':(1,[]),'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(p+'1.0','helpful','the Bretton Woods system')]),
'1.2':(1,[]),
'1.3':(2,[L(p+'1.1','essential','dollar as gold-pegged reserve currency'),L(p+'1.2','helpful','Marshall aid spent on US goods')]),
'1.4':(1,[L('hist-eur6-s2.0.7','essential','uses NSC-68')]),
'1.5':(1,[]),'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L(p+'2.3','helpful','uses Sputnik and the space race','low')]),
'2.5':(1,[L(p+'2.0','essential','the Interstate programme')]),
'2.6':(1,[]),'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),
'3.2':(1,[L(p+'3.0','essential','uses the farewell address warning')]),
'3.3':(1,[]),
'3.4':(2,[L(p+'3.0','helpful','Eisenhower speech echoing Mills')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(p+'4.0','essential','uses Whyte and his book')]),
'4.2':(2,[L(p+'4.1','essential','uses Whyte social ethic argument')]),
'4.3':(1,[L(p+'4.0','helpful','Whyte study of suburban communities')]),
'4.4':(2,[L(p+'4.1','helpful','the conformity worry Whyte described')]),
'4.5':(1,[L(p+'4.1','helpful','the Organization Man as conformist')]),
'4.6':(1,[L(p+'4.5','helpful','similar corporate figure')]),
'4.7':(1,[L(p+'4.5','essential','uses the Organization Man')]),
'4.8':(1,[L(p+'4.1','helpful','Whyte conformity thesis')]),
'5.b':(1,[]),'5.0':(2,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[L('hist-eur6-s2.0.b','helpful','uses containment')]),
'5.5':(1,[]),'5.6':(1,[]),'5.7':(1,[]),'5.8':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(2,[L(p+'6.0','helpful','strong unions in core industries')]),
'6.2':(1,[L(p+'6.1','essential','uses the Treaty of Detroit agreements')]),
'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(p+'6.2','helpful','the postwar bargain with unions','low')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L(p+'7.0','helpful','Keynesian demand management')]),
'7.2':(1,[L(p+'7.1','helpful','tax cut Heller argued for')]),
'7.3':(1,[L(p+'7.2','essential','uses the 1964 tax cut')]),
'7.4':(2,[L(p+'7.0','helpful','Keynesian demand management')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(p+'0.1','helpful','US dominance of world production in 1945')]),
'8.2':(1,[L(p+'1.4','helpful','defence spending fed growth','low')]),
'8.3':(2,[L(p+'0.4','helpful','uses GI Bill benefits')]),
'8.4':(1,[]),'8.5':(1,[]),
}
txt=open(P+'packs/hist-eur6-s6.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(p)]
assert set(i[len(p):] for i in tgt)==set(D) and len(tgt)==len(D)
out={i:{"cost":D[i[len(p):]][0],"needs":D[i[len(p):]][1]} for i in tgt}
for v in out.values():
  for n in v['needs']: assert n['id'] in ids and n['id'] not in out or True
for k,v in out.items():
  for n in v['needs']: assert n['id'] in ids and n['id']!=k
json.dump(out,open(P+'point-links/hist-eur6-s6.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
