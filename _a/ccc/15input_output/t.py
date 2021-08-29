n=123.456
n2=200

print(n)

# format print
# simple way
print("number is %.2f" % n)
print("number is %.2f and %10d" % (n,n2))
print('number is %010d' % 123)
print('number is %10s' % 123)
print('%+10s|' % 'test')
print('%-10s|' % 'test')

# another way (but not simple)
print('number is {0:.2f}'.format(n))

# new way (format string)
# this is a good
# c,c++,java
print(f'number is {n:.2f} and {n2:10d}')

#
print('%.1f' % n)

#
s='abc'
# zero fill
ss=s.zfill(10)
print(ss)
