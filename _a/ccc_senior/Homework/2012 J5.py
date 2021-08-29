'''
1 find a solution
2 if slow, find reason, come up a new solution
'''
def canPutOn(a,b):
   # if a=='':
   #     return False
   # if int(a[0])>int(b[0]):
   #     return False
   # return True
   try:
       if (a!='' and b!='' and int(a[0])<int(b[0])) or (a!='' and b==''):
           return True
       return False
   except:
       print(a,b)
       print('error')


def getNeighbour(config,n):
   ns=[]
   # 1,2,3 -> '',12,3
   #       -> 1 ,'',23
   for i in range(n-1):
       # n=3, i=0 1
       # i i+1: 0 1, 1 2
       if canPutOn(config[i],config[i+1]):
           # 1,2,3
           coin=config[i][0]
           a=config[i][1:]
           b=coin+config[i+1]
           newConfig=config[:i]+(a,)+(b,)+config[i+2:]
           ns.append(newConfig)
       elif canPutOn(config[i+1],config[i]):
           # 2,1,3 => 12,'',3
           coin=config[i+1][0]
           a=coin+config[i]
           b=config[i+1][1:]
           newConfig=config[:i]+(a,)+(b,)+config[i+2:]
           ns.append(newConfig)
   return ns

def bfs(config,goal):
   num=len(config)
   if config==goal:
       return [config]

   q=[[config,[config]]]
   visited={config}

   while q:
       node,path=q.pop(0)

       for n in getNeighbour(node,num):
           if n==goal:
               return path+[n]
           if n not in visited:
               visited.add(n)
               q.append([n,path+[n]])

while True:
   n=int(input())
   if n==0:
       break

   config=tuple(input().split()) # 3 2 1
   goal=tuple([str(i) for i in range(1,n+1)]) # 1 2 3

   path=bfs(config,goal)
   if path:
       # for p in path:
       #     print(p)
       print(len(path)-1)
   else:
       print('IMPOSSIBLE')

'''
3
3 2 1
0

20

2
2 1
Impossible
'''


