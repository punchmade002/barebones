import json
T='hom-family-law-s6.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),'0.0':(1,[L('0.b','helpful','uses will and estate')]),
'0.1':(2,[L('0.0','essential','uses intestacy rules')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'0.7':(1,[L('0.3','helpful','uses executor')]),'0.8':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L('1.3','helpful','follows the witnessing step')]),
'1.5':(2,[L('0.3','helpful','contrasts with executor','low')]),
'1.6':(1,[L('0.3','helpful','uses executor')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[L('0.3','helpful','uses executor role')]),
'2.3':(2,[L('4.0','helpful','uses spouse legal right','low')]),
'2.4':(1,[]),
'2.5':(1,[L('1.3','helpful','uses two-witness rule')]),
'2.6':(1,[L('0.3','helpful','uses executor')]),
'3.b':(1,[]),
'3.0':(1,[L('1.3','helpful','uses signing and witnessing rules')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(1,[L('0.3','helpful','uses executor')]),
}
out={T+k:{"cost":c,"needs":[dict(n,id=T+n['id']) for n in ns]} for k,(c,ns) in d.items()}
json.dump(out,open('point-links/hom-family-law-s6.t1g1.json','w'),indent=0)
