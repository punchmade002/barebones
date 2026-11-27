import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,w,c='h'): return {"id":i,"strength":"helpful","why":w,"confidence":{'h':'high','l':'low'}[c]}
p='chem24-s3.'
L2={ '3.4':[L('chem25-s1.13.0','biodegradable meaning')],
 '4.1':[L('chem25-s1.3.5','combustion releases energy')],
 '4.4':[L('chem25-s1.7.0','polymer and monomer definitions')],
 '4.5':[L('chem25-s1.9.0','poly(ethene) from ethene')],
 '4.6':[L('chem25-s1.10.0','PVC from chloroethene')],
 '4.7':[L('chem25-s1.12.6','properties of addition polymers')],
 '5.5':[L('chem25-s1.7.0','monomers link into polymers')],
 '8.0':[L('chem25-s1.3.5','combustion gives carbon dioxide','l')],
 '8.2':[L('chem25-s1.13.1','addition polymers non-biodegradable')],
 '8.3':[L('chem25-s1.14.2','microplastics form')],
 '8.4':[L('chem25-s1.15.2','burning PVC releases toxic gas','l')],
 '10.1':[L('chem25-s1.15.0','recycling and reuse')],
 '10.2':[L('chem25-s1.13.0','biodegradable meaning')],
 '14.3':[L('chem25-s1.1.3','esterification','l')],
 '21.5':[L('chem25-s1.1.3','esterification of an -OH','l')],
}
txt=open(P+'packs/chem24-s3.t1g2.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',txt.split('\nCANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
for k in L2: assert p+k in tg
out={k:{"needs":L2.get(k[len(p):],[])} for k in tg}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(P+'point-links/chem24-s3.t1g2.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
