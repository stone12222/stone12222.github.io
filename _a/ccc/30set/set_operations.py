"""
query
"""
s={1,2,3}
print(2 in s)
print(2 not in s)

"""
set operations
"""
s1={1,2,3}
s2={2,3,4}

# union
s3=s1|s2
print(s3)
# intersection
print(s1&s2)
# difference
print(s1-s2)
print(s2-s1)
# symmetric difference, exclusive or
s1={1,2,3}
s2={2,3,4}
print(s1^s2)
# subset, superset
s1={1,2}
s2={1,2,3,4}
print(s1<=s2)
print(s1.issubset(s2))
print(s2.issuperset(s1))

# disjoint
print({1,2,3}.isdisjoint({5,6}))

# difference_update
s={1,2,3}
s.difference_update({1,3,4})
print('s',s)


