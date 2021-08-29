l=['*']*6
print(l)

# 8by8 chess board
l=[['_']*8]*8
for row in l:
    print(*row)

# change only first element
l[0][0]=0
# strange, all elements in first column changed to 0
print(l)

# if hard code
l=[[1,1,1],[1,1,1],[1,1,1]]
print(l)
l[0][0]=0
print(l)

# summary
# the 3 inner lists are same (1 reference duplicate 3 times)

# solve
l=[[1]*3 for x in range(3)]
print(l)
l[0][0]=0
print(l)
