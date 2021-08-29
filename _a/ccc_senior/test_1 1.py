'''
LLSLM
'''
import sys
from collections import deque

input = sys.stdin.readline

dicts={}

def next(y,x,m,b):
    if y==n-1 and x==m-1:
        return 1
    else:
        dicts[(y,x)]=0
        if moves >= maps[y][x]:
            if can_go(y + 1, x) and ((y + 1, x) not in b):
                b.add((y + 1, x))
                dicts[(y,x)]+=next(y + 1, x, moves + 1,b)
            elif (y + 1, x) in dicts:
                dicts[(y, x)]+=dicts[(y + 1, x)]

            if can_go(y - 1, x) and ((y - 1, x) not in b):
                b.add((y - 1, x))
                dicts[(y,x)]+=next(y - 1, x, moves + 1,b)
            elif (y - 1, x) in dicts:
                dicts[(y, x)]+=dicts[(y - 1, x)]

            if can_go(y, x + 1) and ((y, x + 1) not in b) :
                b.add((y, x + 1))
                dicts[(y,x)]+=next(y, x + 1, moves + 1,b)
            elif (y, x+1) in dicts:
                dicts[(y, x)]+=dicts[(y, x+1)]

            if can_go(y, x - 1) and ((y, x - 1) not in b):
                b.add((y, x - 1))
                dicts[(y,x)]+=next(y, x - 1, moves + 1,b)
            elif (y, x-1) in dicts:
                dicts[(y, x)]+=dicts[(y, x-1)]

    return dicts[(y,x)]

def can_go(y, x):
    return 0 <= y < n and 0 <= x < m

n, m, k = [int(i) for i in input().split()]

bull = []
maps = [[-1 for i in range(m)] for j in range(n)]

for i in range(k):
    y, x, s, d = input().split()
    bull.append([int(y) - 1, int(x) - 1, int(s), d])

for e in bull:
    moves = 0
    maps[e[0]][e[1]] = moves
    if e[3] == "R":
        x = e[2]
        y = 0
    elif e[3] == "L":
        x = -e[2]
        y = 0
    elif e[3] == "U":
        x = 0
        y = -e[2]
    else:
        x = 0
        y = e[2]
    while 0 <= e[0] + y < n and 0 <= e[1] + x < m:
        e[0] += y
        e[1] += x
        moves += 1
        if maps[e[0]][e[1]] < moves:
            maps[e[0]][e[1]] = moves



print(next(0,0,0,{(0,0)}))
