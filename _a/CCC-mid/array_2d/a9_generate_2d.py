"""
4 5

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
"""

# 1
rows=4
cols=5

g=[]
n=1
for r in range(rows):
    row=[]
    for c in range(cols):
        row.append(n)
        n+= 1
    g.append(row)

for r in g:
    print(*r)

# 2
g=[]
l = []
for i in range(1,rows*cols+1):
    l.append(i)
    if i%cols==0:
        g.append(l)
        l = []

for row in g:
    print(row)


# 3
def increment():
    global n
    n+=1
    return n

n=5
g=[[increment() for r in range(10)] for c in range(10)]
for r in g:
    print(r)

#
n=1
f=lambda :n+1
g=[[f() for r in range(10)] for c in range(10)]
for r in g:
    print(r)


