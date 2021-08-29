# tracking
steps=1
directions=[(1,0),(0,1),(-1,0),(0,-1)]
mIndex=0

#
start=0,0
r,c=start

while True:
    for _ in range(2):
        # find pattern
        dr,dc=directions[mIndex % 4]

        print(dir.__name__, steps)
        mIndex+=1

        # use pattern to move
        for s in range(steps):
            r+=dr
            c+=dc
            print(dir,r,c)
    steps+=1

    if steps==5:
        break









