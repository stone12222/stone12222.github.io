# local scope
s=100

def p():
    global s
    s=200 # shadow global var
    print(s)

p()
print(s)

# reference global before assignment cause an error
# need explicitly define global s
def p1():
    # global s
    s=s+100
p1()

"""
1. function can read global var
2. if function define a var which has same name as
global var, local var will shadow the global var
3. if function want to override the global var,
use 'global varname'
"""
