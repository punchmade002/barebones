import json,re
P='hom-clothing-selection-s5'
t='hom-textiles-fibres-s5'; s4='hom-clothing-selection-s4'
def L(i,s='helpful',w='',c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
m=lambda n:P+'.'+n
R={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L(s4+'.0.b','helpful','uses line, shape, colour, pattern')]),
'0.3':(1,[L(m('1.0'),'helpful','fashion sketch features')]),
'0.4':(1,[]),
'0.5':(1,[L(m('6.b'),'helpful','plan of work order')]),
'0.6':(1,[L(s4+'.7.b','helpful','function, comfort, appearance criteria')]),
'0.7':(2,[]),
'1.b':(1,[]),
'1.0':(2,[L(s4+'.0.b','essential','uses elements line shape colour'),L(s4+'.4.b','helpful','proportion and harmony principles')]),
'1.1':(1,[]),'1.2':(2,[]),
'1.3':(1,[L(m('1.2'),'essential','features named in description')]),
'1.4':(1,[L(m('1.1'),'helpful','labelled front view')]),
'2.b':(1,[]),
'2.0':(2,[L(t+'.8.b','helpful','fabric performance tests')]),
'2.1':(1,[L(t+'.8.5','helpful','shrinkage test method')]),
'2.2':(2,[L(s4+'.6.5','helpful','crisp and soft fabric effects','low')]),
'2.3':(1,[]),'2.4':(2,[]),
'2.5':(1,[L(m('2.4'),'helpful','interfacing is a notion')]),
'3.b':(1,[]),
'3.0':(1,[L(m('9.3'),'helpful','darts','low')]),
'3.1':(2,[]),
'3.2':(2,[L(m('4.b'),'helpful','taking body measurements')]),
'3.3':(1,[]),'3.4':(1,[]),
'3.5':(1,[L(m('2.4'),'helpful','notions list')]),
'3.6':(1,[]),
'4.b':(1,[L(m('3.2'),'helpful','pattern size from measurements')]),
'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L(t+'.0.5','helpful','selvedge is finished edge')]),
'5.2':(1,[]),
'5.3':(1,[L(s4+'.0.5','helpful','pattern or print','low')]),
'5.4':(1,[]),
'5.5':(1,[L(m('5.1'),'helpful','grain line and selvedge')]),
'6.b':(1,[]),
'6.0':(1,[L(m('5.b'),'helpful','laying out pattern pieces')]),
'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L(m('9.b'),'helpful','fastenings process steps','low')]),
'6.4':(1,[L(m('6.5'),'helpful','pressing','low'),L(m('0.6'),'helpful','evaluate against brief')]),
'6.5':(1,[]),'6.6':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L(m('7.3'),'helpful','alteration lines')]),
'7.2':(1,[L(m('7.3'),'helpful','alteration lines')]),
'7.3':(1,[]),'7.4':(1,[]),
'7.5':(1,[L(m('5.1'),'helpful','grain line')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),
'8.2':(1,[L(m('0.7'),'essential','design specification')]),
'8.3':(1,[L(m('9.b'),'helpful','the three processes')]),
'8.4':(2,[]),'8.5':(1,[]),'8.6':(1,[]),
'9.b':(1,[]),
'9.0':(2,[L(m('2.5'),'helpful','interfacing reinforcement')]),
'9.1':(1,[]),
'9.2':(1,[L(m('9.0'),'helpful','matches buttonhole position')]),
'9.3':(2,[L(s4+'.6.1','helpful','what darts do')]),
'9.4':(1,[]),
'9.5':(1,[L(s4+'.6.3','helpful','gathers pleats tucks')]),
'9.6':(2,[]),'9.7':(1,[]),
'9.8':(1,[L(m('2.5'),'helpful','interfacing')]),
}
ids=re.findall(r'^\[('+P+r'\.[^\]]+)\]',open('../packs/'+P+'-s5.t1g1.txt'.replace('-s5-s5','-s5') if False else '../packs/hom-clothing-selection-s5.t1g1.txt').read().split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',open('../packs/hom-clothing-selection-s5.t1g1.txt').read(),re.M))
out={}
for i in ids:
    c,n=R[i[len(P)+1:]]
    out[i]={"cost":c,"needs":n}
assert len(ids)==len(R)==len(out),(len(ids),len(R))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open('../point-links/hom-clothing-selection-s5.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
