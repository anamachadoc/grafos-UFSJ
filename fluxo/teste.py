d = {}
if 'a' not in d.keys():
    d['a'] = 2
    
if 'a' not in d.keys():
    d['a'] = 3
else:
    d['a'] = d['a'] + 8
    
print(d)