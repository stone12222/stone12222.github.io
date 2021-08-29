'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9
'''
import sys

r = int(input())
c = int(input())

room = []

for i in range(r):
    room.append(input().split())

graph = {}

def findNb(num,room):
    divisors = []
    ret = []
    for i in range(1,num+1):
        if num%i == 0:
            divisors.append(i)
            divisors.append(num//i)
        if len(divisors) == 2:
            try:
                ret.append(room[divisors[0]-1][divisors[1]-1])
            except:
                None
            divisors.clear()
    return ret

for i in range(r):
    for j in range(c):
        graph[room[i][j]] = findNb(int(room[i][j]),room)

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  ret = []

  while queue:
    s = queue.pop(0)
    ret.append(s)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return ret

visited = []
queue = []

bfsed = bfs(visited, graph, room[0][0])

if room[0][0] == '1':
    print('no')
    sys.exit()

if room[r-1][c-1] in bfsed:
    print('yes')
else:
    print('no')