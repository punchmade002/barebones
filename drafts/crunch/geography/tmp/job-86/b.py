import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-population-migration-s5.'
def full(i):
    return i if i.startswith('geo-') else S+i
def L(i,s,w,c='high'): return (i,s,w,c)
H,E='helpful','essential'
# id: (cost, [links])
d1={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L('0.0',H,'ethnic groups'),L('0.1',H,'races')]),
'0.3':(1,[L('0.0',E,'uses ethnic group')]),
'1.b':(1,[]),
'1.0':(1,[L('0.1',H,'race'),L('0.0',H,'ethnicity')]),
'1.1':(1,[L('0.2',H,'religion')]),
'1.2':(1,[L('geo-population-migration-s3.0.6',H,'chain migration')]),
'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[L('0.3',H,'multicultural society')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('0.1',H,'race and visible difference')]),
'2.2':(1,[L('0.2',H,'religion')]),
'2.3':(1,[L('1.2',E,'residential segregation')]),
'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'2.7':(1,[L('1.5',H,'multiculturalism','low')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(2,[]),
'3.5':(1,[L('2.2',H,'places of worship','low')]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('2.0',H,'competition for housing')]),
'4.1':(2,[L('2.5',H,'anti-immigration politics','low')]),
'4.2':(1,[L('geo-population-migration-s4.6.b',H,'asylum accommodation system','low')]),
'4.3':(1,[L('1.0',E,'racism')]),
'5.b':(1,[]),
'5.0':(2,[L('1.0',H,'discrimination')]),
'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[L('1.4',H,'integration')]),
'5.4':(1,[]),
'5.5':(1,[L('4.3',H,'hate crime')]),
'5.6':(2,[L('3.6',E,'Catholic school patronage')]),
'5.7':(1,[L('0.0',H,'ethnic minority')]),
'6.b':(1,[]),
'6.0':(1,[L('5.0',H,'equality laws'),L('4.1',H,'2022-23 protests','low')]),
'6.1':(1,[L('geo-population-migration-s4.6.2',H,'criticisms of direct provision'),L('1.4',H,'integration','low')]),
'6.2':(1,[L('0.0',H,'ethnic minority')]),
'6.3':(1,[]),
'7.b':(1,[]),'7.0':(2,[]),'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[L('7.2',H,'laicite and secularism')]),
'7.4':(1,[L('7.2',H,'laicite and secularism')]),
'7.5':(1,[L('1.2',H,'segregation')]),
'8.b':(1,[]),
'8.0':(2,[L('7.5',E,'banlieues')]),
'8.1':(1,[L('7.5',H,'banlieue unrest')]),
'8.2':(1,[L('1.1',H,'Islamophobia')]),
'8.3':(2,[L('2.5',H,'far-right parties')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(1,[L('9.0',H,'guest workers')]),
'9.2':(1,[L('1.2',H,'segregation')]),
'9.3':(1,[L('9.2',H,'citizenship denied')]),
'9.4':(1,[L('9.3',H,'citizenship law')]),
'9.5':(1,[]),
'9.6':(1,[L('2.5',E,'political exploitation')]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(1,[L('1.0',H,'racism')]),
'10.2':(1,[L('10.1',H,'racial tension')]),
'10.3':(1,[L('1.0',H,'racial discrimination')]),
'10.4':(1,[L('10.0',E,'Windrush arrivals')]),
'11.b':(1,[]),'11.0':(2,[]),
'11.1':(2,[L('11.0',E,'Plantation origins')]),
'11.2':(1,[L('11.1',H,'the Troubles')]),
'11.3':(1,[]),
'11.4':(1,[L('geo-region-concept-s3.6.5',H,'peace walls and segregation')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(1,[]),'12.3':(1,[]),
'13.b':(1,[]),
'13.0':(1,[L('1.3',E,'assimilation')]),
'13.1':(1,[L('5.0',H,'equality law'),L('5.3',H,'integration strategy')]),
'13.2':(1,[L('9.2',H,'exclusion from citizenship'),L('9.3',H,'2000 reform'),L('9.4',H,'2024 reform')]),
}
d2={
'11.1':[L('geo-region-european-s3.2.0',H,'the Troubles')],
'11.2':[L('geo-region-european-s3.2.1',H,'Good Friday Agreement')],
'11.4':[L('geo-region-european-s3.1.3',H,'segregated schools and housing')],
'9.6':[L('geo-region-european-s3.17.0',H,'populism and euroscepticism','low')],
}
def build(pack,out,items,withcost):
    txt=open(P+'packs/'+pack+'.txt').read()
    tg=[]
    for l in txt.split('CANDIDATES')[0].splitlines():
        m=re.match(r'\[(\S+?)\]',l)
        if m: tg.append(m.group(1))
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    assert tg==[full(k) for k in items],set(tg)^set(full(k) for k in items)
    o={};n=0;lo=0;c2=0
    for k in items:
        links=items[k][1] if withcost else items[k]
        needs=[{'id':full(i),'strength':s,'why':w,'confidence':c} for i,s,w,c in links]
        for x in needs: assert x['id'] in allids and x['id']!=full(k),(k,x)
        n+=len(needs);lo+=sum(x['confidence']=='low' for x in needs)
        e={'needs':needs}
        if withcost: e={'cost':items[k][0],**e}; c2+=items[k][0]==2
        o[full(k)]=e
    json.dump(o,open(P+'point-links/'+out+'.json','w'),indent=1)
    print(out,len(o),n,c2,lo)
build('geo-population-migration-s5.t1g1','geo-population-migration-s5.t1g1',d1,True)
d2full={k:d2.get(k,[]) for k in d1}
build('geo-population-migration-s5.t1g2','geo-population-migration-s5.t1g2',d2full,False)
