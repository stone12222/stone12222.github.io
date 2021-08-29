l=[1,2,3,3,4,4,6,7,8]
# [1,2,3,3,4,4,6,7,8]

for n in l:
    if n==3 or n==4:
        l.remove(n)
print(l)
#
find=True
while find:
    for n in l:
        if n==3 or n==4:
            l.remove(n)
            find=True
            break
    else:
        find=False
print(l)

#
l=[1,2,3,3,4,4,5,6,7]
# range(starting index, stop index, step)
for i in range(len(l)-1,-1,-1):
    n=l[i]
    if n==3 or n==4:
        del l[i]
print(l)

#
l=[1,2,3,3,4,4,5,6,7]
ll=[]
for n in l:
    if n!=3 and n!=4:
        ll.append(n)
print(ll)

# comprehension
l=[1,2,3,3,4,4,5,6,7]
ll=[n for n in l if n!=3 and n!=4]
print(ll)

# transfer one collection to another

# set comprehension
s={n for n in range(4)}
print(s)

# dict comprehension
d={
    'a':1,
    'b':2,
    'c':3
}
dd={k:v*2 for k,v in d.items() if v>1}
print(dd)