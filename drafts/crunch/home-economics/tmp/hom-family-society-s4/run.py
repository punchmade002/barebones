exec(open(__file__.replace('run.py','build.py')).read())
out={}
for k,(c,n) in D.items():
    out['hom-family-society-s4.'+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
pk=open(B+'packs/'+name+'.txt').read()
tg=re.findall(r'^\[(\S+)\]',pk.split('CANDIDATES')[0],re.M)
allid=set(re.findall(r'^\[(\S+)\]',pk,re.M))
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allid and n['id']!=k,(k,n)
json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
