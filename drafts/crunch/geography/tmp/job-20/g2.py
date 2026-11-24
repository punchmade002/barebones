import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
ids=re.findall(r'^\[([^\]]+)\]',open(P+'packs/geo-economic-eu-s2.t1g2.txt').read(),re.M)
tg=[i for i in ids if i.startswith('geo-economic-eu-s2.')]
G='geo-economic-globalisation-s1.';K='geo-graph-skills-s1.'
L={'3.2':[(G+'0.0','helpful','multinational company definition','high')],
'4.0':[(K+'4.1','helpful','percentage change calculation','low')],
'4.1':[(K+'3.1','helpful','subtract to find difference','low')],
'9.0':[(K+'4.1','helpful','percentage change calculation','low')],
'10.0':[(G+'0.0','helpful','multinational company definition','low')],
'14.b':[(G+'1.b','helpful','foreign direct investment','high')],
'14.0':[(G+'4.0','helpful','Intel at Leixlip','high'),(G+'13.0','helpful','Apple in Cork','high')],
'14.1':[(G+'1.0','helpful','IDA Ireland role','high'),(G+'2.0','helpful','12.5% corporation tax','high')],
'14.2':[(G+'2.0','essential','15% global minimum tax','high')],
'17.0':[(G+'10.5','helpful','tax change risks MNC moving','low')]}
out={};n=0
for i in tg:
    nd=[{'id':t,'strength':s,'why':w,'confidence':c} for t,s,w,c in L.get(i[len('geo-economic-eu-s2.'):],[])]
    n+=len(nd);out[i]={'needs':nd}
bad=[(i,x['id']) for i,v in out.items() for x in v['needs'] if x['id'] not in ids]
assert not bad,bad
json.dump(out,open(P+'point-links/geo-economic-eu-s2.t1g2.json','w'),indent=1)
print(len(out),n,sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
