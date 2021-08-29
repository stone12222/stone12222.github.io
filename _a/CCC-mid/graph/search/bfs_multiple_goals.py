#     A
#    / \
#   B   C
#  / \   \
# D   E - F G

# def bfs(start):
#     queue=[start]
#     visited={start}
#
#     while queue:
#         node=queue.pop(0)
#         for n in graph[node]:
#             if n not in visited:
#                 visited.add(n)
#                 queue.append(n)
#     return visited

graph={
    'A':{'B','C'},
    'B':{'A','D','E'},
    'C':{'A','F'},
    'D':{'B'},
    'E':{'B','F'},
    'F':{'C','E'},
    'G':{}
}

print(bfs('A',('B','E')))
