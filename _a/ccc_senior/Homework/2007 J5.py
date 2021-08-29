def findneighbor(node):
   neighbors=[]
   ma=node+maxD
   mi=node+minD
   for m in motels:
      if mi<=m<=ma:
        neighbors.append(m)
   return neighbors
def bfs(start, goal):
   count = 0
   q = [start]
   while q:
       node = q.pop(0)
       for n in findneighbor(node):
           if n == goal:
               count += 1
           else:
               q.append(n)

   return count


motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
minD = int(input())
maxD = int(input())

n = int(input())
for _ in range(n):
   motels.append(int(input()))
motels.sort()

#
count = bfs(0, 7000)
print(count)



