"""
      27 26
16 15 14 25
17 10 13 24
18 11 12 23
19 20 21 22

find pattern (direction and moving steps)
direction: move down, move right, move up, move left...
moving steps: move one, move one, move two, move two, move three, move three, ...

down 1
right 1
up 2
left 2
down 3
right 3
up 4
left 4
......
"""
# tracking
steps=1
directions=['down', 'right', 'up', 'left']
mIndex=0

#
start=0,0
r,c=start

#
startNum=1
endNum=27
currNum=startNum

while True:
    for _ in range(2):
        # find pattern
        dir=directions[mIndex % 4]
        mIndex+=1

        # use pattern to move
        print(dir,steps,(r,c))
        for s in range(steps):
            if dir== 'down':
                r+=1
            elif dir== 'right':
                c+=1
            elif dir== 'up':
                r-=1
            elif dir== 'left':
                c-=1
            print(dir,steps,(r,c),currNum)
            currNum+=1
    steps+=1

    if currNum>=endNum:
        break

