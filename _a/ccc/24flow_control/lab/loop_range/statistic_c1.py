"""
i:
how many numbers you have: 4
number 0: 1
number 1: 2
number 2: 3
number 3: 4random.choice(['ben','alan','andrew'])


o:
sum is: 10.0
largest:  4.0
smallest:  1.0
average: 2.5
range: 3.0
"""

import math
i=int(input())

sum=0
largest=-math.inf
smallest=float('inf')

for _ in range(i):
    n=float(input())
    sum+=n

    if largest<n:
        largest=n

    if smallest>n:
       smallest=n

print('sum:',sum)
print('largest:',largest)
print('smallest:',smallest)
print('average:',sum/i)
print('range:',largest-smallest)
