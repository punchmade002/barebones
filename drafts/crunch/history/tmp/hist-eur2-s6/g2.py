import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
L={
'0.0':['8.13.3|H|Russia leaving war in 1917|l'],
'2.2':['8.13.2|H|Soviets as councils on Russian model|h'],
'2.7':['8.16.3|H|Brest-Litovsk cancelled|h'],
'3.2':['8.15.3|H|Bolshevik seizure of power|l'],
'3.5':['8.13.2|H|Russian soviets as councils|h'],
'4.0':['8.15.4|H|Russian council republic|l'],
'4.5':['8.15.4|H|Soviet republic model|l'],
'6.4':['8.15.4|H|Soviet republic model|l'],
'7.0':['8.15.5|H|Bolshevik Decree on Peace|h'],
'13.0':['8.18.2|H|states breaking from Russia|h'],
'16.3':['8.15.3|H|Bolshevik revolution fear|h'],
'16.4':['8.17.1|H|Russian Civil War|h','8.17.7|H|Polish-Soviet war|h'],
'17.0':['8.15.3|H|Bolshevik-style regime|l'],
}
E='''0.b 0.1 0.2 0.3 0.4 0.5 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.3 2.4 2.5 2.6 3.b 3.0 3.1 3.3 3.4 4.b 4.1 4.2 4.3 4.4 5.b 5.0 5.1 5.2 5.3 5.4 5.5 6.b 6.0 6.1 6.2 6.3 7.b 7.1 7.2 7.3 7.4 7.5 7.6 7.7 8.b 8.0 8.1 8.2 8.3 8.4 8.5 8.6 9.b 9.0 9.1 9.2 9.3 9.4 9.5 10.b 10.0 10.1 10.2 10.3 10.4 10.5 10.6 11.b 11.0 11.1 11.2 11.3 11.4 11.5 11.6 11.7 12.b 12.0 12.1 12.2 12.3 12.4 12.5 13.b 13.1 13.2 13.3 13.4 13.5 13.6 13.7 14.b 14.0 14.1 14.2 14.3 14.4 14.5 14.6 14.7 15.b 15.0 15.1 15.2 15.3 15.4 15.5 15.6 15.7 16.b 16.0 16.1 16.2 16.5 17.b 17.1 17.2 17.3 17.4 17.5 17.6 17.7'''.split()
txt=open(D+'packs/hist-eur2-s6.t1g2.txt').read()
head,_=txt.split('CANDIDATES')
tg=[t[len('hist-eur2-s6.'):] for t in re.findall(r'^\[(hist-eur2-s6\.[^\]]+)\]',head,re.M)]
assert set(L)|set(E)==set(tg) and not set(L)&set(E) and len(E)+len(L)==len(tg)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for k in tg:
    ns=[]
    for n in L.get(k,[]):
        r,s,w,c=n.split('|'); i='hist-eur2-s'+r if False else 'hist-eur2-s'+r
        assert i in allids
        ns.append({"id":i,"strength":"helpful" if s=='H' else "essential","why":w,"confidence":"high" if c=='h' else "low"})
    out['hist-eur2-s6.'+k]={"needs":ns}
json.dump(out,open(D+'point-links/hist-eur2-s6.t1g2.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
