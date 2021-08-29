l=[
    ['a','b','c'],
    ['d','e','f']
]

r=int(input())
c=int(input())

# check condition-if-else r and c in the boundary
# -1,-1       -1,3
#       a,b,c
#       d,e,f
# 2,-1        2,3

in_boundary=True
if r<0 or r>len(l):
    in_boundary=False
elif c<0 or c>len(l[0])-1:
    in_boundary=False

if in_boundary:
    print('in boundary')
else:
    print('out of boundary')

