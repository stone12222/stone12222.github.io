"""
i:
26

o:
$20: 1
$10: 0
$5:  1
$2:  0
$1:  1
"""
money=int(input())

twenties=money//20
tens=(money-twenties*20)//10
fives=(money-twenties*20-tens*10)//5
toonies=(money-twenties*20-tens*10-fives*5)//2
lonnie=(money-twenties*20-tens*10-fives*5-toonies*2)

print('$20:', twenties)
print('$10:',tens)
print('$5:',fives)
print('$2:',toonies)
print('$1:',lonnie)
