n=100
print('$',n,sep='')

print('turn int to float: %.3f' % n)

print('turn int to float: {:.3f}'.format(n))

f=34.565
print('%.2f' % round(f,2))

#
print('%f' % f)
print('%.0f' % f)

# 11 -> 000011, 1111-> 001111
n=111
print(str(n).zfill(6))
print('%06d' % n)

# print multiple values
print('{1:.2f} {0:.2f}'.format(11.11, 22.22))
print('%.2f %.2f' % (11.11, 22.22))

# align
print('{:_^10}'.format(11))
