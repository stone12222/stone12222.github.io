#     A
#    / \
#   B   C
#  / \   \
# D   E - F G

# breadth first search
# the core part: put nodes and its neighbours into the queue
# the goal is processing nodes by levels
def bfs(start):
    queue=[start]
    visited={start}

    while queue:
        node=queue.pop(0)
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited

graph={
    'A':{'B','C'},
    'B':{'A','D','E'},
    'C':{'A','F'},
    'D':{'B'},
    'E':{'B','F'},
    'F':{'C','E'},
    'G':{}
}

print(bfs('B'))
