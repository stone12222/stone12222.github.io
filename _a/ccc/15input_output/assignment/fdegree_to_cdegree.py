"""
Formula: Fdegree=Cdegree * 9/5 +32
         Cdegree=(Fdegree-32)*5/9

1. get a floating number for F degree
2. convert to C degree
3. print C degree with 2 digits after point.

output:
F degree 100.00 equals to C degree 37.78
"""

fdegree=float(input())
cdegree=(fdegree-32)*5/9
