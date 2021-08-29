"""
input numbers, until press 'e'
i:
100
50
80
200
e

o:
50 80 100 200

transitions:
get input, save to a list
sort the list
print the list
"""
l=[]
i=input()
while i!='e':
    if i.isdigit():
        i=int(i)
    l.append(i)
    i=input()
l.sort()
for n in l:
    print(n,end=' ')
