#
import random
r=random.random() # [0,1)
print(r)

print(random.randint(0,10)) # [0,10]
print(random.choice(['kevin','richard','harpuneet']))

#
pokers=[2,3,4,5,6,7,'J','K','Q']
random.shuffle(pokers)
print(pokers)
