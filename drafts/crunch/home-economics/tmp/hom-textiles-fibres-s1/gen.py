import json
T='hom-textiles-fibres-s1.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'2.b':(1,[L('3.b','helpful','uses fabric properties')]),
'2.0':(1,[L('3.b','helpful','uses fabric properties','low')]),
'2.1':(1,[L('2.0','helpful','uses fitness for purpose')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L('3.5','helpful','uses drape','low')]),
'2.5':(2,[L('3.3','helpful','uses fade resistance, colourfast','low')]),
'2.6':(1,[L('3.1','helpful','uses flammability')]),
'2.7':(2,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(2,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),'3.6':(2,[]),'3.7':(1,[]),
'4.b':(1,[L('3.b','helpful','uses fabric properties')]),
'4.0':(1,[L('3.0','helpful','uses absorbent')]),
'4.1':(1,[L('3.0','helpful','uses absorbent')]),
'4.2':(2,[L('3.5','helpful','uses drape')]),
'4.3':(2,[L('3.6','helpful','uses shrink resistance and easy to dye','low')]),
'4.4':(2,[L('3.7','helpful','uses wool shrinking in hot wash','low')]),
'4.5':(1,[L('3.4','helpful','uses durable, hard wearing')]),
'4.6':(1,[]),
}
out={T+k:{"cost":c,"needs":[dict(n,id=T+n['id']) for n in ns]} for k,(c,ns) in d.items()}
json.dump(out,open('point-links/hom-textiles-fibres-s1.t1g1.json','w'),indent=0)
