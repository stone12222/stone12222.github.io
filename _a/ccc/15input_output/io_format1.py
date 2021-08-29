# https://pyformat.info/#string_pad_align
n=1.567
print(round(n,2))
print('I convert 1,567 to %.2f' % n)

print('%3d %.3f' % (12.34, 3.45))

# leading zeros
print('%10d' % 123)
print('%010d' % 123)

h=2
m=3
# 02:03

print('%02d:%02d' % (h,m))
print('{0:02d}:{1:02d}'.format(h,m))
print(str(h).zfill(2)+':'+str(m).zfill(2))

#
"""
       joe       nick
1111111111 2222222222
"""
n1='joe'
n2='nick'
p1=1111111111
p2=2222222222
print('%10s %10s' % (n1,n2))
# print('{0:_>10} {1:_>10}'.format(n1,n2))
print('%10d %10d' % (p1,p2))



