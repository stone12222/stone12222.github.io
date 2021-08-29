# tuple is a list, but unchangable list

# immutable (cannot change)
# mutable (can change)
# CRUD: create, read
abc=()
abc=(1,2,3)
print(type(abc))
abc=(1,)

abc=1,
abc=1,2,3
print(type(abc))

print(abc[0])
#
# abc[0]=100

# query
print(2 in abc)

# unpack
t='a','b'
a,b=t
print(a)
print(b)

#
t=(4,5,2,7,1)
print(sorted(t))
