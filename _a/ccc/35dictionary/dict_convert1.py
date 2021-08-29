#
l1=['joe','anna','baker']
l2=['friend','friend','not friend']

z=zip(l1,l2)
print(list(z))

# why? because after list(z), z is dead. why?
z=zip(l1,l2)
d=dict(z)
print(d)