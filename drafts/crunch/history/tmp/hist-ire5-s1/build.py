import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":"hist-ire5-s1."+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),
"0.2":(1,[L("0.1",E,"responds to the Republic of Ireland Act")]),
"0.3":(1,[L("0.2",E,"the Ireland Act consent guarantee")]),
"0.4":(1,[]),"0.5":(2,[]),"0.6":(1,[]),
"0.7":(1,[L("0.1",H,"declaration of the Republic")]),
"0.8":(1,[]),
"1.b":(1,[]),"1.0":(1,[]),
"1.1":(2,[L("0.6",H,"the restricted local franchise")]),
"1.2":(1,[]),"1.3":(1,[]),"1.4":(1,[]),"1.5":(1,[]),"1.6":(1,[]),
"1.7":(1,[L("1.0",H,"Brooke succeeded by O'Neill")]),
"2.b":(1,[]),"2.0":(1,[]),"2.1":(1,[]),
"2.2":(1,[L("2.1",H,"grammar school tier of tripartite system")]),
"2.3":(2,[]),
"2.4":(1,[]),
"2.5":(2,[L("2.0",E,"uses free secondary education")]),
"2.6":(1,[]),
"3.b":(1,[]),"3.0":(1,[]),"3.1":(1,[]),
"3.2":(2,[L("3.1",H,"the Housing Trust")]),
"3.3":(2,[L("3.4",H,"explains gerrymandering")]),
"3.4":(1,[]),
"3.5":(1,[L("3.2",H,"council housing allocation")]),
"3.6":(1,[L("3.4",H,"unionist control by gerrymandering","low")]),
"4.b":(1,[]),"4.0":(1,[]),"4.1":(1,[]),
"4.2":(1,[L("4.0",E,"uses UK-wide benefits parity")]),
"4.3":(1,[L("4.2",E,"uses the principle of parity")]),
"4.4":(2,[L("4.2",E,"formalises the parity principle")]),
"4.5":(2,[L("4.2",H,"uses welfare parity")]),
"5.b":(1,[]),"5.0":(1,[]),"5.1":(1,[]),"5.2":(1,[]),
"5.3":(2,[]),
"5.4":(2,[L("5.3",H,"new industry grants and incentives")]),
"5.5":(1,[L("5.2",H,"links to high unemployment")]),
"5.6":(1,[]),
"6.b":(1,[]),"6.0":(1,[]),
"6.1":(1,[L("1.5",H,"introduces the Royal Ulster Constabulary")]),
"6.2":(1,[L("5.0",H,"the Belfast shipyards")]),
"6.3":(1,[]),"6.4":(1,[]),
"6.5":(2,[L("1.4",E,"introduces the B Specials"),L("1.5",H,"introduces the RUC")]),
"6.6":(1,[]),
"7.b":(1,[]),"7.0":(1,[]),
"7.1":(1,[L("7.0",H,"the Border Campaign")]),
"7.2":(1,[L("7.0",H,"response to the IRA campaign")]),
"7.3":(2,[L("7.0",E,"uses the start of the campaign")]),
"7.4":(1,[L("7.0",E,"ends the Border Campaign")]),
"7.5":(2,[L("7.4",E,"follows the campaign's failure")]),
"7.6":(1,[L("7.0",H,"the Border Campaign")]),
"8.b":(1,[]),"8.0":(1,[]),"8.1":(1,[]),"8.2":(1,[]),"8.3":(1,[]),"8.4":(1,[]),"8.5":(1,[]),
"9.0":(1,[L("2.0",H,"education reform"),L("3.0",H,"the NHS")]),
"9.1":(2,[L("7.0",H,"the IRA border campaign")]),
"9.2":(2,[L("6.b",H,"discrimination against Catholics"),L("3.2",H,"housing allocation")]),
"9.3":(2,[L("5.b",H,"economic decline and distribution")]),
"9.4":(2,[L("1.b",H,"Brooke's stability and loyalty")]),
"9.5":(2,[L("1.3",E,"uses the Special Powers Act")]),
"9.6":(2,[L("4.5",H,"welfare reforms and Catholic grievance")]),
"9.7":(1,[L("2.0",H,"1947 education reforms"),L("3.0",H,"the NHS")]),
}
txt=open(P+'packs/hist-ire5-s1.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire5-s1\.[^\]]+)\]',txt,re.M)
allid=set(tg)
dd={"hist-ire5-s1."+k:v for k,v in d.items()}
assert list(dd)==tg,(set(tg)^set(dd))
out={}
for k,(c,n) in dd.items():
    for x in n: assert x['id'] in allid and x['id']!=k
    out[k]={"cost":c,"needs":n}
json.dump(out,open(P+'point-links/hist-ire5-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
