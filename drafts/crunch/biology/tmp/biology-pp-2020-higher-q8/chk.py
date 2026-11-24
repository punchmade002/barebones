import sys,json,re
d='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
for q in sys.argv[1:]:
  t=open(d+'packages/'+q+'.txt').read()
  ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
  parts=re.findall(r'^PART (\S+) ',t,re.M)
  j=json.load(open(d+'out/'+q+'.json'))
  assert list(j)==parts,(q,list(j),parts)
  n=0
  for p,l in j.items():
    for m in l:
      n+=1
      assert 1<=m['k']<=len(m['of']),p
      for i in m['of']: assert i in ids,(p,i)
  print(q,len(parts),n,[p for p,l in j.items() if not l])
