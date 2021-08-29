a=[1,2,3]
b=[4,5,6]

# cartesian product
for aa in a:
    for bb in b:
        print(aa,bb)

#
from itertools import product
p=product(a,b)
for item in p:
    print(*item)

#
s=[[1,2],[3,4]]

p=product(*s)
for item in p:
    print(item)

#
s=[1,2,3]
p=product(s,repeat=6)
for item in p:
    print(item)