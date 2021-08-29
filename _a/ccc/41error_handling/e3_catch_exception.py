def validate_user_name(name):
    if len(name)<8:
        raise Exception('The user name should be more than 8 chars')
    print('username is good')

"""
why raise exception:
1. tell caller what's wrong
2. tell caller to handle the error
"""

try:
    validate_user_name('joe123')
    print('everything good')
except Exception:
    print('enter your user name, try again')

"""
why need try
1. prevent program crash because the raised exception
2. give caller a chance continue do something when bad things happen
"""


