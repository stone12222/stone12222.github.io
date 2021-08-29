# 1,7
# 1,4
# 2,1
# 3,4
# 3,5
# 5,4
# 6,2

# adjacent list
g={1:[4,7],
    2:[1],
    3:[4,5],
    4:[],
    5:[4],
    6:[2],
    7:[]}

#
in_degree={k:0 for k in g}
for node,neighbour in g.items():
    for n in neighbour:
        in_degree[n]+=1
print(in_degree)

#
for neighbour in g.values():
    for n in neighbour:
        in_degree[n]+=1
print(in_degree)

#
out_degree={k:0 for k in g}
for node,neighbour in g.items():
    out_degree[node]=len(neighbour)
print(out_degree)
#
out_degree = {n:len(v) for n, v in g.items()}

print(out_degree)

