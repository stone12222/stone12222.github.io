'''
4
5
7
R 3
C 1
C 2
R 2
R 2
C 1
R 4
'''
n = int(input())
m = int(input())

canvas = [[1]*m for i in range(n)]

k = int(input())

choices = []
for i in range(k):
    choices.append(input().split())


for i in range(k):
    c = int(choices[i][1]) - 1
    if choices[i][0] == 'R':
        for j in range(m):
            canvas[c][j] = canvas[c][j] * (-1)
    else:
        for j in range(n):
            canvas[j][c] = canvas[j][c] * (-1)

count = 0
for i in range(n):
    count += canvas[i].count(-1)
print(count)