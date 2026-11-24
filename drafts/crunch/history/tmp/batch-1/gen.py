import json
E,H="essential","helpful"
D={
"hist-ire1-s1":[],
"hist-ire1-s2":[("s1",E,"uses Catholic Association, Emancipation and O'Connell's early career","high")],
"hist-ire1-s3":[("s2",H,"Poor Law 1838 underlies the Poor Law Extension Act","high"),("s1",H,"Dublin Castle administration and Union government machinery","low")],
"hist-ire1-s4":[("s3",E,"private relief responds to the Famine and government policy","high")],
"hist-ire1-s5":[("s4",E,"post-Famine economy builds on Famine population and land impact","high")],
"hist-ire1-s6":[("s2",H,"Young Ireland and 1848 precede Fenianism and Repeal legacy","high"),("s4",H,"Famine emigration and bitterness feed Fenianism and Tenant League","high"),("s5",H,"post-Famine landlordism underlies Tenant League demands","high")],
"hist-ire1-s7":[("s4",H,"Famine shaped devotional revolution, language decline and identities","high"),("s2",H,"Young Ireland and Thomas Davis cultural nationalism","high")],
"hist-ire2-s1":[],
"hist-ire2-s2":[("s1",E,"uses Parnell, the New Departure and Home Rule party","high")],
"hist-ire2-s3":[("s1",E,"uses Parnell's Irish Party and Home Rule movement","high"),("s2",H,"uses the Land War and coercion background","low")],
"hist-ire2-s4":[("s3",E,"uses the First Home Rule Bill and 1885-86 elections","high"),("s2",H,"uses the Plan of Campaign and land agitation","high")],
"hist-ire2-s5":[("s3",E,"uses the First Home Rule Bill and unionist mobilisation 1886","high"),("s4",H,"uses the Second Home Rule Bill and Redmond's party","low")],
"hist-ire2-s6":[("s4",H,"uses the Irish Party's attitude to suffrage and nationalism","low"),("s5",H,"uses unionism for suffrage, nationalism and unionism","low")],
"hist-ire2-s7":[],
"hist-ire2-s8":[("s2",H,"uses Congested Districts Board and constructive unionism","low")],
"hist-ire2-s9":[("s4",H,"uses the Parnell split and the IRB","high")],
"hist-ire2-s10":[("s9",E,"compares the GAA and builds on its founding","high"),("s4",H,"uses Parnell's fall as backdrop to cultural revival","low")],
"hist-ire2-s11":[],
"hist-ire3-s1":[],
"hist-ire3-s2":[("s1",E,"uses the 1916 Rising and its shift in opinion","high")],
"hist-ire3-s3":[("s1",E,"uses the Home Rule crisis and Ulster Volunteers","high"),("s2",H,"uses War of Independence violence behind the 1920 Act","low")],
"hist-ire3-s4":[("s2",E,"uses the War of Independence, Truce and Dáil","high"),("s3",H,"uses partition and the Northern Ireland question","high")],
"hist-ire3-s5":[("s4",E,"uses the Treaty and Dáil debates behind the split","high"),("s3",H,"uses the Boundary Commission and Northern state","low")],
"hist-ire3-s6":[("s5",E,"uses Cosgrave's state and Fianna Fáil's rise to power","high"),("s4",E,"uses the Treaty terms and oath that de Valera dismantles","high"),("s3",H,"uses partition and the ports and North in 1938","low")],
"hist-ire3-s7":[("s6",H,"uses the Economic War and protectionist policy","high"),("s5",H,"uses Cumann na nGaedheal government and 1932 change","high"),("s3",H,"uses partition's economic effects","high")],
"hist-ire3-s8":[("s6",E,"uses de Valera, 1938 Agreements and Treaty ports for neutrality","high"),("s7",H,"uses the wartime economy's prewar state","low")],
"hist-ire3-s9":[("s3",E,"uses the Northern Ireland state and unionist government","high"),("s8",H,"compares with neutral South's wartime experience","low")],
"hist-ire3-s10":[("s5",H,"uses Free State state building and Catholic ethos","high"),("s3",H,"uses the Unionist state for education and identity in the North","high"),("s6",H,"uses the 1937 Constitution and de Valera's cultural aims","low")],
"hist-ire3-s11":[("s5",E,"uses Cosgrave's Free State and the 1932 transfer of power","high"),("s6",H,"uses de Valera's government and Governor-General dispute","high"),("s3",H,"uses unionist reactions in Northern Ireland","low"),("s10",H,"uses Catholic ethos and Church-state relations","high")],
}
out={}
for k,v in D.items():
    p=k.split("-s")[0]
    out[k]=[{"needs":p+"-"+n,"strength":s,"why":w,"confidence":c} for n,s,w,c in v]
base="/Users/gabrielwhelan/barebones/drafts/crunch/history/"
json.dump(out,open(base+"prereqs-1.json","w"),indent=1,ensure_ascii=False)
ids=open(base+"batch-1.txt").read().split()
o=json.load(open(base+"prereqs-1.json"))
assert list(o)==ids
l=[x for v in o.values() for x in v]
for k,v in o.items():
    n=[x["needs"] for x in v]; assert len(set(n))==len(n) and k not in n
    assert all(x.split("-s")[0]==k.split("-s")[0] and x in ids for x in n)
    assert all(len(x["why"].split())<=12 for x in v)
print(len(o),len(l),sum(x["strength"]=="essential" for x in l),sum(x["confidence"]=="low" for x in l))
