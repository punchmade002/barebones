import json,re
P='geo-option-atmosphere-ocean-s5.'
ids="18.2 18.3 18.4 18.5 19.b 19.0 19.1 19.2 19.3 19.4 19.5 19.6 20.b 20.0 21.b 21.0 21.1 21.2 21.3 21.4 21.5 22.b 22.0 22.1 22.2 22.3 22.4 23.b 23.0 23.1 23.2 23.3 23.4 23.5 24.b 24.0 24.1 24.2 24.3 24.4 24.5 24.6 25.b 25.0 25.1 25.2 25.3 25.4 25.5 25.6 26.b 26.0 26.1 26.2 26.3 26.4 26.5 26.6 27.b 27.0 27.1 27.2 27.3 27.4 27.5 28.b 28.0 28.1 28.2 28.3 28.4 28.5 29.b 29.0 29.1 29.2 30.b 30.0 30.1 30.2 30.3 31.b 31.0 31.1 31.2 31.3 31.4 32.b 32.0 32.1 32.2 32.3 32.4 32.5 32.6 33.b 33.0 33.1 33.2 33.3 34.b 34.0 34.1 34.2 35.b 35.0 35.1 35.2".split()
L={'19.0':[{"id":"geo-plate-tectonics-s2.5.5","strength":"helpful","why":"plate movement over geological time","confidence":"low"}],
'19.4':[{"id":"geo-plate-tectonics-s2.5.5","strength":"helpful","why":"moving continents change ocean map","confidence":"high"}]}
out={P+i:{"needs":L.get(i,[])} for i in ids}
json.dump(out,open('../../point-links/geo-option-atmosphere-ocean-s5.t2g4.json','w'),indent=1)
t=open('../../packs/geo-option-atmosphere-ocean-s5.t2g4.txt').read().split('CANDIDATES')[0]
tid=re.findall(r'^\[([^\]]+)\]',t,re.M)
print(len(tid),set(tid)==set(out),len(out),sum(len(v['needs']) for v in out.values()))
