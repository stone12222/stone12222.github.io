"""
reverse
"""
l=[1,2,3]
l.reverse()
# or
# l=l[::-1]
print(l)
l1=reversed(l)
print(list(l1))

"""
sort
"""
l=[100,50,80]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l=["Nicolas","daniel","qiqi","YuanYuan"]
l.sort()
print(l)
l.sort(key=str.lower)
print(l)

"""
or sorted
"""
l=[100,50,80]
l1=sorted(l)
print('l:',l)
print('l1:',l1)

"""
count
"""
l=[1,1,2,2,2,3]
print(l.count(2))

