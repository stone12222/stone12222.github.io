# given:
# start point
# facing direction
# a matrix
# some movements
# print final move condition-if-else exist, otherwise, print ()

def in_boundary(p, l):
    r,c=p

    in_b=True
    if r<0 or r>len(l)-1:
        in_b=False
    elif c<0 or c>len(l[0])-1:
        in_b=False

    return in_b

def valid_position(p, l):
    r,c=p
    return in_boundary(p, l) and l[r][c] != 'X'

def get_final_position(sp,fd,l,ms):
    r,c=sp

    for m in ms:
        # print((r,c),fd,m)
        if m=='F':
            if fd==0:
              r=r-1
            if fd==90:
              c=c+1
            if fd==180:
              r=r+1
            if fd==270:
              c=c-1
        if m=='R':
            if fd==0:
                fd=90
            elif fd==90:
                fd=180
            elif fd==180:
                fd=270
            elif fd==270:
                fd=0
        if m=='L':
            if fd==0:
                fd=270
            elif fd==270:
                fd=180
            elif fd==180:
                fd=90
            elif fd==90:
                fd=0
        # check every intermediate positions
        if not valid_position((r,c),l):
            # print('break')
            return ()
    else:
        return (r,c)

sp=(0,1) # start position
fd=0 # facing direction
l=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
ms=['R','F','R','F']
print(get_final_position(sp,fd,l,ms))
# (1,2)
