g={
    1:[4,7],
    2:[1],
    4:[],
    5:[4],
    6:[2],
    3:[4,5],
    7:[]}

# step 1
in_degree={node:0 for node in g}
for neighbour in g.values():
    for node in neighbour:
        in_degree[node]+=1
print(in_degree)

# step 2
q=[node for node in in_degree if in_degree[node]==0]

order=[]
while len(q)>0:
    # step 3, pop
    node=q.pop(0)
    order.append(node)

    for neighbour in g[node]:
        # step 4, remove dependencies from node
        in_degree[neighbour]-=1
        # step 5, add free node to queue
        if in_degree[neighbour]==0:
            q.append(neighbour)

print(order)
