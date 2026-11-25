import json,re
P='hist-eur1-s9.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
# id: (cost, links)
g1={
'0.b':(1,[L('hist-eur1-s7.0.0',H,'industrialisation and the factory shift')]),
'0.0':(1,[]),
'0.1':(1,[L(P+'0.0',H,'early water-powered mills')]),
'0.2':(1,[]),
'0.3':(1,[L(P+'0.2',E,'uses laissez-faire')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[L(P+'1.1',H,'his Manchester mill work')]),
'1.3':(2,[L(P+'1.2',H,'Manchester experience shaping his belief')]),
'1.4':(1,[L(P+'1.3',H,'character formed by surroundings')]),
'1.5':(1,[L(P+'2.2',H,'David Dale as mill owner')]),
'1.6':(1,[L(P+'1.5',H,'link to Dale and New Lanark')]),
'2.b':(1,[]),
'2.0':(1,[L('hist-eur1-s7.7.2',H,'Arkwright, cotton spinning pioneer','low')]),
'2.1':(1,[L(P+'2.0',H,'the New Lanark site and Dale')]),
'2.2':(1,[L(P+'0.1',H,'pauper apprentices')]),
'2.3':(1,[L(P+'2.2',H,'pauper children housed by Dale')]),
'2.4':(2,[L(P+'2.0',E,'Dale, Arkwright and the founding'),L('hist-eur1-s7.7.2',H,'the water frame','low')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[L(P+'0.0',H,'discipline by fines and beatings')]),
'3.4':(1,[L(P+'1.3',E,'character formed by environment')]),
'3.5':(1,[L('hist-eur1-s7.13.0',H,'the factory system','low')]),
'4.b':(1,[]),
'4.0':(2,[L(P+'0.1',E,'pauper apprentices')]),
'4.1':(1,[L(P+'3.0',H,'thirteen-hour working day')]),
'4.2':(1,[]),
'4.3':(1,[L(P+'7.0',H,'schools funded','low')]),
'5.b':(1,[]),
'5.0':(1,[L(P+'3.3',H,'earlier punishment-based discipline')]),
'5.1':(2,[]),
'5.2':(1,[L(P+'5.1',E,'uses the silent monitor')]),
'5.3':(1,[L(P+'5.1',E,'uses the silent monitor')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'3.1',H,'dirty overcrowded village housing')]),
'6.1':(1,[]),
'6.2':(1,[L(P+'3.2',H,'drunkenness found by Owen')]),
'6.3':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,[L(P+'7.0',H,'infant school housed in Institute')]),
'7.2':(1,[L(P+'7.1',E,'the infant school')]),
'7.3':(1,[]),
'7.4':(2,[L(P+'8.2',H,'William Allen as partner')]),
'7.5':(1,[L(P+'7.1',E,'the infant school')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(P+'4.3',H,'spending profits on schools')]),
'8.2':(2,[L(P+'8.1',H,'1813 sale and new partners')]),
'8.3':(1,[L(P+'8.2',H,'William Allen and partners')]),
'8.4':(1,[L(P+'8.3',E,'partners objecting to his methods')]),
'9.b':(1,[]),
'9.0':(2,[L(P+'1.3',H,'character formed by circumstances')]),
'9.1':(2,[L(P+'0.1',H,'pauper apprentices')]),
'9.2':(1,[L(P+'9.1',H,'the elder Peel')]),
'9.3':(1,[L(P+'9.2',H,'campaign and Peel committee')]),
'9.4':(1,[L(P+'9.3',E,'the 1819 Act')]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(1,[L(P+'10.0',E,'villages of co-operation')]),
'10.2':(1,[]),
'11.b':(1,[]),
'11.0':(1,[L(P+'10.0',H,'co-operative communities plan')]),
'11.1':(1,[L(P+'11.0',E,'New Harmony')]),
'11.2':(1,[L(P+'10.0',H,'Owenite co-operative communities')]),
'11.3':(1,[]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),
'12.2':(1,[L(P+'12.1',E,'the GNCTU')]),
'12.3':(1,[]),'12.4':(1,[]),'12.5':(2,[]),
'13.b':(1,[]),'13.0':(1,[]),
'13.1':(1,[L(P+'0.2',E,'laissez-faire belief')]),
'13.2':(1,[L(P+'8.2',H,'unusual partners')]),
'13.3':(1,[L(P+'0.1',H,'water mills needed housing')]),
'13.4':(2,[L(P+'10.2',H,'attack on religion'),L(P+'11.1',H,'New Harmony failure')]),
'13.5':(2,[]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[L(P+'10.1',H,'Cobbett and the villages')]),
'14.2':(2,[]),
'14.3':(1,[L(P+'5.1',H,'the silent monitor')]),
'14.4':(1,[]),
'15.b':(1,[]),
'15.0':(2,[L(P+'4.0',H,'no young child labour')]),
'15.1':(1,[L(P+'8.4',H,'partners curbed him')]),
'15.2':(2,[L(P+'9.3',H,'the 1819 Act')]),
'15.3':(2,[L(P+'9.4',H,'weak 1819 Act'),L(P+'11.1',H,'New Harmony failure')]),
'15.4':(2,[]),'15.5':(2,[]),'15.6':(2,[]),'15.7':(2,[]),
}
def L8(i,w,c='high'): return L('hist-eur1-s8.'+i,H,w,c)
g2={k:[] for k in g1}
g2['12.b']=[L8('4.0','socialism as common ownership')]
g2['12.2']=[L8('1.3','the Tolpuddle case')]
g2['12.5']=[L8('8.0','class struggle in Marx')]
g2['15.6']=[L8('21.b','Peel as reforming statesman')]
out1={P+k:{"cost":c,"needs":n} for k,(c,n) in g1.items()}
out2={P+k:{"needs":n} for k,n in g2.items()}
json.dump(out1,open('point-links/hist-eur1-s9.t1g1.json','w'),indent=1)
json.dump(out2,open('point-links/hist-eur1-s9.t1g2.json','w'),indent=1)
# check
for n,o in (('t1g1',out1),('t1g2',out2)):
    txt=open(f'packs/hist-eur1-s9.{n}.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[l for l in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
    assert list(o)==tg,(n,set(tg)^set(o))
    links=[x for v in o.values() for x in v['needs']]
    assert all(x['id'] in ids for x in links)
    assert all(k!=x['id'] for k,v in o.items() for x in v['needs'])
    print(n,len(o),len(links),sum(v.get('cost')==2 for v in o.values()),sum(x['confidence']=='low' for x in links))
