"""
i: 100
o: 01:00

i: 1100
o: 11:00
"""

i=input()
i=i.zfill(4)
h=i[:2]
m=i[2:]
print(h,':',m,sep='')
