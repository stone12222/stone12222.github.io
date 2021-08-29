'''
5
6 3 3
5 9 7
14 6 2
25 3 1
19 4 5
'''
n = int(input())
friends = []
for i in range(n):
    friends.append(input().split())

shortest = 100000
time = 0

for c in range(1000):
    i = 0
    for p,w,d in friends:
        i += 1
        if c > int(p):
            if c - int(d) > int(p):
               time += abs(int(w)*(c-int(d)-int(p)))
               # print(c,p,abs(int(w)*(c+int(d)-int(p))),time)
        elif c < int(p):
            if c + int(d) < int(p):
                time += abs(int(w)*(c+int(d)-int(p)))
                # print(c,p,abs(int(w)*(c+int(d)-int(p))),time)


        if i == n:
            # print(c,time)
            if shortest > time:
                shortest = time
                short = c
            time = 0
            i == 0

print(shortest,short)

'''
3
1 3 5
2 3 1
9 3 1
'''