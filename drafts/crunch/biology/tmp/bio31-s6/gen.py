import json,re
P='bio31-s6.'
H,L,E,He='high','low','essential','helpful'
d={ # id:(cost,[(target,strength,why,conf)])
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[('s5.0.4',He,'limiting factors',H)]),
'1.b':(1,[]),
'1.0':(1,[('0.2',He,'little environmental resistance',H)]),
'1.1':(1,[('1.0',He,'J-curve exponential shape',H)]),
'1.2':(1,[('1.0',E,'J-shaped growth conditions',H)]),
'1.3':(2,[('1.0',E,'J-shaped growth',H),('s5.0.3',He,'carrying capacity',H)]),
'1.4':(2,[('1.0',He,'explosive J-shaped growth',H)]),
'1.5':(1,[('1.4',E,'algal bloom nutrient enrichment',H)]),
'1.6':(1,[('1.0',He,'rapid J-shaped spread',H)]),
'1.7':(1,[('1.0',He,'plague numbers, J-shaped growth',H)]),
'1.8':(1,[('1.0',E,'J-curve shape and meaning',H)]),
'2.b':(1,[]),
'2.0':(1,[('0.2',He,'limited resources, environmental resistance',L)]),
'2.1':(1,[('2.0',E,'S-curve phases',H)]),
'2.2':(1,[('2.0',E,'S-curve phases',H)]),
'2.3':(2,[('2.0',E,'S-curve phases',H),('s5.5.0',He,'density-dependent factors',H)]),
'2.4':(2,[('s5.0.3',E,'carrying capacity K',H),('2.0',E,'S-curve phases',H)]),
'2.5':(2,[('2.4',E,'population around K',H)]),
'3.b':(1,[]),
'3.0':(1,[('2.0',E,'S-curve growth',H)]),
'3.1':(1,[('2.0',E,'S-curve growth',H)]),
'3.2':(1,[('2.0',He,'S-curve growth',H)]),
'3.3':(2,[('2.0',E,'four S-curve phases',H),('0.2',He,'environmental resistance',H)]),
'4.b':(1,[]),
'4.0':(1,[('2.0',He,'S-curve limited resources',H)]),
'4.1':(1,[('0.2',E,'environmental resistance',H)]),
'4.2':(1,[('2.0',He,'S-curve growth slowing',H)]),
'4.3':(1,[('1.3',E,'J-curve crash',H),('2.4',He,'stable population at K',H)]),
'4.4':(1,[('1.2',He,'J-curve conditions',L)]),
'5.b':(1,[('s5.0.6',He,'carrying capacity changes',H)]),
'5.0':(1,[('2.4',E,'plateau at K',H)]),
'5.1':(1,[('s5.3.0',He,'food as limiting factor',L)]),
'5.2':(2,[('s5.5.4',He,'habitat loss lowers carrying capacity',H)]),
'5.3':(1,[('s5.3.2',He,'squirrelpox disease limits squirrels',L)]),
'5.4':(1,[('s5.3.7',He,'predators limit prey',H)]),
'5.5':(2,[('s5.0.7',E,'overshooting carrying capacity',H)]),
'5.6':(2,[('s5.5.2',E,'density-independent factors',H),('2.4',He,'S-curve recovery to K',L)]),
'6.b':(1,[]),
'6.0':(1,[('s5.3.7',He,'predator and prey limit each other',H)]),
'6.1':(1,[('6.0',E,'predator-prey cycles',H)]),
'6.2':(1,[('6.0',E,'predator-prey cycles',H),('5.2',He,'lower carrying capacity',L)]),
'7.b':(1,[]),
'7.0':(2,[('1.0',E,'J-shaped growth',H),('s5.0.3',He,'raising carrying capacity',H)]),
'7.1':(1,[('2.0',E,'S-curve levelling off',H)]),
'7.2':(2,[('1.3',He,'crash when resource fails',H)]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":[{"id":(t if t.startswith('s5') and False else (('bio31-'+t) if t.startswith('s5') else P+t)),"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
base='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
json.dump(out,open(base+'point-links/bio31-s6.json','w'),indent=1)
pk=open(base+'points/bio31-s6.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith(P)]
assert list(out)==tg,(set(tg)^set(out))
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
