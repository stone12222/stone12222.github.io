graph = {'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B','F'},
        'F': {'C','E'}
        }
"""
      A
     / \
    B   C
   / \   \
  D   E - F
"""

def dfs(start):
   s=[start]
   visited=[start]
   while s:
       node=s.pop()
       if node not in visited:
           visited.append(node)

       for n in graph[node]:
           if n not in visited:
               s.append(n)
   return visited

print(dfs('A'))

def dfs_recursion(start,visited):
   print('visit',start)
   visited.append(start)

   for n in graph[start]:
       if n not in visited:
           dfs_recursion(n,visited)
   print('return',start)


v=[]
dfs_recursion('A',v)
print(v)



