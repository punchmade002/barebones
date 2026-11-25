import json
def o(*ids,k=1): return {"k":k,"of":list(ids)}
d={
"(a)":[o("bio31-s1.2.1","bio32-s4.0.b")],
"(b)":[o("bio31-s1.3.0")],
"(c)":[o("bio31-s1.0.2")],
"(d)":[o("bio31-s1.0.1")],
"(e)":[o("bio31-s10.0.0")],
"(f)":[o("bio31-s1.1.0")],
"(g)":[o("bio32-s2.0.0")],
}
json.dump(d,open("/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/out/biology-pp-2018-higher-q2.json","w"),indent=1)
