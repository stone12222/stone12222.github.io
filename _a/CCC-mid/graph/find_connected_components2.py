#     a
#    / \
#   b   c
#  /   / \
# d   e   f   g   h-i

# adjacency list
graph={
    'A':{'B','C'},
    'B':{'A','D'},
    'C':{'A','E','F'},
    'D':{'B'},
    'E':{'C'},
    'F':{'C'},
    'G':set(),
    'H':{'I'},
    'I':{'H'}
}

#
groups=[]

while graph:
    n=next(iter(graph))
    # bfs
    q=[n]
    visited=[]

    while q:
        node=q.pop(0)
        if node not in visited:
            visited.append(node)
        neighbours=graph[node]
        unvisited_neighbour=neighbours-set(visited)
        q.extend(unvisited_neighbour)
    #
    groups.append(visited)

    #
    for n in visited:
        del graph[n]

print(groups)



