import json,re
P='bio27-s1.'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(2,[]),
'0.3':(2,[('0.2','h','digestion definition')]),
'0.4':(1,[('0.3','h','absorbed digestion products')]),
'0.5':(1,[('0.2','h','products of digestion')]),
'0.6':(1,[]),
'0.7':(1,[('0.6','e','egestion definition')]),
'1.b':(1,[]),'1.0':(2,[]),
'1.1':(1,[('1.0','h','gut as the tube')]),
'1.2':(1,[('1.0','h','gut lining')]),
'1.3':(1,[('1.0','h','parts of the gut')]),
'2.b':(1,[]),
'2.0':(2,[('4.0','h','saliva and salivary glands')]),
'2.1':(1,[('1.1','e','peristalsis')]),
'2.2':(1,[('2.1','h','oesophagus route')]),
'2.3':(1,[('1.0','h','position in the gut')]),
'2.4':(2,[('2.3','h','stomach structure'),('0.2','h','protein digestion by enzymes')]),
'2.5':(1,[('1.3','e','sphincter function'),('2.4','h','chyme')]),
'3.b':(1,[]),
'3.0':(2,[('4.1','h','bile from liver'),('4.4','h','pancreatic juice')]),
'3.1':(1,[('3.0','h','small intestine parts')]),
'3.2':(1,[('1.0','h','gut order')]),
'3.3':(1,[('3.2','h','appendix location')]),
'3.4':(1,[('3.2','h','colon as part'),('0.7','h','egestion not excretion')]),
'3.5':(1,[('0.6','h','egestion')]),
'3.6':(1,[('1.3','h','sphincters')]),
'4.b':(1,[]),
'4.0':(1,[('2.0','h','saliva added in mouth')]),
'4.1':(1,[]),
'4.2':(2,[('0.5','h','absorbed products of digestion')]),
'4.3':(1,[('4.1','e','bile')]),
'4.4':(2,[('3.0','h','duodenum')]),
'4.5':(1,[('4.4','h','pancreas')]),
'4.6':(1,[('4.b','e','associated organs, ducts')]),
'5.b':(1,[]),
'5.0':(2,[('1.0','h','order of gut parts'),('4.6','h','associated organs')]),
'6.b':(1,[]),
'6.0':(1,[('0.2','h','mechanical and chemical digestion')]),
'6.1':(1,[('2.1','h','oesophagus transport')]),
'6.2':(1,[('2.4','h','stomach churning, protein')]),
'6.3':(1,[('3.0','h','duodenum digestion')]),
'6.4':(1,[('3.1','h','ileum absorption')]),
'6.5':(1,[('3.4','h','colon water absorption')]),
'6.6':(1,[('3.5','h','rectum storage')]),
'6.7':(1,[('3.6','h','anus'),('0.6','h','egestion')]),
}
txt=open('points/bio27-s1.txt').read()
ids=re.findall(r'^\[(bio27-s1\.[^\]]+)\]',txt,re.M)
out={}
for i in ids:
    c,n=d[i[len(P):]]
    out[i]={"cost":c,"needs":[{"id":P+a,"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high"} for a,s,w in n]}
assert set(i[len(P):] for i in ids)==set(d)
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open('point-links/bio27-s1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()))
