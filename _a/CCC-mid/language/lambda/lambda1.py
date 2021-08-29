def add1(a,b):
    print(a,b)
    return a+b

# anonymous function

# syntax
# lambda argument_list: expression
add2=lambda a,b:a+b
print(add2(100,200))

# syntax sugar: more simple than function

l=[1,2,3,4,5,6]

ll=[(lambda x:x*2)(e) for e in l]
print(ll)


