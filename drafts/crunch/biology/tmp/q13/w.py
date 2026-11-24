import json
def o(*ids,k=1): return {"k":k,"of":list(ids)}
d={
"(a)(i)":[o("bio14-s2.0.3"),o("bio14-s2.0.4")],
"(a)(ii)":[o("bio14-s2.0.3","bio14-s4.1.2")],
"(b)(i)":[o("bio14-s3.0.4"),o("bio14-s3.2.1"),o("bio14-s3.2.0"),o("bio14-s3.1.1"),o("bio14-s3.1.2"),o("bio14-s3.1.3","bio14-s3.1.4")],
"(b)(ii)":[o("bio14-s1.1.0"),o("bio14-s1.1.1")],
"(b)(iii)":[o("bio14-s4.0.6","bio14-s4.2.2","bio14-s1.6.1")],
"(b)(iv)":[o("bio14-s4.0.3","bio14-s4.2.1"),o("bio14-s4.0.3","bio14-s4.2.1")],
"(c)(i)":[o("bio16-s1.0.3")],
"(c)(ii)":[o("bio16-s1.4.4"),o("bio16-s1.4.5"),o("bio16-s1.4.7")],
"(c)(iii)1":[o("bio16-s1.6.1"),o("bio16-s1.6.1")],
"(c)(iii)2":[o("bio16-s1.6.2"),o("bio16-s1.6.3")],
"(c)(iv)1":[o("bio16-s2.2.0")],
"(c)(iv)2":[o("bio16-s2.3.0"),o("bio16-s2.3.2")],
}
json.dump(d,open("/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/out/biology-pp-2017-higher-q13.json","w"),indent=1)
