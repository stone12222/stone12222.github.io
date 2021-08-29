li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

from a1_getposition_rowcol1 import getPos

# up, down, left, right
def getEnd(start, direction, numOfSteps):
    sr, sc=getPos(start)
    if direction=='right':
        er=sr
        ec=sc+4
        end=li[er][ec]
        return end
    elif direction=='up':
        er=sr
        ec=sc+4
        end=li[er][ec]
        return end
    elif direction=='down':
        er=sr
        ec=sc+4
        end=li[er][ec]
        return end
    elif direction=='down':
        er=sr
        ec=sc+4
        end=li[er][ec]
        return end


end=getEnd('H','right',4)
print(end)
