l=[1,2,3]

# print(l[4])

def safeIndex(l,i):
    try:
        return l[i]
    except Exception:
        return None

n=int(input())
print(safeIndex(l,n))

