import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio8-s7.txt').read()
tgt=re.findall(r'^\[(bio8-s7\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
H,E='helpful','essential'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
d={t:{"cost":1,"needs":[]} for t in tgt}
def S(k,cost=None,*needs):
    if cost:d[k]['cost']=cost
    d[k]['needs']=list(needs)
S('bio8-s7.0.2',None,n('bio2-s2.0.1',H,'independent variable'),n('bio2-s2.0.2',H,'dependent variable'))
S('bio8-s7.0.3',None,n('bio2-s2.0.3',H,'controlled variables'))
S('bio8-s7.0.4',None,n('bio2-s2.2.3',H,'negative control'))
S('bio8-s7.0.5',None,n('bio2-s2.2.4',H,'positive control'))
S('bio8-s7.0.6',None,n('bio8-s7.0.4',E,'negative control colour'),n('bio8-s7.0.5',E,'positive control colour'))
S('bio8-s7.2.1',None,n('bio8-s7.2.0',H,'crushed food in water'))
S('bio8-s7.3.b',None,n('bio8-s2.3.1',H,'starch as plant storage'))
S('bio8-s7.3.2',None,n('bio8-s7.0.4',H,'negative control'),n('bio8-s7.0.5',H,'positive control'))
S('bio8-s7.3.3',None,n('bio8-s2.3.1',H,'starch','low'))
S('bio8-s7.4.0',2,n('bio8-s2.0.2',H,'mono/disaccharide sugars'))
S('bio8-s7.4.3',None,n('bio8-s7.0.4',H,'negative control'),n('bio8-s7.0.5',H,'positive control'))
S('bio8-s7.4.4',2,n('bio8-s7.4.0',E,'reducing sugar definition'))
S('bio8-s7.4.5',2,n('bio8-s7.4.0',E,'reducing sugar reduces copper(II)'),n('bio8-s7.4.4',H,'colour sequence'))
S('bio8-s7.4.6',None,n('bio8-s7.4.4',H,'brick-red result'))
S('bio8-s7.4.7',2,n('bio8-s2.2.2',E,'hydrolysis of disaccharide'),n('bio8-s2.2.4',H,'sucrose = glucose + fructose'))
S('bio8-s7.5.b',None,n('bio8-s2.7.4',H,'peptide bonds join amino acids'))
S('bio8-s7.5.3',None,n('bio8-s2.7.4',E,'peptide bonds'))
S('bio8-s7.6.b',None,n('bio8-s2.4.1',H,'lipids insoluble in water'))
S('bio8-s7.6.2',None,n('bio8-s7.6.0',E,'grease-spot method'))
S('bio8-s7.6.3',None,n('bio8-s2.4.1',H,'lipid dissolves dye, not water','low'))
S('bio8-s7.6.5',None,n('bio8-s7.6.3',E,'Sudan III method'))
S('bio8-s7.7.1',None,n('bio8-s7.4.2',H,'Benedict\'s water bath heating'))
S('bio8-s7.7.2',None,n('bio8-s7.6.3',H,'Sudan III stain'))
S('bio8-s7.8.1',2,n('bio8-s7.4.0',H,'sucrose non-reducing'))
S('bio8-s7.8.2',None,n('bio8-s7.0.1',H,'hypothesis'))
S('bio8-s7.9.0',None,n('bio8-s7.0.6',H,'comparing with controls'))
S('bio8-s7.9.3',None,n('bio8-s7.2.0',H,'crushing breaks open cells'))
S('bio8-s7.9.4',None,n('bio8-s7.4.0',E,'reducing vs non-reducing sugar'))
S('bio8-s7.9.6',None,n('bio8-s7.4.2',H,'hot water bath step'))
for t,v in d.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(d,open(P+'point-links/bio8-s7.json','w'),indent=1)
r=json.load(open(P+'point-links/bio8-s7.json'))
assert list(r)==tgt
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
