'''
1   day 0
5   day 1
25  day 2 25+5+1

750

4?
j1,j2,j3
j4
j5
s1,s2,s3
'''

p=1
n=5
day=0
r=750

total=p
import time
while True:
    p=p*n
    day+=1
    total+=p
    # print('day',day,'people',p,'total',total)
    # time.sleep(1)

    if total>=750:
        print(day)
        break

