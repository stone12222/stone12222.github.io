l=[1,2,3,4,5,6]

import time
s=time.time()
for i in range(1000000):
    c=[e*2 for e in l]
end=time.time()
print(end-s)

s=time.time()
for i in range(1000000):
    c=map(lambda e:e*2,l)
end=time.time()
print(end-s)
