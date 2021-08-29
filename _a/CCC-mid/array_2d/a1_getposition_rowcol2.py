def getPos(c):
    row_id=0
    for row in li:
        if c in row:
            col_id=row.index(c)
            return row_id,col_id
        row_id+=1

def getPosXY(c):
    row_id=0
    for row in li:
        if c in row:
            col_id=row.index(c)
            y=row_id
            x=col_id
            return x,y
        row_id+=1

def getPosXY2(c):
    row_id=0
    for row in li:
        if c in row:
            col_id=row.index(c)
            # row, col
            # 1, 1
            # 3, 1

            # 2, 1
            # 2, 1
            y=len(li)-1-row_id
            x=col_id
            return x,y
        row_id+=1
# 2d list
li = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', ' ', '-', '.', 'enter']
]

result=getPos('P')
print(result) # 2,3
result=getPosXY('P')
print(result) # 2,3
result=getPosXY2('T')
print(result) # 2,3
