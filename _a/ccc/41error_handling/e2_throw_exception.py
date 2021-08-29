def validateUserName(name):
    if len(name)>8:
        print('the name is good')
    else:
        raise Exception('name must be > 8')

"""
why exception:
explicitly tell caller to handle exception
give caller a second choice to try or clean up
"""

try:
    validateUserName('joe')
    print('hello world')
except Exception:
    print('try again')

