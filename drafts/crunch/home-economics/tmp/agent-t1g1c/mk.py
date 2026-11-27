import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return (i,s,w,c)
H,E='helpful','essential'
D={}
# package 1
p='hom-environmental-issues-s1.'
D['hom-environmental-issues-s1']={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(2,[]),
'1.b':(1,[L('0.1',H,'renewable resources defined')]),
'1.0':(2,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'1.6':(2,[L('1.0',H,'uses solar thermal panels','low')]),
'1.7':(1,[L('1.b',H,'renewable meaning','low')]),
'2.b':(1,[]),
'2.0':(1,[L('0.0',H,'sustainable use meaning')]),
'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[L('1.0',H,'solar panels on roof','low')]),'2.4':(1,[]),
'2.5':(1,[L('1.0',H,'solar output varies')]),
'2.6':(1,[]),'2.7':(1,[]),
'3.b':(1,[]),'3.0':(2,[]),
'3.1':(1,[L('3.0',H,'peat as fossil fuel')]),
'3.2':(1,[]),'3.3':(2,[]),
'3.4':(1,[L('3.0',H,'fossil fuels')]),
'3.5':(2,[L('0.0',H,'sustainable use meaning','low')]),
'4.b':(1,[]),
'4.0':(1,[L('3.0',H,'burning fossil fuels')]),
'4.1':(1,[L('3.0',H,'coal, oil, peat fuels')]),
'4.2':(1,[]),
'4.3':(1,[L('3.1',H,'peat cut from bogs'),L('4.0',H,'carbon dioxide effect','low')]),
'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(1,[L('4.0',H,'fossil fuel burning harms')]),
'5.1':(2,[L('1.6',H,'heat pump renewable heat')]),
'5.2':(1,[]),
'5.3':(1,[L('3.3',H,'finite metals mined')]),
'5.4':(1,[]),
}
U={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[L('0.0',H,'basic needs standard')]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[L('1.0',H,'absolute poverty meaning')]),
'1.3':(1,[L('2.0',H,'relative poverty meaning')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(2,[L('2.1',H,'poverty line')]),
'2.3':(1,[L('2.1',H,'poverty line')]),'2.4':(1,[L('2.0',H,'relative poverty standard')]),
'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),'3.0':(1,[L('2.1',E,'poverty line at 60% median')]),
'3.1':(1,[L('2.4',H,'basic items in examples')]),
'3.2':(1,[L('3.1',E,'enforced deprivation')]),
'3.3':(2,[L('3.0',E,'below poverty line'),L('3.1',E,'enforced deprivation')]),
'3.4':(1,[L('3.3',E,'consistent poverty meaning'),L('3.0',H,'at-risk-of-poverty rate')]),
'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),'5.7':(2,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
}
U['0.1']=(1,[L('0.0',H,'acceptable standard of living')])
W={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[L('0.1',H,'child under 16 defined')]),
'1.1':(2,[L('0.1',H,'children defined')]),'1.2':(2,[L('1.3',H,'light work meaning')]),
'1.3':(1,[]),'1.4':(1,[L('0.1',H,'children defined','low')]),
'2.b':(1,[]),
'2.0':(1,[L('1.3',H,'light work meaning'),L('1.2',H,'14-15 holiday work')]),
'2.1':(1,[L('1.3',H,'light work meaning'),L('1.2',H,'15s work in term')]),
'2.2':(1,[L('1.2',H,'work experience allowed')]),
'2.3':(1,[]),'2.4':(1,[L('0.1',H,'young person is 16 or 17')]),
'3.b':(1,[]),'3.0':(1,[L('0.1',H,'children are under 16')]),
'3.1':(1,[L('0.1',H,'children are under 16','low')]),
'3.2':(1,[L('0.1',H,'young person is 16 or 17')]),
'3.3':(1,[L('0.1',H,'young person is 16 or 17','low')]),
'3.4':(1,[L('0.1',H,'young person is 16 or 17','low')]),
'4.b':(1,[]),'4.0':(1,[L('0.1',H,'children are under 16')]),
'4.1':(1,[L('0.1',H,'young person is 16 or 17')]),
'4.2':(1,[L('4.1',H,'night window for young persons')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[L('0.1',H,'child is under 16')]),
'5.2':(2,[]),'5.3':(1,[L('0.3',H,'WRC inspectors enforce')]),'5.4':(1,[L('0.3',H,'offence and prosecution')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[L('0.0',H,'hour, rest, night-work limits')]),
'7.b':(1,[]),'7.0':(2,[]),'7.1':(1,[]),'7.2':(2,[]),
'7.3':(1,[L('7.2',H,'Employment Equality Acts')]),
'7.4':(2,[]),'7.5':(2,[]),
'7.6':(1,[L('0.3',H,'WRC role','low')]),
}
# fix U strengths given as 'H' typo guard
def fix(d):
    return d
def build(sub,items,fn):
    txt=open(B+'packs/'+fn+'.txt').read()
    ids=re.findall(r'^\[(%s\.[^\]]+)\]'%re.escape(sub),txt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert [sub+'.'+k for k in items]==ids,(sub,set(ids)^set(sub+'.'+k for k in items))
    out={};nl=0;c2=0;lo=0
    for k,(c,ls) in items.items():
        n=[]
        for (i,s,w,cf) in ls:
            fi=i if i.startswith('hom-') else sub+'.'+i
            assert fi in allids and fi!=sub+'.'+k
            assert s in(H,E) and len(w.split())<=8
            n.append({'id':fi,'strength':s,'why':w,'confidence':cf}); lo+=cf=='low'
        nl+=len(n);c2+=c==2
        out[sub+'.'+k]={'cost':c,'needs':n}
    json.dump(out,open(B+'point-links/'+fn+'.json','w'),indent=1)
    print(fn,len(out),nl,c2,lo)
# normalise L tuples with 4 fields
def norm(d):
    for k,(c,ls) in d.items():
        d[k]=(c,[x if len(x)==4 else x for x in ls])
import os
os.makedirs(B+'point-links',exist_ok=True)
build('hom-environmental-issues-s1',D['hom-environmental-issues-s1'],'hom-environmental-issues-s1.t1g1')
build('hom-unemployment-poverty-s4',U,'hom-unemployment-poverty-s4.t1g1')
build('hom-work-leisure-s4',W,'hom-work-leisure-s4.t1g1')
