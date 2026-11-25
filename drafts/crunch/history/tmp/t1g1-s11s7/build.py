import json,re,sys
base='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
S={'e':'essential','h':'helpful'};C={'H':'high','L':'low'}
def L(i,s,w,c): return {"id":i,"strength":S[s],"why":w,"confidence":C[c]}
a11='hist-eur3-s11.';a3='hist-eur3-s3.';a9='hist-eur3-s9.';a2='hist-eur3-s2.'
d11={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(2,[L(a2+'3.4','h','Mein Kampf written in prison','H')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L(a11+'1.2','e','the Nuremberg Laws','H')]),
'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[]),'2.0':(2,[]),
'2.1':(2,[L(a11+'2.0','e','the Kristallnacht pogrom','H')]),
'2.2':(1,[L(a11+'2.1','h','arrests followed the pogrom','L'),L(a3+'1.8','h','Dachau and the camps','H')]),
'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L(a9+'0.1','h','the invasion of Poland','H')]),
'3.1':(2,[]),
'3.2':(1,[L(a11+'3.1','e','the ghettos','H')]),
'3.3':(1,[L(a9+'2.0','h','the invasion of the Soviet Union','H')]),
'3.4':(1,[L(a11+'3.3','h','Einsatzgruppen mass shootings','H')]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(2,[L(a11+'3.3','h','the Einsatzgruppen','H')]),
'4.1':(1,[L(a3+'1.7','h','Reinhard Heydrich','H')]),
'4.2':(2,[L(a11+'4.1','e','the Wannsee Conference','H')]),
'4.3':(2,[]),
'4.4':(2,[L(a11+'4.3','h','the extermination camps','H')]),
'4.5':(2,[L(a11+'4.0','h','the decision for genocide','H')]),
'5.b':(1,[]),
'5.0':(1,[L(a11+'3.1','e','the Warsaw ghetto','H')]),
'5.1':(1,[L(a11+'4.3','h','Treblinka and Sobibor camps','H')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),'5.7':(1,[]),'5.8':(1,[]),
'6.b':(1,[]),
'6.0':(1,[L(a11+'8.0','h','Auschwitz-Birkenau','H')]),
'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L(a11+'6.2','h','the Nuremberg trials','H')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,[L(a11+'7.0','h','Nazi eugenic policy','L')]),
'7.2':(1,[]),'7.3':(1,[]),'7.4':(2,[]),
'8.b':(1,[]),'8.0':(2,[]),
'8.1':(1,[L(a11+'4.3','h','Operation Reinhard camps','H')]),
'8.2':(1,[L(a11+'8.0','h','Auschwitz as destination','H')]),
'8.3':(1,[L(a11+'3.1','h','the ghettos','H')]),
'8.4':(1,[L(a9+'5.4','h','Soviet advance in 1944-45','L')]),
'8.5':(2,[]),
'8.6':(1,[L(a11+'8.0','h','bombing Auschwitz','H')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(1,[L(a11+'4.0','h','decision for systematic murder','H')]),
'9.2':(2,[L(a11+'2.3','e','the Evian Conference','H'),L(a11+'8.6','h','Allied knowledge of the killings','H')]),
'9.3':(1,[L(a11+'6.2','e','the Nuremberg trials','H'),L(a11+'5.6','h','rescuers','L')]),
'9.4':(1,[]),
'9.5':(1,[L(a11+'4.5','h','debate on intentions','L')]),
}
b7='hist-eur3-s7.'
d7={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(b7+'1.0','e','return to the gold standard','H')]),
'1.2':(1,[]),
'1.3':(1,[L(b7+'1.2','e','the miners lock-out','H')]),
'1.4':(1,[L(b7+'1.3','e','the General Strike','H')]),
'1.5':(1,[L(b7+'1.3','h','the General Strike','H')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L(b7+'2.0','h','coal as a staple industry','H')]),
'2.2':(1,[L(b7+'2.0','h','cotton as a staple industry','H')]),
'2.3':(1,[L(b7+'2.0','h','shipbuilding as a staple industry','H')]),
'2.4':(2,[L(b7+'2.0','h','the declining staple industries','L')]),
'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),
'3.2':(2,[L(b7+'3.1','e','the May Committee cuts','H'),L(b7+'3.0','h','the Labour government','H')]),
'3.3':(1,[L(b7+'1.0','e','the gold standard','H'),L(b7+'3.2','h','the 1931 crisis','H')]),
'3.4':(1,[L(b7+'3.2','e','the National Government','H')]),
'3.5':(1,[L(b7+'3.3','h','leaving gold days later','H'),L(b7+'3.1','h','the pay cuts','L')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(b7+'4.0','h','tariffs and trade policy','L')]),
'4.2':(1,[]),
'4.3':(1,[L(b7+'4.0','e','the tariffs','H')]),
'4.4':(1,[L(b7+'4.1','e','the Ottawa Agreements','H')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(2,[]),'5.2':(2,[]),
'5.3':(1,[L(b7+'5.2','e','the means test','H')]),
'5.4':(2,[L(b7+'5.2','e','the means test and the Board','H')]),
'5.5':(1,[L(b7+'5.2','h','the later means test system','H')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(b7+'6.0','e','the Special Areas Act','H')]),
'6.2':(2,[]),'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(b7+'6.0','h','regional policy','H'),L(b7+'6.4','h','new light industries','L')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(2,[]),'7.2':(1,[]),
'7.3':(2,[L(b7+'7.2','h','Keynes argued for public works','H')]),
'7.4':(1,[L(b7+'7.3','e','Keynes\'s deficit spending ideas','H')]),
'7.5':(2,[L(b7+'7.3','h','Keynes\'s policies','H')]),
'7.6':(1,[]),
'7.7':(2,[L(b7+'7.3','h','Keynes\'s economic ideas','L')]),
'7.8':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(b7+'1.3','h','the 1926 General Strike','H')]),
'8.2':(2,[]),'8.3':(2,[]),'8.4':(1,[]),'8.5':(1,[]),
'9.b':(1,[]),
'9.0':(1,[L(b7+'3.3','e','abandonment of gold','H'),L(b7+'4.2','e','cheap money policy','H')]),
'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[
 L(b7+'5.2','e','the means test','H'),L(b7+'6.0','e','the Special Areas policy','H')]),
'9.4':(1,[L(b7+'3.3','h','protecting the currency','L')]),
'9.5':(1,[L(b7+'4.2','h','monetary policy','L'),L(b7+'6.4','h','consumer demand in south-east','L')]),
}
for pk,pre,d in [('hist-eur3-s11.t1g1',a11,d11),('hist-eur3-s7.t1g1',b7,d7)]:
    txt=open(base+'packs/'+pk+'.txt').read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=re.findall(r'^\[(%s[^\]]+)\]'%re.escape(pre),txt,re.M)
    assert set(d)=={t[len(pre):] for t in tgt}, (set(d)^{t[len(pre):] for t in tgt})
    out={}
    for t in tgt:
        c,n=d[t[len(pre):]]
        for x in n: assert x['id'] in allids and x['id']!=t,(t,x)
        out[t]={"cost":c,"needs":n}
    json.dump(out,open(base+'point-links/'+pk+'.json','w'),indent=1)
    j=json.load(open(base+'point-links/'+pk+'.json'))
    links=[x for v in j.values() for x in v['needs']]
    print(pk,len(j),len(links),sum(v['cost']==2 for v in j.values()),sum(x['confidence']=='low' for x in links))
