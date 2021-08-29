from itertools import cycle
# tracking
directions=['down', 'right', 'up', 'left']

# how many numbers
startNum=10
endNum=27

#
nums=endNum-startNum+1
size= int(nums**.5+.5)
if nums>size**2:
    nr=size+1
else:
    nr=size
nc=size

# create 2d space
square = [['_'] * nc for _ in range(nr)]
def p():
    for r in square:
        for c in r:
            if c=='_':
                print('%2s' % c,end=' ')
            else:
                print('%2d' % c,end=' ')
        print()
    print()


def populateSquare():
    # and we start by placing a 1 in the center:
    if nr%2==0:
        r=nr//2-1
    else:
        r=nr//2

    if nc%2==0:
        c=nc//2-1
    else:
        c=nc//2

    square[r][c] = startNum
    currNum=startNum+1

    steps=1
    cyc=cycle(directions)
    while True:
        for _ in range(2):
            # find pattern
            dir=next(cyc)

            # use pattern to move
            for s in range(steps):
                if dir== 'down':
                    r+=1
                elif dir== 'right':
                    c+=1
                elif dir== 'up':
                    r-=1
                elif dir== 'left':
                    c-=1
                square[r][c]=currNum
                if currNum==endNum:
                    return
                currNum+=1
        steps+=1
populateSquare()
p()
