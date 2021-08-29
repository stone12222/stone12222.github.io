s='abc'

# query
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())
print(s.islower())
print(s.isnumeric())
print(s.isspace())
print(s.isupper())
print('aabb'.rfind('a'))
print('aabb'.rindex('a'))

# case
print('AbC'.swapcase())
print('abc bcd efg'.title())
print('Abc Bcd Efg'.istitle())
print("Fly In Sky".capitalize())

point = {'a':1,'b':2}
print('{a} {b}'.format_map(point))

# format
print(s.center(10,'.'))
print(s.zfill(10))
print(s.ljust(10,'.'))
print(s.rjust(10,'.'))

# translate
intrans='abcde'
outtrans='12345'
dictionary=str.maketrans(intrans,outtrans)
print('an apple'.translate(dictionary))

# split
print('a,b,c'.partition(','))
print('a,b,c'.rpartition(','))
print('a,b,c'.split(','))
