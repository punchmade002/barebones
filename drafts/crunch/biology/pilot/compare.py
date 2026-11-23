import json,sys,glob,re
from pathlib import Path
D=Path(__file__).parent; P=D.parent/'points'
for sid in ['bio15-s1','bio14-s3']:
    pkg=(P/f'{sid}.txt').read_text(); ids=set(re.findall(r'^\[([^\]]+)\]',pkg,re.M))
    own=[i for i in re.findall(r'^\[([^\]]+)\]',pkg,re.M) if i.startswith(sid+'.')]
    res={}
    for m in ['haiku','sonnet']:
        f=D/f'{m}-{sid}.json'
        if not f.exists(): print(sid,m,'missing'); continue
        r=json.loads(f.read_text()); res[m]=r
        links={(k,l['id']) for k,v in r.items() for l in v['needs']}
        bad=[l for l in links if l[1] not in ids or l[0]==l[1]]
        print(f"{sid} {m}: {len(r)}/{len(own)} items, {len(links)} links "
              f"({sum(1 for k,v in r.items() for l in v['needs'] if l['strength']=='essential')} ess), "
              f"cost2 {sum(1 for v in r.values() if v['cost']==2)}, cross-subsection {sum(1 for a,b in links if not b.startswith(sid+'.'))}, bad {len(bad)}")
    if len(res)==2:
        a={(k,l['id']) for k,v in res['haiku'].items() for l in v['needs']}; b={(k,l['id']) for k,v in res['sonnet'].items() for l in v['needs']}
        agree=sum(1 for k in own if res['haiku'].get(k,{}).get('cost')==res['sonnet'].get(k,{}).get('cost'))
        print(f"  link overlap {len(a&b)} shared, {len(a-b)} haiku-only, {len(b-a)} sonnet-only; cost agreement {agree}/{len(own)}")
