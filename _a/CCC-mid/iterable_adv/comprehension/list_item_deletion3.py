l=[1,2,3,3,4,4,6,7,8]

# luke
while 3 in l:
    l.remove(3)
while 4 in l:
    l.remove(4)

#
l=[1,2,3,3,4,4,6,7,8]
l=[1,2,3,4,4,6,7,8]
for e in l:
    if e==3 or e==4:
        l.remove(e)
print(l)

#
l=[1,2,3,3,4,4,6,7,8]
for i in range(len(l)-1,-1,-1):
    if l[i]==3 or l[i]==4:
        del l[i]
print(l)

#
l=[1,2,3,3,4,4,6,7,8]
s1=set(l)
s2={3,4}
print(list(s1-s2))

#
ll=[]
for e in l:
    if e!=3 and e!=4:
        ll.append(e)
print(ll)

# comprehension: convert a collection to another
ll=[e for e in l if e!=3 and e!=4]
