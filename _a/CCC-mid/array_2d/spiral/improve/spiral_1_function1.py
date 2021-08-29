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
directions=[down,right,up,left]
mIndex=0

#
start=0,0
r,c=start

while True:
    for _ in range(2):
        # find pattern
        dir=directions[mIndex % 4]
        print(dir.__name__, steps)
        mIndex+=1

        # use pattern to move
        for s in range(steps):
            r,c=dir(r,c)
            print(r,c)
    steps+=1

    if steps==5:
        break









