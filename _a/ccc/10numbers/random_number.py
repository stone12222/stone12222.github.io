import random

print(random.random()) # Random 0.0<=x<1.0
random.randrange(11) # 0<=x<11
number=random.randint(1,10) # a<=x<=b

# else usage
# choice
print(random.choice('abcdefghijklmnopqrst'))

#shuffle
pokers=[1,2,3,4,5,'J','Q','K','A']
random.shuffle(pokers)
print(pokers)

#sample
print(random.sample(pokers, 3))
