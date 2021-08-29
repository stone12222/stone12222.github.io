import functools

# combine with map, reduce, filter
# lambda version
result=map(lambda n:n*2, [1,2,3])
for n in result:
    print('map',n)

# filter
number_largerthan100=filter(lambda x:x>100, [100,200,300])
for n in number_largerthan100:
    print('filter',n)

# reduce
total=functools.reduce(lambda x,y:x+y,[1,2,3])
print('reduce',total)

#
print((lambda x, y: x + y)(2, 3))

a=lambda x,y:x+y
print(a)
print(a(2,3))