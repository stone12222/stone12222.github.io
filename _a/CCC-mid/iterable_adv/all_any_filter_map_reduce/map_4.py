# l=[1,2,3]

# for i in range(len(l)):
#     l[i]=l[i]*2
# print(l)

# ll=[]
# for i in range(len(l)):
#     ll.append(l[i]*2)
# print(ll)

#
# def double(e):
#     return e*2
#
# l=[1,2,3]
# m=map(double,l)
# for num in m:
#     print(num)

# map vs comprehension
# save memory

# 1 2 3
a,b,c=map(int,input().split())
print(a+b+c)

# what map can do
# map transform one collection to another