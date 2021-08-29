l=[1,2,3,4]

s=0
for i in l:
    s+=i
print(s)

#
def add(a,b):
    return a+b

from functools import reduce
r=reduce(add,l)
print(r)

# what reduce can do
# reduce convert one collection to a value

# map reduce
# a task map to multiple server
# collect result from servers and combine to one result

# big data
# hadoop: map-reduce

# spark
