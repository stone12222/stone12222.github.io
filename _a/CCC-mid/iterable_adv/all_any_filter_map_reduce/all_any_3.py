l=[1,2,3,4,5,6]
# all
print(list(e<7 for e in l))
print(all(e<7 for e in l))

# any
print(any(e>6 for e in l))

# filter
def fi1ter(func:callable,l):
    ll=[]
    for i in l:
        if func(i):
            ll.append(i)
    return ll

def largethan3(e):
    return e>3

print(list(filter(largethan3,l)))

# map
def double(e):
    return e*2
print(list(map(double,l)))
print([double(e) for e in l])

ll=lambda e:e*2
print(list(map(ll,l)))

# reduce
def add(a,b):
    return a+b

def reduce(func,b):
    r=0
    for e in b:
        r=func(r,e)
    return r

import functools
print(reduce(add,l))

# why use map?

