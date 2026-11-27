import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
# (suffix list, cost list) per subsection, explicit; b first then 0..n
sub={0:[1]*6,1:[1]*7,2:[1]*8,3:[1]*9,4:[1]*7,5:[1]*4,6:[1]*7,7:[1,1,1,1,2,1,2],8:[1,1,1,1,1,2],9:[1]*3,10:[1]*5,11:[1]*5,12:[1]*4,13:[1]*4,14:[1]*5,15:[1]*4,16:[1]*7,17:[1]*3,18:[1]*4,19:[1]*5}
# note 7: b,0,1,2,3,4,5 -> costs b1,0 1,1 1,2 1,3 2,4 1,5 2
sub[7]=[1,1,1,1,2,1,2]
cost={}
for s,cs in sub.items():
    names=['b']+[str(i) for i in range(len(cs)-1)]
    for n,c in zip(names,cs): cost['chem23-s1.%d.%s'%(s,n)]=c
def L(i,st,w,c='high'): return {"id":i,"strength":st,"why":w,"confidence":c}
g1={
'1.3':[L('chem23-s3.1.b','helpful','alkanes and aromatics defined','low')],
'1.5':[L('chem23-s3.10.1','helpful','boiling point rises with size','high')],
'4.0':[L('chem23-s3.2.5','helpful','alkenes form addition polymers')],
'4.4':[L('chem23-s3.11.1','helpful','like dissolves like, non-polar solvents')],
'4.5':[L('chem23-s1.1.5','helpful','largest molecules at bottom of column')],
'5.0':[L('chem23-s3.10.3','helpful','small alkanes are gases')],
'5.1':[L('chem23-s3.2.4','helpful','alkenes react by addition')],
'5.2':[L('chem23-s3.10.4','helpful','large alkanes liquids or waxy solids','low')],
'3.7':[L('chem23-s3.3.5','helpful','ethyne burns in oxygen for welding')],
'7.3':[L('chem23-s1.7.0','essential','mole ratio from combustion equation'),L('chem23-s1.7.2','essential','moles from mass and molar mass')],
'7.4':[L('chem23-s1.7.1','essential','octane combustion equation')],
'7.5':[L('chem23-s1.7.1','essential','octane combustion equation'),L('chem23-s1.7.4','essential','moles of octane')],
'8.0':[L('chem20-s1.1.2','essential','burning returns stored carbon to atmosphere')],
'8.1':[L('chem20-s1.3.3','essential','greenhouse gases absorb and re-emit IR')],
'8.2':[L('chem23-s1.8.1','helpful','methane as greenhouse gas')],
'8.4':[L('chem20-s1.14.1','helpful','CO2 dissolving lowers ocean pH')],
'9.0':[L('chem20-s1.16.1','helpful','carbon capture and storage detail','low')],
'10.1':[L('chem20-s1.10.0','helpful','NOx formation in engines')],
'10.2':[L('chem20-s1.10.5','helpful','sulfur oxides from burning fuels')],
'10.3':[L('chem23-s3.4.6','helpful','benzene is carcinogenic','low')],
'11.0':[L('chem23-s1.10.0','helpful','carbon monoxide from incomplete combustion')],
'11.2':[L('chem23-s1.10.1','helpful','nitrogen oxides formation')],
'11.3':[L('chem23-s1.10.2','helpful','sulfur dioxide formation')],
'12.2':[L('chem23-s1.10.1','helpful','pollutants these devices remove','low')],
'13.0':[L('chem23-s3.2.5','helpful','alkenes form addition polymers')],
'13.1':[L('chem23-s3.20.3','helpful','addition polymers alkane-like, slow to break down')],
'13.2':[L('chem23-s1.13.1','essential','bonds resist microorganisms')],
'18.2':[L('chem23-s1.4.b','helpful','hydrocarbons as feedstocks','low')],
}
g2={
'3.0':[L('chem21-s5.0.1','essential','complete combustion gives CO2 and water')],
'6.1':[L('chem1-s2.8.b','helpful','judging authority, evidence, date, bias')],
'6.2':[L('chem1-s2.7.0','helpful','peer-reviewed sources most reliable')],
'6.0':[L('chem1-s2.5.0','helpful','focused research question')],
'7.0':[L('chem21-s5.0.1','essential','complete combustion gives CO2 and water')],
'7.1':[L('chem21-s5.1.b','helpful','balancing combustion equations')],
'10.0':[L('chem21-s5.0.2','essential','incomplete combustion gives CO and soot')],
'19.3':[L('chem1-s2.8.b','helpful','judging source limitations','low')],
}
def out(path,pack,links,withcost):
    txt=open(D+'packs/'+pack).read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for k in cost:
        e={}
        if withcost:e['cost']=cost[k]
        e['needs']=links.get(k.split('s1.')[1],[])
        res[k]=e
    for v in res.values():
        for n in v['needs']: assert n['id'] in ids and True
    tgt=[x for x in re.findall(r'^\[(chem23-s1\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
    assert tgt==list(res), (set(tgt)^set(res))
    for k,v in res.items():
        for n in v['needs']: assert n['id']!=k
    json.dump(res,open(D+'point-links/'+path,'w'),indent=0)
    j=json.load(open(D+'point-links/'+path))
    nl=sum(len(v['needs']) for v in j.values())
    lo=sum(n['confidence']=='low' for v in j.values() for n in v['needs'])
    print(path,len(j),nl,sum(v.get('cost')==2 for v in j.values()) if withcost else '-',lo)
out('chem23-s1.t1g1.json','chem23-s1.t1g1.txt',g1,True)
out('chem23-s1.t1g2.json','chem23-s1.t1g2.txt',g2,False)
