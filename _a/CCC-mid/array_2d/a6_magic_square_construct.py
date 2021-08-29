size=int(input('size: '))

# magic square
mq=[]
for i in range(size):
    row=[]
    for j in range(size):
        row.append(0)
    mq.append(row)

for r in mq:
    print(r)

row=0
col=size//2

for n in range(1,size**2+1):
    mq[row][col]=n

    # backup row, col
    row1 = row
    col1 = col

    row-=1
    if row<0:
        row+=size

    col+=1
    if col==size:
        col=0

    if mq[row][col]!=0:
        row=row1
        col=col1
        row+=1

for r in mq:
    for n in r:
        print(n,end="\t")
    print()


