# use normal function to build and return a list
# disadvantage: memory need hold a full list
def get_list_integers1(n):
    curr=0
    integers=[]
    while curr < n:
        integers.append(curr)
        curr += 1
    return integers

print(get_list_integers1(10))

# use iterable pattern which get each integer on demand
# so save memory
# disadvantage: code is complex
class get_list_integers2:
    def __init__(self, n):
        self.n = n
        self.curr=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < self.n:
            r=self.curr
            self.curr=self.curr+1
            return r
        else:
            raise StopIteration()

# the following statement process in detail:
# 1. init class and return an object 'o'
# 2. for loop call o.__iter__ to get an iterator, return 'o'
# 3. for loop call iterator next() method,
# 4.__next__() to get each value
for i in get_list_integers2(10):
    print(i)

# Generators are more simple and powerful tool for creating iterators

# use generator function which return generator,
# not the full list, also the code is simple
def get_list_integers3(n):
    curr = 0
    while curr < n:
        yield curr # use yield, whenever I want to return data
        curr += 1

for i in get_list_integers3(10): # set breakpoint
    print(i)

# Yield is like return

# The yield keyword helps a function to remember its state.
# Each time next() is called on it, the generator resumes
# where it left off (it remembers all the data values and which statement was last executed)

# in other words, yield makes function stateful.

# What makes generators so compact is that the __iter__() and __next__() methods are
# created automatically.
# In addition to automatic method creation and saving program state,
# when generators terminate, they automatically raise StopIteration.
