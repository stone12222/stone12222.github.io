l=[1,2,3,4,5,6]

# consumes more memory
import time
s=time.time()
for i in range(10000):
    ll=[e for e in l if e>=4]
    for e in ll:
        pass
    # print(ll)
e=time.time()
print(e-s)

# speed slow, but save memory
def greaterOrEqual4(e):
    return e>=4

s=time.time()
for i in range(10000):
    ll=filter(greaterOrEqual4,l)
    for e in ll:
        pass
e=time.time()
print(e-s)

# for e in ll:
#     print(e)
