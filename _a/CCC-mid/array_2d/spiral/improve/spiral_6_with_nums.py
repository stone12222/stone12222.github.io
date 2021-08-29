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
def getMoves(sn,en):
    steps=1
    start=0,0
    r,c=start

    while True:
        for _ in range(2):
            # find pattern
            dir=next(directions)

            # use pattern to move
            for s in range(steps):
                r,c=dir(r,c)
                yield sn,dir.__name__,r,c
                if sn==en:
                    return
                sn+=1
        steps+=1

for m in getMoves(10,37):
    print(m)
