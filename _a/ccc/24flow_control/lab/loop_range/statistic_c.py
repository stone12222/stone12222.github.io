"""
i:
how many numbers you have: 4
number 1: 1
number 2: 2
number 3: 3
number 4: 4

o:
sum is: 10.0
largest:  4.0
smallest:  1.0
average 2.5
range: 3.0

"""
a = int(input('how many numbers you have: '))
sum=0
numOfNodes=0

import math
largest =-math.inf
smallest = math.inf

for i in range(1,a+1):
   num=int(input('number' + str(i)+':'))
   sum+=num
   numOfNodes+=1
   if largest<num:
       largest=num
   if smallest>num:
       smallest=num

print('sum is',sum)
print('largest',largest)
print('smallest',smallest)
print('average', sum / numOfNodes)
print('range',largest-smallest)


