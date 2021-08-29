l=[1,2,3,4]

# reduce
def add(a,b):
    return a+b

import functools
print(functools.reduce(add,l,100))
print(functools.reduce(lambda a,b:a+b,l))

# all, any, map, filter, reduce
