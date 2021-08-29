# 0, 90, 180, 270
start=90

# R, L
def getDirection(dir, turns):
    for turn in turns:
        if turn=='R':
            dir+=90
        elif turn=='L':
            dir-=90
        dir%=360
    return dir

turns=['R','R','L','R']
print(getDirection(start,turns))
