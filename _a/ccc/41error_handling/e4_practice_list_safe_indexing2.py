l=[1,2,3,4]
# print(l[5])

def safeIndex(c,ind):
    try:
        return c[ind]
    except IndexError:
        print('abc')
        return None

print(safeIndex(l,4))

