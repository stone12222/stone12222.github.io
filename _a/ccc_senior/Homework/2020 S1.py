'''
3
0 100
20 50
10 120
'''

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

# speed = []
speed = abs((int(arr[1][1]) - int(arr[0][1]))/(int(arr[1][0]) - int(arr[0][0])))
for i in range(n):
    for j in range(n):
        if j == i:
            break
        curr = abs((int(arr[j][1]) - int(arr[i][1]))/(int(arr[j][0]) - int(arr[i][0])))
        if speed < curr:
            speed = curr
print(speed)