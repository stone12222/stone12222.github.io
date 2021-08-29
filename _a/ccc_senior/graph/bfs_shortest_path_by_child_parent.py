graph = {'A': {'B', 'C'},
        'B': {'A', 'D', 'E','C'},
        'C': {'A', 'F','B'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'},
        'G':set()
}
# Machine learning is branch of AI
"""
    A
   / \
  B - C
 / \   \
D   E - F G

"""
# loop is natural
def bfs(start,goal):
   parentMap={start:None}
   if start==goal:
       return parentMap
   # node, path to node
   queue=[start]
   visited={start}

   while queue:
       node=queue.pop(0)
       for n in graph[node]:
           if n==goal:
               parentMap[n]=node
               return parentMap

           if n not in visited:
               visited.add(n)
               queue.append(n)
               parentMap[n]=node

goal='D'
map=(bfs('A',goal))
node=goal


path=[goal]
while True:
   p=map[node]
   if p==None:
       break
   path.insert(0,p)
   node=p

print(path)





