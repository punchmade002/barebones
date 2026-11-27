import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
E,H='essential','helpful'
def run(name,pre,data):
    txt=open(D+'packs/'+name+'.txt').read()
    tid=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={};lows=0;links=0;c2=0
    for k,(c,needs) in data.items():
        out[pre+k]={"cost":c,"needs":[{"id":pre+n,"strength":s,"why":w,"confidence":f} for n,s,w,f in needs]}
        c2+=c==2;links+=len(needs);lows+=sum(n[3]=='low' for n in needs)
    assert list(out)==tid,(set(tid)^set(out))
    for v in out.values():
        for n in v['needs']: assert n['id'] in allids
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),links,c2,lows)
w={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[('0.0',H,'paid work','high')]),
'0.2':(2,[('0.0',H,'paid employment','high')]),'0.3':(2,[]),'0.4':(1,[('0.3',H,'unpaid work in the home','high')]),
'0.5':(1,[]),'0.6':(1,[('0.5',H,'voluntary work','high')]),
'0.7':(2,[('0.0',E,'paid work type','high'),('0.3',E,'unpaid home work type','high'),('0.5',E,'voluntary work type','high')]),
'0.8':(1,[('0.0',H,'paid work brings income','high')]),
'1.b':(1,[]),'1.0':(2,[]),'1.1':(1,[('1.0',H,'pay as extrinsic reward','high')]),'1.2':(1,[]),
'1.3':(1,[('1.0',E,'extrinsic rewards','high')]),'1.4':(2,[]),'1.5':(1,[]),'1.6':(1,[]),
'1.7':(1,[('1.4',H,'intrinsic satisfaction','high')]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[('2.0',H,'work ethic','high')]),'2.2':(1,[('2.0',E,'work ethic','high')]),
'2.3':(2,[]),'2.4':(1,[('2.3',H,'work attainment','high')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[('1.6',H,'status and identity from work','low')]),
'3.4':(1,[]),'3.5':(2,[]),'3.6':(1,[]),
'4.b':(1,[('1.b',H,'intrinsic and extrinsic satisfaction','high')]),
'4.0':(1,[('1.4',E,'intrinsic satisfaction','high')]),'4.1':(1,[('1.0',E,'extrinsic rewards','high')]),
'4.2':(1,[]),'4.3':(1,[('0.1',H,'self-employment','high'),('1.4',H,'intrinsic satisfaction','high')]),
'4.4':(1,[('1.6',H,'status from work','high')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[('1.4',E,'intrinsic satisfaction','high')]),
'5.2':(1,[('1.0',E,'extrinsic satisfaction','high')]),'5.3':(1,[]),
'5.4':(2,[('1.4',E,'intrinsic satisfaction','high'),('1.0',E,'extrinsic satisfaction','high')]),
'6.b':(1,[]),'6.0':(2,[('1.b',E,'intrinsic and extrinsic sources','high')]),
'6.1':(1,[('1.4',E,'intrinsic satisfaction','high')]),'6.2':(1,[]),'6.3':(1,[('1.0',E,'extrinsic satisfaction','high')]),
'6.4':(1,[]),'6.5':(1,[]),
}
# fix ids: keys like '1.6' above refer to numbered ids; ok
run('hom-work-leisure-s1.t1g1','hom-work-leisure-s1.',w)
p={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[('6.b',H,'welfare payments','low')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[('3.3',H,'voluntary deduction','high')]),
'1.3':(1,[('6.b',H,'welfare payments','low')]),'1.4':(2,[]),
'2.b':(1,[]),'2.0':(1,[('1.2',H,'pensions','high')]),'2.1':(1,[]),'2.2':(2,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[('3.0',E,'gross income','high')]),'3.2':(1,[('4.b',H,'PAYE PRSI USC','high')]),
'3.3':(2,[]),'3.4':(1,[('3.1',E,'net income','high')]),
'4.b':(1,[]),'4.0':(2,[]),'4.1':(1,[('4.0',H,'PAYE calculation','high')]),'4.2':(1,[('4.0',H,'PAYE','high')]),
'4.3':(2,[]),'4.4':(1,[('4.3',E,'PRSI','high')]),'4.5':(2,[]),'4.6':(1,[('4.5',E,'USC','high')]),
'5.b':(1,[('4.0',H,'income tax PAYE','high')]),'5.0':(1,[('4.0',H,'income tax PAYE','high')]),
'5.1':(2,[('5.0',E,'tax credits','high'),('3.0',H,'gross income','high')]),
'5.2':(1,[('5.0',E,'tax credits','high')]),'5.3':(1,[('4.5',E,'USC','high')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[('6.0',H,'social insurance payments','high')]),
'6.2':(1,[('6.0',H,'contrast with social insurance','high')]),'6.3':(1,[('6.2',H,'social assistance','high')]),
'6.4':(1,[('6.2',H,'means-tested payments','high')]),
'7.b':(1,[('6.4',H,'means test','high')]),'7.0':(1,[]),'7.1':(2,[('6.4',E,'means test','high')]),
'7.2':(1,[('6.4',H,'means test','high')]),'7.3':(1,[]),'7.4':(1,[('6.0',H,'social insurance payment','high')]),'7.5':(2,[]),
'8.b':(1,[('6.b',H,'insurance versus assistance','high')]),'8.0':(1,[('6.0',H,'PRSI-based payments','high')]),
'8.1':(1,[('6.4',H,'means test','high')]),'8.2':(1,[('6.4',E,'means-tested','high')]),'8.3':(1,[('6.4',H,'means test','high')]),
}
run('hom-personal-finance-s1.t1g1','hom-personal-finance-s1.',p)
c={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(2,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[('0.0',H,'line','high')]),'1.0':(1,[('0.0',E,'line','high')]),'1.1':(1,[('0.0',E,'line','high')]),
'1.2':(1,[('0.0',H,'line','high')]),'1.3':(1,[('0.0',H,'line','high')]),'1.4':(1,[('1.0',H,'vertical line effect','high')]),
'2.b':(1,[]),'2.0':(1,[('0.2',E,'colour tone','high')]),'2.1':(1,[('0.2',E,'colour','high')]),
'2.2':(1,[('0.3',E,'contrasting colour schemes','high')]),'2.3':(1,[('0.4',E,'texture','high')]),'2.4':(1,[('0.4',E,'texture','high')]),
'3.b':(1,[]),'3.0':(1,[('0.5',E,'pattern','high')]),'3.1':(1,[('1.0',E,'vertical lines','high')]),
'3.2':(1,[('0.5',E,'pattern','high')]),'3.3':(1,[('0.1',E,'shape','high')]),'3.4':(1,[('0.1',E,'shape','high')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),'5.0':(2,[('1.0',E,'vertical lines','high'),('2.0',E,'dark colour effect','high')]),
'5.1':(2,[('2.0',E,'light colour effect','high')]),'5.2':(1,[('3.2',E,'pattern draws the eye','high')]),
'5.3':(1,[('2.0',E,'dark colours reduce size','high')]),'5.4':(1,[('0.3',H,'colour suits wearer','high')]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[('0.0',H,'line from seams','high')]),'6.1':(1,[]),'6.2':(1,[('1.4',E,'princess seam','high')]),
'6.3':(1,[]),'6.4':(1,[('4.2',H,'emphasis','low')]),'6.5':(1,[]),'6.6':(1,[('0.5',H,'pattern','low')]),
'7.b':(1,[]),'7.0':(2,[]),'7.1':(2,[]),'7.2':(2,[('4.b',H,'principles of design','high')]),
'7.3':(1,[('7.0',H,'function','high')]),'7.4':(1,[('5.0',H,'flattering with line/colour','high')]),'7.5':(1,[]),'7.6':(1,[]),
}
run('hom-clothing-selection-s4.t1g1','hom-clothing-selection-s4.',c)
