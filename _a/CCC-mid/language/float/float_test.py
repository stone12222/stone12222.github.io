print('0.1+0.2=',0.1+0.2)

from decimal import *
print(getcontext())
print(getcontext().prec)
print('0.1+0.2=',Decimal(0.1)+Decimal(0.2))
# more accurate
getcontext().prec=56
print('0.1+0.2=',Decimal(0.1)+Decimal(0.2))

"""
why?

# To do number calculation,
1st thing is how to represent numbers

# in fraction form:
1/10, 1/2, 1/3

# in Decimal system
1/10 is represented as 0.1
1/2=5/10 is represented as 0.5

1/3~=3333/10000~=0.3333
So decimal system that cannot accurately represent 1/3

A finite fraction where the denominator can be
transformed to the power of 10 can be represented accurately

# for Binary (base 2)
Computers use a binary system to represent number
1/2 = 0.5 = 1*2^-1 = 0.1 (in binary)
1/10 = 0.1 = 1/10~=1*2^-4+1*2^-5+1*2^-6~=0.00011(1) (in binary)

A finite fraction where the denominator can be transformed to
the power of 2 can be represented accurately
"""

"""
How to get the best approximate result?
Python has an arbitrary-precision decimal type named Decimal
	Decimal('0.1')+Decimal('0.2') = 0.3

How to Round?
	"%.2f" for 1.2399, returns "1.24"
"""

"""
resource:
http://floating-point-gui.de/
"""
