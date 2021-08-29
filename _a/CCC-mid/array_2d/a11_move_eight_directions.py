# 100 x 100
n=0
g=[]
for r in range(10):
    row=[]
    for c in range(10):
        num=str(n)
        num=num.rjust(2,' ')
        row.append(num)
        n+=1
    g.append(row)

for row in g:
    print(*row)

'''
8 moving direction path
'''
def in_boundary(r,c):
    if r<0 or r>len(g)-1:
        return False
    if c<0 or c>len(g[0])-1:
        return False
    return True

start=(5,4)
r,c=start

for rdir,cdir in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
        print('start moving')
        r,c=start
        while in_boundary(r,c):
                print(g[r][c],end=' ')
                r+=rdir
                c+=cdir
        print()



