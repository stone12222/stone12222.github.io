# if statement
# input a number check condition-if-else it > 100 or <=100
n=int(input())
if n>100:
    print('n > 100')
else:
    print('n<100 or n=100')

# check number condition-if-else it is odd or even
"""
1. get input
2. condition-if-else the input is even, print 'even'
3. else, print 'odd'
"""
n=int(input())
if n%2==0:
    print('even')
else:
    print('odd')

# eval password
password = input("enter your password: ")
if not password=='123abc':
    print("wrong password")
else:
    pass
