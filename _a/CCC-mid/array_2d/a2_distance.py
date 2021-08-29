li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

def getPos(letter):
    for rowid,row in enumerate(li):
        if letter in row:
            colid=row.index(letter)
            return rowid,colid

def getDistance(a,b):
    ax,ay=getPos(a)
    bx,by=getPos(b)
    return abs(ax-bx)+abs(ay-by)

print(getDistance('H','Q'))
