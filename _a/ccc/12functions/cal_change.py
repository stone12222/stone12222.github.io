# 75

'''
$20: 3
$10: 1
$5: 1
$2: 0
$1: 0
'''

def printChange(change):
    # //
    twenties=change//20
    change=change-twenties*20

    tens=change//10
    change=change-tens*10

    fives=change//5
    change=change-fives*5

    toonies=change//2
    change=change-toonies*2

    loonies=change

    print('$20:',twenties)
    print('$10:',tens)
    print('$5:',fives)
    print('$2:',toonies)
    print('$1:',loonies)

printChange(75)
