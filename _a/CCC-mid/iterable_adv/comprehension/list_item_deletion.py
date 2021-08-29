l=[1,2,3,3,4,4,5,6,7,8]

#
# l=[1,2,5,6,7,8]

#
# for e in l:
#     if e==3 or e==4:
#         l.remove(e)
# print(l)

#
# l1=[]
# for e in l:
#     if e!=3 and e!=4:
#         l1.append(e)
# l=l1
# print(l)

# jennifer
# for i in range(len(l)-1,-1,-1):
#     if l[i]==3 or l[i]==4:
#         del l[i]
# print(l)

# comprehension
print([e for e in l if e!=3 or e!=4])
