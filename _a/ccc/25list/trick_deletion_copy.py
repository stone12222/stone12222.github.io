'''
del l[2]
l.remove(4)
a=l.pop()
a=l.pop(2)
l.clear()

l=[1,2,2,3,4,4,5,6]
     ^
l=[1,2,3,4,4,5,6]
       ^
'''

#
l=[1,2,2,3,4,4,5,6]
for v in l:
    if v==2 or v==4:
        l.remove(v)
print(l)
#
l=[1,2,2,3,4,4,4,5,6]
twos=l.count(2)
fours=l.count(4)
rounds=max(twos,fours)
for i in range(rounds):
    for v in l:
        if v==2 or v==4:
            l.remove(v)
print(l)

#
l=[1,2,2,3,4,4,4,5,6]
while True:
    found=False
    for v in l:
        if v==2 or v==4:
            l.remove(v)
            found=True
    if not found:
        break
print(l)

#
l=[1,2,2,3,4,4,4,5,6]
i=0
while i<=len(l)-1:
   if l[i]==2 or l[i]==4:
       del l[i]
       i-=1
   i+=1
print(l)

#
l=[1,2,2,3,4,4,4,5,6]
for i in range(len(l)-1,-1,-1):
    pass

#
'''
go through each num in l:
    if the num not 2 and not 4:
        ll.append(num)
l=ll
print(l)
'''
l=[1,2,2,3,4,4,4,5,6]
ll=[]
for v in l:
    if v!=2 and v!=4:
        ll.append(v)
l=ll
print(l)
