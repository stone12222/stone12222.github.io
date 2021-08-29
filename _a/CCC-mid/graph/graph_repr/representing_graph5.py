# graph: nodes and edges

# 1 way: edges list
# good: easy, bad:slow
g=[
    [1,4],
    [2,1],
    [1,7],
    [6,2],
    [3,4],
    [3,5],
    [5,4]
]
# find if 3 connect to 5
for edge in g:
    if edge==[3,5]:
        print('yes')
        break
else:
    print('no')

# 2 way: adjacent matrix
# good: fast
# bad: more memory
g=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,1],
    [0,1,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
if g[3][5]==1:
    print('yes')
else:
    print('no')

l=[[0]*4]*4
print(l)

# 3 way: adjacent list
# good: faster than edges list, less memory than matrix
g={
    1:{4,7},
    2:{1},
    3:{4,5},
    4:{},
    5:{4},
    6:{2},
    7:{}
}

in_degree={
    1:0+1,
    2:0+1,
    3:0,
    4:1+1+1,
    5:0+1,
    6:0,
    7:0+1
}

for node in g[3]:
    if node==5:
        print('yes')
        break
else:
    print('no')

# out-degree
out_degree={k:len(v) for k,v in g.items()}
print(out_degree)

# in-degree
in_degree={k:0 for k in g}
print(in_degree)

for v in g.values():
    for vv in v:
        in_degree[vv]=in_degree[vv]+1
        print(in_degree)
