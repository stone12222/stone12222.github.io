def findneighbor(node):
   neighbors = []
   ma = node + maxD
   mi = node + minD
   for m in motels:
       if mi <= m <= ma:
           neighbors.append(m)
   return neighbors

knowledge={}
def dfs(start, goal):
   if start in knowledge:
       return knowledge[start]

   if start == goal:
       return 1
   count = 0
   for n in findneighbor(start):
       count += dfs(n, goal)
   knowledge[start]=count
   return count


# count = 0
# def dfs(start, goal):
#     global count
#     if start == goal:
#         count += 1
#     for n in findneighbor(start):
#         dfs(n,goal)

motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
minD = int(input())
maxD = int(input())

n = int(input())
for _ in range(n):
   motels.append(int(input()))
motels.sort()

#
count = dfs(0,7000)
print(count)


