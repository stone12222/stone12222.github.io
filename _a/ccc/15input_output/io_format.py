value=123.456

# 123.46
print('formated number: %.2f' % value)
print(f'formated number: {value:.2f}')

# leading zeros
# 000123.456????
print('%010g' % value)
print(f'{value:010g}')

# %010d
# % starting a format string
# 0 add leading zeros
# 10 take 10 spaces
# d format as a integer
print('%010d' % 1234)
print('%10d' % 1234)
print('%10d - %10d' % (1234,12345))
print(f'{1234567:10d}')

#
name='joe'
age=20

print(f'{name:20s} with age {age}')
