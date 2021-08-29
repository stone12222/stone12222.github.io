# convert
s='abc'
print(list(s))

#
l=list(s)
s=''.join(l)
print(s)

# sort
l=[8,5,4,6,2]
l.sort() # when we sort original list
print(l)

l=[8,5,4,6,2]
ll=sorted(l) # when we keep original list
print(l)
print(ll)

# reverse
l.reverse()
print(l)
ll=reversed(l)
print(ll)

# count
l=list('aabbbcccc')
print(l.count('b'))

# unpack
l=[1,2]
# a,b=l
a=l[0]
b=l[1]