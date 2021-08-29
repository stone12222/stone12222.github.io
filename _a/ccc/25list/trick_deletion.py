"""
delete 2<number<7
"""
l=[1,2,3,4,5,6,7,8,9]

# wrong
for e in l:
    if 2<e<7:
        l.remove(e)
        print(l)
print(l)

# correct
while True:
    for e in l:
        if 2<=e<=7:
            l.remove(e)

    sign=False
    for e in l:
        if 2<=e<=7:
            sign=True
    if not sign:
        break

# correct
l=[1,2,3,4,5,6,7,8,9]
for index in range(len(l)-1,-1,-1):
    if 2<l[index]<7:
        l.remove(l[index])
print(l)

# correct
l=[1,2,3,4,5,6,7,8,9]
l1=[]
for e in l:
    if 2<e<7:
        pass
    else:
        l1.append(e)
l=l1
print(l)

# correct (why this works?)
l=[1,2,3,4,5,6,7,8,9]
for e in l[::-1]:
    if 2<e<7:
        l.remove(e)
print(l)


