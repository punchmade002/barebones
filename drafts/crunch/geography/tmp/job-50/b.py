import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
sec={0:"1111",1:"112111",2:"1211",3:"122",4:"1111",5:"1111",6:"11111111",7:"11111",8:"1111",9:"12122121",10:"1111",11:"11111",12:"1111",13:"111111",14:"1112111",15:"111",16:"111111",17:"1111",18:"111111111",19:"1121122",20:"112211211",21:"111111",22:"11111",23:"11112",24:"1111",25:"111111",26:"111",27:"1111121",28:"1121111",29:"11111111",30:"111",31:"111",32:"11111"}
S='geo-option-culture-identity-s2.'
def L(i,strength,why,conf='high'): return {"id":i,"strength":strength,"why":why,"confidence":conf}
l={}
def add(k,*a):
    l.setdefault(S+k,[]).append(L(*a))
add('1.0','geo-option-culture-identity-s5.0.5','helpful','uses nation state concept')
add('1.4','geo-option-culture-identity-s5.18.0','helpful','who the Kurds are','low')
add('3.1',S+'3.0','essential','Irish place-name elements')
add('4.0','geo-option-culture-identity-s5.0.6','helpful','multinational state like Belgium','low')
add('5.2',S+'5.0','helpful','language families')
add('6.0',S+'5.0','essential','language family concept')
for k in '12345': add('6.'+k,S+'5.0','helpful','language family concept')
for k in '0123': add('9.'+k,S+'6.0','helpful','Indo-European family')
add('9.5',S+'6.0','helpful','Indo-European family')
add('11.3',S+'15.0','helpful','minority language meaning')
add('12.2',S+'15.0','helpful','minority language meaning','low')
add('18.0',S+'19.0','helpful','Article 8 for Irish')
add('20.3',S+'20.2','essential','enforces the Official Languages Act')
add('20.4','geo-option-culture-identity-s5.30.0','helpful','Good Friday Agreement','low')
add('22.1',S+'22.0','essential','the 2007 study')
add('22.2',S+'19.1','helpful','Irish speaker census figures')
add('24.2',S+'14.2','essential','S4C campaign')
add('27.3',S+'27.2','essential','second-home pressure')
add('28.0','geo-option-culture-identity-s5.10.0','helpful','autonomy of regions')
add('28.4',S+'14.4','essential','EITB broadcaster')
add('29.3',S+'31.0','helpful','European Charter for minority languages')
add('31.1',S+'10.1','helpful','Irish EU status')
add('5.2',S+'5.0','helpful','language families') if False else None
import collections
def build(pack,out,withcost):
    t=open(P+'packs/'+pack).read()
    tgt=[];cands=set();mode=None
    for line in t.split('\n'):
        if line.startswith('TARGET'):mode='t'
        elif line.startswith('CANDIDATES'):mode='c'
        m=re.match(r'\[([^\]]+)\]',line)
        if m: (tgt if mode=='t' else cands.add(m.group(1)) or []).append(m.group(1)) if mode=='t' else cands.add(m.group(1))
    exp=[]
    for n in range(33):
        exp+= [S+f'{n}.b']+[S+f'{n}.{i}' for i in range(len(sec[n])-1)]
    assert exp==tgt,(len(exp),len(tgt))
    cost={}
    for n in range(33):
        ids=[S+f'{n}.b']+[S+f'{n}.{i}' for i in range(len(sec[n])-1)]
        for i,c in zip(ids,sec[n]): cost[i]=int(c)
    res={}
    for i in tgt:
        res[i]={}
    return tgt,cands,cost
