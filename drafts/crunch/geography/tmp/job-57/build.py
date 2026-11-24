import json,re
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-option-culture-identity-s6.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful'
S5='geo-option-culture-identity-s5.';S4='geo-option-culture-identity-s4.';S1='geo-option-culture-identity-s1.';R3='geo-region-european-s3.'
jobs={
't2g4':{
 '35.b':[L(S5+'1.1','helpful','new nation states from empires',"low")],
 '36.0':[L(S5+'0.0',H,'state recognition by other states','low')],
 '36.1':[L(S5+'0.0',H,'state recognition by other states','low')],
 '36.2':[L(S5+'10.2',H,'power-sharing between groups')],
 '37.b':[L(S5+'5.3',H,'boundaries softening via Schengen')],
 '37.0':[L(S5+'5.3',H,'Schengen removes passport checks')],
 '38.0':[L(S5+'9.1',H,'boundaries placing groups in wrong state')],
 '38.1':[L(S5+'10.2',H,'power-sharing between groups')],
 '38.2':[L(S5+'5.3',H,'boundaries softening via Schengen','low')],
 '41.b':[L(S5+'10.1',H,'devolution defined')],
 '41.1':[L(S5+'12.1',H,'devolution 1999 created Senedd')],
 '53.b':[L(S5+'10.0',H,'federalism and autonomy')],
 '53.1':[L(S5+'10.0',H,'federalism and autonomy')],
 '61.1':[L(S5+'10.1',H,'devolution')],
},
't2g5':{
 '32.2':[L(S4+'31.0',H,'Eurovision as national expression')],
 '33.0':[L(S1+'12.1',H,'guest workers settling')],
 '33.1':[L(S1+'19.0',H,'source area loses young adults')],
 '33.b':[L(S1+'19.0',H,'source area loses young adults','low')],
 '34.1':[L(S1+'13.0',H,'refugee defined')],
 '34.b':[L(S1+'13.0',H,'refugee defined')],
 '44.0':[L(S4+'30.4',H,'National Eisteddfod of Wales')],
 '49.2':[L(S4+'30.3',H,'fest-noz on UNESCO list')],
 '49.4':[L(S4+'30.2',H,'Festival Interceltique de Lorient')],
 '51.0':[L(S4+'30.2',H,'Festival Interceltique de Lorient')],
 '56.2':[L(S1+'12.2',H,'labour agreements with Morocco, Turkey')],
 '58.0':[L(S4+'3.1',H,'UNESCO intangible heritage list')],
 '59.b':[L(S1+'12.3',H,'labour migrants to Belgium')],
 '59.2':[L(S1+'12.2',H,'labour agreements with Morocco, Turkey')],
 '46.b':[L(S1+'18.0',H,'migrants change destination culture','low')],
},
't2g6':{
 '37.0':[L(R3+'12.1',H,'Croatia joined the euro 2023')],
 '37.1':[L(R3+'18.0',H,'EU candidate countries')],
 '41.b':[L(R3+'10.1',H,'devolution defined')],
 '52.2':[L(R3+'7.4',H,'French long the language of government')],
 '53.b':[L(R3+'8.5',H,"Belgium's federal solution")],
 '53.1':[L(R3+'7.1',H,'Flanders, Wallonia, Brussels regions')],
 '54.b':[L(R3+'7.1',H,'language groups and regions')],
 '54.0':[L(R3+'7.1',H,'regional populations')],
 '54.1':[L(R3+'7.3',H,'Dutch and French speaker shares')],
 '54.2':[L(R3+'7.1',H,'Brussels officially bilingual')],
 '55.b':[L(R3+'8.2',H,'no nationwide parties')],
 '55.0':[L(R3+'8.1',H,'Leuven university split 1968')],
 '55.1':[L(R3+'8.2',H,'no nationwide parties')],
 '55.2':[L(R3+'8.3',H,'541 days without government')],
 '55.3':[L(R3+'8.4',H,'N-VA and De Wever')],
 '59.3':[L(R3+'8.6',H,'Brussels hosts EU and NATO')],
 '60.b':[L(R3+'8.0',H,'Wallonia decline, Flanders growth')],
 '60.0':[L(R3+'8.0',H,'Wallonia coal and steel decline')],
 '60.1':[L(R3+'8.0',H,'Flanders growth via Antwerp')],
 '60.2':[L(R3+'8.0',H,'economic reversal of wealth')],
 '61.1':[L(R3+'8.5',H,'federal solution and devolution','low')],
}}
for k,links in jobs.items():
    txt=open(G+'packs/geo-option-culture-identity-s6.%s.txt'%k).read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tids=[i for i in re.findall(r'^\[(geo-option-culture-identity-s6\.[^\]]+)\]',txt,re.M)]
    out={}
    for t in tids:
        key=t[len(P):]
        out[t]={"needs":links.get(key,[])}
    for key,ls in links.items():
        assert P+key in out,key
        for l in ls: assert l['id'] in pk,(k,l['id'])
    json.dump(out,open(G+'point-links/geo-option-culture-identity-s6.%s.json'%k,'w'),ensure_ascii=False)
    d=json.load(open(G+'point-links/geo-option-culture-identity-s6.%s.json'%k))
    n=sum(len(v['needs']) for v in d.values()); lo=sum(l['confidence']=='low' for v in d.values() for l in v['needs'])
    print(k,len(d),len(tids),n,lo)
