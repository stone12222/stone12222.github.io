# normal function
def gen_ints(n):
    l=[]
    for i in range(n):
        l.append(i)
    return l

print(gen_ints(5))

# iterator class
class Gen_ints_by_iter:
    def __init__(self,n):
        self.n=n
        self.curr=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr<self.n:
            r=self.curr
            self.curr+=1
            return r
        else:
            raise StopIteration()
g=Gen_ints_by_iter(10)
for e in g:
    print(e)

# generator function
# python will translate generator to iterator class
def gen_ints_by_generator(n):
    curr=0
    while curr<n:
        yield curr
        curr+=1

g=gen_ints_by_generator(10)
for e in g:
    print(e)

"""
1. efficient in memory
2. easy implemention compared with Iterator class
3. when produce infinite things
"""

#
# from itertools import count
# for n in count(100):
#     print(n)




