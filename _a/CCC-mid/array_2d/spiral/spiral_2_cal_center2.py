"""
21 20 19 18 17
22  7  6  5 16
23  8  1  4 15
24  9  2  3 14
25 10 11 12 13
"""
"""
Down 1
Right 1
Up 2
Left 2
Down 3
Right 3
"""
startNum=int(input())
endNum=int(input())
movingDirs='DRUL'
n=endNum-startNum+1

# find center
size=int(n**.5+.5)

#
if n>size**2:
    nr=size+1
else:
    nr=size
nc=size

#
r=int(nr/2-0.5)
c=int(nc/2-0.5)
bakr=r
bakc=c
#
square=[[' ']*nc for _ in range(nr)]
def p():
    # for row in square:
    #     for col in row:
    #         # print(str(col).rjust(2),end=' ')
    #         print("%4s"%str(col),end=' ')
    #     print()
        # break
    for i in range(size):
        print(square[i][i])



#
square[r][c]=1
# p()

count=1
ind=0
def move():
    global r,c,startNum,count,ind
    while True:
        for i in range(2):
            dir=movingDirs[ind%len(movingDirs)]
            ind+=1
            # print(dir,count)

            for j in range(count):
                if dir=='D':
                    r+=1
                if dir=='R':
                    c+=1
                if dir=='U':
                    r-=1
                if dir=='L':
                    c-=1
                startNum+=1
                square[r][c]=startNum
                # p()

                if startNum>=endNum:
                    return
        count+=1
move()
p()
