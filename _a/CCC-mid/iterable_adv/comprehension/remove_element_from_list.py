l=[1,1,2,3,4,5,5,6,7,8]

# while True:
#     found=False
#     for n in l:
#         if n==1 or n==5:
#             l.remove(n)
#             found=True
#     if not found:
#        break
# print(l)
#

# l=[1,1,2,3,4,5,5,6,7,8]
# for i in range(len(l)-1,-1,-1):
#     if l[i]==1 or l[i]==5:
#         l.remove(l[i])
# print(l)

#
ll=[]
for n in l:
    if n!=1 and n!=5:
        ll.append(n)
print(ll)

# comprehension
ll=[n for n in l if n!=1 and n!=5]
print(ll)
