d = {'a': 100,
     'b': 200,
     'c': 300
     }

for k in d:
     print(k)

print(d.keys())

for v in d.values():
     print(v)

for ki, k in enumerate(d):
     print(ki,k)

for item in d.items():
     print(item)

"""
a -> 100
b -> 200
c -> 300
"""

for k,v in d.items():
     print(k,'->',v)
