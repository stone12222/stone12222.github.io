try:
    f=open('noexistfile')
except: # will catch any error
    print('Error 001: FileNotFound')
else: # run if no exception happens
    r = f.readlines()
    for line in r:
        print(line)
finally:
    print('this line will be printed anyway')