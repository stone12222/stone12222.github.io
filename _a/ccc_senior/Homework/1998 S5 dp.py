moves=[(1,0),(-1,0),(0,-1),(0,1)]

def dp(start):
   record=[[inf]*(size+1) for _ in range(size+1)]
   # p(record)
   record[1][1]=0

   #
   q=[start]
   while q:
       r,c=q.pop(0)
       for dr,dc in moves:
           nr=dr+r
           nc=dc+c
           curr_elevation=mountain[r][c]
           if 1<=nr<=size and 1<=nc<=size:
               neighbour_elevation = mountain[nr][nc]
               if abs(neighbour_elevation-curr_elevation)<=2:
                   if neighbour_elevation>startElevation or curr_elevation>startElevation:
                       neighbour_oxygen=record[r][c]+1
                   else:
                       neighbour_oxygen=record[r][c]

                   if neighbour_oxygen<record[nr][nc]:
                       record[nr][nc]=neighbour_oxygen
                       q.append((nr,nc))

   # p(record)
   return record[size][size]

def p(g):
   print(*g,sep='\n')

n = int(input())

from math import inf

for i in range(n):
   size = int(input())
   #
   mountain = [[inf] * (size + 1)]
   for j in range(size):
       r = [inf]
       for k in range(size):
           r.append(int(input()))
       mountain.append(r)
   #
   # p(mountain)
   startElevation=mountain[1][1]
   record = dp((1, 1))
   if record!= inf:
       print(record)
   else:
       print('CANNOT MAKE THE TRIP')
