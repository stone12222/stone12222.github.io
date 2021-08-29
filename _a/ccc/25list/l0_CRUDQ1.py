"""
create
"""
l=[]
l=[1,2,3]
l=[1,True,'abc']

l=[1,2,[3,4]]
print(l)

"""
read
"""
# indexing
e=l[1]
print(e)
e=l[-1]
print(e)
print(l[-1][-1])

# slicing
l=[1,2,3,4,5,6]
print(l[1:])
print(l[2:5])
print(l[:4])

# get all
pos=0
for e in l:
    print(pos,e)
    pos+=1

for e in enumerate(l):
    print(e)

# unpack
l=['joan',14,'central']
name,age,school=l

"""
update
"""
l[1]=15
l[2:]=['central','high','school']
print(l)

"""
add
"""
l=[1,2,3]
l.append(4)
l.append([5,6])
print(l)
l.extend([7,8])
print(l)
l.insert(1,100)
print(l)
l[1:1]=['x','y','z']
print(l)

"""
delete
"""
# by position
del l[-3]
# by value
l.remove(100)
print(l)
# delete and get deleted ele
lastone=l.pop()
anyone=l.pop(3)
print(l)
# delete all
l.clear()
print(l)

"""
query
"""
l=[1,2,3]
print(100 not in l)
print(l.index(2))


