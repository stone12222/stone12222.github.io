s='abc'
s1=s+'def'
print(s1)

# special
print('hello\nworld')
print('hello\tworld')
# for i in range(100000):
#     for j in range(1000000):
#         pass
#     print('\a')

# long str
s='text text text text text \
  text text text text text text\
  text text text text text text\
  text text text text text text\
  text text text text text text\
  text'
print(s)

# preformat string
#   *
# *   *
#   *
print('\t*')
print('*\t\t*')
print('\t*')

print('  *')
print('*   *')
print('  *')

# preserve predefined format
s="""
    *
  *   *
    *
"""
print('  *'
      '*   *'
      '  *')
print(s)

# escape character
# s='we're coders'
s="we're coders"
s='we\'re coders'

# raw string
s='c:\number\name'
s='c:\\number\\name'
s='c:\\num\\root\\tony'
s=r'c:\num\root\tony'

# why not use str
str='abc'
print(str)

# query
b='ab' in 'abc'
print(b)

#
s='*'
print(s*30)

