# finalPos -> direction+forward
# direction -> turns
def in_boundary(r,c):
    if r<0 or r>len(g)-1:
        return False
    if c<0 or c>len(g[0])-1:
        return False
    return True

def finalPos(startPos, startDir,moves):
    r,c=startPos
    for m in moves:
        if m=='R':
            startDir+=90
        if m=='L':
            startDir-=90
        startDir%=360

        if m=='F':
            if startDir==0:
                r-=1
                if not in_boundary(r,c):
                    r+=1
                    return r,c,'out of boundary'
            if startDir==90:
                c+=1
                if not in_boundary(r,c):
                    c-=1
                    return r,c,'out of boundary'
            if startDir==180:
                r+=1
                if not in_boundary(r,c):
                    r-=1
                    return r,c,'out of boundary'
            if startDir==270:
                c-=1
                if not in_boundary(r,c):
                    c+=1
                    return r,c,'out of boundary'
        print(g[r][c])
    return r,c,'In boundary'

g = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

startPos=(5,2)
startDir=0
moves=['R','F','F','L','F','F','F','F','F','F']

# (4,4)
fp=finalPos(startPos,startDir,moves)
fpx,fpy,message=fp
print(g[fpx][fpy],message)
