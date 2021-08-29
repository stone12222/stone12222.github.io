print('Enumerate list')
l=['a','b','c']
for j in l:
    print(j)

print('Enumerate map')
m=map(lambda e:e, l)
for j in m:
    print(j)

print('Note: can only enumerate once')
for j in m:
    print(j)
# because map returns an iterator, which you can only iterate over once.

'''
1 2 3 
      ^
'''