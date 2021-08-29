# global variable
# are the one that are defined and declared outside a function

# the order doesn't matter
def p():
    print(s)

s=100

p()

l=list(globals().items())
for e in l:
    print(e)



