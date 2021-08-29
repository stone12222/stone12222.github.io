# a circle area A == PI*r**2
# condition-if-else r==1
# A == PI
# A/4 == PI/4
# a quarter area A/4==QA==PI/4 => PI==QA*4

# how to get a quarter area QA?
# Generate random x and y between 0 and 1 for N times
# count how many times T, x**2+y**2<=1
# QA==T/N
# PI==QA*4==T/N*4


import random

def one_time_approximate_pi(N):
    T=0
    x=0
    y=0
    for j in range(N):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            T+=1
    Pi=T/N*4
    return Pi

def approximate_pi(N):
    total_pi=0
    for i in range(10):
        pi=one_time_approximate_pi(N)
        print(pi)
        total_pi+=pi


    mean=total_pi/10
    return mean

# input N one by one, 10, 100, 1000, 10000, 100000, 1000000
for i in range(6):
    N=int(input())
    pi=approximate_pi(N)
    print(pi)

"""
100
3.1480000000000006
1000
3.1376
10000
3.14088
100000
3.141764
1000000
3.1415232
10000000
3.14149856
"""




