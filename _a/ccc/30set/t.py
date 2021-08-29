# 5 basic operations, data structure such as list
# create, read, update, delete, query

#
s=set()
print(type(s))
print(s)

# no order
s={'Tony',1,'Collin',2}
print(s)
# no position concept
# print(s[0])

# no duplicate elements (unique)
s={1,1,2,2,2}
print(s)

# set like your backpack

# read
for e in s:
    print(e)

# update
s={1,2,3,4}
s.update(['a','b']) # addall
s.update({'a','b','c'})
print(s)
s.add('d')
print(s)

# delete
# for i in range(100):
s={'abc','bob','card','dog'}
e=s.pop() # pop arbitrary element
print(e)
s.remove('abc') # throw error
print(s)
s.discard('bob') # discard is very friendly
print(s)

s.remove('abc') # throw error

# query
print('abc' in s)
print(len(s))

