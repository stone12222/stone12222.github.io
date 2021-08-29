# input/output

#
print(12.3333)
# any string with %
# f: float
print('%.2f' % 12.3356)

#
print('%10d' % 100)
print('%10d' % 100000)
print('%10d' % 100000000)
# leading zero
# tradition way
print('number takes 10 spaces: %010d' % 9999)
# new way
print('{1:_>10d} {0:10d}'.format(9999, 88))
print('{0:_<10d}'.format(9999))

# leading 0
print('9999'.zfill(10))

