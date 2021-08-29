graph = {'A': {'B', 'C'},
        'B': {'A', 'D', 'E','C'},
        'C': {'A', 'F','B'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'},
        'G':set()
}
"""
    A
   / \
  B - C
 / \   \
D   E - F G

"""
# loop is natural
def bfs(start,goal):
   # node, path to node
   queue=[[start,[start]]]
   visited={start}

   while queue:
       node,path=queue.pop(0)
       for n in graph[node]:
           if n==goal:
               path.append(n)
               return path
           if n not in visited:
               visited.add(n)
               newPath=path+[n]
               queue.append([n,newPath])

print(bfs('D','C'))


