s='alan:5197017988'
name_phone=s.split(':')
print(name_phone)

name=name_phone[0]
phone=name_phone[1]
print(name, phone)

name, phone=s.split(':')
print(name, phone)

#
s='alan     5197017988'
name,phone=s.split()
print(name,phone)

# strip
print('!!hello!!'.strip('!ho'))

# replace
# string is immutable (not changeable)
s='today is bad day'
s=s.replace('bad','good')
print(s)

# format
s='123'
s=s.zfill(100)
print(s)

# query
s='ccc.py'
print(s.endswith('py'))
print(s.startswith('cc'))
print(s.count('c'))
print('100'.isdigit())
print('123.345'.isdigit())

print(s.find('p'))
print(s.find('q'))

# print(s.index('p'))
# print(s.index('q'))

print('Abc'.lower())
print('Abc'.upper())
print(len(s))

# python is minimalist
# remove
s='dog is was lovely'
s=s.replace('was','')
print(s)
