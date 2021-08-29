#     A
#  1 / \5
#   B   C
# 2/ \5  \8
# D   E - F
#       1
import heapq
import math

graph = {
    'A': {'B':1, 'C':5},
    'B': {'A':1, 'D':2, 'E':5},
    'C': {'A':5, 'F':8},
    'D': {'B':2},
    'E': {'B':5, 'F':1},
    'F': {'C':1, 'E':1},
}
def get_distance(s):
    distance={s:0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex]=math.inf
    return distance

def dijkstra(s):
    parent={s:None}
    distance=get_distance(s)
    seen=set(s)
    q=[]
    heapq.heappush(q,(0,s))
    while q:
        dis,vertex = heapq.heappop(q)
        node=graph[vertex]
        seen.add(vertex)
        for w in node:
            if w not in seen:
                if graph[vertex][w]+dis<distance[w]:
                    heapq.heappush(q,(dis+graph[vertex][w],w))
                    parent[w]=vertex
                    distance[w]=dis+graph[vertex][w]
    return parent

parent=dijkstra('A')
vertex='F'
path=[]
while vertex:
    path.append(vertex)
    vertex=parent[vertex]
print(*reversed(path),sep="->")