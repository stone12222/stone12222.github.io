# reduce
# aggregate many elements to one
def add(x,y):
    return x+y

import functools
total=functools.reduce(add,[1,2,3])
print(total)

# add initializer
total=functools.reduce(add,[1,2,3], 100)
print(total)
