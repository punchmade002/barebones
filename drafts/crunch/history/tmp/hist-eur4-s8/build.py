import json
H,E="helpful","essential"
def L(i,s,w,c="high"): return {"id":i,"strength":s,"why":w,"confidence":c}
P="hist-eur4-s8."
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[]),
"0.2":(1,[]),
"0.3":(1,[L("hist-eur4-s1.4.2",H,"Comecon's founding and purpose")]),
"0.4":(1,[L(P+"0.0",H,"uses Soviet five-year plans")]),
"0.5":(2,[L("hist-eur4-s1.3.7",H,"Soviet-style institutions imposed on states","low")]),
"0.6":(2,[L("hist-eur4-s1.2.5",E,"uses the Marshall Plan"),L(P+"0.3",H,"Comecon's role in trade")]),
"0.7":(1,[L("hist-eur4-s1.4.4",H,"Soviet reparations and dismantling","low")]),
"0.8":(1,[]),
"1.b":(1,[]),
"1.0":(1,[L(P+"0.0",H,"planners' output targets")]),
"1.1":(1,[]),
"1.2":(1,[]),
"1.3":(1,[]),
"1.4":(1,[L(P+"0.2",H,"collectivised farming")]),
"1.5":(1,[]),
"1.6":(1,[]),
"1.7":(1,[L(P+"0.1",H,"priority to heavy industry")]),
"1.8":(2,[]),
"2.b":(1,[]),
"2.0":(1,[L("hist-eur4-s2.1.3",H,"1957 regional economic councils reform")]),
"2.1":(1,[L("hist-eur4-s2.0.11",H,"Kosygin as Soviet premier")]),
"2.2":(1,[]),
"2.3":(1,[L(P+"2.2",H,"Hungary's New Economic Mechanism")]),
"2.4":(1,[L("hist-eur4-s4.3.2",H,"1968 invasion of Czechoslovakia")]),
"2.5":(1,[]),
"2.6":(1,[L(P+"2.1",E,"uses the 1965 Kosygin reform"),L("hist-eur4-s4.3.2",H,"1968 invasion of Czechoslovakia")]),
"2.7":(2,[L("hist-eur4-s1.3.8",H,"Yugoslavia's 1948 break with Moscow")]),
"2.8":(1,[L(P+"2.2",H,"Hungary's reforms")]),
"3.b":(1,[L("hist-eur4-s2.0.11",H,"Brezhnev becoming Soviet leader")]),
"3.0":(1,[]),
"3.1":(2,[]),
"3.2":(1,[]),
"3.3":(1,[L(P+"1.3",H,"arms race burden on economy")]),
"3.4":(1,[L("hist-eur4-s2.7.0",H,"Soviet invasion of Afghanistan")]),
"3.5":(1,[L(P+"1.1",H,"shortages and black markets")]),
"4.b":(1,[]),
"4.0":(1,[L("hist-eur4-s4.2.1",H,"Gomułka's return to power","low")]),
"4.1":(1,[L(P+"4.0",E,"Gierek replaced Gomułka")]),
"4.2":(1,[L(P+"4.1",H,"Gierek's government and its policy")]),
"4.3":(2,[L(P+"4.1",H,"Gierek's Western borrowing"),L("hist-eur4-s4.4.0",H,"Gdańsk strikes and Solidarity's founding")]),
"4.4":(1,[L(P+"4.1",H,"Gierek's borrowing from the West")]),
"4.5":(1,[L("hist-eur4-s4.4.0",H,"Gdańsk strikes of August 1980")]),
"4.6":(1,[L(P+"4.1",E,"Gierek's import of Western technology")]),
"4.7":(2,[L(P+"4.3",H,"Poland's debt and 1980 strikes"),L("hist-eur4-s4.4.5",H,"Round Table talks of 1989")]),
"5.b":(1,[]),
"5.0":(1,[L("hist-eur4-s4.0.2",E,"perestroika defined"),L(P+"3.1",H,"Soviet dependence on oil revenue")]),
"5.1":(1,[]),
"5.2":(1,[]),
"5.3":(1,[]),
"5.4":(2,[L("hist-eur4-s4.0.2",H,"perestroika restructuring")]),
"5.5":(1,[]),
"5.6":(1,[]),
"5.7":(2,[L(P+"5.2",H,"East Germany's dependence on West German credit"),L("hist-eur4-s4.7.5","helpful","German currency union 1990","low")]),
"6.b":(1,[]),
"6.0":(2,[L(P+"2.4",H,"Ota Šik's reform")]),
"6.1":(1,[L("hist-eur4-s2.3.4",H,"building of the Berlin Wall")]),
"6.2":(1,[]),
"6.3":(1,[L(P+"5.1",H,"Ceaușescu's debt repayment austerity")]),
"6.4":(2,[L(P+"2.8",H,"Hungary's partial reforms"),L(P+"4.1",H,"Poland's Western borrowing","low")]),
"7.b":(1,[]),
"7.0":(1,[]),
"7.1":(1,[]),
"7.2":(2,[]),
"7.3":(2,[]),
"7.4":(1,[]),
"7.5":(2,[]),
}
import re
txt=open("/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur4-s8.t1g1.txt").read()
tgt=re.findall(r"^\[(hist-eur4-s8\.[^\]]+)\]",txt,re.M)
ids=set(re.findall(r"^\[([^\]]+)\]",txt,re.M))
assert [P+k for k in d]==tgt,(set(tgt)^{P+k for k in d})
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
for k,v in out.items():
    for n in v["needs"]: assert n["id"] in ids and n["id"]!=k,(k,n)
json.dump(out,open("/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur4-s8.t1g1.json","w"),ensure_ascii=False,indent=1)
print(len(out),sum(len(v["needs"]) for v in out.values()),sum(v["cost"]==2 for v in out.values()),sum(n["confidence"]=="low" for v in out.values() for n in v["needs"]))
