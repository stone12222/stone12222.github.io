'''
10  cols
8   rows
3   width
2   height
15  steps

7'''
10  cols
8   rows
3   width
2   height
15  steps

7
7

11
12
5
5
20

6
11

15
20
5
5
150

8
18

'''
cols=int(input())
rows=int(input())
width=int(input())
height=int(input())
steps=int(input())

# cols=10
# rows=8
# width=3
# height=2
# steps=15

house=[[0]*cols for i in range(rows)]

# 0 can walk
# 1 past
# 2 wall
def p():
   # for row in house:
   #     print(*row)
   # print()
   pass

for i in range(height):
   for j in range(width):
       house[i][j]=2

       r=0
       c=cols-width
       house[r+i][c+j]=2

       r=rows-height
       c=0
       house[r+i][c+j]=2

       r=rows-height
       c=cols-width
       house[r+i][c+j]=2
       p()

'''
1. moving pattern
2. when stop
'''
directions='RDRDLDLULURU'
r=0
c=width
house[r][c]=1
p()

while True:
   for dir in directions:
       trapped=True
       if dir=='R':
           while c+1<cols and house[r][c+1]==0 and (r-1<0 or house[r-1][c]!=0):
               c+=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='D':
           while r+1<rows and house[r+1][c]==0 and (c+1>=cols or house[r][c+1]!=0):
               r+=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='L':
           while house[r][c-1]==0 and (r+1>=rows or house[r+1][c]!=0):
               c-=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='U':
           while house[r-1][c]==0 and house[r][c-1]!=0:
               r-=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif trapped:
           break
       if steps == 0:
           break
   if steps==0:
       print(c+1)
       print(r+1)
       break
   if trapped:
       print(c+1)
       print(r+1)
       break











7

11
12
5
5
20

6
11
'''
cols=int(input())
rows=int(input())
width=int(input())
height=int(input())
steps=int(input())

# cols=10
# rows=8
# width=3
# height=2
# steps=15

house=[[0]*cols for i in range(rows)]

# 0 can walk
# 1 past
# 2 wall
def p():
   for row in house:
       print(*row)
   print()
   # pass

for i in range(height):
   for j in range(width):
       house[i][j]=2

       r=0
       c=cols-width
       house[r+i][c+j]=2

       r=rows-height
       c=0
       house[r+i][c+j]=2

       r=rows-height
       c=cols-width
       house[r+i][c+j]=2
       p()

'''
1. moving pattern
2. when stop
'''
directions='RDRDLDLULURU'
r=0
c=width
house[r][c]=1
p()

while True:
   for dir in directions:
       trapped=True
       if dir=='R':
           while c+1<cols and house[r][c+1]==0 and (r-1<0 or house[r-1][c]!=0):
               c+=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='D':
           while r+1<rows and house[r+1][c]==0 and (c+1>=cols or house[r][c+1]!=0):
               r+=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='L':
           while house[r][c-1]==0 and (r+1>=rows or house[r+1][c]!=0):
               c-=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif dir=='U':
           while house[r-1][c]==0 and house[r][c-1]!=0:
               r-=1
               house[r][c]=1
               trapped = False
               p()
               steps-=1
               if steps==0:
                   break
       elif trapped:
           break
       if steps == 0:
           break
   if steps==0:
       print(c+1)
       print(r+1)
       break
   if trapped:
       print(c+1)
       print(r+1)
       break












