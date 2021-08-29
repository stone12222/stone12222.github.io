# generate 10 nums
result=[]
for i in range(10):
    result.append(i)
print(result)

# iterator
# object oriented programming OOP
# server programming, OOP
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

d1=Dog('peter',2)
d2=Dog('green',3)
print(d1.name)

# how to implement iterator
class Iterable:
    def __init__(self,n):
        self.n=n
        self.curr=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr<self.n: # lazy
            result=self.curr+1
            self.curr+=1
            return result
        else:
            raise StopIteration()

i=Iterable(3)
it=iter(i)
print(it.__next__())
print(it.__next__())
print(it.__next__())

for i in Iterable(3):
    print(i)

#
def generator(n):
    curr=0
    while curr+1<n:
        yield curr+1 # return
        curr+=1

g=generator(10) # simple way to write iterator

for n in g:
    print(n)








