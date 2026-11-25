import json
E,H="essential","helpful"
d={}
ids=[l.strip() for l in open('batch-2.txt') if l.strip()]
L={
"hist-ire4-s2":[("s1",H,"chain-emigration and Famine emigration patterns","high")],
"hist-ire4-s3":[("s1",H,"Famine emigrants triggered anti-Irish hostility","high"),("s2",H,"settlement and occupations of emigrants abroad","high")],
"hist-ire4-s4":[("s3",H,"Irish-American political organisation and communities","high"),("s1",H,"Famine emigrants' bitterness fuelling Fenianism","low")],
"hist-ire4-s5":[("s4",E,"uses Irish America, Clan na Gael and Devoy's networks","high"),("s3",H,"Irish-American political participation and leaders","high")],
"hist-ire4-s6":[("s2",H,"emigrant settlement and community abroad","high"),("s3",H,"Church in Irish-American political and social life","low")],
"hist-ire4-s7":[("s6",H,"Catholic Church's overseas expansion and clergy","high")],
"hist-ire4-s8":[("s3",H,"anti-Irish stereotypes abroad","high"),("s2",H,"emigration shaping images of Ireland","low")],
"hist-ire5-s2":[("s1",E,"uses Unionist government, discrimination and Brookeborough legacy","high")],
"hist-ire5-s3":[("s2",H,"civil rights movement and O'Neill's government","high"),("s1",H,"discrimination against nationalists in public life","high")],
"hist-ire5-s4":[("s2",E,"civil rights crisis, Paisley and O'Neill's fall","high"),("s1",H,"IRA border campaign and discrimination","low")],
"hist-ire5-s5":[("s4",E,"Direct Rule, Faulkner and internment background","high")],
"hist-ire5-s6":[("s5",E,"Sunningdale collapse and its legacy","high"),("s4",H,"Direct Rule and Provisional IRA origins","high")],
"hist-ire5-s7":[("s4",E,"Provisionals, loyalist paramilitaries and Direct Rule origins","high"),("s6",H,"hunger strikes and Anglo-Irish Agreement context","high")],
"hist-ire5-s8":[("s4",E,"outbreak and violence of the Troubles","high"),("s7",H,"paramilitary campaigns causing deaths and disruption","low")],
"hist-ire5-s9":[("s2",H,"Paisley's early career and civil rights","high"),("s4",H,"Troubles context for cultural responses","low")],
"hist-ire5-s10":[("s4",H,"Battle of the Bogside and 1969 violence","high")],
"hist-ire6-s2":[("s1",E,"uses 1950s stagnation, emigration and economic failure","high")],
"hist-ire6-s3":[("s1",H,"Church role in health policy and Mother and Child","high"),("s2",H,"economic expansion funding educational reform","low")],
"hist-ire6-s4":[("s2",E,"uses Lemass-era economy and free trade before 1970s shocks","high"),("s1",H,"emigration and Fianna Fáil-Inter-Party alternation","low")],
"hist-ire6-s5":[("s2",H,"Free Trade Agreement and trade dependence","high"),("s1",H,"1949 Act and anti-partition campaign context","high"),("s4",H,"Lynch, Haughey and FitzGerald leadership","high")],
"hist-ire6-s6":[("s2",E,"move to free trade and economic reasons for EEC","high"),("s5",H,"joint EEC entry with Britain","high")],
"hist-ire6-s7":[("s6",E,"uses EEC applications, accession and the CAP basis","high"),("s2",H,"free trade and economic modernisation before entry","high")],
"hist-ire6-s8":[("s1",H,"1950s emigration and stagnation","high"),("s3",H,"education and social change shaping women's status","low")],
"hist-ire6-s9":[("s1",H,"McQuaid and Church power before Vatican II","high"),("s3",H,"education reform and changing attitudes","low")],
"hist-ire6-s10":[("s2",H,"Lemass-era modernisation behind television policy","high"),("s9",H,"censorship, Church influence and Irish culture","high"),("s4",H,"Arms Crisis and government pressure on broadcasters","low")],
}
for i in ids:
    p=i.rsplit('-s',1)[0]
    d[i]=[{"needs":p+"-"+n,"strength":s,"why":w,"confidence":c} for n,s,w,c in L.get(i,[])]
json.dump(d,open('prereqs-2.json','w'),indent=1)
x=json.load(open('prereqs-2.json'))
assert list(x)==ids
a=[l for v in x.values() for l in v]
for k,v in x.items():
    for l in v: assert l['needs'].rsplit('-s',1)[0]==k.rsplit('-s',1)[0] and l['needs'] in ids and l['needs']!=k
print(len(x),len(a),sum(l['strength']==E for l in a),sum(l['confidence']=='low' for l in a))
