# y direction is towards top

li=[
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','enter']
]

def get_position(key):
    for row_id,row in enumerate(li):
        for col_id, k in enumerate(row):
            if key==k:
                return (row_id,col_id)

def get_path(start,end,command):
    sr=start[0]
    sc=start[1]
    er=end[0]
    ec=end[1]

    r1=[]
    if command=='l':
        for c in range(ec,sc):
            r1.append((sr,c))
    if command=='r':
        for c in range(sc+1,ec+1):
            r1.append((sr,c))
    if command=='u':
        for r in range(er,sr):
            r1.append((r,sc))
    if command=='d':
        for r in range(sr+1,er+1):
            r1.append((r,sc))
    return r1

p1=get_position('N')
p2=get_position('B')
command='u'

path=get_path(p1,p2,command)

for row,col in path:
    x=col
    y=-row
    print(li[row][col],'(x,y)->(',x,y,')')
