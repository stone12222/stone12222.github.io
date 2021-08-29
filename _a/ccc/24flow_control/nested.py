"""
i:
3 4

o:
1 2 3 4
1 2 3 4
1 2 3 4
"""
a,b=input().split()
a=int(a)
b=int(b)

for j in range(a):
    for i in range(1,b+1):
        print(i,end=' ')
    print()
