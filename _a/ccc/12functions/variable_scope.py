# global variable
# because this variable outside of all functions

'''
in function, we can read a global var
in function, we can create/read/write a local var
in function, if we want to update a global var, we have to
use 'global var'

'''
v=200

v1=300

v2=200

def fun():
    global v1
    print(v2)

    # local variable
    v=300
    print('in function',v)

    v1=400
    print('in function v1',v1)


# def fun1():
#     print(v)

fun()
print('outside of function',v)
print('outside of function v1',v1)
