a={1,2,3}
b={2,3,4}

# union
c=a|b
c=a.union(b)
print(c)

# intersection
c=a&b
print(c)

# difference
# select elements in a which are not in b
print(a-b)
print(b-a)

# symmetric difference
print(a^b)

#
a={1,2,3} #set()
b={1,2,3}
print(a<=b)
print(b>=a)