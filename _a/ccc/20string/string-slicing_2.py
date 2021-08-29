s= "hello"
# slicing with 3 parameters
# by default the first parameter is 0, the second parameter is total length,
# condition-if-else the third parameter is positive
l=len(s)
print('with 3 parameters')
print(s[0:l:1])
print(s[:l:1])
print(s[::1])


# by default the 1st parameter is the total length-1, the 2nd parameter is
# -1, condition-if-else the 3rd parameter is negative
print(s[l-1:-1:-1])
# 4 3 2 1 0
print(s[::-1])

