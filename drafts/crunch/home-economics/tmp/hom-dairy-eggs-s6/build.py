import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-dairy-eggs-s6.t1g1'
t='hom-dairy-eggs-s6.';e5='hom-dairy-eggs-s5.';p5='hom-proteins-s5.';l4='hom-lipids-s4.'
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(2,[]),
'0.4':(2,[]),
'0.5':(2,[]),
'0.6':(1,[]),
'0.7':(2,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[]),
'1.4':(1,[]),
'1.5':(1,[]),
'1.6':(1,[(t+'0.6',H,'Bord Bia Quality mark','high')]),
'2.b':(1,[(e5+'0.0',H,'porous shell','high')]),
'2.0':(1,[]),
'2.1':(1,[(e5+'0.0',H,'porous shell absorbs smells','high')]),
'2.2':(1,[(e5+'0.1',E,'cuticle protects shell','high')]),
'2.3':(1,[]),
'2.4':(1,[]),
'2.5':(1,[]),
'2.6':(2,[(e5+'3.7',H,'raw egg salmonella risk','high')]),
'2.7':(2,[(e5+'0.4',H,'air cell grows with age','high'),(e5+'1.1',H,'thick white shows freshness','high')]),
'3.b':(1,[(p5+'0.3',H,'coagulation of protein','high')]),
'3.0':(1,[(p5+'0.6',H,'egg white and yolk set temperatures','low')]),
'3.1':(2,[(p5+'0.0',E,'denaturation unfolds protein','high')]),
'3.2':(1,[(t+'3.1',H,'protein bonding traps water','high')]),
'3.3':(1,[]),
'3.4':(2,[]),
'3.5':(2,[]),
'3.6':(2,[]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(2,[(p5+'1.0',H,'whisking denatures albumen into film','high')]),
'4.2':(2,[(p5+'1.2',H,'heat coagulates foam permanently','high')]),
'4.3':(1,[]),
'4.4':(1,[]),
'4.5':(2,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[(l4+'4.4',H,'lecithin as emulsifier','high')]),
'5.2':(2,[(l4+'4.4',H,'hydrophilic and hydrophobic ends','high')]),
'5.3':(1,[(t+'5.2',H,'lecithin holds oil and water','high')]),
'5.4':(1,[(l4+'2.1',H,'whisking forms droplets','low')]),
'5.5':(2,[(t+'5.1',H,'yolk lecithin emulsifies','high')]),
'5.6':(1,[(t+'5.1',H,'yolk emulsifier','low')]),
'6.b':(1,[]),
'6.0':(1,[(p5+'0.3',H,'coagulation of white','high')]),
'6.1':(1,[]),
'6.2':(1,[]),
'6.3':(1,[(p5+'0.3',H,'protein coagulation toughens','low')]),
'6.4':(2,[]),
'6.5':(1,[]),
}
txt=open(B+'packs/'+P+'.txt').read()
tg=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert [t+k for k in D]==tg,(set(tg)^{t+k for k in D})
out={}
for k,(c,n) in D.items():
    for x in n: assert x[0] in allids and x[0]!=t+k,x
    out[t+k]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(out,open(B+'point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
