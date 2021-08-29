# a list, but unchangable list
t=(1,2,3)
t=1,2,3
print(type(t))
print(t[1])

#
t=()
t=('a',)
print(type(t))
t='a',
print(type(t))
#
t[:]
# count
print((1,2,3,2,3,3).count(2))

# tuple to list
l=list(t)
t=tuple(l)
print(l)

# unchangable = immutable
a=(1,2)
b=(3,4)
c=a+b
print(c)

#
t=(7,2,3,6,5,9)
print(sorted(t,reverse=True))

#
s=set()
l=(1,2)
s.add(l)

# why tuple
'''
1. creating tuple is fast (about 5 times faster than list)
2. tuple can be shared, because it is read-only
3. can be used as key
'''
# time, we cannot prove for now?
import time
t=(1,2,3,6,100,200,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
s=time.time()
for i in range(1000000):
    for j in range(len(t)):
        a=t[j]
e=time.time()
print(e-s)

l=[1,2,3,6,100,200,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
s=time.time()
for i in range(1000000):
    for j in range(len(t)):
        b=l[j]
e=time.time()
print(e-s)

'''
s=r'''
a=(1,2,3)
for i in range(3):
    v=a[i]
'''
timeit.timeit(s,number=1000000)
'''


