import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem1-s4.'
def L(k,s,w,c='h'): return {"id":P+k,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":'high' if c=='h' else 'low'}
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(2,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L('0.1','h','volume unit conversions')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[L('1.1','h','precision')]),
'1.3':(1,[L('1.1','e','precision'),L('1.0','h','accuracy')]),
'1.4':(1,[L('1.0','e','accuracy'),L('1.1','h','precision')]),
'1.5':(1,[]),
'1.6':(2,[L('1.5','e','instrument uncertainty')]),
'1.7':(1,[L('1.0','h','accuracy of glassware')]),
'1.8':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('2.0','e','random error')]),
'2.2':(1,[]),
'2.3':(1,[L('2.2','e','systematic error')]),
'2.4':(1,[L('2.2','e','systematic error'),L('2.0','h','repeating reduces random error')]),
'2.5':(1,[L('2.1','h','reading the meniscus')]),
'2.6':(1,[]),
'2.7':(1,[L('1.0','h','accepted value')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),
'3.2':(1,[L('3.0','h','qualitative data'),L('3.1','h','quantitative data')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L('4.0','h','column layout')]),
'4.2':(1,[L('1.2','e','resolution of instrument')]),
'5.b':(1,[]),
'5.0':(1,[L('4.0','h','independent and dependent variables')]),
'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[L('5.2','h','plotted points')]),
'5.4':(1,[L('5.3','h','line of best fit')]),
'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L('5.3','h','straight line on graph')]),
'6.2':(1,[L('6.1','e','gradient'),L('5.3','h','curve of best fit')]),
'6.3':(1,[L('5.3','h','line of best fit')]),
'6.4':(1,[L('6.3','e','interpolation and extrapolation')]),
'6.5':(1,[]),'6.6':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L('7.0','e','standard form')]),
'7.2':(1,[L('7.0','e','standard form')]),
'8.b':(1,[]),
'8.0':(1,[L('2.6','h','anomalous results')]),
'8.1':(1,[L('8.0','e','anomalous result'),L('5.3','h','line of best fit')]),
'8.2':(1,[L('6.0','h','describing the relationship')]),
'8.3':(1,[]),
'8.4':(1,[L('8.2','h','conclusion from data')]),
'8.5':(1,[]),
}
pk=open(B+'packs/chem1-s4.t1g1.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',pk,re.M)
assert tg==[P+k for k in D],[t for t in tg if t[len(P):] not in D]
out={}
for k,(c,n) in D.items():
    for x in n: assert x['id'] in tg and x['id']!=P+k
    out[P+k]={"cost":c,"needs":n}
json.dump(out,open(B+'point-links/chem1-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
