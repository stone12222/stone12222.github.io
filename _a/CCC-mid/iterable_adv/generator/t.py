# generator expression
s=(e for e in range(5))
print(s)

for e in s:
    print(e)

# generator expression vs comprehension
# generator expression only generates element when needed (lazy, less memory)
# comprehension generate all element already before needed (delligent, fast speed)

# normal function
# use global variable
num=0
def getNum():
    global num
    num+=1
    return num

# use memory
def getNum():
    l=[]
    for e in range(100):
        l.append(e)
    return l

# print(getNum())
# print(getNum())
# print(getNum())
# print(getNum())
# print(getNum())

# generator function
# not use global var and memory
def getNum():
    n=0
    while True:
        r=n
        n+=1
        yield r # return n

g=getNum()
print(g) # iterator
print(g.__next__())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
