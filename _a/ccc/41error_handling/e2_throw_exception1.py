def validateUsername(n):
    if len(n)<8:
        # print('username should >=8')
        raise Exception('username should >=8')
    # else:
    print('saved',n,'to database')

"""
why raise exception instead of if-else:
'raise' exception can force caller to handle it
"""
try:
    validateUsername('joe')
    print('all good')
except Exception:
    print('try enter again')
finally:
    print('always work')
"""
why need try-except:
1. caller have chance to do clearup work or try again
2. prevent program crash from an exception or error
"""
int()
