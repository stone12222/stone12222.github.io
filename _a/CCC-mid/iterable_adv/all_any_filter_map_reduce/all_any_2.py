l=[1,2,3,4,5,6]
# all
print(list(e<7 for e in l))
print(all(e<7 for e in l))

# any
print(any(e>6 for e in l))

# filter
# print([e for e in l if e>3])

def greatthan3(e):
    return e>3

# def filter(func, l):
#     b=[]
#     for a in l:
#         if func(a):
#             b.append(a)
#         else:
#             pass
#     return b

f=filter(greatthan3,l)
print(list(f))

# map
# 100 200 300
# i=input().split()
# a=int(i[0])
# b=int(i[1])
# c=int(i[2])

# a,b,c=[int(e) for e in input().split()]

# def map(func,l):
#     o=[]
#     for x in l:
#         o.append(func(x))
#     return o

# a,b,c=map(int,input().split())
# print(a,b,c)

# reduce
l=[1,2,3]
def add(a,b):
    return a+b

'''
1 2 3

1=0+1
3=1+2
6=3+3
'''
def reduce(func,l):
    r=l[0]
    for e in l[1:]:
        r=func(r,e)
    return r

# import functools
# print(functools.reduce(add,l))
print(reduce(add,l))
