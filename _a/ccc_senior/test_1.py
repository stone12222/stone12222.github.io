'''
ACTGAGCAAAB
'''
# import sys
#
# input = sys.stdin.readline
import math

k= int(input())
lists=[9,2,9]
j=1
i=1
maps=[3]

if k == 1:
    print(1)
    print(9)
elif k==2 or k==3:
    print(2)
    print("9 2")
else:
    for i in range(int(math.pow(10,5))):
        num=0
        if j>i:
            i+=1
        else:
            j+=1
        ii=i
        jj=j
        for e in range(i+j,0,-1):
            num+=math.factorial(i+j)/(math.factorial(i+j-e)*math.factorial(ii)*math.factorial(jj))
        if num>=k:
            print(i+j)
            for e in range(1, i+1):
                print(9, end=" ")
            for e in range(1, j):
                print(2, end=" ")
            print(2)
            break
    else:
        print("Sad Chris")








