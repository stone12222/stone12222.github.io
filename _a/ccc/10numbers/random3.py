import random
# [0,1)
n=random.random()

# [0,1)->[0,10)
# [0,1)->[1,10)
n=int(random.random()*9+1)
print(n)

# [1,10]
print(random.randint(1,10))

#
for i in range(1000000):
    print(random.randint(1,100000))

