# why can be used in for loop
# an object with __iter__() is iterable
for i in range(10):
    print(i)

# iterable has __next__() which returns an element
o=range(10).__iter__() # o is an iterator
# an object with __next__() is iterator
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()

# iteration == loop, repeatedly do something

'''
iterator = iterable.__iter__()
element=iterator.__next__()
'''

# what is iterable
print('abc'.__iter__())
print(iter('abc'))
print('abc'.__iter__().__next__())
print(next(iter('abc')))
print([1,2,3].__iter__().__next__())
print(next(iter([1,2,3])))
# all collection should be iterable

# if not use for
s='abc'
i=iter(s)
while True:
    try:
        e = next(i)
        if e:
            print(e)
    except StopIteration:
        break
