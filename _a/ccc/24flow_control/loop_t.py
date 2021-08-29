'''
i:
3 5

o:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
a,b=input().split()
a=int(a)
b=int(b)

# nested loop
for j in range(a):
    for i in range(1,b+1):
        print(i,end=' ')
    print()

