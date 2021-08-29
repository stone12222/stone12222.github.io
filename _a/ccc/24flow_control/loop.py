"""
o:
1 2 3 4 5 6 7 8 9
"""

for e in [1,2,3,4,5,6,7]:
    print('hello world')

for n in range(10):
    print(n,end=' ')
print()

n=1
while n<10:
    print(n,end=' ')
    n+=1
print()

s='abc'
"""
0 a
1 b
2 c
"""
numOfNodes=0
for c in s:
    print(numOfNodes, c)
    numOfNodes+=1

for index,c in enumerate(s):
    print(index,c)
for index,c in enumerate(s,start=100):
    print(c,index)






