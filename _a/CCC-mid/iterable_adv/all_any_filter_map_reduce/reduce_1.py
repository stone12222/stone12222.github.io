#
l=[1,2,3,4]

# add
def add(a,b):
    return a+b

import functools
total=functools.reduce(add,l,100)
print(total)
"""
a -> a1
b -> b1
ab=a1+b1
"""
