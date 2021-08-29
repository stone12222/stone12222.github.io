# tracking
def down(r,c):
    return r+1,c
def right(r,c):
    return r,c+1
def up(r,c):
    return r-1,c
def left(r,c):
    return r,c-1

steps=1
from itertools import cycle
directions=cycle([down,right,up,left])

#
start=0,0
r,c=start

while True:
    for _ in range(2):
        # find pattern
        dir=next(directions)
        print(dir.__name__, steps)

        # use pattern to move
        for s in range(steps):
            r,c=dir(r,c)
            print(r,c)
    steps+=1

    if steps==5:
        break









