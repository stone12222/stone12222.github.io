# tuple is a list, but un-changable (immutable)
# 元组
# crq
t=()
print(type(t))

t=(1,2,3)
t=1,2,3
print(t[0:])

t=1,2,(4,5)

t=1,
print(type(t))
print(t)

# why? speed faster

q=(100,200)
t=q
'''
      ----------
t    |  ABF0 -> EEF0  |
100   ----------
q    | EEF0    |
      ----------
ABF0 | (1,2,3) |
      ----------
EEF0 | (100,200)|
      ----------
'''

# count, in, copy
t=(1,2,3)
tt=t # alias

# zip
a=(1,2,3)
b=('jeffery','luke','ivan')
c=zip(a,b)
print(list(c))

#
a=(4,2,3,1)
b=tuple(sorted(a))
print(b)