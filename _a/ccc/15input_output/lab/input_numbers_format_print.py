# accept input for 2 float numbers
# print with 2 rounded decimal
"""
i:
100.123
45.666

o:
100.12 45.67
"""
f1=float(input())
f2=float(input())

print('%.2f' % round(f1,2))
print('%.2f' % round(f2,2))
