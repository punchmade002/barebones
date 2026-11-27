import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E='essential';H='helpful'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
P='chem20-s2.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'1.b':(1,[]),'1.0':(2,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[L(P+'1.0',H,'energy used in processing water')]),
'2.b':(1,[]),
'2.0':(1,[L('chem8-s2.13.0',H,'p.p.m. as a unit')]),
'2.1':(1,[]),
'2.2':(2,[L(P+'2.0',E,'dissolved oxygen in water'),L(P+'2.1',H,'bacteria use oxygen breaking organic matter')]),
'2.3':(2,[L(P+'2.2',E,'BOD definition')]),
'2.4':(1,[L(P+'2.2',E,'BOD values in mg per litre')]),
'2.5':(1,[L(P+'2.2',H,'BOD of farm waste')]),
'3.b':(1,[]),
'3.0':(1,[L(P+'2.2',E,'BOD test conditions')]),
'3.1':(1,[L(P+'2.0',H,'oxygen solubility falls when warmer')]),
'3.2':(1,[L(P+'2.2',H,'five-day BOD definition')]),
'3.3':(1,[L(P+'2.2',E,'dissolved oxygen is what BOD measures')]),
'3.4':(2,[L(P+'3.0',H,'dark prevents photosynthesis')]),
'3.5':(1,[L(P+'3.4',E,'sample incubated five days')]),
'3.6':(1,[L(P+'3.5',E,'initial and final oxygen readings')]),
'3.7':(1,[L(P+'3.4',E,'bottle set-up for incubation')]),
'4.b':(1,[]),
'4.0':(1,[L(P+'2.2',E,'BOD')]),
'4.1':(1,[L(P+'6.b',H,'eutrophication')]),
'4.2':(1,[]),'4.3':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L(P+'2.2',E,'BOD')]),
'5.2':(1,[L(P+'6.b',H,'eutrophication')]),
'5.3':(1,[]),
'5.4':(1,[L('chem8-s2.13.1',H,'mg per litre concentration','low')]),
'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(2,[L(P+'2.1',E,'aerobic bacteria decompose, use oxygen'),L(P+'2.2',H,'BOD rises','low')][:1]),
'6.3':(1,[L(P+'6.2',E,'oxygen depletion after algae die')]),
'6.4':(1,[]),
'6.5':(1,[L(P+'6.0',H,'nutrient sources to cut')]),
'6.6':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L('chem11-s2.11.0',H,'pH scale','low')]),
'7.2':(1,[L(P+'2.2',E,'BOD')]),
'7.3':(1,[L(P+'2.0',H,'warmer water holds less oxygen')]),
'7.4':(1,[L(P+'7.3',H,'less oxygen in warm water')]),
'7.5':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(2,[]),'8.2':(1,[]),'8.3':(1,[]),
'8.4':(1,[L(P+'8.3',E,'bioaccumulation')]),
'8.5':(2,[]),
'9.b':(1,[]),
'9.0':(1,[L(P+'11.b',H,'acidic water dissolves lead','low')]),
'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),
'9.4':(1,[L(P+'8.4',H,'biomagnification up food chain')]),
'9.5':(1,[]),'9.6':(1,[]),'9.7':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),
'10.4':(1,[L(P+'10.0',H,'microplastic size')]),
'10.5':(1,[]),'10.6':(1,[]),
'11.b':(1,[]),
'11.0':(1,[L('chem20-s1.10.5',H,'sulfur oxides from burning fuels','low')]),
'11.1':(2,[L(P+'11.0',H,'SO2 dissolving in rain')]),
'11.2':(2,[L('chem20-s1.10.1',H,'NO2 formation','low')]),
'11.3':(1,[L(P+'7.1',H,'acidic industrial waste water')]),
'11.4':(1,[L('chem20-s1.0.4',H,'CO2 dissolving to form acid')]),
'12.b':(1,[]),
'12.0':(1,[L('chem11-s2.11.0',H,'pH and H+ concentration','low')]),
'12.1':(1,[]),'12.2':(1,[]),
'12.3':(1,[L('chem20-s1.14.5',H,'acid dissolving calcium carbonate')]),
'12.4':(1,[L(P+'9.0',H,'lead from pipes')]),
}
for pk,out in (('t1g1',None),('t1g2',None)):
    txt=open(B+'packs/chem20-s2.%s.txt'%pk).read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(chem20-s2\.[\w.]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([\w.\-]+)\]',txt,re.M))
    R={}
    for i in ids:
        c,n=D[i.split('s2.',1)[1]]
        if pk=='t1g1': R[i]={"cost":c,"needs":n}
        else: R[i]={"needs":[]}
    n=0;lo=0;c2=0
    for v in R.values():
        for x in v['needs']:
            assert x['id'] in allids and x['id'] in tgt or x['id'] in allids; n+=1; lo+=x['confidence']=='low'
        c2+= v.get('cost')==2
    assert set(R)==set(ids) and len(ids)==len(set(ids))
    json.dump(R,open(B+'point-links/chem20-s2.%s.json'%pk,'w'),ensure_ascii=False)
    print(pk,len(ids),n,c2,lo)
