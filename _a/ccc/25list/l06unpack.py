# In Python, the * character is not only used for multiplication and replication,
# but also for unpacking
l=[1,2,3]
print(l)
print(*l)

# easy to print nested list
print()
l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for r in l:
    for c in r:
        print(c,end=' ')
    print()
# by unpack operator *
for r in l:
    print(*r)

# unpack any iterable
print(*"abc")
print(*(1,2,3))



