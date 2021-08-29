b=True
b=False

# boolean
print(type(b))

n=100
print(type(n))

# comparison operator
print(100>50)
print(100>=50)
print(100<50)
print(100<=50)
print(100==50)
print(100!=50)
print(not 100==50)
print(0<100<200)

# relational operator
print(100>50 and 50>30)
print(100>50 or 50<30)
print(100>50 and 50<30)
print(True or False) # True

# truthy table
'''
and table
T T => T
T F => F
F T => F
F F => F 

or table
T T => T
T F => T
F T => T
F F => F
'''

# short-circuit
print(100<50 and 1000/0)
print(100>50 or 1000/0)

# 'abc'
s='abc'