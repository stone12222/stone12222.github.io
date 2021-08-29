'''
2 1
3 3

1
'''
'''
version 3
'''
moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

a,b=map(int,input().split())
c,d=map(int,input().split())

def bfs(start,goal):
   if start==goal:
       return 0

   # path length
   q=[[start,0]]
   visited={start}

   while q:
       node,path_length=q.pop(0)

       r,c=node
       for dr, dc in moves:
           if 0 < dr + r < 9 and 0 < dc + c < 9:
               neighbour=dr+r,dc+c
               if neighbour == goal:
                   return path_length+1
               if neighbour not in visited:
                   visited.add(neighbour)
                   q.append([neighbour,path_length+1])
print(bfs((a,b),(c,d)))

'''
version 2
'''
# def getNeighbour(node):
#     r,c=node
#     ns=[]
#     for dr,dc in moves:
#         if 0<dr+r<9 and 0<dc+c<9:
#             ns.append((dr+r,dc+c))
#     return ns
#
# moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
#
# a,b=[int(e) for e in input().split()]
# c,d=[int(e) for e in input().split()]
#
# def bfs(start,goal):
#     if start==goal:
#         return 0
#
#     # path length
#     q=[[start,0]]
#     visited=[start]
#
#     while q:
#         node,path_length=q.pop(0)
#
#         for n in getNeighbour(node):
#             if node == goal:
#                 return path_length
#             if n not in visited:
#                 visited.append(n)
#                 q.append([n,path_length+1])
# print(bfs((a,b),(c,d)))
'''
version 1
'''
# def getNeighbour(node):
#     r,c=node
#     ns=[]
#     for dr,dc in moves:
#         if 0<dr+r<9 and 0<dc+c<9:
#             ns.append((dr+r,dc+c))
#     return ns

# moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
#
# a,b=[int(e) for e in input().split()]
# c,d=[int(e) for e in input().split()]
#
# def bfs(start,goal):
#     if start==goal:
#         return [start]
#
#     q=[[start,[start]]]
#     visited=[start]
#
#     while q:
#         node,path=q.pop(0)
#
#         for n in getNeighbour(node):
#             if node == goal:
#                 return path
#             if n not in visited:
#                 visited.append(n)
#                 q.append([n,path+[n]])
# print(len(bfs((a,b),(c,d)))-1)






