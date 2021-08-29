# 0, 0.5, 1, 1.5 ....
def newrange(s,e,step):
    while s<e:
        yield s
        s+=step

#
g=newrange(0,3,0.5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for i in newrange(0,3,0.5):
    print(i)

"""
how for loop works:
1. get iterator
2. keep call next(iterator) and save to i
3. handle StopIterator exception 
"""


