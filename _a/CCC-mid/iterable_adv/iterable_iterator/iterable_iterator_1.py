# iteration: loop
for i in range(5):
    print(i)

# iterable: collection
# if the object has __iter__(), it is iterable
l=[1,2,3]
print(l.__iter__())
print(iter(l)) # build-in

for n in l: # that's why we can use it in the loop
    print(n)

# iterator
# an object with __next__()
print('###################')
iterator=iter(l)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

iterator=iter(l)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#
i=iter(l) # iterator
while True:
    try:
        e = next(i)
        print(e)
    except StopIteration:
        break

# iterable has iterator(pointer), by iterator, we can get elements from iterable
# 1,2,3
#     ^
