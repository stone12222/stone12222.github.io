def finalDir(dir,turns):
    for turn in turns:
        if turn=='R':
            dir+=90
        if turn=='L':
            dir-=90
        dir%=360
        # if dir<0:
        #     dir+=360
        # if dir>=360:
        #     dir-=360
    return dir

# 0, 90, 180, 270
start=0

# R, L
turns=['R','R','R','R','R','R','R']
print(finalDir(start,turns))
