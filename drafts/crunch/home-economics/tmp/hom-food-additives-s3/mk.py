import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-food-additives-s3.'
def L(i,s,w,c='high'): return {"id":i if '-s3.' in i and i.startswith('hom-') else P+i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),
'0.2':(1,[L('0.b','helpful','defines contaminant')]),
'0.3':(1,[L('0.b','helpful','defines contaminant')]),
'0.4':(1,[]),'0.5':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[L('1.0','helpful','uses pesticide types')]),
'1.2':(2,[L('1.0','helpful','effects of pesticides')]),
'1.3':(1,[L('0.2','helpful','residues left after legitimate use')]),
'1.4':(1,[L('0.2','helpful','maximum residue limits')]),
'1.5':(1,[L('0.2','helpful','pesticide residue on produce')]),
'1.6':(1,[L('0.5','helpful','agencies under FSAI service contracts')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('0.2','helpful','veterinary residues')]),
'2.2':(2,[L('2.1','helpful','antibiotic residues in milk')]),
'2.3':(1,[L('2.1','helpful','antibiotic residues')]),
'2.4':(1,[L('2.1','helpful','antibiotic residues')]),
'2.5':(1,[L('2.1','helpful','withdrawal periods')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[L('3.0','helpful','heavy metals as contaminants')]),
'3.2':(2,[L('3.0','helpful','heavy metals entering food')]),
'3.3':(2,[L('3.0','helpful','heavy metals such as mercury'),L('hom-environmental-issues-s3.4.3','helpful','toxins accumulating up food chain','low')]),
'3.4':(1,[L('3.0','helpful','heavy metals')]),
'3.5':(2,[L('3.0','helpful','heavy metals')]),
'3.6':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L('4.0','helpful','lubricants as contaminants')]),
'4.2':(1,[]),
'4.3':(1,[L('4.2','essential','migration from packaging')]),
'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(2,[L('1.3','helpful','pre-harvest interval'),L('2.1','helpful','withdrawal periods')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[L('1.5','helpful','washing and peeling produce')]),
'5.5':(1,[]),
}
txt=open(B+'packs/hom-food-additives-s3.t1g1.txt').read()
ids=re.findall(r'^\[(hom-food-additives-s3\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    c,n=D[i[len(P):]]; out[i]={"cost":c,"needs":n}
assert len(D)==len(ids)==len(out)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(B+'point-links/hom-food-additives-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
