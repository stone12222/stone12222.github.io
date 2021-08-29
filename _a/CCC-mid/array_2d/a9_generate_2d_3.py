'''
i:
3 4

o:
[
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
]
'''
a,b=input().split()
a=int(a)
b=int(b)

# a,b=[int(x) for x in input().split()]

L=[]
for j in range(a):
    l=[]
    for i in range(b):
        l.append(0)
    L.append(l)
print(L)

#
LL=[]
for j in range(a):
    l=[0]*b
    LL.append(l)
print(LL)

#
LL=[[0]*b for i in range(a)]
print(LL)

# for read is ok, not for write
LLL=[[0]*b]*a
# for l in LLL:
#     print(id(l))

# LLL[0][0]=100
# print(LLL)
