import json
def o(*ids,k=1): return {"k":k,"of":list(ids)}
d={
"(a)":[o("bio35-s1.0.0")],
"(b)(i)":[o("bio35-s1.5.1")],
"(b)(ii)":[o("bio35-s1.6.0")],
"(b)(iii)":[o("bio35-s1.6.4","bio35-s1.6.3")],
"(c)(i)":[o("bio35-s1.8.0"),o("bio35-s1.8.1","bio35-s1.8.0")],
"(c)(ii)":[o("bio35-s1.9.0"),o("bio35-s1.9.0")],
"(c)(iii)":[o("bio35-s1.7.0"),o("bio35-s1.7.0")],
}
json.dump(d,open("/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/out/biology-pp-2024-higher-q7.json","w"),indent=1)
