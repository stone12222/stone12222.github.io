# double ended queue
from collections import deque

import time
s=time.time()
l=[]
for i in range(1000000):
    l.append(i)
    l.pop()
e=time.time()
print(e-s)

q=deque()
s=time.time()
for i in range(1000000):
    q.append(i)
    q.pop()
e=time.time()
print(e-s)
