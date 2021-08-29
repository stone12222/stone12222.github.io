#     a
#    / \
#   b   c
#  /   / \
# d   e   f   g   h-i

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

def connected_components(graph):
    result = []
    while graph:
        start = next(iter(graph.keys()))

        # find connected components and save into group
        group = set()
        queue = [start]
        while queue:
            n = queue.pop(0)

            if n not in group:
                group.add(n)
                neighbors = graph[n]
                neighbors.difference_update(group)
                queue.extend(neighbors)

        # Remove the remaining nodes from the graph
        for node in group:
            del graph[node]

        # Add the group
        result.append(group)
    return result


# Find all the connected components.
groups = connected_components(graph)
for group in groups:
    nodes = sorted(node for node in group)
    print(nodes)

# ['g']
# ['a', 'b', 'c', 'd', 'e', 'f']
# ['h', 'i']
