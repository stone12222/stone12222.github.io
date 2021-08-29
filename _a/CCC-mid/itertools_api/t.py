a=[1,2]
b=[4,5]
c=[7,8]

'''
1 4
1 5
1 6
2 4
2 5
...
'''
for aa in a:
    for bb in b:
        for cc in c:
            print(aa,bb,cc)

# why use product? we don't need know how many collections
# when we are writing code
from itertools import product
s=[]
s.append(a)
s.append(b)
s.append(c)

p=product(*s)
for pp in p:
    print(pp)

#
'''
1-1-1
 x x
2-2-2
'''
p=product(a,repeat=3)
for pp in p:
    print(pp)


