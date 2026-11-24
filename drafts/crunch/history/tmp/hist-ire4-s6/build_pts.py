import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,Hl='essential','helpful'
def run(pkg,pre,data):
    txt=open(H+'packs/'+pkg+'.txt').read()
    tg=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={};links=0;c2=0;low=0
    for k in tids:
        assert k in data,k
    assert set(data)==set(tids),set(data)^set(tids)
    for k in tids:
        cost,needs=data[k]
        ns=[]
        for t,s,w,c in needs:
            t=t if t.startswith('hist-') else pre+'.'+t
            assert t in allids and t!=k,(k,t)
            ns.append({"id":t,"strength":s,"why":w,"confidence":c})
            links+=1;low+=c=='low'
        c2+=cost==2
        out[k]={"cost":cost,"needs":ns}
    json.dump(out,open(H+'point-links/'+pkg+'.json','w'),indent=1)
    json.load(open(H+'point-links/'+pkg+'.json'))
    print(pkg,len(tids),links,c2,low)
p='hist-ire4-s6'
d={
'0.b':(1,[]),
'0.0':(1,[('hist-ire4-s2.0.1',Hl,'US took most emigrants','low')]),
'0.1':(2,[('0.0',Hl,'Irish dominance of hierarchy','high')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[]),'0.6':(2,[]),'0.7':(1,[]),
'1.0':(1,[('hist-ire4-s2.2.4',Hl,'Irish settlement in British cities','high')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(2,[]),'1.4':(1,[]),
'1.5':(1,[('0.5',Hl,'Christian Brothers, Sisters of Mercy','high')]),
'1.6':(1,[]),
'1.7':(1,[('hist-ire4-s3.2.b',Hl,'sectarian suspicion of the Irish','low')]),
'2.0':(1,[('hist-ire4-s2.2.7',Hl,'Irish emigration to Canada','low')]),
'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[('6.2',Hl,'Orange influence in Ontario','high')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[('3.0',Hl,'Mannix background','high')]),
'3.2':(2,[]),'3.3':(1,[('3.2',E,'conscription campaign','high')]),
'3.4':(1,[]),'3.5':(2,[('3.4',Hl,'Mannix and Irish independence','low')]),
'3.6':(1,[('6.6.6',Hl,'Orange Order in Australia','high')]),
'3.7':(2,[]),'3.8':(1,[('3.3',Hl,'accusations of disloyalty','high')]),
'3.9':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[('hist-ire4-s2.2.0',Hl,'Irish settlement in US cities','low')]),
'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[('5.0',Hl,'Ulster Presbyterian settlers','high')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[('6.0',Hl,'Orange Order origins','high')]),
'6.2':(1,[]),'6.3':(2,[]),'6.4':(1,[]),
'6.5':(1,[('6.0',Hl,'Orange Order origins','low')]),
'6.6':(1,[]),'6.7':(2,[]),
'7.b':(1,[]),'7.0':(1,[('0.7',Hl,'parish as social centre','high')]),
'7.1':(1,[]),'7.2':(1,[('0.4',Hl,'parish schools','low')]),'7.3':(1,[]),
'7.4':(1,[('6.b',Hl,'Orange rivalry in Canada, Australia','high')]),
'7.5':(1,[]),
'8.0':(1,[('0.7',Hl,'church community role','low')]),
'8.1':(1,[('hist-ire4-s2.7.5',Hl,'assimilation of second generation','high')]),
'8.2':(2,[('hist-ire4-s3.0.b',Hl,'nativist hostility to Irish','low')]),
'8.3':(2,[]),
'8.4':(2,[('5.b',Hl,'Ulster Protestant loyalism','high')]),
}
d={p+'.s6.'+k if False else p+'.'+k:v for k,v in d.items()}
# ids in package: 'hist-ire4-s6.X'; short keys expand relative to p
def fix(d,p,fixer):pass
d2={}
for k,(c,n) in d.items(): d2[k]=(c,n)
# expand short link targets: those not starting with hist- get prefix in run()
run(p+'.t1g1',p,d2)
q='hist-eur6-s10'
e={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(2,[('hist-eur6-s9.0.3',Hl,'Brown v Board decision','high')]),
'0.4':(2,[]),'0.5':(1,[('0.4',E,'Colvin arrest as test case','high')]),
'0.6':(1,[]),'0.7':(1,[('hist-eur6-s9.0.3',Hl,'Brown prompted resistance','high')]),
'1.b':(1,[]),
'1.0':(2,[('0.0',Hl,'bus segregation rules','high')]),
'1.1':(1,[]),'1.2':(2,[('1.0',E,"Parks's arrest",'high')]),
'1.3':(1,[('1.0',E,"Parks's arrest",'high')]),
'1.4':(1,[('0.3',E,'WPC and Jo Ann Robinson','high')]),
'1.5':(1,[('1.4',E,'leaflets calling for boycott','high')]),
'1.6':(1,[('1.5',Hl,'announcement of the boycott','high')]),
'1.7':(2,[('1.6',Hl,'Holt Street meeting','low')]),
'1.8':(1,[('1.7',E,'the original modest demands','high')]),
'2.b':(1,[]),'2.0':(2,[('1.6',Hl,'Holt Street meeting decision','low')]),
'2.1':(1,[('2.0',E,'King as MIA president','high')]),
'2.2':(1,[('1.2',Hl,'E. D. Nixon','low')]),
'2.3':(1,[]),'2.4':(1,[('2.3',Hl,'car pool','high')]),
'2.5':(1,[]),'2.6':(1,[('2.3',Hl,'car pool kept boycott going','low')]),
'2.7':(1,[('2.0',Hl,"King's leadership of MIA",'high')]),
'2.8':(1,[('3.2',Hl,'threats after bombing','low')]),
'3.b':(1,[]),'3.0':(1,[('2.3',E,'car pool','high')]),
'3.1':(1,[('2.0',Hl,'King as MIA leader','high')]),
'3.2':(1,[]),
'3.3':(2,[('3.1',Hl,"King's arrest",'low')]),
'3.4':(1,[('3.3',E,'indictments of leaders','high')]),
'3.5':(2,[('0.4',Hl,'Colvin and Smith arrests','high')]),
'3.6':(1,[('3.5',E,'Browder v Gayle case','high')]),
'3.7':(2,[('3.5',E,'Browder v Gayle case','high')]),
'3.8':(1,[('3.7',E,'federal court ruling','high'),('hist-eur6-s9.0.3',Hl,'Brown v Board','high')]),
'3.9':(2,[('3.8',E,'Supreme Court ruling','high'),('2.3',Hl,'car pools','high')]),
'3.10':(1,[('3.8',E,'Supreme Court order','high')]),
'4.b':(1,[]),'4.0':(1,[('3.10',E,'end of boycott','high')]),
'4.1':(1,[('4.0',Hl,'desegregation of buses','high')]),
'4.2':(2,[('4.0',Hl,'desegregated buses','high')]),
'4.3':(1,[('4.2',E,'the bombings','high')]),
'4.4':(1,[('2.0',Hl,"King's role in MIA",'high'),('hist-eur6-s9.3.2',Hl,'SCLC','low')]),
'4.5':(1,[]),'4.6':(1,[('1.0',Hl,"Parks's arrest",'high')]),
'5.b':(1,[]),'5.0':(1,[('4.2',Hl,'bombing of Graetz home','low')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[('hist-eur6-s9.0.4',Hl,'Southern Manifesto','high')]),
'5.5':(1,[('3.0',Hl,'arrests and harassment','low')]),
'6.b':(1,[]),'6.0':(1,[('2.0',Hl,'King elected MIA president','high')]),
'6.1':(1,[('2.7',Hl,'Rustin and Smiley advice','high')]),
'6.2':(1,[('3.2',Hl,'bombing of his home','high'),('3.3',Hl,'his conviction','high'),('3.1',Hl,'his arrest','high')]),
'6.3':(1,[]),'6.4':(1,[]),
'6.5':(2,[('6.0',Hl,"King's role in boycott",'low')]),
'7.b':(1,[]),
'7.0':(1,[('6.1',Hl,"King's non-violence",'high')]),
'7.1':(1,[('2.6',Hl,'economic pressure of boycott','high')]),
'7.2':(1,[('4.4',E,'SCLC formation','high')]),
'7.3':(2,[('1.4',Hl,'WPC leaflets','high')]),
'7.4':(2,[('1.1',Hl,"Parks's activist background",'high')]),
'7.5':(2,[('3.7',E,'Browder v Gayle ruling','high'),('hist-eur6-s9.0.3',Hl,'Brown v Board','high')]),
'7.6':(1,[]),
'8.0':(2,[('3.10',Hl,'end of boycott','low')]),
'8.1':(2,[('4.4',Hl,'SCLC formation','high'),('hist-eur6-s9.1.3',Hl,'Birmingham campaign','high'),('hist-eur6-s9.2.7',Hl,'Selma campaign','high')]),
'8.2':(1,[('4.5',Hl,'segregation remaining','low')]),
'8.3':(2,[('4.2',Hl,'violence after victory','high')]),
'8.4':(2,[]),'8.5':(2,[]),
}
run(q+'.t1g1',q,e)
