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
from itertools import cycle
def printPatterns(start,end):
    directions=['down','right','up','left']
    # while True:

    dirIndex=0
    count=1

    r,c=0,0
    startNum=start

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
                print(dir, count,(r,c),startNum)
                startNum+=1

                if startNum>end:
                    return
        count+=1

printPatterns(1,17)