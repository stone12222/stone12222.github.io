l=[1,2,2,2,3,4,4,5,6,7]
# for e in l:
#     condition-if-else e==2 or e==4 or e==6:
#         l.remove(e)
#
#         # 1,2,3,4,5,7

for i in range(len(l)-1,-1,-1):
    if l[i]==2 or l[i]==4 or l[i]==6:
        l.remove(l[i])

for o in l:
    print(o)
