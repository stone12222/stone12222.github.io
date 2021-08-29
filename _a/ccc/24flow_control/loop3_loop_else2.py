for i in range(10):
    if i==8:
        break
    print(i)
else: #
    print('the loop completely finish')

'''
How to do same thing without using 'else'
'''

def loop():
    for i in range(10):
        if i==8:
            return
        print(i)
    else: #
        print('the loop completely finish')

loop()

