import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem1-s3.'
E,H='essential','helpful'
two={'3.2','4.0','8.6','2.1'}
L={'0.1':[('0.0',H,'scientific question defined')],'1.1':[('1.0',H,'independent variable')],
'1.2':[('1.0',H,'variable being changed')],'2.1':[('1.0',E,'independent variable'),('1.1',E,'dependent variable')],
'2.3':[('2.0',H,'hypothesis')],'2.4':[('2.0',E,'hypothesis')],'3.3':[('3.2',E,'criteria for comparing strategies')],
'4.0':[('1.0',H,'variables in plan')],'4.1':[('8.1',H,'risk defined')],'4.2':[('1.0',E,'independent variable values')],
'4.3':[('1.2',H,'controlled factors')],'5.0':[('1.2',E,'controlled variables')],'5.1':[('5.0',E,'fair test')],
'5.3':[('5.2',E,'reliability')],'8.1':[('8.0',E,'hazard vs risk')],'8.2':[('8.0',E,'hazard')],
'8.3':[('8.1',E,'risk')],'8.4':[('8.3',H,'assessed risk')],'8.6':[('8.2',H,'hazard pictograms')],'8.7':[('8.1',H,'risk of harm')]}
txt=open(D+'packs/chem1-s3.t1g1.txt').read()
ids=re.findall(r'^\[(chem1-s3\.[^\]]+)\]',txt,re.M)
out={}
for i in ids:
    k=i[len(P):]
    out[i]={'cost':2 if k in two else 1,'needs':[{'id':P+t,'strength':s,'why':w,'confidence':'high'} for t,s,w in L.get(k,[])]}
for k in L: assert P+k in out
for i,v in out.items():
    for n in v['needs']: assert n['id'] in out and n['id']!=i
json.dump(out,open(D+'point-links/chem1-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),0)
