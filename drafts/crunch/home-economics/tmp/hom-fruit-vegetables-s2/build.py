import json,re
P='hom-fruit-vegetables-s2'
F='../packs/hom-fruit-vegetables-s2.t1g1.txt'
txt=open(F).read()
ids=re.findall(r'^\['+P+r'\.([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
def L(i,s='helpful',w='',c='high'):
    if not i.startswith('hom-'): i=P+'.'+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
fs5='hom-food-safety-s5.';fs3='hom-food-safety-s3.';c1='hom-cooking-methods-s1.';fp='hom-food-preservation-s2.'
R={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(2,[]),'0.2':(2,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'0.6':(1,[L(c1+'5.4','helpful','cutting loses vitamin C')]),
'0.7':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[L('0.5','helpful','pre-prepared produce')]),'1.3':(1,[]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[]),'2.2':(1,[]),
'2.3':(1,[L('2.2','helpful','Class II compared with others','low')]),
'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L('6.0','helpful','enzymes continue ripening')]),
'3.1':(1,[L('3.0','helpful','produce deteriorates after harvest')]),
'3.2':(1,[L('3.0','helpful','vitamin C falls in storage')]),
'4.b':(1,[]),
'4.0':(2,[L('7.3','helpful','cool humid storage slows moisture loss','low')]),
'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),
'4.4':(2,[L('4.3','helpful','ethylene speeds ripening')]),
'4.5':(1,[L(fs3+'4.3','helpful','preventing cross-contamination','low')]),
'5.b':(1,[]),
'5.0':(1,[L(fp+'3.6','helpful','storage at -18 degrees','low'),L(fp+'4.3','helpful','no refreezing after thawing')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'6.b':(1,[L(fs5+'0.b','helpful','what enzymes are')]),
'6.0':(1,[L(fs5+'1.0','helpful','ripening enzymes after picking')]),
'6.1':(1,[L(fs5+'2.b','helpful','enzymic browning needs oxygen')]),
'6.2':(1,[L('6.1','helpful','enzymic browning')]),
'6.3':(1,[L(fs5+'0.4','helpful','cold slows enzymes')]),
'6.4':(2,[L(fs5+'0.3','essential','heat denatures enzymes'),L(fs5+'4.0','helpful','blanching method')]),
'6.5':(1,[L(c1+'2.5','helpful','acid slows browning')]),
'6.6':(1,[L(c1+'2.4','helpful','excluding oxygen stops browning')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L('7.0','helpful','moisture loss')]),
'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),
'8.b':(1,[L(fs3+'0.0','helpful','micro-organisms cause spoilage')]),
'8.0':(1,[]),'8.1':(1,[]),
'8.2':(2,[L(fs3+'3.b','helpful','conditions for microbial growth')]),
'8.3':(2,[L(fs3+'3.2.0'.replace('3.2.0','2.0'),'helpful','mould growth and mycotoxins')]),
'8.4':(1,[L(fs3+'2.2','helpful','yeasts ferment sugars')]),
'8.5':(2,[L(fs3+'4.3','helpful','preventing contamination')]),
'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
}
out={}
for i in ids:
    c,n=R[i]; out[P+'.'+i]={"cost":c,"needs":n}
assert len(ids)==len(R)==len(out),(len(ids),len(R),set(ids)^set(R))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open('../point-links/'+P+'.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
