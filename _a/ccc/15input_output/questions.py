"""

"""

"""
1. Write a program that accepts the radius of a circle from the user and compute the area.
(notes, how to get pi value from python? we need import math module like this 'from math import pi')
Sample Input:
1.1

Sample Output:
Area = 3.8013271108436504

2. Write a program that accepts an integer ‘n’ and computes the value of n+nn+nnn. 5+55+555
Sample input：
5

Sample output：
615

3. Write a program to accept an integer 'n',
and get the difference between n and 66 (The difference is the absolute difference)
Sample input:
10

Sample ouput:
56

Sample input:
100

Sample output:
34
"""

'''
get input
convert input to a number
calculate area based on the number and save to 'area'
print area
'''

n=float(input())
import math
area=math.pi*n**2
print("Area = %.2f" % area)
