def isUnfilled(r,c,holes):
   for row,col,size in holes:
       if (r>=row and r<row+size) and (c>=col and c<col+size):
           return True
   return False

def printSquare(b,t,l,r,size,holes):
   b=size-b
   t=size-t
   l=l-1
   r=r-1
   for row in range(t,b+1):
       for col in range(l,r+1):
           if isUnfilled(row,col,holes):
               print(' ',end=' ')
           else:
               print('*',end=' ')
       print()
   print()

# n=int(input())
n=1
for i in range(n):
   # iteration=int(input()) #3
   iteration=3
   # b=int(input())
   # t=int(input())
   # l=int(input())
   # r=int(input())
   b=2
   t=10
   l=5
   r=27

   total_size=iteration**3

   holes=[]
   squares=[(0,0,total_size)]
   while True:
       sr, sc, size=squares.pop(0)
       if size==1:
           break

       #
       new_size=size//3
       row= sr + new_size
       col= sc + new_size

       hole=row,col,new_size
       holes.append(hole)

       #
       printSquare(1,total_size,1,total_size,total_size,holes)

       #
       s1=sr,sc,new_size
       s2=sr,sc+new_size,new_size
       s3=sr,sc+new_size*2,new_size
       s4=sr+new_size,sc,new_size
       s5=sr+new_size,sc+new_size*2,new_size
       s6=sr+2*new_size,sc,new_size
       s7=sr+2*new_size,sc+new_size,new_size
       s8=sr+2*new_size,sc+2*new_size,new_size
       squares.extend([s1,s2,s3,s4,s5,s6,s7,s8])

   printSquare(b,t,l,r,total_size,holes)
