#
l=[1,0,2,3,4,5,6,7]

# for i in range(len(l)):
#     if l[i]>0:
#         print('good')
#     else:
#         print('bad')

# a=[]
counter=0
for i in l:
    if i>0:
        counter+=1
if counter==len(l):
    print('all larger than 0')
else:
    print('not all larger than 0')

#
result=True
for i in l:
    if i<=0:
        result=False
print(result)

# all is check if all elements are True in a collection
result=all([True,True])
print(result)

#
l=[1,0,2,3,4,5,6,7,-1]
result=all(e>0 for e in l)
print(result)

# any
l=[1,0,2,3]
p=list(e>0 for e in l)
print(p)
result=any(p)
print(result)

#
def larger_than_2(e):
    return e>2

l=[1,2,3,4,5]
ll=filter(larger_than_2,l)
print(list(ll))

