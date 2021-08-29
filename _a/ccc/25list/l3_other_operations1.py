l=[4,5,3,2,7,1]
print('original l:',l)
# reverse, if you want to change the original list
l.reverse()
print(l)

# if you want to keep original list
ll=reversed(l)
ll=list(ll)
print(ll)

# sort
ll.sort()
print(ll)

ll=sorted(l)
print(ll)

#
print(ll.count(2))

#
l=sorted(['Ray','hanson','richard','stone','frank','samar'],key=str.lower)
print(l)

#
l=[4,5,3,8,2,1]
l.sort(reverse=True)
print(l)
