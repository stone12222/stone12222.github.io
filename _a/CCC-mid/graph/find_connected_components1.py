#     a
#    / \
#   b   c
#  /   / \
# d   e   f   g   h-i

def connected_components(graph):
    # node=graph.popitem()[0]

    groups=[]
    while graph:
        node=next(iter(graph))

        visited=[]
        q=[node]
        while q:
            n=q.pop(0)
            if n not in visited:
                visited.append(n)
            neighbours=graph[n]
            unvisitedNeighbours=neighbours-set(visited)
            q.extend(unvisitedNeighbours)

        for k in visited:
            del graph[k]

        groups.append(visited)
    return groups

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


# Find all the connected components.
groups = connected_components(graph)
print(groups)


