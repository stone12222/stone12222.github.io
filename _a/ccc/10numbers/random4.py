import random

print(random.random())  # [0,1)

# 10,100
print(random.randint(10,100)) # [10,100]

# 1,2,3,4,5,6,7,8,9,10
# ^   ^   ^   ^   ^
print(random.randrange(1,10,2))
