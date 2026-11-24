import json
def o(*ids,k=1): return {"k":k,"of":list(ids)}
d={
"(a)(i)":[o("bio29-s3.3.0")],
"(a)(ii)":[o("bio29-s3.3.1")],
"(b)(i)":[o("bio29-s3.4.0","bio29-s3.3.3")],
"(b)(ii)":[o("bio2-s2.2.1")],
"(b)(iii)1":[o("bio29-s3.4.0"),o("bio29-s3.4.3","bio2-s2.0.2")],
"(b)(iii)2":[],
"(b)(iv)":[o("bio29-s3.4.0"),o("bio29-s3.3.5","bio29-s3.4.0"),o("bio29-s3.4.1","bio29-s3.4.0")],
}
json.dump(d,open("/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/out/biology-pp-2016-higher-q8.json","w"),indent=1)
