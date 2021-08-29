def isHole(row,col):
   for r,c,s in holes:
       if row<r+s and row>=r and col<c+s and col>=c:
           return True
   return False

def print_square(t,b,l,r):
   t=size-t
   b=size-b
   l=l-1
   r=r-1
   for row in range(t,b+1):
       for col in range(l,r+1):
           if isHole(row,col):
               print(' ',end='')
           else:
               print('*',end='')
       print()
   print()

def unfill(square):
   row, col, width = square
   if width==1:
       return

   s = width // 3
   hole = (row + s, col + s, s)
   holes.append(hole)

   #
   print_square(size, 1, 1, size)

   #
   sq1 = row, col, s
   unfill(sq1)
   sq2 = row, col + s, s
   unfill(sq2)
   sq3 = row, col + 2 * s, s
   unfill(sq3)
   sq4 = row + s, col, s
   unfill(sq4)
   sq5 = row + s, col + 2 * s, s
   unfill(sq5)
   sq6 = row + 2 * s, col, s
   unfill(sq6)
   sq7 = row + 2 * s, col + s, s
   unfill(sq7)
   sq8 = row + 2 * s, col + 2 * s, s
   unfill(sq8)

n=int(input())
for i in range(n):
   iterations=int(input())
   b=int(input())
   t = int(input())
   l = int(input())
   r = int(input())

   #
   size=3**iterations
   square=(0,0,size)
   holes=[]

   # more squares
   unfill(square)

   #
   print_square(t,b,l,r)
