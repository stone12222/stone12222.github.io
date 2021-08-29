"""
i:
3
6

o:
1 2 3 4
1 2 3 4
1 2 3 4
"""
# i=int(input())
# j=int(input())
#
# for r in range(i):
#     for c in range(1,j+1):
#         print(c, end=' ')
#     print()

n=int(input())
m=int(input())
n1=1
m1=1

while n1<=n:
    while m1<=m:
        print(m1,end=' ')
        m1+=1
    m1=1
    print()
    n1+=1

# 2 ways
# top-down, bottom-up
