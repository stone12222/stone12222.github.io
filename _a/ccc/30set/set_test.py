s=set()
s={100,2,3,'joe','a'}
print(type(s))

# crudq

# no order (no position)
for e in s:
    print(e)

# unique
# update
s.add(500)
print(s)
s.add(500)
print(s)

s.update((1,2))
print(s)

# delete
s.remove(3)
print(s)
s.discard(3)
print(s)
# s.remove(3)
# print(s)

#
s.clear()

# set theory
a={1,2,3}
b={2,3,4}
c=a&b
print(c)
c=a|b
print(c)
c=a-b
print(c)
c=a^b
c=(a-b)|(b-a)
print(c)

a={1,2}
b={1,2,3}
# a is subset of b
# b is superset of a
print(a<b)

# query
print('a' in s)

#
l=[1,2,3]
s=set(l)
print(s)
print(set('abc'))

#
print(list(s))

#




