"""
make software reusable
"""
import mymodule

n=mymodule.add(100,200)
print(n)

"""
simple function
"""
def func():
    pass
print(func())

"""
default parameter value
"""
def multiple(a=100,b=200):
    print('a',a,'b',b)
    print(a*b)
multiple()
multiple(4,6)

"""
named arguments
"""
multiple(b=10,a=20)

"""
variable number of parameters
"""
print("########## ")
def multiple(a,b,*others):
    print(others)
    print(type(others))
    m=a*b
    for o in others:
        m=m*o
    return m

print(multiple(1,2,3,4,5))

"""
None
"""
def pr(a=None,b=None):
    if (a is None) and (b is None):
        print(0)
    elif (a is None):
        print(b)
    elif (b is None):
        print(a)
    else:
        print(a+b)

pr()
pr(1,2)
pr(1)
pr(b=2)

# keyworded variable length of arguments
def add(a, **other_numbers):
    print(other_numbers)

add(100,one=1,two=2,three=3)
