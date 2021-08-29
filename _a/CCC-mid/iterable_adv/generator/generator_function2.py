# generate 10 ints
l=[]
for i in range(10):
    l.append(i)
print(l)

ll=[e for e in range(10)]

# iterator
class IterImpl:
    def __init__(self,number): # constructor
        self.currNum=0
        self.maxNum=number
    def __iter__(self):
        return self
    def __next__(self):
        r=self.currNum
        if self.currNum<self.maxNum:
            self.currNum+=1
            return r
        else:
            raise StopIteration()

iterImpl=IterImpl(3)
print(iterImpl.currNum)
print(iterImpl.maxNum)

iterator=iterImpl.__iter__()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# generator function is a function which
# has one or more 'yield'
def generator(n):
    curr=0
    while curr<n:
        r=curr
        curr+=1
        # return r
        yield r
        print('abc')
        print('zzz')
    # raise StopIteration()
    # return 100

g=generator(3)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

# why?
"""
1. memory efficient
2. simple impl compared with Iterator class
3. necessary when we generate infinite things
4. piping
"""
