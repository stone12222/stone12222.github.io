"""
i: Rows Cols such as
2 3

o:
1 2 3
4 5 6

"""
rows=int(input("Rows "))
cols=int(input("Cols "))

n=1
for i in range(rows):
    for j in range(cols):
        print(n,end=" ")
        n=n+1
    print()
