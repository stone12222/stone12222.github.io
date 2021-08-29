"""
i: a number, such as 6

o:
1 every time
2 every time, every 2 time
3 every time, every 3 time
4 every time, every 2 time
5 every time
6 every time, every 2 time, every 3 time

"""
for i in range(1,7):
    print(i,'every time',end='')
    if i%2==0:
        print(', every 2 time',end='')
    if i%3==0:
        print(', every 3 time',end='')
    print()
