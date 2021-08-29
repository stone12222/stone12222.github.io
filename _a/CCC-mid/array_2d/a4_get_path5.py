li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

def find(letter):
    for rowid,row in enumerate(li):
        if letter in row:
            colid=row.index(letter)
            return rowid,colid

def get_path(a,b):
    path=[a]
    ax,ay=find(a)
    bx,by=find(b)
    diff_row=ax-bx
    diff_col=ay-by

    #
    if diff_row>0:
        for i in range(ax-1,ax-diff_row-1,-1):
            path.append(li[i][ay])

    elif diff_row<0:
        for i in range(ax+1,ax-diff_row+1):
            path.append(li[i][ay])

    ax=ax-diff_row

    if diff_col>0:
        for i in range(ay-1,ay-diff_col-1,-1):
            path.append(li[ax][i])
    elif diff_col<0:
        for i in range(ay+1,ay-diff_col+1):
            path.append(li[ax][i])
    return path

path=get_path('F','A')
print(path)

