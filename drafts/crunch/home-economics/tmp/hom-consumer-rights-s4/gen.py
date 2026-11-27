import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics'
def h(i,w,c='high'): return dict(id=i,strength='helpful',why=w,confidence=c)
def e(i,w,c='high'): return dict(id=i,strength='essential',why=w,confidence=c)
P={}
p='hom-consumer-rights-s4.'; s3='hom-consumer-rights-s3.'
P['hom-consumer-rights-s4']=[
('0.b',1,[]),
('0.0',1,[h(s3+'0.1','trader as retailer or seller')]),
('0.1',1,[h(s3+'0.0','consumer definition')]),
('0.2',1,[]),
('0.3',1,[h(p+'0.2','statutory rights apply automatically')]),
('0.4',1,[h(p+'1.b','standards of quality and description')]),
('1.b',1,[]),
('1.0',2,[]),
('1.1',1,[]),
('1.2',1,[]),
('1.3',1,[]),
('1.4',1,[]),
('1.5',1,[h(s3+'0.2','retailer responsible for faults')]),
('2.b',1,[]),
('2.0',1,[]),
('2.1',1,[h(p+'1.0','satisfactory quality standard'),h(p+'1.1','fit for purpose standard')]),
('2.2',1,[]),
('2.3',1,[]),
('2.4',1,[]),
('3.b',1,[]),
('3.0',1,[h(p+'1.b','standards goods must meet')]),
('3.1',1,[e(p+'3.0','repair or replacement fails first')]),
('3.2',1,[h(p+'3.0','repair as the usual first remedy')]),
('3.3',1,[h(p+'2.b','service standard')]),
('3.4',1,[h(s3+'0.4','guarantee defined'),h(p+'0.2','statutory rights automatic')]),
('4.b',1,[]),
('4.0',1,[h(p+'3.1','refund remedy','low')]),
('4.1',1,[h(p+'0.2','statutory rights apply automatically')]),
('4.2',1,[h(p+'1.4','fault present at supply','low')]),
('4.3',1,[h(p+'4.2','fault pointed out beforehand exception')]),
('4.4',1,[h(p+'1.4','fault present when supplied')]),
('4.5',1,[h(s3+'2.4','keeping receipts','low')]),
('5.b',1,[]),
('5.0',1,[]),
('5.1',1,[]),
('5.2',1,[]),
('5.3',1,[h(s3+'1.7','quality marks','low')]),
('5.4',1,[h(s3+'1.5','CCPC role')]),
('5.5',1,[h(p+'5.4','state body CCPC takes action','low')]),
('6.b',1,[h(p+'5.0','misleading information')]),
('6.0',1,[h(p+'5.0','misleading actions')]),
('6.1',1,[h(p+'6.0','false price information')]),
('6.2',1,[h(p+'6.1','misleading price comparisons')]),
]
p='hom-food-preservation-s1.'; s3='hom-food-safety-s3.'
P['hom-food-preservation-s1']=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[h(p+'0.0','reduced waste')]),
('0.2',1,[]),
('0.3',1,[h(p+'1.1','food poisoning micro-organisms')]),
('0.4',1,[]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',2,[]),
('1.2',1,[h(p+'1.1','bacteria cause putrefaction')]),
('1.3',1,[]),
('1.4',1,[]),
('1.5',1,[h(p+'1.1','micro-organisms speed with warmth'),h(p+'1.0','enzymes speed with warmth')]),
('1.6',1,[h(p+'1.1','micro-organisms carried onto food')]),
('1.7',1,[]),
('2.b',1,[]),
('2.0',2,[]),
('2.1',2,[h(p+'2.0','warmth condition')]),
('2.2',1,[h(p+'2.0','time condition','low')]),
('2.3',1,[h(p+'1.1','moulds and yeasts')]),
('2.4',1,[h(p+'1.1','moulds and yeasts')]),
('2.5',1,[h(p+'1.0','enzymes')]),
('2.6',1,[h(p+'2.0','moisture condition')]),
('3.b',1,[]),
('3.0',1,[]),
('3.1',1,[]),
('3.2',1,[]),
('3.3',1,[h(p+'3.2','moulds spread by spores')]),
('3.4',1,[h(p+'1.0','enzymes')]),
('4.b',1,[]),
('4.0',1,[h(p+'4.b','partially permeable membrane')]),
('4.1',1,[h(p+'4.0','water leaving the cell')]),
('4.2',1,[h(p+'4.b','osmosis')]),
('5.b',1,[h(p+'2.0','conditions micro-organisms need')]),
('5.0',2,[h(p+'1.1','micro-organisms destroyed'),h(p+'1.0','enzymes inactivated')]),
('5.1',1,[h(p+'2.1','temperature and growth')]),
('5.2',2,[e(p+'4.b','osmosis draws water out'),h(p+'2.6','water needed for growth')]),
('5.3',2,[h(p+'2.0','pH condition')]),
('5.4',2,[]),
('5.5',2,[h(p+'2.0','oxygen condition')]),
('5.6',1,[h(p+'1.6','poor hygiene contaminates food')]),
('5.7',2,[h(p+'5.0','heat principle'),h(p+'5.2','sugar and osmosis'),h(p+'5.3','acid principle')]),
('6.b',1,[]),
('6.0',1,[h(p+'5.1','low temperature principle')]),
('6.1',1,[h(p+'5.0','heat principle')]),
('6.2',1,[h(p+'5.2','water removal principle')]),
('6.3',1,[h(p+'5.4','chemical preservatives')]),
('6.4',1,[h(p+'5.3','fermentation acids','low')]),
]
p='hom-food-industry-s1.'; s8='hom-food-safety-s8.'
P['hom-food-industry-s1']=[
('0.b',1,[]),
('0.0',2,[]),
('0.1',1,[h(p+'0.0','raw materials from primary sector')]),
('0.2',2,[]),
('0.3',1,[]),
('0.4',1,[]),
('0.5',1,[]),
('1.b',1,[h(p+'0.b','three levels of industry')]),
('1.0',1,[]),('1.1',1,[]),('1.2',1,[]),('1.3',1,[]),('1.4',1,[]),('1.5',1,[]),('1.6',1,[]),
('2.b',1,[]),
('2.0',1,[h(p+'1.0','dairy sector')]),
('2.1',1,[h(p+'1.1','meat sector')]),
('2.2',1,[h(p+'1.1','meat sector')]),
('2.3',1,[h(p+'1.2','beverages sector')]),
('2.4',1,[h(p+'1.4','seafood sector')]),
('2.5',1,[h(p+'1.6','prepared foods sector')]),
('3.b',1,[]),
('3.0',1,[]),('3.1',1,[]),('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),('3.5',1,[]),
('3.6',1,[h(p+'2.0','dairy exports','low')]),
('3.7',1,[h(p+'2.b','exports')]),
('4.b',1,[]),
('4.0',1,[]),
('4.1',1,[h(p+'4.0','Bord Bia role')]),
('4.2',1,[h(p+'4.0','Bord Bia role')]),
('4.3',1,[h(p+'4.0','Bord Bia role')]),
('4.4',1,[]),('4.5',1,[]),('4.6',1,[]),
('4.7',1,[h(s8+'1.0','FSAI food safety role')]),
('4.8',1,[]),
('5.b',1,[h(p+'0.b','industry structure')]),
('5.0',1,[h(p+'0.b','primary secondary tertiary levels')]),
('5.1',1,[]),
('5.2',1,[h(p+'2.b','export markets','low')]),
('5.3',1,[h(p+'0.4','employment and rural income')]),
('5.4',1,[]),
]
for sub,items in P.items():
    out={}
    for k,c,n in items:
        out[sub+'.'+k]={'cost':c,'needs':n}
    ptxt=open(f'{D}/packs/{sub}.t1g1.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',ptxt,re.M))
    tgt=re.findall(r'^\[([^\]]+)\]',ptxt.split('CANDIDATES')[0],re.M)
    assert list(out)==tgt,(sub,set(tgt)^set(out),)
    links=0
    for k,v in out.items():
        for x in v['needs']:
            assert x['id'] in ids and x['id']!=k,(k,x)
            assert len(x['why'].split())<=8,(k,x)
            links+=1
    json.dump(out,open(f'{D}/point-links/{sub}.t1g1.json','w'),indent=1)
    d=json.load(open(f'{D}/point-links/{sub}.t1g1.json'))
    print(sub,len(d),links,sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
