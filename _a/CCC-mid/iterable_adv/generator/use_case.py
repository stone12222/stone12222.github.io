def generator():
    curr=0
    while True:
        r=curr
        curr+=1
        yield r

g=generator()
print(g.__next__())



