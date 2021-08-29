# join
l1=[1,2,3]
l2=[4,5,6]

print(l1)
print(l2)
print(l1+l2)

#
l3=l1
print(l3)
l1.append(100)
print(l1)
print(l3) # l3 is not a copy, l3 is an alias

# copy
l1=[1,2,3]
l4=l1[:]
l1.append(100)
print(l1)
print(l4)

# copy vs alias

# convert
s='abc'
l=list(s)
print(l)

ss=''.join(l)
print(ss)

# count
l=list('aabbb')
print(l.count('b'))

# reverse
l=[1,2,3]
l.reverse()
print(l)

ll=reversed(l)
print(ll)
print(list(ll))

