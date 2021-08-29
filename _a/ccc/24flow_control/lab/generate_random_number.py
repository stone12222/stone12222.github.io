import random
# 1. let user input how many random numbers
# users want to generate
# 2. generate and print those numbers

# 2 times
# while
# for















how_many=input("How many you want: ")
how_many=int(how_many)

while how_many>0:
    number=random.randint(1,1000)
    print(number)
    how_many=how_many-1

for i in range(how_many):
    print(i)
