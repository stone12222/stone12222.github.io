l=['_']*4
s=[]
for i in range(4):
    s.append(l[:])
# s=[l,l[:],l[:],l[:]]

s=[['_']*4 for i in range(4)]

# s=[['_']*4]*4

s[0][0]=9

for row in s:
    print(*row)
