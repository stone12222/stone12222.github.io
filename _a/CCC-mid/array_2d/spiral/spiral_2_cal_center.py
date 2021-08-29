"""
21 20 19 18 17
22  7  6  5 16
23  8  1  4 15
24  9  2  3 14
25 10 11 12 13
"""
# how many numbers
nums = 17
# how big the square?
size= int(nums**.5+.5)

# num of rows
if nums>size**2:
    nr=size+1
else:
    nr=size
# num of cols
nc=size

# create 2d space
square = [['_'] * nc for _ in range(nr)]

# and we start by placing a 1 in the center:
if nr%2==0:
    r=nr//2-1
else:
    r=nr//2

if nc%2==0:
    c=nc//2-1
else:
    c=nc//2

square[r][c] = 1

for r in square:
    for c in r:
            print(c,end="  ")
    print()
