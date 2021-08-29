b=True
b=False
print(type(b))

# ==,!=,>=,<=,>,<, not
print(1==100)
print(1!=100)
print(1<=100)
print(not 1==100)

#
print(50>100 and 60>20)
print(100>50 and 60>20)
'''
truth table
T T => T
T F => F
F T => F
F F => F
'''
print(50>100 or 60>20)
'''
T T => T
T F => T
F T => T
F F => F
'''

# multi comparison
v=50
print(1<v<100)

#
user=input()
password=input()
if user=='kevin' and password=='abc':
    print('login successfully')
else:
    print('try again')

#
username="kevin"
if username:
    print('you entered ',username)
else:
    print('your username should not be empty')

'''
falsey values:
string: ''
number: 0
boolean: False
list: []
tuple: ()
set: set()
dict: {}
None

others are considered as Truthy value

'''
