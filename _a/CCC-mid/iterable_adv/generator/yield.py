# function with one or more yield will return a generator
# the function will execute and return values only when calling next(generator)
def foo_with_yield():
    print('function exec')
    yield 1
    yield 2
    yield 3
    print('this will executed when call generator at 4th times')

x=foo_with_yield()
print(x)
# <generator object foo_with_yield at 0x10f0dd7d8>

# call generator, the function code is executed
print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # throw StopIteration exception
