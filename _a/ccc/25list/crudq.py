'''
5 operations:
create, read, update, delete, query
'''
l=[]
result=type(l)
print(result)

l=['a','b','c',['d','e']]
print(l)

ll=[['#','D','#'],
   ['#','.','#']]

# read (indexing)
print(l[3])
print(l[-1])
print(l[0])

print(l[-1][0])

# slicing
print(l[0:3])
print(l[:3])
print(l[1:])
print(l[:])

# loop
# s=input() # abc
# l=list(s)
for e in l:
   print(e)

# query
print('a' not in l)


#
l=[100,200,300]
a,b,c=l
print(a)
print(l)

# update
l[1]=2
print(l)
l[2:]=['z','madhu','+']
print(l)

# add
l=['a','b']
l.append('c')
print(l)
l.append(['d','e'])
print(l)
# ['a','b','c','d','e']
l.extend(['d','e'])
print(l)
l.insert(2,100)
print(l)
# insert multiple
l[2:2]=[800,900]
print(l)

# delete
# by position
del l[-1]
del l[-1]
print(l)
# by value
l.remove(100)
print(l)
#
v=l.pop()
print(l)
print(v)
l.pop(1)
print(l)

#
l.clear()
print(l)

#
l=[100,200,300]
print(l.index(300))