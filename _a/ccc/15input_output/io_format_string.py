"""
padding and aligning
"""
print('%10s|' % 'test')
print('%-10s|' % 'test')
print('{:10}|'.format('test'))

# new way can choose padding character
print('{:_<10}'.format('test'))
print('{:_>10}'.format('test'))
print('{:_^10}'.format('test'))

# format string
str1="one"
str2="two"
print("{0:>10} {1:>10}".format(str1, str2))
print("{0:0>10} {1:0>10}".format(str1, str2))

"""
truncating long strings
"""
print('%.5s' % ('abcdefg'))
print('{:.5}'.format('abcdefg'))
