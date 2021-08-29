a=100
b=200

try:
    print(eval(input()))
except ZeroDivisionError:
    print('can not divide by 0')
except SyntaxError:
    print('syntax error')
except NameError:
    print('variable is not defined')
