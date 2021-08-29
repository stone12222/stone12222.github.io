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

# from A, visit every thing
def dfs1(start, visited):
   if start not in visited:
       visited.append(start)

   for n in graph[start]:
       if n not in visited:
           dfs1(n, visited)

import time

v=[]
def dfs2(start):
   if start not in v:
       v.append(start)

   for n in graph[start]:
       if n not in v:
           dfs2(n)

# use global list
s=time.process_time()
for i in range(1000000):
   dfs2('A')
e=time.process_time()
print('global',e-s)

# not use global list, use parameter
s=time.process_time()
visited=[]
for i in range(1000000):
   dfs1('A', visited)
   # print(visited)
e=time.process_time()
print('parame',e-s)
