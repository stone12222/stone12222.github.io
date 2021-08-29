"""
4 5

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
"""

# 1 (not work)
rows=4
cols=5
g=[[0]*cols]*rows

g[0][0]=100
for row in g:
    print(id(row))
    print(row)

# 2 (work)
g=[[0]*cols for r in range(rows)]
g[0][0]=100
for r in g:
    print(r)
