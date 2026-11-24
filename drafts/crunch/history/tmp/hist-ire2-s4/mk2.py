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
# x = candidate prefix applied; e.g. 'xs3.6.3' -> epre + 's3.6.3'
S4=[
('0.b',1,[]),
('0.0',1,[('xs2.4.0',E,'the Plan of Campaign',h)]),
('0.1',1,[('xs3.6.3',Hh,'the Liberal alliance',h)]),
('0.2',1,[('xs3.7.4',Hh,'Times forged letters aimed at Parnell',l)]),
('0.3',1,[('0.2',E,'the forged letter in The Times',h)]),
('0.4',1,[('0.2',Hh,'the charges from The Times',h)]),
('0.5',2,[('0.3',E,'Pigott as forger of the letters',h)]),
('0.6',1,[('0.5',Hh,'Pigott collapse vindicating Parnell',h)]),
('0.7',1,[('0.4',E,'the Special Commission',h)]),
('1.b',1,[]),
('1.0',1,[('xs3.7.2',Hh,'O’Shea as former Irish Party MP',l)]),
('1.1',1,[('1.0',E,'the O’Shea divorce suit',h)]),
('1.2',1,[('1.1',Hh,'the divorce case outcome',h)]),
('1.3',1,[('1.2',Hh,'Gladstone’s letter to Morley',h)]),
('1.4',1,[('xs3.0.6',Hh,'bishops’ role in nationalist politics',l)]),
('1.5',1,[('1.3',Hh,'Gladstone’s ultimatum on Parnell',l)]),
('1.6',2,[('1.3',Hh,'Gladstone’s demand that Parnell go',h)]),
('1.7',2,[('1.6',E,'the split in Committee Room 15',h)]),
('1.8',1,[('1.7',Hh,'the anti-Parnellite split',h)]),
('1.9',1,[('1.0',Hh,'Katharine O’Shea and the divorce',h)]),
('2.b',1,[]),
('2.0',1,[('xs3.2.0',Hh,'the 85 MPs of 1885',h)]),
('2.1',2,[('0.3',E,'the Pigott affair',h),('1.0',E,'the O’Shea affair',h)]),
('2.2',2,[('1.4',Hh,'bishops against Parnell',h),('1.7',E,'Parnellites vs anti-Parnellites',h)]),
('2.3',1,[('0.5',E,'the Pigott collapse',h)]),
('2.4',2,[]),
('2.5',2,[('xs2.2.3',Hh,'violence in the Land War',l)]),
('2.6',2,[]),
('2.7',1,[]),
('3.b',1,[]),
('3.0',1,[('xs3.3.3',Hh,'the First Home Rule Bill',h)]),
('3.1',1,[('xs3.3.5',Hh,'Irish MPs excluded from Westminster',h)]),
('3.2',1,[('3.0',Hh,'the Second Home Rule Bill',h)]),
('3.3',1,[('3.2',Hh,'the Commons passing the Bill',h)]),
('3.4',1,[('xs3.5.3',Hh,'Ulster unionist organisation',l)]),
('3.5',1,[('xs2.5.b',E,'killing Home Rule with kindness',h)]),
('3.6',2,[('1.7',E,'Parnellite and anti-Parnellite factions',h)]),
('3.7',1,[('xs2.1.b',Hh,'the land agitation',l)]),
('3.8',1,[('3.6',E,'the feuding factions reuniting',h)]),
('4.b',1,[]),
('4.0',1,[('xs2.6.0',E,'the Land Conference',h),('xs2.6.1',E,'the Wyndham Act',h)]),
('4.1',1,[]),
('4.2',1,[('xs3.6.5',Hh,'Liberals needing a majority',l)]),
('4.3',2,[('4.2',Hh,'Liberal dependence on Irish votes',h)]),
('4.4',2,[('4.3',E,'the Parliament Act’s two-year delay',h)]),
('4.5',1,[('4.4',E,'the Third Home Rule Act',h)]),
('4.6',1,[('4.4',Hh,'the Third Home Rule Bill',h)]),
('4.7',1,[('7.3',E,'the Irish Volunteers',h)]),
('5.b',1,[]),
('5.0',1,[]),
('5.1',1,[('1.7',Hh,'the Parnellite group',h)]),
('5.2',2,[('4.0',E,'the Land Conference',h),('4.3',E,'the 1911 Parliament Act',h),('4.4',E,'the 1912 Bill',h)]),
('5.3',2,[('6.b',Hh,'Griffith’s separatist alternative',h),('7.1',Hh,'the IRB',h)]),
('5.4',2,[('7.3',E,'the Irish Volunteers',h)]),
('5.5',1,[('5.4',E,'the Volunteers split',h)]),
('5.6',2,[('5.2',Hh,'Redmond’s achievements',h)]),
('5.7',2,[('4.6',E,'acceptance of Ulster opt-out',h)]),
('5.8',2,[('5.4',Hh,'war wrecking Redmond’s leadership',l)]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[('6.0',Hh,'Griffith’s early movement',l)]),
('6.2',2,[]),
('6.3',2,[('6.2',E,'the Hungarian model',h)]),
('6.4',2,[('6.1',E,'Cumann na nGaedheal',h),('6.3',Hh,'the Sinn Féin policy',h)]),
('6.5',1,[('6.3',E,'the Sinn Féin policy',h)]),
('6.6',1,[('6.3',E,'abstention and self-reliance',h)]),
('7.b',1,[]),
('7.0',1,[]),
('7.1',1,[('7.0',E,'Tom Clarke',h),('6.4',Hh,'Bulmer Hobson',l)]),
('7.2',1,[]),
('7.3',1,[('7.2',E,'MacNeill’s article',h),('7.1',Hh,'IRB influence',h)]),
('7.4',1,[('7.3',E,'the Irish Volunteers',h)]),
('7.5',2,[('7.3',E,'the Irish Volunteers',h)]),
('7.6',1,[('5.4',E,'the Woodenbridge speech',h),('7.3',Hh,'the Irish Volunteers',h)]),
('8.b',1,[]),
('8.0',1,[('4.4',Hh,'the Home Rule Act',h),('4.0',Hh,'land reform',h)]),
('8.1',2,[('3.3',E,'the Lords killing the 1893 Bill',h),('1.6',Hh,'Parnell’s fall',h)]),
('8.2',1,[('6.3',Hh,'Sinn Féin policy',h),('7.1',Hh,'the IRB',h)]),
('8.3',2,[('5.3',Hh,'Redmond’s standing',l)]),
('8.4',1,[('5.4',Hh,'war and Volunteer split',h)]),
]
run('packs/hist-ire2-s4.t1g1.txt','point-links/hist-ire2-s4.t1g1.json','hist-ire2-s4','hist-ire2-',[(k,c,l_) for k,c,l_ in S4])
