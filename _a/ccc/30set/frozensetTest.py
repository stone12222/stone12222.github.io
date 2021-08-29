# element in set must can be hashable
s={100}
s.add(frozenset({1,2,3}))
print(s)

# how we know if element is hashable or not
print(frozenset().__hash__())

"""
frozenset(iterable)
"""
s=frozenset([1,2,3])
print(s)

#
number = {"one": 1, "two": 2, "three": 3}
fSet = frozenset(number)
print(fSet)

#
a={1,2}
b=frozenset({3,4})
c=a.union(b)
print(a)
print(c)

# put frozenset in set, keep unique
a=frozenset({1,2})
b=frozenset({2,1})
c=set()
c.add(a)
c.add(b)
print(c)

# or check if a set in list
l=[]
a={1,2,3}
b={2,1,3}
l.append(a)
print(a in l)
print(b in l)

