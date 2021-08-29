a=[1,2,3]
b=[4,5,6]

# Cartesian product
# loop only works for compile time (your coding time)
for x in a:
    for y in b:
        print((x,y))

# itertools product
from itertools import product
p=product(a,b) # C
for pp in p:
    print(type(pp),pp)

# why dynamic (sth happen in runtime)
s=[]
s.append(a)
s.append(b)
p=product(*s)
for pp in p:
    print(pp)

#
p=product(a,repeat=6)
for pp in p:
    print(pp)
