moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

def getNeighbours(node):
   row,col=node

   ns=[]
   for dr,dc in moves:
       nr=dr+row
       nc=dc+col
       if 1<=nr<=r and 1<=nc<=c:
           ns.append((nr,nc))
   return ns

def bfs_sp(start,goals):
   if start in goals:
       goals[start][-1]=0

   q=[(start,0)]
   visited={start}

   num_goals=len(goals)
   while q:
       node,steps=q.pop(0)

       for n in getNeighbours(node):
           if n in goals and goals[n][-1]==-1:
               goals[n][-1]=steps+1
               num_goals-=1
               if num_goals==0:
                   return
               q.append((n, steps + 1)) # still need add to queue
           else:
               if n not in visited:
                   visited.add(n)
                   q.append((n,steps+1))

n=int(input())

for i in range(n):
   r=int(input())
   c=int(input())
   pr=int(input())
   pc=int(input())
   kr=int(input())
   kc=int(input())

   # generate goals
   # [pr,pc,pawn_steps,knight_steps]
   goals={(k,pc):[k-pr,-1] for k in range(pr+1,r+1)}

   # fill out knight steps for each goal
   bfs_sp((kr,kc),goals)

   # process pawn_step and knight_step
   for k,v in goals.items():
       # print(k,v)
       gr,gc=k
       pawn_step,knight_step=v
       if knight_step==-1:
           continue

       if pawn_step>=knight_step:
           diff=pawn_step-knight_step
           if diff%2==0 and gr!=r:
               print('Win in',pawn_step, 'knight move(s).')
               break
           elif diff%2==1 and gr!=r:
               print('Stalemate in',knight_step,'knight move(s).')
               break
   else:
       pawn_last_step=r-pr
       print('Loss in', pawn_last_step - 1, 'knight move(s).')

'''
1
3
3
1
1
1
3
Win

1
3
3
1
1
1
2
Stalemate

1
3
3
1
1
3
2
Loss

'''

'''
1
10
10
8
4
10
4

Loss in 1 knight moves(s).

1
99
2
1
1
1
2

Stalemate in 1 knight moves(s).

1
99
2
1
1
3
1

Win in 2 knight moves(s).
'''

'''
3
99
99
33
33
33
35
3
3
1
1
2
3
99
99
96
23
99
1

Win in 1 knight move(s).
Stalemate in 1 knight move(s).
Loss in 2 knight move(s).
'''


