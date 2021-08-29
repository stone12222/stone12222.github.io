l=[1,2,2,3,3,4,5]
for n in l:
    if n<5:
        l.remove(n)
print(l)

#
def g(l):
    p=0
    while p<len(l):
        yield l[p]
        p+=1

for n in g(l):
    if n<5:
        l.remove(n)
print(l)