# input, output (IO)
h=4
m=5
# 04:05
print(0,h,':',0,m)
print('0'+str(h)+':'+'0'+str(m))
print(0,h,':',0,m,sep='禹琛')

# leading zero
print(str(h).zfill(2),end='')
print(':',end='')
print(str(m).zfill(2))

#
n=123.456
# 123.46
print('the number is %.2f')
print('the number is %.2f' % n)
print('the number is {0:.2f}'.format(n))
print(f'the number is {n:.2f}')
print(f'the number is {n:10}')
print(f'the number is {n:010}')



