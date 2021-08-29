def add(a,b):
    return a+b

print(add(100,200))

# syntax sugar
# anonymous function
# a function without name
l=lambda a,b:a+b
print(l(100,200))

#
from functools import reduce
l=[1,2,3]
print(reduce(lambda a,b:a+b,l))

