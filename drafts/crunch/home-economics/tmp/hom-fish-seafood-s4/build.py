import json
P='hom-fish-seafood-s4.'
def L(i,w,c='high',s='helpful'): return {"id":i,"strength":s,"why":w,"confidence":c}
F='hom-food-preservation-'
d=[
('0.b',1,[]),
('0.0',2,[L(F+'s1.5.b','preservation principles behind methods')]),
('0.1',1,[L(F+'s1.1.3','oxidation causes rancidity')]),
('0.2',1,[]),
('1.b',1,[]),
('1.0',1,[L(F+'s2.0.0','low temperature slows enzymes, microbes')]),
('1.1',1,[L(F+'s2.0.2','ice unavailable to micro-organisms')]),
('1.2',1,[L(F+'s2.1.1','small ice crystals cause little damage')]),
('1.3',1,[]),
('1.4',1,[L(F+'s2.1.5','drip loses soluble vitamins')]),
('1.5',1,[L(F+'s2.4.0','freezer burn')]),
('1.6',1,[]),('1.7',1,[]),
('2.b',1,[]),
('2.0',2,[L(F+'s3.2.1','sealing and retort sterilising cans')]),
('2.1',2,[L(F+'s3.0.0','heat destroys microbes, denatures enzymes'),L(F+'s3.0.1','airtight seal prevents re-contamination')]),
('2.2',1,[]),
('2.3',1,[L(F+'s3.0.5','B vitamins heat-sensitive')]),
('2.4',1,[]),('2.5',1,[]),
('3.b',1,[]),('3.0',1,[]),
('3.1',1,[L(F+'s5.2.0','salt draws water by osmosis')]),
('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),
('3.5',1,[L(F+'s5.2.6','excess sodium raises blood pressure')]),
('3.6',1,[]),
('4.b',1,[]),
('4.0',2,[L(F+'s5.5.5','order of steps for smoking fish')]),
('4.1',1,[]),
('4.2',1,[L(F+'s5.5.0','smoke chemicals inhibit microbes')]),
('4.3',1,[L(F+'s5.5.3','cold smoking temperature')]),
('4.4',1,[L(F+'s5.5.3','cold smoking not cooked')]),
('4.5',1,[L(F+'s5.5.4','hot smoking cooks the food')]),
('4.6',1,[]),('4.7',1,[]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),('5.4',1,[]),('5.5',1,[]),('5.6',1,[]),('5.7',1,[]),
]
json.dump({P+k:{"cost":c,"needs":n} for k,c,n in d},open('../../point-links/hom-fish-seafood-s4.t1g1.json','w'),indent=1)
