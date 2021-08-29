s='abcde'

"""
o: all possible sequences
0 1 a
0 2 ab
0 3 abc
0 4 abcd
0 5 abcde
----------
1 2 b
1 3 bc
1 4 bcd
1 5 bcde
---------
2 3 c
2 4 cd
2 5 cde
---------
3 4 d
3 5 de
---------
4 5 e
"""

import time
startTime=time.time()

s='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
l=len(s)
for a in range(l):
    for b in range(1,l+1):
        if b>a:
            print(a,b,end=' ')
            print(s[a:b])

endTime=time.time()
print('we spent: ',endTime-startTime)
