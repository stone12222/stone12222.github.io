"""
i: Rows Cols such as
2
3

o:
1 2 3
4 5 6

transitions:
input->?->?->...->ouput
ouput->?->?->...->input

3 -> 1 2 3
"""
r=int(input())
c=int(input())
v=1
for col in range(c):
    print(v, end=' ')
    v=v+1

print()




