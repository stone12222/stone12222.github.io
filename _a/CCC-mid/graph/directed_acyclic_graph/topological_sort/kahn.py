# kahn
g={
    1:[4,7],
    2:[1],
    4:[],
    5:[4],
    6:[2],
    3:[4,5],
    7:[]}

in_degree={node:0 for node in g}
for vs in g.values():
    for v in vs:
        in_degree[v]+=1

#
q=[node for node in g if in_degree[node]==0]

#
result=[]
while q: # when q is not empty
    # 1. get node from queue
    n=q.pop(0)
    # 2. add node to result
    result.append(n)

    for neighbour in g[n]:
        # 3. remove edges
        in_degree[neighbour]-=1
        # 4. add node with in-degree 0 to queue
        if in_degree[neighbour]==0:
            q.append(neighbour)

#
print(result)



