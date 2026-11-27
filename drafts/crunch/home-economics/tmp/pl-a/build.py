import json,re,os
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
P={}
# (id): (cost, [links])
P['hom-home-services-s7.t1g1']={
'hom-home-services-s7.0.b':(1,[]),
'hom-home-services-s7.0.0':(1,[]),
'hom-home-services-s7.0.1':(2,[]),
'hom-home-services-s7.0.2':(1,[]),
'hom-home-services-s7.0.3':(1,[L('hom-home-services-s7.5.0',H,'uses condensation process')]),
'hom-home-services-s7.0.4':(2,[]),
'hom-home-services-s7.0.5':(1,[]),
'hom-home-services-s7.0.6':(1,[]),
'hom-home-services-s7.1.b':(1,[]),
'hom-home-services-s7.1.0':(1,[]),
'hom-home-services-s7.1.1':(2,[L('hom-home-services-s7.5.0',H,'uses how condensation forms')]),
'hom-home-services-s7.1.2':(1,[]),
'hom-home-services-s7.1.3':(1,[]),
'hom-home-services-s7.1.4':(1,[]),
'hom-home-services-s7.1.5':(1,[]),
'hom-home-services-s7.1.6':(1,[L('hom-home-services-s7.0.0',H,'combustion needs air supply')]),
'hom-home-services-s7.2.b':(1,[]),
'hom-home-services-s7.2.0':(1,[L('hom-home-services-s5.0.1',H,'uses convection currents')]),
'hom-home-services-s7.2.1':(1,[]),
'hom-home-services-s7.2.2':(1,[]),
'hom-home-services-s7.2.3':(1,[L('hom-home-services-s7.2.0',H,'hot gases rise by convection')]),
'hom-home-services-s7.3.b':(1,[]),
'hom-home-services-s7.3.0':(1,[L('hom-home-services-s7.2.0',H,'uses convection principle'),L('hom-home-services-s7.2.2',H,'uses cross-ventilation')]),
'hom-home-services-s7.3.1':(1,[L('hom-home-services-s7.2.0',H,'high and low openings convection')]),
'hom-home-services-s7.3.2':(1,[]),
'hom-home-services-s7.3.3':(1,[L('hom-home-services-s7.2.3',H,'uses flue and rising hot gases')]),
'hom-home-services-s7.3.4':(1,[]),
'hom-home-services-s7.3.5':(1,[L('hom-home-services-s7.2.0',H,'shows convection air movement')]),
'hom-home-services-s7.4.b':(1,[]),
'hom-home-services-s7.4.0':(2,[L('hom-home-services-s7.2.1',H,'uses suction principle')]),
'hom-home-services-s7.4.1':(2,[]),
'hom-home-services-s7.4.2':(2,[]),
'hom-home-services-s7.4.3':(1,[]),
'hom-home-services-s7.4.4':(2,[]),
'hom-home-services-s7.4.5':(1,[]),
'hom-home-services-s7.4.6':(1,[L('hom-home-services-s7.2.1',H,'cites suction principle')]),
'hom-home-services-s7.4.7':(1,[L('hom-home-services-s7.4.0',H,'draws extractor fan'),L('hom-home-services-s7.4.2',H,'draws ducted cooker hood')]),
'hom-home-services-s7.5.b':(1,[]),
'hom-home-services-s7.5.0':(1,[]),
'hom-home-services-s7.5.1':(1,[]),
'hom-home-services-s7.5.2':(2,[]),
'hom-home-services-s7.5.3':(1,[L('hom-home-services-s7.5.1',H,'targets everyday moisture sources'),L('hom-home-services-s7.3.2',H,'uses trickle vents','low')]),
'hom-home-services-s7.5.4':(1,[L('hom-home-services-s7.5.1',H,'targets drying clothes moisture')]),
'hom-home-services-s7.5.5':(1,[L('hom-home-services-s6.3.1',H,'double glazing keeps surfaces warm','low')]),
'hom-home-services-s7.6.b':(1,[]),
'hom-home-services-s7.6.0':(1,[L('hom-home-services-s7.1.1',H,'signs of condensation and damp','low')]),
'hom-home-services-s7.6.1':(1,[L('hom-home-services-s7.3.1',H,'air bricks and vents')]),
'hom-home-services-s7.6.2':(2,[L('hom-home-services-s7.4.2',H,'cooker hood'),L('hom-home-services-s7.3.2',H,'trickle vents')]),
}
c='hom-clothing-selection-s2.'
S='hom-sociological-concepts-s'; R='hom-consumer-rights-s'
P['hom-clothing-selection-s2.t1g1']={
c+'0.b':(1,[]),c+'0.0':(1,[]),c+'0.1':(1,[]),
c+'0.2':(1,[L(R+'1.0.0',H,'uses household income limit','low')]),
c+'0.3':(1,[]),c+'0.4':(1,[]),c+'0.5':(1,[]),
c+'1.b':(1,[L(S+'1.1.0',H,'uses culture as way of life')]),
c+'1.0':(2,[L(S+'1.1.0',H,'culture shapes dress and customs')]),
c+'1.1':(1,[]),
c+'1.2':(1,[L(R+'1.1.3',H,'other people influence choice','low')]),
c+'1.3':(1,[]),c+'1.4':(1,[]),
c+'2.b':(1,[]),
c+'2.0':(1,[L(R+'1.3.0',H,'advertising popularises products')]),
c+'2.1':(1,[L(R+'1.3.3',H,'celebrity endorsement influence','low')]),
c+'2.2':(2,[L(c+'2.1',H,'admired people copied')]),
c+'2.3':(1,[]),
c+'2.4':(1,[]),
c+'2.5':(1,[]),
c+'3.b':(1,[]),
c+'3.0':(1,[L(S+'1.3.4',H,'uses conformity')]),
c+'3.1':(1,[]),
c+'4.b':(1,[]),
c+'4.0':(1,[L(R+'1.0.1',H,'spare money after essentials','low')]),
c+'4.1':(1,[L(R+'1.0.2',H,'trading down to cheaper goods','low')]),
c+'4.2':(1,[]),
c+'5.b':(1,[]),c+'5.0':(1,[]),c+'5.1':(1,[]),c+'5.2':(1,[]),
c+'5.3':(1,[L(c+'2.0',H,'media spreads styles','low')]),
}
# fix: clothing ids (0..5) numbering above for s2 targets
P['hom-clothing-selection-s2.t1g1'][c+'2.5']=(1,[L(c+'2.2',E,'uses trendsetters'),L(c+'2.4',E,'uses fashion definition')])
f='hom-personal-finance-s4.'; B='hom-personal-finance-s'; Q='hom-personal-finance-s'
t={}
for i,cs in {'0.b':1,'0.0':1,'0.1':1,'0.2':1,'0.3':1,'0.4':1,'0.5':1,'0.6':1,'0.7':2,
 '1.b':1,'1.0':1,'1.1':1,'1.2':1,'2.b':1,'2.0':1,'2.1':1,'2.2':1,'2.3':1,'2.4':1,
 '3.b':1,'3.0':1,'3.1':1,'3.2':1,'3.3':1,'3.4':1,'3.5':1,'4.b':1,'4.0':1,'4.1':1,'4.2':1,'4.3':1,'4.4':1,
 '5.b':1,'5.0':2,'5.1':1,'5.2':1,'6.b':1,'6.0':1,'6.1':1,'6.2':1,
 '7.b':1,'7.0':2,'7.1':1,'7.2':2,'7.3':1,'7.4':2,'7.5':2,'7.6':1,
 '8.b':1,'8.0':1,'8.1':1,'8.2':1,'8.3':1,'8.4':1}.items(): t[f+i]=(cs,[])
