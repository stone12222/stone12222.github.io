'''
number, string, boolean, list, set, tuple, dictionary

5 operations:
Create, Read, Update, Delete, Query (CRUDQ)
'''

# create
a={}
print(type(a))
a={
    'a':100,
    'b':200,
    'c':300
   }
# dictionary is a collection of key-value pairs

# read
print(a['a'])
l=[1,2,3]
print(l[1])

print(a.keys())
print(a.values())

#  delete
del a['a']
# a.pop('a')

# query
print('a' in a)

# copy
aa=dict(a)
print(aa)
print(id(aa))
print(a)
print(id(a))

# zip
l=[1,2,3]
ll=['a','b','c']
d=dict(zip(l,ll))
print(d)

# what data type can be used as key
# as long as they are immutable (hashable)
# such as number, boolean, string, tuple
a[(1,2,3)]=1000

# how to know if a data type is hashable
# use hash(...)

