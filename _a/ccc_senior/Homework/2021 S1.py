'''
4
6 4 9 7 3
5 2 4 1
'''

n = int(input())
h = input().split()
w = input().split()
area = 0
for i in range(n):
    area += int(w[i])*(int(h[i])+int(h[i+1]))/2

if area % 1 == 0:
    print(int(area))
else:
    print(area)