def A(i,*l): t[f+i]=(t[f+i][0],list(l))
A('0.3',L(B+'3.5.3',H,'uses interest charged on credit'))
A('0.2',L(B+'3.5.0',H,'credit lets purchases be spread','low'))
A('1.0',L(f+'2.1',H,'demand deposit gives easy access','low'))
A('2.2',L(f+'2.1',H,'compares with demand deposit'))
A('2.3',L(f+'2.2',H,'compares fixed term with notice','low'))
A('3.4',L(f+'7.5',H,'uses DIRT tax exemption'))
A('3.2',L(f+'2.3',H,'uses fixed-term deposit idea','low'))
A('4.2',L(f+'3.0',H,'dividend vs interest','low'))
A('4.4',L(f+'6.0',H,'Deposit Guarantee Scheme'))
A('4.3',L(B+'3.2.5',H,'credit union loan','low'))
A('5.1',L(f+'0.1',H,'emergency fund purpose'))
A('5.2',L(f+'5.0',E,'equity-linked products'))
A('6.1',L(f+'3.b',H,'State Savings backed by State'))
A('6.2',L(f+'5.0',H,'investment funds and shares'))
A('7.2',L(f+'7.1',E,'builds on interest rate'),L(f+'7.3',H,'compounding'))
A('7.3',L(f+'7.1',H,'interest earned'))
A('7.5',L(f+'3.4',H,'State Savings exempt from DIRT'))
A('7.0',L(f+'6.0',H,'deposit guarantee'))
A('7.6',L(Q+'2.0.0',H,'low-income household spending','low'))
A('7.4',L(f+'2.1',H,'instant, notice or fixed term access'))
A('8.0',L(f+'2.1',E,'demand deposit'),L(f+'4.0',H,'credit union share account'))
A('8.1',L(f+'2.2',E,'notice account'))
A('8.2',L(f+'2.3',E,'term deposit'))
A('8.3',L(f+'4.1',H,'credit union regular saving'),L(f+'2.4',H,'regular saver account'))
A('8.4',L(f+'1.0',H,'short-term needs easy access'),L(f+'1.1',H,'long-term accepts restricted access'))
P['hom-personal-finance-s4.t1g1']=t
for name,d in P.items():
    txt=open(D+'packs/'+name.replace('.t1g1','')+'.t1g1.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=re.search(r'TARGET (\S+):',txt).group(1)
    targets=[i for i in ids if i.startswith(tgt+'.')]
    # target section ends at first CANDIDATES
    first=txt.split('CANDIDATES')[0]
    targets=re.findall(r'^\[([^\]]+)\]',first,re.M)
    assert targets==list(d.keys()),(name,[x for x in targets if x not in d],[x for x in d if x not in targets])
    out={k:{"cost":v[0],"needs":v[1]} for k,v in d.items()}
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids,n['id']
    json.dump(out,open(D+'point-links/'+name.replace('.t1g1','')+'.t1g1.json','w'),indent=1)
    links=sum(len(v['needs']) for v in out.values())
    print(name,len(out),links,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
