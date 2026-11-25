import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur6-s5.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
# id: (cost, [links])
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L('hist-eur6-s2.0.0',H,'post-1945 US internationalism','low')]),
'0.2':(1,[]),
'0.3':(2,[L(P+'1.0'.replace('1.0','0.3'),E,'x')][:0]+[L('hist-eur6-s2.14.1',H,'Vietnamisation handing war to South')]),
'0.4':(1,[L('hist-eur6-s1.9.2',H,'Watergate and Nixon resignation')]),
'1.b':(1,[]),'1.0':(2,[]),
'1.1':(1,[L(P+'1.0',E,'the Paris Peace Accords'),L(P+'3.0',H,'Kissinger as negotiator')]),
'1.2':(1,[L(P+'1.0',H,'US withdrawal under the Accords')]),
'1.3':(2,[L('hist-eur6-s1.1.1',H,'presidential veto and congressional override','low')]),
'1.4':(1,[L(P+'1.3',E,'the War Powers Resolution')]),
'1.5':(1,[L(P+'1.0',H,'the Paris Accords it followed')]),
'2.b':(1,[]),
'2.0':(1,[L(P+'1.5',H,'Congress barring funds for Vietnam')]),
'2.1':(1,[L(P+'2.2',H,'the fall of Saigon')]),
'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L(P+'3.0',H,'Kissinger who made the policy')]),
'3.2':(2,[]),
'3.3':(1,[L(P+'3.2',E,"Nixon's opening to China")]),
'3.4':(2,[L(P+'4.0',H,'SALT I agreements','low')]),
'4.b':(1,[]),'4.0':(2,[]),
'4.1':(2,[L(P+'4.0',E,'the ABM Treaty as part of SALT I'),L(P+'0.0',H,'deterrence through retaliation')]),
'4.2':(1,[L(P+'4.0',H,'the Interim Agreement in SALT I')]),
'4.3':(1,[L(P+'4.2',E,'the missile limits being sidestepped'),L(P+'0.2',H,'MIRVs')]),
'4.4':(1,[L(P+'4.3',E,'MIRVs adding warheads')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L(P+'4.0',H,'SALT I as basis for a second SALT','low')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(P+'3.2',H,"Nixon's opening to China")]),
'6.2':(1,[]),
'6.3':(1,[L(P+'6.2',E,'the embassy seizure')]),
'6.4':(1,[L(P+'6.2',H,'the Iran hostage crisis')]),
'7.b':(1,[]),
'7.0':(2,[L(P+'4.0',H,'SALT I that SALT II built on')]),
'7.1':(1,[L(P+'7.0',E,'SALT II terms')]),
'7.2':(1,[]),
'7.3':(1,[L(P+'7.2',E,'the invasion of Afghanistan'),L(P+'7.0',H,'SALT II')]),
'7.4':(1,[L(P+'7.2',E,'response to Afghanistan invasion')]),
'7.5':(1,[L(P+'7.2',H,'Afghanistan invasion prompting it')]),
'7.6':(1,[L(P+'7.2',E,'boycott in response to Afghanistan')]),
'7.7':(1,[L(P+'7.3',H,'SALT II never ratified')]),
'8.b':(1,[]),
'8.0':(1,[L(P+'3.b',H,"Nixon's détente approach",'low')]),
'8.1':(1,[]),
'8.2':(1,[L(P+'8.1',H,'Pershing II missiles')]),
'9.b':(1,[L(P+'0.0',H,'deterrence by threat of retaliation')]),
'9.0':(1,[L(P+'0.2',H,'missile defence technology')]),
'9.1':(1,[L(P+'9.0',E,'the SDI proposal')]),
'9.2':(1,[L(P+'9.0',E,'SDI')]),
'9.3':(1,[L(P+'4.1',E,'the ABM Treaty'),L(P+'9.0',E,'SDI')]),
'10.b':(1,[]),'10.0':(2,[]),'10.1':(1,[]),
'10.2':(1,[L(P+'10.0',H,'Gorbachev as Soviet leader')]),
'10.3':(1,[L(P+'9.0',E,'SDI'),L(P+'10.2',E,'the Reykjavik meeting')]),
'10.4':(2,[]),
'10.5':(1,[L(P+'10.4',E,'the INF Treaty'),L(P+'4.b',H,'SALT limiting growth')]),
'10.6':(1,[L('hist-eur6-s2.6.2',H,'the Berlin Wall')]),
'11.b':(1,[]),
'11.0':(1,[L(P+'7.2',E,'the Soviet war in Afghanistan')]),
'11.1':(1,[L(P+'10.1',H,"Gorbachev's loosening of control")]),
'11.2':(1,[L('hist-eur6-s2.6.2',E,'the Berlin Wall built in 1961'),L(P+'11.1',H,'no Soviet intervention')]),
'11.3':(1,[L(P+'10.0',H,'Gorbachev as leader')]),
'12.b':(1,[]),
'12.0':(2,[L(P+'4.0',E,'SALT I'),L(P+'5.0',H,'Helsinki Final Act'),L(P+'3.2',H,'opening to China'),L(P+'10.4',H,'INF Treaty'),L(P+'7.3',H,'SALT II not ratified')]),
'12.1':(2,[L(P+'9.0',E,'the Strategic Defense Initiative'),L(P+'8.1',H,'the Reagan defence build-up')]),
'12.2':(2,[L(P+'10.1',H,"Gorbachev's reforms")]),
'12.3':(1,[L(P+'10.2',H,'Reagan-Gorbachev talks')]),
'12.4':(1,[L(P+'10.4',E,'the INF Treaty')]),
'12.5':(1,[L(P+'11.0',H,'Soviet war in Afghanistan')]),
'12.6':(1,[L(P+'2.4',H,'the Vietnam syndrome'),L(P+'0.1',H,'internationalism')]),
}
def mk(path,full):
    txt=open(B+'packs/'+path).read()
    sec=txt.split('CANDIDATES')
    tgt=re.findall(r'^\[(hist-eur6-s5\.[^\]]+)\]',sec[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    return tgt,allids
def out(pk,o,full,extra=None):
    tgt,allids=mk(pk+'.txt',full)
    res={}
    for t in tgt:
        k=t[len(P):]
        c,l=full[k] if k in full else extra[k]
        for x in l: assert x['id'] in allids and x['id']!=t,(t,x)
        res[t]={"cost":c,"needs":l} if o=='c' else {"needs":l}
    assert set(res)==set(tgt)==set(P+k for k in full),set(full)^set(k[len(P):] for k in tgt)
    return res
# fix 0.3 oddity
d['0.3']=(2,[L('hist-eur6-s2.14.1',H,'Vietnamisation handing war to South')])
r=out('hist-eur6-s5.t1g1','c',d)
json.dump(r,open(B+'point-links/hist-eur6-s5.t1g1.json','w'),ensure_ascii=False,indent=1)
s3=lambda i:'hist-eur6-s3.'+i
e={k:(0,[]) for k in d}
e['0.3']=(0,[L(s3('4.b'),H,"Johnson's escalation"),L(s3('10.b'),H,'the Tet Offensive'),L(s3('7.b'),H,'the anti-war movement')])
e['1.4']=(0,[L(s3('3.3'),E,'Gulf of Tonkin Resolution')])
r2=out('hist-eur6-s5.t1g2','l',e)
json.dump(r2,open(B+'point-links/hist-eur6-s5.t1g2.json','w'),ensure_ascii=False,indent=1)
for n,x in(('g1',r),('g2',r2)):
    print(n,len(x),sum(len(v['needs']) for v in x.values()),sum(v.get('cost')==2 for v in x.values()),sum(l['confidence']=='low' for v in x.values() for l in v['needs']))
