import json,re,sys
B='/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
for b in ['batch-01','batch-18']:
    for blk in open(B+'batches/%s.txt'%b).read().split('='*40):
        m=re.search(r'QUESTION (\S+)',blk)
        if not m: continue
        q=m.group(1); d=json.load(open(B+'out/%s.json'%q))
        parts=re.findall(r'PART "([^"]*)" \((\d+) marks',blk)
        ids=set(re.findall(r'^\[([^\]]+)\]',blk,re.M))
        assert list(d)==[p for p,_ in parts],(q,list(d))
        for p,mk in parts:
            assert len(d[p])<=max(int(mk)//2,1) or not d[p] ,(q,p,len(d[p]),mk)
            for x in d[p]: assert 1<=x['k']<=len(x['of']) and set(x['of'])<=ids,(q,p,x)
print('ok')
