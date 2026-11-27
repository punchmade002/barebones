import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry'
last={0:4,1:2,2:5,3:2,4:5,5:2,6:4,7:3,8:1,9:1,10:6,11:7,12:4,13:2,14:5,15:2,16:6,17:3,18:4,19:6,20:4,21:3,22:5,23:7,24:7,25:7}
ids=[]
for s in range(26):
    ids.append(f'chem25-s2.{s}.b'); ids+= [f'chem25-s2.{s}.{i}' for i in range(last[s]+1)]
def L(i,st,w,c='high'): return {"id":i,"strength":st,"why":w,"confidence":c}
links={
'2.2':[L('chem9-s2.10.0','helpful','heat flammable liquids in water bath')],
'3.1':[L('chem9-s2.10.0','helpful','water bath for flammable liquids')],
'6.3':[L('chem18-s1.0.7','helpful','weak acid only partly dissociated')],
'20.1':[L('chem18-s1.0.5','helpful','esterification is reversible')],
'21.0':[L('chem18-s1.1.0','helpful','equilibrium: forward and reverse rates equal')],
'21.1':[L('chem18-s1.7.1','helpful','partial conversion at equilibrium','low')],
'22.3':[L('chem9-s2.10.2','helpful','Liebig condenser')],
'22.4':[L('chem9-s2.10.0','helpful','water bath for flammable liquids')],
'23.0':[L('chem9-s2.12.0','helpful','separating funnel purifies ester')],
'23.1':[L('chem9-s2.12.b','helpful','immiscible layers by density')],
'23.3':[L('chem9-s2.12.2','helpful','run off lower layer through tap')],
'23.5':[L('chem9-s2.9.0','helpful','distillation by boiling point')],
'24.1':[L('chem18-s1.7.6','helpful',"Le Chatelier shifts equilibrium",'low')],
'24.2':[L('chem9-s2.10.0','helpful','water bath not naked flame')],
'24.4':[L('chem9-s2.10.1','helpful','never heat a closed system')],
'24.7':[L('chem9-s2.9.0','helpful','distillation by boiling point')],
'25.2':[L('chem26-s2.6.0','helpful','reaction not going to completion')],
'25.3':[L('chem26-s2.6.2','helpful','product lost in transfers')],
'25.4':[L('chem26-s2.0.3','essential','percentage yield definition')],
}
out={i:{"needs":links.get(i.split('chem25-s2.')[1],[])} for i in ids}
# check
txt=open(D+'/packs/chem25-s2.t1g3.txt').read()
tgt=re.findall(r'^\[(chem25-s2\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert tgt==ids,(set(tgt)^set(ids))
assert all(n['id'] in allids for v in out.values() for n in v['needs'])
assert set(links)<=set(i.split('chem25-s2.')[1] for i in ids)
json.dump(out,open(D+'/point-links/chem25-s2.t1g3.json','w'),ensure_ascii=False,indent=0)
n=sum(len(v['needs']) for v in out.values())
print(len(out),n,sum(1 for v in out.values() for x in v['needs'] if x['confidence']=='low'))
