"""
what can be used as key?
list? no
set? no
frozenset? yes

how to check if an object o is hashable?
o has __hash__()
or
print(o.__hash__)
or
use hash(o) to test
"""

"""
what is hash?
convert one value to hashcode
"""
l=[1,2]

s=frozenset([1,2,3])

d={}
# d[l]='2 numbers'
d[s]='3 numbers'
print(d)
