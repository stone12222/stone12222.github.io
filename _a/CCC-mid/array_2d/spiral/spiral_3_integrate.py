# tracking
def down(r,c):
    return r+1,c
def right(r,c):
    return r,c+1
def up(r,c):
    return r-1,c
def left(r,c):
    return r,c-1

from itertools import cycle
directions=cycle([down,right,up,left])

#
def makeMoves(r, c, sn, en):
    steps=1
    square[r][c]=sn

    while True:
        for _ in range(2):
            # find pattern
            dir=next(directions)

            # use pattern to move
            for s in range(steps):
                r,c=dir(r,c)
                # yield sn,dir.__name__,r,c
                sn+=1
                square[r][c]=sn
                if sn==en:
                    return
        steps+=1

"""
populate square
"""
from math import sqrt
sn=1
en=21
nums = en-sn+1
size= int(sqrt(nums)+.5)
if nums>size**2:
    nr=size+1
else:
    nr=size
nc=size

# create 2d space
square = [['_'] * nc for _ in range(nr)]

# init center
if nr%2==0:
    r=nr//2-1
else:
    r=nr//2

if nc%2==0:
    c=nc//2-1
else:
    c=nc//2
# populate others
makeMoves(r, c, sn, en)

# print
for row in square:
    for col in row:
        if str(col).isdigit():
            print('%2d'%col,end=' ')
        else:
            print('%2s'%col,end=' ')
    print()

