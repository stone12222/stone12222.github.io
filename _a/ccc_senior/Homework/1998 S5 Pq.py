import heapq
moves=[(1,0),(-1,0),(0,1),(0,-1)]
from math import inf
def bfs(goal):
   q=[]
   heapq.heappush(q,(0,(0,0)))
   visited={(0,0)}
   oxygen_table = {goal:inf}

   while q:
       curr_oxygen,node=heapq.heappop(q)
       r, c = node
       if node not in visited:
           visited.add(node)
       #
       for dr,dc in moves:
           nr=dr+r
           nc=dc+c
           curr_elevation=mountain[r][c]
           if 0<=nr<size and 0<=nc<size:
               neighbour_elevation = mountain[nr][nc]
               if abs(neighbour_elevation-curr_elevation)<=2:
                   if neighbour_elevation>startElevation or curr_elevation>startElevation:
                       newOxygen=curr_oxygen+1
                   else:
                       newOxygen=curr_oxygen

                   if (nr,nc)==goal:
                       if oxygen_table[(nr,nc)]>newOxygen:
                           oxygen_table[(nr,nc)]=newOxygen

                   if (nr,nc) not in visited:
                       heapq.heappush(q,(newOxygen,(nr,nc)))
   if oxygen_table[goal]!=inf:
       return oxygen_table[goal]
   return None

n=int(input())

for _ in range(n):
   size=int(input())
   #
   mountain=[]
   for i in range(size):
       r=[]
       for j in range(size):
           r.append(int(input()))
       mountain.append(r)
   #
   startElevation=mountain[0][0]
   oxygen=bfs((size-1,size-1))
   if oxygen:
       print(oxygen)
   else:
       print('CANNOT MAKE THE TRIP')


