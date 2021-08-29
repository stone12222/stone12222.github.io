
"""
Usually, in math, the modulo results always positive number,
but in computer languages, it depends:
For python, The modulo operator always produce a result with the same sign as its second operand
"""

""" 1st way to find modulo
x=quotient*y+r
x/y=quotient+r/y
condition-if-else r has different sign than the second operand, r=y+r

then r is x%y
"""

""" 2nd way to find modulo
the remainder can be understood by string index
# 'abc' string index example:
#  0  1  2
# -3 -2 -1

1. draw the first line by the second operand
   the length of line is the abs of the second operand
   condition-if-else 2nd operand is position, write from 0 to the operand from left to right
   condition-if-else 2nd operand is negative, write the -1 to the operand from right to left
2. draw the second line by the first operand
   condition-if-else the first operand is positive, write from 0 until the operand from left to right, condition-if-else beyond the length, wrap around
   condition-if-else the first operand is negative, write from -1 until the operand from right to left, condition-if-else beyond the length, wrap around
   use the column of the last number to find the modulo in the first row which has the same column

"""

"""
Python make the modulo means same element in the indexing system
for example, -7 in 3 length sequence, always means the 2nd element
because -7%-3=-1 which is 2, and -7%3=2
and 7 always mean the 1st element
7%-3=-2 which is 1 and 7%3=1
"""

# remainder
print('7%3=',7%3) # 1
# 0 1 2
# 0 1 2
# 3 4 5
# 6 7

print('-7%3=',-7%3)
# 0  1   2
# -3 -2 -1
# -6 -5 -4
#       -7

print('7%-3=',7%-3) #-2
# 7=-2*-3+1, -3+1=-2
# -3 -2 -1
# 0  1  2
# 3  4  5
# 6  7

print('-7%-3=',-7%-3) #-1
# -7=2*-3-1
# -3 -2 -1
# -3 -2 -1
# -6 -5 -4
#       -7





# number %3   Result
# 5           2
# 4           1
# 3           0
# 2           2
# 1           1
# 0           0
# -1          2
# -2          1
# -3          0
