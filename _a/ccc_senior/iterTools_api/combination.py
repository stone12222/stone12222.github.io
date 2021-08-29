l = 'abc'

# ab, bc, ac

# static
for i in range(len(l)):
    for j in range(i+1, len(l)):
        print(l[i], l[j])

# dynamic
from itertools import combinations
c = combinations(l,i)
for e in c:
    print(e)