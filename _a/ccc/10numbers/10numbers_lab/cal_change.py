'''
i:
24

o:
$20: 1
$10: 0
$5:  0
$2:  2
$1:  0
'''
dollars=int(input("Enter an amount of money:"))

twenties=dollars//20
tens=(dollars-twenties*20)//10
fives=(dollars-twenties*20-tens*10)//5
toonies=(dollars-twenties*20-tens*10-fives*5)//2
lonnie=dollars-twenties*20-tens*10-fives*5-toonies*2

print('$20:', twenties)
print('$10:',tens)
print('$5:',fives)
print('$2:',toonies)
print('$1:',lonnie)


