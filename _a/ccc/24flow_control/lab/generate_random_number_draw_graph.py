import random
import matplotlib.pyplot as plt

how_many=input("How many you want: ")
how_many=int(how_many)

l=[]
for i in range(how_many):
    number=random.randint(1,1000)
    l.append(number)

print(l)

plt.plot(list(range(how_many)), l)

# plt.plot([1,2,3],[4,3,10])

plt.show()
