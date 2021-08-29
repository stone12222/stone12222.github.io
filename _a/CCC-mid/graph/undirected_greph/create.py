"""
1,7
1,4
2,1
3,4
3,5
5,4
6,2
"""

edges=[
    (1,7),
    (1,4),
    (2,1),
    (3,4),
    (3,5),
    (5,4),
    (6,2)]

# def createGraph(edges):
#     graph={}
#
#     for edge in edges:
#         n1,n2=edge
#         if n1 not in graph:
#             graph[n1]={n2}
#         else:
#             graph[n1].add(n2)
#
#         if n2 not in graph:
#             graph[n2]={n1}
#         else:
#             graph[n2].add(n1)
#     return graph

from collections import defaultdict

def createGraph(edges):
    graph=defaultdict(set)
    for edge in edges:
        n1,n2=edge
        graph[n1].add(n2)
        graph[n2].add(n1)

print(createGraph(edges))

