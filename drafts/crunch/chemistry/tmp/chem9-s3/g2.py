import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem9-s3.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
'0.0':[L('chem1-s4.6.0','helpful','inversely proportional')],
'1.0':[L('chem1-s4.6.0','helpful','directly proportional')],
'2.0':[L('chem1-s4.6.0','helpful','directly proportional')],
'3.0':[L('chem1-s4.0.3','helpful','kelvin and Celsius scales')],
'4.b':[L('chem1-s4.6.0','helpful','what proportional means on a graph')],
'4.0':[L('chem1-s4.5.0','helpful','labelling graph axes with units'),L('chem1-s4.6.0','essential','straight line through origin means proportional')],
'7.0':[L('chem1-s4.0.0','helpful','SI units pascal and cubic metre')],
'7.1':[L('chem1-s4.0.0','helpful','SI derived units')],
'8.b':[L('chem1-s4.0.5','helpful','converting units with conversion factors')],
'8.0':[L('chem1-s4.0.4','essential','kPa to Pa')],
'8.1':[L('chem1-s4.0.1','essential','cm³ to larger volume units')],
'8.2':[L('chem1-s4.0.1','essential','litre and cubic metre relations')],
'8.3':[L('chem1-s4.0.3','essential','°C to K conversion')],
'9.3':[L('chem1-s4.6.6','helpful','rearranging equations')],
'9.4':[L('chem1-s4.1.8','helpful','significant figures')],
'9.5':[L('chem1-s4.0.1','helpful','m³ to litres')],
'10.2':[L('chem1-s4.6.6','helpful','rearranging equations')],
'10.3':[L('chem1-s4.1.8','helpful','significant figures')],
'11.3':[L('chem1-s4.1.8','helpful','significant figures')],
'12.2':[L('chem1-s4.6.6','helpful','rearranging equations')],
'12.3':[L('chem1-s4.1.8','helpful','significant figures')],
}
raw=open(D+'packs/chem9-s3.t1g2.txt').read()
ids=re.findall(r'^\[(\S+?)\]',raw.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',raw,re.M))
assert set(P+k for k in links)<=set(ids)
out={i:{"needs":links.get(i[len(P):],[])} for i in ids}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(D+'point-links/chem9-s3.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(ids),sum(len(v['needs']) for v in out.values()),0,0)
