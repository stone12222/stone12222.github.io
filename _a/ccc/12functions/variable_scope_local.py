# global scope
s=100

def p():
    # global s
    s=200 # shadow global var

    print(list(locals().items()))
    print(s)

p()
print(s)
