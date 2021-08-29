"""
given a string
Print each char

i: a string such as
abc

o:
0 a
1 b
2 c
"""




















i='abcd'
print(list(enumerate(i)))

for c in enumerate(i):
    index,ele=c
    print(index,ele)

for index,ele in enumerate(i):
    print(index,ele)




























































