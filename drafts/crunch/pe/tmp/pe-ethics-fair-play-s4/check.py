import json,re,sys
d='/Users/gabrielwhelan/barebones/drafts/crunch/pe/'
for s in ['s4','s5']:
    n='pe-ethics-fair-play-'+s
    txt=open(d+'points/'+n+'.txt').read()
    tgt=txt.split('\nCANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    raw=open(d+'point-links/'+n+'.json').read()
    j=json.loads(raw)
    assert list(j)==tids,(set(tids)^set(j))
    links=sum(len(v['needs']) for v in j.values())
    for k,v in j.items():
        for x in v['needs']: assert x['id'] in allids and x['id']!=k,(k,x)
    print(s,len(j),links,sum(v['cost']==2 for v in j.values()),sum(x['confidence']=='low' for v in j.values() for x in v['needs']))
