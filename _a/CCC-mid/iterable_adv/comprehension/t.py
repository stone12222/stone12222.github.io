l=[1,2,3,4,5,6]

#
ll=[]
# for i in range(len(l)):
#     l[i]=l[i]*2

for n in l:
    ll.append(n*2)
print(ll)

# syntax sugar
# comprehension
ll=[n*2 for n in l if n>3]
print(ll)

# 2d
# a=[[1,2,3],[1,2,3],[1,2,3]]
a=[[e for e in range(1,4)] for i in range(3)]
print(a)

# set comprehension
# transform one collection to another
s={n*2 for n in l}
print(s)

# dict comprehension
# a collection of key-value pairs
# 3.7
d={1:100, 2:200}
dd={k:v*10 for k,v in d.items()}
print(dd)