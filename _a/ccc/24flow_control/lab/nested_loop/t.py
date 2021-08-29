s='abcde'

"""
o: all possible sequences
0 1 a
0 2 ab
0 3 abc
0 4 abcd
0 5 abcde

1 2 b
1 3 bc
1 4 bcd
1 5 bcde
2 3 c
2 4 cd
2 5 cde
3 4 d
3 5 de
4 5 e
"""

# for i in range(4):
#     for j in range(4):
#         print(i,j,s[i:j])

# for sindex,c in enumerate(s):
#     for eindex in range(sindex,len(s)+1):
#         print(sindex,eindex,s[sindex:eindex])

s = 'abcde'
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(i,j,s[i:j])

