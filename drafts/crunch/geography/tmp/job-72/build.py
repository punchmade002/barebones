import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s3.'
def L(i,s,w,c='high',pre=S): return {"id":pre+i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
# cost + links (package 1); explicit for every target
p1={
'22.0':(1,[]),'22.1':(1,[]),'22.2':(2,[]),'22.3':(1,[]),'22.4':(2,[]),
'22.5':(1,[L('22.3',H,'dependence on the potato')]),
'22.6':(1,[]),
'22.7':(1,[L('22.4',H,'emigration during the Famine')]),
'23.b':(1,[]),
'23.0':(2,[L('22.1',H,'rack-rents and eviction answered')]),
'23.1':(2,[L('23.0',H,'Land League and Land War','low')]),
'23.2':(2,[L('23.0',E,'the Three Fs')]),
'23.3':(2,[]),
'23.4':(1,[L('22.2',H,'tiny plots in the west','low')]),
'23.5':(1,[L('23.3',H,'tenants buying their holdings')]),
'23.6':(1,[L('0.2',H,'meaning of empowerment')]),
'24.b':(1,[]),'24.0':(1,[]),
'24.1':(1,[L('24.0',H,'landless families in Brazil')]),
'24.2':(2,[]),
'24.3':(1,[L('24.2',E,'the 1913 land pattern')]),
'24.4':(1,[]),'24.5':(1,[]),
'25.b':(1,[]),'25.0':(1,[]),
'25.1':(1,[L('25.0',E,'both land reforms')]),
'25.2':(2,[]),
'26.b':(1,[]),'26.0':(1,[]),'26.1':(2,[]),
'26.2':(1,[L('21.1',E,'land as collateral for credit')]),
'27.b':(1,[]),'27.0':(1,[]),
'28.b':(1,[]),
'28.0':(1,[L('28.b',H,'what a co-operative is')]),
'28.1':(1,[L('28.b',H,'what a co-operative is')]),
'28.2':(2,[L('28.b',H,'what a co-operative is')]),
'28.3':(1,[L('28.b',H,'co-operative idea','low')]),
'29.b':(1,[]),
'29.0':(1,[L('28.b',H,'what a co-operative is')]),
'29.1':(1,[L('28.b',H,'what a co-operative is')]),
'29.2':(1,[L('28.b',H,'what a co-operative is')]),
'29.3':(2,[L('28.b',H,'worker-owned co-operatives')]),
'30.b':(1,[]),
'30.0':(1,[L('28.b',H,'dairy co-operative')]),
'30.1':(1,[L('30.0',E,'the Amul model')]),
'30.2':(2,[L('28.b',H,'co-operative bank')]),
'31.b':(1,[]),'31.0':(1,[]),'31.1':(1,[]),
'32.b':(1,[]),'32.0':(1,[]),'32.1':(1,[]),'32.2':(1,[]),'32.3':(1,[]),'32.4':(1,[]),
'33.b':(1,[]),'33.0':(2,[]),
'33.1':(1,[L('33.0',E,'Local Enterprise Offices')]),
'33.2':(2,[]),
'33.3':(1,[L('31.0',H,'top-down decisions','low')]),
'34.b':(1,[]),
'34.0':(1,[L('31.1',H,'participation ladder','low')]),
'34.1':(1,[]),'34.2':(2,[]),
'34.3':(1,[L('34.2',E,'the Sardar Sarovar dam')]),
'35.b':(1,[]),'35.0':(1,[]),
'35.1':(1,[L('3.0',E,'structural adjustment programmes')]),
'35.2':(1,[]),
'36.b':(1,[]),'36.0':(1,[]),
'36.1':(1,[L('36.0',H,'meaning of exploitation')]),
'37.b':(1,[]),'37.0':(1,[]),'37.1':(1,[]),
'37.2':(1,[L('37.b',H,'supply and value chains')]),
'37.3':(1,[]),'37.4':(1,[]),'37.5':(2,[]),'37.6':(1,[]),
'38.b':(1,[]),'38.0':(2,[]),'38.1':(1,[]),
'39.b':(1,[]),
'39.0':(1,[L('22.1',E,'rack-rents and eviction')]),
'39.1':(2,[]),'39.2':(1,[]),'39.3':(1,[]),'39.4':(1,[]),
'40.b':(1,[]),'40.0':(1,[]),'40.1':(1,[]),
'40.2':(1,[L('0.0',H,'GDP definition')]),
'41.b':(1,[]),'41.0':(1,[]),
'41.1':(1,[L('28.b',H,'co-operatives')]),
'41.2':(1,[]),
'41.3':(1,[L('37.0',H,'Rana Plaza garment disaster','low')]),
'41.4':(1,[L('37.b',H,'supply chains')]),
'41.5':(1,[]),
'42.b':(1,[]),'42.0':(1,[]),
'42.1':(1,[L('42.0',E,'meaning of gender roles')]),
'43.b':(1,[L('0.0',H,'GDP definition')]),
'43.0':(1,[]),'43.1':(1,[]),
'44.b':(1,[]),'44.0':(1,[]),
'44.1':(1,[L('21.1',E,'land as collateral')]),
'44.2':(1,[]),'44.3':(1,[]),'44.4':(1,[]),
'45.b':(1,[L('0.3',H,'empowerment links growth to development')]),
'45.0':(1,[]),'45.1':(1,[]),
'45.2':(1,[L('0.0',H,'GDP definition','low')]),
'45.3':(1,[L('25.2',H,'Kerala human development')]),
'46.b':(1,[]),'46.0':(2,[]),
'46.1':(1,[L('46.0',E,'Grameen Bank and Yunus')]),
'46.2':(2,[L('46.0',E,'what microfinance is')]),
'46.3':(1,[L('30.2',H,'SEWA')]),
'46.4':(1,[]),'46.5':(1,[]),
'46.6':(1,[L('37.0',H,'Rana Plaza')]),
'47.b':(1,[]),'47.0':(1,[]),'47.1':(2,[]),'47.2':(1,[]),'47.3':(1,[]),
}
s1='geo-option-global-interdependence-s1.1.'; e1='geo-economic-development-s1.'
s4='geo-economic-development-s4.'; e3='geo-economic-development-s3.'
p2={ # links only; others empty
'24.4':[L('1.0',H,'colonial era land and rule','low',s1)],
'25.2':[L('0.1',H,'meaning of human development','high',s1)],
'31.0':[L('16.0',H,'bottom-up development','high',s1)],
'32.0':[L('27.5',H,'local knowledge dismissed','low',s1)],
'34.2':[L('8.0',H,'prestige dam projects','low',s1)],
'37.2':[L('11.1',H,'cocoa exported unprocessed','low',s1)],
'37.6':[L('10.3',H,'profit repatriation','high',s1)],
'40.2':[L('4.1',H,'unpaid work excluded from output','high',e1)],
'43.b':[L('4.1',H,'unpaid work excluded from output','high',e1)],
}
p3={
'24.b':[L('0.b',H,'colonialism','high',e3)],
'27.0':[L('20.0',H,'land grabbing','high',s4)],
'37.1':[L('17.0',H,'multinationals seek cheap labour','low',s4)],
'37.2':[L('3.2',H,'value chain share of price','high',s4)],
'41.0':[L('21.2',H,'trade unions campaign for workers','low',s4)],
'41.1':[L('6.b',H,'what fair trade is','high',s4)],
'41.2':[L('21.0',H,'ethical consumer campaigns','high',s4)],
'41.3':[L('18.3',H,'the Bangladesh Accord','high',s4)],
}
ids=[]
for l in open(P+'packs/geo-option-global-interdependence-s3.t2g1.txt').read().split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[(geo-option-global-interdependence-s3\.(\d+\.\w+))\]',l)
    if m and int(m.group(2).split('.')[0])>=22: ids.append(m.group(2))
print([i for i in ids if i not in p1],[k for k in p1 if k not in ids])
for i in ids: assert i in p1,i
def pk(name):
    t=open(P+'packs/'+name+'.txt').read()
    return set(re.findall(r'^\[([^\]]+)\]',t,re.M)), set(re.findall(r'TARGET [^\n]*\n((?:\[[^\n]*\n)+)',t) and re.findall(r'^\[([^\]]+)\]',t.split('CANDIDATES')[0],re.M))
outs={
 'geo-option-global-interdependence-s3.t2g1':{S+i:{"cost":p1[i][0],"needs":p1[i][1]} for i in ids},
 'geo-option-global-interdependence-s3.t2g2':{S+i:{"needs":p2.get(i,[])} for i in ids},
 'geo-option-global-interdependence-s3.t2g3':{S+i:{"needs":p3.get(i,[])} for i in ids},
}
for n,d in outs.items():
    allids,tg=pk(n)
    assert set(d)==tg and len(d)==len(tg)
    links=0;low=0;c2=0
    for k,v in d.items():
        for x in v['needs']:
            assert x['id'] in allids and x['id']!=k,(n,k,x['id']); links+=1; low+=x['confidence']=='low'
        c2+=v.get('cost')==2
    json.dump(d,open(P+'point-links/'+n+'.json','w'),indent=1,ensure_ascii=False)
    print(n,len(d),links,c2,low)
