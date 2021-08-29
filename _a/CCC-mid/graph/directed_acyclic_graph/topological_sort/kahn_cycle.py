g={
    1:[4,7],
    2:[1],
    4:[3],
    5:[4],
    6:[2],
    3:[5],
    7:[]}

in_degree={node:0 for node in g}
for neighbour in g.values():
    for node in neighbour:
        in_degree[node]+=1
print(in_degree)

# step 2
q=[node for node in in_degree if in_degree[node]==0]

# step 3
result=[]
while q:
    node=q.pop(0)
    result.append(node)

    for neighbour in g[node]:
        # step 4
        in_degree[neighbour]-=1
        # step 5
        if in_degree[neighbour]==0:
            q.append(neighbour)

if len(result)==len(g):
    print(result)
else:
    print('there is circle, but partial order is',result)


