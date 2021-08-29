l=[1,2,3,4]
# print(l[5])

def indexing(l,index):
    try:
        return l[index]
    except IndexError:
        return None
    # if index<(len(l)-1):
    #     return l[index]
    # else:
    #     return None

print(indexing(l,5))
