"""
input from console, convert to a nested list

i:
4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

o:
[1, 1, 1, 1] [2, 2, 2, 2] [3, 3, 3, 3] [4, 4, 4, 4]
"""









# 1. get all inputs to a list
n=int(input())

l=[]
for _ in range(n):
    inp=input()
    l.append(inp)
print(l)

# 2. convert string to character list
l1=[]
for e in l:
    l1.append(e.split())
print(l1)

"""
[['1', '2'], ['3', '4']]
"""
# 3. convert character list to int list
l2=[]
for e in l1:
    t=[]
    for n in e:
        t.append(int(n))
    l2.append(t)
print(l2)

# 4. print the int list
for e in l2:
    print(e,end=' ')
