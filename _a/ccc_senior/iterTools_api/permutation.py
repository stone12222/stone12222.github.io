#product

a = [1,2,3]
b = [4,5,6]

for i in a:
    for j in b:
        print(a,b)

#
from itertools import product
s = []

for i in range(7//3):
    l = [2*i+1, 2*i+2, 2*i+3]
    s.append(l)

p = product(*s)

for e in p:
    print(e)

#
l = [1,2,3]
p = product(l,repeat = 3)

for i, aa in enumerate(l):
    for j, bb in enumerate(l):
        for k, cc in enumerate(l):
            if i != j and j != k and i!= k:
                print(aa,bb,cc)

print('#')
from itertools import permutations
permutations(l,3)
for i in p:
    print(i)