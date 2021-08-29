"""

i: input 5 numbers, such as
23 22 30 11 25

o:
ascending, descending, or "not in order"
"""

l1=int(input())
l2=int(input())
l3=int(input())
l4=int(input())
l5=int(input())

if l1<l2<l3<l4<l5:
    print("ascending")
elif l1>l2>l3>l4>l5:
    print("descending")
else:
    print("Not in order")
