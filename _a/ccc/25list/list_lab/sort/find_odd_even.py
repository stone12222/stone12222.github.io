# generate 100 random numbers between 0-100
# sort and print odd number list
# sort and print even number list

import random
# print(random.randint(0,100))

t=0
el=[]
ol=[]
while t<20:
    n=random.randint(0,100)
    t+=1

    if n%2==0:
        el.append(n)
    else:
        ol.append(n)

el.sort()
ol.sort()
print(el)
print(ol)






