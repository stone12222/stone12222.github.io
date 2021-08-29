"""
i:
a c d z f
d w s

o:
yes

or
no
"""

# get input

a=input()
b=input()
# convert input to 2 lists
list_a = []
list_b = []
for ch in a:
    list_a.append(ch)
for item in b:
    list_b.append(item)
print(list_a)
print(list_b)

#
sign=False
for i in list_b:
    for j in list_a:
        if i == j:
            sign=True
            break
print('yes' if sign else 'no')

#

