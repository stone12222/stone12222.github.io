l=['a','b','c']
for s in enumerate(l):
    print(s)
for s in enumerate(l,start=100):
    print(s)

for i,e in enumerate(l):
    print(i,e)

pos=0
for e in l:
    print(pos,e)
    pos+=1