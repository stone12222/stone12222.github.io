"""
use while and use for
i:
10

o:
*
**
***
****
*****
******
*******
********
*********
**********

1. get a number N
2. generate number I from 1 to N
3. each round to print I stars
"""
n=int(input())
for i in range(1,n+1):
    print('*'*i)
