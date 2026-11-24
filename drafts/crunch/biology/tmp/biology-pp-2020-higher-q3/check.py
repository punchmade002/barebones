import json, re, sys
pkg_path, out_path = sys.argv[1], sys.argv[2]
text = open(pkg_path, encoding='utf-8').read()
ids = set(re.findall(r'^\[([A-Za-z0-9.\-]+)\] ', text, re.M))
labels = re.findall(r'^PART (\(.+?\)(?:\(.+?\))*) \(\d+ marks\)', text, re.M)
data = json.load(open(out_path, encoding='utf-8'))
assert list(data.keys()) == labels, ('labels mismatch', list(data.keys()), labels)
total = 0; empty = []
for lab, mps in data.items():
    assert isinstance(mps, list), lab
    if not mps: empty.append(lab)
    for mp in mps:
        assert set(mp.keys()) == {'k', 'of'}, (lab, mp)
        of = mp['of']
        assert isinstance(of, list) and of, (lab, mp)
        assert 1 <= mp['k'] <= len(of), (lab, mp)
        for i in of:
            assert i in ids, ('unknown id', lab, i)
        total += 1
print('OK parts=%d marking_points=%d empty=%s' % (len(labels), total, empty))
