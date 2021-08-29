moves=[(-1,0),(1,0),(0,1),(0,-1)]
def getNeighbours(node):
   r,c=node
   for dr,dc in moves:
       nr=r+dr
       nc=c+dc

       currElevation=mountain[r][c]
       if 0<=nr<size and 0<=nc<size:
           neighbourElevation = mountain[nr][nc]
           if abs(currElevation-neighbourElevation)<=2:
               yield nr,nc

def bfs(start,goal):
   q=[[start]]

   while q:
       path=q.pop(0)
       node=path[-1]

       for n in getNeighbours(node):
           if n==goal:
               return path+[n]
           else:
               if n not in path:
                   q.append(path+[n])


n=int(input())

for _ in range(n):
   size=int(input())
   #
   mountain=[]
   for i in range(size):
       row=[]
       for j in range(size):
           elevation=int(input())
           row.append(elevation)
       mountain.append(row)

   #
   # print(*mountain,sep='\n')

   #
   path=bfs((0,0),(size-1,size-1))

   #
   startElevation=mountain[0][0]
   #
   # print(*path,sep='\n')
   unit=0
   if path:
       for i in range(len(path)-1):
           a,b=path[i]
           c,d=path[i+1]
           if mountain[a][b]>startElevation or \
               mountain[c][d]>startElevation:
               unit+=1
       print(unit)
   else:
       print('CANNOT MAKE THE TRIP')




'''
2
5
5
4
3
2
1
7
5
6
6
6
8
8
8
9
6
9
6
9
9
6
4
5
4
5
3
2
4
9
9
4

'''