li = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', ' ', '-', '.', 'enter']
]

# rowid, colid
def getPos(letter):
    for rowid,row in enumerate(li):
        if letter in row:
            colid=row.index(letter)
        # for colid,col in enumerate(row):
        #     if col==letter:
            return rowid,colid

# print(getPos('N'))
# 2 1

# origin at top/left corner
def getPosXY(letter):
    for rowid,row in enumerate(li):
        for colid,col in enumerate(row):
            if col==letter:
                return colid, rowid
# print(getPosXY('N'))
# 1 2

# origin at bottom/left corner
# origin at top/left corner
def getPosXY1(letter):
    for rowid,row in enumerate(li):
        for colid,col in enumerate(row):
            if col==letter:
                return colid, len(li)-1-rowid
# print(getPosXY1('N'))
