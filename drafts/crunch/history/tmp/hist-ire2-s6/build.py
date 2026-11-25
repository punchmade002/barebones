import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history'
P='hist-ire2-'
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
R={
"s6.0.b":(1,[]),"s6.0.0":(1,[]),
"s6.0.1":(1,[n("s6.1.2",H,"Tod's campaign for 1882 Act")]),
"s6.0.2":(1,[n("s6.1.1",H,"Tod's Ulster suffrage society")]),
"s6.0.3":(1,[]),"s6.0.4":(1,[]),"s6.0.5":(1,[]),"s6.0.6":(2,[]),
"s6.0.7":(1,[n("s6.0.6",E,"uses the 1898 local government Act")]),
"s6.0.8":(1,[n("s6.1.6",H,"Tod as unionist opposing Home Rule")]),
"s6.1.b":(1,[]),
"s6.1.0":(1,[n("s6.4.b",H,"Hanna Sheehy-Skeffington as contrast")]),
"s6.1.1":(1,[]),
"s6.1.2":(1,[n("s6.0.1",H,"the 1882 Married Women's Property Act")]),
"s6.1.3":(2,[n("s6.6.7",H,"Margaret Byers, Ladies' Collegiate School","low")]),
"s6.1.4":(2,[n("s6.6.0",H,"Intermediate Education Act 1878"),n("s6.7.2",H,"Royal University degrees for women")]),
"s6.1.5":(1,[]),
"s6.1.6":(1,[n("s5.3.3",H,"Liberal Unionists opposed 1886 Bill","low")]),
"s6.1.7":(1,[]),
"s6.1.8":(1,[n("s6.1.1",H,"first sustained Ulster suffrage organisation")]),
"s6.2.b":(1,[n("s4.5.b",H,"Redmond and the Irish Party")]),
"s6.2.0":(1,[]),
"s6.2.1":(1,[n("s6.3.b",H,"Franchise League's direct action")]),
"s6.2.2":(1,[n("s6.2.b",H,"Irish Party refusing to back votes")]),
"s6.2.3":(2,[n("s4.6.b",H,"Redmond and Dillon, Irish Party leaders")]),
"s6.2.4":(2,[n("s5.7.3",E,"uses the Third Home Rule Bill")]),
"s6.2.5":(1,[n("s6.4.b",H,"Hanna Sheehy-Skeffington's views")]),
"s6.3.b":(1,[n("s6.2.1",H,"Irish Women's Franchise League")]),
"s6.3.0":(1,[]),
"s6.3.1":(1,[n("s6.3.0",H,"the Franchise League")]),
"s6.3.2":(1,[n("s6.3.0",H,"the Franchise League members")]),
"s6.3.3":(2,[n("s4.6.b",H,"Redmond as Irish Party leader","low")]),
"s6.3.4":(1,[n("s6.3.2",H,"imprisoned suffragettes")]),
"s6.3.5":(1,[n("s6.3.4",H,"hunger strike by suffragettes")]),
"s6.3.6":(1,[n("s6.3.b",H,"militant suffragette tactics")]),
"s6.4.b":(1,[]),"s6.4.0":(1,[]),"s6.4.1":(1,[]),
"s6.4.2":(1,[n("s6.3.0",H,"founding of Franchise League")]),
"s6.4.3":(1,[n("s6.5.1",H,"Cumann na mBan's auxiliary status")]),
"s6.4.4":(1,[]),"s6.4.5":(1,[]),"s6.4.6":(1,[]),
"s6.5.b":(1,[]),
"s6.5.0":(1,[n("s5.8.1",E,"women's Ulster Day declaration")]),
"s6.5.1":(1,[n("s4.8.4",H,"founding of Cumann na mBan")]),
"s6.5.2":(1,[]),
"s6.5.3":(1,[n("s6.3.1",E,"the Irish Citizen newspaper")]),
"s6.5.4":(1,[]),
"s6.5.5":(1,[n("s6.5.4",H,"women's vote in 1918")]),
"s6.6.b":(1,[]),"s6.6.0":(1,[n("s6.6.b",H,"Intermediate Education Act 1878")]),
"s6.6.1":(1,[n("s6.6.0",E,"Intermediate Board examinations")]),
"s6.6.2":(1,[n("s6.6.1",E,"results fees system")]),
"s6.6.3":(1,[n("s6.6.0",E,"Intermediate examinations open to girls")]),
"s6.6.4":(1,[n("s6.6.1",E,"payment by results")]),
"s6.6.5":(2,[n("s6.6.1",H,"payment by results principle")]),
"s6.6.6":(1,[n("s6.6.5",H,"1900 programme and Irish in schools")]),
"s6.6.7":(1,[]),
"s6.7.b":(1,[]),"s6.7.0":(1,[]),
"s6.7.1":(1,[n("s6.7.0",H,"Catholic grievance over universities")]),
"s6.7.2":(1,[n("s6.7.1",E,"the Royal University")]),
"s6.7.3":(2,[n("s6.7.1",H,"the Royal University being dissolved")]),
"s6.7.4":(1,[n("s6.7.3",E,"the NUI")]),
"s6.7.5":(1,[n("s6.7.3",H,"the NUI and matriculation")]),
"s6.8.b":(1,[]),
"s6.8.0":(2,[n("s6.0.6",H,"women's local government votes"),n("s6.7.2",H,"degree access for women")]),
"s6.8.1":(1,[n("s6.2.4",H,"Home Rule Bills offering women nothing"),n("s6.3.6",H,"militancy dividing opinion")]),
"s6.8.2":(1,[n("s6.6.0",H,"Intermediate system"),n("s6.7.3",H,"1908 Universities Act")]),
"s6.8.3":(1,[n("s6.6.4",E,"payment by results criticism")]),
"s6.8.4":(1,[n("s6.2.3",E,"Irish Party opposing suffrage for Home Rule")]),
"s6.8.5":(2,[n("s6.5.b",H,"national question dividing suffragists")]),
}
txt=open(D+'/packs/hist-ire2-s6.t1g1.txt').read()
tg=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-ire2-s6\.[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tids:
    c,nd=R[t[len(P):]]
    for x in nd: assert x['id'] in allids and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":nd}
assert len(R)==len(tids)==len(out),(len(R),len(tids))
json.dump(out,open(D+'/point-links/hist-ire2-s6.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
