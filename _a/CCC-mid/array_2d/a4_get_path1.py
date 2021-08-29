def getPosition(char):
    rid,row=[(rid,r) for rid,r in enumerate(li) if char in r][0]
    col=row.index(char)
    return rid, col

def get_path(char1,char2):
    r1,c1=getPosition(char1)
    r2,c2=getPosition(char2)

    d=''
    if r1==r2:
        if c1<c2:
            d='r'
        else:
            d='l'
    else:
        if r1<r2:
            d='d'
        else:
            d='u'

    path=[]
    if d=='u':
        for i in range(r1,r2-1,-1):
            path.append(li[i][c1])
    if d=='d':
        for i in range(r1,r2+1):
            path.append(li[i][c1])
    if d=='l':
        for i in range(c1,c2-1,-1):
            path.append(li[r1][i])
    if d=='r':
        for i in range(c1,c2+1):
            path.append(li[r1][i])
    return path

li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

l=get_path('A','F')
print(*l)
l=get_path('F','A')
print(*l)
l=get_path('Y','A')
print(*l)
l=get_path('A','Y')
print(*l)


