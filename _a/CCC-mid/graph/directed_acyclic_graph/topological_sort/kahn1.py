# kahn
g={
    1:[4,7],
    2:[1],
    4:[],
    5:[4],
    6:[2],
    3:[4,5],
    7:[]}

in_degree={k:0 for k in g}

for v in g.values():
    for vv in v:
        in_degree[vv]+=1
print(in_degree)

q=[]
for k,v in in_degree.items():
    if v==0:
        q.append(k)
print(q)

result=[]
while len(q)>0:
    # pop first one from queue and save it to result
    node=q.pop(0)
    result.append(node)

    # remove dependency for neighbours
    for neighbour in g[node]:
        in_degree[neighbour]-=1
        # add node with in-degree 0 to the queue
        if in_degree[neighbour]==0:
            q.append(neighbour)

print(result)





