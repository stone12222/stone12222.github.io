def add(a,b):
    return a+b

add1=lambda a,b:a+b

import time

s=time.time()
for i in range(1000000):
    add1(100,200)
e=time.time()
print('for lambda',e-s)

s=time.time()
for i in range(1000000):
    add(100,200)
e=time.time()
print('for function',e-s)

# lambda and function same speed

