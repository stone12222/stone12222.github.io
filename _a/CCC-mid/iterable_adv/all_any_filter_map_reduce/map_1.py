# map
# transfer 1 collection to another

#
l=[1,2,3]
l1=[e*2 for e in l]

#
def double(n):
    print(n)
    return n*2

r=map(double,l)
print(list(r))
r=map(double,l)
for e in r:
    print(e)
"""
map vs comprehension
1. map function can do more work
2. map save memory
3. map can reuse existing function
"""
l=[1,2,3]
ll=[str(e) for e in l]
ll=map(str,l)


