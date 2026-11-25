import json,re
P='bio7-s3.'
H,L='high','low'
E,Hp='essential','helpful'
# id: (cost, [(target,strength,why,conf)])
d={
'0.b':(1,[]),
'0.0':(1,[('0.3',Hp,'cell membrane location',H)]),
'0.1':(2,[('0.0',E,'cell wall function',H)]),
'0.2':(1,[('0.0',E,'cell wall',H)]),
'0.3':(2,[]),
'0.4':(1,[('0.3',E,'proteins in membrane',H)]),
'0.5':(1,[('0.3',Hp,'cell membrane',H)]),
'1.b':(1,[]),
'1.0':(1,[('0.3',Hp,'inside the cell membrane',H)]),
'1.1':(2,[('1.0',E,'cytoplasm',H)]),
'1.2':(1,[]),
'1.3':(2,[('1.2',E,'plant vacuole',H),('0.0',Hp,'cell wall pressure',L)]),
'1.4':(1,[('1.2',Hp,'vacuole',H)]),
'1.5':(1,[('1.2',E,'plant vacuole',H)]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[('2.0',E,'cristae and membranes',H)]),
'2.2':(1,[('2.0',Hp,'mitochondrion',H)]),
'2.3':(1,[('bio7-s1.0.1',E,'eukaryotic cells',H)]),
'2.4':(1,[('2.2',Hp,'energy release by mitochondria',H)]),
'2.5':(1,[('6.0',Hp,'ribosomes',H)]),
'2.6':(1,[('2.0',E,'mitochondrion structure',H)]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[('3.0',E,'chloroplast structure',H)]),
'3.2':(2,[('3.0',E,'thylakoids and chlorophyll',H)]),
'3.3':(1,[('3.0',Hp,'stacked thylakoid membranes',H)]),
'3.4':(1,[]),
'3.5':(1,[('3.4',Hp,'where chloroplasts occur',H)]),
'3.6':(1,[('3.0',Hp,'chloroplast structure',H)]),
'3.7':(1,[('3.0',E,'chloroplast structure',H)]),
'4.b':(1,[]),
'4.0':(2,[('bio7-s1.0.1',Hp,'eukaryotic nucleus, nuclear envelope',H)]),
'4.1':(2,[('4.0',E,'DNA in nucleus',H)]),
'4.2':(2,[('4.0',E,'DNA in nucleus',H)]),
'4.3':(1,[('4.0',E,'inside the nucleus',H),('6.0',Hp,'ribosomes',H)]),
'4.4':(1,[('4.0',E,'nucleus',H)]),
'4.5':(1,[('4.0',E,'nuclear envelope',H)]),
'4.6':(2,[('4.5',E,'nuclear pores',H)]),
'4.7':(1,[('4.5',E,'nuclear pores',H)]),
'5.b':(1,[]),
'5.0':(1,[('4.0',Hp,'DNA and histones',H)]),
'5.1':(1,[('5.0',E,'chromosome',H),('4.0',Hp,'chromatin',L)]),
'5.2':(1,[('5.1',Hp,'uncoiled chromosomes',H)]),
'5.3':(1,[]),
'5.4':(1,[('5.0',E,'chromosomes carry genes',H)]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(2,[('6.0',E,'ribosome',H),('4.2',Hp,'mRNA code',H)]),
'6.2':(1,[('bio7-s1.0.0',Hp,'prokaryotic cells',H)]),
'6.3':(1,[('6.0',E,'ribosomes',H)]),
'6.4':(1,[('4.0',Hp,'DNA in nucleus',L)]),
'7.b':(1,[]),
'7.0':(1,[('4.0',Hp,'nuclear envelope',H)]),
'7.1':(2,[('7.0',E,'endoplasmic reticulum',H),('6.0',Hp,'ribosomes',H)]),
'7.2':(1,[('7.1',E,'rough ER',H)]),
'7.3':(1,[('7.0',E,'endoplasmic reticulum',H)]),
'7.4':(1,[('7.0',E,'ER',H)]),
'8.b':(1,[]),
'8.0':(1,[]),
'8.1':(2,[('7.1',E,'proteins from rough ER',H)]),
'8.2':(2,[('8.1',E,'secretory vesicles from Golgi',H),('0.3',Hp,'cell membrane',L)]),
'8.3':(1,[('8.0',E,'Golgi apparatus',H)]),
'8.4':(2,[('4.6',E,'mRNA through nuclear pore',H),('7.1',E,'rough ER protein making',H)]),
'8.5':(2,[('8.1',E,'Golgi modifies and packages',H),('8.2',E,'secretory vesicle exocytosis',H)]),
'8.6':(2,[('8.4',E,'secretory pathway',H)]),
'9.b':(1,[]),
'9.0':(1,[]),
'9.1':(1,[('0.0',Hp,'cell wall',H)]),
'9.2':(1,[('9.1',Hp,'rigid wall',H)]),
'9.3':(1,[]),
'9.4':(2,[('4.7',Hp,'electron microscope structures',L)]),
'9.5':(2,[('9.0',E,'shared organelles',H)]),
'9.6':(2,[('9.1',E,'plant-only structures',H)]),
}
def f(t): return t if t.startswith('bio') else P+t
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":[{"id":f(t),"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio7-s3.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith(P)]
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio7-s3.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
