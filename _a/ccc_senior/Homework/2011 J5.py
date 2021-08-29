'''
3
3 -> 1
3 -> 2
'''
n=int(input())
g={k:[] for k in range(1,n+1)}

for i in range(1,n):
   friend=int(input())
   g[friend].append(i)
print(g)

#
def ways(n):
   neighbours=g[n]

   if len(neighbours)==0:
       return 1

   result=1
   for nn in neighbours:
       result=result*(1+ways(nn))
   return result

print(ways(n))




