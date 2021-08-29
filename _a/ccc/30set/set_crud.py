"""
create, read, update, delete
"""
# create
s=set()
s={1,2}
print(s)

# 1. no position
# 2. no order
s={4,3,2,'a','b'}
print(s)
# 3. no duplicate
s.add('b')
print(s)
s.add('c')
print(s)

# add more / update
s={1,2,3}
s.update([3,4,5,6])
print("s",s)

# delete
s.remove(4)
print(s)
s.discard(5)
print(s)
# s.remove(5)
s.discard(5)
print(s)

# delete random one
for _ in range(1000):
    s1={1,'a','c',2}
    deleted=s1.pop()
    print(deleted)

# delete all
s.clear()


