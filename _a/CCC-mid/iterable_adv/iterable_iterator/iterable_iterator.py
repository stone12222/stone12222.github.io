s='abc'

"""
iterable has __iter__() method or __getitem__() method
return an iterator
"""
i=s.__iter__()
print(s)
# or
i=iter(s)
print(i)

"""
iterator object has __next__() in python 3
"""
print(i.__next__())
# or
print(next(i))

# raise StopIteration exception
try:
    print(i.__next__())
except StopIteration:
    print('no next element')

