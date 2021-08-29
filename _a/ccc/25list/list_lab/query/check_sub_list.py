"""
given 2 list:
i:
4 1 2 3
1 2 3 5 6

o:
YES if the first list has a longest sublist in the second list
"""

a = input().split()
# b = input().split()

# how to get all sublist from a list
# a=[4,1,2,3]
# [4],[4,1],[4,1,2],[4,1,2,3],[1],[1,2] ......
for x in range(len(a)):
    for i in range(x,len(a)):
        print(a[x:i+1])
