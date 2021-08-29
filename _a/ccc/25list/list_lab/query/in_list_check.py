"""
check if 4 in the list

"""
l=[1,2,3,[4,5]]

inlist=False
for e in l:
    if isinstance(e, list):
        inlist=True
    elif e==4:
        inlist=True
print(inlist)


"""
if elements in list are all iterable
"""
mylist = ['a','b','c', ['d','e']]
print('b' in [j for i in mylist for j in i])
