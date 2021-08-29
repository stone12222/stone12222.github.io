start_hz,start_pat=float(input()),int(input())

get=False

l=[start_hz]
lens=1.26
s=start_hz*lens
lens=0.63
print(s)

for i in range(12):
    start_hz *= 2 ** (1 / 12)
    if get:
        get=False
        start_pat+=1
        l.append(start_hz)
    elif start_pat == 4:
        start_pat=1
        l.append(start_hz)
    else:
        get=True
ll=[]
for i in l:
    if i != l[0]:
        l_new=(s/i)/2
        ll.append((lens-l_new)*100)

for i in range(1,len(l)):
    print(l[i],ll[i-1])
print(l)
print(ll)