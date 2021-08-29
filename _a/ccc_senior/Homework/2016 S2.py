a, n = int(input()), int(input())
d, p = sorted([int(i) for i in input().split()]), sorted([int(i) for i in input().split()])


if a == 2:
    p.reverse()

total = 0
for i in range(n):
    total += max(d[i], p[i])

print(total)