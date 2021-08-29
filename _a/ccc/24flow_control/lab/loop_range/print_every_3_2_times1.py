"""
i:
6

o:
every time
every time, every 2 time
every time, every 3 time
every time, every 2 time
every time
every time, every 2 time, every 3 time
"""
n=int(input())

for i in range(1,n+1):
    print('every time',end='')
    if i%2==0:
        print(', every 2 time',end='')
    if i%3==0:
        print(', every 3 time',end='')
    print()





