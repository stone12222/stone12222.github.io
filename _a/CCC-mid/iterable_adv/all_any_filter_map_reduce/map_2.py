# map
# transfer 1 collection to another

#
l=[1,2,3]
l1=[e*2 for e in l]

#
def double(n):
    return n*2
print(list(map(double, l)))

# why map: save memory because lazy mode
ll=map(double,l)
for e in ll:
    print(e)
for e in ll: # print nothing
    print(e)
