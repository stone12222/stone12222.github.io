# indexing
s='abcdef'
print(s[0])
print(s[-2])

# slicing
t='12:30'
# [startIndex:stopIndex]
hour=t[0:2]
min=t[3:5]
print(hour, min)

hour=t[:2]
min=t[3:]
print(hour, min)

# no error
# print(t[1000])
print(t[-1000:1000])

# step
print('012345678'[0:9:3])
print('012345678'[::3])
print('012345678'[-1:-10:-1])
print('012345678'[::-1])

#
s='abcdefg'
print(s[-1:2:-1]) #gfed
print(s[::-1])

#
print(s.find('cd')) # more friendly
print(s.index('cd')) # not friendly if str cannot be found
print(s.find('hi'))
print(s.index('hi'))

print('will not print')
