"""
filter
"""
" 1 way "
l1=[]
for e in l:
    if e<4:
        l1.append(e)
print(l1)

" 2 way "
print([e for e in l if e<4])

" 3 way "
def lessthan4(n):
    return n<4

print(list(filter(lessthan4,l)))








