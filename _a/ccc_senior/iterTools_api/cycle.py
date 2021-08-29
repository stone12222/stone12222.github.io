s = 'abcd'

from itertools import cycle

c = cycle(s)
for e in c:
    print(e)

#
pos = 0
while True:
    print(s[pos])
    pos += 1
    if pos == len(s)-1:
        pos = 0