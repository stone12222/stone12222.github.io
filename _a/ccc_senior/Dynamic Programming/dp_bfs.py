'''
dp vs greedy
solve subproblem, save knowledge
solve other subproblem by using the knowledge, and save knowledge
make decision when have all knowledge

subproblem: independent, optimal
'''
g = {
   'A': {'B':1,'C':2},
   'B': {'A':1,'D':6, 'E': 7, 'F': 8},
   'C': {'A':2,'D':5, 'E': 4, 'F': 3},
   'D': {'B':6,'C':5,'G': 7, 'H': 8},
   'E': {'B':7,'C':4,'G': 5, 'H': 6},
   'F': {'B':8,'C':3,'G': 3, 'H': 4},
   'G': {'D':7,'E':5,'F':3,'I': 1},
   'H': {'D':8,'E':6,'F':4,'I': 2},
   'I': {'G':1,'H':2}
}

knowledge={
   'I':0
}

parent={
   'I':None
}

q=['I']

while q:
   node=q.pop(0)

   for n,weight in g[node].items():
       new_knowledge=weight+knowledge[node]
       # new found node
       if n not in knowledge:
           knowledge[n]=new_knowledge
           q.append(n)
           parent[n]=node
       else:
           if new_knowledge<knowledge[n]:
               # knowledge updated
               knowledge[n]=new_knowledge
               q.append(n)
               parent[n]=node

#
for k,v in knowledge.items():
   print(k,v,parent[k])

# dp is a strategy

# here is only the graph representation
g = {
   'A': {'B': 1, 'C': 2},
   'B': {'D': 6, 'E': 7, 'F': 8},
   'C': {'D': 5, 'E': 4, 'F': 3},
   'D': {'G': 7, 'H': 8},
   'E': {'G': 5, 'H': 6},
   'F': {'G': 3, 'H': 4},
   'G': {'I': 1},
   'H': {'I': 2},
   'I':{}
}

#
# reverse graph
from collections import defaultdict
graph=defaultdict(dict)

for n,neighours in g.items():
   for neighbour,weight in neighours.items():
       graph[neighbour][n]=weight

for k,v in graph.items():
   print(k,v)

# update knowledge
knowledge={'I':0}
# bfs
goal='A'
q=['I']
while q:
   node=q.pop(0)

   for n in graph[node]:
       number=graph[node][n]+knowledge[node]
       if n not in knowledge:
           knowledge[n]=number
           q.append(n) # n not in knowlege, so add it to queue
       else:
           if knowledge[n]>number:
               knowledge[n]=number
               # knowledge updated, so add n to q
               # because n may be a middle node in the shortest path
               q.append(n)

#
for k in knowledge:
   print(k,knowledge[k])

print(knowledge['A'])