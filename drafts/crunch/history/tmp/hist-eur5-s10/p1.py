import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hist-eur5-s10.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(2,[L(p+'0.0','helpful','French assimilation idea')]),
'0.3':(1,[L('hist-eur5-s5.0.0','helpful','uses indirect rule')]),
'0.4':(1,[]),
'1.0':(2,[]),'1.1':(1,[]),
'1.2':(1,[L(p+'1.0','essential','Négritude movement')]),
'1.3':(2,[L(p+'1.0','helpful','Senghor as Négritude founder')]),
'1.4':(2,[L(p+'1.2','essential','Négritude ideas being criticised')]),
'1.5':(2,[L(p+'1.0','helpful','Césaire and Senghor as founders')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(2,[L(p+'2.0','helpful','mission churches')]),
'2.2':(2,[]),'2.3':(1,[]),
'2.4':(2,[L('hist-eur5-s5.0.0','essential','uses Lugard and indirect rule')]),
'2.5':(1,[]),'2.6':(1,[]),'2.7':(1,[]),'2.8':(1,[]),'2.9':(1,[]),'2.10':(1,[]),
'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[L(p+'3.2','essential','The Satanic Verses')]),
'3.4':(1,[L(p+'3.2','essential','Rushdie and the novel')]),
'3.5':(2,[L(p+'3.2','essential','the Rushdie affair')]),
'3.6':(1,[]),
'3.7':(2,[L(p+'3.2','helpful','Rushdie affair campaign')]),
'4.0':(1,[]),
'4.1':(1,[L(p+'4.0','helpful','spread of English')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'4.6':(2,[]),'4.7':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[]),
'5.2':(2,[L(p+'5.1','helpful','Achebe debut novel')]),
'5.3':(1,[L('hist-eur5-s5.1.3','essential','Biafra and its war')]),
'5.4':(2,[L(p+'4.4','helpful','English in African literature debate')]),
'5.5':(2,[]),'5.6':(1,[]),'5.7':(1,[]),'5.8':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(2,[]),'6.3':(1,[]),
'6.4':(2,[]),'6.5':(1,[]),'6.6':(1,[]),
'7.0':(2,[L(p+'4.4','helpful','colonial languages in African literature')]),
'7.1':(1,[L('hist-eur5-s5.1.4','helpful','Nigerian civil war')]),
'7.2':(1,[L(p+'5.8','helpful','African Writers Series origin')]),
'7.3':(1,[]),'7.4':(1,[]),'7.5':(2,[]),
'8.0':(1,[]),
'8.1':(1,[L(p+'0.1','helpful','mission schools discouraging languages')]),
'8.2':(1,[L(p+'4.2','essential','Tanzania choosing Swahili')]),
'8.3':(1,[L(p+'4.4','helpful','English versus local languages debate')]),
'8.4':(1,[]),
'8.5':(2,[L(p+'5.4','helpful','Achebe argument on English'),L(p+'7.0','helpful','Ngũgĩ argument on languages')]),
}
txt=open(P+'packs/hist-eur5-s10.t1g1.txt').read()
tg=re.findall(r'^\[(hist-eur5-s10\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tg:
    c,n=D[t[len(p):]]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tg)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(P+'point-links/hist-eur5-s10.t1g1.json','w'),ensure_ascii=False)
o=json.load(open(P+'point-links/hist-eur5-s10.t1g1.json'))
ln=[n for v in o.values() for n in v['needs']]
print(len(o),len(ln),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in ln))
