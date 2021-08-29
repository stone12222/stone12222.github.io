l=[1,2,3]

# update
l[2]=300
print(l)

# add
l.append(400)
print(l)

l.insert(1,500)
print(l)

# delete
del l[-1]
e=l.pop()
print(l)
print(l.pop(1))
l.clear()

#
l=['a','b','c']
print('c' in l)