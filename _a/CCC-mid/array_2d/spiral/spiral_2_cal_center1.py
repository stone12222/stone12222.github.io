"""
21 20 19 18 17
22  7  6  5 16
23  8  1  4 15
24  9  2  3 14
25 10 11 12 13

        17
7  6  5 16
8  1  4 15
9  2  3 14
10 11 12 13

"""
def p():
    for row in square:
        for col in row:
            if col=='_':
                print('%2s' % col, end=' ')
            else:
                print('%2d' % col, end=' ')
        print()

#
s=int(input())
e=int(input())
nums=(e-s)+1

# size
size=int(nums**.5+0.5)
# print(size)

# row, col
import math
nr=math.ceil(nums/size)
nc=size

#
if nr%2==0:
    r=nr//2-1
else:
    r=nr//2
if nc%2==0:
    c=nc//2-1
else:
    c=nc//2

#
square=[['_']*nc for i in range(nr)]

#


# moving
from itertools import cycle
def moving(start, end):
    global r,c

    directions=['down','right','up','left']

    dirIndex=0
    count=1

    currNum=start
    square[r][c]=currNum
    p()
    currNum+=1

    direction=cycle(directions)
    while True:
        for i in range(2):
            dir=next(direction)
            dirIndex+=1

            for _ in range(count):
                if dir=='down':
                    r+=1
                if dir=='right':
                    c+=1
                if dir=='up':
                    r-=1
                if dir=='left':
                    c-=1
                print(dir, count,(r,c),currNum)
                square[r][c]=currNum
                p()
                currNum+=1

                if currNum>end:
                    return
        count+=1
moving(s,e)