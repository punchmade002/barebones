import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def build(pack,out,spec):
    txt=open(H+'packs/'+pack).read()
    tgt=[];allids=set();sec=None
    for l in txt.splitlines():
        if l.startswith('TARGET'): sec='t'
        elif l.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[(\S+)\] ',l)
        if m:
            allids.add(m[1])
            if sec=='t': tgt.append(m[1])
    res={}
    for k,(cost,needs) in spec.items():
        res[k]={"cost":cost,"needs":[{"id":i,"strength":s,"why":w,"confidence":c} for i,s,w,c in needs]}
    assert list(res)==tgt,(set(tgt)^set(res))
    for v in res.values():
        for n in v['needs']: assert n['id'] in allids and n['id']
    json.dump(res,open(H+'point-links/'+out,'w'),ensure_ascii=False,indent=1)
    L=sum(len(v['needs']) for v in res.values())
    print(out,len(res),L,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
P='hist-ire2-s6.'
def s(i,c,needs=()): return (P+i,(c,[(a if '-' in a else a,b,w,cf) for a,b,w,cf in needs]))
E='essential';Hh='helpful'
spec=dict([
s('0.b',1),s('0.0',2),s('0.1',1),s('0.2',1),s('0.3',1),s('0.4',1),s('0.5',2),
s('0.6',1,[('hist-ire2-s5.0.b',Hh,'unionism as a political camp','low')]),
s('0.7',1),
s('0.8',1,[(P+'0.2',Hh,'Dublin society she led','high')]),
s('1.b',1),s('1.0',1),
s('1.1',2,[(P+'0.0',Hh,'Married Women’s Property Acts','high'),(P+'6.0',Hh,'Intermediate Education Act','high')]),
s('1.2',1),s('1.3',1),
s('1.4',1,[('hist-ire2-s5.0.3',Hh,'Gladstone’s Home Rule conversion, Liberal Unionists','low')]),
s('1.5',1,[('hist-ire2-s5.0.b',Hh,'unionism','low')]),
s('1.6',1,[(P+'0.1',Hh,'first Ulster suffrage society','high')]),
s('2.b',1,[('hist-ire2-s4.5.b',Hh,'the Irish Party under Redmond','low')]),
s('2.0',1),
s('2.1',1,[(P+'3.0',Hh,'League’s founding and aims','high')]),
s('2.2',1,[('hist-ire2-s4.5.b',Hh,'Irish Party','low')]),
s('2.3',1,[('hist-ire2-s4.4.4',Hh,'Third Home Rule Bill','high')]),
s('2.4',1,[('hist-ire2-s4.4.4',E,'Third Home Rule Bill','high')]),
s('2.5',1,[(P+'4.b',Hh,'Sheehy-Skeffington as militant','high')]),
s('3.b',1),s('3.0',2),
s('3.1',1,[(P+'3.0',Hh,'the Irish Women’s Franchise League','high')]),
s('3.2',1,[(P+'3.0',Hh,'League members','high')]),
s('3.3',2,[('hist-ire2-s4.4.4',Hh,'Asquith and Home Rule Bill','low')]),
s('3.4',1),
s('3.5',1,[(P+'3.4',Hh,'hunger strikes by suffragettes','high')]),
s('3.6',1),s('4.b',1),s('4.0',1),s('4.1',1),
s('4.2',1,[(P+'3.0',Hh,'founding the Franchise League','high')]),
s('4.3',2,[('hist-ire2-s4.7.4',Hh,'Cumann na mBan','high'),('hist-ire2-s4.5.b',Hh,'the Irish Party','low')]),
s('4.4',1),s('4.5',1),s('4.6',1),s('5.b',1),
s('5.0',1,[('hist-ire2-s5.4.5',E,'Ulster Day and the Covenant','high')]),
s('5.1',1,[('hist-ire2-s4.7.4',E,'Cumann na mBan','high'),('hist-ire2-s4.7.3',Hh,'the Volunteers','high')]),
s('5.2',1),
s('5.3',1,[(P+'3.1',Hh,'the Irish Citizen','high')]),
s('5.4',1),s('6.b',1),s('6.0',2),s('6.1',1),s('6.2',1),s('6.3',1),s('6.4',2),
s('6.5',2,[(P+'6.1',E,'payment by results','high')]),
s('6.6',1),
s('6.7',1,[(P+'1.2',Hh,'Margaret Byers and the Ladies’ Collegiate School','high')]),
s('7.b',1),s('7.0',1),
s('7.1',1,[(P+'7.0',E,'the Royal University','high'),(P+'4.0',Hh,'Sheehy-Skeffington','high')]),
s('7.2',1),
s('7.3',2,[(P+'7.0',E,'the Royal University','high')]),
s('7.4',1,[(P+'7.3',E,'the National University of Ireland','high')]),
s('7.5',1,[(P+'7.4',Hh,'the NUI Senate','high')]),
s('8.b',1),
s('8.0',2,[(P+'0.4',Hh,'local government votes','low')]),
s('8.1',1,[(P+'2.4',Hh,'Home Rule Bills and suffrage','low')]),
s('8.2',1,[(P+'6.0',Hh,'Intermediate system','high'),(P+'7.3',Hh,'1908 Act','high')]),
s('8.3',1,[(P+'6.1',E,'payment by results','high'),(P+'7.3',Hh,'1908 Act','high')]),
s('8.4',1,[(P+'2.3',Hh,'Irish Party view of suffrage','high')]),
s('8.5',2,[(P+'6.5.b'.replace('6.5.b','5.b'),Hh,'nationalism and unionism entanglement','high')]),
])
build('hist-ire2-s6.t1g1.txt','hist-ire2-s6.t1g1.json',spec)

Q='hist-ire6-s9.'
def t(i,c,needs=()): return (Q+i,(c,list(needs)))
spec2=dict([
t('0.b',1),t('0.0',1),t('0.1',1,[(Q+'0.0',Hh,'Irish as national language','high')]),
t('0.2',2),t('0.3',1),t('0.4',1),
t('0.5',1,[(Q+'0.1',Hh,'compulsory Irish','high')]),
t('0.6',2,[(Q+'0.1',E,'compulsory Irish in school and civil service','high')]),
t('1.0',1),t('1.1',1,[(Q+'1.0',Hh,'campaign for Irish radio','high')]),t('1.2',1),t('1.3',1),
t('1.4',1,[(Q+'0.0',Hh,'Irish’s symbolic official status','low')]),
t('2.b',1),t('2.0',1),t('2.1',1),t('2.2',1),t('2.3',1),t('2.4',1),t('2.5',1),t('2.6',1),
t('3.0',1),
t('3.1',1,[(Q+'0.2',Hh,'Mise Éire film','high')]),
t('3.2',2,[(Q+'4.b',E,'Vatican II changes','high'),(Q+'3.1',Hh,'Ó Riada’s music','high')]),
t('3.3',2),t('3.4',1),
t('4.b',1),t('4.0',1),t('4.1',1),t('4.2',1),t('4.3',2),t('4.4',1),t('4.5',1),t('4.6',1),
t('5.b',1,[(Q+'4.b',Hh,'Vatican II','high')]),
t('5.0',1,[(Q+'4.0',Hh,'attending the council','high')]),
t('5.1',1,[(Q+'4.3',Hh,'ecumenism','high')]),
t('5.2',1,[('hist-ire6-s1.2.b',E,'the Mother and Child dispute','high')]),
t('5.3',1),t('5.4',1),t('5.5',1),
t('5.6',2,[('hist-ire6-s1.2.b',Hh,'Mother and Child affair','low')]),
t('6.0',1),t('6.1',1),t('6.2',1),t('6.3',1),t('6.4',1),t('6.5',2),
t('7.0',1),
t('7.1',1,[(Q+'7.0',E,'censorship of books','high'),(Q+'5.b',Hh,'Archbishop of Dublin','high')]),
t('7.2',2,[(Q+'7.0',E,'the 1929 and 1946 bans','high')]),
t('7.3',1),
t('7.4',1,[(Q+'7.0',Hh,'censorship of publications','low')]),
t('7.5',1),
t('8.0',1),t('8.1',1),t('8.2',1),t('8.3',1),
t('8.4',1,[(Q+'8.2',Hh,'RTÉ’s broadcasting monopoly','high')]),
t('8.5',1),t('8.6',1),
t('9.0',2,[(Q+'4.b',Hh,'Vatican II reforms','low')]),
t('9.1',2,[(Q+'5.b',Hh,'McQuaid’s caution','high')]),
t('9.2',1),t('9.3',2),
])
build('hist-ire6-s9.t1g1.txt','hist-ire6-s9.t1g1.json',spec2)
