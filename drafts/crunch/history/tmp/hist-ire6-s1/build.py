import json,re
P='hist-ire6-s1.'
E,H='essential','helpful'
def l(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
D={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),"0.2":(1,[]),"0.3":(1,[]),
"1.b":(1,[]),"1.0":(1,[]),
"1.1":(1,[l("1.0",E,"balance of payments deficit")]),
"1.2":(1,[l("1.0",H,"balance of payments deficit"),l("1.1",H,"drained foreign reserves")]),
"1.3":(1,[l("1.2",E,"deflation"),l("6.2",H,"MacEntee's 1952 budget")]),
"2.b":(1,[]),"2.0":(1,[]),"2.1":(1,[]),
"2.2":(2,[l("2.1",H,"Clann na Poblachta")]),
"2.3":(1,[l("2.2",H,"the 1948 coalition")]),
"2.4":(1,[l("2.1",H,"Clann na Poblachta")]),
"2.5":(1,[l("2.2",H,"the parties in the coalition")]),
"3.b":(1,[]),
"3.0":(1,[l("2.3",H,"Costello as Taoiseach")]),
"3.1":(1,[l("3.0",E,"the announcement of a republic")]),
"3.2":(1,[l("3.1",E,"the Republic of Ireland Act")]),
"3.3":(1,[l("3.2",E,"the Ireland Act 1949")]),
"3.4":(1,[l("2.4",H,"MacBride as External Affairs minister")]),
"3.5":(1,[]),"3.6":(2,[]),
"3.7":(2,[l("2.4",H,"Noel Browne as Health Minister")]),
"3.8":(1,[]),
"4.b":(1,[l("0.3",H,"Church influence on policy")]),
"4.0":(2,[l("2.4",H,"Browne's ministry")]),
"4.1":(1,[l("4.0",E,"the Mother and Child scheme")]),
"4.2":(2,[l("4.0",E,"the Mother and Child scheme"),l("0.3",H,"Church influence on policy")]),
"4.3":(1,[l("4.2",H,"the bishops' objections")]),
"4.4":(2,[l("4.3",E,"the bishops' letters"),l("2.4",H,"Browne and MacBride")]),
"4.5":(1,[l("4.4",E,"the dispute over Browne's resignation")]),
"4.6":(2,[l("4.4",E,"Browne's resignation"),l("2.1",H,"Clann na Poblachta")]),
"4.7":(1,[l("4.0",E,"the Mother and Child scheme")]),
"5.b":(1,[l("4.b",H,"the 1950-51 crisis")]),
"5.0":(1,[]),
"5.1":(1,[l("0.3",H,"the 1937 Constitution and Church")]),
"5.2":(2,[l("4.2",E,"the Church's objections"),l("4.0",H,"Browne's scheme")]),
"5.3":(1,[l("4.2",H,"the bishops' objection")]),
"5.4":(1,[l("4.4",H,"Browne's view of the dispute","low")]),
"5.5":(2,[l("4.5",H,"government deferring to bishops")]),
"6.b":(1,[l("1.2",H,"deflation")]),
"6.0":(1,[]),
"6.1":(1,[l("6.0",H,"the minority government")]),
"6.2":(2,[l("1.2",E,"deflation"),l("1.0",H,"balance of payments deficit")]),
"6.3":(1,[]),
"6.4":(1,[l("4.7",E,"the Mother and Child scheme replaced"),l("4.0",H,"Mother and Child scheme")]),
"6.5":(1,[l("6.2",H,"effects of deflation")]),
"7.b":(1,[l("1.0",H,"balance of payments problem")]),
"7.0":(1,[l("2.1",H,"Clann na Poblachta")]),
"7.1":(1,[]),
"7.2":(1,[l("1.0",E,"balance of payments")]),
"7.3":(1,[l("1.2",E,"deflation"),l("7.2",H,"the 1955-56 crisis")]),
"7.4":(1,[]),
"7.5":(1,[l("2.1",H,"Clann na Poblachta")]),
"7.6":(1,[l("7.5",E,"Clann na Poblachta pressure"),l("7.0",H,"outside support for government")]),
"8.b":(1,[]),"8.0":(1,[]),
"8.1":(2,[]),
"8.2":(1,[l("8.1",H,"emigration to Britain")]),
"8.3":(1,[]),
"8.4":(1,[l("0.0",H,"tariffs and the Control of Manufactures Acts")]),
"8.5":(1,[]),
"8.6":(1,[l("0.2",H,"link to sterling")]),
"9.b":(1,[]),
"9.0":(1,[l("7.6",H,"the election that followed")]),
"9.1":(1,[l("6.0",H,"Lemass and MacEntee in 1951")]),
"9.2":(1,[]),
"9.3":(2,[]),
"9.4":(2,[l("8.6",H,"the sterling link"),l("0.2",H,"dependence on Britain")]),
"9.5":(2,[l("3.5",H,"the IDA"),l("6.3",H,"Underdeveloped Areas Act")]),
"10.b":(1,[]),
"10.0":(2,[l("3.1",H,"Republic of Ireland Act"),l("3.5",H,"the IDA"),l("6.3",H,"Underdeveloped Areas Act"),l("3.7",H,"anti-TB campaign")]),
"10.1":(2,[l("1.2",E,"deflation"),l("8.1",H,"emigration")]),
"10.2":(2,[l("4.4",H,"the Mother and Child affair")]),
"10.3":(2,[l("4.6",H,"the 1951 election"),l("7.6",H,"the 1957 election")]),
"10.4":(2,[l("9.3",H,"the wasted years view"),l("9.4",H,"dependence on Britain")]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in D.items()}
json.dump(out,open("point-links/hist-ire6-s1.t1g1.json","w"),indent=1)
txt=open("packs/hist-ire6-s1.t1g1.txt").read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt,re.M)
o=json.load(open("point-links/hist-ire6-s1.t1g1.json"))
assert list(o)==tg,(set(tg)^set(o))
n=lo=0
for k,v in o.items():
    for x in v["needs"]:
        assert x["id"] in ids and x["id"]!=k,(k,x);n+=1;lo+=x["confidence"]=="low"
print(len(o),n,sum(v["cost"]==2 for v in o.values()),lo)
