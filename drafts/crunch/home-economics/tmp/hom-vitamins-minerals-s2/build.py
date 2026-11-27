import json,re
P='hom-vitamins-minerals-s2'
F='../packs/hom-vitamins-minerals-s2.t1g1.txt'
txt=open(F).read()
ids=re.findall(r'^\['+P+r'\.([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
def L(i,s='helpful',w='',c='high'):
    if not i.startswith('hom-'): i=P+'.'+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
s1='hom-vitamins-minerals-s1.';e4='hom-energy-nutrition-s4.';c1='hom-cooking-methods-s1.'
R={
'0.b':(1,[L(s1+'0.1','helpful','fat-soluble versus water-soluble classes')]),
'0.0':(1,[L(s1+'0.1','helpful','water-soluble vitamin class')]),
'0.1':(1,[L('0.0','helpful','uses water-soluble storage rule')]),
'0.2':(1,[]),
'0.3':(1,[L(e4+'3.b','helpful','RDA as planning value')]),
'1.b':(1,[]),'1.0':(2,[]),'1.1':(2,[]),'1.2':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('2.0','helpful','collagen')]),
'2.2':(2,[L('5.5','helpful','reducing agent converts ferric iron','low')]),
'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'3.b':(1,[L('2.0','helpful','collagen needs vitamin C')]),
'3.0':(1,[]),
'3.1':(1,[L('2.0','essential','weak collagen without vitamin C')]),
'3.2':(1,[L('2.1','helpful','healing depends on collagen')]),
'3.3':(1,[L('2.2','essential','vitamin C aids iron absorption')]),
'3.4':(1,[L('2.5','helpful','vitamin C supports immunity')]),
'4.b':(1,[L('5.b','helpful','properties explain loss','low')]),
'4.0':(1,[]),
'4.1':(2,[L(c1+'5.4','helpful','cut surface and soaking increase loss')]),
'4.2':(2,[L('5.1','helpful','water-soluble, lost into cooking water')]),
'4.3':(1,[L('5.2','helpful','alkalis destroy vitamin C')]),
'4.4':(1,[L(c1+'5.0','helpful','vitamins dissolve in cooking water')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('0.2','helpful','lost into cooking water')]),
'5.2':(2,[]),
'5.3':(1,[L(c1+'2.0','helpful','oxidase enzyme meets phenolics when cut')]),
'5.4':(1,[]),
'5.5':(2,[L('2.2','essential','ferric to ferrous iron conversion')]),
'6.b':(1,[]),'6.0':(2,[]),
'6.1':(1,[L('6.0','helpful','B12 only in animal foods')]),
'6.2':(1,[]),
'6.3':(1,[L('0.1','helpful','B12 liver store')]),
'7.b':(1,[]),
'7.0':(1,[L('10.4','helpful','B12 and folate form red cells','low')]),
'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'8.b':(1,[]),
'8.0':(1,[L('7.0','helpful','B12 forms red blood cells')]),
'8.1':(1,[L('8.0','helpful','megaloblastic anaemia')]),
'8.2':(1,[L('7.2','helpful','myelin sheath insulates nerves')]),
'8.3':(1,[L('6.1','essential','plant foods lack B12')]),
'8.4':(1,[L('6.2','essential','intrinsic factor needed for absorption')]),
'8.5':(1,[L('6.2','helpful','absorption failure','low')]),
'9.b':(1,[]),
'9.0':(1,[L('0.2','helpful','water-soluble loss in cooking water')]),
'9.1':(1,[]),'9.2':(1,[]),
'10.b':(1,[]),'10.0':(2,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),
'10.4':(1,[L('7.0','helpful','B12 and red blood cells','low')]),
'10.5':(1,[L('10.3','helpful','folate in cell division')]),
'11.b':(1,[L('10.5','helpful','neural tube forms early')]),
'11.0':(2,[L('8.0','helpful','same megaloblastic anaemia as B12')]),
'11.1':(1,[L('10.5','essential','folate forms neural tube')]),
'11.2':(1,[L('10.3','helpful','folate needed for growth')]),
'11.3':(1,[L('10.5','helpful','folic acid protects neural tube')]),
'12.b':(1,[L('10.2','helpful','folic acid versus folate','low')]),
'12.0':(1,[]),
'12.1':(1,[L('12.0','helpful','water-soluble folate lost in boiling')]),
'12.2':(1,[L('10.2','helpful','folic acid is synthetic form')]),
}
out={}
for i in ids:
    c,n=R[i]; out[P+'.'+i]={"cost":c,"needs":n}
assert len(ids)==len(R)==len(out),(len(ids),len(R),set(ids)^set(R))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open('../point-links/'+P+'.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
