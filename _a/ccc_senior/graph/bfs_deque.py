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

# loop is natural
def bfs_list(start):
   queue=[start]
   visited={start}

   while queue:
       node=queue.pop(0)
       for n in graph[node]:
           if n not in visited:
               visited.add(n)
               queue.append(n)
   return visited

from collections import deque
def bfs_deque(start):
   queue=deque()
   queue.append(start)
   visited={start}

   while queue:
       node=queue.popleft()
       for n in graph[node]:
           if n not in visited:
               visited.add(n)
               queue.append(n)
   return visited

import time
# use deque
s=time.process_time()
for i in range(1000000):
   bfs_deque('A')
e=time.process_time()
print('use dequ',e-s)

# use list
s=time.process_time()
for i in range(1000000):
   bfs_list('A')
e=time.process_time()
print('use list',e-s)


