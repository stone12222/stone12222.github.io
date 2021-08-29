# 1 way
def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

random.sort(key=takeSecond)
print(random)

# 2 way
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=lambda e:e[1])
print(random)

# 3 way
from operator import itemgetter
f=itemgetter(1) # return callable
c=f('ABCDEFG') # call callable
print(c)
# =
print(itemgetter(1)('ABCDEFG'))

print(itemgetter(1,3,5)('ABCDEFG'))

#
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=itemgetter(1))
print(random)

# compare with lambda, operator is faster

