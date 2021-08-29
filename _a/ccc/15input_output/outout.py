print('hello')

a=100
b=200
print(a,b)

#
print('hello',end=' ')
print('world')

#
print(1,2,3,4,sep=' ',end='!')
print()

# format
print(12.3456)
print("%.2f %.3f" % (12.3456,45.6789))
print("%10d" % 100)
print("%10d"%10000)
print("%10d"%1000000)
print("%10s"%"abc")

# zfill
print('9999'.zfill(10))

#
print("joe\t\t 12345\t")
print("Richard\t 9876590\t")

# 9:30
h=9
m=30
print(h,':',m,sep='')

# bad
print('{0:.2f}'.format(12.3456))

# newest
n=12.3456
print(f'{n:.2f}')
print(f'{100:10f}')
print(f'{100:10d}')

#
name='joe'
print(f'Hey {name:>10s}')
print('Hey', name)

