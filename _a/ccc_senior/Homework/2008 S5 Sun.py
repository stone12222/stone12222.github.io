"""
i:
6
0 2 0 2
1 3 1 3
1 5 0 3
3 3 3 3
8 8 6 7
8 8 8 8

o:
Roland
Patrick
Roland
Roland
Roland
Patrick
"""
def canPlay(a,b,c,d,pattern):
   return a>=pattern.count('A') and \
       b>=pattern.count('B') and \
       c>=pattern.count('C') and \
       d>=pattern.count('D')

players=['Patrick','Roland']

results={}
def canWin(a,b,c,d,rounds):
   # print('   '*rounds,players[rounds%2],'play','A'*a+'B'*b+'C'*c+'D'*d)
   if (a,b,c,d) in results:
       return results[(a,b,c,d)]

   # print('   '*rounds,players[rounds%2],'try','AABDD')
   if canPlay(a,b,c,d,"AABDD") and not canWin(a-2,b-1,c,d-2,rounds+1):
       results[(a,b,c,d)]=True
       return True

   # print('   ' * rounds, players[rounds % 2], 'try', 'ABCD')
   if canPlay(a,b,c,d,"ABCD") and not canWin(a-1,b-1,c-1,d-1,rounds+1):
       results[(a,b,c,d)]=True
       return True

   # print('   ' * rounds, players[rounds % 2], 'try', 'CCD')
   if canPlay(a,b,c,d,"CCD") and not canWin(a,b,c-2,d-1,rounds+1):
       results[(a,b,c,d)]=True
       return True

   # print('   ' * rounds, players[rounds % 2], 'try', 'BBB')
   if canPlay(a,b,c,d,"BBB") and not canWin(a,b-3,c,d,rounds+1):
       results[(a,b,c,d)]=True
       return True

   # print('   ' * rounds, players[rounds % 2], 'try', 'AD')
   if canPlay(a,b,c,d,"AD") and not canWin(a-1,b,c,d-1,rounds+1):
       results[(a,b,c,d)]=True
       return True

   # print('   ' * rounds, players[rounds % 2], 'Lose')
   results[(a, b, c, d)] = False
   return False

n=int(input())
for i in range(n):
   a,b,c,d=[int(e) for e in input().split()]
   if canWin(a,b,c,d,0):
       print('Patrick')
   else:
       print('Roland')


