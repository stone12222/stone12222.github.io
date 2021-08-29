'''
a weighted graph has n vertices

1 create dist (a n × n array). The minimum distances are set to ∞

2 for each vertex v
3     dist[v][v] ← 0

4 for each edge (u,v)
5     dist[u][v] ← w(u,v)  // the weight of the edge (u,v)

6 for k from 1 to n
7     for i from 1 to n
8         for j from 1 to n
9             if dist[i][j] > dist[i][k] + dist[k][j]
10                dist[i][j] ← dist[i][k] + dist[k][j]
11            end if
'''
graph = {
   1: {3: -2},
   2: {1: 4, 3: 3},
   3: {4: 2},
   4: {2: -1}
}

# warshall
from math import inf
size=len(graph)
# 1
dist=[[inf]*(size+1) for _ in range(size+1)]
# 2
for n in range(1,size+1):
   dist[n][n]=0
# 3
for i in range(1,size+1):
   for j in range(1,size+1):
       if j in graph[i]:
           dist[i][j]=graph[i][j]
# 4 try 1 for every pair of nodes, then try 2, then 3.....
for i in range(1, size + 1):
   for j in range(1, size + 1):
       for k in range(1, size + 1):
           if dist[i][k]+dist[k][j]<dist[i][j]:
               dist[i][j]=dist[i][k]+dist[k][j]
print(*dist, sep='\n')


'''
[inf, inf, inf, inf, inf]
[inf, 0, -1, -2, 0]
[inf, 4, 0, 2, 4]
[inf, 5, 1, 0, 2]
[inf, 3, -1, 1, 0]

[inf, inf, inf, inf, inf]
[inf, 0, inf, -2, 0]
[inf, 4, 0, 2, 4]
[inf, inf, 1, 0, 2]
[inf, 3, -1, 1, 0]

'''