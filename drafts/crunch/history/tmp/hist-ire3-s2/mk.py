import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,Hh='essential','helpful'
def run(pack,out,pre,epre,data):
    ids=[];allids=set();mode=None
    for l in open(H+'packs/'+pack):
        if l.startswith('TARGET'):mode='t'
        elif l.startswith('CANDIDATES'):mode='c'
        m=re.match(r'\[(\S+?)\]',l)
        if m:
            allids.add(m.group(1))
            if mode=='t':ids.append(m.group(1))
    full=[pre+'.'+k for k,_,_ in data]
    assert full==ids,(set(ids)-set(full),set(full)-set(ids))
    res={};nl=n2=nlow=0
    for k,c,links in data:
        needs=[]
        for t,s,w,cf in links:
            i=(epre+t[1:]) if t[0]=='x' else pre+'.'+t
            assert i in allids and i!=pre+'.'+k,i
            needs.append({"id":i,"strength":s,"why":w,"confidence":cf})
            nl+=1;nlow+=cf=='low'
        n2+=c==2
        res[pre+'.'+k]={"cost":c,"needs":needs}
    json.dump(res,open(H+out,'w'),indent=1,ensure_ascii=False)
    json.load(open(H+out))
    print(pre,len(res),nl,n2,nlow)
h,l='high','low'
S=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[('xs1.6.3',Hh,'Joseph Plunkett executed in 1916',h)]),
('0.2',1,[('xs1.6.1',Hh,'internment of 1916 prisoners',l)]),
('0.3',1,[('xs1.5.2',Hh,'de Valera in 1916',l)]),
('0.4',1,[('xs1.5.7',Hh,'Ashe\u2019s role in 1916',h)]),
('0.5',1,[('0.0',Hh,'Griffith\u2019s Sinn F\u00e9in',h)]),
('0.6',1,[('0.5',Hh,'de Valera elected president',l)]),
('0.7',1,[('xs1.1.5',Hh,'the Irish Volunteers',h)]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',2,[('1.0',E,'the Military Service Act',h)]),
('1.2',1,[('1.1',Hh,'the anti-conscription campaign',h)]),
('1.3',2,[('1.0',Hh,'Britain\u2019s conscription crisis',h)]),
('1.4',1,[('1.3',E,'the German Plot arrests',h)]),
('1.5',2,[('1.3',E,'the German Plot arrests',h),('xs1.3.8',Hh,'Redmond\u2019s party losing influence',h)]),
('2.b',1,[]),
('2.0',1,[]),
('2.1',1,[]),
('2.2',2,[('xs1.0.0',Hh,'the Irish Parliamentary Party',h)]),
('2.3',1,[('2.2',Hh,'the 1918 result',h)]),
('2.4',1,[('2.2',Hh,'the 1918 result',h)]),
('2.5',1,[('xs1.2.0',Hh,'Ulster exclusion and partition',l)]),
('2.6',1,[('8.1',Hh,'Markievicz held in Holloway',h)]),
('2.7',1,[('0.3',Hh,'de Valera winning East Clare',l)]),
('3.b',1,[]),
('3.0',1,[('2.2',E,'the 1918 election of deputies',h)]),
('3.1',2,[('3.0',E,'the First D\u00e1il',h)]),
('3.2',1,[('3.0',Hh,'the D\u00e1il electing a head',h)]),
('3.3',2,[('3.2',E,'the D\u00e1il ministry',h)]),
('3.4',1,[('3.3',Hh,'Collins as Finance minister',h)]),
('3.5',1,[('3.0',Hh,'loyalty to the D\u00e1il',h)]),
('3.6',1,[('3.0',Hh,'the D\u00e1il',h)]),
('3.7',1,[('xs1.1.5',Hh,'the Volunteers',h)]),
('3.8',1,[('3.0',E,'the First D\u00e1il',h)]),
('4.b',1,[]),
('4.0',2,[('3.0',Hh,'the D\u00e1il',h)]),
('4.1',1,[('4.0',Hh,'start of the IRA campaign',l)]),
('4.2',2,[('4.1',Hh,'attacks on RIC barracks',h)]),
('4.3',1,[]),
('4.4',1,[('4.3',Hh,'Collins\u2019s intelligence network',h)]),
('4.5',2,[]),
('4.6',1,[]),
('4.7',2,[('4.4',E,'the Squad',h)]),
('4.8',2,[('4.7',E,'Bloody Sunday killings',h),('5.1',Hh,'the Auxiliaries',h)]),
('4.9',2,[('5.1',E,'the Auxiliaries',h)]),
('4.10',1,[]),
('4.11',1,[]),
('5.b',1,[]),
('5.0',1,[('4.1',Hh,'RIC withdrawal and attacks',l)]),
('5.1',1,[('5.0',Hh,'the Black and Tans',l)]),
('5.2',1,[]),
('5.3',2,[('5.0',Hh,'the Black and Tans',h)]),
('5.4',1,[('5.3',Hh,'the reprisals',h)]),
('5.5',2,[('xs1.9.5',Hh,'partition in 1920',l)]),
('5.6',2,[('5.5',E,'the Northern parliament',h)]),
('5.7',1,[('5.6',Hh,'talks following the invitation',h)]),
('5.8',2,[('5.3',Hh,'reprisals damaging Britain',h)]),
('5.9',1,[('7.4',Hh,'de Valera in America',h)]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[('xs1.5.0',Hh,'the GPO in 1916',h),('xs1.6.1',Hh,'Frongoch internment',h)]),
('6.2',1,[('0.4',E,'Ashe\u2019s funeral',h)]),
('6.3',2,[('3.4',E,'the D\u00e1il Loan',h),('4.4',E,'the Squad',h),('4.3',Hh,'Director of Intelligence',h)]),
('6.4',1,[('6.3',Hh,'Collins\u2019s wartime role',h)]),
('6.5',1,[]),
('6.6',2,[('6.3',Hh,'Collins\u2019s wartime role',l)]),
('6.7',2,[('6.3',Hh,'Collins\u2019s wartime role',h)]),
('7.b',1,[]),
('7.0',1,[]),
('7.1',1,[('xs1.5.2',Hh,'Boland\u2019s Mill garrison',h)]),
('7.2',1,[('0.3',E,'winning East Clare',h)]),
('7.3',1,[('1.3',E,'the German Plot arrest',h),('3.2',E,'the Lincoln escape and D\u00e1il head',h)]),
('7.4',1,[('5.9',E,'the American mission',h)]),
('7.5',1,[('5.6',E,'Lloyd George\u2019s invitation',h)]),
('7.6',2,[]),
('7.7',1,[]),
('8.b',1,[]),
('8.0',1,[('xs1.8.4',Hh,'her release at the 1917 amnesty',h)]),
('8.1',1,[('1.3',E,'the German Plot',h),('2.6',Hh,'her 1918 election',h)]),
('8.2',1,[('3.3',Hh,'the D\u00e1il ministry',h)]),
('8.3',1,[('5.7',E,'the Truce',h)]),
('8.4',1,[('8.2',Hh,'her ministerial role',h)]),
('8.5',1,[]),
('8.6',1,[]),
('8.7',1,[]),
('9.b',1,[]),
('9.0',1,[('2.2',E,'the 1918 result',h)]),
('9.1',2,[('5.8',Hh,'why Britain went to talks',h)]),
('9.2',1,[]),
('9.3',2,[('2.2',Hh,'the 1918 result',h)]),
('9.4',2,[('3.0',Hh,'the D\u00e1il',l)]),
('9.5',2,[]),
('9.6',1,[('3.0',E,'the D\u00e1il',h),('3.7',Hh,'the IRA',h)]),
]
run('hist-ire3-s2.t1g1.txt','point-links/hist-ire3-s2.t1g1.json','hist-ire3-s2','hist-ire3-',S)
