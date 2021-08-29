def getPos(letter):
    for rowid,row in enumerate(li):
        if letter in row:
            colid=row.index(letter)
            return rowid,colid

def getEnd(c,dir,steps):
    r,c=getPos(c)

    if dir=='up':
        r-=steps
    elif dir=='right':
        c+=steps
    elif dir=='left':
        c-=steps
    elif dir=='down':
        r+=steps

    r=r%len(li)
    c=c%len(li[0])
    return li[r][c]

li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

#
c=getEnd('T','left',3)
print(c)


