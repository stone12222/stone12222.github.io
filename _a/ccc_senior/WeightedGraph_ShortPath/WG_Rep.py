 # version 1
graph1 = [
   [1, 3, -2],
   [2, 1, 4],
   [4, 2, -1],
   [3, 4, 2],
   [2, 3, 3]
]

# version 2
from math import inf

graph2 = [
   [0, inf, -2, inf],
   [4, 0, 3, inf],
   [inf, inf, 0, 2],
   [inf, -1, inf, 0]
]

print(' ',*range(1,len(graph2)+1))
for i in range(1,len(graph2)+1):
   print(i,end=' ')
   for v in graph2[i-1]:
       if v==inf:
           print('_',end=' ')
       else:
           print(v,end=' ')
   print()


# version 3
# adjacency list
graph = {
   1: {3: -2},
   2: {1: 4, 3: 3},
   3: {4: 2},
   4: {2: -1}
}

print(' ',*range(1,len(graph)+1))

for i in range(1,len(graph)+1):
   print(i,end=' ')
   for j in range(1,len(graph)+1):
       if i==j:
           print(0,end=' ')
       elif j in graph[i]:
           print(graph[i][j],end=' ')
       else:
           print('_',end=' ')
   print()




