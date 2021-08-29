# generate 200 random numbers between 0-100
# sort and print odd number list
# sort and print even number list

import random

el=[]
ol=[]
for n in range(200):
   n1=random.randint(0,100)
   if n1%2==0:
      el.append(n1)
   else:
      ol.append(n1)

el.sort()
ol.sort()
print(el)
print(ol)

