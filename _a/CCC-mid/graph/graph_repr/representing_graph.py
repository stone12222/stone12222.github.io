# look at Floyd-Warshall2-transitive-closure.png

# 1st (edges list)
# check if an edge exist? search through list
# find neighbor? g_2[2]
# small space, low speed
g=[
[1,7],
[1,4],
[2,1],
[3,4],
[3,5],
[5,4],
[6,2]
]
for e in g:
    if e==[6,2]:
        print('has edge')

# 2nd: adjacency matrices
# check if an edge exist? g[2][6]
# big space, fast speed
g=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,1],
    [0,1,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

if g[3][4]:
    print('has edge from 3 to 4')

# adjacency lists
# if exist an edge (i,j)? g[i], then search a list
# find neighbour? g[i]
# small space, fast speed

g={
    1:[4,7],
    2:[1],
    3:[4,5],
    4:[],
    5:[4],
    6:[2],
    7:[]
   }

if g[3]:
    if 4 in g[3]:
        print('edge')
