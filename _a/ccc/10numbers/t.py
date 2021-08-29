'''
i:
24

o:
$20 1
$10 0
$5  0
$2  2
$1  0

code, result, code, result

works, readable, simple
'''
i=int(input())
twenties=i//20
tens=(i%20)//10
fives=(i%10)//5
twos=(i%5)//2
ones=i-twenties*20-tens*10-fives*5-twos*2

print('$20',twenties)
print('$10',tens)
print('$5',fives)
print('$2',twos)
print('$1',ones)