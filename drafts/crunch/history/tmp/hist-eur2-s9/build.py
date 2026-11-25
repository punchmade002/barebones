import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def run(pkg,out,prefix,spec):
    txt=open(B+'packs/'+pkg).read()
    tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    for l in txt.split('\n'):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[([^\]]+)\]',l)
        if m: tgt.append(m.group(1))
    res={}
    for t in tgt:
        k=t[len(prefix)+1:]
        assert k in spec,t
        c,n=spec[k]; res[t]={"cost":c,"needs":[L(prefix+'-'+a if False else a,s,w,cf) for a,s,w,cf in n]}
    assert len(spec)==len(tgt),(len(spec),len(tgt))
    for t,v in res.items():
        for n in v['needs']: assert n['id'] in ids and n['id']!=t,(t,n)
    json.dump(res,open(B+'point-links/'+out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(out,len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))

P='hist-eur2-s9.'
def l(i,s,w,c='high'): return (i,s,w,c)
sp={}
def a(k,c,*n): sp[k]=(c,list(n))
for k in ['4.b','5.b','7.b','0.b','0.0','0.2','0.3','1.b','1.0','1.1','1.2','1.3','2.b','2.0','2.1','2.2','2.3','2.5','2.6','3.b','3.0','3.1','3.2','3.3','3.4','4.2','4.3','5.1','5.2','5.3','5.4','5.5','5.6','6.b','6.0','6.1','6.2','6.3','6.4','7.0','7.1','8.b','9.b','9.0','9.1','9.2','9.3','9.4','10.b','10.0','10.2','10.4','10.6','11.b','11.0','11.1','11.3','11.4','11.5','12.b','12.0','13.b','13.0','13.3','14.b','14.3','14.4','14.5','15.b','15.0','15.3','15.4','16.b','17.b','17.0','17.1']: a(k,1)
a('0.1',2,l('hist-eur2-s5.5.0',H,'war of attrition'))
a('0.4',1,l(P+'0.3',E,'Military Service Act'))
a('1.4',1,l('hist-eur2-s5.5.2',H,'shell shortage 1915'))
a('1.5',1,l(P+'1.3',H,'Ministry of Munitions'))
a('2.4',2,l('hist-eur2-s5.16.2',H,'submarine campaign cut supplies'))
a('3.5',1,l(P+'2.5',H,'Corn Production Act'))
a('4.0',1,l('hist-eur2-s5.15.0',H,'British blockade of Germany'))
a('4.1',1,l(P+'4.0',H,'blockade shortages'))
a('5.0',2); a('5.1',1)
a('7.2',1,l(P+'7.0',E,'WSPU suffragettes'),l(P+'7.1',E,'NUWSS suffragists'))
a('8.0',1,l(P+'0.3',H,'conscription'))
a('8.1',1,l(P+'1.4',E,'Shell Crisis'))
a('8.2',1); a('8.3',1,l(P+'8.2',E,'dilution')); a('8.4',1,l(P+'8.2',H,'dilution'))
a('9.0',1); a('9.5',1,l(P+'9.0',H,'munitionettes'))
a('10.1',1,l(P+'1.3',H,'Ministry of Munitions'))
a('10.3',1)
a('10.5',1,l(P+'2.1',E,'Auxiliary Service Law'))
a('11.2',1,l('hist-eur2-s5.16.2',H,'submarine campaign made food priority'))
a('11.6',1,l(P+'11.5',H,'women\'s auxiliary corps'))
a('12.1',1,l(P+'8.2',E,'dilution')); a('12.2',1,l(P+'8.3',E,'dilution for the war only'))
a('13.0',1,l(P+'7.0',E,'WSPU militant campaign'))
a('13.1',1,l(P+'7.0',H,'WSPU'))
a('13.2',1,l(P+'7.0',H,'Pankhursts and WSPU'))
a('13.4',1,l(P+'7.1',H,'women\'s suffrage campaign','low'))
a('14.0',2,l(P+'7.b',H,'women barred from voting'))
a('14.1',1,l(P+'14.0',H,'1918 vote'))
a('14.2',1,l(P+'14.0',E,'1918 Act limits'))
a('15.1',1,l(P+'8.3',E,'Treasury Agreement promise to unions'))
a('15.2',1,l(P+'9.0',H,'munitions work'))
a('16.0',2,l(P+'9.0',H,'munitions work'),l(P+'14.0',H,'the vote'))
a('16.1',2,l(P+'14.0',H,'over-30 vote'))
a('16.2',1); a('16.3',1); a('16.4',1,l(P+'14.0',H,'the vote')); a('16.5',1,l(P+'14.5',H,'French vote 1944'),l(P+'14.0',H,'British vote'))
a('17.2',1,l(P+'3.1',E,'Britain debtor to USA'))
run('hist-eur2-s9.t1g1.txt','hist-eur2-s9.t1g1.json','hist-eur2-s9',sp)
